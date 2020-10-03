'''
	Author : Deepak Chauhan
	GitHub : https://github.com/royaleagle73
	Email : 2018PGCACA63@nitjsr.ac.in
'''
import os

class get_network_info:
	'''
	CLASS get_network_info PROVIDES THE CURRENT NETWORK CONNECTION STATUS, IP ADDRESS, NET MASK ADDRESS AND BROADCAST ADDRESS ALONGWITH ALL INTERFACE STATS.
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
		self.data = ""																		# FINAL DATA WOULD BE SAVED IN THIS VARIABLE IN FORMATTED WAY
		self.current_path = os.getcwd()														# TO SAVE CURRENT DIRECTORY PATH		
	
	def work(self):
		'''
		work() DOCFILE:
			work() RETURNS A SIBGLE STRING CONTAINING FORMATTED NETWORK INFORMATION CONTAINING IP ADDRESSES, INTERFACE DATA AND MAC ADDRESSES
		'''
		ret_data = {}
		temp_list = []
		temp_key = ""
		self.data += os.popen("nmcli -p device show").read()													# GETTING DATA FROM COMMAND LINE
		self.data = self.data.replace("-","")
		self.data = self.data.replace("GENERAL.","")
		## REMOVinG EXTRA LINES WITH NO LETTERS 
		for i in self.data.split('\n'):
			if i != '' and i.find('=') == -1:
				if i.find('Device details') != -1:
					temp_key = i.split('(')[1].split(')')[0]
					ret_data[temp_key] = [["Property", "Value"]]
				elif i.split(':')[1].strip() is not '':
					ret_data[temp_key].append([i.split(':')[0],i.split(':')[1].strip()])

		# if self.current_path.find("output") == -1:																# CHECKING IF CURRENT WORKING DIRECTORY IS OUTPUT FOLDER
		# 	self.current_path += "/output/"
		# os.chdir(self.current_path)																				# CHANGING CURRENT WORKING DIRECTORY
		# with open("network_info.txt","w") as network:															# SAVNG DATA INTO FILE
		# 	network.write(self.data)
		
		return ret_data																				# RETURNING FILE NAME FOR SUCCESSFUL RETURNS