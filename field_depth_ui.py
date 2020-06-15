# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\field_depth.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(982, 849)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 20, 481, 461))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(520, 20, 311, 461))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.verticalLayoutWidget_2)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 139))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 139))
        self.groupBox.setObjectName("groupBox")
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(10, 20, 251, 31))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.output_field_depth = QtWidgets.QCheckBox(self.gridLayoutWidget_4)
        self.output_field_depth.setChecked(True)
        self.output_field_depth.setObjectName("output_field_depth")
        self.gridLayout_4.addWidget(self.output_field_depth, 0, 1, 1, 1)
        self.output_params = QtWidgets.QCheckBox(self.gridLayoutWidget_4)
        self.output_params.setChecked(True)
        self.output_params.setObjectName("output_params")
        self.gridLayout_4.addWidget(self.output_params, 0, 3, 1, 1)
        self.output_image_distance = QtWidgets.QCheckBox(self.gridLayoutWidget_4)
        self.output_image_distance.setObjectName("output_image_distance")
        self.gridLayout_4.addWidget(self.output_image_distance, 0, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 0, 0, 1, 1)
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(10, 50, 251, 31))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.input_focus_length = QtWidgets.QCheckBox(self.gridLayoutWidget_5)
        self.input_focus_length.setObjectName("input_focus_length")
        self.gridLayout_5.addWidget(self.input_focus_length, 0, 1, 1, 1)
        self.input_distance = QtWidgets.QCheckBox(self.gridLayoutWidget_5)
        self.input_distance.setChecked(True)
        self.input_distance.setObjectName("input_distance")
        self.gridLayout_5.addWidget(self.input_distance, 0, 3, 1, 1)
        self.input_apeture = QtWidgets.QCheckBox(self.gridLayoutWidget_5)
        self.input_apeture.setObjectName("input_apeture")
        self.gridLayout_5.addWidget(self.input_apeture, 0, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.label_6.setObjectName("label_6")
        self.gridLayout_5.addWidget(self.label_6, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBox_4 = QtWidgets.QGroupBox(self.verticalLayoutWidget_2)
        self.groupBox_4.setObjectName("groupBox_4")
        self.formLayoutWidget = QtWidgets.QWidget(self.groupBox_4)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 20, 198, 100))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.basic_setting = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.basic_setting.setContentsMargins(0, 0, 0, 0)
        self.basic_setting.setObjectName("basic_setting")
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.basic_setting.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.basic_setting.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.aperture = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.aperture.setSingleStep(0.1)
        self.aperture.setProperty("value", 1.4)
        self.aperture.setObjectName("aperture")
        self.basic_setting.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.aperture)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.basic_setting.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.focus_distance = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.focus_distance.setBaseSize(QtCore.QSize(2, 2))
        self.focus_distance.setProperty("value", 2.0)
        self.focus_distance.setObjectName("focus_distance")
        self.basic_setting.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.focus_distance)
        self.focus_length = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.focus_length.setMaximum(200.0)
        self.focus_length.setProperty("value", 50.0)
        self.focus_length.setObjectName("focus_length")
        self.basic_setting.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.focus_length)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.basic_setting.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.sensor_size_list = QtWidgets.QComboBox(self.formLayoutWidget)
        self.sensor_size_list.setObjectName("sensor_size_list")
        self.basic_setting.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.sensor_size_list)
        self.verticalLayout_2.addWidget(self.groupBox_4)
        self.groupBox_2 = QtWidgets.QGroupBox(self.verticalLayoutWidget_2)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_2)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(20, 60, 261, 41))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.confusion_circle_diam = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_2)
        self.confusion_circle_diam.setDecimals(3)
        self.confusion_circle_diam.setMaximum(1.0)
        self.confusion_circle_diam.setSingleStep(0.005)
        self.confusion_circle_diam.setProperty("value", 0.04)
        self.confusion_circle_diam.setObjectName("confusion_circle_diam")
        self.gridLayout_2.addWidget(self.confusion_circle_diam, 0, 2, 1, 1)
        self.confusion_circle_diam_slide = QtWidgets.QSlider(self.gridLayoutWidget_2)
        self.confusion_circle_diam_slide.setProperty("value", 50)
        self.confusion_circle_diam_slide.setOrientation(QtCore.Qt.Horizontal)
        self.confusion_circle_diam_slide.setObjectName("confusion_circle_diam_slide")
        self.gridLayout_2.addWidget(self.confusion_circle_diam_slide, 0, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 1)
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_2)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(20, 30, 201, 31))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.sensor_size = QtWidgets.QDoubleSpinBox(self.formLayoutWidget_2)
        self.sensor_size.setMaximum(100.0)
        self.sensor_size.setSingleStep(0.005)
        self.sensor_size.setProperty("value", 43.27)
        self.sensor_size.setObjectName("sensor_size")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.sensor_size)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 982, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "景深计算器"))
        self.groupBox.setTitle(_translate("MainWindow", "变量设置"))
        self.output_field_depth.setText(_translate("MainWindow", "景深"))
        self.output_params.setText(_translate("MainWindow", "参数"))
        self.output_image_distance.setText(_translate("MainWindow", "像距"))
        self.label_5.setText(_translate("MainWindow", "图像输出"))
        self.input_focus_length.setText(_translate("MainWindow", "焦距"))
        self.input_distance.setText(_translate("MainWindow", "物距"))
        self.input_apeture.setText(_translate("MainWindow", "光圈"))
        self.label_6.setText(_translate("MainWindow", "变量"))
        self.groupBox_4.setTitle(_translate("MainWindow", "基础设置"))
        self.label_4.setText(_translate("MainWindow", "焦距(mm)"))
        self.label.setText(_translate("MainWindow", "光圈(F)"))
        self.label_2.setText(_translate("MainWindow", "物体距离(m)"))
        self.label_8.setText(_translate("MainWindow", "sensor尺寸(英寸)"))
        self.groupBox_2.setTitle(_translate("MainWindow", "高级设置"))
        self.label_7.setText(_translate("MainWindow", "弥散圈直径(mm)"))
        self.label_3.setText(_translate("MainWindow", "sensor尺寸(mm)"))
        self.pushButton.setText(_translate("MainWindow", "确认"))
