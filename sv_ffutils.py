import subprocess
import os
import sv_utils

def defaultOutput (input, suffix):
    root, ext = os.path.splitext (input)
    return root + suffix + ext
    
def ffmpegParams():
    return ["ffmpeg", "-y", "-hide_banner", "-loglevel", "error"]
#    return ["ffmpeg", "-y"]
    
def ffmpegSafeString (someText):
    return someText.replace(":", "\:").replace("%", "\\\%")

def getLengthOfStream (stream):
    if type(stream) is type ({}):
        length = sv_utils.dictValue(stream, "length", None)
        if length is not None:
            return length
    
    filepath = getFileFromInput (stream)
    finishedProc = subprocess.run (["ffprobe", filepath], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out = str(finishedProc.stderr) + str(finishedProc.stdout)
    durationIndex = out.index("Duration")
    out = out[durationIndex:];
    commaIndex = out.index(",")
    out = out[0:commaIndex]
    spaceIndex  = out.index(" ")
    out = out[spaceIndex+1:]

    timeInSec = sv_utils.getSeconds(out)
    return timeInSec

def hasAudio(stream):
    filepath = getFileFromInput (stream)
    
    finishedProc = subprocess.run (["ffprobe", filepath], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out = str(finishedProc.stderr) + str(finishedProc.stdout)
    return out.find(": Audio:") > 0

    
def getResolution (filepath):
    finishedProc = subprocess.run (["ffprobe", filepath], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out = str(finishedProc.stderr) + str(finishedProc.stdout)
    durationIndex = out.find(": Video:")
    if durationIndex < 0:
        return (0, 0)

    out = out[durationIndex:];
    endIndex = out.index("fps")
    out = out[0:endIndex]

    outArr = out.split(",")
    for entry in outArr:
        resolutionAttemptArr = entry.split("x")
        try:
            if (len (resolutionAttemptArr) > 1):
                pieceW = resolutionAttemptArr[0].replace(" ","")
                pieceH = resolutionAttemptArr[1].split(" ")[0].replace(" ","")
                return (int(pieceW), int(pieceH))
        except:
            continue
            
    return (0, 0)

def getSar(filepath):
    finishedProc = subprocess.run (["ffprobe", filepath], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out = str(finishedProc.stderr) + str(finishedProc.stdout)
    sarIndex = out.find("[SAR ")
    if sarIndex < 0:
        return (0, 0)

    out = out[sarIndex + 5:];
    darIndex = out.index(" DAR ")
    out = out[0:darIndex]

    outArr = out.split(":")
    return (int(outArr[0]), int(outArr[1]))
