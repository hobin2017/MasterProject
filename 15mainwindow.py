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
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas # subclass of the QWidget class
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar # subclass of the QWidget class
from matplotlib.figure import Figure
import pandas as pd
#from multiprocessing import Process
from threading import Thread
import os
import sys
#for simulation--------------------------------------------------------------------------------------------
from core.compDPK_hobin import compDPK
# -------------------------------------------------------------------------------------------------------
class Projectviewer(QTreeWidget):
    sendChemical = pyqtSignal(object)
    sendVH = pyqtSignal(object)
    sendSC = pyqtSignal(object)
    sendVE = pyqtSignal(object)
    sendDE = pyqtSignal(object)
    sendHF = pyqtSignal(object)
    sendBD = pyqtSignal(object)

    def __init__(self,parent=None):
        super(Projectviewer, self).__init__(parent) # The parent is SurreyWindow class
        self.setColumnCount(1)
        self.setHeaderLabel('Project')
        #self.setColumnWidth(0, 1) # First one is column number；Second one is width
        #self._parent=parent # Might be used in future
        #self.setContextMenuPolicy(Qt.CustomContextMenu) #It will make contextMenuEvent unavailable
        #self.customContextMenuRequested.connect()

    def closeProject(self):
        #self.index_pro=self.indexOfTopLevelItem(self.currentItem().parent())
        self.index_pro = self.indexOfTopLevelItem(self.currentItem())
        self.takeTopLevelItem(self.index_pro)

    def contextMenuEvent(self, event):
        # If the current item is not the TopLevelItem,the index is -1.
        if not self.indexOfTopLevelItem(self.currentItem()) == -1:
            self.contextmenu = QMenu(self)
            oneAction = self.contextmenu.addAction('Close Project')
            oneAction.triggered.connect(self.closeProject)
            twoAction = self.contextmenu.addAction('Save Project')
            twoAction.triggered.connect(self.currentItem().saveproject)
            if self.currentItem().childCount()==0:
                threeAction = self.contextmenu.addAction('Compartment Setup')
                threeAction.triggered.connect(self.currentItem().configure) # the function belongs to ProjectItem
            self.contextmenu.exec_(event.globalPos()) # The argument is the location of the mouse
# -------------------------------------------------------------------------------------------------------
class Parameterviewer0(QTableWidget):
    def __init__(self,parent):
        super(Parameterviewer0,self).__init__(parent)
        self.setColumnCount(2)
        self.setRowCount(12)
        self.verticalHeader().setVisible(False)
        self.horizontalHeader().setVisible(False)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # self.horizontalHeader().setStretchLastSection(True)
        self._names = QTableWidgetItem('Name')
        self._names.setFlags(Qt.NoItemFlags) #Not editable
        self._values = QTableWidgetItem('Value')
        self._values.setFlags(Qt.NoItemFlags)
        #Properties of chemical, total: 9
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
        # Signals connection
        self.button1.clicked.connect(self.commit)
        self.button2.clicked.connect(self.abandon)
        # Restriction on QLineEdit
        self.CHEM_NO_data.setValidator(QIntValidator(bottom=0, top=999, parent=self))
        self.CHEM_MW_data.setValidator(QDoubleValidator(bottom=0.0, top=9999.99,parent=self))
        self.CHEM_KOW_data.setValidator(QDoubleValidator(bottom=0.0, top=999.99,parent=self))
        self.CHEM_PKA_data.setValidator(QDoubleValidator(parent=self))
        self.CHEM_NONION_data.setValidator(QDoubleValidator(bottom=0,top=999.99,parent=self))
        self.CHEM_UNBND_data.setValidator(QDoubleValidator(bottom=0,top=999.99,parent=self))
        self.CHEM_ACIDBASE_data.setValidator(QRegularExpressionValidator(QRegularExpression(r'[A-Z]+'),self))
        self.CHEM_DENSITY_data.setValidator(QDoubleValidator(bottom=0,top=99999.99,parent=self))
        self.CHEM_PHASE_data.setValidator(QRegularExpressionValidator(QRegularExpression(r'[A-Z]+'),self))
        # Tips in the QLineEdit
        self.CHEM_ACIDBASE_data.setWhatsThis('Please enter upper case letter')
        self.CHEM_PHASE_data.setWhatsThis('Please enter upper case letter') #focus on this widget, then press SHIFT+F1
        self._parent = parent

    def showchemical(self, showdata):
        self._parent.maintablelayout.setCurrentWidget(self)
        # It is not a copy of project data. If a=[10,9];b=a;b[0]=0，then a will be [0,9] (is not [10,9]).
        self._projData = showdata #It will be used in the commit funciton.
        self.CHEM_NO_data.setText(showdata.CHEM_NO.iat[0])
        self.CHEM_MW_data.setText(showdata.CHEM_MW.iat[0])
        self.CHEM_KOW_data.setText(showdata.CHEM_KOW.iat[0])
        self.CHEM_PKA_data.setText(showdata.CHEM_PKA.iat[0])
        self.CHEM_NONION_data.setText(showdata.CHEM_NONION.iat[0])
        self.CHEM_UNBND_data.setText(showdata.CHEM_UNBND.iat[0])
        self.CHEM_ACIDBASE_data.setText(showdata.CHEM_ACIDBASE.iat[0])
        self.CHEM_DENSITY_data.setText(showdata.CHEM_DENSITY.iat[0])
        self.CHEM_PHASE_data.setText(showdata.CHEM_PHASE.iat[0])

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

    def abandon(self):
        self.showchemical(self._projData)
        self.tips.setText('Successful abandon')
