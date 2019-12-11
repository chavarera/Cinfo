import os

class get_startup_list:
	def __init__(self):
		'''
		__init__ DOCFILE:
			__init__ BLOCK CONTAINS INITIALISED VARIABLES FOR LATER USE.
		'''
		self.data = ""																							# TO SAVE FETCHED DATA
		self.current_path = ""																					# TO GET THE CURRENT WORKING DIRECTORY 
		self.services = ""																						# THIS VARIABLES SAVED COMMAND LINE OUTPUT
		self.service_list = []																					# LIST TO SAVE THE OUTPUT IN A FORMATTED WAY

	def work(self):
		'''
		work() DOCFILE:
			THE work() FUNCTIONS WORKS IN FOLLOWING WAY:
				1) SERVICE DATA IS COLLECTED IN A VARIABLE.
				2) A LIST IS CREATED FROM THE VARIABLE.
				3) REDUNDANT DATA IS REMOVED FROM THE LIST.
				4) EACH ELEMENT IS SPLITTED INTO SUBLIST.
				5) REDUNDANT DATA IS REMOVED FROM EVERY SUBLIST.
				6) SERIAL NUMBER IS ADDED TO EVERY SUBLIST.
				7) FIALLY FULL DATA IS WRITTEN INTO A SINGLE VARIABLE.
				8) VARIABLE IS RETURNED AS RETURNED VALUE FROM THE FUNCTION.
		'''
		self.services = os.popen("systemctl list-unit-files --type=service").read()								# EXECUTING COMMAND AND SAVING THE OUTPUT IN STRING VARIABLE
		self.service_list = self.services.split('\n')															# SPLITTING THE SERVICES DATA INTO THE LIST
		try:
			while True:																							# REMOVING EXTRA INDUCED SPACES INTO THE LIST
				self.service_list.remove('')
		except Exception as e:
			pass

		self.service_list.pop()																					# REMOVING LAST LIST ELEMENT WHICH IS NOT NEEDED
		self.service_list.pop(0)																				# REMOVING FIRST LIST ELEMENT WHICH IS REDUNDANT

		for i in range(0, len(self.service_list)):																# SPLITTING INDIVIDUAL ELEMENT INTO TWO PARTS i.e. SERVICE AND IT'S STATUS
			self.service_list[i] = self.service_list[i].split(' ')

		for service in self.service_list:																		# REMOVING EXTRA SPACES INDUCED IN EACH SUBLIST
			try:
				while True:
					service.remove('')
			except Exception as e:
				pass


		for i in range(0, len(self.service_list)):																# HOVERING OVER THE WHOLE LIST TO EXECUTE SIMPLE FUNCTIONS 
			self.service_list[i].insert(0, "%d"%(i+1))															# ADDING SERIAL NUMBER TO SUBLIST FOR LATER TABLE PRINTING
			if ".service" in self.service_list[i][1]: 															# REMOVING .Service IF EXISTS IN SERVICE NAME
				self.service_list[i][1] = self.service_list[i][1].replace(".service", '')	
			if "@" in self.service_list[i][1]:																	# REMOVING @ IF EXISTS IN SERVICE NAME
				self.service_list[i][1] = self.service_list[i][1].replace("@", '')


		self.current_path = os.getcwd()																			# SAVING THE CURRENT WORKING DIRECTORY FOR LATER USE
		
		if self.current_path.find("output") == -1:																# CHECKING IF CURRENT WORKING DIRECTORY IS OUTPUT FOLDER
			self.current_path += "/output/"
		
		os.chdir(self.current_path)
		
		self.data = ""
		self.data += "S.No,Service,Status\n"

		for i in self.service_list:
			self.data+=i[0]+","+i[1]+","+i[2]+"\n"
		with open("startup applications.csv", 'w') as startup:													# OPENNG NEW FILE TO SAVE DATA
			startup.write(self.data)																			# WRITING DATA TO FILE 

		return "Startup applications.csv"																		# RETURNING THE VARIABLE FOR LATER USE THE DATA IN FORM OF MODULES
