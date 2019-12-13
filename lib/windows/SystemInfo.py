from lib.windows.common.RegistryHandler import RegistryHandler
from datetime import datetime
import platform



class SystemInfo:
    '''
    Class Name:SystemInfo
    Desciption:this class used to fetch the operating system related information

    call this method to get all system related data:
        objectName.GetSystemInfo()
    
    '''
    def getPlatform(self,name):
        '''Return a string machine platform windows or ubuntu

            call this method
            objectName.getPlatform()
        '''
        try:
           return getattr(platform, name)()
        except:
            return None
    def getMachineName(self):
        '''Return machine name

            call this method
            objectName.getMachineName()
        '''
        try:
            return platform.node()
        except:
            return None
        
    def get_reg_value(self,name):
        '''Return string value of given key name inside windows registery

            Hkeys=reg.HKEY_LOCAL_MACHINE
            path=r'SOFTWARE\Microsoft\Windows NT\CurrentVersion'
            
            call this method
            objectName.get_reg_value(name)
        '''
        try:
            path=r'SOFTWARE\Microsoft\Windows NT\CurrentVersion'
            reg=RegistryHandler("HLM",path)
            return reg.getValues(name)
        except:
            return None
        
    def GetSystemInfo(self):
        '''
        This Method Return a dictionary object of  System Information using Windows Registery and module platform

        class this method
            objectname.GetSystemInfo()
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
                system_data[name]=str(datetime.fromtimestamp(value))
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

