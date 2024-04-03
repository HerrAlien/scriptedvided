import scriptedvided

configs = { "defaultAudioFile" : "The Outer Worlds AMD.ogg",\
"mediaFolder" : "F:\\Videos\\TheOuterWorlds_R9", \
"stockFolder" : "F:\\Videos\\stock",\
"outputFolder" : "F:\\Videos\\TheOuterWorlds_R9\\output", \
"outputFile" : "The Outer Worlds R9.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "The Outer Worlds - free on Epic Games Store", "until" : "1920x1080 results"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "1920x1080 results", "until" : "Conclusions"}}, \
{"file" : "Inspired - MaikonMusic  Free Background Music  Audio Library Release.mp3", "timestamps" : ("00:00", None ), "destinationTimestamp" : {"title" : "Conclusions", "until" : "EOF"}}, \
], "volume" : 0.06 },\
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
"tags" : "The Outer Worlds,AMD,Radeon,GCN,R9,R9 290X,R9 280,R9 270,HD 2950,HD7950,HD 7870,HD7870,Epic Games,Epic Games Store",\
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
lastTS = "00:00"
configs["episodes"].append(\
{ "title": "The Outer Worlds - free on Epic Games Store",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "00:11.75" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "IndianaEpicGameStore-Win64-Shipping_2024_03_31_07_57_33_680-converted.mp4" , "start" : "00:36"},\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

# website screenshot
configs["episodes"].append(\
{ "title": "Epic Games",\
"audio" : {"timestamps" : (lastTS, "00:26.9" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "2024-04-01 13-06-02.mkv", "start" : "00:04"},\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]


configs["episodes"].append(\
{ "title": "Below the minimum requirements",\
"audio" : {"timestamps" : (lastTS, "00:42.9" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "2024-04-01 13-06-02.mkv", "start" : "01:04"},\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]


configs["episodes"].append(\
{ "title": "R9 290X",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "00:53.2" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "breel_r9_290x_outside.mp4"},\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "R9 280",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "00:59.3" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "breel_r9_280_outside.mp4"},\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "R9 270",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "01:06.2" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "breel_GigASUS_R9_270.mp4"},\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

# black screen
configs["episodes"].append(\
{ "title": "Test system and settings",\
"audio" : {"timestamps" : (lastTS, "01:09.2" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "black_screen.mkv"},\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]


configs["episodes"].append(\
{ "title": "Z230",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "01:21.6" ), "volume" : 0.999, "padAudio" : 0.1 },\
"overlay" : { \
    "text" : ["'Z230 workstation from HP'",\
              "'CPU\: E3-1241v3 Xeon (i7 4770 equivalent)'",\
              "'RAM\: 32GB DDR3 at 1600 MHz, dual channel'",\
    ]\
}, \
"video" : {"file" : "Z230_closed.mp4", "rotation" : 180}\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

# capture with settings
configs["episodes"].append(\
{ "title": "Settings",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "01:31" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "IndianaEpicGameStore-Win64-Shipping_2024_03_31_17_22_41_226-converted.mp4"},\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]


configs["episodes"].append(\
{ "title": "1920x1080 results",\
"audio" : {"timestamps" : (lastTS, "02:13" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "IndianaEpicGameStore-Win64-Shipping_2024_03_31_07_58_52_988-converted.mp4", "start" :"06:40"},\
"overlay" : { \
    "image" : {"file" : "1080, low settings.png", "chromaColor" : "0x00FF00"}\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]


configs["episodes"].append(\
{ "title": "1600x900 results",\
"audio" : {"timestamps" : (lastTS, "02:58.5" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "IndianaEpicGameStore-Win64-Shipping_2024_03_31_17_17_58_163-converted.mp4", "start" : "00:04"},\
"overlay" : { \
    "image" : {"file" : "900, low settings.png", "chromaColor" : "0x00FF00"}\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "1280x720 results",\
"audio" : {"timestamps" : (lastTS, "03:34" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "IndianaEpicGameStore-Win64-Shipping_2024_03_31_17_22_41_226-converted.mp4", "start" : "01:50"},\
"overlay" : { \
    "image" : {"file" : "720, low settings.png", "chromaColor" : "0x00FF00"}\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

#R9 290X breel?
# overlay with FPS for the 290X
configs["episodes"].append(\
{ "title": "Conclusions",\
"audio" : {"timestamps" : (lastTS, "03:49" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "breel_r9_290x_outside.mp4"},\
"overlay" : { \
    "text" : [scriptedvided.r6sText('1920x1080, low settings, 100% render scale',59,32), \
              scriptedvided.r6sText('1600x900, low settings, 100% render scale', 77,44), \
              scriptedvided.r6sText('1280x720, low settings, 100% render scale', 85,47), \
    ]\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

#R9 280 breel
configs["episodes"].append(\
{ "title": "R9 280 - 720p",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "04:05.25" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "breel_r9_280_outside.mp4"},\
"overlay" : { \
    "text" : [scriptedvided.r6sText('1920x1080, low settings, 100% render scale', 41,29), \
              scriptedvided.r6sText('1600x900, low settings, 100% render scale', 45,28), \
              scriptedvided.r6sText('1280x720, low settings, 100% render scale',57 ,37), \
    ]\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

#R9 270 breel
configs["episodes"].append(\
{ "title": "r9 270 nope",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "04:18.8" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "breel_GigASUS_R9_270.mp4"},\
"overlay" : { \
    "text" : [scriptedvided.r6sText('1920x1080, low settings, 100% render scale',21 ,7), \
              scriptedvided.r6sText('1600x900, low settings, 100% render scale',25 ,8), \
              scriptedvided.r6sText('1280x720, low settings, 100% render scale', 29,11), \
    ]\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

# gameplay
configs["episodes"].append(\
{ "title": "bye",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "04:30" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "IndianaEpicGameStore-Win64-Shipping_2024_03_31_17_17_58_163-converted.mp4", "start" : "02:36"},\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]


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