# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Cinfo.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from lib.windows import SystemInfo,NetworkInfo,SoftwareInfo,StorageInfo
from lib.windows import HardwareInfo,FileInfo,DeviceInfo,MiscInfo,ServiceInfo
from lib.windows.common import Utility as utl
import json
import os
import pickle

    
class Ui_Cinfo(object):
    def __init__(self):
        self.module_list = ['system','hardware','network','software','device','storage','service']
        self.submodules = []
        self.modules=""
        self.current_selected = []
        self.os = os.name
        self.cheklist = []
        self.checked_modules = []
        self.fetchedData = self.OpenPickle()
        self.filterdata = []
        
    def closeEvent(self, event):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Question)
        msg.setInformativeText("Are you sure you want to close this window?")
        msg.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.Cancel)
        msg.setWindowTitle("Are you sure?")
        replay=msg.exec_()
        if(replay==QtWidgets.QMessageBox.Yes):
            exit(0)
        else:
            pass
        
    def setupUi(self, Cinfo):
        Cinfo.setObjectName("Cinfo")
        Cinfo.resize(640, 461)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/info.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Cinfo.setWindowIcon(icon)
        Cinfo.setIconSize(QtCore.QSize(32, 24))
        self.centralwidget = QtWidgets.QWidget(Cinfo)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.Modules_verticalLayout = QtWidgets.QVBoxLayout()
        self.Modules_verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.Modules_verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.Modules_verticalLayout.setSpacing(1)
        self.Modules_verticalLayout.setObjectName("Modules_verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAutoFillBackground(False)
        self.label.setLineWidth(1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.Modules_verticalLayout.addWidget(self.label)
        self.gridLayout.addLayout(self.Modules_verticalLayout, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.result_tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.result_tableWidget.setObjectName("result_tableWidget")
        self.result_tableWidget.setColumnCount(0)
        self.result_tableWidget.setRowCount(0)
        

        self.horizontalLayout.addWidget(self.result_tableWidget)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(QtCore.Qt.PlainText)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 2)
        Cinfo.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Cinfo)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.menuFile.setFont(font)
        self.menuFile.setObjectName("menuFile")
        self.menuExport_As = QtWidgets.QMenu(self.menuFile)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.menuExport_As.setFont(font)
        self.menuExport_As.setObjectName("menuExport_As")
        self.menuOption = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.menuOption.setFont(font)
        self.menuOption.setObjectName("menuOption")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.menuHelp.setFont(font)
        self.menuHelp.setObjectName("menuHelp")
        Cinfo.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(Cinfo)
        self.toolBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.toolBar.setMovable(True)
        self.toolBar.setIconSize(QtCore.QSize(30, 24))
        self.toolBar.setObjectName("toolBar")
        Cinfo.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.statusBar = QtWidgets.QStatusBar(Cinfo)
        self.statusBar.setObjectName("statusBar")
        Cinfo.setStatusBar(self.statusBar)
        self.actionExcel = QtWidgets.QAction(Cinfo)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/excel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExcel.setIcon(icon1)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.actionExcel.setFont(font)
        self.actionExcel.setObjectName("actionExcel")
        self.actionJson = QtWidgets.QAction(Cinfo)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/Json.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionJson.setIcon(icon2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.actionJson.setFont(font)
        self.actionJson.setObjectName("actionJson")
        self.actionText = QtWidgets.QAction(Cinfo)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/text.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionText.setIcon(icon3)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.actionText.setFont(font)
        self.actionText.setObjectName("actionText")
        self.actionRefresh = QtWidgets.QAction(Cinfo)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/Refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRefresh.setIcon(icon4)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.actionRefresh.setFont(font)
        self.actionRefresh.setObjectName("actionRefresh")
        self.actionExit = QtWidgets.QAction(Cinfo)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon5)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.actionExit.setFont(font)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QtWidgets.QAction(Cinfo)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/about.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout.setIcon(icon6)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.actionAbout.setFont(font)
        self.actionAbout.setObjectName("actionAbout")
        self.actionHelp = QtWidgets.QAction(Cinfo)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icons/help.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHelp.setIcon(icon7)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.actionHelp.setFont(font)
        self.actionHelp.setObjectName("actionHelp")
        self.actionPreferences = QtWidgets.QAction(Cinfo)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icons/Prefrences.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPreferences.setIcon(icon8)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.actionPreferences.setFont(font)
        self.actionPreferences.setObjectName("actionPreferences")
        self.menuExport_As.addAction(self.actionExcel)
        self.menuExport_As.addAction(self.actionJson)
        self.menuExport_As.addAction(self.actionText)
        self.menuFile.addAction(self.actionRefresh)
        self.menuFile.addAction(self.menuExport_As.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuOption.addAction(self.actionPreferences)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionHelp)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuOption.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionRefresh)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionExcel)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionJson)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionText)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionExit)
        self.toolBar.addSeparator()
        self.comboBoxNew = QtWidgets.QComboBox()
        self.Modules_verticalLayout.addWidget(self.comboBoxNew)
        self.comboBoxNew.currentTextChanged.connect(self.on_SubModule_change)
        
        self.retranslateUi(Cinfo)
        QtCore.QMetaObject.connectSlotsByName(Cinfo)
        
        self.actionJson.triggered.connect(self.ExportToJson)
        self.actionExit.triggered.connect(self.closeEvent)
        self.AddModules()
        
    def ShowAlertMsg(self,message,types):
        if types=="success":
            alert_icon=QtWidgets.QMessageBox.Information
            alert_type="Success"
        if types=="error":
            alert_icon=QtWidgets.QMessageBox.Critical
            alert_type="Error"
            
        message=message   
        msg = QtWidgets.QMessageBox()
        msg.setIcon(alert_icon)
        msg.setInformativeText(str(message))
        msg.setWindowTitle(alert_type)
        msg.exec_()

    def OpenPickle(self,filepath='result.pickle'):
      try:
           with open(filepath,"rb") as file:
              return pickle.load(file)
      except:
          print("First Run Follwing command on Command Prompt \npython Cinfo.py")
          exit(0)
        
    def FilterRecord(self,filters):
        if len(filters)>0:
           self.filterdata=[self.fetchedData[module] for module in filters]
           
    def ExportToJson(self):
        status,res=utl.ExportTOJson(self.fetchedData)
        if status:
            self.ShowAlertMsg(res,"success")
        else:
            self.ShowAlertMsg(res,"error")
        
    def SubFilter(self,module,subFilter):
        try:
            self.current_selected=self.fetchedData[module][subFilter]
        except Exception as Ex:
            pass
    
            
            
    def ModuleInfo(self):
        for i in range(self.comboBoxNew.count()+1):
            self.comboBoxNew.removeItem(i)
        checkeds=[val.isChecked() for val in self.cheklist]
        
        self.checked_modules=[val for status,val in zip(checkeds,self.module_list) if status]
        self.modules=self.checked_modules[0]
        self.FilterRecord(self.checked_modules)
        self.SetData(self.checked_modules)
        
    def on_SubModule_change(self):

        current_submodule=self.comboBoxNew.currentText()
        self.result_tableWidget.setColumnCount(2)
        keys=['Parameter','Value']
        
        self.SubFilter(self.modules,current_submodule)
        all_values=self.current_selected[0].keys()
        rows_count=0
        self.result_tableWidget.setRowCount(0)
        if len(self.current_selected)==1:
            self.result_tableWidget.insertRow(0)
            self.result_tableWidget.setHorizontalHeaderLabels(keys)
            for result in self.current_selected:
                vals=result.values()
                for idx,value in enumerate(result.keys()):
                    if result[value]!="":
                        self.result_tableWidget.insertRow(rows_count)
                        self.result_tableWidget.setItem(rows_count, 0, QtWidgets.QTableWidgetItem(str(value)))
                        self.result_tableWidget.setItem(rows_count, 1, QtWidgets.QTableWidgetItem(str(result[value])))
                        rows_count+=1
        else:
            keys=self.current_selected[0].keys()
            self.result_tableWidget.setColumnCount(len(keys))
            self.result_tableWidget.setHorizontalHeaderLabels(keys)
            for result in self.current_selected:
            
                self.result_tableWidget.insertRow(rows_count)
                vals=result.values()
                for idx,value in enumerate(vals):
                    self.result_tableWidget.setItem(rows_count, idx, QtWidgets.QTableWidgetItem(str(value)))
                rows_count+=1

        self.result_tableWidget.resizeColumnsToContents()     

        
    def SetData(self,modules):
        self.comboBoxNew.clear()
        self.result_tableWidget.setRowCount(0)
        self.submodules=[key for key,value in self.filterdata[0].items()]
        self.comboBoxNew.addItems(self.submodules)
       
        
              
    def AddModules(self):
        font = QtGui.QFont()
        font.setPointSize(12)
        test=[]
        for modules in self.module_list:
            self.radioButton = QtWidgets.QRadioButton(Cinfo)
            self.radioButton.setObjectName(modules)
            self.radioButton.setText(modules)
            self.radioButton.setFont(font)
            self.radioButton.toggled.connect(self.ModuleInfo)
            self.Modules_verticalLayout.addWidget(self.radioButton)
            self.cheklist.append(self.radioButton)

    def retranslateUi(self, Cinfo):
        _translate = QtCore.QCoreApplication.translate
        Cinfo.setWindowTitle(_translate("Cinfo", "Cinfo"))
        self.label.setText(_translate("Cinfo", "Select Module"))
        self.label_2.setText(_translate("Cinfo", "Cinfo ( Computer Information )"))
        self.menuFile.setTitle(_translate("Cinfo", "File"))
        self.menuExport_As.setTitle(_translate("Cinfo", "Export As"))
        self.menuOption.setTitle(_translate("Cinfo", "Option"))
        self.menuHelp.setTitle(_translate("Cinfo", "Help"))
        self.toolBar.setWindowTitle(_translate("Cinfo", "toolBar"))
        self.actionExcel.setText(_translate("Cinfo", "Excel"))
        self.actionExcel.setToolTip(_translate("Cinfo", "Export Record IntoExcel"))
        self.actionJson.setText(_translate("Cinfo", "Json"))
        self.actionJson.setToolTip(_translate("Cinfo", "Export into json File"))
        self.actionText.setText(_translate("Cinfo", "Text"))
        self.actionText.setToolTip(_translate("Cinfo", "Export Into Text File"))
        self.actionRefresh.setText(_translate("Cinfo", "Refresh"))
        self.actionRefresh.setToolTip(_translate("Cinfo", "refresh"))
        self.actionRefresh.setShortcut(_translate("Cinfo", "Ctrl+F5"))
        self.actionExit.setText(_translate("Cinfo", "Exit"))
        self.actionExit.setToolTip(_translate("Cinfo", "Exit Window"))
        self.actionExit.setShortcut(_translate("Cinfo", "Ctrl+Q"))
        self.actionAbout.setText(_translate("Cinfo", "About"))
        self.actionAbout.setToolTip(_translate("Cinfo", "Information "))
        self.actionAbout.setShortcut(_translate("Cinfo", "Ctrl+I"))
        self.actionHelp.setText(_translate("Cinfo", "Help"))
        self.actionHelp.setShortcut(_translate("Cinfo", "Ctrl+F1"))
        self.actionPreferences.setText(_translate("Cinfo", "Preferences"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Cinfo = QtWidgets.QMainWindow()
    ui = Ui_Cinfo()
    ui.setupUi(Cinfo)
    Cinfo.show()
    sys.exit(app.exec_())
