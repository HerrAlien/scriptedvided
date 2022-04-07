import subprocess
import os
import shutil
import sv_utils
import sv_ffutils

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

def toInputParams (inputStream):
    params = [];

    if (type(inputStream) is type({})):        
        length = sv_utils.dictValue(inputStream,"length", 0)
        if (length > 0):
            params.append("-t")
            params.append(str(length))
        
        start = sv_utils.dictValue(inputStream,"start", None)
        if start is not None:
            if (start >= 0):
                params.append("-ss")
                params.append(str(start))
            else:
                params.append("-sseof")
                params.append(str(start - length))
        
        params.append("-i")
        file = sv_utils.dictValue(inputStream,"file")
        params.append(file)
        
    else:
        params.append("-i")
        file = inputStream
        params.append(file)

    return params

    
def getDrawTextCommandFromArray (text, opts):
    textSize = float(sv_utils.dictValue(opts,"fontsize", 48))
    paramText = ""
    borderWidth = 0.5 * textSize
    boxcolor=sv_utils.dictValue(opts,"boxcolor", "#80000080")
    fontcolor=sv_utils.dictValue(opts,"fontcolor", "White")

    '''
        if (t > 4)
            x = borderWidth;
        else
        {
            velocity = (width + borderWidth) / 2
            x = (t-4) * velocity
        }
        
        (Tshow - completeTransition) * velocity = -width.
        (Tshow - (Tshow + transitionAlone)) * velocity = -width.
        
        -transitionAlone * velocity = -width => velocity = width/transitionAlone
        
        
    '''
    
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
    for line in fileLines:
        if benchmarkCompletedMark in line:
            currentKey = line[21:]
            posOfEnd = currentKey.index(benchmarkCompletedMark)
            currentKey = currentKey[0:posOfEnd]
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
                
            lineIndexFollowingKey = lineIndexFollowingKey + 1
    return returnedDict
    
# move to UTILS
def getFpsArrayFromBenchmarkFile (episodeName, benchmarkFile):
    #get all names for episode name
    episodeAliases = aliases(episodeName)    
    benchmarkFileDict = parseBenchmarkFile(benchmarkFile)
    if benchmarkFileDict is None:
        return []
    
    keyList = list(benchmarkFileDict)
    for episodeAlias in episodeAliases:
        if episodeAlias in keyList:
            return benchmarkFileDict[episodeAlias]
    
    return []
    
def getTextArrayForEpisode (episode, benchmarkFile=None):
    overlay = sv_utils.dictValue (episode, "overlay", None)
    if (overlay is None):
        return None
    
    # maybe we should call sv_ffutils.ffmpegSafeString for this one, and allow usage
    # of regular text in the config file ...
    textArray = sv_utils.dictValue (overlay, "text", None)
    if (textArray is not None):
        return (textArray)

    benchmark = sv_utils.dictValue (overlay, "benchmark", None)
    if (benchmark is None):
        return None
    
    episodeName = sv_utils.dictValue (episode, "title", None)

    fpsArr = sv_utils.dictValue (benchmark, "FPS values", None)
    if (fpsArr is None):
        if benchmarkFile is None:
            return None
        fpsArr = getFpsArrayFromBenchmarkFile (episodeName, benchmarkFile)
    
    settings = sv_utils.dictValue (benchmark, "settings", None)
    if ( (settings is None) or (0 == len(fpsArr)) ):
        return None

    average = None
    onePercent = None
    pointOnePercent = None
    
    lenTextArr = len(fpsArr)
    if lenTextArr >= 1:
        average = fpsArr[0]
    if lenTextArr >= 2:
        onePercent = fpsArr[1]
    if lenTextArr >= 3:
        pointOnePercent = fpsArr[2]
        
    fpsAsText = getFpsStatsText (average, onePercent, pointOnePercent)
    
    return (["'" + sv_ffutils.ffmpegSafeString(episodeName + " (" + settings) + ")'", fpsAsText ])
        
def getScaleCommand(resolutionPair):
    return "scale="+str(resolutionPair[0])+ "x" +str(resolutionPair[1]) + ":flags=lanczos"
    
