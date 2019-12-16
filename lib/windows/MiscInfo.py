from lib.windows.common.CommandHandler import CommandHandler
from lib.windows.common import Utility as utl
class MiscInfo:
    
    def __init__(self):
        self.cmd=CommandHandler()
        
    def Preprocess(self,text):
        cmd=f'wmic {text} list /format:csv'
        Command_res=self.cmd.getCmdOutput(cmd)
        result=utl.CsvTextToDict(Command_res)
        return result
    def getMiscInfo(self):
        misc_info={}
        misc_list=['ENVIRONMENT','GROUP','LOGON','REGISTRY','SYSACCOUNT','USERACCOUNT']
        for part in misc_list:
            misc_info[part]=self.Preprocess(part)
        return misc_info
