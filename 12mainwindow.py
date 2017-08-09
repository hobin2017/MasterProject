# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 21:53:34 2017

@author: hobin
"""

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas #是QWidget的子类
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar #是QWidget的子类
from matplotlib.figure import Figure
import numpy as np
import pandas as pd
import os
import sys
# -------------------------------------------------------------------------------------------------------
class Projectviwer(QTreeWidget):
    sendChemical = pyqtSignal(object)
    sendVH = pyqtSignal(object)
    sendSC = pyqtSignal(object)
    sendVE = pyqtSignal(object)
    sendDE = pyqtSignal(object)
    sendHF = pyqtSignal(object)
    sendBD = pyqtSignal(object)

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
    def __init__(self,parent):
        super(Parameterviwer0,self).__init__(parent)
        self.setColumnCount(2)
        self.setRowCount(12)
        self._names = QTableWidgetItem('Name')
        self._names.setFlags(Qt.NoItemFlags)
        self._values = QTableWidgetItem('Value')
        self._values.setFlags(Qt.NoItemFlags)
        self.verticalHeader().setVisible(False)
        self.horizontalHeader().setVisible(False)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        #self.horizontalHeader().setStretchLastSection(True)
        #Properties of chemical
        self.CHEM_NO = QTableWidgetItem('CHEM_NO')
        self.CHEM_NO.setFlags(Qt.NoItemFlags)
        self.CHEM_NO_data = QLineEdit()
        self.CHEM_MW = QTableWidgetItem('CHEM_MW')
        self.CHEM_MW.setFlags(Qt.NoItemFlags)
        self.CHEM_MW_data = QLineEdit()
        self.CHEM_KOW =QTableWidgetItem('CHEM_KOW')
        self.CHEM_KOW.setFlags(Qt.NoItemFlags)
        self.CHEM_KOW_data = QLineEdit()
        self.CHEM_PKA = QTableWidgetItem('CHEM_PKA')
        self.CHEM_PKA.setFlags(Qt.NoItemFlags)
        self.CHEM_PKA_data = QLineEdit()
        self.CHEM_NONION = QTableWidgetItem('CHEM_NONION')
        self.CHEM_NONION.setFlags(Qt.NoItemFlags)
        self.CHEM_NONION_data = QLineEdit()
        self.CHEM_UNBND = QTableWidgetItem('CHEM_UNBND')
        self.CHEM_UNBND.setFlags(Qt.NoItemFlags)
        self.CHEM_UNBND_data = QLineEdit()
        self.CHEM_ACIDBASE = QTableWidgetItem('CHEM_ACIDBASE')
        self.CHEM_ACIDBASE.setFlags(Qt.NoItemFlags)
        self.CHEM_ACIDBASE_data = QLineEdit()
        self.CHEM_DENSITY = QTableWidgetItem('CHEM_DENSITY')
        self.CHEM_DENSITY.setFlags(Qt.NoItemFlags)
        self.CHEM_DENSITY_data = QLineEdit()
        self.CHEM_PHASE = QTableWidgetItem('CHEM_PHASE')
        self.CHEM_PHASE.setFlags(Qt.NoItemFlags)
        self.CHEM_PHASE_data = QLineEdit()
        #User's components
        self.button1 = QPushButton('Commit',self)
        self.button2 = QPushButton('Abandon',self)
        self.tips = QTableWidgetItem()
        self.tips.setFlags(Qt.NoItemFlags)
        self.tips.setTextAlignment(Qt.AlignCenter)
        #Layout for QTableWidget
        self.setItem(0, 0, self._names)
        self.setItem(0, 1, self._values)
        self.setItem(1, 0, self.CHEM_NO)
        self.setCellWidget(1, 1, self.CHEM_NO_data)
        self.setItem(2, 0, self.CHEM_MW)
        self.setCellWidget(2, 1, self.CHEM_MW_data)
        self.setItem(3, 0, self.CHEM_KOW)
        self.setCellWidget(3, 1, self.CHEM_KOW_data)
        self.setItem(4, 0, self.CHEM_PKA)
        self.setCellWidget(4, 1, self.CHEM_PKA_data)
        self.setItem(5, 0, self.CHEM_NONION)
        self.setCellWidget(5, 1, self.CHEM_NONION_data)
        self.setItem(6, 0, self.CHEM_UNBND)
        self.setCellWidget(6, 1, self.CHEM_UNBND_data)
        self.setItem(7, 0, self.CHEM_ACIDBASE)
        self.setCellWidget(7, 1, self.CHEM_ACIDBASE_data)
        self.setItem(8, 0, self.CHEM_DENSITY)
        self.setCellWidget(8, 1, self.CHEM_DENSITY_data)
        self.setItem(9, 0, self.CHEM_PHASE)
        self.setCellWidget(9, 1, self.CHEM_PHASE_data)
        self.setItem(10, 0, self.tips)
        self.setSpan(10, 0, 1, 2)
        self.setCellWidget(11,0, self.button1)
        self.setCellWidget(11,1, self.button2)
        # Signals
        #self.itemChanged.connect(self.readchemical) #用户双击不同工程的Chemical层，会触发很多很多次该函数
        #self.doubleClicked.connect(self.readchemical) #只有“可编辑的”单元格，它们才会触发函数
        self.button1.clicked.connect(self.commit)
        self.button2.clicked.connect(self.abandon)
        #设计用户输入的限制
        self.CHEM_NO_data.setValidator(QIntValidator(0, 999, self))  # 范围0到1的整数
        self.CHEM_MW_data.setValidator(QDoubleValidator(bottom=0.0, top=999.99,parent=self))#范围0到100的浮点数，记录小数点后3位。可以有e！
        self.CHEM_PHASE_data.setValidator(QRegularExpressionValidator(QRegularExpression(r'[A-Z]+'),self))
        #用户提示
        self.CHEM_NO_data.setWhatsThis('The range is [0,999]') #focus on this widget, then press SHIFT+F1
        self.CHEM_PHASE_data.setWhatsThis('Please enter upper case letter')
        self._parent = parent
    #
    def showchemical(self, showdata):
        self._parent.maintablelayout.setCurrentWidget(self)
        self._projData = showdata #并不是copy！就像a=[10,9];b=a;如果b[0]=0，那么a为[0,9]而非原来的[10,9]
        #self.CHEM_NO_data.setText('%s' % showdata.CHEM_NO.iat[0]) #用这种方式的话，就会在界面出现None或者np.nan字样！
        self.CHEM_NO_data.setText(showdata.CHEM_NO.iat[0]) #用这种方式，就不会在界面上出现None或者np.nan字样
        self.CHEM_MW_data.setText(showdata.CHEM_MW.iat[0])
        self.CHEM_KOW_data.setText(showdata.CHEM_KOW.iat[0])
        self.CHEM_PKA_data.setText(showdata.CHEM_PKA.iat[0])
        self.CHEM_NONION_data.setText(showdata.CHEM_NONION.iat[0])
        self.CHEM_UNBND_data.setText(showdata.CHEM_UNBND.iat[0])
        self.CHEM_ACIDBASE_data.setText(showdata.CHEM_ACIDBASE.iat[0])
        self.CHEM_DENSITY_data.setText(showdata.CHEM_DENSITY.iat[0])
        self.CHEM_PHASE_data.setText(showdata.CHEM_PHASE.iat[0])
    #
    def commit(self):
        self._projData.CHEM_NO.iat[0] = self.CHEM_NO_data.text()
        self._projData.CHEM_MW.iat[0] = self.CHEM_MW_data.text()
        self._projData.CHEM_KOW.iat[0] = self.CHEM_KOW_data.text()
        self._projData.CHEM_PKA.iat[0] = self.CHEM_PKA_data.text()
        self._projData.CHEM_NONION.iat[0] = self.CHEM_NONION_data.text()
        self._projData.CHEM_UNBND.iat[0] = self.CHEM_UNBND_data.text()
        self._projData.CHEM_ACIDBASE.iat[0] = self.CHEM_ACIDBASE_data.text()
        self._projData.CHEM_DENSITY.iat[0] = self.CHEM_DENSITY_data.text()
        self._projData.CHEM_PHASE.iat[0] = self.CHEM_PHASE_data.text()
        self.tips.setText('Successful commit')
    #
    def abandon(self):
        self.showchemical(self._projData)
        self.tips.setText('Successful abandon')
#-------------------------------------------------------------------------------------------------------------
class Parameterviwer1(QTableWidget):
    def __init__(self, parent):
        super(Parameterviwer1, self).__init__(parent)
        self.setColumnCount(2)
        self.setRowCount(18)
        self._names = QTableWidgetItem('Name')
        self._names.setFlags(Qt.NoItemFlags)
        self._values = QTableWidgetItem('Value')
        self._values.setFlags(Qt.NoItemFlags)
        self.verticalHeader().setVisible(False)
        self.horizontalHeader().setVisible(False)
        #self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.horizontalHeader().setStretchLastSection(True)
        #Vehicle setting
        self.INFINITE_VH = QTableWidgetItem('INFINITE_VH')
        self.INFINITE_VH.setFlags(Qt.NoItemFlags)
        self.INFINITE_VH_data = QLineEdit()
        self.AREA_VH = QTableWidgetItem('AREA_VH')
        self.AREA_VH.setFlags(Qt.NoItemFlags)
        self.AREA_VH_data = QLineEdit()
        self.INIT_CONC_VH = QTableWidgetItem('INIT_CONC_VH')
        self.INIT_CONC_VH.setFlags(Qt.NoItemFlags)
        self.INIT_CONC_VH_data = QLineEdit()
        self.KW_VH = QTableWidgetItem('KW_VH')
        self.KW_VH.setFlags(Qt.NoItemFlags)
        self.KW_VH_data = QLineEdit()
        self.D_VH = QTableWidgetItem('D_VH')
        self.D_VH.setFlags(Qt.NoItemFlags)
        self.D_VH_data = QLineEdit()
        self.VH_comp0 = QTableWidgetItem('ID_VH')
        self.VH_comp0.setFlags(Qt.NoItemFlags)
        self.VH_comp0_data = QLineEdit()
        self.VH_comp1 = QTableWidgetItem('LEN_X')
        self.VH_comp1.setFlags(Qt.NoItemFlags)
        self.VH_comp1_data = QLineEdit()
        self.VH_comp2 = QTableWidgetItem('LEN_Y')
        self.VH_comp2.setFlags(Qt.NoItemFlags)
        self.VH_comp2_data = QLineEdit()
        self.VH_comp3 = QTableWidgetItem('N_MESH_X')
        self.VH_comp3.setFlags(Qt.NoItemFlags)
        self.VH_comp3_data = QLineEdit()
        self.VH_comp4 = QTableWidgetItem('N_MESH_Y')
        self.VH_comp4.setFlags(Qt.NoItemFlags)
        self.VH_comp4_data = QLineEdit()
        self.EVAP_SOLVENT_VH = QTableWidgetItem('EVAP_SOLVENT_VH')
        self.EVAP_SOLVENT_VH.setFlags(Qt.NoItemFlags)
        self.EVAP_SOLVENT_VH_data = QLineEdit()
        self.EVAP_SOLUTE_VH = QTableWidgetItem('EVAP_SOLUTE_VH')
        self.EVAP_SOLUTE_VH.setFlags(Qt.NoItemFlags)
        self.EVAP_SOLUTE_VH_data = QLineEdit()
        self.SOLVENT_MW = QTableWidgetItem('SOLVENT_MW')
        self.SOLVENT_MW.setFlags(Qt.NoItemFlags)
        self.SOLVENT_MW_data = QLineEdit()
        self.SOLUBILITY_VH = QTableWidgetItem('SOLUBILITY_VH')
        self.SOLUBILITY_VH.setFlags(Qt.NoItemFlags)
        self.SOLUBILITY_VH_data = QLineEdit()
        self.SOLVENT_DENSITY = QTableWidgetItem('SOLVENT_DENSITY')
        self.SOLVENT_DENSITY.setFlags(Qt.NoItemFlags)
        self.SOLVENT_DENSITY_data = QLineEdit()
        #User's components
        self.button1 = QPushButton('Commit', self)
        self.button2 = QPushButton('Abandon', self)
        self.tips = QTableWidgetItem()
        self.tips.setFlags(Qt.NoItemFlags)
        self.tips.setTextAlignment(Qt.AlignCenter)
        #Layout
        self.setItem(0, 0, self._names)
        self.setItem(0, 1, self._values)
        self.setItem(1, 0, self.INFINITE_VH)
        self.setCellWidget(1, 1, self.INFINITE_VH_data)
        self.setItem(2, 0, self.AREA_VH)
        self.setCellWidget(2, 1, self.AREA_VH_data)
        self.setItem(3, 0, self.INIT_CONC_VH)
        self.setCellWidget(3, 1, self.INIT_CONC_VH_data)
        self.setItem(4, 0, self.KW_VH)
        self.setCellWidget(4, 1, self.KW_VH_data)
        self.setItem(5, 0, self.D_VH)
        self.setCellWidget(5, 1, self.D_VH_data)
        self.setItem(6, 0, self.VH_comp0)
        self.setCellWidget(6, 1, self.VH_comp0_data)
        self.setItem(7, 0, self.VH_comp1)
        self.setCellWidget(7, 1, self.VH_comp1_data)
        self.setItem(8, 0, self.VH_comp2)
        self.setCellWidget(8, 1, self.VH_comp2_data)
        self.setItem(9, 0, self.VH_comp3)
        self.setCellWidget(9, 1, self.VH_comp3_data)
        self.setItem(10, 0, self.VH_comp4)
        self.setCellWidget(10, 1, self.VH_comp4_data)
        self.setItem(11, 0, self.EVAP_SOLVENT_VH)
        self.setCellWidget(11, 1, self.EVAP_SOLVENT_VH_data)
        self.setItem(12, 0, self.EVAP_SOLUTE_VH)
        self.setCellWidget(12, 1, self.EVAP_SOLUTE_VH_data)
        self.setItem(13, 0, self.SOLVENT_MW)
        self.setCellWidget(13, 1, self.SOLVENT_MW_data)
        self.setItem(14, 0, self.SOLUBILITY_VH)
        self.setCellWidget(14, 1, self.SOLUBILITY_VH_data)
        self.setItem(15, 0, self.SOLVENT_DENSITY)
        self.setCellWidget(15, 1, self.SOLVENT_DENSITY_data)
        self.setItem(16, 0, self.tips)
        self.setSpan(16, 0, 1, 2)
        self.setCellWidget(17, 0, self.button1)
        self.setCellWidget(17, 1, self.button2)
        #Signals
        self.button1.clicked.connect(self.commit)
        self.button2.clicked.connect(self.abandon)
        #设计用户输入的限制
        self._parent = parent
    #
    def showVH(self, showdata):
        self._parent.maintablelayout.setCurrentWidget(self)
        self._projData = showdata
        self.INFINITE_VH_data.setText(showdata.INFINITE_VH.iat[0])
        self.AREA_VH_data.setText(showdata.AREA_VH.iat[0])
        self.INIT_CONC_VH_data.setText(showdata.INIT_CONC_VH.iat[0])
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
    #
    def commit(self):
        self._projData.INFINITE_VH.iat[0] = self.INFINITE_VH_data.text()
        self._projData.AREA_VH.iat[0] = self.AREA_VH_data.text()
        self._projData.INIT_CONC_VH.iat[0] = self.INIT_CONC_VH_data.text()
        self._projData.KW_VH.iat[0] = self.KW_VH_data.text()
        self._projData.D_VH.iat[0] = self.D_VH_data.text()
        self._projData.COMP_VH.iat[0] = self.VH_comp0_data.text()
        self._projData.COMP_VH.iat[1] = self.VH_comp1_data.text()
        self._projData.COMP_VH.iat[2] = self.VH_comp2_data.text()
        self._projData.COMP_VH.iat[3] = self.VH_comp3_data.text()
        self._projData.COMP_VH.iat[4] = self.VH_comp4_data.text()
        self._projData.EVAP_SOLVENT_VH.iat[0] = self.EVAP_SOLVENT_VH_data.text()
        self._projData.EVAP_SOLUTE_VH.iat[0] = self.EVAP_SOLUTE_VH_data.text()
        self._projData.SOLVENT_MW.iat[0] = self.SOLVENT_MW_data.text()
        self._projData.SOLUBILITY_VH.iat[0] = self.SOLUBILITY_VH_data.text()
        self._projData.SOLVENT_DENSITY.iat[0] = self.SOLVENT_DENSITY_data.text()
        self.tips.setText('Successful commit')
    #
    def abandon(self):
        self.showVH(self._projData)
        self.tips.setText('Successful abandon')
#-------------------------------------------------------------------------------------------------------------
class Parameterviwer2(QTableWidget):
    def __init__(self,parent):
        super(Parameterviwer2, self).__init__(parent)
        self.setColumnCount(2)
        self.setRowCount(11)
        self._names = QTableWidgetItem('Name')
        self._names.setFlags(Qt.NoItemFlags)
        self._values = QTableWidgetItem('Value')
        self._values.setFlags(Qt.NoItemFlags)
        self.verticalHeader().setVisible(False)
        self.horizontalHeader().setVisible(False)
        self.horizontalHeader().setStretchLastSection(True)
        #Stratum corneum
        self.INIT_CONC_SC = QTableWidgetItem('INIT_CONC_SC')
        self.INIT_CONC_SC.setFlags(Qt.NoItemFlags)
        self.INIT_CONC_SC_data = QLineEdit()
        self.KW_SC = QTableWidgetItem('KW_SC')
        self.KW_SC.setFlags(Qt.NoItemFlags)
        self.KW_SC_data = QLineEdit()
        self.D_SC = QTableWidgetItem('D_SC')
        self.D_SC.setFlags(Qt.NoItemFlags)
        self.D_SC_data = QLineEdit()
        self.SC_comp0 = QTableWidgetItem('ID_SC')
        self.SC_comp0.setFlags(Qt.NoItemFlags)
        self.SC_comp0_data = QLineEdit()
        self.SC_comp1 = QTableWidgetItem('N_LAYER_X_SC')
        self.SC_comp1.setFlags(Qt.NoItemFlags)
        self.SC_comp1_data = QLineEdit()
        self.SC_comp2 = QTableWidgetItem('N_LAYER_Y_SC')
        self.SC_comp2.setFlags(Qt.NoItemFlags)
        self.SC_comp2_data = QLineEdit()
        self.SC_comp3 = QTableWidgetItem('N_MESH_X_SC_LP')
        self.SC_comp3.setFlags(Qt.NoItemFlags)
        self.SC_comp3_data = QLineEdit()
        self.SC_comp4 = QTableWidgetItem('N_MESH_Y_SC_LP')
        self.SC_comp4.setFlags(Qt.NoItemFlags)
        self.SC_comp4_data = QLineEdit()
        #User's components
        self.button1 = QPushButton('Commit', self)
        self.button2 = QPushButton('Abandon', self)
        self.tips = QTableWidgetItem()
        self.tips.setFlags(Qt.NoItemFlags)
        self.tips.setTextAlignment(Qt.AlignCenter)
        #Layout
        self.setItem(0, 0, self._names)
        self.setItem(0, 1, self._values)
        self.setItem(1, 0, self.INIT_CONC_SC)
        self.setCellWidget(1, 1, self.INIT_CONC_SC_data)
        self.setItem(2, 0, self.KW_SC)
        self.setCellWidget(2, 1, self.KW_SC_data)
        self.setItem(3, 0, self.D_SC)
        self.setCellWidget(3, 1, self.D_SC_data)
        self.setItem(4, 0, self.SC_comp0)
        self.setCellWidget(4, 1, self.SC_comp0_data)
        self.setItem(5, 0, self.SC_comp1)
        self.setCellWidget(5, 1, self.SC_comp1_data)
        self.setItem(6, 0, self.SC_comp2)
        self.setCellWidget(6, 1, self.SC_comp2_data)
        self.setItem(7, 0, self.SC_comp3)
        self.setCellWidget(7,1, self.SC_comp3_data)
        self.setItem(8, 0, self.SC_comp4)
        self.setCellWidget(8, 1, self.SC_comp4_data)
        self.setItem(9, 0, self.tips)
        self.setSpan(9, 0, 1, 2)
        self.setCellWidget(10, 0, self.button1)
        self.setCellWidget(10, 1, self.button2)
        #Signals
        self.button1.clicked.connect(self.commit)
        self.button2.clicked.connect(self.abandon)
        self._parent = parent
    #
    def showSC(self,showdata):
        self._parent.maintablelayout.setCurrentWidget(self)
        self._projData = showdata
        self.INIT_CONC_SC_data.setText(showdata.INIT_CONC_SC.iat[0])
        self.KW_SC_data.setText(showdata.KW_SC.iat[0])
        self.D_SC_data.setText(showdata.D_SC.iat[0])
        self.SC_comp0_data.setText(showdata.COMP_SC.iat[0])
        self.SC_comp1_data.setText(showdata.COMP_SC.iat[1])
        self.SC_comp2_data.setText(showdata.COMP_SC.iat[2])
        self.SC_comp3_data.setText(showdata.COMP_SC.iat[3])
        self.SC_comp4_data.setText(showdata.COMP_SC.iat[4])
    #
    def commit(self):
        self._projData.INIT_CONC_SC.iat[0] = self.INIT_CONC_SC_data.text()
        self._projData.KW_SC.iat[0] = self.KW_SC_data.text()
        self._projData.D_SC.iat[0] = self.D_SC_data.text()
        self._projData.COMP_SC.iat[0] = self.SC_comp0_data.text()
        self._projData.COMP_SC.iat[1] = self.SC_comp1_data.text()
        self._projData.COMP_SC.iat[2] = self.SC_comp2_data.text()
        self._projData.COMP_SC.iat[3] = self.SC_comp3_data.text()
        self._projData.COMP_SC.iat[4] = self.SC_comp4_data.text()
        self.tips.setText('Successful commit')
    #
    def abandon(self):
        self.showSC(self._projData)
        self.tips.setText('Successful abandon')
#-------------------------------------------------------------------------------------------------------------
class Parameterviwer3(QTableWidget):
    def __init__(self,parent):
        super(Parameterviwer3, self).__init__(parent)
        self.setColumnCount(2)
        self.setRowCount(11)
        self._names = QTableWidgetItem('Name')
        self._names.setFlags(Qt.NoItemFlags)
        self._values = QTableWidgetItem('Value')
        self._values.setFlags(Qt.NoItemFlags)
        self.verticalHeader().setVisible(False)
        self.horizontalHeader().setVisible(False)
        self.horizontalHeader().setStretchLastSection(True)
        #Viable epidermis
        self.INIT_CONC_VE = QTableWidgetItem('INIT_CONC_VE')
        self.INIT_CONC_VE.setFlags(Qt.NoItemFlags)
        self.INIT_CONC_VE_data = QLineEdit()
        self.KW_VE = QTableWidgetItem('KW_VE')
        self.KW_VE.setFlags(Qt.NoItemFlags)
        self.KW_VE_data = QLineEdit()
        self.D_VE = QTableWidgetItem('D_VE')
        self.D_VE.setFlags(Qt.NoItemFlags)
        self.D_VE_data = QLineEdit()
        self.VE_comp0 = QTableWidgetItem('ID_VE')
        self.VE_comp0.setFlags(Qt.NoItemFlags)
        self.VE_comp0_data = QLineEdit()
        self.VE_comp1 = QTableWidgetItem('N_LAYER_X_VE')
        self.VE_comp1.setFlags(Qt.NoItemFlags)
        self.VE_comp1_data = QLineEdit()
        self.VE_comp2 = QTableWidgetItem('N_LAYER_Y_VE')
        self.VE_comp2.setFlags(Qt.NoItemFlags)
        self.VE_comp2_data = QLineEdit()
        self.VE_comp3 = QTableWidgetItem('N_MESH_X_VE_LP')
        self.VE_comp3.setFlags(Qt.NoItemFlags)
        self.VE_comp3_data = QLineEdit()
        self.VE_comp4 = QTableWidgetItem('N_MESH_Y_VE_LP')
        self.VE_comp4.setFlags(Qt.NoItemFlags)
        self.VE_comp4_data = QLineEdit()
        #User's components
        self.button1 = QPushButton('Commit', self)
        self.button2 = QPushButton('Abandon', self)
        self.tips = QTableWidgetItem()
        self.tips.setFlags(Qt.NoItemFlags)
        self.tips.setTextAlignment(Qt.AlignCenter)
        #Layout
        self.setItem(0, 0, self._names)
        self.setItem(0, 1, self._values)
        self.setItem(1, 0, self.INIT_CONC_VE)
        self.setCellWidget(1, 1, self.INIT_CONC_VE_data)
        self.setItem(2, 0, self.KW_VE)
        self.setCellWidget(2, 1, self.KW_VE_data)
        self.setItem(3, 0, self.D_VE)
        self.setCellWidget(3, 1, self.D_VE_data)
        self.setItem(4, 0, self.VE_comp0)
        self.setCellWidget(4, 1, self.VE_comp0_data)
        self.setItem(5, 0, self.VE_comp1)
        self.setCellWidget(5, 1, self.VE_comp1_data)
        self.setItem(6, 0, self.VE_comp2)
        self.setCellWidget(6, 1, self.VE_comp2_data)
        self.setItem(7, 0, self.VE_comp3)
        self.setCellWidget(7,1, self.VE_comp3_data)
        self.setItem(8, 0, self.VE_comp4)
        self.setCellWidget(8, 1, self.VE_comp4_data)
        self.setItem(9, 0, self.tips)
        self.setSpan(9, 0, 1, 2)
        self.setCellWidget(10, 0, self.button1)
        self.setCellWidget(10, 1, self.button2)
        #Signals
        self.button1.clicked.connect(self.commit)
        self.button2.clicked.connect(self.abandon)
        self._parent = parent
    #
    def showVE(self,showdata):
        self._parent.maintablelayout.setCurrentWidget(self)
        self._projData = showdata
        self.INIT_CONC_VE_data.setText(showdata.INIT_CONC_VE.iat[0])
        self.KW_VE_data.setText(showdata.KW_VE.iat[0])
        self.D_VE_data.setText(showdata.D_VE.iat[0])
        self.VE_comp0_data.setText(showdata.COMP_VE.iat[0])
        self.VE_comp1_data.setText(showdata.COMP_VE.iat[1])
        self.VE_comp2_data.setText(showdata.COMP_VE.iat[2])
        self.VE_comp3_data.setText(showdata.COMP_VE.iat[3])
        self.VE_comp4_data.setText(showdata.COMP_VE.iat[4])
    #
    def commit(self):
        self._projData.INIT_CONC_VE.iat[0] = self.INIT_CONC_VE_data.text()
        self._projData.KW_VE.iat[0] = self.KW_VE_data.text()
        self._projData.D_VE.iat[0] = self.D_VE_data.text()
        self._projData.COMP_VE.iat[0] = self.VE_comp0_data.text()
        self._projData.COMP_VE.iat[1] = self.VE_comp1_data.text()
        self._projData.COMP_VE.iat[2] = self.VE_comp2_data.text()
        self._projData.COMP_VE.iat[3] = self.VE_comp3_data.text()
        self._projData.COMP_VE.iat[4] = self.VE_comp4_data.text()
        self.tips.setText('Successful commit')
    #
    def abandon(self):
        self.showVE(self._projData)
        self.tips.setText('Successful abandon')
#-------------------------------------------------------------------------------------------------------------
class Parameterviwer4(QTableWidget):
    def __init__(self,parent):
        super(Parameterviwer4, self).__init__(parent)
        self.setColumnCount(2)
        self.setRowCount(11)
        self._names = QTableWidgetItem('Name')
        self._names.setFlags(Qt.NoItemFlags)
        self._values = QTableWidgetItem('Value')
        self._values.setFlags(Qt.NoItemFlags)
        self.verticalHeader().setVisible(False)
        self.horizontalHeader().setVisible(False)
        self.horizontalHeader().setStretchLastSection(True)
        #Dermis
        self.INIT_CONC_DE = QTableWidgetItem('INIT_CONC_DE')
        self.INIT_CONC_DE.setFlags(Qt.NoItemFlags)
        self.INIT_CONC_DE_data = QLineEdit()
        self.KW_DE = QTableWidgetItem('KW_DE')
        self.KW_DE.setFlags(Qt.NoItemFlags)
        self.KW_DE_data = QLineEdit()
        self.D_DE = QTableWidgetItem('D_DE')
        self.D_DE.setFlags(Qt.NoItemFlags)
        self.D_DE_data = QLineEdit()
        self.DE_comp0 = QTableWidgetItem('ID_DE')
        self.DE_comp0.setFlags(Qt.NoItemFlags)
        self.DE_comp0_data = QLineEdit()
        self.DE_comp1 = QTableWidgetItem('N_LAYER_X_DE')
        self.DE_comp1.setFlags(Qt.NoItemFlags)
        self.DE_comp1_data = QLineEdit()
        self.DE_comp2 = QTableWidgetItem('N_LAYER_Y_DE')
        self.DE_comp2.setFlags(Qt.NoItemFlags)
        self.DE_comp2_data = QLineEdit()
        self.DE_comp3 = QTableWidgetItem('N_MESH_X_DE_LP')
        self.DE_comp3.setFlags(Qt.NoItemFlags)
        self.DE_comp3_data = QLineEdit()
        self.DE_comp4 = QTableWidgetItem('N_MESH_Y_DE_LP')
        self.DE_comp4.setFlags(Qt.NoItemFlags)
        self.DE_comp4_data = QLineEdit()
        #User's components
        self.button1 = QPushButton('Commit', self)
        self.button2 = QPushButton('Abandon', self)
        self.tips = QTableWidgetItem()
        self.tips.setFlags(Qt.NoItemFlags)
        self.tips.setTextAlignment(Qt.AlignCenter)
        #Layout
        self.setItem(0, 0, self._names)
        self.setItem(0, 1, self._values)
        self.setItem(1, 0, self.INIT_CONC_DE)
        self.setCellWidget(1, 1, self.INIT_CONC_DE_data)
        self.setItem(2, 0, self.KW_DE)
        self.setCellWidget(2, 1, self.KW_DE_data)
        self.setItem(3, 0, self.D_DE)
        self.setCellWidget(3, 1, self.D_DE_data)
        self.setItem(4, 0, self.DE_comp0)
        self.setCellWidget(4, 1, self.DE_comp0_data)
        self.setItem(5, 0, self.DE_comp1)
        self.setCellWidget(5, 1, self.DE_comp1_data)
        self.setItem(6, 0, self.DE_comp2)
        self.setCellWidget(6, 1, self.DE_comp2_data)
        self.setItem(7, 0, self.DE_comp3)
        self.setCellWidget(7,1, self.DE_comp3_data)
        self.setItem(8, 0, self.DE_comp4)
        self.setCellWidget(8, 1, self.DE_comp4_data)
        self.setItem(9, 0, self.tips)
        self.setSpan(9, 0, 1, 2)
        self.setCellWidget(10, 0, self.button1)
        self.setCellWidget(10, 1, self.button2)
        #Signals
        self.button1.clicked.connect(self.commit)
        self.button2.clicked.connect(self.abandon)
        self._parent = parent
    #
    def showDE(self,showdata):
        self._parent.maintablelayout.setCurrentWidget(self)
        self._projData = showdata
        self.INIT_CONC_DE_data.setText(showdata.INIT_CONC_DE.iat[0])
        self.KW_DE_data.setText(showdata.KW_DE.iat[0])
        self.D_DE_data.setText(showdata.D_DE.iat[0])
        self.DE_comp0_data.setText(showdata.COMP_DE.iat[0])
        self.DE_comp1_data.setText(showdata.COMP_DE.iat[1])
        self.DE_comp2_data.setText(showdata.COMP_DE.iat[2])
        self.DE_comp3_data.setText(showdata.COMP_DE.iat[3])
        self.DE_comp4_data.setText(showdata.COMP_DE.iat[4])
    #
    def commit(self):
        self._projData.INIT_CONC_DE.iat[0] = self.INIT_CONC_DE_data.text()
        self._projData.KW_DE.iat[0] = self.KW_DE_data.text()
        self._projData.D_DE.iat[0] = self.D_DE_data.text()
        self._projData.COMP_DE.iat[0] = self.DE_comp0_data.text()
        self._projData.COMP_DE.iat[1] = self.DE_comp1_data.text()
        self._projData.COMP_DE.iat[2] = self.DE_comp2_data.text()
        self._projData.COMP_DE.iat[3] = self.DE_comp3_data.text()
        self._projData.COMP_DE.iat[4] = self.DE_comp4_data.text()
        self.tips.setText('Successful commit')
    #
    def abandon(self):
        self.showDE(self._projData)
        self.tips.setText('Successful abandon')
#-------------------------------------------------------------------------------------------------------------
class Parameterviwer5(QTableWidget):
    def __init__(self,parent):
        super(Parameterviwer5, self).__init__(parent)
        self.setColumnCount(2)
        self.setRowCount(11)
        self._names = QTableWidgetItem('Name')
        self._names.setFlags(Qt.NoItemFlags)
        self._values = QTableWidgetItem('Value')
        self._values.setFlags(Qt.NoItemFlags)
        self.verticalHeader().setVisible(False)
        self.horizontalHeader().setVisible(False)
        self.horizontalHeader().setStretchLastSection(True)
        #Hypodermis
        self.INIT_CONC_HF = QTableWidgetItem('INIT_CONC_HF')
        self.INIT_CONC_HF.setFlags(Qt.NoItemFlags)
        self.INIT_CONC_HF_data = QLineEdit()
        self.KW_HF = QTableWidgetItem('KW_HF')
        self.KW_HF.setFlags(Qt.NoItemFlags)
        self.KW_HF_data = QLineEdit()
        self.D_HF = QTableWidgetItem('D_HF')
        self.D_HF.setFlags(Qt.NoItemFlags)
        self.D_HF_data = QLineEdit()
        self.HF_comp0 = QTableWidgetItem('ID_HF')
        self.HF_comp0.setFlags(Qt.NoItemFlags)
        self.HF_comp0_data = QLineEdit()
        self.HF_comp1 = QTableWidgetItem('N_LAYER_X_HF')
        self.HF_comp1.setFlags(Qt.NoItemFlags)
        self.HF_comp1_data = QLineEdit()
        self.HF_comp2 = QTableWidgetItem('N_LAYER_Y_HF')
        self.HF_comp2.setFlags(Qt.NoItemFlags)
        self.HF_comp2_data = QLineEdit()
        self.HF_comp3 = QTableWidgetItem('N_MESH_X_HF_LP')
        self.HF_comp3.setFlags(Qt.NoItemFlags)
        self.HF_comp3_data = QLineEdit()
        self.HF_comp4 = QTableWidgetItem('N_MESH_Y_HF_LP')
        self.HF_comp4.setFlags(Qt.NoItemFlags)
        self.HF_comp4_data = QLineEdit()
        #User's components
        self.button1 = QPushButton('Commit', self)
        self.button2 = QPushButton('Abandon', self)
        self.tips = QTableWidgetItem()
        self.tips.setFlags(Qt.NoItemFlags)
        self.tips.setTextAlignment(Qt.AlignCenter)
        #Layout
        self.setItem(0, 0, self._names)
        self.setItem(0, 1, self._values)
        self.setItem(1, 0, self.INIT_CONC_HF)
        self.setCellWidget(1, 1, self.INIT_CONC_HF_data)
        self.setItem(2, 0, self.KW_HF)
        self.setCellWidget(2, 1, self.KW_HF_data)
        self.setItem(3, 0, self.D_HF)
        self.setCellWidget(3, 1, self.D_HF_data)
        self.setItem(4, 0, self.HF_comp0)
        self.setCellWidget(4, 1, self.HF_comp0_data)
        self.setItem(5, 0, self.HF_comp1)
        self.setCellWidget(5, 1, self.HF_comp1_data)
        self.setItem(6, 0, self.HF_comp2)
        self.setCellWidget(6, 1, self.HF_comp2_data)
        self.setItem(7, 0, self.HF_comp3)
        self.setCellWidget(7,1, self.HF_comp3_data)
        self.setItem(8, 0, self.HF_comp4)
        self.setCellWidget(8, 1, self.HF_comp4_data)
        self.setItem(9, 0, self.tips)
        self.setSpan(9, 0, 1, 2)
        self.setCellWidget(10, 0, self.button1)
        self.setCellWidget(10, 1, self.button2)
        #Signals
        self.button1.clicked.connect(self.commit)
        self.button2.clicked.connect(self.abandon)
        self._parent = parent
    #
    def showHF(self,showdata):
        self._parent.maintablelayout.setCurrentWidget(self)
        self._projData = showdata
        self.INIT_CONC_HF_data.setText(showdata.INIT_CONC_HF.iat[0])
        self.KW_HF_data.setText(showdata.KW_HF.iat[0])
        self.D_HF_data.setText(showdata.D_HF.iat[0])
        self.HF_comp0_data.setText(showdata.COMP_HF.iat[0])
        self.HF_comp1_data.setText(showdata.COMP_HF.iat[1])
        self.HF_comp2_data.setText(showdata.COMP_HF.iat[2])
        self.HF_comp3_data.setText(showdata.COMP_HF.iat[3])
        self.HF_comp4_data.setText(showdata.COMP_HF.iat[4])
    #
    def commit(self):
        self._projData.INIT_CONC_HF.iat[0] = self.INIT_CONC_HF_data.text()
        self._projData.KW_HF.iat[0] = self.KW_HF_data.text()
        self._projData.D_HF.iat[0] = self.D_HF_data.text()
        self._projData.COMP_HF.iat[0] = self.HF_comp0_data.text()
        self._projData.COMP_HF.iat[1] = self.HF_comp1_data.text()
        self._projData.COMP_HF.iat[2] = self.HF_comp2_data.text()
        self._projData.COMP_HF.iat[3] = self.HF_comp3_data.text()
        self._projData.COMP_HF.iat[4] = self.HF_comp4_data.text()
        self.tips.setText('Successful commit')
    #
    def abandon(self):
        self.showHF(self._projData)
        self.tips.setText('Successful abandon')
#-------------------------------------------------------------------------------------------------------------
class Parameterviwer6(QTableWidget):
    def __init__(self,parent):
        super(Parameterviwer6, self).__init__(parent)
        self.setColumnCount(2)
        self.setRowCount(11)
        self._names = QTableWidgetItem('Name')
        self._names.setFlags(Qt.NoItemFlags)
        self._values = QTableWidgetItem('Value')
        self._values.setFlags(Qt.NoItemFlags)
        self.verticalHeader().setVisible(False)
        self.horizontalHeader().setVisible(False)
        self.horizontalHeader().setStretchLastSection(True)
        #BloodFlow
        self.INIT_CONC_BD = QTableWidgetItem('INIT_CONC_BD')
        self.INIT_CONC_BD.setFlags(Qt.NoItemFlags)
        self.INIT_CONC_BD_data = QLineEdit()
        self.K_DE2BD = QTableWidgetItem('K_DE2BD')
        self.K_DE2BD.setFlags(Qt.NoItemFlags)
        self.K_DE2BD_data = QLineEdit()
        self.CLEAR_BD = QTableWidgetItem('CLEAR_BD')
        self.CLEAR_BD.setFlags(Qt.NoItemFlags)
        self.CLEAR_BD_data = QLineEdit()
        self.BD_comp0 = QTableWidgetItem('ID_BD')
        self.BD_comp0.setFlags(Qt.NoItemFlags)
        self.BD_comp0_data = QLineEdit()
        self.BD_comp1 = QTableWidgetItem('N_LAYER_X_BD')
        self.BD_comp1.setFlags(Qt.NoItemFlags)
        self.BD_comp1_data = QLineEdit()
        self.BD_comp2 = QTableWidgetItem('N_LAYER_Y_BD')
        self.BD_comp2.setFlags(Qt.NoItemFlags)
        self.BD_comp2_data = QLineEdit()
        self.BD_comp3 = QTableWidgetItem('N_MESH_X_BD_LP')
        self.BD_comp3.setFlags(Qt.NoItemFlags)
        self.BD_comp3_data = QLineEdit()
        self.BD_comp4 = QTableWidgetItem('N_MESH_Y_BD_LP')
        self.BD_comp4.setFlags(Qt.NoItemFlags)
        self.BD_comp4_data = QLineEdit()
        #User's components
        self.button1 = QPushButton('Commit', self)
        self.button2 = QPushButton('Abandon', self)
        self.tips = QTableWidgetItem()
        self.tips.setFlags(Qt.NoItemFlags)
        self.tips.setTextAlignment(Qt.AlignCenter)
        #Layout
        self.setItem(0, 0, self._names)
        self.setItem(0, 1, self._values)
        self.setItem(1, 0, self.INIT_CONC_BD)
        self.setCellWidget(1, 1, self.INIT_CONC_BD_data)
        self.setItem(2, 0, self.K_DE2BD)
        self.setCellWidget(2, 1, self.K_DE2BD_data)
        self.setItem(3, 0, self.CLEAR_BD)
        self.setCellWidget(3, 1, self.CLEAR_BD_data)
        self.setItem(4, 0, self.BD_comp0)
        self.setCellWidget(4, 1, self.BD_comp0_data)
        self.setItem(5, 0, self.BD_comp1)
        self.setCellWidget(5, 1, self.BD_comp1_data)
        self.setItem(6, 0, self.BD_comp2)
        self.setCellWidget(6, 1, self.BD_comp2_data)
        self.setItem(7, 0, self.BD_comp3)
        self.setCellWidget(7,1, self.BD_comp3_data)
        self.setItem(8, 0, self.BD_comp4)
        self.setCellWidget(8, 1, self.BD_comp4_data)
        self.setItem(9, 0, self.tips)
        self.setSpan(9, 0, 1, 2)
        self.setCellWidget(10, 0, self.button1)
        self.setCellWidget(10, 1, self.button2)
        #Signals
        self.button1.clicked.connect(self.commit)
        self.button2.clicked.connect(self.abandon)
        self._parent = parent
    #
    def showBD(self,showdata):
        self._parent.maintablelayout.setCurrentWidget(self)
        self._projData = showdata
        self.INIT_CONC_BD_data.setText(showdata.INIT_CONC_BD.iat[0])
        self.K_DE2BD_data.setText(showdata.K_DE2BD.iat[0])
        self.CLEAR_BD_data.setText(showdata.CLEAR_BD.iat[0])
        self.BD_comp0_data.setText(showdata.COMP_BD.iat[0])
        self.BD_comp1_data.setText(showdata.COMP_BD.iat[1])
        self.BD_comp2_data.setText(showdata.COMP_BD.iat[2])
        self.BD_comp3_data.setText(showdata.COMP_BD.iat[3])
        self.BD_comp4_data.setText(showdata.COMP_BD.iat[4])
    #
    def commit(self):
        self._projData.INIT_CONC_BD.iat[0] = self.INIT_CONC_BD_data.text()
        self._projData.K_DE2BD.iat[0] = self.K_DE2BD_data.text()
        self._projData.CLEAR_BD.iat[0] = self.CLEAR_BD_data.text()
        self._projData.COMP_BD.iat[0] = self.BD_comp0_data.text()
        self._projData.COMP_BD.iat[1] = self.BD_comp1_data.text()
        self._projData.COMP_BD.iat[2] = self.BD_comp2_data.text()
        self._projData.COMP_BD.iat[3] = self.BD_comp3_data.text()
        self._projData.COMP_BD.iat[4] = self.BD_comp4_data.text()
        self.tips.setText('Successful commit')
    #
    def abandon(self):
        self.showBD(self._projData)
        self.tips.setText('Successful abandon')
#-------------------------------------------------------------------------------------------------------------
class MyCanvas(QWidget):
    def __init__(self,parent=None):
        super(MyCanvas, self).__init__(parent)
        self.dpi = 100
        self.fig = Figure(figsize=(5.0, 4.0),dpi=self.dpi) #width=5, height=4
        self.canvas = FigureCanvas(self.fig) #传入一个Figure类
        self.canvas.setParent(self)
        self.axes = self.fig.add_subplot(1,1,1)
        #其实下面这个用法要提供一个事件类型，就好像某QWidget.clicked.connect()中的clicked，声明触发类型！
        #self.canvas.mpl_connect() #第一个参数是内置事件类型，第二个参数是连接的函数（相当于重写“某事件函数”）。
        #matplotlib.backend_bases.Event(name, canvas, guiEvent=None) #某个guiEvent触发自定义的matplotlib事件
        self.mpl_toolbar = NavigationToolbar(self.canvas, self) #控制相应的FigureCanvas！并且指定父窗口
        mainlayout = QVBoxLayout(self)
        mainlayout.addWidget(self.mpl_toolbar)
        mainlayout.addWidget(self.canvas)
        self.setLayout(mainlayout)
#-------------------------------------------------------------------------------------------------------------
class SurreyWindow(QMainWindow):
    def __init__(self,parent=None):
        super(SurreyWindow,self).__init__(parent)
        # QTableWidget
        self.tableviewer0 = Parameterviwer0(self)
        self.tableviewer1 = Parameterviwer1(self)
        self.tableviewer2 = Parameterviwer2(self)
        self.tableviewer3 = Parameterviwer3(self)
        self.tableviewer4 = Parameterviwer4(self)
        self.tableviewer5 = Parameterviwer5(self)
        self.tableviewer6 = Parameterviwer6(self)
        self.blankwidget = QTableWidget(self) #To initially make the table blank
        self.maintablelayout = QStackedLayout(self)
        self.maintablelayout.addWidget(self.tableviewer0)
        self.maintablelayout.addWidget(self.tableviewer1)
        self.maintablelayout.addWidget(self.tableviewer2)
        self.maintablelayout.addWidget(self.tableviewer3)
        self.maintablelayout.addWidget(self.tableviewer4)
        self.maintablelayout.addWidget(self.tableviewer5)
        self.maintablelayout.addWidget(self.tableviewer6)
        self.maintablelayout.addWidget(self.blankwidget)
        self.maintablelayout.setCurrentWidget(self.blankwidget)
        # QTreeWidget
        self.projectview = Projectviwer(self)
        self.projectview.sendChemical.connect(self.tableviewer0.showchemical)
        self.projectview.sendVH.connect(self.tableviewer1.showVH)
        self.projectview.sendSC.connect(self.tableviewer2.showSC)
        self.projectview.sendVE.connect(self.tableviewer3.showVE)
        self.projectview.sendDE.connect(self.tableviewer4.showDE)
        self.projectview.sendHF.connect(self.tableviewer5.showHF)
        self.projectview.sendBD.connect(self.tableviewer6.showBD)
        # Result
        self.resultviewer1 = QTextBrowser() #显示运行过程中的一些东西
        self.resultviewer2 = MyCanvas(self)
        self.mainresultlayout = QStackedLayout(self)
        self.mainresultlayout.addWidget(self.resultviewer1)
        self.mainresultlayout.addWidget(self.resultviewer2)
        self.mainresultlayout.setCurrentWidget(self.resultviewer2)
        # Mainwindow Layout
        self.mainwindow=QWidget(self) #应用程序主窗口
        self.mainlayout=QHBoxLayout(self)
        self.mainlayout.addWidget(self.projectview)
        self.mainlayout.addLayout(self.maintablelayout)
        self.mainlayout.addLayout(self.mainresultlayout)
        self.mainlayout.setStretchFactor(self.projectview, 1)#原本以为设置组件的宽度，用了一晚
        self.mainlayout.setStretchFactor(self.maintablelayout, 1)
        self.mainlayout.setStretchFactor(self.mainresultlayout, 3)
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
        self.resize(1024,640)
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
        #print(self.tableviewer0.CHEM_NO_data.text()=='') #QLineEdit.text()返回'str'。当输入框什么都没有时，结果为True
        #print(self.openproject._projData.isnull()) #如果输入框里面有东西且commit了，对应的位置判断为False!而非True
        #print(self.newproject._projData.CHEM_NO.isnull().all()) #注释在下一行
        #只要在QLineEdit键入过东西，即使全部删除了也不再是None了，而是空字符串。此时用isnull来判断的结果是False
        pass

    #重新定义应用程序的closeEvent方法
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
        self.move( (screen.width()-size.width())/2, \
                   (screen.height()-size.height())/2)

#-----------------------------------------------------------------------------------------------------------
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

# ------------------------------------------------------------------------------------------------------------
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
        #默认显示出所有数据。因为新建的工程，你并不知道对方会用哪些数据！
        self._dict1 = {
            'COMPARTMENT_SETUP': pd.Series(['V,S,E,D,H']),
            'COMP_VH': pd.Series(['', '', '', '', '']),
            'COMP_SC': pd.Series(['', '', '', '', ''], dtype='str'),
            'COMP_VE': pd.Series(['', '', '', '', ''], dtype='str'),
            'COMP_DE': pd.Series(['', '', '', '', ''], dtype='str'),
            'COMP_HF': pd.Series(['', '', '', '', ''], dtype='str'),
            'COMP_BD': pd.Series(['', '', '', '', ''], dtype='str'),
            'CHEM_NO': pd.Series([''], dtype='str'),
            'CHEM_MW': pd.Series([''], dtype='str'),
            'CHEM_KOW': pd.Series([''], dtype='str'),
            'CHEM_PKA': pd.Series([''], dtype='str'),
            'CHEM_NONION': pd.Series([''], dtype='str'),
            'CHEM_UNBND': pd.Series([''], dtype='str'),
            'CHEM_ACIDBASE': pd.Series([''], dtype='str'),
            'CHEM_DENSITY': pd.Series([''], dtype='str'),
            'CHEM_PHASE': pd.Series([''], dtype='str'),
            'INFINITE_VH': pd.Series([''], dtype='str'),
            'AREA_VH': pd.Series([''], dtype='str'),
            'EVAP_SOLVENT_VH': pd.Series([''], dtype='str'),
            'EVAP_SOLUTE_VH': pd.Series([''], dtype='str'),
            'SOLVENT_MW': pd.Series([''], dtype='str'),
            'SOLUBILITY_VH': pd.Series([''], dtype='str'),
            'SOLVENT_DENSITY': pd.Series([''], dtype='str'),
            'INIT_CONC_VH': pd.Series([''], dtype='str'),
            'INIT_CONC_SC': pd.Series([''], dtype='str'),
            'INIT_CONC_VE': pd.Series([''], dtype='str'),
            'INIT_CONC_DE': pd.Series([''], dtype='str'),
            'INIT_CONC_HF': pd.Series([''], dtype='str'),
            'INIT_CONC_BD': pd.Series([''], dtype='str'),
            'KW_VH': pd.Series([''], dtype='str'),
            'D_VH': pd.Series([''], dtype='str'),
            'KW_SC': pd.Series([''], dtype='str'),
            'D_SC': pd.Series([''], dtype='str'),
            'KW_VE': pd.Series([''], dtype='str'),
            'D_VE': pd.Series([''], dtype='str'),
            'KW_DE': pd.Series([''], dtype='str'),
            'D_DE': pd.Series([''], dtype='str'),
            'KW_HF': pd.Series([''], dtype='str'),
            'D_HF': pd.Series([''], dtype='str'),
            'K_DE2BD': pd.Series([''], dtype='str'),
            'CLEAR_BD': pd.Series([''], dtype='str')
        }
        self._projData=pd.DataFrame(self._dict1)
        self.cols = list(self._projData) #得到列索引，想让数据结构按照COMPARTMENT_SETUP在最前面的方式排序，...
        self.cols.insert(0, self.cols.pop(self.cols.index('COMPARTMENT_SETUP')))
        self.cols.insert(1, self.cols.pop(self.cols.index('COMP_VH')))
        self.cols.insert(2, self.cols.pop(self.cols.index('COMP_SC')))
        self.cols.insert(3, self.cols.pop(self.cols.index('COMP_VE')))
        self.cols.insert(4, self.cols.pop(self.cols.index('COMP_DE')))
        self.cols.insert(5, self.cols.pop(self.cols.index('COMP_HF')))
        self.cols.insert(6, self.cols.pop(self.cols.index('COMP_BD')))
        self._projData = self._projData.loc[:, self.cols]
        #默认数据代表“某一层不使用”，loaddata函数需要
        #内部核心数据--------------------------------------------------------
        self._parent = parent # parent在原来中是self.projectview
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
                    #lin = list( filter(lambda x:x!='NaN', lin)) #去掉NaN数据
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
                # print('loaddata-COMP sucess')
            elif self._dict2[tokens[1]] == 'E':
                self._projData.COMP_VE = tokens[1:6]
            elif self._dict2[tokens[1]] == 'D':
                self._projData.COMP_DE = tokens[1:6]
                # print(self._projData.COMP_DE)
            elif self._dict2[tokens[1]] == 'H':
                self._projData.COMP_HF = tokens[1:]
                # print(self._projData.COMP_HF)
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
        #Vehicle settings
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
            return
    #
    def saveproject(self):
        # self.newprojectPath=QFileDialog.getSaveFileName(self,'Create Project','.','Project File (*.cfg)') #如果自己键入.txt的话，会代替.cfg的！
        # self.newproject_name=os.path.split(os.path.splitext(self.newprojectPath)[0])[1]
        self.saveprojectPath = QFileDialog.getExistingDirectory(self._parent, 'Save your project')  # 返回一个绝对路径
        if self.saveprojectPath:
            self.cfg_name,self.cfg_ok = QInputDialog.getText(self._parent, 'New cfg file', 'Enter cfg-file name: ')
            if self.cfg_ok and bool(self.cfg_name):
                if os.name == 'nt':
                    self.saveprojectPath = self.saveprojectPath.replace('/', '\\')

                self.saveprojectPath_config = os.path.join(self.saveprojectPath, 'config') #config文件夹路径
                if not os.path.exists(self.saveprojectPath_config):
                    os.mkdir(self.saveprojectPath_config)
                self.saveprojectPath_simu = os.path.join(self.saveprojectPath, 'simu') #simu文件夹路径
                if not os.path.exists(self.saveprojectPath_simu):  # 防止Bug
                    os.mkdir(self.saveprojectPath_simu)
                self.saveproject_configPath = os.path.join(self.saveprojectPath_config, self.cfg_name+'.cfg') #cfg文件路径
                #print(self.saveproject_configPath)
                #保存前的数据整理
                saveData = pd.DataFrame()
                for i in self._projData:
                    if self._projData[i].iat[0]!='':
                        saveData[i]=self._projData[i] #自动添加列，也自动地过滤不需要的列
                saveData.rename(columns={'COMP_VH': 'COMP', 'COMP_SC': 'COMP', 'COMP_VE': 'COMP', 'COMP_DE': 'COMP',
                                         'COMP_HF': 'COMP', 'COMP_BD': 'COMP'}).T.to_csv(self.saveproject_configPath,sep=' ',header=False)

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
        elif self.VH_setting0.isSelected():
            self._parent.sendVH.emit(self._projData)
        elif self.SC_setting0.isSelected():
            self._parent.sendSC.emit(self._projData)
            print(2)
        elif self.VE_setting0.isSelected():
            self._parent.sendVE.emit(self._projData)
            print(3)
        elif self.DE_setting0.isSelected():
            self._parent.sendDE.emit(self._projData)
            print(4)
        elif self.HF_setting0.isSelected():
            self._parent.sendHF.emit(self._projData)
            print(5)
        elif self.BD_setting0.isSelected():
            self._parent.sendBD.emit(self._projData)
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