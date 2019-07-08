import os
from tabulate import tabulate

class get_hw_info:
	def __init__(self):
		self.mem_info = ""																							# TO SAVE MEMORY INFO
		self.drivers = []																							# TO SAVE LIST OF INSTALLED DRIVERS
		self.drivers_data = []																						# TO SAVE MODIFIED DATA INTO A SEPERATE LIST
		self.cpu_info = []																							# TO SAVING CPU INFORMATION
		self.ram_size = " "																							# TO SAVE RAM SIZE			
		self.data = ""																								# TO SAVE THE FINALIZED DATA TO BE RETURNED	

	def work(self):
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
		self.mem_info = os.popen("free").read().split('\n')
		self.mem_info = [mem.split(" ") for mem in self.mem_info]

		for mem in self.mem_info:
			try:
				while True:
					mem.remove('')
			except Exception as e:
				pass
		self.mem_info.pop()
		self.mem_info[0].insert(0, 'Memory Type')

		for mem in self.mem_info[1:]:
			for m in range(1,len(mem)):
				 mem[m] = str(int(mem[m])/1000000) + " GB"

		for mem in self.mem_info:
			if len(mem) <= len(self.mem_info[0]):
				for i in range(0, len(self.mem_info[0]) - len(mem)):
					mem.append('-')

		# RAM SIZE
		self.ram_size = self.mem_info[1][1]
		self.cpu_info.append(["Installed RAM", self.ram_size])

		self.data += "-------------------- BASIC INFORMATION --------------------\n"
		self.data += tabulate(self.cpu_info, headers=['PROPERTY', 'VALUE'])
		self.data += "\n\n\n--------------------------------------- MEMORY STATS ---------------------------------------\n"
		self.data += tabulate(self.mem_info[1:], headers=self.mem_info[0])
		self.data += "\n\n\n-------------- DRIVERS INSTALLED --------------\n"
		self.data += tabulate(self.drivers_data, headers=['LIST 1','LIST 2','LIST 3','LIST 4'])

		return self.data

