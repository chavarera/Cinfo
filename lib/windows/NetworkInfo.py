import socket
from lib.windows.common.CommandHandler import CommandHandler
from uuid import getnode as get_mac
from lib.windows.common import Utility as utl
from lib.windows import SystemInfo 

class NetworkInfo:
    '''
    class Name:NetworkInfo
    Description: used to Find out network related information using ipconfig /all and os module

    To get All Network information call this method
        objectName.networkinfo()

    '''
    def __init__(self):
        self.cmd=CommandHandler()
    
    def getIpConfig(self):
        ''' This Method returns the list of avialble intefaaces which is shown in
            ipconfig /all

            call this Method
                objectName.getIpConfig()
        '''
        try:
            cmd=["ipconfig", "/all"]
            results=self.cmd.getCmdOutput(cmd)
            return results.splitlines()
        except:
            return None
        
    def getNetworkName(self):
        '''
        This method retuns an machine host name in Network
        call this Method
                objectName.getNetworkName()
        '''
        try:
            s1=SystemInfo.SystemInfo()
            return s1.getMachineName()
        except:
            return None
        
    def getIpAddress(self):
        '''
        This method retuns an machine Ip Address
        call this Method
                objectName.getIpAddress()
        '''
        try:
            return socket.gethostbyname(socket.gethostname())
        except Exception as ex:
            return None
        
    def getMacAddress(self):
        '''
        This method retuns an machine MAC Address
        call this Method
                objectName.getMacAddress()
        '''
        try:
            mac = get_mac()
            macid=':'.join(("%012X" % mac)[i:i+2] for i in range(0, 12, 2))
            return macid
        except Exception as ex:
            return None
    def Preprocess(self,text):
        cmd=f'wmic {text} list /format:csv'
        Command_res=self.cmd.getCmdOutput(cmd)
        result=utl.CsvTextToDict(Command_res)
        return result
    
    def networkinfo(self):
        '''
        This method retuns Complete Network Related Information
        call this Method
                objectName.networkinfo()
        '''
        network_info={}
        ipandmacAddress={}
        ipandmacAddress['HostNodeName']=self.getNetworkName()
        ipandmacAddress['IpAddress']=self.getIpAddress()
        ipandmacAddress['MacAddress']=self.getMacAddress()
        network_info['ipandmacAddress']=[ipandmacAddress]
        network_categories=['netclient','NETPROTOCOL','nic','RDNIC','NICCONFIG']
        for part in network_categories:
            network_info[part]=self.Preprocess(part)
        return network_info
