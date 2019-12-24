
from lib.windows.common.CommandHandler import CommandHandler
from lib.windows.common.RegistryHandler import RegistryHandler
from lib.windows.common import Utility as utl
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
        
    def Preprocess(self,text):
        cmd=f'wmic {text} list /format:csv'
        Command_res=self.cmd.getCmdOutput(cmd)
        result=utl.CsvTextToDict(Command_res)
        return result

    
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
        biosinfo=self.Preprocess('bios')
        return biosinfo
    
    def CsProduct(self):
        computer_systemP=self.Preprocess('CSPRODUCT')
        return computer_systemP
    
    def getCpuInfo(self):
        cpuinfo=self.Preprocess('cpu')
        return cpuinfo
    
    def getBaseboard(self):
        Baseboard=self.Preprocess('BASEBOARD')
        return Baseboard
    
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
        hardwarinfo={
                     'usb':[self.usbPortInfo()]
            }
        Hardware_parameter=['onboarddevice','bios','cpu','BASEBOARD','CSPRODUCT','PORTCONNECTOR','SYSTEMSLOT']
        for part in Hardware_parameter:
            hardwarinfo[part]=self.Preprocess(part)
        
        return hardwarinfo


