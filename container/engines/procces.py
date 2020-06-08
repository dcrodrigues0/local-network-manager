import os
import time
import dpkt

from container.engines import parsePcap as parser

fileSrc = os.getenv("FILE_PATH")
backup = os.getenv("FILE_FOLDER_BACKUP")
queue = []
queueFile = os.getenv("QUEUE_FILE")

def proccess():
    if len(queue) > 0:
            files = queueFile.split(";")
            for f in files:
                addQueue(f)

    while True:
        if len(queue) == 0:
            continue

        #print("queue size " + str(len(queue)))
        try:
            filepath = queue.pop()
            filecap, file = read(filepath)
            parser.parse(filecap)
            file.close()
            os.remove(filepath)
        except Exception as e:
            print(e)

        time.sleep(30)

def read(filepath):
    f = open(filepath, 'rb')
    pcap = dpkt.pcap.Reader(f)
    return pcap, f

def addQueue(filepath):
    queue.append(filepath)

def addEnvOnQueue():
    addQueue(fileSrc)
