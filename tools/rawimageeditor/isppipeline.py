import tools.rawimageeditor.isp as isp
from tools.rawimageeditor.rawImage import RawImageInfo, RawImageParams


class IspPipeline():
    def __init__(self):
        self.old_pipeline = [0]
        self.pipeline = [0]
        self.calc_data = []
        # self.data = RawImageInfo()
        self.params = RawImageParams()
        # img_list存储了pipeline中途所有的图像
        self.img_list = []
        self.img_list.append(RawImageInfo())
        self.need_flush = False

    def set_pipeline(self, pipeline):
        self.old_pipeline = self.pipeline
        self.pipeline = pipeline

    def pipeline_clear(self):
        self.old_pipeline = self.pipeline
        self.pipeline = [0]

    def add_pipeline_node(self, node):
        """
        function: 为pipeline添加一个节点
        输入是pipeline_dict的字符串
        """
        if(node in isp.pipeline_dict):
            self.pipeline.append(isp.pipeline_dict[node])

    def get_pipeline_node_index(self, node):
        """
        返回该node在pipeline的index
        """
        if(node in isp.pipeline_dict and isp.pipeline_dict[node] in self.pipeline):
            return self.pipeline.index(isp.pipeline_dict[node])+1

    def compare_pipeline(self):
        """
        function: 对比新老pipeline的区别
        如果不同的话，会返回一个index，表示从第index个值开始不一样的,注意这个index可能不存在于老的pipeline中
        如果相同的话，会返回0
        """
        for i, node in enumerate(self.pipeline):
            if(i > len(self.old_pipeline) - 1 or node != self.old_pipeline[i]):
                return i
        return 0

    def check_pipeline(self):
        """
        检查pipeline，如果有不同的，修改img_list
        ret: 如果pipeline不需要修改，就返回None，如果需要修改，就返回需要修改的pipeline
        """
        if(self.need_flush == False):
            index = self.compare_pipeline()
            if(index != 0):
                self.remove_img_node_tail(index)
                return self.pipeline[index:]
            return None
        else:
            self.remove_img_node_tail(1)
            self.need_flush = False
            return self.pipeline

    def run_pipeline(self, process_bar=None):
        """
        运行pipeline，process_bar是用于显示进度的process bar
        """
        pipeline = self.check_pipeline()
        if (process_bar is not None):
            process_bar.setValue(0)

        if (pipeline is not None):
            length = len(pipeline)
            i = 1
            for node, data in zip(pipeline, self.img_list):
                self.img_list.append(isp.run_node(node, data, self.params))
                if (process_bar is not None):
                    process_bar.setValue(i / length * 100)
                    i += 1
        else:
            if (process_bar is not None):
                process_bar.setValue(100)


    def get_pipeline(self):
        return self.pipeline

    def update_pipeline(self, pipeline):
        self.pipeline = pipeline

    def add_img_nodes(self, num):
        for i in range(num):
            self.img_list.append(RawImageInfo())

    def add_img_node(self, img):
        self.img_list.append(img)

    def remove_img_node_tail(self, index):
        """
        function: 去除>=index之后的node
        """
        while index < len(self.img_list):
            self.img_list.pop()

    def get_image(self, index):
        """
        获取pipeline中的一幅图像
        """
        if (index < len(self.img_list)):
            return self.img_list[index]
        else:
            return None

    def flush_pipeline(self):
        """
        刷新pipeline的参数，防止设置参数没有生效
        """
        self.need_flush = True
