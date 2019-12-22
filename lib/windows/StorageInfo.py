from lib.windows.common.CommandHandler import CommandHandler
import math
from lib.windows.common import Utility as utl
import wmi

class StorageInfo:
    '''
    className:StorageInfo
    Description:this will return the Disk Total Size and partitions details and Ram Details

    call this method:
        objectName.getStorageinfo()
    '''
    def __init__(self):
        self.cmd=CommandHandler()
        
    def convert_size(self,size_bytes):
       '''
       Accept the integer bytes size and convert into KB,MB,GB sizes 
       '''
       if size_bytes == 0:
           return "0B"
       size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
       i = int(math.floor(math.log(size_bytes, 1024)))
       p = math.pow(1024, i)
       s = round(size_bytes / p, 2)
       return "%s %s" % (s, size_name[i])
    
    def getDiskSize(self):
        '''
        Return the Total Disk Size 
        '''
        cmd='wmic diskdrive GET caption,size'
        result=self.cmd.getCmdOutput(cmd)
        list_disk=[]
        for i in result.splitlines():
            splited_text=i.split()
            disk={}
            if len(splited_text)>2:
                name=" ".join(splited_text[:-1])
                size=splited_text[-1]
                try:
                   size=self.convert_size(int(size))
                except ValueError:
                   size=None
                   pass
                disk['Name']=name
                disk['TotalSize']=size
                list_disk.append(disk)
        return list_disk
                
            
    def getRamSize(self):
        '''
        Return Total Usable Ram Size
        '''
        comp = wmi.WMI()
        ram=[]
        for i in comp.Win32_ComputerSystem():
            ram_sizes={}
            ram_sizes['PhysicalMemory']=self.convert_size(int(i.TotalPhysicalMemory))
            ram.append(ram_sizes)
        return ram
    
    def Preprocess(self,text):
        cmd=f'wmic {text} list /format:csv'
        Command_res=self.cmd.getCmdOutput(cmd)
        result=utl.CsvTextToDict(Command_res)
        return result
    
    def getLogicalDisk(self):
        '''
        Returns the Disk partitions details
        '''
        cmd='wmic logicaldisk get size,freespace,caption'
        result=self.cmd.getCmdOutput(cmd)
        drives=[]
        for i in result.splitlines():
            splited_text=i.split()
            if ':' in i and len(splited_text)>2:
                drive={}
                drive['Name']=splited_text[0].split(":")[0]
                drive['FreeSpace']=self.convert_size(int(splited_text[1]))
                drive['TotalSize']=self.convert_size(int(splited_text[2]))
                drives.append(drive)
                
        return drives
                
    def getStorageinfo(self):
        '''
        Return:Logical disks,Ram,Total Disk Size
        '''
        sinfo={}
        sinfo['Partions']=self.getLogicalDisk()
        sinfo['Ram']=self.getRamSize()
        sinfo['DiskSize']=self.getDiskSize()
        
        storage_catgories=['memoryphiscial','logicaldisk','CDROM','DEVICEMEMORYADDRESS','DISKDRIVE','DISKQUOTA','DMACHANNEL','LOGICALDISK','MEMCACHE','MEMORYCHIP','MEMPHYSICAL','PAGEFILE','PARTITION','VOLUME']
        for part in storage_catgories:
            sinfo[part]=self.Preprocess(part)
        return sinfo
        
