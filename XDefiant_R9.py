import scriptedvided

configs = { "defaultAudioFile" : "XDefiant_R9.ogg",\
"mediaFolder" : "F:\\Videos\\XDefiant_R9", \
"stockFolder" : "F:\\Videos\\stock",\
"outputFolder" : "F:\\Videos\\XDefiant_R9\\output", \
"outputFile" : "XDefiant_R9.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : " ", "until" : " "}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : " ", "until" : " "}}, \
{"file" : "Inspired - MaikonMusic  Free Background Music  Audio Library Release.mp3", "timestamps" : ("00:00", None ), "destinationTimestamp" : {"title" : " ", "until" : "EOF"}}, \
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
"tags" : "XDefiant,AMD,Radeon,GCN,R9,R9 290X,R9 280,R9 270,HD 2950,HD7950,HD 7870,HD7870,Ubisoft Connect",\
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
{ "title": "Missed the launch",\
"audio" : {"timestamps" : (lastTS, "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "XDefiant_2024_05_28_23_50_27_454.mp4"},\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Below the minimum requirements. Again.",\
"audio" : {"timestamps" : (lastTS, "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : ""},\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "The R9 family",\
"audio" : {"timestamps" : (lastTS, "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "R9_family_poor.mkv"},\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "R9 290X",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "breel_r9_290x_outside.mp4"},\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "R9 280",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "breel_r9_280_outside.mp4"},\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "R9 270",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "breel_r9_270_outside.mp4"},\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

# black screen
configs["episodes"].append(\
{ "title": "Test system and settings",\
"audio" : {"timestamps" : (lastTS, "" ), "volume" : 0.999, "padAudio" : 0.1 },\
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
{ "title": "captures at 720",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "XDefiant_2024_05_28_23_01_28_977.mp4"},\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]


configs["episodes"].append(\
{ "title": "1920x1080 results",\
"audio" : {"timestamps" : (lastTS, "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "XDefiant_2024_05_28_22_53_25_357.mp4"},\
"overlay" : { \
    "image" : {"file" : "1080, low settings.png", "chromaColor" : "0x00FF00"}\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]


configs["episodes"].append(\
{ "title": "1280x720 results",\
"audio" : {"timestamps" : (lastTS, "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "XDefiant_2024_05_28_23_27_12_246.mp4"},\
"overlay" : { \
    "image" : {"file" : "720, low settings.png", "chromaColor" : "0x00FF00"}\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

#R9 290X breel?
# overlay with FPS for the 290X
configs["episodes"].append(\
{ "title": "Conclusions",\
"audio" : {"timestamps" : (lastTS, "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "XDefiant_2024_05_28_23_50_27_454.mp4"},\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

#R9 280 breel
configs["episodes"].append(\
{ "title": "minimum req are fine",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : ""},\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

#R9 270 breel
configs["episodes"].append(\
{ "title": "r9 270",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : ""},\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

# gameplay
configs["episodes"].append(\
{ "title": "bye",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "XDefiant_2024_05_28_23_27_12_246.mp4"},\
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