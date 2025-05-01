''' 
Scripted Video Editor - a bunch of python script to allow rendering of videos 
using FFMPEG.

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

import subprocess
import os
import shutil
import sv_utils
import sv_ffutils
import sv_ops
import random

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
    
# moved to UTILS
def getFpsArrayFromBenchmarkFile (episodeName, benchmarkFile):
    #get all names for episode name
    episodeAliases = aliases(episodeName)    
    benchmarkFileDict = sv_utils.parseBenchmarkFile(benchmarkFile)
    if benchmarkFileDict is None:
        return []
    
    keyList = list(benchmarkFileDict)
    for episodeAlias in episodeAliases:
        if episodeAlias in keyList:
            return benchmarkFileDict[episodeAlias]
    
    return [0,0,0]
    
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
  
def selectSuitableVideo (paths, desiredLength=30, desiredYRes=1080):
    if (len(paths) == 1):
        return paths[0]
    elif (len(paths) > 1):
        return paths[random.randrange(0, len(paths)-1)]
    else:
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

# todo: implement this one!
def getSuitableImage (episode, configs):
    names = []
    overlayDict = overlay = sv_utils.dictValue (episode, "overlay", None)
    if overlayDict is None:
        return None

    imageDictInEpisode = sv_utils.dictValue (overlayDict, "image", None)
    if imageDictInEpisode is None:
        return None
        
    imageFileNameInOverlay = sv_utils.dictValue (imageDictInEpisode, "file", None)
    if imageFileNameInOverlay is None:
        return None

    chromaColor = sv_utils.dictValue (imageDictInEpisode, "chromaColor", "0x00FF00")
        
    mediaFolder = sv_utils.dictValue(configs, "mediaFolder", None)
    stockFolder = sv_utils.dictValue(configs, "stockFolder", None)
     
    mediaDict = {"file" : getSuitableVideoFromFolders ([mediaFolder, stockFolder], [imageFileNameInOverlay], [".png", ".jpg", ".jpeg"]), "chromaColor" : chromaColor}
    
    return mediaDict

    
def getSuitableVideo (folder, names):
    return getSuitableVideoFromFolders([folder], names, [".mp4", ".mov", ".avi", ".mkv"])


def makeVideoForEpisode (episode, configs, targetRes=(1920,1080) ):

    indexInEpisodes = configs["episodes"].index(episode)

    if sv_utils.dictValue(configs, "TOC", None) is None:
        configs["TOC"] = []

    dir = sv_utils.dictValue(configs, "outputFolder", ".")
    expectedEpisodeVideo = os.path.join(dir, sv_utils.filePathSafeString(sv_utils.twoDigitString(indexInEpisodes) + " " + episode["title"]))
#    expectedEpisodeVideo = os.path.join(dir, sv_utils.filePathSafeString(episode["title"]))
    for existingFile in os.listdir(dir):
        existingAbsPath = os.path.join(dir, existingFile)
        existingAbsPathNoExt = os.path.splitext(existingAbsPath)[0]
        if expectedEpisodeVideo == existingAbsPathNoExt:
            print ('"' + episode["title"] +'" already has a video: "' + existingAbsPath + '"; will do nothing.')
            configs["TOC"].append({"title" : episode["title"], "length" : sv_ffutils.getLengthOfStream(existingAbsPath), "isChapter" : sv_utils.dictValue(episode, "isChapter", True) })
            return existingAbsPath

    videoDict = getSuitableVideoStream(episode, configs)
    if videoDict is None or videoDict == {}:
        print ("WARNING: no video for " + episode["title"])
    audioDict = getSuitableAudioStream(episode, configs)
    if audioDict is None or audioDict == {}:
        print ("WARNING: no video for " + episode["title"])
    textArray = getTextArrayForEpisode(episode, sv_utils.dictValue(configs, "benchmarkFile", None))
    if textArray is None:
        print ("WARNING: no overlay text for " + episode["title"])
    overlayImageDict = getSuitableImage(episode, configs)
    if overlayImageDict is None or overlayImageDict == {}:
        print ("WARNING: no overlay image for " + episode["title"])
    
    audioPadding = sv_utils.dictValue(audioDict, "padding", 0.25)
    opts = {"padAudio": audioPadding, "videoSoundVolume" : 0.07, "targetRes": targetRes }
    
    audioVolume = sv_utils.dictValue(audioDict, "volume", None)
    if audioVolume is not None:
        opts["videoSoundVolume"] = 1 - float(audioVolume)
        
    textOpts = {"fontcolor" : "White", "boxcolor" : "#80000080", "fontsize" : 48}
    textOptsFromCfg = sv_utils.dictValue(configs, "textOpts", None)
    if textOptsFromCfg is not None:
        for textOpt in list(textOptsFromCfg):
            textOpts[textOpt] = textOptsFromCfg[textOpt]
            
    opts["textOpts"] = textOpts
    
    opts["padAudio"] = sv_utils.dictValue(audioDict, "padAudio", opts["padAudio"])
    
    builtVideo = makeEpisodeWithAllInputs (videoDict, audioDict, textArray, overlayImageDict, opts)
    # get extension and dir
    dir = sv_utils.dictValue(configs, "outputFolder", ".")
    ext = os.path.splitext(builtVideo)[1]
    episodeVideo = os.path.join(dir, sv_utils.filePathSafeString(sv_utils.twoDigitString(indexInEpisodes) + " " + episode["title"]) + ext)
#    episodeVideo = os.path.join(dir, sv_utils.filePathSafeString(episode["title"]) + ext)
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
            
        audioForSegment = sv_utils.dictValue(track,"file")
        if not os.path.exists (audioForSegment):
            baseFileName = os.path.basename(audioForSegment)
            audioForSegment = os.path.join(configs["stockFolder"], baseFileName)
            
        padAtBeginning = trackIsInsertedAt - previousTrackEndedAt
        if padAtBeginning > 0:
            sv_ops.padAudioStream( {"file" :  audioForSegment, "start" : trackStartsAt, "length" :trackLength }, segmentName, padAtBeginning, 0.1 )
            audioToConcat.append(segmentName)
        else:
            audioToConcat.append({"file" : audioForSegment , "start" : trackStartsAt, "length" :trackLength })
                
        previousTrackEndedAt = trackIsInsertedAt + trackLength
        
        segmentIndex = segmentIndex + 1
    
    backgroundAufioFile = sv_ops.appendMultiple (audioToConcat, "background_track.ogg" , video=False)
    
    print("Audio tracks: ")
    print (audioToConcat)
    
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

    # consider testing all paths from the config, then raise errors
        
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
        sv_ops.appendMultiple(episodeVideos, noBackgroundVideo)
    else:
        print ('WARNING: "' + noBackgroundVideo + '" already exists; will do nothing and use the existing file')
    
    backgroundTrack = sv_utils.dictValue(configs, "backgroundTrack", None)
    if backgroundTrack is not None:    
        backgroundAudioFile = buildBackgroundTrack (backgroundTrack, configs)        
        videoAudioWeight = 1 - sv_utils.dictValue(backgroundTrack, "volume", 0.1)        
        sv_ops.overlayAudio (noBackgroundVideo, backgroundAudioFile, videoPath, firstStreamAudioWeight=videoAudioWeight)
    else:
        shutil.copyfile(noBackgroundVideo, videoPath)        
    
    enhanceYoutubeData(configs)
    print("\n\n --- youtube -- \n\n")
    for key in configs["youtube"]:
        print(key + "\n---------\n" + str (configs["youtube"][key]) + "\n\n")
    
    return videoPath
    

# needs an audio - see makeAudioForEposiode
def makeEpisodeWithAllInputs (video, audio, textLinesArray, overlayImageDict, options):
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
        
        fixedVideo = sv_ops.appendMultiple(appendToFitToLength) # this needs rework
    
    videoLen = sv_ffutils.getLengthOfStream(fixedVideo)
    videoStart = sv_utils.dictValue (video, "start", None)
    if videoStart is None:
        totalSlack = int (videoLen - (audioLen + padding + padding) + 0.5)
        if totalSlack < 0:
            print ("ERR: video length is smaller than audio length + padding. Slack is " + str(totalSlack))
            print ("Video is " + sv_utils.dictValue (video, "file", "N/A"))
            a = 1/0 
        ##videoStart = totalSlack * 0.5    
        if totalSlack == 0:
            videoStart = 0
        else:
            videoStart = random.randrange(0, totalSlack)
    
    fixedVideo = sv_ops.truncate (fixedVideo, videoStart, audioLen + padding + padding)
    
    rotation = sv_utils.dictValue(video, "rotation", None)
    if rotation is not None:
        rotatedVideo = sv_ops.rotateVideo(fixedVideo, rotation)
        os.remove(fixedVideo)
        fixedVideo = rotatedVideo

    targetRes = sv_utils.dictValue(options, "targetRes", (1920,1080))
    resolution = sv_ffutils.getResolution(fixedVideo)
    
    if (resolution[1] != targetRes[1]):
        scaledVideo = sv_ops.scaleVideo(fixedVideo, targetRes)
        os.remove(fixedVideo)
        fixedVideo = scaledVideo
        
    paddedAudio = sv_ops.padAudioStream (audio, "padded.ogg", padding, padding)
    videoAudioWeight = sv_utils.dictValue (options, "videoSoundVolume", 0.07)
    
# then  overlay the audio

    videoWithOverlayedAudio = sv_ops.overlayAudio (fixedVideo, paddedAudio, firstStreamAudioWeight=videoAudioWeight)
    os.remove(fixedVideo)
    os.remove(paddedAudio)
    
    fixedVideo = videoWithOverlayedAudio
    
# overlay the image - optional step
    if overlayImageDict is not None and overlayImageDict != {}:
        videoWithImage = sv_ops.overlayImage (fixedVideo, overlayImageDict, overlayImageDict["chromaColor"])
        os.remove(fixedVideo)
        fixedVideo = videoWithImage
# ------------------    

# then print the text - also optional
    if type(textLinesArray) is type ([]) and len(textLinesArray) > 0:
        videoWithText = sv_ops.drawText (fixedVideo, textLinesArray, opts=options["textOpts"])
        os.remove(fixedVideo)
        fixedVideo = videoWithText
    
    return fixedVideo

# move to UTILS
def aliases(inputName):
    gameAliases = [\
        ["Apex", "Apex Legends", "ApexLegends", "Apex_Legends", "r5apex.exe", "R5Apex", "r5apex_dx12.exe", "r5apex_dx12"],\
        ["Alien Isolation", "Alien: Isolation", "Alien:Isolation", "AlienIsolation", "Alien_Isolation", "AI.exe"],\
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
        ["Control", "Control_DX11.exe", "Control_DX12.exe" , "Control_DX12", "Control_DX11"],\
        ["DOTA2", "DOTA 2", "dota2.exe"],\
        ["Grand Theft Auto V", "gtav", "gta5", "GTA5.exe", "GTA V", "GTA_V", "gta_5"],\
        ["Splitgate", "PortalWars-Win64-Shipping.exe", "PortalWars"],\
        ["Fortnite", "FortniteClient-Win64-Shipping.exe"],\
        ["Valorant", "VALORANT-Win64-Shipping.exe"],\
        ["Paladins", "Paladins.exe"],\
        ["Overwatch 2", "Overwatch", "Overwatch.exe", "Overwatch2", "Overwatch_2"],\
        ["Dying Light", "DyingLightGame", "DyingLightGame.exe", "DyingLight"],\
        ["Resident Evil 4 (Remake)", "re4demo.exe", "re4demo"],\
        ["PUBG", "TslGame.exe", "TslGame"],\
        ["CS2", "Counter-Strike 2" , "cs2.exe"],\
        ["The Finals", "Finals" , "Discovery.exe"],\
        ["Doom Eternal", "DoomEternal" , "DOOMEternalx64vk.exe" ],\
        ["Fallout 4", "Fallout4" , "Fallout4.exe" ],\
        ["Prey", "Prey.exe" ],\
        ["Shadow of the Tomb Raider", "SOTTR", "SOTTR.exe" ],\
        ["Borderlands 3", "Borderlands3", "Borderlands3.exe" ],\
        ["Terminator: Resistance", "Terminator", "Terminator-Win64-Shipping.exe" , "Terminator-Win64-Shipping" ],\
        ["Zenless Zone Zero", "ZenlessZoneZero", "ZenlessZoneZero.exe" ],\
        ["XDefiant", "X-Defiant", "XDefiant.exe" ],\
        ["Far Cry 6", "FarCry 6", "FarCry6Trial", "FarCry6Trial.exe"],\
        ["Delta Force", "DeltaForce", "DeltaForceClient"],\
        ["Marvel Rivals", "MarvelRivals", "Marvel-Win64-Shipping.exe", "Marvel-Win64-Shipping"],\
        ["Robocop", "RoboCop-Win64-Shipping.exe", "RoboCop-Win64-Shipping"],\
        ["Cyberpunk 2077", "Cyberpunk2077.exe", "Cyberpunk2077"],\
    ]

    if inputName is None:
        for namesArr in gameAliases:
            print(namesArr[0])
        return []
    
    arrToReturn = []
    
    for namesArr in gameAliases:
        for potentialName in namesArr:
            if potentialName.upper() == inputName.upper():
                arrToReturn = namesArr

    for namesArr in gameAliases:
        for potentialName in namesArr:
            potentialNameUpper = potentialName.upper()
            inputNameUpper = inputName.upper()
            if potentialNameUpper.find(inputNameUpper) >= 0 or inputNameUpper.find(potentialNameUpper) >= 0:
                arrToReturn = namesArr

    if len(arrToReturn) == 0:
        print ("WARNING: '" + inputName + "' has no known aliases.")
    else:
        uppedArr = []
        for name in arrToReturn:
            uppedArr.append(name.upper())
        
        arrToReturn = uppedArr
        
    return arrToReturn # no lnown
    
def r6sText (settings, average, _1percent):
    text = settings + " - Average: " + str(average) + "fps, 1% lows: " + str(_1percent) + "fps"
    return "'" + sv_ffutils.ffmpegSafeString(text) + "'"

def nextTS (configs):
    return configs["episodes"][-1]["audio"]["timestamps"][1];

    
if __name__ == "__main__":
#   truncatedvid = sv_ops.truncate ( "C:\\Users\\Admin\\Videos\\hd7770\\hd7770_RainbowSix_720p_100renderScale.mp4", -10, 30, "vid.mp4" )
#   truncatedvid = sv_ops.scaleVideo ( "C:\\Users\\Admin\\Videos\\hd7770\\hd7770_RainbowSix_720p_100renderScale.mp4", (1920,1080), "zz.mp4" )
#   truncatedaudio = truncate ( "C:\\Users\\Admin\\Videos\\Generic old GPU advice.ogg", -10, 30, "audio.ogg" )
#   truncatedaudio2 = truncate ("C:\\Users\\Admin\\Videos\\Generic old GPU advice.ogg", None, -2, 30)
#   sv_ops.overlayAudio ({"file":"C:\\Users\\Admin\\Videos\\hd7770\\hd7770_RainbowSix_720p_100renderScale.mp4", "start" : -10, "length" : 30}, \
#   {"file":"C:\\Users\\Admin\\Videos\\Generic old GPU advice.ogg", "start":-10, "length" : 30} , "merged_audio.mp4", 0.15)
#   truncatedvid1 = truncate ("C:\\Users\\Admin\\Videos\\hd7770\\hd7770_RainbowSix_720p_100renderScale.mp4", "t1.mp4", -40, 10)
#   truncatedvid2 = truncate ("C:\\Users\\Admin\\Videos\\hd7770\\hd7770_RainbowSix_720p_100renderScale.mp4", "t2.mp4", -10, 10)
#   sv_ops.append({"file":"C:\\Users\\Admin\\Videos\\hd7770\\hd7770_RainbowSix_720p_100renderScale.mp4", "start" : -10, "length" : 10}, \
#   {"file":"C:\\Users\\Admin\\Videos\\hd7770\\hd7770_RainbowSix_720p_100renderScale.mp4", "start" : -40, "length" : 10}, "appended.mp4")
    #print(sv_ffutils.getLengthOfStream ("C:\\Users\\Admin\\Videos\\stock\\jensen_oven.mkv"))
#    print(getFpsStatsText(73, 32, 27, 80, 27))
#    sv_ops.drawText ("merged_audio.mp4", ["'Rainbow 6 Siege (720p, low settings, render scale 100\\\%)'", getFpsStatsText(73, 32, 27)])
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
#    sv_ops.scaleVideo ("C:\\Users\\Admin\\Videos\\hd5770\\hd5770_AlienIsolation_1200pUltra.mp4", (1920, 1080), "C:\\Users\\Admin\\Videos\\hd5770\\output\\Alien - Isolation.mp4")    
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
    #sv_ops.overlayAudio ({"file":"C:\\Users\\Admin\\Videos\\hd7770\\hd7770_RainbowSix_720p_100renderScale.mp4", "start" : -10, "length" : 30}, \
#{"file":"C:\\Users\\Admin\\Videos\\Generic old GPU advice.ogg"} , "merged_audio.mp4", 0.15)
#    print(parseBenchmarkFile("C:\\Program Files (x86)\\MSI Afterburner\\Benchmark.txt"))
#    sv_ops.concatNoRecompress(vids)
#    aliases(None)
#    sv_ops.rotateVideo("C:\\Users\\Admin\\Videos\\msi_hd7770\\IMG_0059.MOV", 90)
#    sv_ops.rotateVideo("C:\\Users\\Admin\\Videos\\msi_hd7770\\fan controller, glued in.mp4", 90)
    sv_ops.overlayImage("F:\\Videos\\stock\\6500xt_short_rant.mp4", "F:\\Videos\\gta5_vs_ts2\\720_2.png", output="F:\\Videos\\1.mp4")