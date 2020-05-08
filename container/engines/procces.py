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

    try:
        os.path.exists(fileSrc)
        filecap, file = read()
        parser.parse(filecap)
        file.close()
    except  Exception as e:
        print(e)
        return e

def read():
    f = open(fileSrc, 'rb')
    pcap = dpkt.pcap.Reader(f)
    return pcap, f

