import scriptedvided

configs = { "defaultAudioFile" : "R5_2400G.ogg",\
"mediaFolder" : "F:\\Videos\\R5_2400G", \
"stockFolder" : "F:\\Videos\\stock",\
"benchmarkFile" : "F:\\Videos\\R5_2400G\\Benchmark_R5_2400G_cpu.txt",\
"outputFolder" : "F:\\Videos\\R5_2400G\\output", \
"outputFile" : "R5_2400G.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "First gen Ryzen quad core, really?", "until" : "Marvel Rivals"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Marvel Rivals", "until" : "Overwatch 2"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Overwatch 2", "until" : "Video rendering test (The GigASUS)"}}, \
{"file" : "Ferco - Inquisitiveness.ogg", "timestamps" : ("01:01", None ), "destinationTimestamp" : {"title" : "Video rendering test (The GigASUS)", "until" : "Conclusions"}}, \
{"file" : "Inspired - MaikonMusic  Free Background Music  Audio Library Release.mp3", "timestamps" : ("00:00", None ), "destinationTimestamp" : {"title" : "Conclusions", "until" : "EOF"}}, \
], "volume" : 0.038 },\
"episodes" : [],\
"youtube" : {"title" : "", \
"description" : '''''',\
"links" : '''
Track: Bliss Of Heaven - SOMM [Audio Library Release]
Music provided by Audio Library Plus
Watch: https://www.youtube.com/watch?v=JQ6mKeQLZak&t=0s
Free Download / Stream: https://alplus.io/blisss-heaven

Track: Far Far Away - Ferco [Audio Library Release]
Music provided by Audio Library Plus
Watch: https://www.youtube.com/watch?v=SrkQ3K1umlc&t=0s 
Free Download / Stream: https://alplus.io/far-far-away

Track: Ferco - Inquisitiveness
Creative Commons - Attribution 3.0 Unported (CC BY 3.0)
Free Download: https://hypeddit.com/mlsvxq
Streams: https://share.amuse.io/track/ferco-inquisitiveness
Video: https://www.youtube.com/watch?v=dhJdmwLWtFM&t=0s


Track: Inspired - MaikonMusic [Audio Library Release]
Music provided by Audio Library Plus
Watch: https://www.youtube.com/watch?v=RUkdTkk_52o&t=0s
Free Download / Stream: https://alplus.io/inspired

''', \
"tags" : "",\
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

#"isChapter" : False, \

####################### intro ###############################

# this is the hook 
#  scriptedvided.nextTS\(configs\)\, *\"[0-9][0-9]\:[0-9][0-9]\.?[0-9]?[0-9]?\"
#  \"file\" *\: *\".*\"
#  \"video\" *: *\{\"file\" *: *\".* \"\}
#  scriptedvided.r6sText\('.*' *\, *[0-9]*\, *[0-9]*\)
#   "timestamps" *\: *\( *"[0-9\:\.]*" *\, *"[0-9\:\.]*" *\)
#configs["episodes"].append(\
#{ "title": "A favorite of miners and gamers alike",\
#"audio" : {"timestamps" : (scriptedvided.nextTS(configs),  "" ), "volume" : 0.999, "padAudio" : 0.05 },\
#"video" : {"file" : " "},\
#})

configs["episodes"].append(\
{ "title": "One of the first AM4 APUs",\
"audio" : {"timestamps" : ("00:00", "00:14.7"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : " "},\
})

# focus on PCIE lanes
configs["episodes"].append(\
{ "title": "4600G",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:22.7" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : " "},\
})

# focus on PCIE lanes
configs["episodes"].append(\
{ "title": "The CPU",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:34.4" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : " "},\
})

# focus on PCIE lanes
configs["episodes"].append(\
{ "title": "L3 cache",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:42.8" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : " "},\
})

# focus on PCIE lanes
configs["episodes"].append(\
{ "title": "PCIE lanes",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:54.8" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : " "},\
})

# focus on PCIE lanes
configs["episodes"].append(\
{ "title": "What actually gets benchmarked",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:03" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : " "},\
})

# focus on PCIE lanes
configs["episodes"].append(\
{ "title": "sample benchmark",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:13" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : " "},\
})

configs["episodes"].append(\
{ "title": "The test system",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:26.7" ), "volume" : 0.999, "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Custom PC'",\
              "'CPU\: Ryzen 5 1500X'",\
              "'RAM\: 32GB DDR4, 2933MHz, dual channel'",\
              "'GPU\: Radeon RX 580'",\
    ]\
}, \
"video" : {"file" : " "},\
})

configs["episodes"].append(\
{ "title": "RX 580 broll",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:40.8" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : " "},\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "IGPU test settings broll",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:50.9" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : " "},\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "will have gigasus",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:02.3" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : " "},\
"isChapter" : False,\
})


####################### end of intro ###############################


####################### gaming section ###############################
configs["episodes"].append(\
{ "title": "Marvel Rivals",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:24.2" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, 30% render scale, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Marvel all",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:37.5" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, 30% render scale, low settings", \
    }\
}, \
"isChapter" : False,\
"overlay" : { "image" : {"file" : "Marvel Rivals.png"} }, \
"video" : {"file" : " "}\
})

# needs redone
configs["episodes"].append(\
{ "title": "Cyberpunk 2077",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:04" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1024x768, performance FSR, lowest settings", \
    }\
}, \
})

# needs redone
configs["episodes"].append(\
{ "title": "Cyberpunk 2077 all",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:12.8" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1024x768, performance FSR, lowest settings", \
    }\
}, \
"isChapter" : False,\
"overlay" : { "image" : {"file" : "Cyberpunk 2077.png"} }, \
"video" : {"file" : " "}\
})

configs["episodes"].append(\
{ "title": "ARC Raiders",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:38.3" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, 50% render scale, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "ARC Raiders all",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:47.2" ), "padAudio" : 0.05 },\
"video" : {"file" : " "},\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, 50% render scale, low settings", \
    }\
}, \
"isChapter" : False,\
"overlay" : { "image" : {"file" : "ARC Raiders.png"} }, \
"video" : {"file" : " "}\
})

configs["episodes"].append(\
{ "title": "Fortnite",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:10" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, 50% render scale, performance mode", \
    }\
}, \
"video" : {"file" : " "}\
})

configs["episodes"].append(\
{ "title": "Fortnite all",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:25.3" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, 50% render scale, performance mode", \
    }\
}, \
"video" : {"file" : " "}\
"isChapter" : False,\
"overlay" : { "image" : {"file" : "Fortnite.png"} }, \
})

configs["episodes"].append(\
{ "title": "Control",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:51.1" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "960x540, lowest settings", \
    }\
},\
})

configs["episodes"].append(\
{ "title": "Control all",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:00.3" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "960x540, lowest settings", \
    }\
},\
"video" : {"file" : " "},\
"isChapter" : False,\
"overlay" : { "image" : {"file" : "Control.png"} }, \
})

configs["episodes"].append(\
{ "title": "Rainbow Six: Siege",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:18.6"), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1024x768, 50% scale, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Rainbow Six: Siege all",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:30.1"), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1024x768, 50% scale, low settings", \
    }\
}, \
"isChapter" : False,\
"overlay" : { "image" : {"file" : "Rainbow 6_ Siege.png"} }, \
"video" : {"file" : " "}\
})

# single resolution
configs["episodes"].append(\
{ "title": "Doom Eternal",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:48.7" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "800x600, low settings", \
    }\
}\
})

# single resolution
configs["episodes"].append(\
{ "title": "Doom Eternal all",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:06.1" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "800x600, low settings", \
    }\
}\
"isChapter" : False,\
"overlay" : { "image" : {"file" : "Doom Eternal.png"} }, \
"video" : {"file" : " "}\
})

configs["episodes"].append(\
{ "title": "Apex Legends",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:29" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
},
})

configs["episodes"].append(\
{ "title": "Apex Legends all",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:39.8" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
},
"isChapter" : False,\
"overlay" : { "image" : {"file" : "Apex Legends.png"} }, \
"video" : {"file" : " "}\
})

configs["episodes"].append(\
{ "title": "Far Cry 6",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:02.9" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, 50% render scale, low settings", \
    }\
}\
})

configs["episodes"].append(\
{ "title": "Far Cry 6 all",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:14.9" ), "padAudio" : 0.05 },\
"video" : {"file" : " "},\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, 50% render scale, low settings", \
    }\
}\
"isChapter" : False,\
"overlay" : { "image" : {"file" : "Far Cry 6.png"} }, \
"video" : {"file" : " "}\
})

configs["episodes"].append(\
{ "title": "Overwatch 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:44.9" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, 50% render scale, low settings", \
    }\
}\
})

configs["episodes"].append(\
{ "title": "Overwatch 2 all",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:54.9" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, 50% render scale, low settings", \
    }\
}\
"isChapter" : False,\
"overlay" : { "image" : {"file" : "Overwatch 2.png"} }, \
"video" : {"file" : " "}\
})

configs["episodes"].append(\
{ "title": "RE4",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:24.1" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "800x600, performance FSR, low settings", \
    }\
}\
})

configs["episodes"].append(\
{ "title": "RE4 all",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:39.9" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "800x600, performance FSR, low settings", \
    }\
}\
"isChapter" : False,\
"overlay" : { "image" : {"file" : "Overwatch 2.png"} }, \
"video" : {"file" : " "}\
})

configs["episodes"].append(\
{ "title": "Counter-Strike 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:59.9" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, balanced FSR, low settings", \
    }\
}\
})

configs["episodes"].append(\
{ "title": "Counter-Strike 2 all",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "09:11.8" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, balanced FSR, low settings", \
    }\
}\
"isChapter" : False,\
"overlay" : { "image" : {"file" : "Counter-Strike 2.png"} }, \
"video" : {"file" : " "}\
})

configs["episodes"].append(\
{ "title": "Borderlands 3",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "09:32.9" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, 50% render scale, very low settings", \
    }\
},\
})

configs["episodes"].append(\
{ "title": "Borderlands 3 all",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "09:49.4" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, 50% render scale, very low settings", \
    }\
},\
"isChapter" : False,\
"overlay" : { "image" : {"file" : "Borderlands 3.png"} }, \
"video" : {"file" : " "}\
})

configs["episodes"].append(\
{ "title": "DOTA 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "10:08.5" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
},\
"video" : "stock_dota2_1080pLow_scale100.mp4"\
})

configs["episodes"].append(\
{ "title": "DOTA 2 all",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "10:19.6" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
},\
"video" : "stock_dota2_1080pLow_scale100.mp4"\
"isChapter" : False,\
"overlay" : { "image" : {"file" : "DOTA2.png"} }, \
})

configs["episodes"].append(\
{ "title": "The Finals",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "10:42.4" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, 50% scale, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "The Finals all",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "10:56.1" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, 50% scale, low settings", \
    }\
}, \
"isChapter" : False,\
"overlay" : { "image" : {"file" : "The Finals.png"} }, \
"video" : {"file" : " "}\
})

#redo and specify a smoother video
configs["episodes"].append(\
{ "title": "Shadow of the Tomb Raider",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "11:17.2" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "800x600, lowest settings", \
    }\
},\
})

#redo and specify a smoother video
configs["episodes"].append(\
{ "title": "Shadow of the Tomb Raider all",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "11:32.9" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "800x600, lowest settings", \
    }\
},\
"isChapter" : False,\
"overlay" : { "image" : {"file" : "Shadow of the Tomb Raider.png"} }, \
"video" : {"file" : " "}\
})

#redo and specify a smoother video
configs["episodes"].append(\
{ "title": "Terminator",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "11:49.6" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x1024, 50% scale, low settings", \
    }\
},\
})

#redo and specify a smoother video
configs["episodes"].append(\
{ "title": "Terminator all",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "12:00.5" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x1024, 50% scale, low settings", \
    }\
},\
"isChapter" : False,\
"overlay" : { "image" : {"file" : "Terminator_ Resistance.png"} }, \
"video" : {"file" : " "}\
})

####################### end of gaming section ###############################


############################ productivity #################################

# this is both time and cycles, for both SMT on and off
configs["episodes"].append(\
{ "title": "Video rendering test (The GigASUS)",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "12:19.2" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : " "},\
})

configs["episodes"].append(\
{ "title": "By itself",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "12:32.3" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : " "},\
"isChapter" : False,\
"overlay" : { \
    "image" : {"file" : "overlays.png"}\
}, \
})

configs["episodes"].append(\
{ "title": "Compared with others",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "12:45.3" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : " "},\
"isChapter" : False,\
"overlay" : { \
    "image" : {"file" : "ipc_w_others.png"}\
}, \
})

#############################################################################



####################### conclusion ###############################
# happy that it works
configs["episodes"].append(\
{ "title": "Conclusions",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "13:03.2" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : " "},\
})

configs["episodes"].append(\
{ "title": "side by side with the 1500X",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "13:13.5" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : " "},\
})

configs["episodes"].append(\
{ "title": "not the best stopgap",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "13:33" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : " "},\
})

configs["episodes"].append(\
{ "title": "2400G and 4600G together or APU vs CPU and GPU",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "13:44.6" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : " "},\
})

configs["episodes"].append(\
{ "title": "bye",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "13:53.3" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : " "},\
})


##configs["episodes"].append(\
##{ "title": "Blooper",\
##"isChapter" : False,\
##"audio" : {"timestamps" : (scriptedvided.nextTS(configs),  "" ) },\
##"video" : {"file" : " "}\
##})

#scriptedvided.makeVideoForEpisode(configs["episodes"][8], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][9], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][13], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][15], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][16], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][17], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][18], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][19], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][21], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][22], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][24], configs)
#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "Borderlands 3"][0], configs)
#scriptedvided.makeVideo(configs)

#for x in range(19,26):
#    scriptedvided.makeVideoForEpisode(configs["episodes"][x], configs)
#
scriptedvided.makeVideo(configs)

