from subprocess import getoutput

class CommandHandler:
    def __init__(self,command_text=""):
        self.command_text=command_text
        
    def getCmdOutput(self,cmdtext):
        try:
            return getoutput(cmdtext)
        except Exception as ex:
            return ex
