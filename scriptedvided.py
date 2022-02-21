import subprocess
import os
import shutil

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

def getSeconds (timeAsString):
    times = timeAsString.split(":")
    factor = 1.0
    value = 0.0
    arrayLen = len(times)
    
    for index in range(0, arrayLen):
        value = value + float(times[arrayLen - 1 - index]) * factor
        factor = factor * 60
    return value
        
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
    textSize = 36
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
    
    return (["'" + episodeName + " (" + settings + ")'", fpsAsText ])
        
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

def getLengthOfStream (stream):
    if type(stream) is type ({}):
        length = dictValue(stream, "length", None)
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

    timeInSec = getSeconds(out)
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
    
def getMediaArrayFromFoldersAndNames (folders, names, extensions):
    paths = []
    for folder in folders:
        if (folder is not None):
            for file in os.listdir(folder):
                ext = os.path.splitext(file)[1].upper()
                hasExtension = False
                for arrExt in extensions:
                    if arrExt.upper() == ext:
                        hasExtension = True
                        break
                
                if hasExtension:
                    for name in names:
                        fullPath = os.path.join(folder, file)
                        nameUpper = name.upper()
                        if file.upper().find(nameUpper) >= 0:
                            paths.append(fullPath)
                        elif fullPath.upper() == nameUpper:
                            paths.append(fullPath)
    return paths

def getSuitableVideoFromFolders (folders, names, extensions=[".mp4", ".mov", ".avi"]):
    media = getMediaArrayFromFoldersAndNames (folders, names, extensions)
    return selectSuitableVideo(media)


    
    
def getSuitableMediaStream (episode, configs, keyInEpisode, defaultMediaKey, extensions):
    names = []

    mediaDict =  dictValue (episode, keyInEpisode, None)
    # see if we can simply return it as is
    if type(mediaDict) is type({}):
        # check that we have a full path for "file"
        dictFile = dictValue (mediaDict, "file", None)
        if dictFile is not None:
            if os.path.exists(dictFile):
                return mediaDict # path exists, so just use that
            else:
                names.append(dictFile) # not a full path, we'll search for it.
    elif type (mediaDict) is type (""): # we passed a string
        names.append(mediaDict) # so add it to the search names
        mediaDict = {}
    else: # we passed nothing
        mediaDict = {}
            
    episodeTitle = dictValue (episode, "title", None)
    if episodeTitle is not None:
        names.append(episodeTitle)
        # TODO: append the aliases as well
        names = names + aliases (episodeTitle)
        
    mediaFolder = dictValue(configs, "mediaFolder", None)
    stockFolder = dictValue(configs, "stockFolder", None)
     
    mediaDict["file"] = getSuitableVideoFromFolders ([mediaFolder, stockFolder], names, extensions)
    if mediaDict["file"] is None:
        defaultMedia = dictValue (configs, defaultMediaKey, None)
        if defaultMedia is None:
            return {}
            
        mediaDict["file"] = getSuitableVideoFromFolders ([mediaFolder, stockFolder], [defaultMedia], extensions)
        
        
    # check if we have a timestamps entry; convert that to start and length.
    timestamps = dictValue (mediaDict, "timestamps", None)
    if timestamps is not None:
        startSecond = getSeconds(timestamps[0])
        endSecond = getSeconds(timestamps[1])
        mediaDict["start"] = startSecond
        mediaDict["length"] = endSecond - startSecond
    else:
        altVal = dictValue (mediaDict, "start", None)
        if altVal is not None:
            mediaDict["start"] = getSeconds(altVal)

        altVal = dictValue (mediaDict, "length", None)
        if altVal is not None:
            mediaDict["length"] = getSeconds(altVal)
        
    return mediaDict
    
    
    
def getSuitableVideoStream (episode, configs):
    return getSuitableMediaStream (episode, configs, "video", "defaultVideoFile", [".mp4", ".mov", ".avi"])

def getSuitableAudioStream (episode, configs):
    return getSuitableMediaStream (episode, configs, "audio", "defaultAudioFile", [".mp3", ".ogg", ".flac"])

    
def getSuitableVideo (folder, names):
    return getSuitableVideoFromFolders([folder], names)


