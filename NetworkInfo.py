import socket
import subprocess
from uuid import getnode as get_mac
import SystemInfo
import re
class NetworkInfo:
    '''
    class Name:NetworkInfo
    Description: used to Find out network related information using ipconfig /all and os module

    To get All Network information call this method
        objectName.networkinfo()

    '''
    def parseipText(self,ip_output):
        ''' This Method Return a list of interface name and its key value
        You can Call this methods as follow
        objectname.parseipText(subprocess.check_output(["ipconfig", "/all"]))
        '''
        #final Output array
        final_output=[]
        lines=ip_output.splitlines()
        blanks=[idx for idx,line in enumerate(lines) if len(line.decode('utf-8'))==0]
        new_list=[]
        for i in range(0,len(blanks),2):
            if i+2<len(blanks):
                new_list.append([blanks[i]+1,blanks[i+2]-1])
            else:
                new_list.append([blanks[i]+1,blanks[i+1]])
        for n in new_list[:-1]:
            interface_data={}
            interface_data['name']=lines[n[0]].decode('utf-8')
            keys_value=[]
            for i in range(n[0]+2,n[1]+1):
                key_data={}
                result=lines[i].decode('utf-8').find(":")
                data=lines[i]
                keys=data[:result].decode('utf-8').replace(".","")
                values=data[result+2:].decode('utf-8')
                ks='{}'.format(keys.strip())
                if values.strip()!='':
                    vals=values.strip()
                    if ks=='Autoconfiguration Enabled':
                        ks='Config Enabled'
                    if ks=='Physical Address':
                        ks='Physical Addr.'
                    if ks=='IP Routing Enabled':
                        ks='Ip Route Enable'
                    if ks=='WINS Proxy Enabled':
                        ks='W proxy Enable'
                    if ks=='DHCPv6 Client DUID':
                        ks='DHCPv6 DUID'
                    if ks=='Link-local IPv6 Address':
                        ks='Link-local IPv6'
                    if ks=='NetBIOS over Tcpip':
                        ks='NetBIOS Tcpip'
                    key_data[ks]=values.strip()
                    keys_value.append(key_data)
            interface_data['details']=keys_value
            final_output.append(interface_data)
        return final_output
                
    
    def getIpConfig(self):
        ''' This Method returns the list of avialble intefaaces which is shown in
            ipconfig /all

            call this Method
                objectName.getIpConfig()
        '''
        try:
            results=subprocess.check_output(["ipconfig", "/all"])
            return self.parseipText(results)
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
            
    def networkinfo(self):
        '''
        This method retuns Complete Network Related Information
        call this Method
                objectName.networkinfo()
        '''
        #Save into result Dictionary
        final_result={}
        final_result['name']="Important Network Information"
        
        result=[]
        hstName={}
        ip={}
        mac={}
        
        #Network Related Information
        hstName['HostNodeName']=self.getNetworkName()
        result.append(hstName)
        ip['IpAddress']=self.getIpAddress()
        result.append(ip)
        mac['MacAddress']=self.getMacAddress()
        result.append(mac)
        
        final_result['details']=result
        
        #Ipconfig Network information
        res=self.getIpConfig()
        res.append(final_result)

        return res
