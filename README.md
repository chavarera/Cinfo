# CInfo 1.0
CInfo is an utility tool to gaining system,network,file,hardware Information.Cinfo is a python based tool to gather system related information.

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
Python ver : 3.x
Operating  : Windows
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

Download or clone this repository and extract in your Local Machine go to extracted folder.
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
Successfully written Result in to output/20190817-155638.txt
```

Now check output which is stored in output folder in the form of text File

![output](https://github.com/chavarera/Cinfo/blob/master/img/output.PNG)



## Versioning

Cinfo 1.0

## Authors

* **Ravishankar Chavare** - *Initial work* - [chavarera](https://github.com/chavarera)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
