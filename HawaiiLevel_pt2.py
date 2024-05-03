import scriptedvided

configs = { "defaultAudioFile" : "HawaiiLevel_v1.ogg",\
"mediaFolder" : "F:\\Videos\\HawaiiLevel_v1", \
"stockFolder" : "F:\\Videos\\stock",\
"outputFolder" : "F:\\Videos\\HawaiiLevel_v1\\output", \
"outputFile" : "HawaiiLevel_v1.mp4", \
"benchmarkFile" : "",\
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#00008080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "Taking my own advice, again", "until" : "Resident Evil 4 - balanced"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Resident Evil 4 - balanced", "until" : "When medium is better than high"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "When medium is better than high", "until" : "Conclusions"}}, \
{"file" : "Inspired - MaikonMusic  Free Background Music  Audio Library Release.mp3", "timestamps" : ("00:00", None ), "destinationTimestamp" : {"title" : "Conclusions", "until" : "EOF"}}, \
], "volume" : 0.045 },\
"episodes" : [],\
"youtube" : {"title" : "  ...  ... ", \
"description" : '''In this one we're testing the 4(?)GB GTX 970 using some games from today.''',\
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
"tags" : "NVidia,GeForce,GTX,GTX970,GTX 970,Maxwell,Maxwell 2.0,AMD,Radeon,GCN,Polaris,R9 290X,RX570,RX 570",\
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
{ "title": "Taking my own advice, again",\
"audio" : {"timestamps" : (lastTS, "00:18.9" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : ""},\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "What is good enough",\
"audio" : {"timestamps" : (lastTS, "00:34.9" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : ""},\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Meet the (same) hardware",\
"audio" : {"timestamps" : (lastTS, "00:39.6" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "breel_R9_290_RX570_GTX970_attic.mp4", "start" : "00:40", "rotation" : "90" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "GTX 970",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "00:43.4" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "breel_autumn_GTX970.mp4" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "R9 290X",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "00:52" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "breel_r9_290x_outside_dog.mp4" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "RX570",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "00:58.8" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "breel_autumn_RX570.mp4" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Z230",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "01:14.7" ), "volume" : 0.999, "padAudio" : 0.1 },\
"overlay" : { \
    "text" : ["'Z230 workstation from HP'",\
              "'CPU\: E3-1241v3 Xeon (i7 4770 equivalent)'",\
              "'RAM\: 32GB DDR3 at 1600 MHz, dual channel'",\
    ]\
}, \
"video" : {"file" : "Z230_closed.mp4", "rotation" : 180}\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

#########################################

# ===========================================================================
configs["episodes"].append(\
{ "title": "Resident Evil 4 - balanced",\
"audio" : {"timestamps" : (lastTS, "01:34.7" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "R_e_4_low_balanced.mp4"},\
"overlay" : { \
    "image" : {"file" : "re4-low-balanced.png", "chromaColor" : "0x00FF00"}\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Resident Evil 4 - balanced 1080",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "02:15" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "r9_290x_r_e4demo_balanced_s60.mp4", "start" : "01:10"},\
"overlay" : { \
    "image" : {"file" : "re4-balanced-1080.png", "chromaColor" : "0x00FF00"}\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Resident Evil 4 - balanced 900p",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "02:39.3" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "rx570_re4demo_balanced.mp4", "start" : "00:10"},\
"overlay" : { \
    "image" : {"file" : "re4-balanced-900.png", "chromaColor" : "0x00FF00"}\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]


# ===========================================================================
configs["episodes"].append(\
{ "title": "Far Cry 6 - ultra settings",\
"audio" : {"timestamps" : (lastTS, "03:01.6" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "FarCry6Trial_ultra.mp4"},\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Far Cry 6 - ultra settings 1080",\
"audio" : {"timestamps" : (lastTS, "03:35.8" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "FarCry6Trial_ultra.mp4"},\
"isChapter" : False, \
"overlay" : { \
    "image" : {"file" : "fc6-ultra-results.png", "chromaColor" : "0x00FF00"}\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Far Cry 6 - high settings 1080",\
"audio" : {"timestamps" : (lastTS, "03:55.7" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "FarCry6Trial_high.mp4"},\
"isChapter" : False, \
"overlay" : { \
    "image" : {"file" : "fc6-high-results.png", "chromaColor" : "0x00FF00"}\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]


# ===========================================================================
configs["episodes"].append(\
{ "title": "When medium is better than high",\
"audio" : {"timestamps" : (lastTS, "04:24.8" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "tow_high_medium.mp4"},\
"overlay" : { \
    "image" : {"file" : "tow-high-medium.png", "chromaColor" : "0x00FF00"}\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "tow - medium results",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "04:53.4" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "IndianaEpicGameStore-Win64-Shipping_2024_03_31_17_47_13_622-converted.mp4"},\
"overlay" : { \
    "image" : {"file" : "tow-medium.png", "chromaColor" : "0x00FF00"}\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "tow - low results",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "05:10.5" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "IndianaEpicGameStore-Win64-Shipping_2024_03_31_17_22_41_226-converted.mp4"},\
"overlay" : { \
    "image" : {"file" : "tow-low.png", "chromaColor" : "0x00FF00"}\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "tow - medium 900 results",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "05:24.7" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "IndianaEpicGameStore-Win64-Shipping_2024_03_31_17_06_36_774-converted.mp4"},\
"overlay" : { \
    "image" : {"file" : "tow-medium-900.png", "chromaColor" : "0x00FF00"}\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]



# average FPS
configs["episodes"].append(\
{ "title": "Conclusions",\
"audio" : {"timestamps" : (lastTS, "05:35.5" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : ""},\
"overlay" : { \
    "image" : {"file" : "sum-avg-and-one-percent.png", "chromaColor" : "0x00FF00"}\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "subscribe",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "05:46.4" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : ""},\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Bye",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "05:53" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "breel_R9_290_RX570_GTX970_attic.mp4", "start" : "00:40", "rotation" : "90" },\
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