''' 
Scripted Video Editor - a bunch of python script to allow rendering of videos 
using FFMPEG.

SV_UTILS contains various utilities (converting string timestaps to numbers etc.)

Copyright 2022 Herr_Alien <alexandru.garofide@gmail.com>

This program is free software: you can redistribute it and/or modify it under 
the terms of the GNU General Public License as published by the 
Free Software Foundation, either version 3 of the License, or (at your option)
any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY 
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE. See the GNU Affero General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

def filePathSafeString(someText):
    return someText.replace(":", " ").replace("?", " ")

def dictValue(dict, key, default=None):
    try:
        return dict[key]
    except:
        return default

def getSeconds (timeAsString):
    if timeAsString is None:
        return None
        
    if type(timeAsString) is not type (""):
        return float(timeAsString)

    times = timeAsString.split(":")
    arrayLen = len(times)
    
    if arrayLen == 2 and times[1] is None:
        return float(timeAsString)
    
    factor = 1.0
    value = 0.0
    
    try:
        for index in range(0, arrayLen):
            value = value + float(times[arrayLen - 1 - index]) * factor
            factor = factor * 60
    except:
        print("ERR: Could not convert input string to seconds: " + timeAsString)
        
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

# move to UTILS
def getFpsValueFromLine(line):
    valueOfInterest = line.split(":")[1]
    valueOfInterest = valueOfInterest.replace(" ", "")
    valueOfInterest = valueOfInterest.replace("FPS\n", "")
    return int(float(valueOfInterest) + 0.5)
    
# move to UTILS
def parseBenchmarkFile (benchmarkFile):
    returnedDict = {}
    currentKey = ""
    currentValue = [0,0,0]
    benchmarkCompletedMark = " benchmark completed,"
    
    fileHandler = open(benchmarkFile, "r")
    fileLines = fileHandler.readlines()
    lineIndexFollowingKey = -1
    for line in fileLines:
        if benchmarkCompletedMark in line:
            currentKey = line[21:]
            posOfEnd = currentKey.index(benchmarkCompletedMark)
            currentKey = currentKey[0:posOfEnd]
            currentKey = currentKey.upper()
            lineIndexFollowingKey = 0
            currentValue = [0,0,0]
        else:
            if lineIndexFollowingKey == 0: # average
                currentValue[0] = getFpsValueFromLine(line)
            elif lineIndexFollowingKey == 3: # 1%
                currentValue[1] = getFpsValueFromLine(line)
            elif lineIndexFollowingKey == 4: # 0.1%
                currentValue[2] = getFpsValueFromLine(line)
                returnedDict[currentKey] = currentValue
                lineIndexFollowingKey = -1
            
            if lineIndexFollowingKey >= 0:
                lineIndexFollowingKey = lineIndexFollowingKey + 1

    return returnedDict
