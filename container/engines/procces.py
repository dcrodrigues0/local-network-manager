import dpkt
import os
import shutil
import time
from container.engines import parsePcap as parser


fileSrc = ""
def read():
    f = open(fileSrc, 'rb')
    pcap = dpkt.pcap.Reader(f)
    return pcap

def start():
    print("Thread iniciou")
    #while True:
     #   if os.path.exists(fileSrc) and os.stat(fileSrc).st_size > 24:
      #      filecap = read()
       #     parser.parse(filecap)
        #    mili_seconds = lambda: int(round(time.time() * 1000))
         #   shutil.move(fileSrc, "/packets.pcap-"+ str(mili_seconds()))
        #else:
         #   print("File not exist!!")
        #time.sleep(5)

start()
