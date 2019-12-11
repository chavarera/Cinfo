import os
from tabulate import tabulate
from lib.linux import get_browsers
from lib.linux import get_drives
from lib.linux import get_hw_info
from lib.linux import get_network_info
from lib.linux import get_os_info
from lib.linux import get_package_list
from lib.linux import get_ports
from lib.linux import get_startup_list

## Creating objects for the classes in import files
packages = get_package_list.get_package_list()
startup = get_startup_list.get_startup_list()
network = get_network_info.get_network_info()
browsers = get_browsers.get_browsers()
ports = get_ports.get_ports()
drives = get_drives.get_drives()
os_info = get_os_info.get_os_info()
hardware = get_hw_info.get_hw_info()

print("Tool Started... Wait for a moment...")

file_names = []

## WRITING MACHINE INFORMATION
try:
	os.popen("clear")
	print("/...")
	data = os_info.work()+"\n\n"+hardware.work()+"\n\n"+drives.work()+"\n\n"
	current_path = os.getcwd()
	if current_path.find("output") == -1:													# CHECKING IF CURRENT WORKING DIRECTORY IS OUTPUT FOLDER
		current_path += "/output/"
	os.chdir(current_path)																	# CHANGING CURRENT WORKING DIRECTORY
	with open("About Your Machine.txt","w") as about:											# SAVNG DATA INTO FILE
		about.write(data)
	os.popen("clear")
	print("\\...")
	file_names.append[["Computer information","About Your Machine.txt"]]
except Exception as e:
	file_names.append(["Computer Information","About Your Machine.txt"])

## WRIITING NETWORK INFORMATION
try:
	os.popen("clear")
	print("/...")
	file_names.append(["Network Information",network.work()])
	os.popen("clear")
	print("\\...")
except Exception as e:
	file_names.append(["Network Information","Error getting information"])

## WRIITING OPEN PORTS INFORMATION
try:
	os.popen("clear")
	print("/...")
	file_names.append(["Open Ports in Machine",ports.work()])
	os.popen("clear")
	print("\\...")
except Exception as e:
	file_names.append(["Open Ports in Machine","Error getting information"])

## WRIITING INSTALLED BROWSER INFORMATION
try:
	os.popen("clear")
	print("/...")
	file_names.append(["Installed Browsers",browsers.work()])
	os.popen("clear")
	print("\\...")
except Exception as e:
	file_names.append(["Installed Browsers","Error getting information"])

## WRIITING INSTALLED PACKAGES INFORMATION
try:
	os.popen("clear")
	print("/...")
	file_names.append(["Installed Packages",packages.work()])
	os.popen("clear")
	print("\\...")
except Exception as e:
	file_names.append(["Installed Packages","Error getting information"])

## WRIITING STARTUP APPLICATIONS INFORMATION
try:
	os.popen("clear")
	print("/...")
	file_names.append(["Startup Application",startup.work()])
	os.popen("clear")
	print("\\...")
except Exception as e:
	file_names.append(["Startup Application","Error getting information"])


os.popen("clear")
print("/...")
print("Work Done...\n\n")
os.popen("clear")
print("You can find OUTPUT reports with mentioned file names in output folder...\n\n")


print(tabulate(file_names, headers=["Property", "File Name"],tablefmt="fancy_grid"))

print('\n\n\n')