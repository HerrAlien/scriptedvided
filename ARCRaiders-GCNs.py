import scriptedvided

configs = { "defaultAudioFile" : "ARCRaiders-GCNs.ogg",\
"mediaFolder" : "F:\\Videos\\ARCRaiders-GCNs", \
"stockFolder" : "F:\\Videos\\stock",\
"outputFolder" : "F:\\Videos\\ARCRaiders-GCNs\\output", \
"outputFile" : "ARCRaiders-GCNs.mp4", \
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
"tags" : "ARC,ARC Raiders,AMD,Radeon,Vega,Radeon Graphics,RX Vega,Vega 7,Vega 8,Vega 11,Radeon Graphics 448SP,APU,Ryzen,Ryzen 5,Ryzen 3,Ryzen 3 3200G,Ryzen 5 2400G,Ryzen 5 4600G",\
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
{ "title": "We must test even older GPUs",\
"audio" : {"timestamps" : ("00:00", "00:17.4" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : " "},\
"overlay" : { \
    "image" : {"file" : "ARC_overlay_requirements.png"}\
}, \
})

configs["episodes"].append(\
{ "title": "Need more than 2 GB",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : " "},\
})

configs["episodes"].append(\
{ "title": "The GPUs",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : " "},\
})

configs["episodes"].append(\
{ "title": "R9 290X",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : " "},\
})

configs["episodes"].append(\
{ "title": "R9 280",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : " "},\
})

configs["episodes"].append(\
{ "title": "r9 370",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : " "},\
})

configs["episodes"].append(\
{ "title": "r9 370 GPUZ",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : " "},\
})


# black screen
configs["episodes"].append(\
{ "title": "Test system",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"overlay" : { \
    "text" : ["'Custom PC'",\
              "'CPU\: Ryzen 5 5600'",\
              "'RAM\: 32GB DDR4, 3600MHz, dual channel'",\
              "'GPUs\: Radeon R9 370 1024, Radeon R9 280, Radeon R9 290X'",\
    ]\
}, \
"video" : {"file" : " "},\
})

# r9 370, both frequencies
configs["episodes"].append(\
{ "title": "1920x1080 results",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : " "},\
"overlay" : { \
    "image" : {"file" : ""}\
}, \
})

configs["episodes"].append(\
{ "title": "1080 plus R9 280",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : " "},\
"overlay" : { \
    "image" : {"file" : ""}\
}, \
})

configs["episodes"].append(\
{ "title": "1080 plus R9 290x",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : " "},\
"overlay" : { \
    "image" : {"file" : ""}\
}, \
})

# R9 290X only
configs["episodes"].append(\
{ "title": "1600x900 results",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : " "},\
"overlay" : { \
    "image" : {"file" : "ARC Raiders, 1600x900, low settings.png"}\
}, \
})

configs["episodes"].append(\
{ "title": "900p plus r9 280",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : " "},\
"overlay" : { \
    "image" : {"file" : "ARC Raiders, 1600x900, low settings.png"}\
}, \
})

# both frequencies
configs["episodes"].append(\
{ "title": "900p plus r9 370",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : " "},\
"overlay" : { \
    "image" : {"file" : "ARC Raiders, 1600x900, low settings.png"}\
}, \
})

# r9 290X
configs["episodes"].append(\
{ "title": "1280x720 results",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : " "},\
"overlay" : { \
    "image" : {"file" : "ARC Raiders, 1280x720, low settings.png"}\
}, \
})

# add R9 280
configs["episodes"].append(\
{ "title": "720p plus R9 280",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : " "},\
"overlay" : { \
    "image" : {"file" : "ARC Raiders, 1280x720, low settings.png"}\
}, \
})

# add R9 370
configs["episodes"].append(\
{ "title": "720p plus R9 370",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : " "},\
"overlay" : { \
    "image" : {"file" : "ARC Raiders, 1280x720, low settings.png"}\
}, \
})

# breel with APUs
configs["episodes"].append(\
{ "title": "Conclusions",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : " "},\
})

#R9 270 breel
configs["episodes"].append(\
{ "title": "breel 290X",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : " "},\
})

#R9 270 breel
configs["episodes"].append(\
{ "title": "breel 280",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : " "},\
})

#R9 370 breel
configs["episodes"].append(\
{ "title": "breel 370",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : " "},\
})

#R9 370 breel
configs["episodes"].append(\
{ "title": "gameplay",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : " "},\
})

# gameplay
configs["episodes"].append(\
{ "title": "bye with family breel",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "volume" : 0.999, "padAudio" : 0.1 },\
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