# input - the input media to be truncated
# start - the input media to be truncated
def truncate(input, start=None, length=None, output=None, recompress=True):
    params = sv_ffutils.ffmpegParams()
    
    params.append("-i")
    params.append(input)        
    
    if start is not None:
        if (start >= 0):
            params.append("-ss")
            params.append(str(start))
#        else:
#            params.append("-sseof")
#            params.append(str(start - length))
    
    if length is not None and length > 0:
            params.append("-t")
            params.append(str(length))

    if (output == None):
        output = sv_ffutils.defaultOutput (input, "_truncate_" )

    if (not recompress):
        params.append("-c")
        params.append("copy")

    params.append(output)
    
    subprocess.run(params)
    
    return output
    
def overlayAudio (inputVid, inputAudio, output=None, firstStreamAudioWeight=0.1, recompressVideo=True):
    params = sv_ffutils.ffmpegParams();

    params = params + toInputParams(inputVid)    
    params = params + toInputParams(inputAudio)

    inputVideohasAudio = sv_ffutils.hasAudio(inputVid)
    # detect if input video DOES have audio
    if not inputVideohasAudio:
        params.append("-f")
        params.append("lavfi")
        params.append("-i")
        params.append("anullsrc")
    
    params.append ("-map")
    params.append ("0:a?")
    
    params.append ("-map")
    params.append ("1:a")
    
    if not inputVideohasAudio:
        params.append ("-map")
        params.append ("2:a")
    
    if (output == None):
        audioRoot,ext = os.path.splitext (sv_utils.getFileFromInput(inputAudio))
        output = sv_ffutils.defaultOutput (sv_utils.getFileFromInput(inputVid), "_overlay_"  + os.path.basename(audioRoot) )

    weightsStr = str(firstStreamAudioWeight) + " " + str(1 - firstStreamAudioWeight)
        
    params.append ("-filter_complex")
    if inputVideohasAudio:
        params.append ("[0:a][1:a] amix=weights='" + weightsStr + "'")
    else:
        params.append ("[2:a][1:a] amix=weights='" + weightsStr + "':duration=shortest")
        
    params.append ("-map")
    params.append ("0:v")

    if (not recompressVideo):
        params.append ("-c:v")
        params.append ("copy")
    
    params.append(output)
    subprocess.run(params)
    
    return output

def substituteAudio (inputVid, inputAudio, output=None, recompress=True):
    return overlayAudio(inputVid, inputAudio, output, 0.001, recompress)
    
def appendMultiple (streams, output=None, recompressVideo=True, video=True, audio=True):

    params = sv_ffutils.ffmpegParams();
    for stream in streams:
        sar = sv_ffutils.getSar(stream)
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
    
    filter = filter + ":unsafe=1"
    
    params.append(filter)
    
    if (not recompressVideo):
        params.append ("-c:v")
        params.append ("copy")

    params.append ("-fpsmax")
    params.append ("30")
    
    if (output == None):
        secondRoot,ext = os.path.splitext (sv_utils.getFileFromInput(streams[0]))
        output = secondRoot + "_append_" + ext

    params.append(output)
    subprocess.run(params)
    
    return output

def xfadedMultiple (streams, output=None, fadeDuration=1, recompressVideo=True):
    durations = []
    params = sv_ffutils.ffmpegParams();
    for stream in streams:
        if sv_ffutils.getSar(stream) != (1,1):
            stream = setSarToOne(stream)
        params = params + toInputParams(stream)
        durations.append(sv_ffutils.getLengthOfStream(stream))

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
        secondRoot,ext = os.path.splitext (sv_utils.getFileFromInput(streams[0]))
        output = "_append_.mp4"

    params.append(output)
    subprocess.run(params)
    
    return output

def concatNoRecompress(streams, output=None):
    if (output == None):
        secondRoot,ext = os.path.splitext (sv_utils.getFileFromInput(streams[0]))
        output = secondRoot + "_append_" + ext

    params = sv_ffutils.ffmpegParams();
    params.append("-safe")
    params.append("0")

    params.append("-f")
    params.append("concat")
    
    f = open ("concat.txt", "w")
    for stream in streams:
        sar = sv_ffutils.getSar(stream)
        if sar != (1,1) and sar != (0,0):
            stream = setSarToOne(stream)
        f.write("file '" + sv_utils.getFileFromInput(stream) + "'\n")
    f.close()

    params.append("-i")
    params.append("concat.txt")
    params.append("-c")
    params.append("copy")
    params.append(output)
    subprocess.run(params)
    return output
    
    
