import scriptedvided

configs = { "defaultAudioFile" : "GTX960_2GB.ogg",\
"mediaFolder" : "F:\\Videos\\...", \
"stockFolder" : "F:\\Videos\\stock",\
"benchmarkFile" : "F:\\Videos\\...\\....txt",\
"outputFolder" : "F:\\Videos\\...\\output", \
"outputFile" : "GTX960_2GB.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "An old aquaintance", "until" : "Marvel Rivals"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Marvel Rivals", "until" : "Apex both cards"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Apex both cards", "until" : "Conclusions"}}, \
{"file" : "Inspired - MaikonMusic  Free Background Music  Audio Library Release.mp3", "timestamps" : ("00:00", None ), "destinationTimestamp" : {"title" : "Conclusions", "until" : "EOF"}}, \
], "volume" : 0.05 },\
"episodes" : [],\
"youtube" : {"title" : "", \
"description" : '''In this one we re-visit the former mining superstar, AMD's RX 580.''',\
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
"tags" : "Maxwell,GTX,GeForce,NVidia,960,GTX960,GTX 960",\
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
#  scriptedvided.r6sText\('.*' *\, *[0-9]*\, *[0-9]*\)
#   "timestamps" *\: *\( *"[0-9\:\.]*" *\, *"[0-9\:\.]*" *\)
#configs["episodes"].append(\
#{ "title": "A favorite of miners and gamers alike",\
#"audio" : {"timestamps" : (scriptedvided.nextTS(configs),  "" ), "volume" : 0.999, "padAudio" : 0.05 },\
#"video" : {"file" : ""},\
#})

configs["episodes"].append(\
{ "title": "An old aquaintance",\
"audio" : {"timestamps" : ("00:00", "00:07.2" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "All 3 960s",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:23.1" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
"isChapter" : False,\
})

# GPU-Z side by side
configs["episodes"].append(\
{ "title": "The GPU",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:34.6" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "Cooling and thermals",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:59" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
"overlay" : { \
    "text" : ["'Temperatures (Heaven)\: 78C (54C delta over ambient)'"]}, \
})

configs["episodes"].append(\
{ "title": "The test system",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:09.2" ), "volume" : 0.999, "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Custom build'",\
              "'CPU\: Ryzen 5 3600'",\
              "'RAM\: 32GB DDR4 at 3600 MHz, dual channel'",\
    ]\
}, \
"video" : {"file" : ""}\
})

####################### end of intro ###############################


####################### gaming section ###############################
configs["episodes"].append(\
{ "title": "Marvel Rivals",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:26.9" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, lowest settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Cyberpunk 2077",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:01" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Cyberpunk 2077'",\
              scriptedvided.r6sText('1280x720, low settings, no FSR' , 44, 30),\
              scriptedvided.r6sText('1920x1080, low settings, FSR balanced' ,40, 28),\
]}, \
})

configs["episodes"].append(\
{ "title": "CP2077 both cards",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:09.3" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : "Cyberpunk 2077, 1080p, low settings, FSR balanced.png"}\
}, \
"isChapter" : False,\
"video" : {"file" : ""},
})

configs["episodes"].append(\
{ "title": "The Finals",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:21.7" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
}, \
"video" : "Discovery_2025_03_15_22_55_07_819.mp4"\
})

configs["episodes"].append(\
{ "title": "The Finals both cards",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:31.7" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : "The Finals, 1280x720, low settings.png"}\
}, \
"isChapter" : False,\
"video" : {"file" : ""},
})


configs["episodes"].append(\
{ "title": "Robocop",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:45.8" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Robocop both cards",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:56" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : "Robocop, 1280x720, low settings.png"}\
}, \
"isChapter" : False,\
"video" : {"file" : ""},
})

configs["episodes"].append(\
{ "title": "Fortnite",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:20.9" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Fortnite'",\
              scriptedvided.r6sText('1920x1080, performance mode, FAR view distance' , 174, 119),\
              scriptedvided.r6sText('1600x900, performance mode, FAR view distance'  , 209, 130),\
              scriptedvided.r6sText('1280x720, performance mode, FAR view distance'  , 245, 128),\
]}, \
})

configs["episodes"].append(\
{ "title": "Terminator: Resistance",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:36.1" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, epic settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Terminator both cards",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:45.6" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : "Terminator, 1920x1080, epic settings.png"}\
}, \
"isChapter" : False,\
"video" : {"file" : ""},
})

configs["episodes"].append(\
{ "title": "Counter-Strike 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:10.2" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Counter-Strike 2'",\
              scriptedvided.r6sText('1920x1080, low settings', 171, 95),\
              scriptedvided.r6sText('1600x900, low settings' , 185, 95),\
              scriptedvided.r6sText('1280x720, low settings' , 198, 100),\
]}, \
})

configs["episodes"].append(\
{ "title": "Far Cry 6",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:25.1" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Far Cry 6'",\
              scriptedvided.r6sText('1920x1080, low settings'   , 40, 34),\
              scriptedvided.r6sText('1600x900, medium settings' , 37, 32),\
              scriptedvided.r6sText('1280x720, high settings'   ,41, 34),\
]}, \
})

