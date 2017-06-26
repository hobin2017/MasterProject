# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 21:53:34 2017

@author: hobin
"""

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import * 

class InputParameters(QWidget):
    def __init__(self,parent=None):
        super(InputParameters,self).__init__(parent)
        self.a1=self.PropertyOfChemical()
        self.mainlayout=QVBoxLayout()
        self.mainlayout.addWidget(self.groupbox1)
        self.setLayout(self.mainlayout)
        
        
    def PropertyOfChemical(self):
        self.groupbox1=QGroupBox('Property of Chemical')
        self.layout1=QFormLayout()
        self.layout1.addRow(QLabel('CHEM_NO'),QLineEdit())
        self.layout1.addRow(QLabel('CHEM_MW'),QLineEdit())
        self.layout1.addRow(QLabel('CHEM_KOW'),QLineEdit())
        self.layout1.addRow(QLabel('CHEM_PKA'),QLineEdit())
        self.layout1.addRow(QLabel('CHEM_NONION'),QLineEdit())
        self.layout1.addRow(QLabel('CHEM__UNBND'),QLineEdit())
        self.layout1.addRow(QLabel('CHEM_ACIDBASE'),QLineEdit())
        self.groupbox1.setLayout(self.layout1)
        
class SurreyWindow(QMainWindow):
    #主窗口的初始化
    def __init__(self,parent=None):
        super(SurreyWindow,self).__init__(parent)
        #调试
        
        
        #右停靠窗口
        self.dockwindow1=QDockWidget('Input Parameters',self)
        self.dockwindow1.setAllowedAreas(Qt.RightDockWidgetArea)
        self.dockwindow1.mainlayout=InputParameters() #自定义的类
        self.dockwindow1.setWidget(self.dockwindow1.mainlayout)
        self.addDockWidget(Qt.RightDockWidgetArea, self.dockwindow1)
        
        #主窗口
        self.mainwindow1=QWidget()
        self.setCentralWidget(self.mainwindow1)
        
        #主菜单
        menu_view=self.menuBar().addMenu('View')

        
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