'''
	Author : Deepak Chauhan
	GitHub : https://github.com/royaleagle73
	Email : 2018PGCACA63@nitjsr.ac.in
'''
import os
from tabulate import tabulate

class get_hw_info:
	'''
	get_hw_info HAVE A SINGLE METHOD AND A CONSTRUCTOR FUNCTION WHICH ARE NAMED AS :
		1) __init__
		2) work()
			__init__ DOCFILE:
				__init__ CONTAINS INITIALISED AND UNINITIALISED VARIABLES FOR LATER USE BY CLASS METHODS. 
			WORK() DOCFILE:
				work() RETURN A DATA VARIABLE CONTAINING GIVEN DATA :
					1) BASIC INFORMATION 
					2) MEMORY STATISTICS
					3) INSTALLED DRIVERS LIST 
	'''
	def __init__(self):
		'''
		__init__ DOCFILE:
			__init__ CONTAINS INITIALISED AND UNINITIALISED VARIABLES FOR LATER USE BY CLASS METHODS. 
		'''
		self.mem_info = ""																							# TO SAVE MEMORY INFO
		self.drivers = []																							# TO SAVE LIST OF INSTALLED DRIVERS
		self.drivers_data = []																						# TO SAVE MODIFIED DATA INTO A SEPERATE LIST
		self.cpu_info = []																							# TO SAVING CPU INFORMATION
		self.ram_size = " "																							# TO SAVE RAM SIZE			
		self.data = ""																								# TO SAVE THE FINALIZED DATA TO BE RETURNED	

	def work(self):
		'''
		WORK() DOCFILE:
			work() RETURN A DATA VARIABLE CONTAINING GIVEN DATA :
				1) BASIC INFORMATION 
				2) MEMORY STATISTICS
				3) INSTALLED DRIVERS LIST 
		'''

		# CPU INFO
		self.cpu_info = os.popen("lscpu | grep -e 'Model name' -e 'Architecture'").read().split('\n')				# COOLLECTING CPU INFO AND SAVING IT IN A LIST
		(self.cpu_info[0], self.cpu_info[1]) = (self.cpu_info[1], self.cpu_info[0])									# REARRANGING DATA
		self.cpu_info = [cpu.split('  ') for cpu in self.cpu_info]													# SPLITTING LIST ELEMENTS INTO A SUBLIST
		self.cpu_info.pop()																							# REMOVING LAST ELEMENTS

		for cpu in self.cpu_info:																					# REMOVING EXTRA ELEMENTS									
			cpu[0] = cpu[0][:len(cpu[0])-1]																			# REMOVING ':' FROM FIRST ELEMENTS OF THE LIST
			try:
				while True:
					cpu.remove('')
			except Exception as e:
				pass

		# KERNEL DRIVERS
		self.drivers = os.popen("ls -l /lib/modules/$(uname -r)/kernel/drivers/").read().split('\n')				# COLLECTING DRIVER DETAILS
		self.drivers = [drive.split(' ') for drive in self.drivers]													# SPLITTIG DATA 		
		self.drivers.pop(0)																							# REMOVING REDUNDANT FIRST
		self.drivers.pop()																							# REMOVING LAST ELEMENT				
		self.drivers = [driver[len(driver)-1] for driver in self.drivers]

		for index in range(0,len(self.drivers),4):																	# LISTING ELEMENTS INTO FOUR SEPERATE LISTS
			try:
				self.drivers_data.append([ self.drivers[index], self.drivers[index+1], self.drivers[index+2], self.drivers[index+3]])
			except:
				try:
					self.drivers_data.append([ self.drivers[index], self.drivers[index+1], self.drivers[index+2]])
				except:
					try:
						self.drivers_data.append([ self.drivers[index], self.drivers[index+1]])
					except:
						self.drivers_data.append([ self.drivers[index] ])


		# MEMORY INFO
		self.mem_info = os.popen("free").read().split('\n')															# SAVING MEMORY STATS INTO LIST
		self.mem_info = [mem.split(" ") for mem in self.mem_info]													# SUBLISTING THE ELEMENTS IN LIST

		for mem in self.mem_info:																					# REMOVING REDUNDANT ELEMENTS FROM LIST
			try:
				while True:
					mem.remove('')
			except Exception as e:
				pass
		self.mem_info.pop()																							# REMOVING LAST REDUNDANT ELEMENT
		self.mem_info[0].insert(0, 'Memory Type')																	# INSERTNG NEW HEADER ELEMENT AT START OF LIST

		for mem in self.mem_info[1:]:																				# CONVERTING kB DATA TO gB AND ADDING GB AT END OF MEMORY STAT
			for m in range(1,len(mem)):
				 mem[m] = str(int(mem[m])/1000000) + " GB"

		for mem in self.mem_info:																					# ADDING - AT MISSING DATA
			if len(mem) <= len(self.mem_info[0]):
				for i in range(0, len(self.mem_info[0]) - len(mem)):
					mem.append('-')

		# RAM SIZE
		self.ram_size = self.mem_info[1][1]																			# COLLECTING INSTALLED MEMORY INFO FROM MEMORY STATS
		self.cpu_info.append(["Installed RAM", self.ram_size])														# ADDING THIS DATA INTO LIST CONTAINIMG BASIC DETAILS


		# SAVING DATA INTO A DATA VARIABLE WHICH CAN BE RETURNED LATER
		self.data += "-------------------- BASIC INFORMATION --------------------\n"
		self.data += tabulate(self.cpu_info, headers=['PROPERTY', 'VALUE'],tablefmt="fancy_grid")
		self.data += "\n\n\n--------------------------------------- MEMORY STATS ---------------------------------------\n"
		self.data += tabulate(self.mem_info[1:], headers=self.mem_info[0],tablefmt="fancy_grid")
		self.data += "\n\n\n-------------- DRIVERS INSTALLED --------------\n"
		self.data += tabulate(self.drivers_data, headers=['LIST 1','LIST 2','LIST 3','LIST 4'],tablefmt="fancy_grid")

		# RETURNING DATA VARIABLE
		return self.data

l = get_hw_info()
print(l.work())