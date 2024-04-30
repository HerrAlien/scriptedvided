import scriptedvided

configs = { "defaultAudioFile" : "HawaiiLevel_v1.ogg",\
"mediaFolder" : "F:\\Videos\\HawaiiLevel_v1", \
"stockFolder" : "F:\\Videos\\stock",\
"outputFolder" : "F:\\Videos\\HawaiiLevel_v1\\output", \
"outputFile" : "HawaiiLevel_v1.mp4", \
"benchmarkFile" : "",\
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#00008080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "Taking my own advice", "until" : "Control - high settings"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Control - high settings", "until" : "Conclusions"}}, \
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
{ "title": "Taking my own advice",\
"audio" : {"timestamps" : (lastTS, "00:17.4" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "breel_R9_290_RX570_GTX970_attic.mp4", "start" : "00:40", "rotation" : "90" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "This is for single player",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "00:34.6" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "rx570_re4demo_quality.mp4", "start" : "03:30" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "What is good enough",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "00:45.8" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "stock_DOOMEternal_2023_12_26.mp4" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Meet the hardware",\
"audio" : {"timestamps" : (lastTS, "00:51.5" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "breel_R9_290_RX570_GTX970_attic.mp4", "start" : "00:40", "rotation" : "90" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "R9 290X",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "01:00" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "breel_r9_290x_outside_dog.mp4" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "GTX 970",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "01:14.9" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "breel_autumn_GTX970.mp4" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "RX570",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "01:24.8" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "breel_autumn_RX570.mp4" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Z230",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "01:36.5" ), "volume" : 0.999, "padAudio" : 0.1 },\
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


configs["episodes"].append(\
{ "title": "Control - high settings",\
"audio" : {"timestamps" : (lastTS, "01:49.6" ), "padAudio" : 0.1 },\
"video" : {"file" : "c_ontrol_lowest_high.mp4" },\
"overlay" : { \
    "image" : {"file" : "Control-lowest-high.png", "chromaColor" : "0x00FF00"}\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

#needs overlay
configs["episodes"].append(\
{ "title": "Control - high - GTX 970",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "01:57.9" ), "padAudio" : 0.1 },\
"video" : {"file" : "GTX970_Control_DX11_high.mp4", "start" : "00:00" },\
"overlay" : { \
    "image" : {"file" : "Control-high-results.png", "chromaColor" : "0x00FF00"}\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Control - high - R9 290X",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "02:18.2" ), "padAudio" : 0.1 },\
"video" : {"file" : "GTX970_Control_DX11_high.mp4", "start" : "00:08.3"  },\
"overlay" : { \
    "image" : {"file" : "Control-high-results.png", "chromaColor" : "0x00FF00"}\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Control - high - RX570",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "02:27.5" ), "padAudio" : 0.1 },\
"video" : {"file" : "GTX970_Control_DX11_high.mp4", "start" : "00:29.6"  },\
"overlay" : { \
    "image" : {"file" : "Control-high-results.png", "chromaColor" : "0x00FF00"}\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Control - medium settings",\
"audio" : {"timestamps" : (lastTS, "02:35.5" ), "padAudio" : 0.1 },\
"video" : {"file" : "c_ontrol_medium_high.mp4" },\
"overlay" : { \
    "image" : {"file" : "Control-medium-high.png", "chromaColor" : "0x00FF00"}\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Control - medium - all",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "03:12" ), "padAudio" : 0.1 },\
"video" : {"file" : "GTX970_Control_DX11_medium.mp4" , "start" : "00:30"},\
"overlay" : { \
    "image" : {"file" : "Control-medium-results.png", "chromaColor" : "0x00FF00"}\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Control - conclusion",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "03:20.7" ), "padAudio" : 0.1 },\
"video" : {"file" : "GTX970_Control_DX11_medium.mp4", "start" : "01:06.5" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Fallout 4 - ultra",\
"audio" : {"timestamps" : (lastTS, "03:30" ), "padAudio" : 0.1 },\
"video" : {"file" : "GTX970_Fallout4_2024_04_21_21_51_05_157.mp4", "start" : "00:01" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Fallout 4 - high vs medium",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "03:40.4" ), "padAudio" : 0.1 },\
"video" : {"file" : "F4_medium_high.mp4" },\
"overlay" : { \
    "image" : {"file" : "Fallout4-medium-high.png", "chromaColor" : "0x00FF00"}\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Fallout 4 - ultra results",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "04:12" ), "padAudio" : 0.1 },\
"video" : {"file" : "GTX970_Fallout4_2024_04_20_23_20_24_502.mp4", "start" : "00:00" },\
"overlay" : { \
    "image" : {"file" : "Fallout4-ultra.png", "chromaColor" : "0x00FF00"}\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Fallout 4 - high",\
"audio" : {"timestamps" : (lastTS, "04:35" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "GTX970_Fallout4_2024_04_20_23_20_24_502.mp4", "start" : "00:31.4" },\
"overlay" : { \
    "image" : {"file" : "Fallout4-high.png", "chromaColor" : "0x00FF00"}\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Fallout 4 - conclusion",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "04:51.5" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "GTX970_Fallout4_2024_04_20_23_20_24_502.mp4", "start" : "00:58.4" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "The exception to 30 FPS 1% lows",\
"audio" : {"timestamps" : (lastTS, "05:11.7" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "stock_DOOMEternal_2023_12_26.mp4", "start" : "03:19.8" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Doom Eternal - not higher than high",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "05:28" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "DOOMEternalx64vk_noyHigherThanHigh.mp4" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Doom Eternal - high",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "05:58.5" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "stock_DOOMEternal_2023_12_26.mp4", "start" : "04:00" },\
"overlay" : { \
    "image" : {"file" : "DoomEternal-high.png", "chromaColor" : "0x00FF00"}\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Doom Eternal - conclusions",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "06:10.3" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "stock_DOOMEternal_2023_12_26.mp4", "start" : "04:30.5" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

# average FPS
configs["episodes"].append(\
{ "title": "Conclusions",\
"audio" : {"timestamps" : (lastTS, "06:20.5" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "GTX970_Control_DX11_medium.mp4", "start" : "01:16" },\
"overlay" : { \
    "image" : {"file" : "sum-averages.png", "chromaColor" : "0x00FF00"}\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Conclusions one percent",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "06:30.2" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "stock_DOOMEternal_2023_12_26.mp4", "start" : "04:45" },\
"overlay" : { \
    "image" : {"file" : "sum-one-percent.png", "chromaColor" : "0x00FF00"}\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Other games",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "06:36.8" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "stock_FarCry6_benchmark.mp4" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Bye",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "06:45.5" ), "volume" : 0.999, "padAudio" : 0.1 },\
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