configs["episodes"].append(\
{ "title": "fc6 both cards",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:39" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : "Far Cry 6, 1920x1080, low settings.png"}\
}, \
"isChapter" : False,\
"video" : {"file" : ""},
})

configs["episodes"].append(\
{ "title": "Apex Legends",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:02.9" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Apex Legends'",\
              scriptedvided.r6sText('1920x1080, low settings', 99, 71),\
              scriptedvided.r6sText('1600x900, low settings' , 122, 90),\
              scriptedvided.r6sText('1280x720, low settings' , 158, 106),\
]}, \
})

configs["episodes"].append(\
{ "title": "Apex both cards",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:17.4" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : "Apex Legends, 1920x1080, low settings.png"}\
}, \
"isChapter" : False,\
"video" : {"file" : ""},
})

configs["episodes"].append(\
{ "title": "Doom Eternal",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:39.4" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Doom Eternal'",\
              scriptedvided.r6sText('1920x1080, low settings', 57, 43),\
              scriptedvided.r6sText('1600x900, low settings' , 69, 52),\
              scriptedvided.r6sText('1280x720, low settings' , 90, 63),\
]}, \
})

configs["episodes"].append(\
{ "title": "Doom both cards",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:52.3" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : "Doom Eternal, 1920x1080, low settings.png"}\
}, \
"isChapter" : False,\
"video" : {"file" : ""},
})


configs["episodes"].append(\
{ "title": "Rainbow Six: Siege",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:23.1" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Rainbow Six\: Siege'",\
              scriptedvided.r6sText('1920x1080, low settings, 100% render scale', 56, 43),\
              scriptedvided.r6sText('1280x720, low settings, 100% render scale' , 112, 78),\
              scriptedvided.r6sText('1920x1080, low settings, 50% render scale' , 92, 68),\
              scriptedvided.r6sText('1280x720, low settings, 50% render scale'  , 158, 106),\
]}, \
})

configs["episodes"].append(\
{ "title": "Overwatch 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:43" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Overwatch 2'",\
              scriptedvided.r6sText('1920x1080, low settings', 176, 146),\
              scriptedvided.r6sText('1600x900, low settings' , 232, 195),\
              scriptedvided.r6sText('1280x720, low settings' , 334, 278),\
]}, \
})

configs["episodes"].append(\
{ "title": "Overwatch 2 both cards",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:55.5" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : "Overwatch 2, 1920x1080, low settings.png"}\
}, \
"isChapter" : False,\
"video" : {"file" : ""},
})

configs["episodes"].append(\
{ "title": "Resident Evil 4 (Remake)", \
"video" : "stock_re4demo_phoneCall.mp4", \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:19" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Resident Evil 4 \(Remake\)'",\
              scriptedvided.r6sText('1600x900, low settings' , 43, 29),\
              scriptedvided.r6sText('1280x720, low settings' , 58, 35),\
]}, \
})

configs["episodes"].append(\
{ "title": "RE4 both cards",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:30.5" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : "Resident Evil 4, 1280x720, prioritize performance, no FSR.png"}\
}, \
"isChapter" : False,\
"video" : {"file" : ""},
})

configs["episodes"].append(\
{ "title": "DOTA2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:45" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Shadow of the Tomb Raider",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:59.8" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Shadow of the Tomb Raider'",\
              scriptedvided.r6sText('1920x1080, high settings'  , 38, 27),\
              scriptedvided.r6sText('1920x1080, medium settings', 40, 28),\
]}, \
"video" : {"file" : ""}\
})

configs["episodes"].append(\
{ "title": "SOTTR both cards",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:13.7" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : "Shadow of the Tomb Raider, 1920x1080, medium settings.png"}\
}, \
"isChapter" : False,\
"video" : {"file" : ""},
})

configs["episodes"].append(\
{ "title": "Borderlands 3",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:37.8" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Borderlands 3'",\
              scriptedvided.r6sText('1920x1080, very low settings' , 69, 57),\
              scriptedvided.r6sText('1920x1080, medium settings'   , 45, 37),\
              scriptedvided.r6sText('1600x900, high settings'      , 36, 29),\
]}, \
})

configs["episodes"].append(\
{ "title": "BL3 both cards",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:47.4" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : "Borderlands 3, 1920x1080, medium settings.png"}\
}, \
"isChapter" : False,\
"video" : {"file" : ""},
})


####################### end of gaming section ###############################

####################### conclusion ###############################
#
configs["episodes"].append(\
{ "title": "Conclusions",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:58.1" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "Fine for esports",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "09:10.4" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "Pricing",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "09:21.9" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "Pricing 4G",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "09:29.7" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "1050 TI",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "09:44.4" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "Support ending",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "09:59.7" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "bye",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "10:08.3" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})


##configs["episodes"].append(\
##{ "title": "Blooper",\
##"isChapter" : False,\
##"audio" : {"timestamps" : ( "13:40.5", "14:04.2") },\
##"video" : {"file" : ""}\
##})

#scriptedvided.makeVideoForEpisode(configs["episodes"][2], configs)
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

#for x in range(2,28):
#    scriptedvided.makeVideoForEpisode(configs["episodes"][x], configs)

scriptedvided.makeVideo(configs)