#-------------------------------------------------------------------------------------------------------------
class Parameterviewer1(QTableWidget):
    def __init__(self, parent):
        super(Parameterviewer1, self).__init__(parent)
        self.setColumnCount(2)
        self.setRowCount(18)
        self.verticalHeader().setVisible(False)
        self.horizontalHeader().setVisible(False)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        #self.horizontalHeader().setStretchLastSection(True)
        self._names = QTableWidgetItem('Name')
        self._names.setFlags(Qt.NoItemFlags)
        self._values = QTableWidgetItem('Value')
        self._values.setFlags(Qt.NoItemFlags)
        #Vehicle setting, total:15
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
        #Restriction on QLineEdit
        checker1 = QDoubleValidator(parent=self)
        self.INFINITE_VH_data.setValidator(QIntValidator(bottom=0,top=1,parent=self))
        self.AREA_VH_data.setValidator(checker1)
        self.INIT_CONC_VH_data.setValidator(checker1)
        self.KW_VH_data.setValidator(checker1)
        self.D_VH_data.setValidator(checker1)
        self.VH_comp0_data.setValidator(checker1)
        self.VH_comp1_data.setValidator(checker1)
        self.VH_comp2_data.setValidator(checker1)
        self.VH_comp3_data.setValidator(checker1)
        self.VH_comp4_data.setValidator(checker1)
        self.EVAP_SOLVENT_VH_data.setValidator(checker1)
        self.EVAP_SOLUTE_VH_data.setValidator(checker1)
        self.SOLVENT_MW_data.setValidator(checker1)
        self.SOLUBILITY_VH_data.setValidator(checker1)
        self.SOLVENT_DENSITY_data.setValidator(checker1)
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
class Parameterviewer2(QTableWidget):
    def __init__(self,parent):
        super(Parameterviewer2, self).__init__(parent)
        self.setColumnCount(2)
        self.setRowCount(11)
        self.verticalHeader().setVisible(False)
        self.horizontalHeader().setVisible(False)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        #self.horizontalHeader().setStretchLastSection(True)
        self._names = QTableWidgetItem('Name')
        self._names.setFlags(Qt.NoItemFlags)
        self._values = QTableWidgetItem('Value')
        self._values.setFlags(Qt.NoItemFlags)
        #Stratum corneum, total:8
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
        # Restrictions on QLineEdit
        checker2 = QDoubleValidator(parent=self)
        self.INIT_CONC_SC_data.setValidator(checker2)
        self.KW_SC_data.setValidator(checker2)
        self.D_SC_data.setValidator(checker2)
        self.SC_comp0_data.setValidator(checker2)
        self.SC_comp1_data.setValidator(checker2)
        self.SC_comp2_data.setValidator(checker2)
        self.SC_comp3_data.setValidator(checker2)
        self.SC_comp4_data.setValidator(checker2)
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
class Parameterviewer3(QTableWidget):
    def __init__(self,parent):
        super(Parameterviewer3, self).__init__(parent)
        self.setColumnCount(2)
        self.setRowCount(11)
        self.verticalHeader().setVisible(False)
        self.horizontalHeader().setVisible(False)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        #self.horizontalHeader().setStretchLastSection(True)
        self._names = QTableWidgetItem('Name')
        self._names.setFlags(Qt.NoItemFlags)
        self._values = QTableWidgetItem('Value')
        self._values.setFlags(Qt.NoItemFlags)
        #Viable epidermis, total: 8
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
        # Restrctions
        checker3 = QDoubleValidator(parent=self)
        self.INIT_CONC_VE_data.setValidator(checker3)
        self.KW_VE_data.setValidator(checker3)
        self.D_VE_data.setValidator(checker3)
        self.VE_comp0_data.setValidator(checker3)
        self.VE_comp1_data.setValidator(checker3)
        self.VE_comp2_data.setValidator(checker3)
        self.VE_comp3_data.setValidator(checker3)
        self.VE_comp4_data.setValidator(checker3)
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
class Parameterviewer4(QTableWidget):
    def __init__(self,parent):
        super(Parameterviewer4, self).__init__(parent)
        self.setColumnCount(2)
        self.setRowCount(11)
        self.verticalHeader().setVisible(False)
        self.horizontalHeader().setVisible(False)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        #self.horizontalHeader().setStretchLastSection(True)
        self._names = QTableWidgetItem('Name')
        self._names.setFlags(Qt.NoItemFlags)
        self._values = QTableWidgetItem('Value')
        self._values.setFlags(Qt.NoItemFlags)
        #Dermis, total:8
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
        #Restrictions
        checker4 = QDoubleValidator(parent=self)
        self.INIT_CONC_DE_data.setValidator(checker4)
        self.KW_DE_data.setValidator(checker4)
        self.D_DE_data.setValidator(checker4)
        self.DE_comp0_data.setValidator(checker4)
        self.DE_comp1_data.setValidator(checker4)
        self.DE_comp2_data.setValidator(checker4)
        self.DE_comp3_data.setValidator(checker4)
        self.DE_comp4_data.setValidator(checker4)
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
class Parameterviewer5(QTableWidget):
    def __init__(self,parent):
        super(Parameterviewer5, self).__init__(parent)
        self.setColumnCount(2)
        self.setRowCount(11)
        self.verticalHeader().setVisible(False)
        self.horizontalHeader().setVisible(False)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        #self.horizontalHeader().setStretchLastSection(True)
        self._names = QTableWidgetItem('Name')
        self._names.setFlags(Qt.NoItemFlags)
        self._values = QTableWidgetItem('Value')
        self._values.setFlags(Qt.NoItemFlags)
        #Hypodermis, total:8
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
        #restrictions
        checker5 = QDoubleValidator(parent=self)
        self.INIT_CONC_HF_data.setValidator(checker5)
        self.KW_HF_data.setValidator(checker5)
        self.D_HF_data.setValidator(checker5)
        self.HF_comp0_data.setValidator(checker5)
        self.HF_comp1_data.setValidator(checker5)
        self.HF_comp2_data.setValidator(checker5)
        self.HF_comp3_data.setValidator(checker5)
        self.HF_comp4_data.setValidator(checker5)
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
class Parameterviewer6(QTableWidget):
    def __init__(self,parent):
        super(Parameterviewer6, self).__init__(parent)
        self.setColumnCount(2)
        self.setRowCount(11)
        self.verticalHeader().setVisible(False)
        self.horizontalHeader().setVisible(False)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        #self.horizontalHeader().setStretchLastSection(True)
        self._names = QTableWidgetItem('Name')
        self._names.setFlags(Qt.NoItemFlags)
        self._values = QTableWidgetItem('Value')
        self._values.setFlags(Qt.NoItemFlags)
        #BloodFlow, total: 8
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
        # Restrictions
        checker6 = QDoubleValidator(parent=self)
        self.INIT_CONC_BD_data.setValidator(checker6)
        self.K_DE2BD_data.setValidator(checker6)
        self.CLEAR_BD_data.setValidator(checker6)
        self.BD_comp0_data.setValidator(checker6)
        self.BD_comp1_data.setValidator(checker6)
        self.BD_comp2_data.setValidator(checker6)
        self.BD_comp3_data.setValidator(checker6)
        self.BD_comp4_data.setValidator(checker6)
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
        self.fig = Figure(figsize=(5.0, 4.0),dpi=100) #width=5, height=4
        self.axes = self.fig.add_subplot(1, 1, 1)  # showing the coordinate axis otherwise blank.
        self.canvas = FigureCanvas(self.fig) #subclass of the QWidget class
        self.canvas.setParent(self)
        #self.canvas.mpl_connect() #first argument is the type of event, second one is the function to be called
        #matplotlib.backend_bases.Event(name, canvas, guiEvent=None)#One guiEvent will call the self-defined event
        self.mpl_toolbar = NavigationToolbar(self.canvas, self) # to control corresponding FigureCanvas and set parents
        mainlayout = QVBoxLayout(self)
        mainlayout.addWidget(self.mpl_toolbar)
        mainlayout.addWidget(self.canvas)
        self.setLayout(mainlayout)
