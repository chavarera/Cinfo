# CInfo 1.0
![CInfo](https://raw.githubusercontent.com/chavarera/Cinfo/master/img/logo.png)

CInfo is a python based utility tool to gather system,network, 
software,hardware,file related information and export to text file.


## CInfo Gathers Following Information
```
System Information
Network Information
Software Information
Storage Information
Hardware Information
File Information
```


### Prerequisites

What things you need to install the software and how to install them

```
Python ver: 3.x
Operating: Windows
```

### Used Modules
System Information
```
_winreg
datetime
platform
os
```

Network Information
```
socket
uuid
subprocess
re
```
Storage Information
```
subprocess
math
wmi
```

Software Information
```
winreg
```

Hardware Information
```
subprocess
```
File Information
```
os
string 
ctypes
```



### Installing

Download or clone this repository and extract in your Local Machine go to the extracted folder.
use Windows console and run 

```
python Cinfo.py
```

![run](https://github.com/chavarera/Cinfo/blob/master/img/run.PNG)

OutPut
```
Getting System Information
Getting Network Information
Getting Software Information
Getting Storage Information
Getting Hardware Information
Getting File Information
Successfully written Result into output/20190817-155638.txt
```

Now check output which is stored in the output folder in the form of text File

![output](https://github.com/chavarera/Cinfo/blob/master/img/output.PNG)



## Versioning

Cinfo 1.0
1.0 - Initial Release


## Authors

* **Ravishankar Chavare** - [chavarera](https://github.com/chavarera)




**Note:** If You Looking For Similar Version of Software for Unix distribution check out work submitted by 
**Deepak Chauhan**

[Cinfo-for-Linux](https://github.com/RoyalEagle73/Cinfo/tree/Cinfo-for-Linux)

## License
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
