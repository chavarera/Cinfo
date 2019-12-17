from lib.windows.common.CommandHandler import CommandHandler
from lib.windows.common import Utility as utl

class ServiceInfo:
    def __init__(self):
        self.cmd=CommandHandler()
        
    def Preprocess(self,text):
        cmd=f'wmic {text} list /format:csv'
        Command_res=self.cmd.getCmdOutput(cmd)
        result=utl.CsvTextToDict(Command_res)
        return result
    
    def getServiceInfo(self):
        Service_info={}
        Service_list=['LOADORDER','PROCESS','RDACCOUNT']
        for part in Service_list:
            Service_info[part]=self.Preprocess(part)
        return Service_info
