import scriptedvided

configs = { "defaultAudioFile" : "Fortnite_reload_CapeVerde.ogg",\
"mediaFolder" : "F:\\Videos\\Fortnite_Reload_capeVerde", \
"stockFolder" : "F:\\Videos\\stock",\
"outputFolder" : "F:\\Videos\\Fortnite_Reload_capeVerde\\output", \
"outputFile" : "Fortnite_Reload_capeVerde.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "More than old locations for a brand new game mode", "until" : "1920x1080 results"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "1920x1080 results", "until" : "Conclusions"}}, \
{"file" : "Inspired - MaikonMusic  Free Background Music  Audio Library Release.mp3", "timestamps" : ("00:00", None ), "destinationTimestamp" : {"title" : "Conclusions", "until" : "EOF"}}, \
], "volume" : 0.045 },\
"episodes" : [],\
"youtube" : {"title" : "  ", \
"description" : '''In this video, we'll see if 3 of the AMD Radeon entry level R7 cards handle The new Reload mode in Fortnite.
As usual, we're pairing the cards with the i7 4770 equivalent Xeon (E3-1241 v3), and 32 GB DDR3 @1600MHz, in dual channel.''',\
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
"tags" : "Fortnite,Fortnite Reload,Reload,GCN,AMD,Radeon,CapeVerde,Cape Verde,R7 250,R7 250E,R7 250 E,R7 250 512SP,HD7750,HD 7750,R7 250X,R7 250 X,HD7770,HD 7770",\
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

lastTS = "00:00"
configs["episodes"].append(\
{ "title": "More than old locations for a brand new game mode",\
"audio" : {"timestamps" : (lastTS, "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : ""},\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

# this will be split up
configs["episodes"].append(\
{ "title": "The GPUs and test system",\
"audio" : {"timestamps" : (lastTS, "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "stock_CapeVerde_family.mp4", "start" : "00:00", "rotation" : 90}\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "HD 7770",\
"isChapter" : False,\
"audio" : {"timestamps" : (lastTS, "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "stock_CapeVerde_family.mp4", "start" : "00:51", "rotation" : 90}\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "HD 7750",\
"isChapter" : False,\
"audio" : {"timestamps" : (lastTS, "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "stock_CapeVerde_family.mp4", "start" : "01:40", "rotation" : 90}\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "R7 250",\
"isChapter" : False,\
"audio" : {"timestamps" : (lastTS, "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "stock_CapeVerde_family.mp4", "start" : "02:24", "rotation" : 90}\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Z230",\
"isChapter" : False,\
"audio" : {"timestamps" : (lastTS, "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"overlay" : { \
    "text" : ["'Z230 workstation from HP'",\
              "'CPU\: E3-1241v3 Xeon (i7 4770 equivalent)'",\
              "'RAM\: 32GB DDR3 at 1600 MHz, dual channel'",\
    ]\
}, \
"video" : {"file" : "Z230_closed.mp4" , "rotation" : 180}\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "1920x1080 results",\
"audio" : {"timestamps" : (lastTS, "" ), "padAudio" : 0.1 },\
"video" : {"file" : ""},\
"overlay" : { \
    "image" : {"file" : "1080, low settings.png", "chromaColor" : "0x00FF00"}\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "1920x1080 reload results",\
"isChapter" : False,\
"audio" : {"timestamps" : (lastTS, "" ), "padAudio" : 0.1 },\
"video" : {"file" : ""},\
"overlay" : { \
    "image" : {"file" : "1080, reload.png", "chromaColor" : "0x00FF00"}\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]


configs["episodes"].append(\
{ "title": "1600x900 results",\
"audio" : {"timestamps" : (lastTS, "" ), "padAudio" : 0.1 },\
"video" : {"file" : ""},\
"overlay" : { \
    "image" : {"file" : "900, low settings.png", "chromaColor" : "0x00FF00"}\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "1600x900 reload results",\
"isChapter" : False,\
"audio" : {"timestamps" : (lastTS, "" ), "padAudio" : 0.1 },\
"video" : {"file" : ""},\
"overlay" : { \
    "image" : {"file" : "900, reload.png", "chromaColor" : "0x00FF00"}\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]


configs["episodes"].append(\
{ "title": "1280x720 results",\
"audio" : {"timestamps" : (lastTS, "" ), "padAudio" : 0.1 },\
"video" : {"file" : ""},\
"overlay" : { \
    "image" : {"file" : "720, low settings.png", "chromaColor" : "0x00FF00"}\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "1280x720 reload results",\
"isChapter" : False,\
"audio" : {"timestamps" : (lastTS, "" ), "padAudio" : 0.1 },\
"video" : {"file" : ""},\
"overlay" : { \
    "image" : {"file" : "720, reload.png", "chromaColor" : "0x00FF00"}\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]



configs["episodes"].append(\
{ "title": "Conclusions",\
"audio" : {"timestamps" : (lastTS, "" ), "padAudio" : 0.1 },\
"video" : {"file" : "stock_CapeVerde_family.mp4", "start" : "00:00", "rotation" : 90}\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "2x gain",\
"isChapter" : False,\
"audio" : {"timestamps" : (lastTS, "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : ""},\
"overlay" : { \
    "image" : {"file" : "Regular vs Reload 720.png", "chromaColor" : "0x00FF00"}\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "fewer players",\
"isChapter" : False,\
"audio" : {"timestamps" : (lastTS, "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : ""},\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "nice mod",\
"isChapter" : False,\
"audio" : {"timestamps" : (lastTS, "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : ""},\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Bye",\
"isChapter" : False,\
"audio" : {"timestamps" : (lastTS, "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : ""}\
})

#scriptedvided.makeVideoForEpisode(configs["episodes"][15], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][9], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][8], configs)
#print(scriptedvided.makeVideoForEpisode(configs["episodes"][9], configs))
#print(scriptedvided.getSuitableVideoStream(configs["episodes"][9], configs))
#print (configs["youtube"])
#print(scriptedvided.getMusicCreditsString(configs["backgroundTrack"]))
#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "Usefulness of the HD 6850"][0], configs)
#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "actual 1080 results"][0], configs)
#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "actual 900 results"][0], configs)
#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "actual 720 results"][0], configs)
#print (scriptedvided.getSuitableImage([x for x in configs["episodes"] if x["title"] == "actual 1080 results"][0], configs))

scriptedvided.makeVideo(configs)
