import scriptedvided

configs = { "defaultAudioFile" : "HD7790.ogg",\
"mediaFolder" : "F:\\Videos\\HD7790", \
"stockFolder" : "F:\\Videos\\stock",\
"benchmarkFile" : "F:\\Videos\\HD7790\\Benchmark_HD7790.txt",\
"outputFolder" : "F:\\Videos\\HD7790\\output", \
"outputFile" : "HD7790.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "One interesting card", "until" : "Marvel Rivals"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Marvel Rivals", "until" : "Rainbow Six: Siege"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Rainbow Six: Siege", "until" : "Conclusions"}}, \
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
"tags" : "GCN,GCN 2,GCN 2.0,AMD,Radeon,HD7790,HD 7790,R7 260X",\
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
{ "title": "One interesting card",\
"audio" : {"timestamps" : ("00:00", "00:20.1" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "barred_breel_HD7790.mp4"},\
})

# GPU-Z side by side
configs["episodes"].append(\
{ "title": "The GPU",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:40.3" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "HD7790_GPUZ_ValleyAndHeaven.mkv"},\
})

configs["episodes"].append(\
{ "title": "GPU-Z Just 21_5_1 driver",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:49.6" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "HD7790_GpuZ_Heaven.mkv"},\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "side by side with 260X",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:04.2" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_HD7790_260X.mp4"},\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "260X alone",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:08.6" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "r7_260x_breel_outside.mp4"},\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Cooling and thermals",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:22.7" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "barred_breel_HD7790_v3.mp4"},\
})

# same video as for cooling
configs["episodes"].append(\
{ "title": "Temps",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:29.9" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "barred_breel_HD7790_v3.mp4"},\
"isChapter" : False,\
"overlay" : { \
    "text" : ["'Temperatures (Heaven)\: 63C (38C delta over ambient)'"]}, \
})

configs["episodes"].append(\
{ "title": "The test system",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:47.2" ), "volume" : 0.999, "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Custom build'",\
              "'CPU\: Ryzen 5 3600'",\
              "'RAM\: 32GB DDR4 at 3000 MHz, dual channel'",\
    ]\
}, \
"video" : {"file" : "test_system_RX580.mp4" }\
})

####################### end of intro ###############################


####################### gaming section ###############################
configs["episodes"].append(\
{ "title": "Marvel Rivals",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:06.4" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Marvel Rivals'",\
              "... needs more than 1GB of VRAM ",\
]}, \
})

configs["episodes"].append(\
{ "title": "Cyberpunk 2077",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:30.6" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, lowest settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "The Finals",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:47.6" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
}, \
"video" : "Discovery_2025_03_15_22_55_07_819.mp4"\
})

configs["episodes"].append(\
{ "title": "Robocop",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:59.8" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Robocop'",\
              "... needs more than feature level 12_0 ",\
]}, \
})

configs["episodes"].append(\
{ "title": "Fortnite",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:22.6" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Fortnite'",\
              scriptedvided.r6sText('1920x1080, performance mode' , 99, 75),\
              scriptedvided.r6sText('1600x900, performance mode'  , 125, 92),\
              scriptedvided.r6sText('1280x720, performance mode'  , 159, 112),\
]}, \
})

