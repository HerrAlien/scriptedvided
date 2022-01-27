import subprocess
import os

def ffmpegParams():
    return ["ffmpeg", "-y"]

def defaultOutput (input, suffix):
    root, ext = os.path.splitext (input)
    return root + suffix + ext
    
def dictValue(dict, key, default=-1):
    try:
        return dict[key]
    except:
        return default
    
def toInputParams (inputStream):
    params = [];

    if (type(inputStream) is type({})):        
        length = dictValue(inputStream,"length")
        if (length > 0):
            params.append("-t")
            params.append(str(length))
        
        start = dictValue(inputStream,"start")
        if (start >= 0):
            params.append("-ss")
            params.append(str(start))
        else:
            params.append("-sseof")
            params.append(str(start - length))
        
        params.append("-i")
        params.append(dictValue(inputStream,"file"))
    else:
        params.append("-i")
        params.append(inputStream)

    return params

    
def getDrawTextCommand (text):
    textSize = 24
    paramText = ""
    borderWidth = 0.5 * textSize
    boxcolor="#00800080"
#    transition=":enable=gt(t\,2)"
#    transition=":x=if(gt(t\,3)\,0\,\(t-3\)*tw/3)"
    transition=":x=if(gt(t\,4)\, "+ str(borderWidth) + "\,\(t-4\)*\(tw + " + str(borderWidth) + "\)/2)"
    
    if (type(text) is type("")):
        paramText = "drawtext=y=H:box=1:boxborderw=" + str(borderWidth) +":boxcolor="+boxcolor+":font=Arial:fontsize=" + str (textSize) + ":fontcolor=White" + ":text="+text
        paramText = paramText + transition
    else:
        lineSpacing = 0.5 * textSize
        stepSize = (textSize + 2 * borderWidth + lineSpacing)
        offsetFromBottom = len(text) * stepSize
        step = 0
        for line in text:
            iterationStartNode = ";[intermediate"+ str(step) +"]"
            iterationEndNode = "[intermediate"+ str(step + 1) +"]"
            
            if step == 0:
                iterationStartNode = ""
            
            if (step == (len(text) - 1)):
                iterationEndNode = ""

            paramText = paramText  + iterationStartNode + "drawtext=y=H-"+ str(offsetFromBottom) +":box=1:boxborderw="+ str(borderWidth) + ":boxcolor="+boxcolor+":font=Arial:fontsize="+ str (textSize) +":fontcolor=White" + ":text="+line 
            paramText = paramText + transition
            paramText = paramText + iterationEndNode

            offsetFromBottom = offsetFromBottom - stepSize
            step=step+1

    return paramText

def getScaleCommand(resolutionPair):
    return "scale="+str(resolutionPair[0])+ "x" +str(resolutionPair[1]) + ":flags=lanczos"
    
# input - the input media to be truncated
# start - the input media to be truncated
def truncate(input, start=-1, length=-1, output=None, recompress=False):
    params = ffmpegParams() + toInputParams( {"file" : input, "start" : start, "length" : length} );

    if (output == None):
        output = defaultOutput (input, "_truncate_" )

    if (not recompress):
        params.append("-c")
        params.append("copy")

    params.append(output)
    
    subprocess.run(params)
    
    return output
    
def substituteAudio (inputVid, inputAudio, output, recompress=False):
    params = ffmpegParams();

    params.append ("-vn")
    params = params + toInputParams (inputAudio)
    
    params.append("-an")
    params = params + toInputParams (inputVid)
    
    if (output == None):
        audioRoot,ext = os.path.splitext (inputAudio)
        output = defaultOutput (inputVid, "_substituteAudio_"  + os.path.basename(audioRoot) )

    if (not recompress):
        params.append("-c")
        params.append("copy")

    params.append(output)
    subprocess.run(params)
    
    return output
    
