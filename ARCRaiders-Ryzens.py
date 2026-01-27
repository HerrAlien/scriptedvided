import scriptedvided

configs = { "defaultAudioFile" : "ARCRaiders-Ryzens.ogg",\
"mediaFolder" : "F:\\Videos\\ARCRaiders-Ryzens", \
"stockFolder" : "F:\\Videos\\stock",\
"outputFolder" : "F:\\Videos\\ARCRaiders-Ryzens\\output", \
"outputFile" : "ARCRaiders-Ryzens.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "System requirements, again", "until" : "settngs and gameplay video"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "settngs and gameplay video", "until" : "Conclusions"}}, \
{"file" : "Inspired - MaikonMusic  Free Background Music  Audio Library Release.mp3", "timestamps" : ("00:00", None ), "destinationTimestamp" : {"title" : "Conclusions", "until" : "EOF"}}, \
], "volume" : 0.045 },\
"episodes" : [],\
"youtube" : {"title" : " ", \
"description" : ''' ''',\
"links" : '''
Track: Bliss Of Heaven - SOMM [Audio Library Release]
Music provided by Audio Library Plus
Watch: https://www.youtube.com/watch?v=JQ6mKeQLZak&t=0s
Free Download / Stream: https://alplus.io/blisss-heaven

Track: Far Far Away - Ferco [Audio Library Release]
Music provided by Audio Library Plus
Watch: https://www.youtube.com/watch?v=SrkQ3K1umlc&t=0s 
Free Download / Stream: https://alplus.io/far-far-away

Track: Inspired - MaikonMusic [Audio Library Release]
Music provided by Audio Library Plus
Watch: https://www.youtube.com/watch?v=RUkdTkk_52o&t=0s
Free Download / Stream: https://alplus.io/inspired

''', \
"tags" : "ARC,ARC Raiders,AMD,Ryzen 5 5600,R5 5600,Ryzen 5 3600,R5 3600,Ryzen 5 2600,R5 2600,APU,Ryzen,Ryzen 5,Ryzen 3,Ryzen 3 3200G,Ryzen 5 2400G,Ryzen 5 4600G,R6 2400G,R5 4600G,R3 3200G",\
"language" : "EN", \
"Caption certification" : "None",\
"recording date" : None,\
"video location" : None, \
"category" : "Gaming", \
"subtitles" : None, \
"endscreen" : None, \
"cards" : None, \
}\
}

# gameplay
configs["episodes"].append(\
{ "title": "System requirements, again",\
"audio" : {"timestamps" : ("00:00", "00:11.5" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : " "},\
})

configs["episodes"].append(\
{ "title": "CPU req",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:30.8" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : " "},\
"overlay" : { \
    "image" : {"file" : "ARC_overlay_requirements.png"}\
}, \
})

configs["episodes"].append(\
{ "title": "The CPUs",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:34.3" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : " "},\
})

configs["episodes"].append(\
{ "title": "R5 5600",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:43.7" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : " "},\
})

configs["episodes"].append(\
{ "title": "R5 3600",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:56.1" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : " "},\
})

configs["episodes"].append(\
{ "title": "R5 2600",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:06" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : " "},\
})

configs["episodes"].append(\
{ "title": "all 6 cores",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:13.4" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : " "},\
"isChapter" : False, \
})

configs["episodes"].append(\
{ "title": "The APUs",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:15.8" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : " "},\
"isChapter" : False, \
})

configs["episodes"].append(\
{ "title": "3200g",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:26.4" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : " "},\
})

configs["episodes"].append(\
{ "title": "2400g",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:36.7" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : " "},\
})

configs["episodes"].append(\
{ "title": "4600g",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:46.9" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : " "},\
})

# capture with settings
configs["episodes"].append(\
{ "title": "settngs and gameplay video",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:03.1" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : " "},\
"overlay" : { \
    "text" : ["'Test settings\: 1280x720, 50\% render scale, low settings'",\
    ]\
}, \
})


# black screen
configs["episodes"].append(\
{ "title": "Test system and settings",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:19.3" ), "volume" : 0.999, "padAudio" : 0.1 },\
"overlay" : { \
    "text" : ["'Custom PC'",\
              "'CPUs and APUs\: R5 5600, R5 3600, R5 2600, R5 4600G, R5 2400G, R3 3200G'",\
              "'RAM\: 32GB DDR4, 3000MHz, dual channel'",\
              "'GPU\: RX 580'",\
    ]\
}, \
"video" : {"file" : " "},\
})

# capture with settings
configs["episodes"].append(\
{ "title": "bar to cross",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:30.7" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : " "},\
})

# just the quad cores
configs["episodes"].append(\
{ "title": "1280x720 results",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:04.5" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : " "},\
"overlay" : { \
    "image" : {"file" : "ARC Raiders, 1920x1080, low settings.png"}\
}, \
})

configs["episodes"].append(\
{ "title": "Add 2600",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:20.6" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : " "},\
"isChapter" : False, \
})

configs["episodes"].append(\
{ "title": "Add 3600 and 4600g",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:49.9" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : " "},\
"isChapter" : False, \
})

configs["episodes"].append(\
{ "title": "Add 5600",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:04.5" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : " "},\
"isChapter" : False, \
})

# quads are still useful
configs["episodes"].append(\
{ "title": "Conclusions",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:14.3" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : " "},\
})

#R9 270 breel
configs["episodes"].append(\
{ "title": "3600 sweetspot",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:21.3" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : " "},\
})

#R9 270 breel
configs["episodes"].append(\
{ "title": "intel preview",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:32" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : " "},\
})

# gameplay
configs["episodes"].append(\
{ "title": "bye with gameplay",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:38" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : " "},\
})


#scriptedvided.makeVideoForEpisode(configs["episodes"][1], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][4], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][11], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][12], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][13], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][8], configs)
#print(scriptedvided.makeVideoForEpisode(configs["episodes"][9], configs))
#print(scriptedvided.getSuitableVideoStream(configs["episodes"][9], configs))
#print (configs["youtube"])
#print(scriptedvided.getMusicCreditsString(configs["backgroundTrack"]))
#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "Alien Isolation"][0], configs)
#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "actual 1080 results"][0], configs)
#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "actual 900 results"][0], configs)
#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "actual 720 results"][0], configs)
#print (scriptedvided.getSuitableImage([x for x in configs["episodes"] if x["title"] == "actual 1080 results"][0], configs))

scriptedvided.makeVideo(configs)

# meeds better video, or maybe break it up