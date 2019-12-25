import os
import json
from tabulate import tabulate

class saveAs:
	def __init__(self):
		self.saving_directory = os.getcwd()+'/'+'output/'
		self.textData = ""
		self.myJson = {}
	
	def saveAsText(self, myDict,branch):
		if len(myDict[branch][0]) is 1:
			myDict[branch].insert(0,["Usernames"])
		else:
			myDict[branch].insert(0,["Property","Value"])
		self.textData += tabulate(myDict[branch][1:], headers = myDict[branch][0], tablefmt="fancy_grid")
		with open(self.saving_directory+branch+".txt", "w") as myFile:
			myFile.write(self.textData)

	def saveAsCSV(self, myDict,branch):
		if len(myDict[branch][0]) is 1:
			myDict[branch].insert(0,["Usernames"])
		else:
			myDict[branch].insert(0,["Property","Value"])
		for i in myDict[branch]:
			for j in i:
				if i[-1] is j:
					self.textData += j+'\n'
				else:
					self.textData += j + ','
		with open(self.saving_directory+branch+".csv", "w") as myFile:
			myFile.write(self.textData)

	def saveAsJson(self, myDict, branch):
		self.myJson = { branch : {}}
		if len(myDict[branch][0]) is not 1:
			for element in myDict[branch]:
				self.myJson[branch][element[0]] = element[1]
		else:
			self.myJson[branch] = []
			for i in myDict[branch]:
				self.myJson[branch].append(i[0])
		with open(self.saving_directory+branch+".json", "w") as myFile:
			json.dump(self.myJson,myFile)