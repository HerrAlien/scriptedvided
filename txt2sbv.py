import sys
import sv_utils

def twoDigitString(number):
    return sv_utils.twoDigitString(number)

def secondsToTime(seconds):
    return sv_utils.secondsToTime(seconds)

def getSeconds (timeAsString):
    return sv_utils.getSeconds (timeAsString)


def parseTime (inputText, i):
    j = i
    currentChar = inputText[j]
    chunk = ""
    while currentChar != ']':
        currentChar = inputText[j]
        if currentChar != ']':
            chunk = chunk + currentChar
        j = j + 1
    
    return (getSeconds(chunk), j + 1)
    
def refineTimeData (timeDataDict):
    text = timeDataDict['text']
    startT = timeDataDict["timestamps"][0]
    endT = timeDataDict["timestamps"][1]
    textLen = len(text)
    velocity = (endT - startT) / float (textLen)
    
    currentT = startT
    currentStartT = startT
    i = 0
    chunk = ""
    
    refinedData = []
    allTextCovered = True
    while i < textLen:

        currentChar = text[i]
        chunk = chunk + currentChar
        
        if (((currentT - currentStartT) > 7) and (currentChar == '.' or currentChar == ',' or currentChar == ';' or currentChar == ' ' or currentChar == '\n')):
            chunk = chunk.replace("\n\n", "\n")
            refinedData.append({"timestamps" : [currentStartT, currentT] , "text" : chunk })
            currentStartT = currentT
            chunk = ""
            allTextCovered = True
        else:
            allTextCovered = False
            
        currentT = currentT + velocity
        i = i + 1
    
    if not allTextCovered:
        refinedData.append({"timestamps" : [currentStartT, currentT] , "text" : chunk })
    
    
    return refinedData

if __name__ == "__main__":
    inputfilename = sys.argv[1]
    outputfilename = sys.argv[2]
    timelength = float(sys.argv[3])

    inputfile = open(inputfilename, mode="r", encoding="utf-8")
    inputText = inputfile.read()

    inputTextLength = len(inputText)
    
#  [ {"timestamps" : [0, 23.5] , "text" : "bla ....."},  ]
#
    rawTimeData = []
    time = 0
    oldTime = 0
    chunk = ""
    i = 0
    while i < inputTextLength:
        currentChar = inputText[i]
        
        if currentChar == '[':
            i = i + 1
            (time , i) = parseTime (inputText, i)
            
            rawTimeData.append ({ "timestamps" : [oldTime, time], "text" : chunk });
            
            oldTime = time
            chunk = ""
    
        currentChar = inputText[i]
        chunk = chunk + currentChar
        i = i + 1

    rawTimeData.append ({ "timestamps" : [oldTime, timelength], "text" : chunk });
    
    timeData = []
    for rawData in rawTimeData:
        timeData = timeData +  refineTimeData(rawData)
        
    outputfile = open(outputfilename, mode="w", encoding="utf-8")
    for fineData in timeData:
        if fineData["timestamps"][1] - fineData["timestamps"][0] > 1:
            outputfile.write ("\n" + secondsToTime(fineData["timestamps"][0]) + "," + secondsToTime(fineData["timestamps"][1]) + "\n" + fineData["text"]+"\n")
