import os
from tabulate import tabulate

class get_drives:
	'''
	********* THIS SCRIPT RETURNS A VARIABLE CONTAINING DISK INFO IN HUMAN READABLE FORMT *********
	CLASS get_drives DOCINFO:
	get_drives HAVE TWO FUNCTIONS I.E.,
	1) __init__
	2) work()
		
		__init__ DOCFILE: 
			__init__ BLOCK SERVES THE INITIALIZATION FUNCTION, CONTAINING INITIALIZED VARIABLES WHICH IS GOING TO BE USED LATER BY OTHER MEMBER FUNCTION.
		
		WORK() DOCFILE:
			THE FUNCTION WORKS IN FOLLOWING WAY:
			1) COLLECTING DATA FROM COMMANDLINE, AND SAVING IT INTO A LIST.
			2) REMOVING REDUNDANT DATA FROM LIST, AND MAKING SUBLIST OF ITEMS SO THAT THEY CAN BE USED  LATER AS A SINGLE VARIABLE.
			3) COLLECTING NAME OF ALL PARTITIONS AND CREATING A LIST OF AVAILABLE DISKS FROM PARTITIONS.
			4) FINDING THE DISK AND PARTITION ON DISK HAVING LINUX BOOT FILES.
			5) SAVING THE REFINED DATA IN A TABULAR FORMAT IN A SINGLE VARIABLE
			6) RETURNING THE OBTAINED DATA IN A STRING VARIABLE.
		

	'''
	def __init__(self):
		'''
		__init__ DOCFILE: 
			__init__ BLOCK SERVES THE INITIALIZATION FUNCTION, CONTAINING INITIALIZED VARIABLES WHICH IS GOING TO BE USED LATER BY OTHER MEMBER FUNCTION.
		'''	
		self.data = ""																			# FOR SAVING DATA COLLECTED INTO A SINGLE VARIABLE
		self.temp_drive_list = []																# TO SAVE DRIVE LST TEMPORARILY
		self.boot_partition = ""																# STRING TO SAVE PARTITION NAME CONTAINING BOOT PARTITION
		self.drives = []																		# LIST TO STORE ALL THE DRIVE INFO COLLECTED FOR LATER USE


	def work(self):
		'''
			WORK() DOCFILE:
				THE FUNCTION WORKS IN FOLLOWING WAY:
				1) COLLECTING DATA FROM COMMANDLINE, AND SAVING IT INTO A LIST.
				2) REMOVING REDUNDANT DATA FROM LIST, AND MAKING SUBLIST OF ITEMS SO THAT THEY CAN BE USED  LATER AS A SINGLE VARIABLE.
				3) COLLECTING NAME OF ALL PARTITIONS AND CREATING A LIST OF AVAILABLE DISKS FROM PARTITIONS.
				4) FINDING THE DISK AND PARTITION ON DISK HAVING LINUX BOOT FILES.
				5) SAVING THE REFINED DATA IN A TABULAR FORMAT IN A SINGLE VARIABLE
				6) RETURNING THE OBTAINED DATA IN A STRING VARIABLE.
		'''
		disks_available = os.popen("df -h | grep -e '/dev/'").read()							# READINGA ALL DRIVE INFO AND GRASPING ONLY PARTITIONS WHICH ARE READABLE TO USER
		disk_list = disks_available.split('\n')													# SAVING THE DATA COLLECTED IN A LIST FORMAT
		disk_list = [file.split(' ') for file in disk_list]										# SPLITTIG EACH DATA BLCOK INTO IT'S SUB-LIST SO THAT EACH MODULE CAN BE USED AS VARIABLE
		for disk in disk_list:																	# REMOVING DRIVE LISTS WHICH ARE NOT REQUIRED
			if not '/dev/' in disk[0]:
				disk_list.remove(disk)

		while True:																				# WHILE FUNCTION TO REMOVE INDUCED SPACES IN LIST WHOSE SIZE IS 0 OR ARE WHITESPACE
			flag = True
			for disk in disk_list:
				for element in disk:
					if len(element)==0 or element == '':
						disk.remove(element)
						flag = False
			if  flag:
				break


		# For claculating number of devices
		for disk in disk_list:																	
			disk_name = disk[0]																	# SAVING PARTITION NAME IN A TEMPORARY VARIABLE
			for i in range(len(disk_name)-1, 0, -1):											# TRACING NAME FROM REAR END 
				if not disk_name[i].isdigit():													# REMOVING NUMBER AT THE END OF VARIABLE NAME, SO THAT COMMON DRIVE CAN BE FETCHED
					disk_name = disk_name[0:i+1]
					break
			if not disk_name in self.drives:													# IF RECIEVED NAME IS NOT IN DRIVE LIST, IT IS ADDED TO THE LIST
				self.drives.append(disk_name)


		# For calculating boot partition
		for disk in disk_list:																	# FINDING THE BOOT PARTITION AND DRIVE HAVIG THE BOOT PARTITION
			if disk[5] == "/boot":
				self.boot_partition = disk[0]


		# WRITING DATA INTO A VARIABLE FOR BOOT DRIVE
		for drive in self.drives:
			if drive in self.boot_partition:
				self.data += "------------------------------------------- DISK-1 ( Boot Drive ) --------------------------------------------\n"
				self.data += "Linux Installed On : %s\n\n"%(self.boot_partition)
				for disk in disk_list:
					if drive in disk[0]:
						self.temp_drive_list.append(disk)
				self.data += tabulate(self.temp_drive_list, headers=['Partition Name', 'Total Size','Size Consumed', 'Size Remaining','Size Consumed( in percent )', 'Mounted On'],tablefmt="fancy_grid")
				self.drives.remove(drive)

		# WRITING DATA FOR REST OF DRIVES
		for drive in self.drives:
			self.data += "\n\n\n\n\n"
			self.data += "-------------------------------------------------------- DISK-%d --------------------------------------------------------\n"%(self.drives.index(drive)+2)
			self.temp_drive_list.clear()
			for disk in disk_list:
				if drive in disk[0]:
					self.temp_drive_list.append(disk)
			self.data += tabulate(self.temp_drive_list, headers=['Partition Name', 'Total Size','Size Consumed', 'Size Remaining','Size Consumed( in percent )', 'Mounted On'],tablefmt="fancy_grid")
			self.data += "\n\n\n\n\n"

		return self.data
