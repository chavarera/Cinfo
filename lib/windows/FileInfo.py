try:
    import os
    import string
    from ctypes import windll
except Exception as ex:
    print(ex)
import timeit
from datetime import datetime
startTime = datetime.now()


class FileInfo:
    def getDrives(self):
        drives = []
        bitmask = windll.kernel32.GetLogicalDrives()
        for letter in string.ascii_uppercase:
            if bitmask & 1 & os.path.exists('{}:'.format(letter)):
                drives.append(letter+":/")
            bitmask >>= 1
        return drives
    def getFileList(self,path):
        allfiledict=[]
        final=[]
        fil=[final.extend(['{},{}'.format(path,os.path.join(path, name),os.path.splitext(name)[1]) for name in files]) for path, subdirs, files in os.walk(path)]
        return final
    
    def GetCount(self):
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


