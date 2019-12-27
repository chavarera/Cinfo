# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainUi.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

import os
import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets
from lib.linux import get_browsers,get_drives,get_hw_info,get_network_info,get_os_info,get_package_list,get_ports,get_startup_list,list_files, saveFile

class Ui_Cinfo(object):
	def __init__(self):
		self.selectedDict = dict()

	def setupUi(self, Cinfo):
		Cinfo.setObjectName("Cinfo")
		Cinfo.resize(777, 461)
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap("icons/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		Cinfo.setWindowIcon(icon)
		Cinfo.setIconSize(QtCore.QSize(32, 24))
		self.centralwidget = QtWidgets.QWidget(Cinfo)
		self.centralwidget.setObjectName("centralwidget")
		self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
		self.gridLayout.setObjectName("gridLayout")
		self.label = QtWidgets.QLabel(self.centralwidget)
		self.label.setObjectName("label")
		self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
		self.verticalLayout_2 = QtWidgets.QVBoxLayout()
		self.verticalLayout_2.setObjectName("verticalLayout_2")
		## Home Page
		self.homePage = QtWidgets.QRadioButton(self.centralwidget)
		self.homePage.setObjectName("homePage")
		self.homePage.toggled.connect(lambda: self.toggleCheck(self.homePage,0))
		self.verticalLayout_2.addWidget(self.homePage)
		##  About Your Machine
		self.aboutYourMachine = QtWidgets.QRadioButton(self.centralwidget)
		self.aboutYourMachine.setObjectName("aboutYourMachine")
		self.aboutYourMachine.toggled.connect(lambda: self.toggleCheck(self.aboutYourMachine,5))
		self.verticalLayout_2.addWidget(self.aboutYourMachine)
		##  For Network
		self.networkInfo = QtWidgets.QRadioButton(self.centralwidget)
		self.networkInfo.setObjectName("networkInfo")
		self.networkInfo.toggled.connect(lambda: self.toggleCheck(self.networkInfo,4))
		self.verticalLayout_2.addWidget(self.networkInfo)
		##  For Installed Applications
		self.instaLledApplications = QtWidgets.QRadioButton(self.centralwidget)
		self.instaLledApplications.setObjectName("instaLledApplications")
		self.instaLledApplications.toggled.connect(lambda: self.toggleCheck(self.instaLledApplications,3))
		##  For Installed Browsers
		self.installedBrowsers = QtWidgets.QRadioButton(self.centralwidget)
		self.installedBrowsers.setObjectName("installedBrowsers")
		self.installedBrowsers.toggled.connect(lambda: self.toggleCheck(self.installedBrowsers,6))
		self.verticalLayout_2.addWidget(self.installedBrowsers)
		##  For Startup Applications
		self.startUpapplications = QtWidgets.QRadioButton(self.centralwidget)
		self.startUpapplications.setObjectName("startUpapplications")
		self.startUpapplications.toggled.connect(lambda: self.toggleCheck(self.startUpapplications,2))
		self.verticalLayout_2.addWidget(self.startUpapplications)
		self.verticalLayout_2.addWidget(self.instaLledApplications)
		##  Opened Ports
		self.openedPorts = QtWidgets.QRadioButton(self.centralwidget)
		self.openedPorts.setObjectName("openedPorts")
		self.openedPorts.toggled.connect(lambda: self.toggleCheck(self.openedPorts,7))
		self.verticalLayout_2.addWidget(self.openedPorts)
		## For Listing files
		self.listfIles = QtWidgets.QRadioButton(self.centralwidget)
		self.listfIles.setObjectName("listfIles")
		self.listfIles.toggled.connect(lambda: self.toggleCheck(self.listfIles,1))
		self.verticalLayout_2.addWidget(self.listfIles)

		self.gridLayout.addLayout(self.verticalLayout_2, 2, 1, 1, 1)
		self.label_2 = QtWidgets.QLabel(self.centralwidget)
		self.label_2.setObjectName("label_2")
		self.gridLayout.addWidget(self.label_2, 0, 4, 1, 1)
		self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
		self.tableWidget.setProperty("showDropIndicator", True)
		self.tableWidget.setShowGrid(True)
		self.tableWidget.setObjectName("tableWidget")
		self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
		self.tableWidget.verticalHeader().setSortIndicatorShown(False)
		self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
		self.tableWidget.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
		self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
		self.gridLayout.addWidget(self.tableWidget, 2, 4, 1, 1)
		self.tables = QtWidgets.QComboBox(self.centralwidget)
		self.tables.setObjectName("tables")
		self.gridLayout.addWidget(self.tables, 1, 4, 1, 1)
		Cinfo.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(Cinfo)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 777, 26))
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
		self.actionExcel.triggered.connect(lambda :self.saveData(2))
		self.actionJson = QtWidgets.QAction(Cinfo)
		icon2 = QtGui.QIcon()
		icon2.addPixmap(QtGui.QPixmap("icons/Json.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.actionJson.setIcon(icon2)
		font = QtGui.QFont()
		font.setFamily("Segoe UI")
		font.setPointSize(12)
		self.actionJson.setFont(font)
		self.actionJson.setObjectName("actionJson")
		self.actionJson.triggered.connect(lambda :self.saveData(3))
		self.actionText = QtWidgets.QAction(Cinfo)
		icon3 = QtGui.QIcon()
		icon3.addPixmap(QtGui.QPixmap("icons/text.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.actionText.setIcon(icon3)
		font = QtGui.QFont()
		font.setFamily("Segoe UI")
		font.setPointSize(12)
		self.actionText.setFont(font)
		self.actionText.setObjectName("actionText")
		self.actionText.triggered.connect(lambda :self.saveData(1))
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

		self.retranslateUi(Cinfo)
		QtCore.QMetaObject.connectSlotsByName(Cinfo)

	def retranslateUi(self, Cinfo):
		_translate = QtCore.QCoreApplication.translate
		Cinfo.setWindowTitle(_translate("Cinfo", "Cinfo"))
		self.homePage.setText(_translate("Cinfo", "Home"))
		self.listfIles.setText(_translate("Cinfo", "List Files"))
		self.startUpapplications.setText(_translate("Cinfo", "List Startup Applications"))
		self.instaLledApplications.setText(_translate("Cinfo", "List Installed Applications"))
		self.networkInfo.setText(_translate("Cinfo", "Network Information"))
		self.aboutYourMachine.setText(_translate("Cinfo", "About Your Machine"))
		self.installedBrowsers.setText(_translate("Cinfo", "List Installed Browsers"))
		self.openedPorts.setText(_translate("Cinfo", "List Open Ports"))
		self.label.setText(_translate("Cinfo", "Choose Service :"))
		self.label_2.setText(_translate("Cinfo", "Result :"))
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
		self.homePage.setChecked(True)
		self.toggleCheck(self.homePage,0)

## Refresh Function
	def refresh(self):
		print("Refreshed")

## Toggle Check
	def toggleCheck(self,toggledButton, response):
		if response is 0 :
			if toggledButton.isChecked() is True :
				self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
				self.textBrowser.setObjectName("textBrowser")
				self.gridLayout.addWidget(self.textBrowser, 2, 4, 1, 1)
				self.tables.clear()
				self.tables.addItem("Home")
				self.textBrowser.setHtml("""<style type="text/css">p, li { white-space: pre-wrap; }</style>
<center> <img src="./icons/logo.png" align="center"> </center>
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Cantarell'; font-size:11pt;"><em><span style="color: rgb(251, 160, 38);">&nbsp;</span></em></span><span style="color: rgb(251, 160, 38);"><em><span style=" font-family:'Cantarell'; font-size:11pt; font-weight:600;">Cinfo &nbsp;( Computer Information )&nbsp;</span></em></span><span style=" font-family:'Cantarell'; font-size:11pt; font-weight:600; vertical-align:sub;"><em><span style="color: rgb(251, 160, 38);">v1.0&nbsp;</span></em></span></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Cantarell'; font-size:11pt;">
  <br>
</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Cantarell'; font-size:11pt;">Welcome to Cinfo an all in one information board where you gett all information related to your machine.</span></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Cantarell'; font-size:11pt;">
  <br>
</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Cantarell'; font-size:11pt; font-weight:600;">To get Started&nbsp;</span><span style=" font-family:'Cantarell'; font-size:11pt;">:</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Cantarell'; font-size:11pt;">Choose service you want to be informed about, tick on the services and press the 'Let's Go' Button.</span></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Cantarell'; font-size:11pt;">
  <br>
</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Cantarell'; font-size:11pt; font-weight:600;">Result</span><span style=" font-family:'Cantarell'; font-size:11pt;">&nbsp;:</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Cantarell'; font-size:11pt;">Your requested information will be right here in next moment, with title of information you requested.</span></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Cantarell'; font-size:11pt;">
  <br>
</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Cantarell'; font-size:11pt; font-weight:600;">Support Us !!</span><span style=" font-family:'Cantarell'; font-size:11pt;">&nbsp;:</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Cantarell'; font-size:11pt;">To show your support visit </span>
  <a href="https://Github.com/chavarera/Cinfo" rel="noopener noreferrer" target="_blank"><span style=" font-family:'Cantarell'; font-size:11pt;">G</span><span style=" font-family:'Cantarell'; font-size:11pt;">itHub</span></a>
  <a href="https://Github.com/chavarera/Cinfo"></a><span style=" font-family:'Cantarell'; font-size:11pt;">&nbsp;page for the software and give us a star</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">
  <a href="https://Github.com/chavarera/Cinfo"><span style=" font-family:'Cantarell'; font-size:11pt; text-decoration: underline; color:#0000ff;">https://Github.com/chavarera/Cinfo</span></a>
</p>""")
			else:
				self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
				self.tableWidget.setProperty("showDropIndicator", True)
				self.tableWidget.setShowGrid(True)
				self.tableWidget.setObjectName("tableWidget")
				self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
				self.tableWidget.verticalHeader().setSortIndicatorShown(False)
				self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
				self.tableWidget.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
				self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
				self.gridLayout.addWidget(self.tableWidget, 2, 4, 1, 1)
		if toggledButton.isChecked() is True and response is not 0:
				self.returnData(response)

## TO SAVE DATA IN FILE
	def saveData(self, saveCode):
		save = saveFile.saveAs()
		## To save as text file
		if saveCode is 1:
			save.saveAsText(self.selectedDict,self.tables.currentText())
		elif saveCode is 2:
			save.saveAsCSV(self.selectedDict,self.tables.currentText())	
		elif saveCode is 3:
			save.saveAsJson(self.selectedDict,self.tables.currentText())

## TO CREATE A TABLE
	def createTable(self,dataList):
		self.tableWidget.setRowCount(len(dataList)-1)
		self.tableWidget.setColumnCount(len(dataList[0]))
		self.tableWidget.setHorizontalHeaderLabels(dataList[0])
		dataList.pop(0)
		for row in range(len(dataList)):
			for column in range(len(dataList[0])):
				try:
					self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem((dataList[row][column])))
				except Exception as e:
					pass

# CREATE A COMBOBOX FOR GIVEN FUNCTION
	def createCombo(self, myDict):
		self.selectedDict = myDict
		self.tables.clear()
		self.tables.addItem("Choose the appropriate Information ")
		self.tables.addItems(myDict.keys())
		while True:
			try:
				self.tables.currentIndexChanged.disconnect()
			except Exception as e:
				break
		self.tables.currentIndexChanged.connect(lambda : self.bindFunctions(myDict))
		self.tables.setCurrentIndex(1)

## WINDOWS BACKEND DRIVER FUNCTION
	def windowsBackend(self):
		print("Calling windows")

	def bindFunctions(self,myDict):
		if self.tables.currentText() not in ['','Choose the appropriate Information ','Home'] :
			self.createTable(myDict[self.tables.currentText()])

## LINUX BACKEND DRIVER FUNCTION
	def linuxBackend(self, response):
		packages = get_package_list.get_package_list()
		startup = get_startup_list.get_startup_list()
		network = get_network_info.get_network_info()
		browsers = get_browsers.get_browsers()
		ports = get_ports.get_ports()
		drives = get_drives.get_drives()
		os_info = get_os_info.get_os_info()
		hardware = get_hw_info.get_hw_info()
		files = list_files.list_files()
		data = ""
		if response is 1:
			self.createCombo(files.work())
		elif response is 2:
			self.createCombo(startup.work())
		elif response is 3:
			self.createCombo(packages.work())
		elif response is 4:
			self.createCombo(network.work())
		elif response is 7:
			self.createCombo(ports.work())
		elif response is 6:
			self.createCombo(browsers.work())
		elif response is 5:
			self.createCombo(os_info.work())

## CALLING APPROPRIATE FUNCTION FOR APPRORIATE OS
	def returnData(self, response):
		if os.name=='nt':
			self.windowsBackend()
		else:
			self.linuxBackend(response)

## MAIN FUNCTION
if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	Cinfo = QtWidgets.QMainWindow()
	ui = Ui_Cinfo()
	ui.setupUi(Cinfo)
	Cinfo.show()
	sys.exit(app.exec_())
