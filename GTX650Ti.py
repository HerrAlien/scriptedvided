import scriptedvided

configs = { "defaultAudioFile" : "GTX650Ti.ogg",\
"mediaFolder" : "F:\\Videos\\MSI_GTX650Ti", \
"stockFolder" : "F:\\Videos\\stock",\
"benchmarkFile" : "F:\\Videos\\MSI_GTX650Ti\\Benchmark_MSI_GTX650Ti.txt",\
"outputFolder" : "F:\\Videos\\MSI_GTX650Ti\\output", \
"outputFile" : "GTX650Ti.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#00800080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "50 Ti - cards that will not die", "until" : "Cyberpunk 2077"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Cyberpunk 2077", "until" : "Apex both cards"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Apex both cards", "until" : "Conclusions"}}, \
{"file" : "Inspired - MaikonMusic  Free Background Music  Audio Library Release.mp3", "timestamps" : ("00:00", None ), "destinationTimestamp" : {"title" : "Conclusions", "until" : "EOF"}}, \
], "volume" : 0.038 },\
"episodes" : [],\
"youtube" : {"title" : "", \
"description" : '''NVidia's GTX 650 Ti gets tested in 2025. But not on its own.''',\
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
"tags" : "Maxwell,GTX,GeForce,NVidia,650 Ti,GTX650Ti,GTX 650 Ti,MSI",\
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
#"video" : {"file" : " "},\
#})

configs["episodes"].append(\
{ "title": "50 Ti - cards that will not die",\
"audio" : {"timestamps" : ("00:00", "00:12.9" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_MSI_GTX650Ti.mp4"},\
})

# GPU-Z side by side
configs["episodes"].append(\
{ "title": "The GPU",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:25.5" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "MSI-GTX-650-Ti_GPUZ.mkv"},\
})

# GPU-Z side by side
configs["episodes"].append(\
{ "title": "The GPU - dx11",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:35.3" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Fortnite_Win_2025-04-21.mkv"},\
"isChapter" : False,\
})

# GPU-Z side by side
configs["episodes"].append(\
{ "title": "The GPU - counterparts",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:49.3" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "sideBySide_HD7790_R7_260.mp4"},\
"isChapter" : False,\
})

# GPU-Z side by side
configs["episodes"].append(\
{ "title": "The GPU - HD7770",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:57.8" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_MSI_GTX650Ti_HD7770.mp4"},\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Cooling and thermals",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:21.2" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_MSI_GTX650Ti.mp4"},\
"overlay" : { \
    "text" : ["'Temperatures (Valley)\: 57C (34C delta over ambient)'"]}, \
})

configs["episodes"].append(\
{ "title": "The test system",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:33" ), "volume" : 0.999, "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Custom build'",\
              "'CPU\: Ryzen 5 3600'",\
              "'RAM\: 32GB DDR4 at 3600 MHz, dual channel'",\
    ]\
}, \
"video" : {"file" : "test_system_RX580.mp4" }\
})

# GPU-Z side by side
configs["episodes"].append(\
{ "title": "Games failing to launch",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:47.3" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "MSI_GTX650Ti_VRM_barred.mp4"},\
"isChapter" : False,\
})


####################### end of intro ###############################


####################### gaming section ###############################

configs["episodes"].append(\
{ "title": "Cyberpunk 2077",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:02.8" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, lowest settings", \
    }\
}, \
})

#              scriptedvided.r6sText('Radeon HD 7770'      , , ),\
#              scriptedvided.r6sText('GeForce GTX 650 Ti'  , , ),\


configs["episodes"].append(\
{ "title": "CP2077 both cards",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:15.2" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Cyberpunk 2077, 1280x720, lowest settings'",\
              scriptedvided.r6sText('GeForce GTX 650 Ti'  , 17 , 10 ),\
              scriptedvided.r6sText('Radeon HD 7770'      , 20, 12),\
]}, \
"isChapter" : False,\
"video" : {"file" : "Cyberpunk2077_2025_04_06_23_01_24_280-converted.mp4" : "start" : "02:12"},\
})

configs["episodes"].append(\
{ "title": "Fortnite",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:37.6" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Fortnite, performance mode, FAR view distance'",\
              scriptedvided.r6sText('1920x1080' , 81, 65),\
              scriptedvided.r6sText('1600x900'  , 103 , 78),\
              scriptedvided.r6sText('1280x720'  , 132, 92),\
]}, \
})

configs["episodes"].append(\
{ "title": "Fortnite both cards",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:57.8" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Fortnite, performance mode, 1280x720'",\
              scriptedvided.r6sText('GeForce GTX 650 Ti, DX11'  , 132, 92 ),\
              scriptedvided.r6sText('GeForce GTX 650 Ti, DX12'  , 0, 0 ),\
              "",\
              scriptedvided.r6sText('Radeon HD 7770, DX11'      , 123, 98),\
              scriptedvided.r6sText('Radeon HD 7770, DX12'      , 98, 77),\
]}, \
"isChapter" : False,\
"video" : {"file" : "Fortnite_Win_2025-04-21.mkv"},\
})

configs["episodes"].append(\
{ "title": "Terminator: Resistance",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:17.6" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Terminator\: Resistance'",\
              scriptedvided.r6sText('1920x1080, low settings'    , 47, 36 ),\
              scriptedvided.r6sText('1920x1080, medium settings' , 38, 29),\
]}, \
})

configs["episodes"].append(\
{ "title": "Terminator both cards",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:29.3" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Terminator\: Resistance, 1920x1080, low settings'",\
              scriptedvided.r6sText('GeForce GTX 650 Ti'  ,47, 36 ),\
              scriptedvided.r6sText('Radeon HD 7770'      , 40, 30),\
]}, \
"video" : {"file" : "Terminator-Win64-Shipping_2024_07_20_08_16_41_274-converted.mp4", "start" : "02:12"},\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Counter-Strike 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:50.6" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Counter-Strike 2, low settings'",\
              scriptedvided.r6sText('1920x1080' , 67, 49),\
              scriptedvided.r6sText('1600x900'  , 78, 55),\
              scriptedvided.r6sText('1280x720'  , 95, 66),\
]}, \
})

