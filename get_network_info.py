import os
from tabulate import tabulate

class get_net_info:
	'''
	CLASS get_net_info PROVIDES THE CURRENT NETWORK CONNECTION STATUS, IP ADDRESS, NET MASK ADDRESS AND BROADCAST ADDRESS ALONGWITH ALL INTERFACE STATS.
	get_net_info HAVE TWO METHODS:
	1) __init__
	2) work()
		__init__ DOCFILE:
			__init__ BLOCK HOLDS ALL INITIALISED/UNINITIALISED ATTRIBUTES WHICH ARE GOING TO BE LATER IN THE WORK FUNCTION.
		work() DOCFILE:
			work() RETURNS A SIBGLE STRING CONTAINING FORMATTED NETWORK INFORMATION CONTAINING IP ADDRESSES, INTERFACE DATA AND MAC ADDRESSES
	'''
	def __init__(self):
		'''
		__init__ DOCFILE:
			__init__ BLOCK HOLDS ALL INITIALISED/UNINITIALISED ATTRIBUTES WHICH ARE GOING TO BE LATER IN THE WORK FUNCTION.
		'''
		self.ip_list = []																	# THIS LIST CONTAINS  OBTAINED IP ADDRESS FROM COMMAND LINE IN A SINGLE CONTAIMER
		self.ip_list_new = []																# LIST OF IP ADDRESSES OBTAINED FROM COMMANDINE		
		self.interface = []																	# LIST SAVES THE EACH INTERFACE INFORMATION IN A SEPERATE CONTAINER
		self.data = ""																		# FINAL DATA WOULD BE SAVED IN THIS VARIABLE IN FORMATTED WAY
		self.mac_list = []																	# SAVING  INTERFACE MAC ADDRESSES IN A LIST
	
	def work(self):
		'''
		work() DOCFILE:
			work() RETURNS A SIBGLE STRING CONTAINING FORMATTED NETWORK INFORMATION CONTAINING IP ADDRESSES, INTERFACE DATA AND MAC ADDRESSES
		'''

		# COLECTING IP, MAC, AND INTERFACE DATA
		self.mac_list = os.popen("cat /sys/class/net/*/address").read().split('\n')			# READING MAC ADDRESSES FROM COMMANDLINE AND SAVING THEM AS A STRING
		self.ip_list = os.popen("ifconfig | grep 'inet.*broadcast'").read().split(" ")		# READING IP_ADDRESSES IN ASTRING FROM COMMANDLINE
		self.interface = os.popen("nmcli dev status").read().split('\n')					# READING INTERFACE DATA AND 
		
		# REMOVING REDUNDANT LIST ELEMENTS CREATED DURING SPLITTING
		try:
			while True:
				self.ip_list.remove("")
		except Exception as e:
			pass

		# CREATING NEW SUBLIST IN IP LIST WITH IP TYPE AND IP ADDESS TOGEHER
		for i in range(0, len(self.ip_list), 2):
			self.ip_list_new.append([self.ip_list[i],self.ip_list[i+1]])

		# REFINING INTERFACE LIST
		self.interface = self.interface[1:len(self.interface)-1]							# REMOVING FIRST AND LAST ELEMENT i.e. TITLES AND REDUNDANT ELEMENT IN LAST
		self.interface = [inter.split('  ') for inter in self.interface]					# CREATING SUBLIST OF ELEMENTS OF CURRENT LIST CONTAINIG EACH INTERFACE DATA SEPERATELY

		# REMOVING REDUNDANT ELEMENTS IN INTERFACE LIST
		for inter in self.interface:
			try:
				while True:
					inter.remove('')
					if ' ' in inter:
						inter.remove(' ')	
			except Exception as e:
				pass
		# REMOVING REDUNDANT ELEMENTS IN INTERFACE LIST		
		try:
			while True:
				self.mac_list.remove('')
		except:
			pass

		# ADDING MAC ADDRESSES TO RESPECTED INTERFACE LIST
		for i in range(0,len(self.mac_list)):
			self.interface[i].append(self.mac_list[i])

		# IF MAC ADDRESS IS NOT FOUND ON ANY INTERFACE, SO ADDING INFORMATION 
		for single in self.interface:
			if len(single) != 5:
				single.append("No Mac Address Attached")

		# NOW COLLECTING DATA IN A SINGLE VARIABLE
		self.data = "------------------------------------------- IP ADDRESS INFO ---------------------------------------\n"
		if len(self.ip_list_new) != 0:
			self.data += tabulate(self.ip_list_new, headers=['IP TYPE', "IP ADDRESS"])
		else:
			self.data += "No Active Internet Connection Found, So No IP Recognized."
		self.data += "\n\n--------------------------------------- INTERFACE STATUS ------------------------------------------\n"
		self.data += tabulate(self.interface, headers=['DEVICE INTERFACE', 'DEVICE TYPE',  'CONNECTION STATUS', 'DEVICE STATE', 'MAC ADDRESS'])
		self.data += "\n"

		# RETURNING FINALISED FORMATTED DATA
		return self.data
