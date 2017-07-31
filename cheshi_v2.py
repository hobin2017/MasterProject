# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 21:53:34 2017

@author: hobin
"""

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import numpy as np
import os
#-------------------------------------------------------------------------------------------------------------
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
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------
class Projectviwer(QTreeWidget):
    def __init__(self,parent=None):
        super(Projectviwer, self).__init__(parent) #parent是QMainWindow
        self.setColumnCount(1)
        self.setHeaderLabel('Project')
        self.setColumnWidth(0, 1)
        self._parent=parent #方便访问
        #self.setContextMenuPolicy(Qt.CustomContextMenu) #改的话，会使contextMenuEvent失效的
        #self.customContextMenuRequested.connect()

    #
    def contextMenuEvent(self, event):
        if not self.indexOfTopLevelItem(self.currentItem()) == -1:
            self.contextmenu = QMenu(self)
            oneAction = self.contextmenu.addAction('Save Project')
            oneAction.triggered.connect(self._parent.saveProject)
            twoAction = self.contextmenu.addAction('Close Project')
            twoAction.triggered.connect(self._parent.closeProject)
            self.contextmenu.exec_(event.globalPos())




# -------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------------
class SurreyWindow(QMainWindow):

    #主窗口的初始化
    def __init__(self,parent=None):
        super(SurreyWindow,self).__init__(parent)




        #主窗口组件QTreeWidget
        self.projectview= Projectviwer(self)

        #主窗口26
        self.mainwindow=QWidget() #应用程序主窗口
        self.resultviewer=QTextBrowser()
        self.mainlayout=QHBoxLayout()
        self.mainlayout.addWidget(self.projectview)
        self.mainlayout.addWidget(self.resultviewer)
        self.mainlayout.setStretchFactor(self.projectview,1)#原本以为设置组件的宽度，用了一晚
        self.mainlayout.setStretchFactor(self.resultviewer,4)#两组件比例1:4
        self.mainwindow.setLayout(self.mainlayout)
        self.setCentralWidget(self.mainwindow) #应用程序主窗口的显示

        #信号连接汇总



        #主菜单
        self.menu1=self.menuBar().addMenu('&File') #主菜单1显示
        self.menu_newproject=self.menu1.addAction('New Project')#子菜单
        self.menu_newproject.triggered.connect(self.newProject)
        self.menu_openproject=self.menu1.addAction('Open Project')
        self.menu_openproject.triggered.connect(self.openProject)
        self.menu_saveproject = self.menu1.addAction('Save All')
        self.menu_saveproject.triggered.connect(self.saveAll)

        self.menu2=self.menuBar().addMenu('&Run') #主菜单2显示
        self.menu_run=self.menu2.addAction('RunSimulation')#子菜单
        self.menu_run.triggered.connect(self.runSimulation)
        self.menu_test=self.menu2.addAction('TextDesign')
        self.menu_test.triggered.connect(self.textDesign)


        #应用程序窗口
        self.resize(640,480)
        self.center #自定义函数
        self.setWindowTitle('Transdermal Permeation Model')
        #self.setWindowIcon(QIcon('E:\PythonFile\PythonTestFile\icons\chinaz3s.ico')) #设置图标
        #self.setToolTip('Hello World!') #鼠标停留显示文字
        #self.statusBar().showMessage('Ready') #左下角的状态


    #不完善
    def openProject(self):
        self._openproject = QFileDialog.getOpenFileName(self, 'Open File','.','(Project File (*.cfg))')[0] #第三个是默认显示路径
        if self._openprojec:
            with  open(self._openproject, 'r') as self._cfg:
                self._opendata = self._cfg.read() # Data type: 'str'
                print(self._opendata)
    #
    def newProject(self):
        #如果自己键入.txt的话，会代替.cfg的！
        #self.newprojectPath=QFileDialog.getSaveFileName(self,'Create Project','.','Project File (*.cfg)')
        #self.newprojectName=os.path.split(os.path.splitext(self.newprojectPath)[0])[1]
        self.newprojectPath=QFileDialog.getExistingDirectory(self,'Create Project') #返回一个绝对路径
        self.newprojectPath = self.newprojectPath.replace('/', '\\') #如果是Winodows系统，就需要
        #如果用户点击取消，则结束
        if self.newprojectPath:
            self.newprojectPath_config = os.path.join(self.newprojectPath, 'config')
            if not os.path.exists(self.newprojectPath_config):
                os.mkdir(self.newprojectPath_config)
            self.newprojectPath_simu = os.path.join(self.newprojectPath, 'simu')
            if not os.path.exists(self.newprojectPath_simu):  # 防止Bug
                os.mkdir(self.newprojectPath_simu)

            self.newprojectName = os.path.split(self.newprojectPath)[1]
            self.newproject = ProjectItem(self.projectview)  # 传入父窗口参数
            self.newproject.setText(0, '%s' % self.newprojectName)  # 工程名
            self.newproject.setSelected(True)  # 防止Bug
            self.projectview.insertTopLevelItem(0, self.newproject)  # 工程浏览窗口的显示，分离出的
            self.addDockWidget(Qt.RightDockWidgetArea, self.newproject.dockwindow)  # 因改动而分离出的
            self.newproject_configPath=os.path.join(self.newprojectPath_config,'Nicotine.cfg')
            print(self.newproject_configPath)
            with open(self.newproject_configPath, 'w') as self.newproject._file:
                text = np.array([['COMPARTMENT_SETUP   ', 'V,S', '\n'],
                                 ['COMP   ', '0 ', '20e-6 ', '-1 ', '1 ', '1', '\n'],
                                 ['COMP   ', '1 ', '16 ', '1 ', '2 ', '1', '\n'],
                                 ['CHEM_NO   ', '1', '\n'],
                                 ['CHEM_MW   ', '194.19', '\n'],
                                 ['CHEM_KOW   ', '0.851', '\n'],
                                 ['CHEM_PKA   ', '-1', '\n'],
                                 ['CHEM_NONION   ', '0.99', '\n'],
                                 ['CHEM_UNBND   ', '0.63', '\n'],
                                 ['CHEM_ACIDBASE   ', 'B', '\n'],
                                 ['INFINITE_VH   ', '0', '\n'],
                                 ['AREA_VH   ', '0.01', '\n'],
                                 ['INIT_CONC_VH   ', '1', '\n'],
                                 ['INIT_CONC_SC   ', '0', '\n'],
                                 ['INIT_CONC_VE   ', '0', '\n'],
                                 ['INIT_CONC_DE   ', '0', '\n'],
                                 ['INIT_CONC_HF   ', '0', '\n'],
                                 ['INIT_CONC_BD   ', '0', '\n'],
                                 ['KW_VH   ', '1', '\n'],
                                 ['D_VH   ', '-1', '\n'],
                                 ['KW_SC   ', '-1', '\n'],
                                 ['D_SC   ', '-1', '\n'],
                                 ['KW_VE   ', '-1', '\n'],
                                 ['D_VE   ', '-1', '\n'],
                                 ['KW_DE   ', '-1', '\n'],
                                 ['D_DE   ', '-1', '\n'],
                                 ['KW_HF   ', '-1', '\n'],
                                 ['D_HF   ', '-1', '\n'],
                                 ['K_DE2BD   ', '1.01', '\n'],
                                 ['CLEAR_BD   ', '2.66e-6', '\n'],
                                 ]
                                )
                for line in text:
                    self.newproject._file.writelines(line)


    def closeProject(self):
        #self.index_pro=self.projectview.indexOfTopLevelItem(self.projectview.currentItem().parent())
        self.index_pro = self.projectview.indexOfTopLevelItem(self.projectview.currentItem()) #如果不是TopLevelItem则返回-1
        self.projectview.takeTopLevelItem(self.index_pro)

    def saveProject(self):
        pass

    def saveAll(self):
        pass

    def runSimulation(self):
        # 假设Project文件夹用来存cfg和存simul结果
        self.runconfigPath=QFileDialog.getOpenFileName(self,'Select File for configuration','.','cfg File (*.cfg)')[0]
        self.runconfigPath=self.runconfigPath.replace('/','\\')
        if self.runconfigPath:
            self.runresutlPath=QFileDialog.getExistingDirectory(self,'Select File for result')
            self.runresutlPath=self.runresutlPath.replace('/','\\')
            #print(self.runresutlPath)
            runpath = os.path.join(os.path.abspath('.'), 'run_v2.py') # 假设PyQt主程序与run.py在同一目录下
            # 需要别人电脑安装好python，且设置好路径
            cmd = 'python ' + '"' + runpath + '" ' + self.runconfigPath + ' ' + self.runresutlPath
            output = os.popen(cmd)
            print(output.read())



    def textDesign(self):
        print('Total TopLevelItem: %s'% self.projectview.topLevelItemCount())
        print('Total child of current ToplevelItem: %s' % self.newproject.childCount())
        print('The text of currentItem: %s' % self.projectview.currentItem().text(0)) #0列
        
    
    #重新定义应用程序的closeEvent方法
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
                  (screen.height()-size.height())/2)

#--------------------------------------------------------------------------------------------------------
class ProjectItem(QTreeWidgetItem):
    def __init__(self, parent=None):
        super(ProjectItem, self).__init__(parent)
        # 具体工程结构的搭建
        self.VH_setting0 = QTreeWidgetItem(self,0)
        self.VH_setting0.setText(0, 'Vehicle Setting')
        self.SC_setting0 = QTreeWidgetItem(self,0)
        self.SC_setting0.setText(0, 'SC Setting')
        self.VE_setting0 = QTreeWidgetItem(self,0)
        self.VE_setting0.setText(0, 'VE Setting')
        self.DE_setting0 = QTreeWidgetItem(self,0)
        self.DE_setting0.setText(0, 'DE Setting')
        self.HF_setting0 = QTreeWidgetItem(self,0)
        self.HF_setting0.setText(0, 'HF Setting')
        self.BD_setting0 = QTreeWidgetItem(self,0)
        self.BD_setting0.setText(0, 'BD Setting')
        self.result0 = QTreeWidgetItem(self,0)
        self.result0.setText(0, 'Results')


        # 停靠窗口
        self.dockwindow = QDockWidget('Parameters Setting') #这里应该与工程名有关
        self.dockwindow.setAllowedAreas(Qt.RightDockWidgetArea)
        self.input1 = PropertyOfChemical()
        self.input2 = CompartmentSetup()
        self.input3 = VehicleSetting()
        self.input4 = InitialConcentration()
        self.input5 = Partition_Diffusion_Coefficient()
        self.dockwindow.hide()

        #信号连接
        # parent.itemSelectionChanged.connect(self.Viewer)#触发函数
        parent.itemDoubleClicked.connect(self.Viewer)  # 触发函数
        #parent.itemClicked.connect(self.Viewer)#parent在原来中是self.projectview




    #双击树状图，其处理函数
    def Viewer(self):

        if self.VH_setting0.isSelected() == True:
            self.dockwindow.setWidget(self.input1)
            self.dockwindow.show()
            print(1)
        elif self.SC_setting0.isSelected() == True:
            self.dockwindow.setWidget(self.input2)
            self.dockwindow.show()
            print(2)
        elif self.VE_setting0.isSelected() == True:
            self.dockwindow.setWidget(self.input1)
            self.dockwindow.show()
            print(3)
        elif self.DE_setting0.isSelected() == True:
            print(4)
        elif self.HF_setting0.isSelected() == True:
            print(5)
        elif self.BD_setting0.isSelected() == True:
            print(6)
        elif self.result0.isSelected() == True:
            print(7)
# --------------------------------------------------------------------------------------------------------

#测试代码
if __name__=='__main__':
    import sys
    app=QApplication(sys.argv)
    window1=SurreyWindow() #主窗口
    window1.show()
    sys.exit(app.exec_())