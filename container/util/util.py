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
    return [year, month, day, h, minutes, seconds]


def toJson(value):
    return dumps(value)


def formatFloat(value):
    return "{:.2f}".format(round(value, 2))


def replace_ip_string(str1, replace_dots=True):
    if replace_dots is False:
        return str1.replace('/', '.')
    else:
        return str1.replace('.', '/')