#-------------------------------------------------------------------------------------------------------------
class MyThread(Thread):
    def __init__(self,cfg_path):
        self.path = cfg_path
        super(MyThread, self).__init__()

    def run(self):
        compDPK('%s'%self.path)
#-------------------------------------------------------------------------------------------------------------
class SurreyWindow(QMainWindow):
    def __init__(self,parent=None):
        super(SurreyWindow,self).__init__(parent) # the child will rewrite the __init__ method of parent
        # Parameter interface(7 table widgets)
        self.tableviewer0 = Parameterviewer0(self)
        self.tableviewer1 = Parameterviewer1(self)
        self.tableviewer2 = Parameterviewer2(self)
        self.tableviewer3 = Parameterviewer3(self)
        self.tableviewer4 = Parameterviewer4(self)
        self.tableviewer5 = Parameterviewer5(self)
        self.tableviewer6 = Parameterviewer6(self)
        self.blanktable = QTableWidget(self) #To initially make the table blank
        self.maintablelayout = QStackedLayout(self)
        self.maintablelayout.addWidget(self.tableviewer0)
        self.maintablelayout.addWidget(self.tableviewer1)
        self.maintablelayout.addWidget(self.tableviewer2)
        self.maintablelayout.addWidget(self.tableviewer3)
        self.maintablelayout.addWidget(self.tableviewer4)
        self.maintablelayout.addWidget(self.tableviewer5)
        self.maintablelayout.addWidget(self.tableviewer6)
        self.maintablelayout.addWidget(self.blanktable)
        self.maintablelayout.setCurrentWidget(self.blanktable)
        # Project interface (one tree widget)
        self.projectview = Projectviewer(self)
        self.projectview.sendChemical.connect(self.tableviewer0.showchemical)
        self.projectview.sendVH.connect(self.tableviewer1.showVH)
        self.projectview.sendSC.connect(self.tableviewer2.showSC)
        self.projectview.sendVE.connect(self.tableviewer3.showVE)
        self.projectview.sendDE.connect(self.tableviewer4.showDE)
        self.projectview.sendHF.connect(self.tableviewer5.showHF)
        self.projectview.sendBD.connect(self.tableviewer6.showBD)
        # Result interface (one canvas + one text browser)
        self.resultviewer1 = QTextBrowser()
        self.resultviewer2 = MyCanvas(self)
        self.mainresultlayout = QStackedLayout(self)
        self.mainresultlayout.addWidget(self.resultviewer1)
        self.mainresultlayout.addWidget(self.resultviewer2)
        self.mainresultlayout.setCurrentWidget(self.resultviewer2)
        # Mainwindow Layout
        self.mainwindow=QWidget(self) # The main layout
        self.mainlayout=QHBoxLayout(self)
        self.mainlayout.addWidget(self.projectview)
        self.mainlayout.addLayout(self.maintablelayout)
        self.mainlayout.addLayout(self.mainresultlayout)
        self.mainlayout.setStretchFactor(self.projectview, 1)# Using the fixed width of widgets? No!
        self.mainlayout.setStretchFactor(self.maintablelayout, 1)
        self.mainlayout.setStretchFactor(self.mainresultlayout, 3)
        self.mainwindow.setLayout(self.mainlayout)
        self.setCentralWidget(self.mainwindow) # displaying the main layout in the central widget region of QMainWindow

        # Main menu bar
        self.menu1=self.menuBar().addMenu('File') # menubar1
        self.menu_newproject=self.menu1.addAction('New Project')  # the child of menubar1
        self.menu_newproject.triggered.connect(self.newProject)
        self.menu_openproject=self.menu1.addAction('Load Project') # the child of menubar1
        self.menu_openproject.triggered.connect(self.loadProject)
        self.menu_closeprojects = self.menu1.addAction('Close All') # the child of menubar1
        self.menu_closeprojects.triggered.connect(self.closeProjects)

        self.menu2=self.menuBar().addMenu('Run') # menubar2
        self.menu_run=self.menu2.addAction('Run Simulation') # the child of menubar2
        self.menu_run.triggered.connect(self.runSimulation)
        self.menu_test=self.menu2.addAction('Test') # the child of menubar2
        self.menu_test.triggered.connect(self.testDesign)


        # The size of the application
        self.resize(1024,640)
        self.center() # Not in-built function
        self.setWindowTitle('Transdermal Permeation Model')
        #self.setWindowIcon(QIcon('E:\PythonFile\PythonTestFile\icons\chinaz3s.ico')) # setting the icon
        #self.setToolTip('Hello World!') # showing text when the mouse stops
        #self.statusBar().showMessage('Ready') # the status in the left bottom corner

    def newProject(self):
        self.newproject_name, self.newproject_ok = QInputDialog.getText(self, 'New Project', 'Enter project name: ')
        #print(self.newproject_name)
        if self.newproject_ok and bool(self.newproject_name):
            self.newproject = ProjectItem(self.projectview)  # Its parent belong to QTreeWidget
            self.newproject.setText(0, '%s' %self.newproject_name)  # Project name
            self.newproject.setSelected(True)  # Highlighting
            self.projectview.insertTopLevelItem(0,self.newproject)  # showing it in the project interface

    def loadProject(self):
        # The third argument indicates showing the current file path.
        self.openconfigPath, self.Pro_filter1 = QFileDialog.getOpenFileName(self, 'Load Project','.','(Project File (*.cfg))')
        #print(self.openconfigPath)
        if self.openconfigPath:
            if os.name == 'nt':
                self.openconfigPath = self.openconfigPath.replace('/', '\\')
            self.openproject=ProjectItem(self.projectview, cfg_path=self.openconfigPath) #passing the cfg file path!
            self.openproject_name = os.path.split(os.path.split(os.path.split(self.openconfigPath)[0])[0])[1] #project name
            #print(self.openproject_name)
            self.openproject.setText(0, '%s' %self.openproject_name)
            self.openproject.setSelected(True)
            self.projectview.insertTopLevelItem(0,self.openproject)

    def closeProjects(self):
        self.projectview.clear()

    def runSimulation(self):
        self.runconfigPath, self.Pro_filter2 = QFileDialog.getOpenFileName(self,'Select File for configuration','.','cfg File (*.cfg)')
        if self.runconfigPath:
            if os.name == 'nt':
                self.runconfigPath = self.runconfigPath.replace('/', '\\')
            # compDPK('%s'%self.runconfigPath) # run it directly
            self.thread = MyThread('%s' % self.runconfigPath)  # run it by using Thread.(solution2)
            self.thread.setDaemon(True)  # The close of app will close the thread
            self.thread.start()

    def testDesign(self):
        #print('Total TopLevelItem: %s'% self.projectview.topLevelItemCount())
        #print('Total child of current ToplevelItem: %s' % self.newproject.childCount())
        #print('The text of currentItem: %s' % self.projectview.currentItem().text(0))
        #--------------------------------------------------------------------------------------------
        # QLineEdit.text() returns a 'str' data. It is True when there is nothing in the QLineEdit
        #print(self.tableviewer0.CHEM_NO_data.text()=='')
        #--------------------------------------------------------------------------------------------
        # True After commiting, the data is not null anymore. On the contrary, it is ''.
        #print(self.openproject._projData.isnull())
        #--------------------------------------------------------------------------------------------
        # As long as you type something in the QLineEdit and delete all of them,the value is '' but not None.anymore.
        #print(self.newproject._projData.CHEM_NO.isnull().all())
        #--------------------------------------------------------------------------------------------
        #print(self.projectview.indexOfTopLevelItem(self.projectview.currentItem())) #From top to bottom，index increase
        pass

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

    def center(self):
        screen=QDesktopWidget().screenGeometry()
        size=self.geometry()
        # the right gap is as long as the left gap.
        self.move( int((screen.width()-size.width())/2), int((screen.height()-size.height())/2))