def append (firstStream, secondStream, output=None, recompressVideo=True):
    return appendMultiple([firstStream, secondStream], output, recompressVideo)

    
def padAudioStream (stream, output=None, ammountBegin = 0, amountEnd = 0):
    params = sv_ffutils.ffmpegParams();

    params = params + toInputParams(stream)    
    params.append ("-map")
    params.append ("0:a")

    params.append("-filter_complex")
    params.append("[0:a]adelay=" + str(ammountBegin * 1000) + ":all=1[intermediate];[intermediate]apad=pad_dur=" + str(amountEnd))
    
    if (output == None):
        secondRoot,ext = os.path.splitext (sv_utils.getFileFromInput(stream))
        output = sv_ffutils.defaultOutput (sv_utils.getFileFromInput(stream), "_padded_"  + str(ammountBegin) + "_" + str(amountEnd))

    params.append(output)
    subprocess.run(params)
    
    return output

def drawText (stream, text, output=None, opts={"fontcolor" : "White", "boxcolor" : "#80000080", "fontsize" : 48}):
    if (text is None):
        print ("WARNING: no text provided, returning the unmodified input " + "'" + sv_utils.getFileFromInput(stream) + "'")
        return sv_utils.getFileFromInput(stream)
        
    params = sv_ffutils.ffmpegParams();

    params = params + toInputParams(stream)    
    params.append("-filter_complex")

    params.append(getDrawTextCommandFromArray(text, opts))
    
    if (output == None):
        secondRoot,ext = os.path.splitext (sv_utils.getFileFromInput(stream))
        output = sv_ffutils.defaultOutput ("", "_withText_"  + ext)

    params.append(output)
    subprocess.run(params)
    
    return output

def scaleVideo(video, resolutionPair, output=None):
    params = sv_ffutils.ffmpegParams();
    params = params + toInputParams(video)    
    params.append("-filter_complex")

    params.append(getScaleCommand(resolutionPair))
    
    if (output == None):
        root,ext = os.path.splitext (sv_utils.getFileFromInput(video))
        output = sv_ffutils.defaultOutput (sv_utils.getFileFromInput(video), "_scaled_" + str(resolutionPair[0]) + "x" + str(resolutionPair[1])  + ext)

    params.append(output)   
    subprocess.run(params)
    
    return output

def setSarToOne(video, output=None):
    params = sv_ffutils.ffmpegParams();
    params = params + toInputParams(video)    
    params.append("-filter_complex")

    params.append("setsar=1")
    
    if (output == None):
        root,ext = os.path.splitext (sv_utils.getFileFromInput(video))
        output = sv_ffutils.defaultOutput (root, "_setSar1_" + ext)
    
    params.append(output)   
    subprocess.run(params)
    
    return output
    
def selectSuitableVideo (paths, desiredLength=30, desiredYRes=1080):
    potentialVideos = []
    for fullVideoPath in paths:
        if (sv_ffutils.getLengthOfStream(fullVideoPath) > desiredLength):
            resolution = sv_ffutils.getResolution (fullVideoPath)
# we favor 1080p videos - they will not require any scaling.
            if (resolution[1] == desiredYRes):
                return fullVideoPath
            else:
                potentialVideos.append(fullVideoPath)
        else:
            potentialVideos.append(fullVideoPath)
    if len (potentialVideos) > 0:
        return potentialVideos[0]
    elif len (paths) > 0:
        return paths[0]
    
    return None
    
# move to UTILS
def getFilesArrayFromFoldersAndNames (folders, names, extensions):
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

def getSuitableVideoFromFolders (folders, names, extensions):
    media = getFilesArrayFromFoldersAndNames (folders, names, extensions)
    return selectSuitableVideo(media)
    
