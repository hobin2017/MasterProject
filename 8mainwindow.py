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
    sendChemical = pyqtSignal(object)
    sendVH = pyqtSignal(object)
    sendSC = pyqtSignal(object)
    sendVE = pyqtSignal(str)
    sendDE = pyqtSignal(str)
    sendHF = pyqtSignal(str)
    sendBD = pyqtSignal(str)

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
class Parameterviwer0(QTableWidget):
    def __init__(self,parent=None):
        super(Parameterviwer0,self).__init__(parent)
        self._names = QTableWidgetItem('Name')
        self._names.setFlags(Qt.NoItemFlags)
        self._values = QTableWidgetItem('Value')
        self._values.setFlags(Qt.NoItemFlags)
        self.verticalHeader().setVisible(False)
        self.horizontalHeader().setVisible(False)
        #Properties of chemical
        self.CHEM_NO = QTableWidgetItem('CHEM_NO')
        self.CHEM_NO.setFlags(Qt.NoItemFlags)
        self.CHEM_NO_data = QTableWidgetItem()
        self.CHEM_MW = QTableWidgetItem('CHEM_MW')
        self.CHEM_MW.setFlags(Qt.NoItemFlags)
        self.CHEM_MW_data = QTableWidgetItem()
        self.CHEM_KOW =QTableWidgetItem('CHEM_KOW')
        self.CHEM_KOW.setFlags(Qt.NoItemFlags)
        self.CHEM_KOW_data = QTableWidgetItem()
        self.CHEM_PKA = QTableWidgetItem('CHEM_PKA')
        self.CHEM_PKA.setFlags(Qt.NoItemFlags)
        self.CHEM_PKA_data = QTableWidgetItem()
        self.CHEM_NONION = QTableWidgetItem('CHEM_NONION')
        self.CHEM_NONION.setFlags(Qt.NoItemFlags)
        self.CHEM_NONION_data = QTableWidgetItem()
        self.CHEM_UNBND = QTableWidgetItem('CHEM_UNBND')
        self.CHEM_UNBND.setFlags(Qt.NoItemFlags)
        self.CHEM_UNBND_data = QTableWidgetItem()
        self.CHEM_ACIDBASE = QTableWidgetItem('CHEM_ACIDBASE')
        self.CHEM_ACIDBASE.setFlags(Qt.NoItemFlags)
        self.CHEM_ACIDBASE_data = QTableWidgetItem()
        self.CHEM_DENSITY = QTableWidgetItem('CHEM_DENSITY')
        self.CHEM_DENSITY.setFlags(Qt.NoItemFlags)
        self.CHEM_DENSITY_data = QTableWidgetItem()
        self.CHEM_PHASE = QTableWidgetItem('CHEM_PHASE')
        self.CHEM_PHASE.setFlags(Qt.NoItemFlags)
        self.CHEM_PHASE_data = QTableWidgetItem()
        #Layout for QTableWidget
        self.setColumnCount(2)
        self.setRowCount(10)
        self.setItem(0, 0, self._names)
        self.setItem(0, 1, self._values)
        self.setItem(1, 0, self.CHEM_NO)
        self.setItem(1, 1, self.CHEM_NO_data)
        self.setItem(2, 0, self.CHEM_MW)
        self.setItem(2, 1, self.CHEM_MW_data)
        self.setItem(3, 0, self.CHEM_KOW)
        self.setItem(3, 1, self.CHEM_KOW_data)
        self.setItem(4, 0, self.CHEM_PKA)
        self.setItem(4, 1, self.CHEM_PKA_data)
        self.setItem(5, 0, self.CHEM_NONION)
        self.setItem(5, 1, self.CHEM_NONION_data)
        self.setItem(6, 0, self.CHEM_UNBND)
        self.setItem(6, 1, self.CHEM_UNBND_data)
        self.setItem(7, 0, self.CHEM_ACIDBASE)
        self.setItem(7, 1, self.CHEM_ACIDBASE_data)
        self.setItem(8, 0, self.CHEM_DENSITY)
        self.setItem(8, 1, self.CHEM_DENSITY_data)
        self.setItem(9, 0, self.CHEM_PHASE)
        self.setItem(9, 1, self.CHEM_PHASE_data)
        self._parent = parent

    def showchemical(self, showdata):
        self._parent.stacklayout.setCurrentWidget(self)
        #print(showdata)
        self.CHEM_NO_data.setText('%s'%showdata.CHEM_NO.iat[0])
        self.CHEM_MW_data.setText('%s'%showdata.CHEM_MW.iat[0])
        self.CHEM_KOW_data.setText('%s'%showdata.CHEM_KOW.iat[0])
        self.CHEM_PKA_data.setText('%s'%showdata.CHEM_PKA.iat[0])
        self.CHEM_NONION_data.setText('%s'%showdata.CHEM_NONION.iat[0])
        self.CHEM_UNBND_data.setText('%s'%showdata.CHEM_UNBND.iat[0])
        self.CHEM_ACIDBASE_data.setText('%s'%showdata.CHEM_ACIDBASE.iat[0])
        self.CHEM_DENSITY_data.setText('%s'%showdata.CHEM_DENSITY.iat[0])
        self.CHEM_PHASE_data.setText('%s'%showdata.CHEM_PHASE.iat[0])

