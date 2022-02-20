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

def getFpsStatsText(average, onePercent=None, pointOnePercent=None, max=None, min=None):
    text = "'"
    text = text + "Average\: "+ str(average) +"fps"

    if max is not None:
        text = text + ", Max\: "+ str(max) +"fps"
    if min is not None:
        text = text + ", Min\: "+ str(min) +"fps"
    if onePercent is not None:
        text = text + ", 1\\\% lows\: "+ str(onePercent) +"fps"
    if pointOnePercent is not None:
        text = text + ", 0.1\\\% lows\: "+ str(pointOnePercent) +"fps"
        
    text = text + "'"
    return text

def getFileFromInput (inputStream):
    if (type(inputStream) is type({})):        
        return dictValue(inputStream,"file")
    else:
        return inputStream

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

    
def getDrawTextCommandFromArray (text):
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

    
def getTextArrayForEpisode (episode):
    overlay = dictValue (episode, "overlay", None)
    if (overlay is None):
        return None
    
    textArray = dictValue (overlay, "text", None)
    if (textArray is not None):
        return (textArray)

    benchmark = dictValue (overlay, "benchmark", None)
    if (benchmark is None):
        return None
    
    fpsArr = dictValue (benchmark, "FPS values", None)
    if (fpsArr is None):
        return None
    
    episodeName = dictValue (episode, "title", None)
    settings = dictValue (benchmark, "settings", None)
    if (settings is None):
        return None

    fpsAsText = getFpsStatsText (fpsArr[0], fpsArr[1], fpsArr[2])
    
    return ([episodeName + " (" + settings + ")", fpsAsText])
        
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
    
def substituteAudio (inputVid, inputAudio, output=None, recompress=False):
    params = ffmpegParams();

    params.append ("-vn")
    params = params + toInputParams (inputAudio)
    
    params.append("-an")
    params = params + toInputParams (inputVid)
    
    if (output == None):
        audioRoot,ext = os.path.splitext (getFileFromInput(inputAudio))
        output = defaultOutput (getFileFromInput(inputVid), "_substituteAudio_"  + os.path.basename(audioRoot) )

    if (not recompress):
        params.append("-c")
        params.append("copy")

    params.append(output)
    subprocess.run(params)
    
    return output
    
def overlayAudio (inputVid, inputAudio, output=None, firstStreamAudioWeight=0.1, recompressVideo=True):
    params = ffmpegParams();

    params = params + toInputParams(inputVid)    
    params = params + toInputParams(inputAudio)

    params.append ("-map")
    params.append ("0:a")
    
    params.append ("-map")
    params.append ("1:a")
    
    if (output == None):
        audioRoot,ext = os.path.splitext (getFileFromInput(inputAudio))
        output = defaultOutput (getFileFromInput(inputVid), "_overlay_"  + os.path.basename(audioRoot) )

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
        secondRoot,ext = os.path.splitext (getFileFromInput(secondStream))
        output = defaultOutput (getFileFromInput(firstStream), "_append_"  + os.path.basename(secondRoot))

    params.append(output)
    subprocess.run(params)
    
    return output
    
def padAudioStream (stream, output=None, ammountBegin = 0, amountEnd = 0):
    params = ffmpegParams();

    params = params + toInputParams(stream)    
    params.append ("-map")
    params.append ("0:a")

    params.append("-filter_complex")
    params.append("[0:a]adelay=" + str(ammountBegin * 1000) + "[intermediate];[intermediate]apad=pad_dur=" + str(amountEnd))
    
    if (output == None):
        secondRoot,ext = os.path.splitext (getFileFromInput(stream))
        output = defaultOutput (getFileFromInput(stream), "_padded_"  + str(ammountBegin) + "_" + str(amountEnd))

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
    if (text is None):
        print ("WARNING: no text provided, returning the unmodified input " + "'" + getFileFromInput(stream) + "'")
        return getFileFromInput(stream)
        
    params = ffmpegParams();

    params = params + toInputParams(stream)    
    params.append("-filter_complex")

    params.append(getDrawTextCommandFromArray(text))
    
    if (output == None):
        secondRoot,ext = os.path.splitext (getFileFromInput(stream))
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
        root,ext = os.path.splitext (getFileFromInput(video))
        output = defaultOutput (getFileFromInput(video), "_scaled_" + str(resolutionPair[0]) + "x" + + str(resolutionPair[1])  + ext)

    params.append(output)
    subprocess.run(params)
    
    return output
    
def selectSuitableVideo (paths, desiredLength=30, desiredYRes=1080):
    potentialVideos = []
    for fullVideoPath in paths:
        if (getLengthOfStream(fullVideoPath) > desiredLength):
            resolution = getResolution (fullVideoPath)
