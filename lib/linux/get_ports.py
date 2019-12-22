'''
	Author : Deepak Chauhan
	GitHub : https://github.com/royaleagle73
	Email : 2018PGCACA63@nitjsr.ac.in
'''
import os
import re

class get_ports:
	'''
	********* THIS SCRIPT RETURNS A LIST OF TUPLE CONTAINING PORTS AND PROTOCOLS OPEN ON USER'S LINUX SYSTEM *********
	CLASS get_ports DOCINFO:
	get_ports HAVE TWO FUNCTIONS I.E.,
	1) __init__
	2) work()

		__init__ DOCFILE:
			__init__ BLOCK SERVES THE INITIALIZATION FUNCTION, CONTAINING INITIALIZED VARIABLES WHICH IS GOING TO BE USED LATER BY OTHER MEMBER FUNCTION.

		WORK() DOCFILE:
		1) COLLECTS DATA FROM COMMANDLINE INTO STRING AND THEN SPLITTS INTO THE LIST.
		2) TRAVERSES ON EVERY OUTPUT.
		3) EXTRACTS ALL PORTS IN OUTPUT LINE.
		4) CHECKS IF EXTRACTED PORTS COUNT IS GREATER THAN OR EQUAL TO 0.
		5) REMOVS SEMI-COLON(:) FROM THE START OF PORT.
		6) CHECKS IF THE EXTRACTED PORT EXIST BEFORE IN LIST.
		7) EXTRACTS PROTOCOL FROM THE OUTPUT.
		8) SAVES THE PROTOCOL AND PORT IN THE LIST.
		9) SAVES THE PROTOCOL IN SECONDARY LIST FOR LATER COMPARISION.
		10) RETURNS THE FINAL OUTPUT.
	'''

	def __init__(self):
		'''
__init__ DOCFILE:
__init__ BLOCK SERVES THE INITIALIZATION FUNCTION, CONTAINING INITIALIZED VARIABLES WHICH IS GOING TO BE USED LATER BY OTHER MEMBER FUNCTION.
		'''
		self.data = []																					# TO SAVE DATA RECIEVED FROM COMMAND INTO A STRING
		self.final_list = []																			# FOR SAVING BROWSER DATA COLLECTED INTO A SINGLE VARIABLE
		self.secondary_port_list = []																	# FOR SAVING ALL PORTS FOR LATER COMPARISION FOR DUPLICATE PORTS
		self.protocol = ""																				# FOR EXTRACTING PROTOCOLS FROM ALL OUTPUTS
		self.final_data = ""																			# FOR SAVING FINAL DATA IN A STRING
		self.current_path = os.getcwd()																	# For SAVING CURRENT DIRECTORY INFORMATION
	
	def work(self):
		'''
WORK() DOCFILE:
	THE FUNCTION WORKS IN FOLLOWING WAY:
		1) COLLECTS DATA FROM COMMANDLINE INTO STRING AND THEN SPLITTS INTO THE LIST.
		2) TRAVERSES ON EVERY OUTPUT.
		3) EXTRACTS ALL PORTS IN OUTPUT LINE.
		4) CHECKS IF EXTRACTED PORTS COUNT IS GREATER THAN OR EQUAL TO 0.
		5) REMOVS SEMI-COLON(:) FROM THE START OF PORT.
		6) CHECKS IF THE EXTRACTED PORT EXIST BEFORE IN LIST.
		7) EXTRACTS PROTOCOL FROM THE OUTPUT.
		8) SAVES THE PROTOCOL AND PORT IN THE LIST.
		9) SAVES THE PROTOCOL IN SECONDARY LIST FOR LATER COMPARISION.
		10) RETURNS THE FINAL OUTPUT.
		'''
		ret_data = {"Open Ports List":[["Protocol","Port Number"]]}
		data = os.popen("ss -lntu").read().split('\n')													# COLLECTING DATA FROM COMMANDLINE INTO STRING AND THEN SPLITTING INTO THE LIST
		for i in data:																					# TRAVERSING ON EVERY OUTPUT
			self.ports_in_line = re.findall(r':\d{1,5}', i)												# EXTRACTING ALL PORTS IN OUTPUT LINE
			if len(self.ports_in_line) > 0 :															# CHECKING IF EXTRACTED PORTS COUNT IS GREATER THAN OR EQUAL TO 0
				self.extracted_port = self.ports_in_line[0][1:]											# REMOVING SEMI-COLON(:) FROM THE START OF PORT
				if self.extracted_port not in self.secondary_port_list:									# CHECKING IF THE EXTRACTED PORT EXIST BEFORE IN LIST
					self.protocol = i[:i.find(' ')]														# EXTRACTING PROTOCOL FROM THE OUTPUT
					self.final_list.append((self.protocol,self.extracted_port))							# SAVING THE PROTOCOL AND PORT IN THE LIST
					self.secondary_port_list.append(self.extracted_port)								# SAVING THE PROTOCOL IN SECONDARY LIST FOR LATER COMPARISION
		
		self.final_data = "Protocol,Port\n"
		for i in self.final_list:
			self.final_data += i[0]+","+i[1]+"\n"
			ret_data["Open Ports List"].append([i[0],i[1]])

		if self.current_path.find("output") == -1:														# CHECKING IF CURRENT WORKING DIRECTORY IS OUTPUT FOLDER
			self.current_path += "/output/"
		os.chdir(self.current_path)																		# CHANGING CURRENT WORKING DIRECTORY
		with open("Open Ports.csv", "w") as ports:														# SAVING DATA INTO A FILE
			ports.write(self.final_data)

		return ret_data