#-----------------------------------------------------------------------------------------------------------
class ProDlg(QDialog):
    def __init__(self):
        super(ProDlg, self).__init__()
        self.checkbutton0 = QCheckBox('Chemical', self)
        self.checkbutton1 = QCheckBox('Vehicle (VH)',self)
        self.checkbutton2 = QCheckBox('Stratum Corneum (SC)',self)
        self.checkbutton3 = QCheckBox('Viable Epidermis (VE)',self)
        self.checkbutton4 = QCheckBox('Dermis (DE)', self)
        self.checkbutton5 = QCheckBox('Hair Follicle (HF)', self)
        self.checkbutton6 = QCheckBox('Blood (BD)', self)
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.mainLayout = QVBoxLayout(self)
        self.mainLayout.addWidget(self.checkbutton0)
        self.mainLayout.addWidget(self.checkbutton1)
        self.mainLayout.addWidget(self.checkbutton2)
        self.mainLayout.addWidget(self.checkbutton3)
        self.mainLayout.addWidget(self.checkbutton4)
        self.mainLayout.addWidget(self.checkbutton5)
        self.mainLayout.addWidget(self.checkbutton6)
        self.mainLayout.addWidget(self.buttonBox)
        self.setLayout(self.mainLayout)
        self.setWindowTitle('Compartment Setup')
        self.setFixedWidth(230)
