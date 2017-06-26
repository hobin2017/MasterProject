# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 21:53:34 2017

@author: hobin
"""

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import * 

class PropertyOfChemical(QWidget):
    def __init__(self,parent=None):
        super(PropertyOfChemical,self).__init__(parent)
        
        self.a1=QLabel('CHEM_NO')
        self.a2=QLineEdit()
        self.a1.setBuddy(self.a2)
        self.a3=QHBoxLayout()
        self.a3.addWidget(self.a1)
        self.a3.addWidget(self.a2)
        
        self.b1=QLabel('CHEM_MW')
        self.b2=QLineEdit()
        self.b1.setBuddy(self.b2)
        self.b3=QHBoxLayout()
        self.b3.addWidget(self.b1)
        self.b3.addWidget(self.b2)
        
        self.c1=QLabel('CHEM_KOW')
        self.c2=QLineEdit()
        self.c1.setBuddy(self.c2)
        self.c3=QHBoxLayout()
        self.c3.addWidget(self.c1)
        self.c3.addWidget(self.c2)
        
        self.d1=QLabel('CHEM_PKA')
        self.d2=QLineEdit()
        self.d1.setBuddy(self.d2)
        self.d3=QHBoxLayout()
        self.d3.addWidget(self.d1)
        self.d3.addWidget(self.d2)
       
        self.e1=QLabel('CHEM_NONION')
        self.e2=QLineEdit()
        self.e1.setBuddy(self.e2)
        self.e3=QHBoxLayout()
        self.e3.addWidget(self.e1)
        self.e3.addWidget(self.e2)
        
        self.f1=QLabel('CHEM_UNBND')
        self.f2=QLineEdit()
        self.f1.setBuddy(self.f2)
        self.f3=QHBoxLayout()
        self.f3.addWidget(self.f1)
        self.f3.addWidget(self.f2)
        
        self.g1=QLabel('CHEM_ACIDBASE')
        self.g2=QLineEdit()
        self.g1.setBuddy(self.g2)
        self.g3=QHBoxLayout()
        self.g3.addWidget(self.g1)
        self.g3.addWidget(self.g2)
        
        self.z=QVBoxLayout()
        self.z.addLayout(self.a3)
        self.z.addLayout(self.b3)
        self.z.addLayout(self.c3)
        self.z.addLayout(self.d3)
        self.z.addLayout(self.e3)
        self.z.addLayout(self.f3)
        self.z.addLayout(self.g3)
        self.setLayout(self.z)
        
class SurreyWindow(QMainWindow):
    #主窗口的初始化
    def __init__(self,parent=None):
        super(SurreyWindow,self).__init__(parent)
        #调试
        
        
        #停靠窗口
        self.dockwindow1=QDockWidget('Parameters',self)
        self.dockwindow1.setAllowedAreas(Qt.RightDockWidgetArea)
        self.dockwindow1.mainlayout=PropertyOfChemical() #自定义的类
        self.dockwindow1.setWidget(self.dockwindow1.mainlayout)
        self.addDockWidget(Qt.RightDockWidgetArea, self.dockwindow1)
        
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