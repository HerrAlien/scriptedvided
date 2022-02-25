import subprocess
import os
import shutil
import math

def ffmpegParams():
    return ["ffmpeg", "-y", "-hide_banner", "-loglevel", "error"]
    
def ffmpegSafeString (someText):
    return someText.replace(":", "\:").replace("%", "\\\%")

def filePathSafeString(someText):
    return someText.replace(":", " ")

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
        
        start = dictValue(inputStream,"start", 0)
        if (start >= 0):
            params.append("-ss")
            params.append(str(start))
        else:
            params.append("-sseof")
            params.append(str(start - length))
        
        params.append("-i")
        file = dictValue(inputStream,"file")
        params.append(file)
    else:
        params.append("-i")
        file = inputStream
        params.append(file)

    return params

    
def getDrawTextCommandFromArray (text, opts):
    textSize = float(dictValue(opts,"fontsize", 48))
    paramText = ""
    borderWidth = 0.5 * textSize
    boxcolor=dictValue(opts,"boxcolor", "#80000080")
    fontcolor=dictValue(opts,"fontcolor", "White")

    transition=":x=if(gt(t\,4)\, "+ str(borderWidth) + "\,\(t-4\)*\(tw + " + str(borderWidth) + "\)/2)"
    
    if (type(text) is type("")):
        paramText = "drawtext=y=H:box=1:boxborderw=" + str(borderWidth) +":boxcolor="+boxcolor+":font=Arial:fontsize=" + str (textSize) + ":fontcolor=" + fontcolor + ":text="+text
        paramText = paramText + transition
    else:
        lineSpacing = 0.5 * textSize
        stepSize = (textSize + 2 * borderWidth + lineSpacing)
        offsetFromBottom = len(text) * stepSize
        step = 0
        initialOffset = offsetFromBottom
        for line in text:
            iterationStartNode = ";[intermediate"+ str(step) +"]"
            iterationEndNode = "[intermediate"+ str(step + 1) +"]"
            
            if step == 0:
                iterationStartNode = ""
            
            if (step == (len(text) - 1)):
                iterationEndNode = ""

            paramText = paramText  + iterationStartNode + "drawtext=y=(H+"+str(initialOffset)+")/2-"+ str(offsetFromBottom) +":box=1:boxborderw="+ str(borderWidth) + ":boxcolor="+boxcolor+":font=Arial:fontsize="+ str (textSize) +":fontcolor=" + fontcolor + ":text="+line 
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
    
    return (["'" + ffmpegSafeString(episodeName + " (" + settings) + ")'", fpsAsText ])
        
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

def substituteAudio (inputVid, inputAudio, output=None, recompress=False):
    return overlayAudio(inputVid, inputAudio, output, 0.01, recompress)
    
def appendMultiple (streams, output=None, recompressVideo=True, video=True, audio=True):

    params = ffmpegParams();
    for stream in streams:
        sar = getSar(stream)
        if sar != (1,1) and sar != (0,0):
            stream = setSarToOne(stream)
        params = params + toInputParams(stream)    

    params.append("-filter_complex")
    
    streamsIds = ""
    for i in range (0, len(streams)):
        iStr = str(i)
        if video:
            streamsIds = streamsIds + "["+iStr+":v]"
        if audio:
            streamsIds = streamsIds + "["+iStr+":a]"
    
    filter = streamsIds + "concat=n=" + str(len(streams)) 
    if video:
        filter = filter + ":v=1"
    else:
        filter = filter + ":v=0"
    if audio:
        filter = filter + ":a=1"
    else:
        filter = filter + ":a=0"
    
    params.append(filter)
    
    if (not recompressVideo):
        params.append ("-c:v")
        params.append ("copy")
    
    if (output == None):
        secondRoot,ext = os.path.splitext (getFileFromInput(streams[0]))
        output = secondRoot + "_append_" + ext

    params.append(output)
    subprocess.run(params)
    
    return output

