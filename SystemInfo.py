try:
    import _winreg as reg
except:
    import winreg as reg
from datetime import datetime
import platform
import os

class SystemInfo:
    def getPlatform(self,name):
        '''Return machine platform windows or ubuntu '''
        try:
           return getattr(platform, name)()
        except:
            return None
          
    def get_reg_value(self,name):
        try:
            Hkeys=reg.HKEY_LOCAL_MACHINE
            path=r'SOFTWARE\Microsoft\Windows NT\CurrentVersion'
            key = reg.OpenKey(Hkeys, path)
            value = reg.QueryValueEx(key, name)[0]
            reg.CloseKey(key)
            return value
        except:
            return None
        
    def GetSystemInfo(self):
        '''
        Get System Information using Windows Registery and module platform
        '''
        #Create a Dictionary object for saving all data
        system_data={}
        
        #Get System information using Registry
        reg_data=['ProductName','InstallDate','PathName','ReleaseId','CompositionEditionID','EditionID','SoftwareType',
      'SystemRoot','ProductId','BuildBranch','BuildLab','BuildLabEx','CurrentBuild']

        for name in reg_data:
            value=self.get_reg_value(name)
            
            if name=="CompositionEditionID":
                system_data["CompositionID"]=value
            elif name=="InstallDate":
                system_data[name]=datetime.fromtimestamp(value)
            else:
                system_data[name]=value
        #Get system information using platform module
        platform_data=['machine','node','platform','system','release','version','processor']
        platform_name=['Machine Name','Network Name','Platform Type','System Type','Release No ','Version No','Processor Name']
        for idx,name in enumerate(platform_data):
            value=self.getPlatform(name)
            names=platform_name[idx]
            system_data[names]=value

        return system_data
    
