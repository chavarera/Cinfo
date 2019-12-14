'''
	Author : Deepak Chauhan
	GitHub : https://github.com/royaleagle73
	Email : 2018PGCACA63@nitjsr.ac.in
'''
import os
from tabulate import tabulate

class get_os_info:
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
		temp_container = []

		## LIST CONVERSION 
		os1 = os_ker_arch.split('\n')
		os1.pop()
		os2 = os_more.split("\n")

		# OS-DETAILS ADDED HERE
		for fetch in range(2, len(os1)):
			temp_container.append(os1[fetch].split(':'))

		temp_container.append(os1[0].split(':'))
		temp_container.append(os1[1][1:].split(':'))
		self.details += tabulate(temp_container, headers = ["Property", "Value"],tablefmt="fancy_grid")
		temp_container.clear()

		self.details += "\n\n\n------------------------------ CPU Information ------------------------------\n"

		# CPU-INFORMTION ADDED HERE
		for fetch in range(4, 10):
			temp_container.append(os2[fetch].split(':'))

		temp_container.append(os2[2].split(':'))
		temp_container.append(os2[3].split(':'))
		temp_container.append(os2[0].split(':'))
		temp_container.append(os2[1].split(':'))
		
		
		for fetch in range(10, len(os2)):
			temp_container.append(os2[fetch].split(':'))

		self.details += tabulate(temp_container, headers = ["Property", "Value"],tablefmt="fancy_grid")
		
		# FETCHING USERNAMES FROM OS
		user_name_string = os.popen("lslogins -u").read()
		user_name_list = user_name_string.split('\n')
		user_name_list.pop()
		user_names = "root\n"
		final_usernames = []
		
		for user in user_name_list:
			final_usernames.append(user.split(" ")[1])
		final_usernames.pop(0)
		temp_container.clear()
		temp_container.append(["root"])
		for user in final_usernames:
			if user != '':
				temp_container.append([user])
				
		self.details += "\n\n\n------------------------------ Users in Machine ------------------------------\n"
		self.details += tabulate(temp_container, headers = ["Usernames"],tablefmt="fancy_grid")

		# RETURNING ALL FINALISED DETAILS
		return self.details