# we favor 1080p videos - they will not require any scaling.
            if (resolution[1] == desiredYRes):
                return fullVideoPath
            else:
                potentialVideos.append(fullVideoPath)
        else:
            potentialVideos.append(fullVideoPath)
    if len (potentialVideos) > 0:
        return potentialVideos[0]
    return None
    
def getMediaArrayFromFoldersAndNames (folders, names):
    paths = []
    for folder in folders:
        if (folder is not None):
            for file in os.listdir(folder):
                for name in names:
                    fullPath = os.path.join(folder, file)
                    nameUpper = name.upper()
                    if file.upper().find(nameUpper) >= 0:
                        paths.append(fullPath)
                    elif fullPath.upper() == nameUpper:
                        paths.append(fullPath)
    return paths

def getSuitableVideoFromFolders (folders, names):
    media = getMediaArrayFromFoldersAndNames (folders, names)
    return selectSuitableVideo(media)

def getSuitableVideoStream (episode, configs):
    names = []

    videoDict =  dictValue (episode, "video", None)
    # see if we can simply return it as is
    if type(videoDict) is type({}):
        print ("is dictionary")
        # check that we have a full path for "file"
        dictFile = dictValue (videoDict, "file", None)
        if dictFile is not None:
            if os.path.exists(dictFile):
                return videoDict # path exists, so just use that
            else:
                names.append(dictFile) # not a full path, we'll search for it.
    elif type (videoDict) is type (""): # we passed a string
        print ("is string")
        names.append(videoDict) # so add it to the search names
        videoDict = {}
    else: # we passed nothing
        print ("is none")
        videoDict = {}
            
    episodeTitle = dictValue (episode, "title", None)
    if episodeTitle is not None:
        names.append(episodeTitle)
        # TODO: append the aliases as well
        names = names + aliases (episodeTitle)

    mediaFolder = dictValue(configs, "mediaFolder", None)
    stockFolder = dictValue(configs, "stockFolder", None)
     
    videoDict["file"] = getSuitableVideoFromFolders ([mediaFolder, stockFolder], names)
    return videoDict
    
    
def getSuitableVideo (folder, names):
    return getSuitableVideoFromFolders([folder], names)
    
def makeVideoForEpisode (mediaFolders, episodeName, minLength=30, targetRes=(1920,1080) ):
# search a video for that name, and ideally for the 1080p resolution
    names = getNamesFromEpisodeName (episodeName)
    nonScaledVideo = getSuitableVideoFromFolders(mediaFolders, names)    
# should have a pretty good length
    if (getLengthOfStream(nonScaledVideo) < minLength):
        videoToCleanup = nonScaledVideo
        nonScaledVideo = append (nonScaledVideo, nonScaledVideo)
        # cleanup videoToCleanup?
# scale it to 1080p if needed
    scaledVideo = nonScaledVideo
    if not (getResolution (nonScaledVideo)[1] == targetRes[1]):
        scaledVideo = scaleVideo(nonScaledVideo, targetRes)
        #cleanup nonScaledVideo?
        
    return scaledVideo

def makeAudioForEposiode (audioFile, episodeName, config):
# from the config, get the start and end in the audio
# build the output file name from the episode
# then just return a trim.
    return 0

# needs a video - see makeVideoForEpisode
# needs an audio - see makeAudioForEposiode
def makeEpisodeWithAllInputs (video, audio, \
textLinesArray=[], \
options={"padAudio": 1, "videoSoundVolume" : 0.1}):
# pad the audio with 1 second of silence

# video length must be larger than the audio. Loop it if needed.

# then  overlay the audio

# then print the text
    videoLen = getLengthOfStream(video)
    audioLen = getLengthOfStream(audio)
    padding = dictValue (options, "padAudio", 1)
    
    audioToVideoLengthRatio = (audioLen + padding + padding) / videoLen
    fixedVideo = getFileFromInput (video)
    nextIterationVideo = fixedVideo
    for i in range(0, audioToVideoLengthRatio):
        nextIterationVideo = append(fixedVideo, video)
        #cleanup fixedVideo?
        fixedVideo = nextIterationVideo
    
    videoLen = getLengthOfStream(fixedVideo)
    videoStart = (videoLen - (audioLen + padding + padding)) * 0.5
    
    videoInput = { "file" : fixedVideo, "start" : videoStart, "length" : videoLen}
    paddedAudio = padAudioStream (audio, "padded.ogg", padding, padding)
    
    videoAudioWeight = dictValue (options, "videoSoundVolume", 0.1)
    
    videoWithOverlayedAudio = overlayAudio (videoInput, paddedAudio, firstStreamAudioWeight=videoAudioWeight)
    
    returnedVideo = videoWithOverlayedAudio
    
    if len(textLinesArray) > 0:
        returnedVideo = drawText (videoWithOverlayedAudio, textLinesArray)
        # cleanup videoWithOverlayedAudio?
    
    # cleanup paddedAudio?
    # cleanup fixedVideo, if audioToVideoLengthRatio > 1 ?
    return returnedVideo