def overlayAudio (inputVid, inputAudio, output, firstStreamAudioWeight=0.1, recompressVideo=True):
    params = ffmpegParams();

    params = params + toInputParams(inputVid)    
    params = params + toInputParams(inputAudio)

    params.append ("-map")
    params.append ("0:a")
    
    params.append ("-map")
    params.append ("1:a")
    
    if (output == None):
        audioRoot,ext = os.path.splitext (inputAudio)
        output = defaultOutput (inputVid, "_overlay_"  + os.path.basename(audioRoot) )

    weightsStr = str(firstStreamAudioWeight) + " " + str(1 - firstStreamAudioWeight)
        
    params.append ("-filter_complex")
    params.append ("[0:a][1:a] amix=weights='" + weightsStr + "'")

    params.append ("-map")
    params.append ("0:v?")

    params.append ("-map")
    params.append ("1:v?")
    
    if (not recompressVideo):
        params.append ("-c:v")
        params.append ("copy")
    
    params.append(output)
    subprocess.run(params)
    
    return output

def append (firstStream, secondStream, output=None, recompressVideo=True):
    params = ffmpegParams();

    params = params + toInputParams(firstStream)    

    params = params + toInputParams(secondStream)    

        
    params.append("-filter_complex")
    params.append("concat")
    
    if (not recompressVideo):
        params.append ("-c:v")
        params.append ("copy")
    
    if (output == None):
        secondRoot,ext = os.path.splitext (secondStream)
        output = defaultOutput ("", "_append_"  + os.path.basename(secondRoot))

    params.append(output)
    subprocess.run(params)
    
    return output
    
def padStream (stream, output, ammountBegin = 0, amountEnd = 0):
    params = ffmpegParams();

    params = params + toInputParams(stream)    
    params.append ("-map")
    params.append ("0:a")

    params.append("-filter_complex")
    params.append("[0:a]adelay=" + str(ammountBegin * 1000) + "[intermediate];[intermediate]apad=pad_dur=" + str(amountEnd))
    
    if (output == None):
        secondRoot,ext = os.path.splitext (stream)
        output = defaultOutput ("", "_append_"  + os.path.basename(secondRoot))

    params.append(output)
    subprocess.run(params)
    
    return output

