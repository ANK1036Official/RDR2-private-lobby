import os
import signal
import time
import psutil

process_name = 'RDR2.exe'  

def get_pid(name):
    return [p.info['pid'] for p in psutil.process_iter(['pid', 'name']) if name == p.info['name']]

pids = get_pid(process_name)

if not pids:
    print(f"No running process found with name: {process_name}")
else:
    for pid in pids:
        os.kill(pid, signal.SIGSTOP)

    time.sleep(10)

    for pid in pids:
        os.kill(pid, signal.SIGCONT)
