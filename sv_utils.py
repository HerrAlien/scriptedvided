def filePathSafeString(someText):
    return someText.replace(":", " ")

def dictValue(dict, key, default=None):
    try:
        return dict[key]
    except:
        return default

def getSeconds (timeAsString):
    if type(timeAsString) is not type (""):
        return float(timeAsString)

    times = timeAsString.split(":")
    arrayLen = len(times)
    
    if arrayLen == 2 and times[1] is None:
        return float(timeAsString)
    
    factor = 1.0
    value = 0.0
    for index in range(0, arrayLen):
        value = value + float(times[arrayLen - 1 - index]) * factor
        factor = factor * 60
    return value

def twoDigitString(number):
    if (number < 10):
        return "0" + str(number)
    return str(number)
    
def secondsToTime(seconds):
    hours = int(seconds/3600)
    minutes = int((seconds - 3600 * hours) / 60)
    seconds = int((seconds - 3600 * hours - 60 * minutes) + 0.5)

    if seconds == 60:
        seconds = 0
        minutes = minutes + 1
    
    hoursStr = twoDigitString(hours)
    minutesStr = twoDigitString(minutes)
    secondsStr = twoDigitString(seconds)

    return hoursStr + ":" + minutesStr + ":" + secondsStr

def getFileFromInput (inputStream):
    if (type(inputStream) is type({})):        
        return dictValue(inputStream,"file")
    else:
        return inputStream

