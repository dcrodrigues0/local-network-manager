import os
import shutil
import stat

import dpkt
import time
from container.engines import parsePcap as parser

fileSrc = os.getenv("FILE_PATH")
backup = os.getenv("FILE_FOLDER_BACKUP")
def proccess():
    print("Start process job")

    if os.path.exists(fileSrc):
        filecap, file = read()
        parser.parse(filecap)
        file.close()
    else:
        print("File not exist!!")

def read():
    f = open(fileSrc, 'rb')
    pcap = dpkt.pcap.Reader(f)
    return pcap, f

