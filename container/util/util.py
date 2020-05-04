from bson.json_util import dumps

def timestampFormat(timestamp):
     date = timestamp.split(" ")[0]
     year = date.split("-")[0]
     month = date.split("-")[1]
     day = date.split("-")[2]
     hour = timestamp.split(" ")[1].split(":")
     h = hour[0]
     minutes = hour[1]
     seconds = hour[2]

     return [year,month,day,h,minutes,seconds]

def toJson(value):
     return dumps(value)
