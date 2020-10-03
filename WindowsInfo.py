from lib.windows import SystemInfo,NetworkInfo,SoftwareInfo,StorageInfo
from lib.windows import HardwareInfo,DeviceInfo,ServiceInfo
import json
import pickle

def Display(d, indent=0):
   return json.dumps(d,sort_keys=True, indent=4)


def SavePickle(data):
   with open('result.pickle','wb') as file:
         pickle.dump(data,file)
         
def CallData():
   Container={'system':SystemInfo.SystemInfo().GetSystemInfo(),
              'hardware':HardwareInfo.HardwareInfo().getHardwareinfo(),
              'network':NetworkInfo.NetworkInfo().networkinfo(),
              'software':SoftwareInfo.SoftwareInfo().getSoftwareList(),
              'device':DeviceInfo.DeviceInfo().GetDeviceInfo(),
              'storage':StorageInfo.StorageInfo().getStorageinfo(),
              'service':ServiceInfo.ServiceInfo().getServiceInfo()
              }
   #Pretty Print Result
   cdata=Display(Container)
   SavePickle(Container)

   
try:
   CallData()
except Exception as ex:
   print(ex)
else:
   print("Now Run \npython MainUi.py")
   
