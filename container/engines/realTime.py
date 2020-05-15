import os
import random
import subprocess as subprocess
import threading
import time
import container.engines.procces as pro

timeWait = os.getenv("TIME_LOOP_REALTIME")
export = os.getenv("EXPORT_REAL_TIME")
interface = os.getenv("INTERFACE")
processTime = os.getenv("TIME_PROCESS_REALTIME")

def init():
    t = threading.Thread(target=pro.proccess,args=())
    t.start()

    t2 = threading.Thread(target=realtime,args=())
    t2.start()




def realtime():
    print("start")
    while True:

        file = export+str(random.randint(1,101))
        process = subprocess.Popen(('sudo', 'tcpdump', '-i', interface, '-w', file), stdout=subprocess.PIPE)
        time.sleep(int(processTime,base=8))
        process.terminate()
        pro.addQueue(file)
        print("Arquivo gerado:" + file)
        time.sleep(int(timeWait,base=8))