def getSuitableMediaStream (episode, configs, keyInEpisode, defaultMediaKey, extensions):
    names = []

    mediaDict =  sv_utils.dictValue (episode, keyInEpisode, None)
    # see if we can simply return it as is
    if type(mediaDict) is type({}):
        # check that we have a full path for "file"
        dictFile = sv_utils.dictValue (mediaDict, "file", None)
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
          
    if len(names) == 0:
        episodeTitle = sv_utils.dictValue (episode, "title", None)
        if episodeTitle is not None:
            names.append(episodeTitle)
            # TODO: append the aliases as well
            names = names + aliases (episodeTitle)
        
    mediaFolder = sv_utils.dictValue(configs, "mediaFolder", None)
    stockFolder = sv_utils.dictValue(configs, "stockFolder", None)
     
    mediaDict["file"] = getSuitableVideoFromFolders ([mediaFolder, stockFolder], names, extensions)
    if mediaDict["file"] is None:
        defaultMedia = sv_utils.dictValue (configs, defaultMediaKey, None)
        if defaultMedia is None:
            return {}
            
        mediaDict["file"] = getSuitableVideoFromFolders ([mediaFolder, stockFolder], [defaultMedia], extensions)
        
        
    # check if we have a timestamps entry; convert that to start and length.
    timestamps = sv_utils.dictValue (mediaDict, "timestamps", None)
    if timestamps is not None:
        startSecond = sv_utils.getSeconds(timestamps[0])
        endSecond = sv_utils.getSeconds(timestamps[1])
        if startSecond is not None:
            mediaDict["start"] = startSecond
        if endSecond is not None:
            mediaDict["length"] = endSecond - startSecond
    else:
        altVal = sv_utils.dictValue (mediaDict, "start", None)
        if altVal is not None:
            mediaDict["start"] = sv_utils.getSeconds(altVal)

        altVal = sv_utils.dictValue (mediaDict, "length", None)
        if altVal is not None:
            mediaDict["length"] = sv_utils.getSeconds(altVal)
        
    return mediaDict
    
    
    
def getSuitableVideoStream (episode, configs):
    return getSuitableMediaStream (episode, configs, "video", "defaultVideoFile", [".mp4", ".mov", ".avi", ".mkv"])

def getSuitableAudioStream (episode, configs):
    return getSuitableMediaStream (episode, configs, "audio", "defaultAudioFile", [".mp3", ".ogg", ".flac"])

    
def getSuitableVideo (folder, names):
    return getSuitableVideoFromFolders([folder], names, [".mp4", ".mov", ".avi", ".mkv"])


def makeVideoForEpisode (episode, configs, targetRes=(1920,1080) ):
    if sv_utils.dictValue(configs, "TOC", None) is None:
        configs["TOC"] = []

    dir = sv_utils.dictValue(configs, "outputFolder", ".")
    expectedEpisodeVideo = os.path.join(dir, sv_utils.filePathSafeString(episode["title"]))
    for existingFile in os.listdir(dir):
        existingAbsPath = os.path.join(dir, existingFile)
        existingAbsPathNoExt = os.path.splitext(existingAbsPath)[0]
        if expectedEpisodeVideo == existingAbsPathNoExt:
            print ('"' + episode["title"] +'" already has a video: "' + existingAbsPath + '"; will do nothing.')
            configs["TOC"].append({"title" : episode["title"], "length" : sv_ffutils.getLengthOfStream(existingAbsPath), "isChapter" : sv_utils.dictValue(episode, "isChapter", True) })
            return existingAbsPath

    videoDict = getSuitableVideoStream(episode, configs)
    audioDict = getSuitableAudioStream(episode, configs)
    textArray = getTextArrayForEpisode(episode, sv_utils.dictValue(configs, "benchmarkFile", None))
    
    opts = {"padAudio": 1, "videoSoundVolume" : 0.07, "targetRes": targetRes }
    
    audioVolume = sv_utils.dictValue(audioDict, "volume", None)
    if audioVolume is not None:
        opts["videoSoundVolume"] = 1 - float(audioVolume)
    
    builtVideo = makeEpisodeWithAllInputs (videoDict, audioDict, textArray, opts)
    # get extension and dir
    dir = sv_utils.dictValue(configs, "outputFolder", ".")
    ext = os.path.splitext(builtVideo)[1]
    episodeVideo = os.path.join(dir, sv_utils.filePathSafeString(episode["title"]) + ext)
    configs["TOC"].append({"title" : episode["title"], "length" : sv_ffutils.getLengthOfStream(builtVideo), "isChapter" : sv_utils.dictValue(episode, "isChapter", True)})
    shutil.move (builtVideo, episodeVideo)
    return episodeVideo

