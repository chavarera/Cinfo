import os 


if __name__=="__main__":
    #check platform type and Run File(if Windows It will Import from WindowsInfo)
    if os.name=='nt':
        import WindowsInfo
    else:
        import LinuxInfo
