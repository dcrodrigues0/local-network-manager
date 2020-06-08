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


current_milli_time = lambda: int(round(time.time() * 1000))


def realtime():
    while True:

        file = export+str(current_milli_time())
        process = subprocess.Popen(('sudo', 'tcpdump', '-i', interface, '-w', file), stdout=subprocess.PIPE)
        time.sleep(int(processTime,base=8))
        process.terminate()
        pro.addQueue(file)
        print("Arquivo gerado:" + file)
        time.sleep(int(timeWait,base=8))