def xfadedMultiple (streams, output=None, fadeDuration=1, recompressVideo=True):

    durations = []
    params = ffmpegParams();
    for stream in streams:
        if getSar(stream) != (1,1):
            stream = setSarToOne(stream)
        params = params + toInputParams(stream)
        durations.append(getLengthOfStream(stream))

    params.append("-filter_complex")
    
    currentOffset = 0;
    videograph = ""
    audiograph = ""
    fadeDurationStr = str(fadeDuration)
    for i in range (0, len(streams) - 1):
        currentOffset = durations[i] + currentOffset - fadeDuration
        iStr = str(i)
        nextIStr = str(i+1)
        if i == 0:
            nextIStr = str(i+1)
            videograph = "["+iStr+":v]" + "["+nextIStr+":v]xfade=duration="+ fadeDurationStr +":offset="+ str(currentOffset) +"[intermediateV" + iStr + "];"
            audiograph = "["+iStr+":a]" + "["+nextIStr+":a]acrossfade=d="+ fadeDurationStr +"[intermediateA" + iStr + "];"
        else:
            prevIStr = str(i-1)
            videograph = videograph + "[intermediateV" + prevIStr + "]" + "["+nextIStr+":v]xfade=duration="+ fadeDurationStr +":offset="+ str(currentOffset) +"[intermediateV" + iStr + "];"
            audiograph = audiograph + "[intermediateA" + prevIStr + "]" + "["+nextIStr+":a]acrossfade=d="+ fadeDurationStr +"[intermediateA" + iStr + "];"
            
    filtergraph = videograph + audiograph
    filtergraph = filtergraph[:-1]
    
    params.append(filtergraph)
    params.append("-map")
    params.append("[intermediateV"+ str(len(streams) - 2)+"]")

    params.append("-map")
    params.append("[intermediateA"+ str(len(streams) - 2)+"]")
    
    if (not recompressVideo):
        params.append ("-c:v")
        params.append ("copy")
    
    if (output == None):
        secondRoot,ext = os.path.splitext (getFileFromInput(streams[0]))
        output = "_append_.mp4"

    params.append(output)
    subprocess.run(params)
    
    return output
    
    
def append (firstStream, secondStream, output=None, recompressVideo=True):
    return appendMultiple([firstStream, secondStream], output, recompressVideo)

    
def padAudioStream (stream, output=None, ammountBegin = 0, amountEnd = 0):
    params = ffmpegParams();

    params = params + toInputParams(stream)    
    params.append ("-map")
    params.append ("0:a")

    params.append("-filter_complex")
    params.append("[0:a]adelay=" + str(ammountBegin * 1000) + ":all=1[intermediate];[intermediate]apad=pad_dur=" + str(amountEnd))
    
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
    
def drawText (stream, text, output=None, opts={"fontcolor" : "White", "boxcolor" : "#80000080", "fontsize" : 48}):
    if (text is None):
        print ("WARNING: no text provided, returning the unmodified input " + "'" + getFileFromInput(stream) + "'")
        return getFileFromInput(stream)
        
    params = ffmpegParams();

    params = params + toInputParams(stream)    
    params.append("-filter_complex")

    params.append(getDrawTextCommandFromArray(text, opts))
    
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
        output = defaultOutput (getFileFromInput(video), "_scaled_" + str(resolutionPair[0]) + "x" + str(resolutionPair[1])  + ext)

    params.append(output)   
    subprocess.run(params)
    
    return output

def setSarToOne(video, output=None):
    params = ffmpegParams();
    params = params + toInputParams(video)    
    params.append("-filter_complex")

    params.append("setsar=1")
    
    if (output == None):
        root,ext = os.path.splitext (getFileFromInput(video))
        output = defaultOutput (root, "_setSar1_" + ext)
    
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
    
    if dictValue(configs, "TOC", None) is None:
        configs["TOC"] = []

    opts = {"padAudio": 1, "videoSoundVolume" : 0.1, "targetRes": targetRes }
    
    audioVolume = dictValue(audioDict, "volume", None)
    if audioVolume is not None:
        opts["videoSoundVolume"] = 1 - float(audioVolume)
    
    builtVideo = makeEpisodeWithAllInputs (videoDict, audioDict, textArray, opts)
    # get extension and dir
    dir = dictValue(configs, "outputFolder", ".")
    ext = os.path.splitext(builtVideo)[1]
    episodeVideo = os.path.join(dir, filePathSafeString(episode["title"]) + ext)
    configs["TOC"].append({"title" : episode["title"], "length" : getLengthOfStream(builtVideo)})
    shutil.move (builtVideo, episodeVideo)
    return episodeVideo