def buildBackgroundTrack (backgroundTrack, configs):
    #build the background track
    segmentNamePrefix = "backgroundSegment_" + configs["outputFile"].split(".")[0] + "_"
    segmentExt = ".ogg"
    segmentIndex = 0
    audioToConcat = []
    previousTrackEndedAt = 0
    for track in backgroundTrack["audioTracks"]:
        segmentName = segmentNamePrefix + str(segmentIndex) + segmentExt

        # handle padding at the begining.        
        trackIsInsertedAt = None        
        trackIsInsertedAtCfg = sv_utils.dictValue(track, "destinationTimestamp", None)        
        if trackIsInsertedAtCfg is None:
            trackIsInsertedAt = 0
        elif type (trackIsInsertedAtCfg) is type(""):
            trackIsInsertedAt = sv_utils.getSeconds (trackIsInsertedAtCfg)
        else:            
            insertedAt = 0
            for episodeTocDict in configs["TOC"]:
                if episodeTocDict["title"] == trackIsInsertedAtCfg["title"]:
                    break
                insertedAt = insertedAt + float(episodeTocDict["length"])
            trackIsInsertedAt = insertedAt
            
        trackLength = 0
        trackStartsAt = 0
        timestamps = sv_utils.dictValue (track, "timestamps", None)

        if timestamps is not None:
            trackStartsAt = sv_utils.getSeconds(timestamps[0])
            if timestamps[1] is not None:
                endSecond = sv_utils.getSeconds(timestamps[1])
                trackLength = endSecond - trackStartsAt

        if trackLength == 0 or trackLength is None:            
            endsAtEpisode = sv_utils.dictValue (trackIsInsertedAtCfg, "until", None)
            if endsAtEpisode is not None:
                endsAt = 0
                for episodeTocDict in configs["TOC"]:
                    if episodeTocDict["title"] == endsAtEpisode:
                        break
                    endsAt = endsAt + float(episodeTocDict["length"])
                if endsAt > 0:
                    trackLength = endsAt - trackIsInsertedAt
        
        if trackLength == 0 or trackLength is None:            
            trackLength = sv_ffutils.getLengthOfStream(track["file"])
            
        padAtBeginning = trackIsInsertedAt - previousTrackEndedAt
        if padAtBeginning > 0:
            padAudioStream( {"file" : sv_utils.dictValue(track,"file") , "start" : trackStartsAt, "length" :trackLength }, segmentName, padAtBeginning, 0.1 )
            audioToConcat.append(segmentName)
        else:
            audioToConcat.append({"file" : sv_utils.dictValue(track,"file") , "start" : trackStartsAt, "length" :trackLength })
                
        previousTrackEndedAt = trackIsInsertedAt + trackLength
        
        segmentIndex = segmentIndex + 1
    
    backgroundAufioFile = appendMultiple (audioToConcat, "background_track.ogg" , video=False)
    for audioToDelete in audioToConcat:
        if type(audioToDelete) is type(""):
            os.remove(audioToDelete)
    
    return backgroundAufioFile

    
# move to FFUTILS
def getValueForTags (haystack, tags):
    for tag in tags:
        positionOfTag = haystack.find(tag)
        if (positionOfTag < 0):
            continue
        potentialValue = haystack[positionOfTag + len(tag) : ]
        positionOfEnd = potentialValue.find("\n")
        if positionOfEnd > 0:
            potentialValue = potentialValue[0:positionOfEnd]
            if len(potentialValue) > 1:
                return potentialValue
    return None
    