def makeVideoForEpisode (episode, configs, targetRes=(1920,1080) ):
    videoDict = getSuitableVideoStream(episode, configs)
    audioDict = getSuitableAudioStream(episode, configs)
    textArray = getTextArrayForEpisode(episode)

    # TODO pass all options. Do a resize
    builtVideo = makeEpisodeWithAllInputs (videoDict, audioDict, textArray)
    # get extension and dir
    dir = dictValue(configs, "outputFolder", ".")
    ext = os.path.splitext(builtVideo)[1]
    episodeVideo = os.path.join(dir, episode["title"].replace(":", " -") + ext)
    shutil.move (builtVideo, episodeVideo)
    return episodeVideo
    

# needs an audio - see makeAudioForEposiode
def makeEpisodeWithAllInputs (video, audio, textLinesArray, \
options={"padAudio": 1, "videoSoundVolume" : 0.15}):
# pad the audio with 1 second of silence

# video length must be larger than the audio. Loop it if needed.

#truncate them ....

    videoLen = getLengthOfStream(video)
    audioLen = getLengthOfStream(audio)
    padding = dictValue (options, "padAudio", 1)
    
    audioToVideoLengthRatio = int((audioLen + padding + padding) / videoLen)
    fixedVideo = getFileFromInput (video)
    nextIterationVideo = fixedVideo
    if (audioToVideoLengthRatio > 1):
        for i in range(0, audioToVideoLengthRatio):
            nextIterationVideo = append(fixedVideo, video)
            #cleanup fixedVideo?
            fixedVideo = nextIterationVideo
    
    videoLen = getLengthOfStream(fixedVideo)
    videoStart = dictValue (video, "start", None)
    print (str(videoStart) + " of type " + str(type(videoStart)))
    if videoStart is None:
        videoStart = (videoLen - (audioLen + padding + padding)) * 0.5    
    
    trimmedVideo = truncate (fixedVideo, videoStart, audioLen + padding + padding)
    
    paddedAudio = padAudioStream (audio, "padded.ogg", padding, padding)
    
    videoAudioWeight = dictValue (options, "videoSoundVolume", 0.1)
    
# then  overlay the audio

    videoWithOverlayedAudio = overlayAudio (trimmedVideo, paddedAudio, firstStreamAudioWeight=videoAudioWeight)
    returnedVideo = videoWithOverlayedAudio
    
# then print the text
    if len(textLinesArray) > 0:
        returnedVideo = drawText (videoWithOverlayedAudio, textLinesArray)
        os.remove(videoWithOverlayedAudio)
    
    # cleanup paddedAudio?
    # cleanup fixedVideo, if audioToVideoLengthRatio > 1 ?
    os.remove(trimmedVideo)
    return returnedVideo


def aliases(inputName):
    gameAliases = [\
        ["Apex", "Apex Legends", "ApexLegends", "Apex_Legends"],\
        ["Alien Isolation", "Alien: Isolation", "Alien:Isolation", "AlienIsolation", "Alien_Isolation"],\
        ["Call of Duty: Warzone","Call_of_Duty_Warzone", "CallOfDutyWarzone", "COD Warzone", "COD_Warzone", "Warzone"],\
        ["Battlefield V","Battlefield 5", "Battlefield_V", "Battlefield_5", "bfv", "bf5"],\
        ["Rainbow Six Siege","Rainbow 6 Siege", "Rainbow Six: Siege","Rainbow 6: Siege", "Rainbow_Six_Siege","Rainbow_6_Siege", \
        "r6s", "RainbowSixSiege","Rainbow6Siege"],\
        ["Conunter-Strike: Global Offensive","Conunter Strike: Global Offensive", "ConunterStrike: Global Offensive",\
        "ConunterStrike", "cs:go","csgo", "cs-go"],\
        ["Rocket League","Rocket_League", "RocketLeague"],\
        ["Genshin Impact", "GenshinImpact", "Genshin_Impact"], \
        ["Realm Royale", "Realm_Royale", "RealmRoyale"], \
        ["Rogue Company", "Rogue_Company", "RogueCompany"], \
        ["World of Tanks Blitz", "World_of_Tanks_Blitz", "World of Tanks: Blitz", "WorldOfTanksBlitz", "WoT Blitz", "WoT: Blitz",\
        "WoT_Blitz", "wotblitz"], \
    ]
    '''
    TODO:
    Hyperscape
    Control
    DOTA2
    Fortnite
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
