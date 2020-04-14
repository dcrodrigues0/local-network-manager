import threading

from container.engines import procces

def run():
    th = threading.Thread(target=procces.proccess,args=())
    th.start()