# move to FFUTILS
def getAuthorAndSongName (file):
    finishedProc = subprocess.run (["ffprobe", "-show_format" , file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out = str(finishedProc.stderr) + str(finishedProc.stdout)

    authorName = getValueForTags(out, ["TAG:artist=", "TAG:album_artist=", "TAG:composer="])
    songName = getValueForTags(out, ["TAG:title=", "TAG:album="])
    
    if authorName is None or songName is None:
        splitAfterDash = os.path.basename(file).split("-")
        authorName = splitAfterDash[0]
        songName = splitAfterDash[1].split(".")[0]
    
    return (authorName, songName)
    
def getMusicFileCredits(file):
    # get the author and song name, from either the tags or from file name
    author, song = getAuthorAndSongName (file)
    requiredLicenseText = "Music provided by Audio Library Plus"
    if file.lower().find("bensound") > 0:
        requiredLicenseText = "www.bensound.com"
    
    return author + " - " + song + " (" + requiredLicenseText + ")"
    
def getMusicCreditsString(backgroundTrack):
    fullTracksCredits = "Music tracks:\n"
    for track in backgroundTrack["audioTracks"]:
        fullTracksCredits = fullTracksCredits + getMusicFileCredits (track["file"]) + "\n"
    return fullTracksCredits
    
def isGameEpisode (episode):
    return (sv_utils.dictValue(episode, "overlay", None) is not None)
    
def enhanceYoutubeData (configs):
    youtube = "youtube"
    if sv_utils.dictValue(configs, youtube, None) is None:
        configs[youtube] = {}

    episodes = configs["episodes"]
        
    for episode in episodes:
        if isGameEpisode(episode):
            configs[youtube]["tags"] = configs[youtube]["tags"] + "," + episode["title"]

    for episode in episodes:
        if (sv_utils.dictValue(episode, "overlay", None) is not None):
            configs[youtube]["tags"] = configs[youtube]["tags"] + "," + episode["title"]
    
    chapters = ""
    time = 0
    previousChapterIndex = 0
    for tocEntry in configs["TOC"]:
        if tocEntry["isChapter"]:
            chapters = chapters + sv_utils.secondsToTime(time) + " " + tocEntry["title"] + "\n"
        time = time + float(tocEntry["length"])
    
    configs[youtube]["description"] = configs[youtube]["description"] + "\n\n" + chapters

    backgroundTrack = sv_utils.dictValue(configs, "backgroundTrack", None)
    if backgroundTrack is not None:
        configs[youtube]["description"] = configs[youtube]["description"] + "\n\n" + getMusicCreditsString (backgroundTrack)
        
    configs[youtube]["description"] = configs[youtube]["description"] + "\n\n" + configs[youtube]["links"] 
    
    
def makeVideo (configs):
    
    try:
        os.mkdir(configs["outputFolder"])
    except:
        a = 0

    episodeVideos = []
    for episode in configs["episodes"]:
        try:
            episodeVideo = makeVideoForEpisode(episode, configs)
            episodeVideos.append(episodeVideo)
        except:
            print ("ERR: " + episode["title"])
    
    videoPath = os.path.join(configs["outputFolder"], configs["outputFile"])
    noBackgroundVideo = os.path.join(configs["outputFolder"], "_nobackground.mp4")
    if not os.path.exists(noBackgroundVideo):
        appendMultiple(episodeVideos, noBackgroundVideo)
    else:
        print ('WARNING: "' + noBackgroundVideo + '" already exists; will do nothing and use the existing file')
    
    backgroundTrack = sv_utils.dictValue(configs, "backgroundTrack", None)
    if backgroundTrack is not None:    
        backgroundAudioFile = buildBackgroundTrack (backgroundTrack, configs)        
        videoAudioWeight = 1 - sv_utils.dictValue(backgroundTrack, "volume", 0.1)        
        overlayAudio (noBackgroundVideo, backgroundAudioFile, videoPath, firstStreamAudioWeight=videoAudioWeight)
    else:
        shutil.copyfile(noBackgroundVideo, videoPath)        
    
    enhanceYoutubeData(configs)
    print("\n\n --- youtube -- \n\n")
    for key in configs["youtube"]:
        print(key + "\n---------\n" + str (configs["youtube"][key]) + "\n\n")
    
    return videoPath
    

# needs an audio - see makeAudioForEposiode
def makeEpisodeWithAllInputs (video, audio, textLinesArray, options):

    videoLen = sv_ffutils.getLengthOfStream(video)
    audioLen = sv_ffutils.getLengthOfStream(audio)
    padding = sv_utils.dictValue (options, "padAudio", 1)
    
    audioToVideoLengthRatio = int((audioLen + padding + padding) / videoLen)
    fixedVideo = sv_utils.getFileFromInput (video)
    nextIterationVideo = fixedVideo
    appendToFitToLength = []
    if (audioToVideoLengthRatio > 1):
        for i in range(0, audioToVideoLengthRatio):
            appendToFitToLength.append(video)
        
        fixedVideo = appendMultiple(appendToFitToLength) # this needs rework
    
    videoLen = sv_ffutils.getLengthOfStream(fixedVideo)
    videoStart = sv_utils.dictValue (video, "start", None)
    if videoStart is None:
        videoStart = (videoLen - (audioLen + padding + padding)) * 0.5    
    
    trimmedVideo = truncate (fixedVideo, videoStart, audioLen + padding + padding)
    
    scaledVideo = trimmedVideo
    targetRes = sv_utils.dictValue(options, "targetRes", (1920,1080))
    resolution = sv_ffutils.getResolution(trimmedVideo)
    if (resolution[1] != targetRes[1]):
        scaledVideo = scaleVideo(trimmedVideo, targetRes)
        os.remove(trimmedVideo)
    
    paddedAudio = padAudioStream (audio, "padded.ogg", padding, padding)
    
    videoAudioWeight = sv_utils.dictValue (options, "videoSoundVolume", 0.07)
    
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

# move to UTILS
def aliases(inputName):
    gameAliases = [\
        ["Apex", "Apex Legends", "ApexLegends", "Apex_Legends", "r5apex.exe", "R5Apex"],\
        ["Alien Isolation", "Alien: Isolation", "Alien:Isolation", "AlienIsolation", "Alien_Isolation", "AI.exe", "AI"],\
        ["Call of Duty: Warzone","Call_of_Duty_Warzone", "CallOfDutyWarzone", "COD Warzone", "COD_Warzone", "Warzone", "ModernWarfare.exe", "ModernWarfare"],\
        ["Battlefield V","Battlefield 5", "Battlefield_V", "Battlefield_5", "bfv", "bf5", "bfv.exe"],\
        ["Rainbow Six Siege","Rainbow 6 Siege", "Rainbow Six: Siege","Rainbow 6: Siege", "Rainbow_Six_Siege","Rainbow_6_Siege", \
        "r6s", "RainbowSixSiege","Rainbow6Siege", "RainbowSix", "RainbowSixSiege", "RainbowSix.exe", "RainbowSix"],\
        ["Counter-Strike: Global Offensive","Counter Strike: Global Offensive", "ConunterStrike: Global Offensive",\
        "ConunterStrike", "cs:go","csgo", "cs-go", "csgo.exe"],\
        ["Rocket League","Rocket_League", "RocketLeague", "RocketLeague.exe"],\
        ["Genshin Impact", "GenshinImpact", "Genshin_Impact", "GenshinImpact.exe"], \
        ["Realm Royale", "Realm_Royale", "RealmRoyale", "Realm.exe", "Realm"], \
        ["Rogue Company", "Rogue_Company", "RogueCompany", "RogueCompany.exe"], \
        ["World of Tanks Blitz", "World_of_Tanks_Blitz", "World of Tanks: Blitz", "WorldOfTanksBlitz", "WoT Blitz", "WoT: Blitz",\
        "WoT_Blitz", "wotblitz", "wotblitz.exe"], \
        ["Hyperscape", "Hyperscape.exe"],\
        ["Warframe", "Warframe.x64.exe"],\
        ["Control", "Control_DX11.exe"],\
        ["DOTA2", "dota2.exe"],\
        ["Splitgate", "PortalWars-Win64-Shipping.exe", "PortalWars"],\
        ["Fortnite", "FortniteClient-Win64-Shipping.exe"],\
        ["Valorant", "VALORANT-Win64-Shipping.exe"],\
        ["Paladins", "Paladins.exe"],\
    ]

    if inputName is None:
        for namesArr in gameAliases:
            print(namesArr[0])
        return []
    
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
    print(sv_ffutils.getLengthOfStream ("C:\\Users\\Admin\\Videos\\stock\\jensen_oven.mkv"))
#    print(getFpsStatsText(73, 32, 27, 80, 27))
#    drawText ("merged_audio.mp4", ["'Rainbow 6 Siege (720p, low settings, render scale 100\\\%)'", getFpsStatsText(73, 32, 27)])
#     print(sv_ffutils.getResolution ("audio.ogg"))
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
#    vids = []
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
#    print(parseBenchmarkFile("C:\\Program Files (x86)\\MSI Afterburner\\Benchmark.txt"))
#    concatNoRecompress(vids)
    aliases(None)