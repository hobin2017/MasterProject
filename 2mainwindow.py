# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 21:53:34 2017

@author: hobin
"""

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import * 

class CompartmentSetup(QWidget):
    def __init__(self,parent=None):
        super(CompartmentSetup,self).__init__(parent)
        
        self.a1=QLabel('ID')
        self.a2=QLineEdit()
        self.a1.setBuddy(self.a2)
        self.a3=QHBoxLayout()
        self.a3.addWidget(self.a1)
        self.a3.addWidget(self.a2)
        
        self.b1=QLabel('N_LAYER_X_SC')
        self.b2=QLineEdit()
        self.b1.setBuddy(self.b2)
        self.b3=QHBoxLayout()
        self.b3.addWidget(self.b1)
        self.b3.addWidget(self.b2)
        
        self.c1=QLabel('N_LAYER_Y_SC')
        self.c2=QLineEdit()
        self.c1.setBuddy(self.c2)
        self.c3=QHBoxLayout()
        self.c3.addWidget(self.c1)
        self.c3.addWidget(self.c2)
        
        self.d1=QLabel('N_MESH_X_SC_LP')
        self.d2=QLineEdit()
        self.d1.setBuddy(self.d2)
        self.d3=QHBoxLayout()
        self.d3.addWidget(self.d1)
        self.d3.addWidget(self.d2)
       
        self.e1=QLabel('N_MESH_Y_SC_LP')
        self.e2=QLineEdit()
        self.e1.setBuddy(self.e2)
        self.e3=QHBoxLayout()
        self.e3.addWidget(self.e1)
        self.e3.addWidget(self.e2)
        
        self.z=QVBoxLayout()
        self.z.addLayout(self.a3)
        self.z.addLayout(self.b3)
        self.z.addLayout(self.c3)
        self.z.addLayout(self.d3)
        self.z.addLayout(self.e3)
        
        self.groupbox1=QGroupBox('Compartment Setup')
        self.groupbox1.setLayout(self.z)        
        self.mainlayout=QVBoxLayout()
        self.mainlayout.addWidget(self.groupbox1)
        self.setLayout(self.mainlayout)
        
        
class Partition_Diffusion_Coefficient(QWidget):
    def __init__(self,parent=None):
        super(Partition_Diffusion_Coefficient,self).__init__(parent)
        
        self.a1=QLabel('KW_VH')
        self.a2=QLineEdit()
        self.a1.setBuddy(self.a2)
        self.a3=QHBoxLayout()
        self.a3.addWidget(self.a1)
        self.a3.addWidget(self.a2)
        
        self.b1=QLabel('D_VH')
        self.b2=QLineEdit()
        self.b1.setBuddy(self.b2)
        self.b3=QHBoxLayout()
        self.b3.addWidget(self.b1)
        self.b3.addWidget(self.b2)
        
        self.c1=QLabel('KW_SC')
        self.c2=QLineEdit()
        self.c1.setBuddy(self.c2)
        self.c3=QHBoxLayout()
        self.c3.addWidget(self.c1)
        self.c3.addWidget(self.c2)
        
        self.d1=QLabel('D_SC')
        self.d2=QLineEdit()
        self.d1.setBuddy(self.d2)
        self.d3=QHBoxLayout()
        self.d3.addWidget(self.d1)
        self.d3.addWidget(self.d2)
       
        self.e1=QLabel('KW_VE')
        self.e2=QLineEdit()
        self.e1.setBuddy(self.e2)
        self.e3=QHBoxLayout()
        self.e3.addWidget(self.e1)
        self.e3.addWidget(self.e2)
        
        self.f1=QLabel('D_VE')
        self.f2=QLineEdit()
        self.f1.setBuddy(self.f2)
        self.f3=QHBoxLayout()
        self.f3.addWidget(self.f1)
        self.f3.addWidget(self.f2)
        
        self.g1=QLabel('KW_DE')
        self.g2=QLineEdit()
        self.g1.setBuddy(self.g2)
        self.g3=QHBoxLayout()
        self.g3.addWidget(self.g1)
        self.g3.addWidget(self.g2)
        
        self.h1=QLabel('D_DE')
        self.h2=QLineEdit()
        self.h1.setBuddy(self.h2)
        self.h3=QHBoxLayout()
        self.h3.addWidget(self.h1)
        self.h3.addWidget(self.h2)
        
        self.i1=QLabel('KW_HF')
        self.i2=QLineEdit()
        self.i1.setBuddy(self.i2)
        self.i3=QHBoxLayout()
        self.i3.addWidget(self.i1)
        self.i3.addWidget(self.i2)
        
        self.j1=QLabel('D_HF')
        self.j2=QLineEdit()
        self.j1.setBuddy(self.j2)
        self.j3=QHBoxLayout()
        self.j3.addWidget(self.j1)
        self.j3.addWidget(self.j2)
        
        self.k1=QLabel('K_DE2BD')
        self.k2=QLineEdit()
        self.k1.setBuddy(self.k2)
        self.k3=QHBoxLayout()
        self.k3.addWidget(self.k1)
        self.k3.addWidget(self.k2)
        
        self.l1=QLabel('CLEAR_BD')
        self.l2=QLineEdit()
        self.l1.setBuddy(self.l2)
        self.l3=QHBoxLayout()
        self.l3.addWidget(self.l1)
        self.l3.addWidget(self.l2)
        
        self.z=QVBoxLayout()
        self.z.addLayout(self.a3)
        self.z.addLayout(self.b3)
        self.z.addLayout(self.c3)
        self.z.addLayout(self.d3)
        self.z.addLayout(self.e3)
        self.z.addLayout(self.f3)
        self.z.addLayout(self.g3)
        self.z.addLayout(self.h3)
        self.z.addLayout(self.i3)
        self.z.addLayout(self.j3)
        self.z.addLayout(self.k3)
        self.z.addLayout(self.l3)
        
        self.groupbox1=QGroupBox('Partition and Diffisuion Coefficient')
        self.groupbox1.setLayout(self.z)        
        self.mainlayout=QVBoxLayout()
        self.mainlayout.addWidget(self.groupbox1)
        self.setLayout(self.mainlayout)
        
        

class InitialConcentration(QWidget):
    def __init__(self,parent=None):
        super(InitialConcentration,self).__init__(parent)
        
        self.a1=QLabel('INIT_CONC_VH')
        self.a2=QLineEdit()
        self.a1.setBuddy(self.a2)
        self.a3=QHBoxLayout()
        self.a3.addWidget(self.a1)
        self.a3.addWidget(self.a2)
        
        self.b1=QLabel('INIT_CONC_SC')
        self.b2=QLineEdit()
        self.b1.setBuddy(self.b2)
        self.b3=QHBoxLayout()
        self.b3.addWidget(self.b1)
        self.b3.addWidget(self.b2)
        
        self.c1=QLabel('INIT_CONC_VE')
        self.c2=QLineEdit()
        self.c1.setBuddy(self.c2)
        self.c3=QHBoxLayout()
        self.c3.addWidget(self.c1)
        self.c3.addWidget(self.c2)
        
        self.d1=QLabel('INIT_CONC_DE')
        self.d2=QLineEdit()
        self.d1.setBuddy(self.d2)
        self.d3=QHBoxLayout()
        self.d3.addWidget(self.d1)
        self.d3.addWidget(self.d2)
       
        self.e1=QLabel('INIT_CONC_HF')
        self.e2=QLineEdit()
        self.e1.setBuddy(self.e2)
        self.e3=QHBoxLayout()
        self.e3.addWidget(self.e1)
        self.e3.addWidget(self.e2)
        
        self.f1=QLabel('INIT_CONC_BD')
        self.f2=QLineEdit()
        self.f1.setBuddy(self.f2)
        self.f3=QHBoxLayout()
        self.f3.addWidget(self.f1)
        self.f3.addWidget(self.f2)
        
        self.z=QVBoxLayout()
        self.z.addLayout(self.a3)
        self.z.addLayout(self.b3)
        self.z.addLayout(self.c3)
        self.z.addLayout(self.d3)
        self.z.addLayout(self.e3)
        self.z.addLayout(self.f3)

        self.groupbox3=QGroupBox('Initial Concentrations')
        self.groupbox3.setLayout(self.z)        
        self.mainlayout=QVBoxLayout()
        self.mainlayout.addWidget(self.groupbox3)
        self.setLayout(self.mainlayout)
        
        
class VehicleSetting(QWidget):
    def __init__(self,parent=None):
        super(VehicleSetting,self).__init__(parent)
        
        self.a1=QLabel('INFINITE_VH')
        self.a2=QLineEdit()
        self.a1.setBuddy(self.a2)
        self.a3=QHBoxLayout()
        self.a3.addWidget(self.a1)
        self.a3.addWidget(self.a2)
        
        self.b1=QLabel('AREA_VH')
        self.b2=QLineEdit()
        self.b1.setBuddy(self.b2)
        self.b3=QHBoxLayout()
        self.b3.addWidget(self.b1)
        self.b3.addWidget(self.b2)
        
        self.z=QVBoxLayout()
        self.z.addLayout(self.a3)
        self.z.addLayout(self.b3)        

        self.groupbox2=QGroupBox('Vehicle Setting')
        self.groupbox2.setLayout(self.z)        
        self.mainlayout=QVBoxLayout()
        self.mainlayout.addWidget(self.groupbox2)
        self.setLayout(self.mainlayout)        

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
        
        self.groupbox1=QGroupBox('Property of Chemical')
        self.groupbox1.setLayout(self.z)        
        self.mainlayout=QVBoxLayout()
        self.mainlayout.addWidget(self.groupbox1)
        self.setLayout(self.mainlayout) #QWidget的setlayout方法
        
        
        
class SurreyWindow(QMainWindow):
    #主窗口的初始化
    def __init__(self,parent=None):
        super(SurreyWindow,self).__init__(parent)
        #调试
        
        
        #停靠窗口1
        self.dockwindow1=QDockWidget('Parameters',self)
        self.dockwindow1.setAllowedAreas(Qt.RightDockWidgetArea) #此句会限定摆放区域
        self.dockwindow1.a1=PropertyOfChemical() #5个自定义的类
        self.dockwindow1.a2=VehicleSetting()
        self.dockwindow1.a3=InitialConcentration()
        
        self.dockwindow1.z1=QVBoxLayout()
        self.dockwindow1.z1.addWidget(self.dockwindow1.a1)
        self.dockwindow1.z1.addWidget(self.dockwindow1.a2)
        self.dockwindow1.z1.addWidget(self.dockwindow1.a3)
        self.dockwindow1.mainwidget=QWidget() #因为用到QDockWidget的setWidget方法
        self.dockwindow1.mainwidget.setLayout(self.dockwindow1.z1)
        self.dockwindow1.setWidget(self.dockwindow1.mainwidget) 
        self.addDockWidget(Qt.RightDockWidgetArea, self.dockwindow1) #区分与位置
        
        #停靠窗口2
        self.dockwindow2=QDockWidget('Parameters',self)
        self.dockwindow2.setAllowedAreas(Qt.LeftDockWidgetArea) #此句会限定摆放区域
        self.dockwindow2.a4=CompartmentSetup() #5个自定义的类
        self.dockwindow2.a5=Partition_Diffusion_Coefficient()
        
        self.dockwindow2.z1=QVBoxLayout()
        self.dockwindow2.z1.addWidget(self.dockwindow2.a4)
        self.dockwindow2.z1.addWidget(self.dockwindow2.a5)
        self.dockwindow2.mainwidget=QWidget() #因为用到QDockWidget的setWidget方法
        self.dockwindow2.mainwidget.setLayout(self.dockwindow2.z1)
        self.dockwindow2.setWidget(self.dockwindow2.mainwidget) 
        self.addDockWidget(Qt.LeftDockWidgetArea, self.dockwindow2) #区分与位置
        
        
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
            self.dockwindow1.close() #如果dock窗口被拖拽出外面且直接关闭主窗口，这个dock还会存在的
            self.dockwindow2.close()
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