def buildBackgroundTrack (configs):
    backgroundTrack = dictValue(configs, "backgroundTrack", None)
    if backgroundTrack is None:
        return None
    #build the background track
    segmentNamePrefix = "backgroundSegment"
    segmentExt = ".ogg"
    segmentIndex = 0
    audioToConcat = []
    previousTrackEndedAt = 0
    for track in backgroundTrack["audioTracks"]:
        segmentName = segmentNamePrefix + str(segmentIndex) + segmentExt

        # handle padding at the begining.        
        trackIsInsertedAt = dictValue(track, "destinationTimestamp", None)
        if trackIsInsertedAt is None:
            trackIsInsertedAt = 0
        elif type (trackIsInsertedAt) is type(""):
            trackIsInsertedAt = getSeconds (trackIsInsertedAt)
        else:            
            insertedAt = 0
            for episodeTocDict in configs["TOC"]:
                if episodeTocDict["title"] == trackIsInsertedAt["title"]:
                    break
                insertedAt = insertedAt + float(episodeTocDict["length"])
            trackIsInsertedAt = insertedAt
            
        trackLength = 0
        trackStartsAt = 0
        timestamps = dictValue (track, "timestamps", None)
        if timestamps is not None:
            trackStartsAt = getSeconds(timestamps[0])
            endSecond = getSeconds(timestamps[1])
            trackLength = endSecond - trackStartsAt
        else:
            trackLength = getLengthOfStream(track["file"])
            
        padAtBeginning = trackIsInsertedAtAt - previousTrackEndedAt
        if padAtBeginning > 0:
            padAudioStream( {"file" : dictValue(track,"file") , "start" : trackStartsAt, "length" :trackLength }, segmentName, padAtBeginning, 0.1 )
            audioToConcat.append(segmentName)
        else:
            audioToConcat.append({"file" : dictValue(track,"file") , "start" : trackStartsAt, "length" :trackLength })
                
        previousTrackEndedAt = trackIsInsertedAtAt + trackLength
        
        segmentIndex = segmentIndex + 1
    
    backgroundAufioFile = appendMultiple (audioToConcat, "background_track.ogg" , video=False)
    for audioToDelete in audioToConcat:
        if type(audioToDelete) is type(""):
            os.remove(audioToDelete)
    
    return backgroundAufioFile
    
def makeVideo (configs):
    episodeVideos = []
    for episode in configs["episodes"]:
        try:
            episodeVideo = makeVideoForEpisode(episode, configs)
            episodeVideos.append(episodeVideo)
        except:
            print ("ERR: " + episode["title"])

    videoPath = os.path.join(configs["outputFolder"], configs["outputFile"])
    appendMultiple(episodeVideos, videoPath)
    backgroundTrack = dictValue(configs, "backgroundTrack", None)
    if backgroundTrack is None:
        return videoPath
    
    noBackgroundVideo = os.path.join(configs["outputFolder"], "_nobackground.mp4")
    shutil.move(videoPath, noBackgroundVideo)
    
    backgroundAudioFile = buildBackgroundTrack (configs)
    
    videoAudioWeight = 1 - dictValue(backgroundTrack, "volume", 0.1)
    
    return overlayAudio (noBackgroundVideo, backgroundAudioFile, videoPath, firstStreamAudioWeight=videoAudioWeight)
    

# needs an audio - see makeAudioForEposiode
def makeEpisodeWithAllInputs (video, audio, textLinesArray, options):
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
            nextIterationVideo = append(fixedVideo, video, "___appended___.mp4")
            #cleanup fixedVideo?
            fixedVideo = nextIterationVideo
    
    videoLen = getLengthOfStream(fixedVideo)
    videoStart = dictValue (video, "start", None)
    if videoStart is None:
        videoStart = (videoLen - (audioLen + padding + padding)) * 0.5    
    
    trimmedVideo = truncate (fixedVideo, videoStart, audioLen + padding + padding)
    
    scaledVideo = trimmedVideo
    targetRes = dictValue(options, "targetRes", (1920,1080))
    resolution = getResolution(trimmedVideo)
    if (resolution[1] != targetRes[1]):
        scaledVideo = scaleVideo(trimmedVideo, targetRes)
        os.remove(trimmedVideo)
    
    paddedAudio = padAudioStream (audio, "padded.ogg", padding, padding)
    
    videoAudioWeight = dictValue (options, "videoSoundVolume", 0.1)
    
# then  overlay the audio

    videoWithOverlayedAudio = overlayAudio (scaledVideo, paddedAudio, firstStreamAudioWeight=videoAudioWeight)
    returnedVideo = videoWithOverlayedAudio
    os.remove(scaledVideo)
    os.remove(paddedAudio)
    
# then print the text
    if type(textLinesArray) is type ([]) and len(textLinesArray) > 0:
        returnedVideo = drawText (videoWithOverlayedAudio, textLinesArray, opts={"boxcolor" : "#80000080"})
        os.remove(videoWithOverlayedAudio)
    
    return returnedVideo


