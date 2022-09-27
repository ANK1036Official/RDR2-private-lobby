import psutil
import time

def findProcessIdByName(processName):
    listOfProcessObjects = []
    for proc in psutil.process_iter():
       try:
           pinfo = proc.as_dict(attrs=['pid', 'name', 'create_time'])
           if processName.lower() in pinfo['name'].lower() :
               listOfProcessObjects.append(pinfo)
       except (psutil.NoSuchProcess, psutil.AccessDenied , psutil.ZombieProcess) :
           pass
    return listOfProcessObjects;

listOfProcessIds = findProcessIdByName('RDR2.exe')

if len(listOfProcessIds) > 0:
   for elem in listOfProcessIds:
       processID = elem['pid']
       print(f"Attempting to create private lobby... [{processID}]")
       try:
       	p = psutil.Process(processID)
       	p.suspend()
       	time.sleep(10)
       	p.resume()
       	print('Success!')
       except:
       	print('Failed!')
else :
   print('RDR2 not running...')