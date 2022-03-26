# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'first.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
# import sys
import cv2

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

class Ui_MainWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Ui_MainWindow, self).__init__(parent)

        # self.face_recong = face.Recognition()
        self.timer_miceCamera = QtCore.QTimer()
        self.cap = cv2.VideoCapture()
        self.CAM_NUM = 0 # 启动本地摄像头顺序
        self.setupUi(self) # 设置UI界面
        self.slot_init()
        self.__flag_work = 0
        self.x = 0
        self.count = 0
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1127, 851)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 380, 400, 400))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 40, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.open_miceCamera = QtWidgets.QPushButton(self.frame) # 打开大鼠摄像头
        self.open_miceCamera.setGeometry(QtCore.QRect(10, 40, 93, 28))
        self.open_miceCamera.setObjectName("open_miceCamera")
        self.label_miceCamera = QtWidgets.QLabel(self.frame) # 大鼠摄像头标签
        self.label_miceCamera.setGeometry(QtCore.QRect(10, 80, 400, 400)) # 左上宽高
        self.label_miceCamera.setObjectName("label_miceCamera")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(430, 380, 400, 400))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_4.setGeometry(QtCore.QRect(110, 40, 93, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 121, 16))
        self.label_3.setObjectName("label_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 40, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(410, 380, 21, 411))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 370, 1091, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(830, 380, 21, 411))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(850, 380, 231, 401))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_5.setGeometry(QtCore.QRect(70, 40, 61, 28))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 91, 16))
        self.label_4.setObjectName("label_4")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_6.setGeometry(QtCore.QRect(10, 40, 61, 28))
        self.pushButton_6.setObjectName("pushButton_6")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(10, 10, 611, 361))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_7.setGeometry(QtCore.QRect(110, 40, 93, 28))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_8.setGeometry(QtCore.QRect(10, 40, 93, 28))
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 91, 16))
        self.label_2.setObjectName("label_2")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(620, 10, 21, 361))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setGeometry(QtCore.QRect(640, 10, 441, 361))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_5 = QtWidgets.QLabel(self.frame_5)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 121, 16))
        self.label_5.setObjectName("label_5")
        self.pushButton_10 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_10.setGeometry(QtCore.QRect(10, 40, 93, 28))
        self.pushButton_10.setObjectName("pushButton_10")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1127, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        MainWindow.insertToolBarBreak(self.toolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionfffff = QtWidgets.QAction(MainWindow)
        self.actionfffff.setObjectName("actionfffff")
        self.actionrrr = QtWidgets.QAction(MainWindow)
        self.actionrrr.setObjectName("actionrrr")
        self.menu.addSeparator()
        self.menu.addAction(self.actionfffff)
        self.menu.addAction(self.actionrrr)
        self.menubar.addAction(self.menu.menuAction())
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionfffff)
        self.toolBar.addAction(self.actionrrr)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.open_miceCamera.clicked.connect(self.button_open_mice_camera_click)
        self.timer_miceCamera.timeout.connect(self.show_camera)

    def slot_init(self):
        self.open_miceCamera.clicked.connect(self.button_open_mice_camera_click)
        self.timer_miceCamera.timeout.connect(self.show_camera)
        # self.button_close.clicked.connect(self.close) # 退出

    def button_open_mice_camera_click(self):
        if self.timer_miceCamera.isActive() == False:
            flag = self.cap.open(self.CAM_NUM) # openCV检查摄像头开关状态
            if flag == False:
                msg = QtWidgets.QMessageBox.warning(self, u"Warning", u"请检测相机与电脑是否连接正确",
                                                    buttons=QtWidgets.QMessageBox.Ok,
                                                    defaultButton=QtWidgets.QMessageBox.Ok)
            # if msg==QtGui.QMessageBox.Cancel:
            #                     pass
            else:
                self.timer_miceCamera.start(30)

                self.open_miceCamera.setText(u'关闭相机')
        else:
            self.timer_miceCamera.stop()
            self.cap.release()
            self.label_miceCamera.clear()
            self.open_miceCamera.setText(u'打开相机')

    def show_camera(self):
        flag, self.image = self.cap.read()
        # face = self.face_detect.align(self.image)
        # if face:
        #     pass
        show = cv2.resize(self.image, (640, 480))
        show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)
        # print(show.shape[1], show.shape[0])
        # show.shape[1] = 640, show.shape[0] = 480
        showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0], QtGui.QImage.Format_RGB888)
        self.label_miceCamera.setPixmap(QtGui.QPixmap.fromImage(showImage))
        # self.x += 1
        # self.label_move.move(self.x,100)

        # if self.x ==320:
        #     self.label_miceCamera.raise_()

    def closeEvent(self, event):
        ok = QtWidgets.QPushButton()
        cacel = QtWidgets.QPushButton()

        msg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, u"关闭", u"是否关闭！")

        msg.addButton(ok, QtWidgets.QMessageBox.ActionRole)
        msg.addButton(cacel, QtWidgets.QMessageBox.RejectRole)
        ok.setText(u'确定')
        cacel.setText(u'取消')
        # msg.setDetailedText('sdfsdff')
        if msg.exec_() == QtWidgets.QMessageBox.RejectRole:
            event.ignore()
        else:
            #             self.socket_client.send_command(self.socket_client.current_user_command)
            if self.cap.isOpened():
                self.cap.release()
            if self.timer_miceCamera.isActive():
                self.timer_miceCamera.stop()
            event.accept()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "大鼠机器人控制系统"))
        self.pushButton_2.setText(_translate("MainWindow", "关闭"))
        self.open_miceCamera.setText(_translate("MainWindow", "开启大鼠摄像头"))
        self.label_miceCamera.setText(_translate("MainWindow", "大鼠摄像头"))
        self.pushButton_4.setText(_translate("MainWindow", "关闭"))
        self.label_3.setText(_translate("MainWindow", "无人机摄像头"))
        self.pushButton_3.setText(_translate("MainWindow", "开启"))
        self.pushButton_5.setText(_translate("MainWindow", "下一页"))
        self.pushButton_5.setText(_translate("MainWindow", "下一页"))
        self.label_4.setText(_translate("MainWindow", "控制指令记录"))
        self.pushButton_6.setText(_translate("MainWindow", "上一页"))
        self.pushButton_7.setText(_translate("MainWindow", "刷新"))
        self.pushButton_8.setText(_translate("MainWindow", "跳转浏览器"))
        self.label_2.setText(_translate("MainWindow", "地图导航"))
        self.label_5.setText(_translate("MainWindow", "神经信号"))
        self.pushButton_10.setText(_translate("MainWindow", "波形函数"))
        # self.menu.setTitle(_translate("MainWindow", "大鼠机器人控制系统"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionfffff.setText(_translate("MainWindow", "选择1"))
        self.actionrrr.setText(_translate("MainWindow", "选择2"))