def getLengthOfStream (filepath):
    finishedProc = subprocess.run (["ffprobe", filepath], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out = str(finishedProc.stderr) + str(finishedProc.stdout)
    durationIndex = out.index("Duration")
    out = out[durationIndex:];
    commaIndex = out.index(",")
    out = out[0:commaIndex]
    spaceIndex  = out.index(" ")
    out = out[spaceIndex+1:]
    durations = out.split(":")
    timeInSec = float(durations[-1]) + int(durations[-2]) * 60 + int(durations[-3]) * 3600
    return timeInSec
    
def getResolution (filepath):
    finishedProc = subprocess.run (["ffprobe", filepath], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out = str(finishedProc.stderr) + str(finishedProc.stdout)
    durationIndex = out.find("Video:")
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

def drawText (stream, text, output=None):
    params = ffmpegParams();

    params = params + toInputParams(stream)    
    params.append("-filter_complex")

    params.append(getDrawTextCommand(text))
    
    if (output == None):
        secondRoot,ext = os.path.splitext (stream)
        output = defaultOutput ("", "_withText_"  + ext)

    params.append(output)
    subprocess.run(params)
    
    return output

def scaleVideo(video, resolutionPair, output=None):
    params = ffmpegParams();

    params = params + toInputParams(video)    
    params.append("-filter_complex")

    params.append(getScaleCommand(resolutionPair))
    
    if (output == None):
        root,ext = os.path.splitext (video)
        output = defaultOutput ("", "_scaled_" + str(resolutionPair[0]) + "x" + + str(resolutionPair[1])  + ext)

    params.append(output)
    subprocess.run(params)
    
    return output
    
def getSuitableVideos (folder, names):
    videos = []
    potentialVideos = []
    for file in os.listdir(folder):
        for name in names:
# the filename should contain one of the names
            if file.upper().find(name.upper()) >= 0:
                fullVideoPath = os.path.join(folder, file) 
# we want videos of more than 30 seconds length
                if (getLengthOfStream(fullVideoPath) > 30):
                    resolution = getResolution (fullVideoPath)
# we favor 1080p videos - they will not require any scaling.
                    if (resolution[1] == 1080):
                        videos.append (fullVideoPath)
                        return videos
                    else:
                        potentialVideos.append(fullVideoPath)
                else:
                    potentialVideos.append(fullVideoPath)
            if (len(potentialVideos) > 0):
                return potentialVideos
                    
    return potentialVideos

def makeEpisodeFromVideo (video, episodeName):
# then get the audio segment
#   - this means locating a file with how much each episode lasts
#   - search the episode in that file. Then do a trim of the audio
    return 0

def makeEpisodeFromDescriptionAndFolder (mediaFolder, episodeName):
# search a video for that name, and ideally for the 1080p resolution
    nonScaledVideo = getSuitableVideos(mediaFolder, episodeName)[0]    
# should have a pretty good length
    if (getLengthOfStream(nonScaledVideo) < 30):
        nonScaledVideo = append (nonScaledVideo, nonScaledVideo)
# scale it to 1080p if needed
    scaledVideo = nonScaledVideo
    if not (getResolution (nonScaledVideo)[1] == 1080):
        scaledVideo = scaleVideo(nonScaledVideo, (1920,1080))

    return makeEpisodeFromVideo (scaledVideo, episodeName)


def makeEpisodeFromFiles (video, audio, \
textLinesArray=[], \
options={"padAudio": 1, "padInsertText" : 2, "videoSoundVolume" : 0.1}):
# pad the audio with 1 second of silence

# video length must be larger than the audio. Loop it if needed.

# then  overlay the audio

# then print the text
    videoLen = getLengthOfStream(video)
    audioLen = getLengthOfStream(audio)
    padding = 1
    
    videoStart = (videoLen - (audioLen + padding + padding)) * 0.5
    
# if video length is not longer then audio, loop it,
# and make sure you start the video at the begining.
    if videoLen <= audioLen:
        videoStart = 0
        # now do the looping
        baseName,ext = os.path.splitext (video)
        video = append (video, video, baseName + "_doubled" + ext)    
    return 0

    
if __name__ == "__main__":
#   truncatedvid = truncate ( "C:\\Users\\Admin\\Videos\\hd7770\\hd7770_RainbowSix_720p_100renderScale.mp4", -10, 30, "vid.mp4" )
    truncatedvid = scaleVideo ( "C:\\Users\\Admin\\Videos\\hd7770\\hd7770_RainbowSix_720p_100renderScale.mp4", (1920,1080), "zz.mp4" )
#   truncatedaudio = truncate ( "C:\\Users\\Admin\\Videos\\Generic old GPU advice.ogg", -10, 30, "audio.ogg" )
#   truncatedaudio2 = truncate ("C:\\Users\\Admin\\Videos\\Generic old GPU advice.ogg", None, -2, 30)
#   overlayAudio ({"file":"C:\\Users\\Admin\\Videos\\hd7770\\hd7770_RainbowSix_720p_100renderScale.mp4", "start" : -10, "length" : 30}, \
#   {"file":"C:\\Users\\Admin\\Videos\\Generic old GPU advice.ogg", "start":-10, "length" : 30} , "merged_audio.mp4", 0.15)
#   truncatedvid1 = truncate ("C:\\Users\\Admin\\Videos\\hd7770\\hd7770_RainbowSix_720p_100renderScale.mp4", "t1.mp4", -40, 10)
#   truncatedvid2 = truncate ("C:\\Users\\Admin\\Videos\\hd7770\\hd7770_RainbowSix_720p_100renderScale.mp4", "t2.mp4", -10, 10)
#   append({"file":"C:\\Users\\Admin\\Videos\\hd7770\\hd7770_RainbowSix_720p_100renderScale.mp4", "start" : -10, "length" : 10}, \
#   {"file":"C:\\Users\\Admin\\Videos\\hd7770\\hd7770_RainbowSix_720p_100renderScale.mp4", "start" : -40, "length" : 10}, "appended.mp4")
#    print(getLengthOfStream ("C:\\Users\\Admin\\Videos\\hd7770\\hd7770_RainbowSix_720p_100renderScale.mp4"))
#    drawText ("merged_audio.mp4", ["'Rainbow 6 Siege (720p, low settings, render scale 100\\\%)'", "'Average\: 73fps, 1\\\% lows\: 32fps'"])
#     print(getResolution ("audio.ogg"))
#    print(getSuitableVideos ("C:\\Users\\Admin\\Videos\\hd7770", ["fortnite"]))
