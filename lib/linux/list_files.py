'''
	Author : Deepak Chauhan
	GitHub : https://github.com/royaleagle73
	Email : 2018PGCACA63@nitjsr.ac.in
'''
import os
import filetype
import json
from datetime import datetime

class list_files:
	'''
	LIST_FILES CLASS CONTAINS THREE FUNCTIONS:
	1) __INIT__
	2) WORK()
	3) TYPE_COUNT()
	
	INIT BLOCK DOCKINFO :
		INIT BLOCK INITIATES TWO VARIABLES 'ALL_DATA' WHICH IS A LIST THAT WILL CONTAIN ALL THE FETCHED FILES LATER and IT ALSO CONTAINS 'COUNT' WHICH KEEPS 
		RECORD FOR THE NUMBER OF FILES.
	WORK() FUNCTION DOCINFO: 
		1) WORK FUNCTION IS THE MAIN FUNCTION OF CLASS WHICH FINDS ALL THE FILES AND GIVES THE OUTPUT IN FILE "File Found.csv" IN SAME DIRECTORY AS IN SCRIPT
		RESIDES,
		2) IT RETURNS NUMBER OF FILES FOUND AS A RETURN VALUE. 		
	
	type_count() DOCFILE:
		type_count() CHEKCS THE EXTENSIONS OF SCANNED FILES FROM THE OUTPUT FILE AND RETURN A TUPLE OF COUNTS WITH GIVEN FORMAT
		OUTPUT FORMAT:
		(VIDEO COUNT, AUDIO COUNT, IMAGE COUNT, OTHERS)
	'''
	def __init__(self):
		'''
		INIT BLOCK DOCKINFO :
		INIT BLOCK INITIATES TWO VARIABLES 'ALL_DATA' WHICH IS A LIST THAT WILL CONTAIN ALL THE FETCHED FILES LATER and IT ALSO CONTAINS 'COUNT' WHICH KEEPS 
		RECORD FOR THE NUMBER OF FILES.
		'''
		self.all_data = []
		self.categories = {"other":0,"images":0,"videos":0,"audios":0,"archives":0,"fonts":0,}
		self.extension_count = {"other":0}
		self.count = 0
		self.images = ["jpg","jpx","png","gif","webp","cr2","tif","bmp","jxr","psd","ico","heic"]
		self.videos = ["mp4", "m4v", "mkv", "webm", "mov", "avi", "wmv", "mpg", "flv"]
		self.audios = ["mid", "mp3", "m4a", "ogg", "flac", "wav", "amr"]
		self.archives = ["epub", "zip", "tar", "rar", "gz", "bz2", "7z", "xz", "pdf", "exe", "swf", "rtf", "eot", "ps", "sqlite", "nes", "crx", "cab", "deb", "ar", "Z", "lz"]
		self.fonts = ["woff", "woff2", "ttf", "otf"]
		self.current_path  = os.getcwd()
	
	def work(self):
		'''
		WORK() FUNCTION DOCINFO: 
		1) WORK FUNCTION IS THE MAIN FUNCTION OF CLASS WHICH FINDS ALL THE FILES AND GIVES THE OUTPUT IN FILE "File Found.csv" IN SAME DIRECTORY AS IN SCRIPT
		RESIDES,
		2) IT RETURNS NUMBER OF FILES FOUND AS A RETURN VALUE. 
		'''
		print("Starting work....", end='\r')
		for (root, dirs, files) in os.walk("/", topdown=True):		# FINDING ALL FIES IN ROOT DIRECTORY
			file_list = [file+","+root+file for file in files]		# MODIFYING FILE LIST ACCORDING TO REQUIRED FORMAT
			self.all_data.extend(file_list)							# SAVING ALL FILES FOUND IN CURRENT DIRECTORY INTO ALL_DATA LIST WHICH IS GLOBAL LIST FOR ALL FILES	
			for file in files:
				if '.' in file:
					if file.split('.')[-1].lower() in self.images:
						self.categories["images"] += 1
						if file.split('.')[-1].lower() not in self.extension_count.keys():
							self.extension_count[file.split('.')[-1].lower()] = 1
						else:
							self.extension_count[file.split('.')[-1].lower()] += 1
					elif file.split('.')[-1].lower() in self.videos:
						self.categories["videos"] += 1
						if file.split('.')[-1].lower() not in self.extension_count.keys():
							self.extension_count[file.split('.')[-1].lower()] = 1
						else:
							self.extension_count[file.split('.')[-1].lower()] += 1
					elif file.split('.')[-1].lower() in self.audios:
						self.categories["audios"] += 1
						if file.split('.')[-1].lower() not in self.extension_count.keys():
							self.extension_count[file.split('.')[-1].lower()] = 1
						else:
							self.extension_count[file.split('.')[-1].lower()] += 1
					elif file.split('.')[-1].lower() in self.archives:
						self.categories["archives"] += 1
						if file.split('.')[-1].lower() not in self.extension_count.keys():
							self.extension_count[file.split('.')[-1].lower()] = 1
						else:
							self.extension_count[file.split('.')[-1].lower()] += 1
					elif file.split('.')[-1].lower() in self.fonts:
						self.categories["fonts"] += 1
						if file.split('.')[-1].lower() not in self.extension_count.keys():
							self.extension_count[file.split('.')[-1].lower()] = 1
						else:
							self.extension_count[file.split('.')[-1].lower()] += 1
					else:
						self.categories["other"] += 1
						self.extension_count["other"] +=1
				else:
						self.categories["other"] += 1
						self.extension_count["other"] +=1

			self.count += len(file_list)							# INCREASING COUNT BY THE SAME NUMBER OF FILES, FOUND IN CURRENT DIRECTORY
			print("Found %d files"%(self.count), end='\r')
			

		data = "File Name, File Address\n"							# INITIAL SETUP FOR DATA VARIABLE WHICH WILL STORE ALL FILE NAME IN FORMATTED WAY
		data += '\n'.join(self.all_data)							# ADDING FILES DATA INTO DATA VARIABLE SO THAT IT CAN BE WRITTEN DIRECTLY

		if self.current_path.find("output") == -1:																# CHECKING IF CURRENT WORKING DIRECTORY IS OUTPUT FOLDER
			self.current_path += "/output/"
		
		os.chdir(self.current_path)

		with open("File list.csv", "w") as output:					# OOPENING FILE TO BE WRITTEN IN WRITE MODE
			output.write(data)										# DATA VARIABLE IS WRITTEN HERE INTO FILE

		data = {}
		data["Total Files"] = []
		data["Total Files"].append({
				"No of files":self.count
				})
		data["Category"] = []
		for i in self.categories:
			data["Category"].append(
				{
					i : self.categories[i]
				}
			)
		for i in self.extension_count:
			data["Category"].append(
				{
					i : self.extension_count[i]
				}
			)
		os.chdir(self.current_path)

		with open("File Overview.json","w") as filecount:
			json.dump(data,filecount)
		
		return True