configs["episodes"].append(\
{ "title": "CS2 both cards",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:59.8" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Counter-Strike 2, 1280x720, low settings'",\
              scriptedvided.r6sText('GeForce GTX 650 Ti'  , 95, 66 ),\
              scriptedvided.r6sText('Radeon HD 7770'      , 90, 71),\
]}, \
"video" : {"file" : "stock_CS2_CT_R7_260X.mp4"},\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Doom Eternal",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:14" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Doom both cards",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:24.4" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Doom Eternal, 1280x720, low settings'",\
              scriptedvided.r6sText('GeForce GTX 650 Ti'  , 23, 14),\
              scriptedvided.r6sText('Radeon HD 7770'      , 42, 29),\
]}, \
"isChapter" : False,\
"video" : {"file" : "stock_DOOMEternal_2023_12_26.mp4", "start" : "02:03"},\
})

configs["episodes"].append(\
{ "title": "Rainbow Six: Siege",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:44.1" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Rainbow Six: Siege, 1280x720, 50% scale, low settings'",\
              scriptedvided.r6sText('GeForce GTX 650 Ti'  , 0, 0),\
              scriptedvided.r6sText('Radeon HD 7770'      , 48, 26),\
]}, \
})

configs["episodes"].append(\
{ "title": "Control",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs),  "05:08.1" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Control, 1280x720, low settings'",\
              scriptedvided.r6sText('GeForce GTX 650 Ti'  , 30, 23),\
              scriptedvided.r6sText('Radeon HD 7770'      , 35, 16),\
]}, \
})

configs["episodes"].append(\
{ "title": "Overwatch 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:25.4" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Overwatch 2, low settings'",\
              scriptedvided.r6sText('1920x1080' , 86, 70),\
              scriptedvided.r6sText('1600x900'  , 117, 97),\
              scriptedvided.r6sText('1280x720'  , 167, 139),\
]}, \
})

configs["episodes"].append(\
{ "title": "Overwatch 2 both cards",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:37.4" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Overwatch 2, 1280x720, low settings'",\
              scriptedvided.r6sText('GeForce GTX 650 Ti'  , 167, 139 ),\
              scriptedvided.r6sText('Radeon HD 7770'      , 145, 115),\
]}, \
"isChapter" : False,\
"video" : {"file" : "stock_Overwatch2_gameplay.mp4", "start" : "01:50"},\
})

configs["episodes"].append(\
{ "title": "DOTA2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:56.4" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Shadow of the Tomb Raider",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:14.8" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, lowest settings", \
    }\
}, \
"video" : {"file" : "SOTTR_gaming_highest.mp4"}\
})

configs["episodes"].append(\
{ "title": "SOTTR both cards",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:23" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Shadow of the Tomb Raider, 1280x720, lowest settings'",\
              scriptedvided.r6sText('GeForce GTX 650 Ti'  , 38, 25),\
              scriptedvided.r6sText('Radeon HD 7770'      , 49, 35),\
]}, \
"isChapter" : False,\
"video" : {"file" : "SOTTR_gaming_highest.mp4"}\
})

configs["episodes"].append(\
{ "title": "Borderlands 3",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:39.9" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Borderlands 3, very low settings'",\
              scriptedvided.r6sText('1600x900' , 40, 32),\
              scriptedvided.r6sText('1280x720' , 51, 35),\
]}, \
})

configs["episodes"].append(\
{ "title": "BL3 both cards",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:49.1" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Borderlands 3, 1280x720, very low settings'",\
              scriptedvided.r6sText('GeForce GTX 650 Ti'  ,51, 35 ),\
              scriptedvided.r6sText('Radeon HD 7770'      , 46, 36),\
]}, \
"isChapter" : False,\
"video" : {"file" : "Borderlands3_2024_05_03_22_58_15_076.mp4"},\
})


####################### end of gaming section ###############################

####################### conclusion ###############################
#
configs["episodes"].append(\
{ "title": "Conclusions",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:03.7" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_MSI_GTX650Ti.mp4"},\
})

configs["episodes"].append(\
{ "title": "Some games will not run",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:14.07" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "stock_RainbowSixSiege_benchmark3.mp4"},\
})

configs["episodes"].append(\
{ "title": "TTO",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:15.55" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "stock_RainbowSixSiege_benchmark3.mp4"},\
})

configs["episodes"].append(\
{ "title": "Pricing",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:36.8" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GTX650Ti_OLX.mkv"},\
})

configs["episodes"].append(\
{ "title": "bye",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:56" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_MSI_GTX650Ti.mp4"},\
})


##configs["episodes"].append(\
##{ "title": "Blooper",\
##"isChapter" : False,\
##"audio" : {"timestamps" : ( "13:40.5", "14:04.2") },\
##"video" : {"file" : " "}\
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