configs["episodes"].append(\
{ "title": "Terminator: Resistance",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:41.3" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, medium settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Counter-Strike 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:04.85" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Counter-Strike 2'",\
              scriptedvided.r6sText('1920x1080, low settings' , 88, 72),\
              scriptedvided.r6sText('1600x900, low settings'  , 98, 83),\
              scriptedvided.r6sText('1280x720, low settings'  , 133, 102),\
]}, \
})

configs["episodes"].append(\
{ "title": "Far Cry 6",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:22.15" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, lowest settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Apex Legends",\
"audio" : {"timestamps" : ("04:43.4", "05:05.5" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Apex Legends'",\
              scriptedvided.r6sText('1920x1080, low settings' , 50, 38),\
              scriptedvided.r6sText('1600x900, low settings'  , 57, 43),\
              scriptedvided.r6sText('1280x720, low settings'  , 69, 52),\
]}, \
})

configs["episodes"].append(\
{ "title": "Doom Eternal",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:25.4" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Doom Eternal'",\
              "'HD7790 \: nope \:\)'",
              scriptedvided.r6sText('R7 260X, 720p low settings' , 82, 61),\
]}, \
})

configs["episodes"].append(\
{ "title": "Rainbow Six: Siege",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:56" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Rainbow Six\: Siege'",\
              scriptedvided.r6sText('1920x1080, 100% scale, low settings' , 6, 5),\
              scriptedvided.r6sText('1280x720, 100% scale, low settings'  , 15, 10),\
              scriptedvided.r6sText('1920x1080, 50% scale, low settings'  , 12, 10),\
              scriptedvided.r6sText('1280x720, 50% scale, low settings'   , 94, 59),\
]}, \
})

configs["episodes"].append(\
{ "title": "R6S both cards",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:20" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : "R6S_BonaireXT.png"}\
}, \
"isChapter" : False,\
"video" : "stock_RainbowSixSiege_benchmark3.mp4",
})

configs["episodes"].append(\
{ "title": "Control",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:52.6" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Control'",\
              scriptedvided.r6sText('1280x720, lowest settings, DX12' , 31, 20),\
              scriptedvided.r6sText('1280x720, lowest settings, DX11' , 58, 31),\
]}, \
})

configs["episodes"].append(\
{ "title": "Control both cards",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:06.2" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : "Control_BonaireXT.png"}\
}, \
"isChapter" : False,\
"video" : "GTX970_Control_DX11_medium.mp4",
})

configs["episodes"].append(\
{ "title": "Overwatch 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:31.1" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Overwatch 2'",\
              scriptedvided.r6sText('1920x1080, low settings' , 98, 78),\
              scriptedvided.r6sText('1600x900, low settings'  , 137, 111),\
              scriptedvided.r6sText('1280x720, low settings'  , 199, 166),\
]}, \
})

configs["episodes"].append(\
{ "title": "Resident Evil 4 (Remake)", \
"video" : "stock_re4demo_phoneCall.mp4", \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:49.3" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Resident Evil 4 \(Remake\)'",\
              "HD7790 \: LOL",
              scriptedvided.r6sText('R7 260X, 720p prioritize performance' , 47, 27),\
]}, \
})

configs["episodes"].append(\
{ "title": "DOTA2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:09" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Shadow of the Tomb Raider",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:42" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Shadow of the Tomb Raider'",\
              scriptedvided.r6sText('1920x1080, lowest settings' ,38 , 30),\
              scriptedvided.r6sText('1600x900, low settings'     , 38, 27),\
              scriptedvided.r6sText('1280x720, medium settings'  , 39, 29),\
]}, \
"video" : {"file" : "SOTTR_gaming_highest.mp4", "start" : "04:53"}\
})

configs["episodes"].append(\
{ "title": "Borderlands 3",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "09:10.4" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Borderlands 3'",\
              scriptedvided.r6sText('1920x1080, very low settings' , 41, 34),\
              scriptedvided.r6sText('1600x900, low settings'       , 45, 36),\
              scriptedvided.r6sText('1280x720, medium settings'    , 43, 32),\
              scriptedvided.r6sText('1280x720, low settings'       , 58, 45),\
]}, \
})

####################### end of gaming section ###############################

####################### conclusion ###############################
#
configs["episodes"].append(\
{ "title": "Conclusions",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "09:25.3" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "barred_breel_HD7790_v2.mp4"},\
})

configs["episodes"].append(\
{ "title": "12_0 not a silver bullet",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "09:33.5" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "RoboCop-Win64-Shipping_2025_02_24_23_28_48_260.mp4"},\
})

configs["episodes"].append(\
{ "title": "1GB not enough",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "09:49.5" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "stock_RainbowSixSiege_benchmark3.mp4"},\
})

configs["episodes"].append(\
{ "title": "Pricing",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "10:01.5" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "barred_breel_HD7790_v3.mp4"},\
})

configs["episodes"].append(\
{ "title": "Side by side again",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "10:20.8" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_HD7790_260X.mp4"},\
})

configs["episodes"].append(\
{ "title": "bye",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "10:28.4" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "barred_breel_HD7790_v2.mp4"},\
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