try:
    import _winreg as reg
except:
    import winreg as reg

class RegistryHandler:
    def __init__(self,key,path):        
        self.Hkey=self.getRootKey(key)
        self.path=path
        self.key = reg.OpenKey(self.Hkey, self.path)
       
        
    def getRootKey(self,key):
        ROOTS={'HCR':reg.HKEY_CLASSES_ROOT,
               'HCU':reg.HKEY_CURRENT_USER,
               'HLM':reg.HKEY_LOCAL_MACHINE,
               'HU':reg.HKEY_USERS,
               'HCC':reg.HKEY_CURRENT_CONFIG
               }
        try:
            return ROOTS[key]
        except Exception as ex:
            return ex
    
    def getKeys(self):
        key_count = reg.QueryInfoKey(self.key)[0]
        self.key.Close()
        return key_count
    
    def getValues(self,name):
        '''Return string value of given key name inside windows registery
        '''
        return reg.QueryValueEx(self.key, name)[0]
