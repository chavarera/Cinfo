import time

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
   with open(filename,'wt') as file:
      file.write(data)
   print(f"Successfully Exported Result in to {filename} file")

##     key,value = [line.split(',') for line in lines if len(line)>0]
##     final_dict = dict(zip(key,value))
##     clean_dict = {key:value for key,value in final_dict.items() if value!=""}
     
