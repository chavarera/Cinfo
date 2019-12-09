from subprocess import getoutput
from lib.windows.common.RegistryHandler import RegistryHandler
class HardwareInfo:
    def getCmdOutput(self,cmd):
        '''
        Accept the Command prompt query and Return the Output into text format
        '''
        try:
            return getoutput(cmd)
        except Exception as ex:
            return ex
    def getBiosInfo(self):
        biosinfo=[]
        cmd='wmic BIOS get Manufacturer,SerialNumber,SMBIOSBIOSVersion'
        result=self.getCmdOutput(cmd)
        data=[val.split() for val in result.splitlines() if len(val.split())==3]
        for key,val in zip(data[0],data[1]):
            bios={}
            if key=="SMBIOSBIOSVersion":
                bios["SMBIOSBIOSVe"]=val
            else:
                bios[key]=val
            biosinfo.append(bios)
        return biosinfo
    def getCpuInfo(self):
        cpuinfo=[]
        cmd='wmic CPU get Name,NumberOfCores,NumberOfLogicalProcessors'
        result=self.getCmdOutput(cmd)
        data=result.splitlines()
        n=0
        for i in data[0].split():
            res={}
            if n==0:
                res["Name OF The cpu"]=" ".join(data[2].split()[:-2])
            if n==1:
                res["Number Of Cores"]=data[2].split()[-2]
            if n==2:
                res["Logical Proces."]=data[2].split()[-1]
            cpuinfo.append(res)
            n=n+1    
        return cpuinfo
    
    def UsbPortInfo(self):
        Usb_List={}
        key='HCM' #HKEY_LOCAL_MACHINE
        for i in ['ROOT_HUB20','ROOT_HUB30']:            
            path=r'SYSTEM\CurrentControlSet\Enum\USB\{}'.format(i)
            reg_=RegistryHandler(key,path)
            count=reg_.getKeys()
            Usb_List[i[:-1]]=count
        return Usb_List

    def getHardwareinfo(self):
        hardwarinfo={}
        hardwarinfo['bios']=self.getBiosInfo()
        hardwarinfo['cpu']=self.getCpuInfo()
        return hardwarinfo

