
from lib.windows.common.CommandHandler import CommandHandler
from lib.windows.common.RegistryHandler import RegistryHandler

class HardwareInfo:
    '''
    class_Name:HardwareInfo
    Output:Return bios,cpu,usb information

    Functions:
    getBiosInfo()
    getCpuInfo(self)
    usbPortInfo(self)
    '''
    def __init__(self):
        self.cmd=CommandHandler()
        
    def getBiosInfo(self):
        '''
        Usage :object.getBiosInfo()
        Find Bios Info and Return Dictionary Object
        
        Output:
        biosinfo--> An Dictionary Object
        Sample-->{'Manufacturer': 'XXX',
                'SerialNumber': 'XXXXXXXXXXX',
                'SMBIOSBIOSVe': 'XXXXXXXX
                }
        '''
        biosinfo={}
        cmd='wmic BIOS get Manufacturer,SerialNumber,SMBIOSBIOSVersion'
        result=self.cmd.getCmdOutput(cmd)
        data=[val.split() for val in result.splitlines() if len(val.split())==3]
        for key,val in zip(data[0],data[1]):
            bios={}
            if key=="SMBIOSBIOSVersion":
                biosinfo["SMBIOSBIOSVe"]=val
            else:
                biosinfo[key]=val
        return biosinfo
    
    def getCpuInfo(self):
        '''
        Usage :object.getCpuInfo()
        Find CPU Info and Return Dictionary Object
        
        Output:
        cpuinfo--> An Dictionary Object
        Sample-->{'Name OF The cpu': 'XXXXXXXXX',
                'Number Of Cores': '2',
                'Logical Proces.': '2'}

        '''
        cpuinfo={}
        cmd='wmic CPU get Name,NumberOfCores,NumberOfLogicalProcessors'
        result=self.cmd.getCmdOutput(cmd)
        data=result.splitlines()
        n=0
        for i in data[0].split():
            if n==0:
                cpuinfo["Name of the cpu"]=" ".join(data[2].split()[:-2])
            if n==1:
                cpuinfo["Number of cores"]=data[2].split()[-2]
            if n==2:
                cpuinfo["Logical proces."]=data[2].split()[-1]
            n=n+1    
        return cpuinfo
    
    def usbPortInfo(self):
        '''
        Usage :object.usbPortInfo()
        Find USB Port Info and Return Dictionary Object
        
        Output:
        cpuinfo--> An Dictionary Object
        Sample-->{'ROOT_HUB2': 2, 'ROOT_HUB3': 1}
        '''
        Usb_List={}
        key='HLM' #HKEY_LOCAL_MACHINE
        for i in ['ROOT_HUB20','ROOT_HUB30']:            
            path=r'SYSTEM\CurrentControlSet\Enum\USB\{}'.format(i)
            reg_=RegistryHandler(key,path)
            count=reg_.getKeys()
            Usb_List[i[:-1]]=count
        return Usb_List

    def getHardwareinfo(self):
        '''
        usage:object.getHardwareinfo()
        Return bios,cpu,usb information
        '''
        hardwarinfo={}
        hardwarinfo['bios']=self.getBiosInfo()
        hardwarinfo['cpu']=self.getCpuInfo()
        hardwarinfo['usb']=self.usbPortInfo()
        return hardwarinfo


