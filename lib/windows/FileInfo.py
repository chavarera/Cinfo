import os
import win32api


class FileInfo:
    '''
    class Name:
    FileInfo

    Function Names:
    getDrives()
    getFileList(path)
    GetCount()
    '''
    def getDrives(self):
        '''
        getDrives()
        Function Return a object list containing all drives List

        Output:
        List-->All List of Avilable Drives
        '''
        drives = win32api.GetLogicalDriveStrings()
        drives = drives.split('\000')[:-1]
        return drives
    
    def getFileList(self,path):
        '''
       
        Get Total File list at given path 
        getFileList(path):
        Example :
            Object.getFileList(r"D:\Products\admin\images")
            
        Input :
        path-->a valid system path

        Output:
        False-->If path is not Exists
        List-->All Files List
 
        '''
        if os.path.exists(path):
            allfiledict=[]
            final=[]
            fil=[final.extend(['{},{}'.format(path,os.path.join(path, name),os.path.splitext(name)[1]) for name in files]) for path, subdirs, files in os.walk(path)]
            return final
        
        return False
    
    def GetCount(self):
        '''
        GetCount() Return all files Count in Your System

        Output:
        res-->is an dictionary containing all drives and files count
        '''
        drives=self.getDrives()
        filelist=[]
        res=[]
        for i in drives[1:]:
            result={}
            result['drive']=i
            flist=self.getFileList(i)
            filelist.append(flist)
            result['count']=len(flist)
            res.append(result)
        return res

