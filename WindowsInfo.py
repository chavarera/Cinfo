from lib.windows import SystemInfo,NetworkInfo,SoftwareInfo,StorageInfo,HardwareInfo,FileInfo
import time
import pandas as pd
import json

def Display(d, indent=0):
   return json.dumps(d,sort_keys=True, indent=4)

Cinfo={}

sys_info=SystemInfo.SystemInfo()
Cinfo['system']=sys_info.GetSystemInfo()

hard_info=HardwareInfo.HardwareInfo()
Cinfo['hardware']=hard_info.getHardwareinfo()

net_info=NetworkInfo.NetworkInfo()
Cinfo['network']=net_info.networkinfo()

soft_info=SoftwareInfo.SoftwareInfo()
Cinfo['software']=soft_info.getSoftwareList()

Cinfo['webbrowser']=soft_info.GetInstalledBrowsers()

storage_info=StorageInfo.StorageInfo()
Cinfo['storage']=storage_info.getStorageinfo()

cdata=Display(Cinfo)
print(cdata)
