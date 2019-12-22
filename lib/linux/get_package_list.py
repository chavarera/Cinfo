'''
	Author : Deepak Chauhan
	GitHub : https://github.com/royaleagle73
	Email : 2018PGCACA63@nitjsr.ac.in
'''
import os

class get_package_list:
	'''
	get_package_list CLASS COMBINE A SINGLE METHOD AND A CONSTRUCTOR, WHICH ARE AS FOLLOWS:
		1) __init__
		2) work()
			
			__init__ DOCFILE:
				__init__ SERVES THE PURPOSE TO INITIALISE VARIABLES WHICH AREGONG TO BE USED LATER IN PROGRAM.
		
			
			work() DOCFILE :
				work() FUNCTION WORKS THIS WAY:
					1) SEARCHES FOR FILES IN /usr/bin/.
					2) REFINE FILES WHICH ARE NOT SCRIPTS
					3) SAVE THEM IN A FILE.
					4) RETURNS TRUE FOR SUCCESS
	'''
	def __init__(self):
		'''
		__init__ DOCFILE:
			__init__ SERVES THE PURPOSE TO INITIALISE VARIABLES WHICH AREGONG TO BE USED LATER IN PROGRAM.
		'''
		self.file_path = "/usr/bin/"										# SETTING UP FILE PATH TO FIND PACKAGES
		self.files_found = os.listdir(self.file_path)						# FINDING FILES AND SAVING THEM IN A LIST
		self.data = "S.No., Package Name\n"									# INITIALISING VARIABLE TO STORE DATA LATER
		self.current_path = os.getcwd()										# SAVING THE CURRENT WORKING DIRECTORY FOR LATER USE
		self.count = 0														# TO KEEP COUND OF NUMBER OF PACKAGES FOUND

	def work(self):
		'''
		work() DOCFILE :
		work() FUNCTION WORKS THIS WAY:
			1) SEARCHES FOR FILES IN /usr/bin/.
			2) REFINE FILES WHICH ARE NOT SCRIPTS
			3) SAVE THEM IN A FILE.
			4) RETURNS TRUE FOR SUCCESS
		'''
		# CHANGING WORKING DIRECTORY
		os.chdir(self.file_path)											# CHANGING CURRENT WORKING DIRECTORY
		ret_data = {"List of Installed Applications" : [["Applications Name"]]}
		# LISTING ALL FILES AND SERIAL NUMBER EXCLUDING FOLDERS
		for file in self.files_found:										# CHECKING EACH SCANNED FILE ONE BY ONE
			if not os.path.isdir(file):										# CHECKING IS SCANNED FILE IS A FILE OR FOLDER
				if not file.endswith(".sh"):									# REMOVING SCRIPT FILES
					self.count += 1											# IF IT IS A FILE, COUNTING INCREASES BY 1
					self.data += str(self.count) + "," + file + "\n"		# SAVING THE PACKAGE NAME AND SERIAL NUMBER IN DATA VARIABLE
					ret_data["List of Installed Applications"].append([file])

		if self.current_path.find("output") == -1:																# CHECKING IF CURRENT WORKING DIRECTORY IS OUTPUT FOLDER
			self.current_path += "/output/"
		os.chdir(self.current_path)											# CHANGING CURRENT WORKING DIRECTORY
		with open("linux_packages_installed.csv", 'w') as pack:				# OPENNG NEW FILE TO SAVE DATA
			pack.write(self.data)											# WRITING DATA TO FILE 

		return ret_data