#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import cv2

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QPalette, QBrush, QPixmap
import os

# 代码原理就是：
#
# 设定一个定时器，每隔一段时间，从视频流中取一帧放到界面上显示。
class Ui_MainWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Ui_MainWindow, self).__init__(parent) #父类的构造函数

        # self.face_recong = face.Recognition()
        self.timer_camera = QtCore.QTimer() #定义定时器，用于控制显示视频的帧率
        self.cap = cv2.VideoCapture() #视频流
        self.CAM_NUM = 0 #为0时表示视频流来自笔记本内置摄像头
        self.set_ui() #初始化程序界面
        self.slot_init() #初始化槽函数
        self.__flag_work = 0
        self.x = 0
        self.count = 0

    '''程序界面布局'''
    def set_ui(self):

        self.__layout_main = QtWidgets.QHBoxLayout() #总布局
        self.__layout_fun_button = QtWidgets.QVBoxLayout() #按键布局
        self.__layout_data_show = QtWidgets.QVBoxLayout() #数据(视频)显示布局

        self.button_open_camera = QtWidgets.QPushButton(u'打开相机') #建立用于打开摄像头的按键

        self.button_close = QtWidgets.QPushButton(u'退出') #建立用于退出程序的按键

        # Button 的颜色修改
        button_color = [self.button_open_camera, self.button_close]
        for i in range(2):
            button_color[i].setStyleSheet("QPushButton{color:black}"
                                          "QPushButton:hover{color:red}"
                                          "QPushButton{background-color:rgb(78,255,255)}"
                                          "QPushButton{border:2px}"
                                          "QPushButton{border-radius:10px}"
                                          "QPushButton{padding:2px 4px}")

        self.button_open_camera.setMinimumHeight(50) #设置按键大小
        self.button_close.setMinimumHeight(50)

        # move()方法移动窗口在屏幕上的位置到x = 300，y = 300坐标。
        self.move(300, 300)

        # 信息显示
        self.label_show_camera = QtWidgets.QLabel() #定义显示视频的Label
        self.label_move = QtWidgets.QLabel()
        self.label_move.setFixedSize(100, 100)

        self.label_show_camera.setFixedSize(641, 481)  # 窗口最小宽高 #给显示视频的Label设置大小为641x481
        self.label_show_camera.setAutoFillBackground(False)

        self.__layout_fun_button.addWidget(self.button_open_camera) #把打开摄像头的按键放到按键布局中
        self.__layout_fun_button.addWidget(self.button_close) #把退出程序的按键放到按键布局中
        self.__layout_fun_button.addWidget(self.label_move)

        self.__layout_main.addLayout(self.__layout_fun_button)  #把按键布局加入到总布局中
        self.__layout_main.addWidget(self.label_show_camera) #把用于显示视频的Label加入到总布局中
        '''总布局布置好后就可以把总布局作为参数传入下面函数'''
        self.setLayout(self.__layout_main) #到这步才会显示所有控件
        self.label_move.raise_()
        self.setWindowTitle(u'大鼠机器人控制系统')

        '''
        # 设置背景图片
        palette1 = QPalette()
        palette1.setBrush(self.backgroundRole(), QBrush(QPixmap('background.jpg')))
        self.setPalette(palette1)
        '''

    '''初始化所有槽函数'''
    def slot_init(self):
        self.button_open_camera.clicked.connect(self.button_open_camera_click) #若该按键被点击，则调用button_open_camera_clicked()
        self.timer_camera.timeout.connect(self.show_camera) #若定时器结束，则调用show_camera()
        self.button_close.clicked.connect(self.close) #若该按键被点击，则调用close()，注意这个close是父类QtWidgets.QWidget自带的，会关闭程序

    '''槽函数之一'''
    def button_open_camera_click(self):
        if self.timer_camera.isActive() == False: #若定时器未启动
            flag = self.cap.open(self.CAM_NUM) #参数是0，表示打开笔记本的内置摄像头，参数是视频文件路径则打开视频
            if flag == False: #flag表示open()成不成功
                msg = QtWidgets.QMessageBox.warning(self, u"Warning", u"请检测相机与电脑是否连接正确",
                                                    buttons=QtWidgets.QMessageBox.Ok,
                                                    defaultButton=QtWidgets.QMessageBox.Ok)
            # if msg==QtGui.QMessageBox.Cancel:
            #                     pass
            else:
                self.timer_camera.start(30) #定时器开始计时30ms，结果是每过30ms从摄像头中取一帧显示

                self.button_open_camera.setText(u'关闭相机')
        else:
            self.timer_camera.stop() #关闭定时器
            self.cap.release() #释放视频流
            self.label_show_camera.clear() #清空视频显示区域
            self.button_open_camera.setText(u'打开相机')

    def show_camera(self):
        flag, self.image = self.cap.read() #从视频流中读取
        # face = self.face_detect.align(self.image)
        # if face:
        #     pass
        show = cv2.resize(self.image, (640, 480)) #把读到的帧的大小重新设置为 640x480
        show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB) #视频色彩转换回RGB，这样才是现实的颜色
        # print(show.shape[1], show.shape[0])
        # show.shape[1] = 640, show.shape[0] = 480
        showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0], QtGui.QImage.Format_RGB888) #把读取到的视频数据变成QImage形式
        self.label_show_camera.setPixmap(QtGui.QPixmap.fromImage(showImage)) #往显示视频的Label里 显示QImage
        # self.x += 1
        # self.label_move.move(self.x,100)

        # if self.x ==320:
        #     self.label_show_camera.raise_()

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
            if self.timer_camera.isActive():
                self.timer_camera.stop()
            event.accept()


if __name__ == "__main__":
    App = QApplication(sys.argv) #固定的，表示程序应用
    ex = Ui_MainWindow() #实例化Ui_MainWindow
    ex.show() #调用ui的show()以显示。同样show()是源于父类QtWidgets.QWidget的
    sys.exit(App.exec_()) #不加这句，程序界面会一闪而过