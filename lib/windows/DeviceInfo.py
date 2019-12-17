from lib.windows.common.CommandHandler import CommandHandler
from lib.windows.common import Utility as utl

class DeviceInfo:
    def __init__(self):
        self.cmd=CommandHandler()
        
    def Preprocess(self,text):
        cmd=f'wmic {text} list /format:csv'
        Command_res=self.cmd.getCmdOutput(cmd)
        result=utl.CsvTextToDict(Command_res)
        return result
    
    def GetDeviceInfo(self):
        device_info={}
        device_list=['PRINTER','SOUNDDEV','DESKTOPMONITOR']
        for part in device_list:
            device_info[part]=self.Preprocess(part)
        return device_info