#-------------------------------------------------------------------------------------------------------------
class Parameterviwer1(QTableWidget):
    def __init__(self, parent=None):
        super(Parameterviwer1, self).__init__(parent)
        self._names = QTableWidgetItem('Name')
        self._names.setFlags(Qt.NoItemFlags)
        self._values = QTableWidgetItem('Value')
        self._values.setFlags(Qt.NoItemFlags)
        self.verticalHeader().setVisible(False)
        self.horizontalHeader().setVisible(False)
        #Vehicle setting
        self.INFINITE_VH = QTableWidgetItem('INFINITE_VH')
        self.INFINITE_VH.setFlags(Qt.NoItemFlags)
        self.INFINITE_VH_data = QTableWidgetItem()
        self.AREA_VH = QTableWidgetItem('AREA_VH')
        self.AREA_VH.setFlags(Qt.NoItemFlags)
        self.AREA_VH_data = QTableWidgetItem()
        self.INIT_CONC_VH = QTableWidgetItem('INIT_CONC_VH')
        self.INIT_CONC_VH.setFlags(Qt.NoItemFlags)
        self.INIT_CONC_VH_data = QTableWidgetItem()
        self.KW_VH = QTableWidgetItem('KW_VH')
        self.KW_VH.setFlags(Qt.NoItemFlags)
        self.KW_VH_data = QTableWidgetItem()
        self.D_VH = QTableWidgetItem('D_VH')
        self.D_VH.setFlags(Qt.NoItemFlags)
        self.D_VH_data = QTableWidgetItem()
        self.VH_comp0 = QTableWidgetItem('ID_VH')
        self.VH_comp0.setFlags(Qt.NoItemFlags)
        self.VH_comp0_data = QTableWidgetItem()
        self.VH_comp1 = QTableWidgetItem('LEN_X')
        self.VH_comp1.setFlags(Qt.NoItemFlags)
        self.VH_comp1_data = QTableWidgetItem()
        self.VH_comp2 = QTableWidgetItem('LEN_Y')
        self.VH_comp2.setFlags(Qt.NoItemFlags)
        self.VH_comp2_data = QTableWidgetItem()
        self.VH_comp3 = QTableWidgetItem('N_MESH_X')
        self.VH_comp3.setFlags(Qt.NoItemFlags)
        self.VH_comp3_data = QTableWidgetItem()
        self.VH_comp4 = QTableWidgetItem('N_MESH_Y')
        self.VH_comp4.setFlags(Qt.NoItemFlags)
        self.VH_comp4_data = QTableWidgetItem()
        self.EVAP_SOLVENT_VH = QTableWidgetItem('EVAP_SOLVENT_VH')
        self.EVAP_SOLVENT_VH.setFlags(Qt.NoItemFlags)
        self.EVAP_SOLVENT_VH_data = QTableWidgetItem()
        self.EVAP_SOLUTE_VH = QTableWidgetItem('EVAP_SOLUTE_VH')
        self.EVAP_SOLUTE_VH.setFlags(Qt.NoItemFlags)
        self.EVAP_SOLUTE_VH_data = QTableWidgetItem()
        self.SOLVENT_MW = QTableWidgetItem('SOLVENT_MW')
        self.SOLVENT_MW.setFlags(Qt.NoItemFlags)
        self.SOLVENT_MW_data = QTableWidgetItem()
        self.SOLUBILITY_VH = QTableWidgetItem('SOLUBILITY_VH')
        self.SOLUBILITY_VH.setFlags(Qt.NoItemFlags)
        self.SOLUBILITY_VH_data = QTableWidgetItem()
        self.SOLVENT_DENSITY = QTableWidgetItem('SOLVENT_DENSITY')
        self.SOLVENT_DENSITY.setFlags(Qt.NoItemFlags)
        self.SOLVENT_DENSITY_data = QTableWidgetItem()
        #Layout
        self.setColumnCount(2)
        self.setRowCount(16)
        self.setItem(0, 0, self._names)
        self.setItem(0, 1, self._values)
        self.setItem(1, 0, self.INFINITE_VH)
        self.setItem(1, 1, self.INFINITE_VH_data)
        self.setItem(2, 0, self.AREA_VH)
        self.setItem(2, 1, self.AREA_VH_data)
        self.setItem(3, 0, self.INIT_CONC_VH)
        self.setItem(3, 1, self.INIT_CONC_VH_data)
        self.setItem(4, 0, self.KW_VH)
        self.setItem(4, 1, self.KW_VH_data)
        self.setItem(5, 0, self.D_VH)
        self.setItem(5, 1, self.D_VH_data)
        self.setItem(6, 0, self.VH_comp0)
        self.setItem(6, 1, self.VH_comp0_data)
        self.setItem(7, 0, self.VH_comp1)
        self.setItem(7, 1, self.VH_comp1_data)
        self.setItem(8, 0, self.VH_comp2)
        self.setItem(8, 1, self.VH_comp2_data)
        self.setItem(9, 0, self.VH_comp3)
        self.setItem(9, 1, self.VH_comp3_data)
        self.setItem(10, 0, self.VH_comp4)
        self.setItem(10, 1, self.VH_comp4_data)
        self.setItem(11, 0, self.EVAP_SOLVENT_VH)
        self.setItem(11, 1, self.EVAP_SOLVENT_VH_data)
        self.setItem(12, 0, self.EVAP_SOLUTE_VH)
        self.setItem(12, 1, self.EVAP_SOLUTE_VH_data)
        self.setItem(13, 0, self.SOLVENT_MW)
        self.setItem(13, 1, self.SOLVENT_MW_data)
        self.setItem(14, 0, self.SOLUBILITY_VH)
        self.setItem(14, 1, self.SOLUBILITY_VH_data)
        self.setItem(15, 0, self.SOLVENT_DENSITY)
        self.setItem(15, 1, self.SOLVENT_DENSITY_data)
        self._parent = parent

    def showVH(self, showdata):
        self._parent.stacklayout.setCurrentWidget(self)
        self.INFINITE_VH_data.setText(showdata.INFINITE_VH.iat[0])
        self.AREA_VH_data.setText(showdata.AREA_VH.iat[0])
        self.INIT_CONC_VH_data.setText('%s'%showdata.INIT_CONC_VH.iat[0])
        self.KW_VH_data.setText(showdata.KW_VH.iat[0])
        self.D_VH_data.setText(showdata.D_VH.iat[0])
        self.VH_comp0_data.setText(showdata.COMP_VH.iat[0])
        self.VH_comp1_data.setText(showdata.COMP_VH.iat[1])
        self.VH_comp2_data.setText(showdata.COMP_VH.iat[2])
        self.VH_comp3_data.setText(showdata.COMP_VH.iat[3])
        self.VH_comp4_data.setText(showdata.COMP_VH.iat[4])
        self.EVAP_SOLVENT_VH_data.setText(showdata.EVAP_SOLVENT_VH.iat[0])
        self.EVAP_SOLUTE_VH_data.setText(showdata.EVAP_SOLUTE_VH.iat[0])
        self.SOLVENT_MW_data.setText(showdata.SOLVENT_MW.iat[0])
        self.SOLUBILITY_VH_data.setText(showdata.SOLUBILITY_VH.iat[0])
        self.SOLVENT_DENSITY_data.setText(showdata.SOLVENT_DENSITY.iat[0])
