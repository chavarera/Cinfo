import time
import json

def CsvTextToDict(text):
     lines = text.strip().splitlines()
     keys=lines[0].split(",")
     items=[]
     for line in lines[1:]:
          if len(line)>0:
               items.append(dict(zip(keys,line.split(","))))
     return items

def ExportTOJson(data):
   timestr = time.strftime("%Y%m%d-%H%M%S")
   filename=f'output/{timestr}.json'
   try:
        with open(filename, 'w') as fp:
             json.dump(data,fp)
        return True,f"successfully saved fille in {filename}"
   except Exception as ex:
        return False,ex
   
   
   
