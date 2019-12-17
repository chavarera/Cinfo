from lib.windows import SystemInfo,NetworkInfo,SoftwareInfo,StorageInfo
from lib.windows import HardwareInfo,FileInfo,DeviceInfo,MiscInfo,ServiceInfo
from lib.windows.common import Utility as utl
import time
import pandas as pd
import json

def Display(d, indent=0):
   return json.dumps(d,sort_keys=True, indent=4)

Cinfo={}

Container={'system':SystemInfo.SystemInfo().GetSystemInfo(),
           'hardware':HardwareInfo.HardwareInfo().getHardwareinfo(),
           'network':NetworkInfo.NetworkInfo().networkinfo(),
           'software':SoftwareInfo.SoftwareInfo().getSoftwareList(),
           'device':DeviceInfo.DeviceInfo().GetDeviceInfo(),
           'webbrowser':SoftwareInfo.SoftwareInfo().GetInstalledBrowsers(),
           'storage':StorageInfo.StorageInfo().getStorageinfo(),
           'service':ServiceInfo.ServiceInfo().getServiceInfo()
           }

#Pretty Print Result
cdata=Display(Container)
print(cdata)

#Export to Json File
utl.ExportTOJson(cdata)