# ------------------------------------------------------------------------------------------------------------
class ProjectItem(QTreeWidgetItem):
    def __init__(self, parent, cfg_path=None):
        super(ProjectItem, self).__init__(parent)
        self.Chemical_setting0 = QTreeWidgetItem(0)
        self.Chemical_setting0.setText(0,'Chemical')
        self.VH_setting0 = QTreeWidgetItem(0)
        self.VH_setting0.setText(0, 'VH')
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
        self.dialog = ProDlg()
        #By default,showing all data classified to one table. The reason is that you don't know which data will be used by user.
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
        self.cols = list(self._projData) #returns the indexes of columns. And then arranging the indexes!..
        self.cols.insert(0, self.cols.pop(self.cols.index('COMPARTMENT_SETUP')))
        self.cols.insert(1, self.cols.pop(self.cols.index('COMP_VH')))
        self.cols.insert(2, self.cols.pop(self.cols.index('COMP_SC')))
        self.cols.insert(3, self.cols.pop(self.cols.index('COMP_VE')))
        self.cols.insert(4, self.cols.pop(self.cols.index('COMP_DE')))
        self.cols.insert(5, self.cols.pop(self.cols.index('COMP_HF')))
        self.cols.insert(6, self.cols.pop(self.cols.index('COMP_BD')))
        self._projData = self._projData.loc[:, self.cols]
        #
        self._parent = parent # 'parent' refers to 'self.projectview'(the Projectviewer class).
        self._parent.itemDoubleClicked.connect(self.viewData) #This signal will connect various 'viewData' functions
        if cfg_path==None:
            self.configure()
        else:
            with open(cfg_path, 'r') as f:
                lines = f.readlines()  #Data type: 'LIST'.
                #Data cleaning
                for lin in lines:
                    lin = list( filter(None, lin.split()) ) #deleting spaces and enter key.
                    #lin = list( filter(lambda x:x!='NaN', lin)) #deleting symbol 'NaN'.
                    #print(lin)
                    if len(lin) != 0:
                        self.loaddata(tokens=lin)

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

    def saveproject(self):
        # self.saveprojectPath=QFileDialog.getSaveFileName(self,'Create Project','.','Project File (*.cfg)') #If enter '.txt', the cfg will be replaced.
        # self.saveproject_name=os.path.split(os.path.splitext(self.saveprojectPath)[0])[1]
        self.saveprojectPath = QFileDialog.getExistingDirectory(self._parent, 'Save your project')  # Return a absolute path
        if self.saveprojectPath:
            self.cfg_name,self.cfg_ok = QInputDialog.getText(self._parent, 'New cfg file', 'Enter cfg-file name: ')
            if self.cfg_ok and bool(self.cfg_name):
                if os.name == 'nt':
                    self.saveprojectPath = self.saveprojectPath.replace('/', '\\')
                self.saveprojectPath_config = os.path.join(self.saveprojectPath, 'config') # 'config' folder path
                self.saveprojectPath_simu = os.path.join(self.saveprojectPath, 'simu')  # 'simu' folder path
                if not os.path.exists(self.saveprojectPath_config):
                    os.mkdir(self.saveprojectPath_config)
                if not os.path.exists(self.saveprojectPath_simu):
                    os.mkdir(self.saveprojectPath_simu)
                #
                self.saveproject_configPath = os.path.join(self.saveprojectPath_config,self.cfg_name + '.cfg')  # cfg file path
                # print(self.saveproject_configPath)
                saveData = pd.DataFrame() # blank data
                for i in self._projData:
                    if self._projData[i].iat[0]!='':
                        saveData[i]=self._projData[i] #Automatically, only accept the column that is with data.
                saveData = saveData.rename(columns={'COMP_VH': 'COMP', 'COMP_SC': 'COMP', 'COMP_VE': 'COMP', 'COMP_DE': 'COMP',
                                         'COMP_HF': 'COMP', 'COMP_BD': 'COMP'}).T
                saveData.to_csv(self.saveproject_configPath,sep=' ',header=False)

    def configure(self):
        """
        Currently, every project is allowed to configure just once.
        """
        if self.dialog.exec_():
            if self.dialog.checkbutton0.isChecked():
                self.addChild(self.Chemical_setting0)
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

    def viewData(self):
        """
        Double clicking on the QTreeWidget will cause this function to be executed.
        """
        if self.Chemical_setting0.isSelected():
            self._parent.sendChemical.emit(self._projData)
        elif self.VH_setting0.isSelected():
            self._parent.sendVH.emit(self._projData)
        elif self.SC_setting0.isSelected():
            self._parent.sendSC.emit(self._projData)
        elif self.VE_setting0.isSelected():
            self._parent.sendVE.emit(self._projData)
        elif self.DE_setting0.isSelected():
            self._parent.sendDE.emit(self._projData)
        elif self.HF_setting0.isSelected():
            self._parent.sendHF.emit(self._projData)
        elif self.BD_setting0.isSelected():
            self._parent.sendBD.emit(self._projData)
        else:
            pass
# --------------------------------------------------------------------------------------------------------

#Main function
app=QApplication(sys.argv)
window1=SurreyWindow() #last top level window
window1.show()
sys.exit(app.exec_())
