import scriptedvided

configs = { "defaultAudioFile" : "Lethal Company AMD.ogg",\
"mediaFolder" : "F:\\Videos\\Lethal Company AMD", \
"stockFolder" : "F:\\Videos\\stock",\
"outputFolder" : "F:\\Videos\\Lethal Company AMD\\output", \
"outputFile" : "Lethal Company AMD.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#08000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "Coop Horror", "until" : "1920x1080 results"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "1920x1080 results", "until" : "CPU can be 5 generations older"}}, \
{"file" : "Inspired - MaikonMusic  Free Background Music  Audio Library Release.mp3", "timestamps" : ("00:00", None ), "destinationTimestamp" : {"title" : "CPU can be 5 generations older", "until" : "EOF"}}, \
], "volume" : 0.06 },\
"episodes" : [],\
"youtube" : {"title" : "Lethal Company under the minimum requirements", \
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
"tags" : "Lethal Company,Radeon,AMD,HD 6670,HD6670,HD7750,HD 7750,R7 250,RX460,RX 460,GCN,Polaris,TeraScale 2",\
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
{ "title": "Coop Horror",\
"audio" : {"timestamps" : (lastTS, "00:12.2" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "stock_Lethal Company_2024_03_10_3.mp4"},\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]


configs["episodes"].append(\
{ "title": "Requirements look sus",\
"audio" : {"timestamps" : (lastTS, "00:21.6" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "original_requirements.mp4", "start" : "00:05" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "4 GPUs weaker than required",\
"audio" : {"timestamps" : (lastTS, "00:29" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "merged.mp4"},\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]


configs["episodes"].append(\
{ "title": "HD6670",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "00:36.2" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "broll_hd6670_horizontal.mp4"},\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]


configs["episodes"].append(\
{ "title": "R7 250",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "00:42.7" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "r7_250_broll_boxLandscape.mp4"},\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]


configs["episodes"].append(\
{ "title": "HD7750",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "00:49.7" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "breel_hd7750_outside.mp4"},\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "RX 460",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "00:55.5" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "breel_rx460_outside.mp4"},\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "2 CPUs also under minimum specs",\
"audio" : {"timestamps" : (lastTS, "01:09" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "breel_SandyBridge_outside.mp4"},\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]


configs["episodes"].append(\
{ "title": "Game settings",\
"audio" : {"timestamps" : (lastTS, "01:20.8" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "stock_Lethal Company_2024_03_10.mp4"},\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "resolution trick, start",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "01:24.2" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "desktop_resolution.mp4"},\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "resolution trick, end",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "01:28.4" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "video modes.mkv", "start" : "00:10"},\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "RTSS overlay",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "01:36.7" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "L_ethal Company_GT1030.mp4"},\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]


configs["episodes"].append(\
{ "title": "1920x1080 results",\
"audio" : {"timestamps" : (lastTS, "01:54.5" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "Lethal Company_2024_03_09_22_25_45_404-converted.mp4"},\
"overlay" : { \
    "image" : {"file" : "1920x1080.png", "chromaColor" : "0x00FF00"}\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "TS2 no go",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "02:16.8" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "L_ethal Company - HD 6670.mp4"},\
"overlay" : { \
    "image" : {"file" : "1920x1080.png", "chromaColor" : "0x00FF00"}\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "1080 RX 460",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "02:32" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "Lethal Company_2024_03_09_22_25_45_404-converted.mp4"},\
"overlay" : { \
    "image" : {"file" : "1920x1080.png", "chromaColor" : "0x00FF00"}\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]


configs["episodes"].append(\
{ "title": "1600x900 results",\
"audio" : {"timestamps" : (lastTS, "03:09.5" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "Lethal Company_2024_03_09_22_22_06_104-converted.mp4"},\
"overlay" : { \
    "image" : {"file" : "1600x900.png", "chromaColor" : "0x00FF00"}\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "1280x720 results",\
"audio" : {"timestamps" : (lastTS, "03:40.6" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "stock_Lethal Company_2024_03_10_2.mp4"},\
"overlay" : { \
    "image" : {"file" : "1280x720.png", "chromaColor" : "0x00FF00"}\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "CPU can be 5 generations older",\
"audio" : {"timestamps" : (lastTS, "04:03.1" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "breel_SandyBridge_slomo_outside.mp4"},\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "More realistic requirements",\
"audio" : {"timestamps" : (lastTS, "04:31.4" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "fixed_requirements.mp4"},\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

# prepare a chart with all resolutions for one card.
configs["episodes"].append(\
{ "title": "resolution behavior",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "04:54.6" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "stock_Lethal Company_2024_03_10_2.mp4"},\
"overlay" : { \
    "image" : {"file" : "rx460_overlay.png", "chromaColor" : "0x00FF00"}\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]


# overlay with press 'F' to pay respects
configs["episodes"].append(\
{ "title": "TeraScale 2 - not usable",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "05:08.9" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "broll_hd6670_horizontal.mp4"},\
"overlay" : { \
    "image" : {"file" : "pay respects.png", "chromaColor" : "0x00FF00"}\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "NVidia",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "05:23" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "breel_autumn_GT1030_KFA2.mp4"},\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "bye",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "05:29.5" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "L_ethal Company_GT1030.mp4"},\
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