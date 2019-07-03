
#Get System Realted Information
import SystemInfo
s1=SystemInfo.SystemInfo()
result=s1.GetSystemInfo()
print('\n{0:*^80s}\n'.format('Operating System Information'))
for key,value in result.items():
    print('{}\t:\t{}'.format(key,value))


#

