from container.engines import procces

#Inicia o procesos de read and parse do arquivo
def startProcess():
    procces.addEnvOnQueue()
    procces.proccess()