def aliases(inputName):
    gameAliases = [\
        ["Apex", "Apex Legends", "ApexLegends", "Apex_Legends"],\
        ["Alien Isolation", "Alien: Isolation", "Alien:Isolation", "AlienIsolation", "Alien_Isolation"],\
        ["Call of Duty: Warzone","Call_of_Duty_Warzone", "CallOfDutyWarzone", "COD Warzone", "COD_Warzone", "Warzone"],\
    ]
    '''
    TODO:
    Hyperscape
    Battlefield V
    Control
    Rainbow Six Siege
    Conunter-Strike: Global Offensive
    DOTA2
    Fortnite
    Rocket League
    Splitgate
    Valorant
    Genshin Impact, Paladins, Realm Royale, Rogue Company, World of Tanks Blitz, Warframe'''  
  
    for namesArr in gameAliases:
        for potentialName in namesArr:
            if potentialName.upper() == inputName.upper():
                return namesArr

    for namesArr in gameAliases:
        for potentialName in namesArr:
            potentialNameUpper = potentialName.upper()
            inputNameUpper = inputName.upper()
            if potentialNameUpper.find(inputNameUpper) >= 0 or inputNameUpper.find(potentialNameUpper) >= 0:
                return namesArr
                
    print ("WARNING: '" + inputName + "' has no known aliases.")
    return [] # no lnown
    
if __name__ == "__main__":
#   truncatedvid = truncate ( "C:\\Users\\Admin\\Videos\\hd7770\\hd7770_RainbowSix_720p_100renderScale.mp4", -10, 30, "vid.mp4" )
#   truncatedvid = scaleVideo ( "C:\\Users\\Admin\\Videos\\hd7770\\hd7770_RainbowSix_720p_100renderScale.mp4", (1920,1080), "zz.mp4" )
#   truncatedaudio = truncate ( "C:\\Users\\Admin\\Videos\\Generic old GPU advice.ogg", -10, 30, "audio.ogg" )
#   truncatedaudio2 = truncate ("C:\\Users\\Admin\\Videos\\Generic old GPU advice.ogg", None, -2, 30)
#   overlayAudio ({"file":"C:\\Users\\Admin\\Videos\\hd7770\\hd7770_RainbowSix_720p_100renderScale.mp4", "start" : -10, "length" : 30}, \
#   {"file":"C:\\Users\\Admin\\Videos\\Generic old GPU advice.ogg", "start":-10, "length" : 30} , "merged_audio.mp4", 0.15)
#   truncatedvid1 = truncate ("C:\\Users\\Admin\\Videos\\hd7770\\hd7770_RainbowSix_720p_100renderScale.mp4", "t1.mp4", -40, 10)
#   truncatedvid2 = truncate ("C:\\Users\\Admin\\Videos\\hd7770\\hd7770_RainbowSix_720p_100renderScale.mp4", "t2.mp4", -10, 10)
#   append({"file":"C:\\Users\\Admin\\Videos\\hd7770\\hd7770_RainbowSix_720p_100renderScale.mp4", "start" : -10, "length" : 10}, \
#   {"file":"C:\\Users\\Admin\\Videos\\hd7770\\hd7770_RainbowSix_720p_100renderScale.mp4", "start" : -40, "length" : 10}, "appended.mp4")
#    print(getLengthOfStream ("C:\\Users\\Admin\\Videos\\hd7770\\hd7770_RainbowSix_720p_100renderScale.mp4"))
#    print(getFpsStatsText(73, 32, 27, 80, 27))
#    drawText ("merged_audio.mp4", ["'Rainbow 6 Siege (720p, low settings, render scale 100\\\%)'", getFpsStatsText(73, 32, 27)])
#     print(getResolution ("audio.ogg"))
#    print(getSuitableVideos ("C:\\Users\\Admin\\Videos\\hd7770", ["fortnite"]))
    episode = { "title": "Apex Legends",\
"audio" : {"timestamps" : ("02:02", "02:14" ) },\
"video" : "stock_ApexLegends_1080p.mp4", \
"overlay" : { \
    "benchmark" : { \
        "FPS values" : [0, 0, 0], \
        "settings" : "1080p, low settings", \
    }\
} }
    print (getTextArrayForEpisode(episode))
