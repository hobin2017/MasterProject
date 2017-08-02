# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 21:53:34 2017

@author: hobin
"""

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import numpy as np
import pandas as pd
import os
import sys


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
            oneAction = self.contextmenu.addAction('Close Project')
            oneAction.triggered.connect(self._parent.closeProject)
            twoAction = self.contextmenu.addAction('Save Project')
            twoAction.triggered.connect(self.currentItem().saveproject)
            if self.currentItem().childCount()==0:
                threeAction = self.contextmenu.addAction('Compartment Setup')
                threeAction.triggered.connect(self.currentItem().configure) #ProjectItem里面的函数
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

    #
    def newProject(self):
        self.newproject_name, self.newproject_ok = QInputDialog.getText(self, 'New Project', 'Enter project name: ')
        if self.newproject_ok and bool(self.newproject_name):
            self.newproject = ProjectItem(self.projectview)  # 父窗口QTreeWidget
            self.newproject.setText(0, '%s' %self.newproject_name)  # 工程名
            self.newproject.setSelected(True)  # 防止Bug
            self.projectview.insertTopLevelItem(0, self.newproject)  # 工程浏览窗口的显示，分离出的

    #
    def openProject(self):
        self.openconfigPath = QFileDialog.getOpenFileName(self, 'Open File','.','(Project File (*.cfg))')[0] #第三个是默认显示路径
        if os.name == 'nt':
            self.openconfigPath = self.openconfigPath.replace('/','\\')
        #print(self.openconfigPath)
        if self.openconfigPath:
            self.openproject_name =os.path.split(os.path.split(os.path.split(self.openconfigPath)[0])[0])[1]
            #print(self.openproject_name)
            self.openproject=ProjectItem(self.projectview, cfg_path=self.openconfigPath)
            self.openproject.setText(0, '%s' %self.openproject_name)
            self.openproject.setSelected(True)
            self.projectview.insertTopLevelItem(0,self.openproject)

        
    def closeProject(self):
        #self.index_pro=self.projectview.indexOfTopLevelItem(self.projectview.currentItem().parent())
        self.index_pro = self.projectview.indexOfTopLevelItem(self.projectview.currentItem()) #如果不是TopLevelItem则返回-1
        self.projectview.takeTopLevelItem(self.index_pro)


    def runSimulation(self):
        # 假设Project文件夹用来存cfg和存simul结果
        self.runconfigPath=QFileDialog.getOpenFileName(self,'Select File for configuration','.','cfg File (*.cfg)')[0]
        if os.name=='nt':
            self.runconfigPath=self.runconfigPath.replace('/','\\')
        if self.runconfigPath:
            #self.runresutlPath=QFileDialog.getExistingDirectory(self,'Select File for result') #自己选择结果保存路径
            #self.runresutlPath=self.runresutlPath.replace('/','\\')
            self.runresutlPath = os.path.join(os.path.split(os.path.split(self.runconfigPath)[0])[0],'simu')
            runpath = os.path.join(os.path.abspath('.'), 'run_v2.py') # 假设PyQt主程序与run.py在同一目录下
            # 需要别人电脑安装好python，且设置好路径
            cmd = 'python ' + '"' + runpath + '" ' + self.runconfigPath + ' ' + self.runresutlPath
            print(cmd)
            #output = os.popen(cmd)
            #print(output.read())



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
        self.move( (screen.width()-size.width())/2, \
                   (screen.height()-size.height())/2)

#--------------------------------------------------------------------------------------------------------
class ProDlg(QDialog):
    def __init__(self):
        super(ProDlg, self).__init__()
        self.setWindowTitle('Compartment Setup')
        self.setFixedWidth(230)
        self.checkbutton1 = QCheckBox('Vehicle',self)
        self.checkbutton2 = QCheckBox('Stratum Corneum',self)
        self.checkbutton3 = QCheckBox('Viable Epidermis',self)
        self.checkbutton4 = QCheckBox('Dermis', self)
        self.checkbutton5 = QCheckBox('HF', self)
        self.checkbutton6 = QCheckBox('BD', self)
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.mainLayout = QVBoxLayout(self)
        self.mainLayout.addWidget(self.checkbutton1)
        self.mainLayout.addWidget(self.checkbutton2)
        self.mainLayout.addWidget(self.checkbutton3)
        self.mainLayout.addWidget(self.checkbutton4)
        self.mainLayout.addWidget(self.checkbutton5)
        self.mainLayout.addWidget(self.checkbutton6)
        self.mainLayout.addWidget(self.buttonBox)
        self.setLayout(self.mainLayout)

# --------------------------------------------------------------------------------------------------------
class ProjectItem(QTreeWidgetItem):
    def __init__(self, parent, cfg_path=None, prj_path=None):
        super(ProjectItem, self).__init__(parent)
        self.VH_setting0 = QTreeWidgetItem(0)
        self.VH_setting0.setText(0, 'Vehicle')
        self.SC_setting0 = QTreeWidgetItem(0)
        self.SC_setting0.setText(0, 'SC')
        self.VE_setting0 = QTreeWidgetItem(0)
        self.VE_setting0.setText(0, 'VE')
        self.DE_setting0 = QTreeWidgetItem(0)
        self.DE_setting0.setText(0, 'DE')
        self.HF_setting0 = QTreeWidgetItem(0)
        self.HF_setting0.setText(0, 'HF')
        self.BD_setting0 = QTreeWidgetItem(0)
        self.BD_setting0.setText(0, 'BD')
        self.result0 = QTreeWidgetItem(0)
        self.result0.setText(0, 'Results')
        self._parent=parent # parent在原来中是self.projectview
        self._parent.itemDoubleClicked.connect(self.viweData)
        self.dialog = ProDlg()
        if cfg_path==None:
            self.configure()
        else:
            with open(cfg_path, 'r') as self._cfg:
                self.data_cfg = self._cfg.readlines() # Data type: 'list'
                for lin in self.data_cfg:
                    lin=lin.split() #清除空格
                    if lin[0]=='COMPARTMENT_SETUP':
                        lin = lin[1].split(',')
                        print(lin)
                        for i in lin:
                            if i == 'V':
                                self.addChild(self.VH_setting0)
                            if i == 'S':
                                self.addChild(self.SC_setting0)
                            if i == 'E':
                                self.addChild(self.VE_setting0)
                            if i== 'D':
                                self.addChild(self.DE_setting0)
                            if i== 'H':
                                self.addChild(self.HF_setting0)
                            if i == 'B':
                                self.addChild(self.BD_setting0)
                        break
                        


    #
    def saveproject(self):
        # self.newprojectPath=QFileDialog.getSaveFileName(self,'Create Project','.','Project File (*.cfg)') #如果自己键入.txt的话，会代替.cfg的！
        # self.newproject_name=os.path.split(os.path.splitext(self.newprojectPath)[0])[1]
        self.saveprojectPath = QFileDialog.getExistingDirectory(self._parent, 'Save your project')  # 返回一个绝对路径
        # 如果用户点击取消，则结束
        if self.saveprojectPath:
            self.cfg_name,self.cfg_ok = QInputDialog.getText(self._parent, 'New cfg file', 'Enter cfg-file name: ')
            if self.cfg_ok and bool(self.cfg_name):
                if os.name == 'nt':
                    self.saveprojectPath = self.saveprojectPath.replace('/', '\\')
                self.saveprojectPath_config = os.path.join(self.saveprojectPath, 'config')
                if not os.path.exists(self.saveprojectPath_config):
                    os.mkdir(self.saveprojectPath_config)

                self.saveprojectPath_simu = os.path.join(self.saveprojectPath, 'simu')
                if not os.path.exists(self.saveprojectPath_simu):  # 防止Bug
                    os.mkdir(self.saveprojectPath_simu)

                self.saveproject_configPath = os.path.join(self.saveprojectPath_config, self.cfg_name+'.cfg')
                #print(self.saveproject_configPath)
                with open(self.saveproject_configPath, 'w') as self._file:
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
                        self._file.writelines(line)

    #暂时不允许多次configure
    def configure(self):
        if self.dialog.exec_():
            if self.dialog.checkbutton1.isChecked():
                self.addChild(self.VH_setting0)
            if self.dialog.checkbutton2.isChecked():
                self.addChild(self.SC_setting0)
            if self.dialog.checkbutton3.isChecked():
                self.addChild(self.VE_setting0)
            if self.dialog.checkbutton4.isChecked():
                self.addChild(self.DE_setting0)
            if self.dialog.checkbutton5.isChecked():
                self.addChild(self.HF_setting0)
            if self.dialog.checkbutton6.isChecked():
                self.addChild(self.BD_setting0)

    # 双击树状图，其处理函数
    def viweData(self):
        if self.VH_setting0.isSelected() == True:
            print(1)
        elif self.SC_setting0.isSelected() == True:
            print(2)
        elif self.VE_setting0.isSelected() == True:
            print(3)
        elif self.DE_setting0.isSelected() == True:
            print(4)
        elif self.HF_setting0.isSelected() == True:
            print(5)
        elif self.BD_setting0.isSelected() == True:
            print(6)
        elif self.result0.isSelected() == True:
            print(7)
        else:
            pass
# --------------------------------------------------------------------------------------------------------

#测试代码
if __name__=='__main__':
    app=QApplication(sys.argv)
    window1=SurreyWindow() #主窗口
    window1.show()
    sys.exit(app.exec_())