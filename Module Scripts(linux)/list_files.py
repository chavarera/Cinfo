import os
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
		self.video_list = ["webm",'mkv','flv','vob','ogv','ogg','drc','gifv','mng','avi','MTS','M2TS','mov','qt','wmv','yuv','rm','rmvb','asf','amv','mp4','m4p','m4v','mpg','mp2','mpeg','mpe','mpv','mpg','m2v','m4a','svi','3gp','3g2','mxf','roq','nsv','flv','f4v','f4p','f4a','f4b']
		self.audio_list = ['3gp','aa','aac','aax','act','aiff','amr','ape','au','awb','dct','dss','dvf','flac','gsm','iklax','ivs','m4a','m4b','m4p','mmf','mp3','mpc','msv','nmf','nsf','ogg','oga','mogg','opus','ra','rm','raw','sln','tta','voc','vox','wav','wma','wv','webm','8svx']
		self.image_list = ['jpg','jpeg','jpe','jif','jfif','jfi','png','jif','webp','tiff','tif','psd','raw','arw','cr2','nrw','k25','bmp','dib','heif','heic','ind','indd','indt','jp2','j2k','jpf','jpx','jpm','mj2','svg','svgz','ai','eps']
		self.all_data = []
		self.video_count = 0
		self.audio_count = 0
		self.image_count = 0
		self.other_count = 0
		self.count = 0

	def work(self):
		'''
		WORK() FUNCTION DOCINFO: 
		1) WORK FUNCTION IS THE MAIN FUNCTION OF CLASS WHICH FINDS ALL THE FILES AND GIVES THE OUTPUT IN FILE "File Found.csv" IN SAME DIRECTORY AS IN SCRIPT
		RESIDES,
		2) IT RETURNS NUMBER OF FILES FOUND AS A RETURN VALUE. 
		'''
		for (root, dirs, files) in os.walk("/", topdown=True):		# FINDING ALL FIES IN ROOT DIRECTORY
			file_list = [file+","+root+file for file in files]		# MODIFYING FILE LIST ACCORDING TO REQUIRED FORMAT
			self.all_data.extend(file_list)							# SAVING ALL FILES FOUND IN CURRENT DIRECTORY INTO ALL_DATA LIST WHICH IS GLOBAL LIST FOR ALL FILES		
			self.count += len(file_list)							# INCREASING COUNT BY THE SAME NUMBER OF FILES, FOUND IN CURRENT DIRECTORY

		data = "File Name, File Address\n"							# INITIAL SETUP FOR DATA VARIABLE WHICH WILL STORE ALL FILE NAME IN FORMATTED WAY
		data += '\n'.join(self.all_data)							# ADDING FILES DATA INTO DATA VARIABLE SO THAT IT CAN BE WRITTEN DIRECTLY
		with open("File Found.csv", "w") as output:					# OOPENING FILE TO BE WRITTEN IN WRITE MODE
			output.write(data)										# DATA VARIABLE IS WRITTEN HERE INTO FILE
		return self.count 

	def type_count(self):
	'''
	type_count() DOCFILE:
		type_count() CHEKCS THE EXTENSIONS OF SCANNED FILES FROM THE OUTPUT FILE AND RETURN A TUPLE OF COUNTS WITH GIVEN FORMAT
		OUTPUT FORMAT:
		(VIDEO COUNT, AUDIO COUNT, IMAGE COUNT, OTHERS)
	'''
		with open('File Found.csv', 'r') as files:												# OPENING OUTPUT FILE
			for line in files.readlines():														# READING EVERY LINE IN FILE
				line = line.split(',')															# SPLIITING LINE WITH ',' AS SEPERATOR
				temp = line[0].split('.')														# SPLITTING FIRST ELEMENT i.e. FILE NAME TO FETCH THE EXTENSION
				if temp[-1].lower() in self.video_list:											# CHECKING IF TH EXTENSION BELONGS TO VIDEOS
					self.video_count += 1
				elif temp[-1].lower() in self.audio_list:										# CHECKING IF TH EXTENSION BELONGS TO AUDIOS
					self.audio_count += 1
				elif temp[-1].lower() in self.image_list:										# CHECKING IF TH EXTENSION BELONGS TO IMAGES
					self.image_count += 1
				else:																			# IF IT DOESN'T BELONG TO ANY OTHER CATEGORY ABOVE, THEN ADD IT TO OTHER'S
					self.other_count += 1
		return (self.video_count,self.audio_count,self.image_count,self.other_count)			# RETURNING A TUPLE OF RESULTS
