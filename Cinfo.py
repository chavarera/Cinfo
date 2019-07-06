
#Get System Realted Information
import SystemInfo
s1=SystemInfo.SystemInfo()
result=s1.GetSystemInfo()
print('\n{0:-^80s}\n'.format('Operating System Information'))
for key,value in result.items():
    print('{}\t: {}'.format(key,value))



#Network Information
import NetworkInfo
print('\n\n{0:-^80s}'.format('Network Related Information'))
n1=NetworkInfo.NetworkInfo()
for i in n1.networkinfo():
    name="\n\n{0:*^80s}".format(i['name'])
    print(name)
    for values in i['details']:
        val=list(values.items())[0]
        print('{}\t: {}'.format(val[0],val[1]))



#Get Installed Software Information
import SoftwareInfo
print('\n\n{0:-^80s}'.format('User Installed Software'))
soft=SoftwareInfo.SoftwareInfo()
softwares=soft.getSoftwareList()
no=0
for r in softwares:
    no+=1
    print('\nSerial No.\t: {}\nSoftware Name\t: {}\nVersion No\t: {}\nPublisher Name\t: {}'.format(no,r['name'],r['version'],r['publisher']))


#Get Storage Information
import StorageInfo
print('\n\n{0:-^80s}'.format('Storation Information'))
storage1=StorageInfo.StorageInfo()
storage=storage1.getStorageinfo()
Partions=storage['Partions']
print('\n{0:*^50s}\n'.format('Disk partitions Information'))
print("Name\tFreeSpace\tTotalSize")
for p in Partions:
    print('{}    	{}    	{}'.format(p['Name'],p['FreeSpace'],p['TotalSize']))

ram=storage['Ram']
disk=storage['DiskSize']
print('\n{0:*^50s}'.format('Disk Size and RAM Information'))

print("\n1.Disk Size")
for r in disk:
    print('\nName\t: {}\nSize\t: {}'.format(r['Name'],r['TotalSize']))
print("\n2. RAM")
for r in ram:
    print('Usable RAM Size : {}'.format(r['PhysicalMemory']))

