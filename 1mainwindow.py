# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 21:53:34 2017

@author: hobin
"""

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import * 


class SurreyWindow(QMainWindow):
    #主窗口的初始化
    def __init__(self):
        super().__init__()
        #调试
        
        
        #停靠窗口
        self.dockwindow1=QDockWidget('Parameters',self)
        self.dockwindow1.setAllowedAreas(Qt.LeftDockWidgetArea)
        self.dockwindow1.mainlayout= #自定义的类
        self.dockwindow1.setWidget(self.dockwindow1.mainlayout)
        self.addDockWidget(Qt.LeftDockWidgetArea, self.dockwindow1)
        
        #主窗口
        self.mainwindow1=QWidget()
        self.setCentralWidget(self.mainwindow1)
        
        #主菜单
        menu_file=self.menuBar().addMenu('File')
        menu_run=self.menuBar().addMenu('Run')
        menu_tools=self.menuBar().addMenu('Tools')
        menu_help=self.menuBar().addMenu('Help')
        
        #信号连接
        
        #应用程序窗口
        self.resize(640,480)
        self.center #自定义函数
        self.setWindowTitle('Transdermal Permeation Model')
        #self.setWindowIcon(QIcon('E:\PythonFile\PythonTestFile\icons\chinaz3s.ico')) #设置图标
        #self.setToolTip('Hello World!') #鼠标停留显示文字
        #self.statusBar().showMessage('Ready') #左下角的状态
        
        
    #重新定义closeEvent方法
    def closeEvent(self,event):
        reply=QMessageBox.question\
        (self,'Message',
         'Do you want to quit?',
         QMessageBox.Yes,
         QMessageBox.No)
        if reply==QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
    #打开窗口后放在屏幕中间
    def center(self):
        screen=QDesktopWidget().screenGeometry()
        size=self.geometry()
        self.move( (screen.width()-size.width())/2,\
                  (screen,height()-size.height())/2)

#测试代码
if __name__=='__main__':
    import sys
    app=QApplication(sys.argv)
    window1=SurreyWindow() #主窗口
    window1.show()
    
    sys.exit(app.exec_())