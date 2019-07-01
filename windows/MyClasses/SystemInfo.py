#import Required module
import platform


class SystemInfo:
    '''This Class help use to gather System Information'''
    def getPlatform(self):
        '''Return machine platform windows or ubuntu '''
        
        #simple dictionary to save required data
        systemdata={}
        systemdata['machineName']=platform.system()
        systemdata['processor']=platform.processor()
        
        #Return data to calling function
        return systemdata

#Create an Object of SystemInfo
s1=SystemInfo()

#call The getPlatform method from class

result=s1.getPlatform()

#getPlatform return dictionary object now show the Output
for key,value in result.items():
    print('{}\t:{}'.format(key,value))
