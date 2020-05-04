import os
import shutil
import dpkt
import time
from container.engines import parsePcap as parser

fileSrc = "/home/leonardo/Estudo/Faculdade/projetoPI/local-network-manager/files/packests.pcap"
def proccess():
    print("Start process job")

    if os.path.exists(fileSrc):
        filecap, file = read()
        parser.parse(filecap)
        file.close()

        mili_seconds = lambda: int(round(time.time() * 1000))
        #shutil.move(fileSrc, "/home/leonardo/Estudo/Faculdade/projetoPI/local-network-manager/files/backup/packests.pcap-"+ str(mili_seconds()))
    else:
        print("File not exist!!")

def read():
    f = open(fileSrc, 'rb')
    pcap = dpkt.pcap.Reader(f)
    return pcap, f

