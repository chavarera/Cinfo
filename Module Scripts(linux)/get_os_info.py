import os

class get_base_info:
	'''
	CLASS get_base_info PROVIDES ALL DETAILS REGARDING OS, CPU AND USERS IN MACHINE,
	IT CONTAINS TWO FUNCTIONS I.E.
	1) __init__
	2) work()
		__init__ DOCKINFO:
		THIS BLOCK CONTAINS A SIGLE INITIALISED VARIABLES THAT WILL CONTAIN ALL THE INFORMATION RELATED TO OS, CPU, AND USERS IN MACHINE.
		
		work() DOCINFO:
		THIS FUNCTIONS WORKS IN THE FOLLOWING WAYS:
		1) CAPTURING DETAILS.
		2) FORMATTING THE OUPUT.
		3) SAVING THE OUTPUT IN A VARIABLE.
		4) THE VARIABLE IS THEN FINALLY RETURNED.
		
	'''
	def __init__(self):
		'''
		__init__ DOCKINFO:
		THIS BLOCK CONTAINS A SIGLE INITIALISED VARIABLES THAT WILL CONTAIN ALL THE INFORMATION RELATED TO OS, CPU, AND USERS IN MACHINE.
		'''
		self.details = "------------------------------ OS Information ------------------------------\n"

	def work(self):
		'''
		work() DOCINFO:
		THIS FUNCTIONS WORKS IN THE FOLLOWING WAYS:
		1) CAPTURING DETAILS.
		2) FORMATTING THE OUPUT.
		3) SAVING THE OUTPUT IN A VARIABLE.
		4) THE VARIABLE IS THEN FINALLY RETURNED.
		'''
		os_ker_arch = os.popen("hostnamectl | grep -e 'Machine ID' -e 'Boot ID' -e 'Operating System' -e Kernel -e Architecture").read()
		os_more = os.popen("lscpu | grep -e 'Model name' -e 'CPU MHz' -e 'CPU max MHz' -e 'CPU min MHz' -e 'CPU op-mode(s)' -e 'Address sizes' -e 'Thread(s) per core' -e Kernel -e 'Core(s) per socket' -e 'Vendor ID' -e Virtualization -e 'L1d cache' -e 'L1i cache' -e 'L2 cache' -e 'NUMA node0 CPU(s)'").read()
		os_ker_arch = os_ker_arch.replace("  ", "")

		## LIST CONVERSION 
		os1 = os_ker_arch.split('\n')
		os1.pop()
		os2 = os_more.split("\n")

		# OS-DETAILS ADDED HERE
		for fetch in range(2, len(os1)):
			self.details += os1[fetch] + "\n"
		self.details += os1[0] + "\n"
		self.details += os1[1][1:] + "\n"
		self.details = self.details[1:]	

		self.details += "\n------------------------------ CPU Information ------------------------------\n"

		# CPU-INFORMTION ADDED HERE
		for fetch in range(4, 10):
			self.details += os2[fetch] + "\n"

		self.details += os2[2] + "\n"
		self.details += os2[3] + "\n"
		self.details += os2[0] + "\n"
		self.details += os2[1] + "\n"

		for fetch in range(10, len(os2)):
			self.details += os2[fetch] + "\n"

		# CALCULATING MIN AND MAX UID TO FIND ALL USERS
		min_max_UID = os.popen("grep -E '^UID_MIN|^UID_MAX' /etc/login.defs").read().split('\n')
		min_UID = int(min_max_UID[0][11:len(min_max_UID[0])])
		max_UID = int(min_max_UID[1][10:len(min_max_UID[1])])

		# FETCHING USERNAMES FROM OS
		user_name_string = os.popen("getent passwd {%d..%d}"%(min_UID, max_UID)).read()
		user_name_list = user_name_string.split('\n')
		user_name_list.pop()
		user_names = "root\n"
		for user in user_name_list:
			user_names += user.split(':')[0] + "\n"

		self.details += "------------------------------ Users in Machine ------------------------------\n"
		self.details += user_names

		# RETURNING ALL FINALISED DETAILS
		return self.details

