#For gettting time and date
import time
timestr = time.strftime("%Y%m%d-%H%M%S")

#Append all result to alls
alls=[]
def Display(data):
    alls.append(data)


#Get System Realted Information
import SystemInfo
s1=SystemInfo.SystemInfo()
result=s1.GetSystemInfo()
print('Getting System Information')
Display('\n{0:-^80s}\n'.format('Operating System Information'))

for key,value in result.items():
    Display('{}\t: {}'.format(key,value))



#Network Information
print('Getting Network Information')
import NetworkInfo
Display('\n\n{0:-^80s}'.format('Network Related Information'))
n1=NetworkInfo.NetworkInfo()
for i in n1.networkinfo():
    name="\n\n{0:_^80s}".format(i['name'])
    Display(name)
    for values in i['details']:
        val=list(values.items())[0]
        Display('{}\t: {}'.format(val[0],val[1]))



#Get Installed Software Information
print('Getting Software Information')
        
import SoftwareInfo
Display('\n\n{0:-^80s}'.format('User Installed Software'))
soft=SoftwareInfo.SoftwareInfo()
softwares=soft.getSoftwareList()
no=0
for r in softwares:
    no+=1
    Display('\nSerial No.\t: {}\nSoftware Name\t: {}\nVersion No\t: {}\nPublisher Name\t: {}'.format(no,r['name'],r['version'],r['publisher']))


#Get Storage Information
print('Getting Software Information')

import StorageInfo
Display('\n\n{0:-^80s}'.format('Storation Information'))
storage1=StorageInfo.StorageInfo()
storage=storage1.getStorageinfo()
Partions=storage['Partions']
Display('\n{0:_^50s}\n'.format('Disk partitions Information'))
Display("Name\tFreeSpace\tTotalSize")
for p in Partions:
    Display('{}    	{}    	{}'.format(p['Name'],p['FreeSpace'],p['TotalSize']))

ram=storage['Ram']
disk=storage['DiskSize']
Display('\n{0:_^50s}'.format('Disk Size and RAM Information'))

Display("\n1.Disk Size")
for r in disk:
    Display('\nName\t: {}\nSize\t: {}'.format(r['Name'],r['TotalSize']))
Display("\n2. RAM")
for r in ram:
    Display('Usable RAM Size : {}'.format(r['PhysicalMemory']))


#Get System Hardware Information
print('Getting Hardware Information')

import HardwareInfo
hi=HardwareInfo.HardwareInfo()
Display('\n\n{0:-^80s}'.format('Hardware Information '))
res=hi.getHardwareinfo()
for k,v in res.items():
    Display("\n_________{} Information_________".format(k))
    for data in v:
        for kn,kv in data.items():
            Display("{} : {}".format(kn,kv))


#Get Total File Information
print('Getting File Information')
            
import FileInfo
finfo=FileInfo.FileInfo()

Display('\n\n{0:-^80s}'.format('Total File Count '))

cnt=finfo.GetCount()
no=0
for r in cnt:
    Display('\nSerial No.\t: {}\nDrive Name\t: {}\nFile Count\t: {} Files'.format(no,r['drive'][:-2],r['count']))
    no=no+1

#Write All Data To text file inside output folder    
file='output/'+timestr+'.txt'
with open(file, mode='wt', encoding='utf-8') as myfile:
    myfile.write('\n'.join(alls))
print("Successfully written Result in to {}".format(file))
