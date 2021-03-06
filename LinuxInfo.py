'''
	Author : Deepak Chauhan
	GitHub : https://github.com/royaleagle73
	Email : 2018PGCACA63@nitjsr.ac.in
'''
import os
import threading
from timeit import default_timer as timer
from tabulate import tabulate
from lib.linux import get_browsers
from lib.linux import get_drives
from lib.linux import get_hw_info
from lib.linux import get_network_info
from lib.linux import get_os_info
from lib.linux import get_package_list
from lib.linux import get_ports
from lib.linux import get_startup_list
from lib.linux import list_files

## Creating objects for the classes in import files
packages = get_package_list.get_package_list()
startup = get_startup_list.get_startup_list()
network = get_network_info.get_network_info()
browsers = get_browsers.get_browsers()
ports = get_ports.get_ports()
drives = get_drives.get_drives()
os_info = get_os_info.get_os_info()
hardware = get_hw_info.get_hw_info()
files = list_files.list_files()
file_names = []

def indexing():
	## ASKING FOR INDEXING 
	index_answer = input("Want to index all files in system, Y or N?\n(Note : It may take some time to index in first)\n")
	if index_answer == 'Y' or index_answer == 'y':
		try:
			if files.work() == True:
				file_names.append(["File Information","File list.csv"])
				file_names.append(["File Type Overview","File Overview.json"])
		except Exception as e:
			print("Error occured while indexing")
			file_names.append(["File Information","Error : try running with sudo"])
			file_names.append(["File Type Overview","Error, try running with sudo"])

def other_works():	
	## WRITING MACHINE INFORMATION
	try:
		data = os_info.work()+"\n\n"+hardware.work()+"\n\n"+drives.work()+"\n\n"
		current_path = os.getcwd()
		if current_path.find("output") == -1:													# CHECKING IF CURRENT WORKING DIRECTORY IS OUTPUT FOLDER
			current_path += "/output/"
		os.chdir(current_path)																	# CHANGING CURRENT WORKING DIRECTORY
		with open("About Your Machine.txt","w") as about:											# SAVNG DATA INTO FILE
			about.write(data)
		file_names.append[["Computer information","About Your Machine.txt"]]
	except Exception as e:
		file_names.append(["Computer Information","About Your Machine.txt"])

	## WRIITING NETWORK INFORMATION
	try:
		file_names.append(["Network Information",network.work()])
	except Exception as e:
		file_names.append(["Network Information","Error getting information"])

	## WRIITING OPEN PORTS INFORMATION
	try:
		file_names.append(["Open Ports in Machine",ports.work()])
	except Exception as e:
		file_names.append(["Open Ports in Machine","Error getting information"])

	## WRIITING INSTALLED BROWSER INFORMATION
	try:
		file_names.append(["Installed Browsers",browsers.work()])
	except Exception as e:
		file_names.append(["Installed Browsers","Error getting information"])

	## WRIITING INSTALLED PACKAGES INFORMATION
	try:
		file_names.append(["Installed Packages",packages.work()])
		
	except Exception as e:
		file_names.append(["Installed Packages","Error getting information"])

	## WRIITING STARTUP APPLICATIONS INFORMATION
	try:
		file_names.append(["Startup Application",startup.work()])
	except Exception as e:
		file_names.append(["Startup Application","Error getting information"])
	
	print("Please wait while indexing ends...")


t1 = threading.Thread(target=indexing)
t2 = threading.Thread(target=other_works)

start = timer()
t1.start()
t2.start()
t1.join()
end = timer()

print("Task done and dusted...\n\n")
print("You can find OUTPUT reports with mentioned file names in output folder...\n\n")
print("Task completed in %d seconds"%(end-start))

print(tabulate(file_names, headers=["Property", "File Name"],tablefmt="fancy_grid"))

print('\n\n\n')