def aliases(inputName):
    gameAliases = [\
        ["Apex", "Apex Legends", "ApexLegends", "Apex_Legends"],\
        ["Alien Isolation", "Alien: Isolation", "Alien:Isolation", "AlienIsolation", "Alien_Isolation"],\
        ["Call of Duty: Warzone","Call_of_Duty_Warzone", "CallOfDutyWarzone", "COD Warzone", "COD_Warzone", "Warzone"],\
        ["Battlefield V","Battlefield 5", "Battlefield_V", "Battlefield_5", "bfv", "bf5"],\
        ["Rainbow Six Siege","Rainbow 6 Siege", "Rainbow Six: Siege","Rainbow 6: Siege", "Rainbow_Six_Siege","Rainbow_6_Siege", \
        "r6s", "RainbowSixSiege","Rainbow6Siege"],\
        ["Counter-Strike: Global Offensive","Counter Strike: Global Offensive", "ConunterStrike: Global Offensive",\
        "ConunterStrike", "cs:go","csgo", "cs-go"],\
        ["Rocket League","Rocket_League", "RocketLeague"],\
        ["Genshin Impact", "GenshinImpact", "Genshin_Impact"], \
        ["Realm Royale", "Realm_Royale", "RealmRoyale"], \
        ["Rogue Company", "Rogue_Company", "RogueCompany"], \
        ["World of Tanks Blitz", "World_of_Tanks_Blitz", "World of Tanks: Blitz", "WorldOfTanksBlitz", "WoT Blitz", "WoT: Blitz",\
        "WoT_Blitz", "wotblitz"], \
    ]

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
    drawText ("merged_audio.mp4", ["'Rainbow 6 Siege (720p, low settings, render scale 100\\\%)'", getFpsStatsText(73, 32, 27)])
#     print(getResolution ("audio.ogg"))
#    print(getSuitableVideos ("C:\\Users\\Admin\\Videos\\hd7770", ["fortnite"]))
#    episode = { "title": "Apex Legends",\
#"audio" : {"timestamps" : ("02:02", "02:14" ) },\
#"video" : "stock_ApexLegends_1080p.mp4", \
#"overlay" : { \
#    "benchmark" : { \
#        "FPS values" : [0, 0, 0], \
#        "settings" : "1080p, low settings", \
#    }\
#} }
#    print (getDrawTextCommandFromArray(getTextArrayForEpisode(episode) , {}) )
#    scaleVideo ("C:\\Users\\Admin\\Videos\\hd5770\\hd5770_AlienIsolation_1200pUltra.mp4", (1920, 1080), "C:\\Users\\Admin\\Videos\\hd5770\\output\\Alien - Isolation.mp4")    
    vids = []
#    vids.append("C:\\Users\\Admin\\Videos\\hd5770\\output\\Alien - Isolation.mp4")
#    vids.append("C:\\Users\\Admin\\Videos\\hd5770\\output\\Apex Legends.mp4")
#    vids.append("C:\\Users\\Admin\\Videos\\hd5770\\output\\Battlefield V.mp4")
#    vids.append("C:\\Users\\Admin\\Videos\\hd5770\\output\\Control.mp4")
#    vids.append("C:\\Users\\Admin\\Videos\\hd5770\\output\\Counter Strike - Global Offensive.mp4")
#    vids.append("C:\\Users\\Admin\\Videos\\hd5770\\output\\DOTA2.mp4")
#    vids.append("C:\\Users\\Admin\\Videos\\hd5770\\output\\Fortnite.mp4")
#    vids.append("C:\\Users\\Admin\\Videos\\hd5770\\output\\Genshin Impact.mp4")
#    vids.append("C:\\Users\\Admin\\Videos\\hd5770\\output\\Paladins.mp4")
#    vids.append("C:\\Users\\Admin\\Videos\\hd5770\\output\\Rainbow Six - Siege.mp4")
#    vids.append("C:\\Users\\Admin\\Videos\\hd5770\\output\\Realm Royale.mp4")
#    vids.append("C:\\Users\\Admin\\Videos\\hd5770\\output\\Rocket League.mp4")
#    vids.append("C:\\Users\\Admin\\Videos\\hd5770\\output\\Rogue Company.mp4")
#    vids.append("C:\\Users\\Admin\\Videos\\hd5770\\output\\Splitgate.mp4")
#    vids.append("C:\\Users\\Admin\\Videos\\hd5770\\output\\Valorant.mp4")
#    vids.append("C:\\Users\\Admin\\Videos\\hd5770\\output\\Warframe.mp4")
#    vids.append("C:\\Users\\Admin\\Videos\\hd5770\\output\\World of Tanks Blitz.mp4")
#    print(recursivelyXfadeToOne(vids))
    #overlayAudio ({"file":"C:\\Users\\Admin\\Videos\\hd7770\\hd7770_RainbowSix_720p_100renderScale.mp4", "start" : -10, "length" : 30}, \
#{"file":"C:\\Users\\Admin\\Videos\\Generic old GPU advice.ogg"} , "merged_audio.mp4", 0.15)