#-------------------------------------------------------------------------------------------------------------
class SurreyWindow(QMainWindow):

    #主窗口的初始化
    def __init__(self,parent=None):
        super(SurreyWindow,self).__init__(parent)

        #主窗口
        self.tableviewer0 = Parameterviwer0(self)
        self.tableviewer1 = Parameterviwer1(self)
        self.projectview = Projectviwer(self)
        self.projectview.sendChemical.connect(self.tableviewer0.showchemical)
        self.projectview.sendVH.connect(self.tableviewer1.showVH)

        #主窗口Layout
        self.mainwindow=QWidget(self) #应用程序主窗口
        #
        self.resultviewer=QTextBrowser(self)
        #
        self.stacklayout = QStackedLayout(self)
        self.stacklayout.addWidget(self.tableviewer0)
        self.stacklayout.addWidget(self.tableviewer1)
        #
        self.mainlayout=QHBoxLayout(self)
        self.mainlayout.addWidget(self.projectview)
        self.mainlayout.addLayout(self.stacklayout)
        self.mainlayout.addWidget(self.resultviewer)
        self.mainlayout.setStretchFactor(self.projectview,1)#原本以为设置组件的宽度，用了一晚
        self.mainlayout.setStretchFactor(self.stacklayout,1)
        self.mainlayout.setStretchFactor(self.resultviewer,3)#两组件比例1:4
        #
        self.mainwindow.setLayout(self.mainlayout)
        self.setCentralWidget(self.mainwindow) #应用程序主窗口的显示

        #主菜单
        self.menu1=self.menuBar().addMenu('&File') #主菜单1显示
        self.menu_newproject=self.menu1.addAction('New Project')#子菜单
        self.menu_newproject.triggered.connect(self.newProject)
        self.menu_openproject=self.menu1.addAction('Load Project')
        self.menu_openproject.triggered.connect(self.loadProject)
        self.menu_closeprojects = self.menu1.addAction('Close All')
        self.menu_closeprojects.triggered.connect(self.closeProjects)

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
    def loadProject(self):
        self.openconfigPath = QFileDialog.getOpenFileName(self, 'Open File','.','(Project File (*.cfg))')[0] #第三个是默认显示路径
        if os.name == 'nt':
            self.openconfigPath = self.openconfigPath.replace('/','\\')
        if self.openconfigPath:
            self.openproject_name =os.path.split(os.path.split(os.path.split(self.openconfigPath)[0])[0])[1]
            #print(self.openproject_name)
            self.openproject=ProjectItem(self.projectview, cfg_path=self.openconfigPath) #传入cfg文件路径！
            self.openproject.setText(0, '%s' %self.openproject_name)
            self.openproject.setSelected(True)
            self.projectview.insertTopLevelItem(0,self.openproject)

        
    def closeProject(self):
        #self.index_pro=self.projectview.indexOfTopLevelItem(self.projectview.currentItem().parent())
        self.index_pro = self.projectview.indexOfTopLevelItem(self.projectview.currentItem()) #如果不是TopLevelItem则返回-1
        self.projectview.takeTopLevelItem(self.index_pro)

    def closeProjects(self):
        self.projectview.clear()

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
        #print('Total TopLevelItem: %s'% self.projectview.topLevelItemCount())
        #print('Total child of current ToplevelItem: %s' % self.newproject.childCount())
        #print('The text of currentItem: %s' % self.projectview.currentItem().text(0)) #0列
        pass


    
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

    def __init__(self, parent, cfg_path=None):
        super(ProjectItem, self).__init__(parent)
        self.Chemical_setting0 = QTreeWidgetItem(0)
        self.Chemical_setting0.setText(0,'Chemical')
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
        #内部核心数据--------------------------------------------------------
        self._dict1 = {
            'COMPARTMENT_SETUP':pd.Series('V,S,E,D,H'),
            'COMP_VH':pd.Series(['0','0','0','0','0']),
            'COMP_SC':pd.Series(['1']),
            'COMP_VE':pd.Series(['2']),
            'COMP_DE':pd.Series(['3']),
            'COMP_HF':pd.Series(['4']),
            'COMP_BD':pd.Series(['5']),
            'CHEM_NO':pd.Series('-1'),
            'CHEM_MW':pd.Series('-1'),
            'CHEM_KOW':pd.Series('-1'),
            'CHEM_PKA':pd.Series('-1'),
            'CHEM_NONION':pd.Series('-1'),
            'CHEM_UNBND':pd.Series('-1'),
            'CHEM_ACIDBASE':pd.Series('-1'),
            'CHEM_DENSITY':pd.Series('-1'),
            'CHEM_PHASE':pd.Series('SOLID'),
            'INFINITE_VH':pd.Series('-1'),
            'AREA_VH':pd.Series('-1'),
            'EVAP_SOLVENT_VH':pd.Series('-1'),
            'EVAP_SOLUTE_VH':pd.Series('-1'),
            'SOLVENT_MW':pd.Series('-1'),
            'SOLUBILITY_VH':pd.Series('-1'),
            'SOLVENT_DENSITY':pd.Series('-1'),
            'INIT_CONC_VH':pd.Series('-1'),
            'INIT_CONC_SC': pd.Series('-1'),
            'INIT_CONC_VE': pd.Series('-1'),
            'INIT_CONC_DE': pd.Series('-1'),
            'INIT_CONC_HF': pd.Series('-1'),
            'INIT_CONC_BD': pd.Series('-1'),
            'KW_VH':pd.Series('-1'),
            'D_VH':pd.Series('-1'),
            'KW_SC': pd.Series('-1'),
            'D_SC': pd.Series('-1'),
            'KW_VE': pd.Series('-1'),
            'D_VE': pd.Series('-1'),
            'KW_DE': pd.Series('-1'),
            'D_DE': pd.Series('-1'),
            'KW_HF': pd.Series('-1'),
            'D_HF': pd.Series('-1'),
            'K_DE2BD':pd.Series('-1'),
            'CLEAR_BD':pd.Series('-1')
                    }
        self._projData=pd.DataFrame(self._dict1)
        #默认数据代表“某一层不使用”，loaddata函数需要
        #内部核心数据--------------------------------------------------------
        self._parent=parent # parent在原来中是self.projectview
        self._parent.itemDoubleClicked.connect(self.viewData) #假如显示3个工程，那么一次双击就出发这三个工程的viweData
        self.dialog = ProDlg()
        if cfg_path==None:
            self.configure()
        else:
            #传入路径时，就会Copy出一份数据来，并且显示相关组件
            #print(cfg_path)
            with open(cfg_path, 'r') as f:
                lines = f.readlines()  #由于readlines所以Data type: 'LIST'
                #数据清洗+显示
                for lin in lines:
                    lin = list( filter(None, lin.split()) ) #去掉空格和回车
                    lin = list( filter(lambda x:x!='NaN', lin)) #去掉NaN数据
                    #print(lin)
                    if len(lin) != 0:
                        self.loaddata(tokens=lin)

    #
    def loaddata(self, tokens):
        if tokens[0][0]=='#':
            return
        elif tokens[0] == 'COMPARTMENT_SETUP':
            self._projData.COMPARTMENT_SETUP.iat[0] = tokens[1]
            tks = list(filter(None, tokens[1].split(',')))
            #print('catch tks : %s'%tks)
            self._dict2={}
            for i in range(len(tks)):
                self._dict2[str(i)]=tks[i]
            #print(self._dict2)
            for j in tks:
                #如果没有某一层，相应的参数应该使用默认值（代表不使用），而默认值在初始化时完成。
                if j == 'V':
                    self.addChild(self.Chemical_setting0)
                    self.addChild(self.VH_setting0)
                    #print('loaddata-COMPARTMENT_SETUP sucess')
                elif j == 'S':
                    self.addChild(self.SC_setting0)
                elif j == 'E':
                    self.addChild(self.VE_setting0)
                elif j == 'D':
                    self.addChild(self.DE_setting0)
                elif j == 'H':
                    self.addChild(self.HF_setting0)
                elif j == 'B':
                    self.addChild(self.BD_setting0)
        elif tokens[0] == 'COMP':
            if self._dict2[tokens[1]] == 'V':
                self._projData.COMP_VH = tokens[1:6]
            elif self._dict2[tokens[1]] == 'S':
                self._projData.COMP_SC = tokens[1:6]
                #print('loaddata-COMP sucess')
            elif self._dict2[tokens[1]] == 'E':
                self._projData.COMP_VE = tokens[1:6]
            elif self._dict2[tokens[1]] == 'D':
                self._projData.COMP_DE = tokens[1:6]
                #print(self._projData.COMP_DE)
            elif self._dict2[tokens[1]] == 'H':
                self._projData.COMP_HF = tokens[1:]
                #print(self._projData.COMP_HF)
            elif self._dict2[tokens[1]] == 'B':
                self._projData.COMP_BD = tokens[1:]
        #parameters relating to chemical
        elif tokens[0] == 'CHEM_NO':
            self._projData.CHEM_NO.iat[0] = tokens[1]
        elif tokens[0] == 'CHEM_MW':
            self._projData.CHEM_MW.iat[0] = tokens[1]
        elif tokens[0] == 'CHEM_KOW':
            self._projData.CHEM_KOW.iat[0] = tokens[1]
        elif tokens[0] == 'CHEM_PKA':
            self._projData.CHEM_PKA.iat[0] = tokens[1]
        elif tokens[0] == 'CHEM_NONION':
            self._projData.CHEM_NONION.iat[0] = tokens[1]
        elif tokens[0] == 'CHEM_UNBND':
            self._projData.CHEM_UNBND.iat[0] = tokens[1]
        elif tokens[0] == 'CHEM_ACIDBASE':
            self._projData.CHEM_ACIDBASE.iat[0] = tokens[1]
        elif tokens[0] == 'CHEM_DENSITY':
            self._projData.CHEM_DENSITY.iat[0] = tokens[1]
        elif tokens[0] == 'CHEM_PHASE':
            self._projData.CHEM_PHASE.iat[0] = tokens[1]
        elif tokens[0] == 'INFINITE_VH':
            self._projData.INFINITE_VH.iat[0] = tokens[1]
        elif tokens[0] == 'AREA_VH':
            self._projData.AREA_VH.iat[0] = tokens[1]
        elif tokens[0] == 'EVAP_SOLVENT_VH':
            self._projData.EVAP_SOLVENT_VH.iat[0] = tokens[1]
        elif tokens[0] == 'EVAP_SOLUTE_VH':
            self._projData.EVAP_SOLUTE_VH.iat[0] = tokens[1]
        elif tokens[0] == 'SOLVENT_DENSITY':
            self._projData.SOLVENT_DENSITY.iat[0] = tokens[1]
        elif tokens[0] == 'SOLVENT_MW':
            self._projData.SOLVENT_MW.iat[0] = tokens[1]
        elif tokens[0] == 'SOLUBILITY_VH':
            self._projData.SOLUBILITY_VH.iat[0] = tokens[1]
        #Inital conditions
        elif tokens[0] == 'INIT_CONC_VH':
            self._projData.INIT_CONC_VH.iat[0] = tokens[1]
        elif tokens[0] == 'INIT_CONC_SC':
            self._projData.INIT_CONC_SC.iat[0] = tokens[1]
        elif tokens[0] == 'INIT_CONC_VE':
            self._projData.INIT_CONC_VE.iat[0] = tokens[1]
        elif tokens[0] == 'INIT_CONC_DE':
            self._projData.INIT_CONC_DE.iat[0] = tokens[1]
        elif tokens[0] == 'INIT_CONC_HF':
            self._projData.INIT_CONC_HF.iat[0] = tokens[1]
        elif tokens[0] == 'INIT_CONC_BD':
            self._projData.INIT_CONC_BD.iat[0] = tokens[1]
        # partition and diffusion coefficients
        elif tokens[0] == 'KW_VH':
            self._projData.KW_VH.iat[0] = tokens[1]
        elif tokens[0] == 'D_VH':
            self._projData.D_VH.iat[0] = tokens[1]
        elif tokens[0] == 'KW_SC':
            self._projData.KW_SC.iat[0] = tokens[1]
        elif tokens[0] == 'D_SC':
            self._projData.D_SC.iat[0] = tokens[1]
        elif tokens[0] == 'KW_VE':
            self._projData.KW_VE.iat[0] = tokens[1]
        elif tokens[0] == 'D_VE':
            self._projData.D_VE.iat[0] = tokens[1]
        elif tokens[0] == 'KW_DE':
            self._projData.KW_DE.iat[0] = tokens[1]
        elif tokens[0] == 'D_DE':
            self._projData.D_DE.iat[0] = tokens[1]
        elif tokens[0] == 'KW_HF':
            self._projData.KW_HF.iat[0] = tokens[1]
        elif tokens[0] == 'D_HF':
            self._projData.D_HF.iat[0] = tokens[1]
        elif tokens[0] == 'K_DE2BD':  # dermis to blood partition
            self._projData.K_DE2BD.iat[0] = tokens[1]
        elif tokens[0] == 'CLEAR_BD':
            self._projData.CLEAR_BD.iat[0] = tokens[1]
        else:
            print('Unrecognised line in config file')
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
                self.addChild(self.Chemical_setting0)
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
    def viewData(self):
        if self.Chemical_setting0.isSelected():
            #只能从这里调用函数，使TableWidget显示数据
            self._parent.sendChemical.emit(self._projData)
            print(0)
        elif self.VH_setting0.isSelected():
            self._parent.sendVH.emit(self._projData)
            print(1)
        elif self.SC_setting0.isSelected():
            print(2)
        elif self.VE_setting0.isSelected():
            print(3)
        elif self.DE_setting0.isSelected():
            print(4)
        elif self.HF_setting0.isSelected():
            print(5)
        elif self.BD_setting0.isSelected():
            print(6)
        elif self.result0.isSelected():
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