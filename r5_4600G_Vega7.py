import scriptedvided

configs = { "defaultAudioFile" : "R5_4600G_Vega7.ogg",\
"mediaFolder" : "F:\\Videos\\Ryzen5_4600G", \
"stockFolder" : "F:\\Videos\\stock",\
"benchmarkFile" : "F:\\Videos\\Ryzen5_4600G\\Benchmark_R5_4600G_Vega7.txt",\
"outputFolder" : "F:\\Videos\\Ryzen5_4600G\\output_Vega7", \
"outputFile" : "Ryzen5_4600G_Vega7.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "Vega 7 better be worth it", "until" : "Marvel Rivals"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Marvel Rivals", "until" : "DOTA2 both"}}, \
{"file" : "Ferco - Inquisitiveness.ogg", "timestamps" : ("01:01", None ), "destinationTimestamp" : {"title" : "Terminator both", "until" : "Control"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Control", "until" : "Conclusions"}}, \
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
{ "title": "Vega 7 better be worth it",\
"audio" : {"timestamps" : ("00:00", "00:10.5"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_R5_4600G_CpuAlone_barred.mp4"},\
})

# GPU-Z
configs["episodes"].append(\
{ "title": "The GPU",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:27.6" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Vega7-GPUZ.mkv"},\
})

configs["episodes"].append(\
{ "title": "IGPU price",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:41.4" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Vega7-PriceAsDeltaOfMSRPs.mkv"},\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "DGPUs",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:59.3" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "rx460_GTX750Ti_GTX1050ti_barred.mp4", "start" : "00:55"},\
"isChapter" : False,\
})

# broll with the H81 mobo from GA
configs["episodes"].append(\
{ "title": "The test system",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:13.6" ), "volume" : 0.999, "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Custom PC'",\
              "'CPU\: Ryzen 5 4600G'",\
              "'RAM\: 32GB DDR4, 3000MHz, dual channel'",\
              "'GPUs\: Radeon Vega 7, Radeon RX 460, GTX 1050Ti'",\
    ]\
}, \
"video" : {"file" : "breel_R5_2400g_platform.mp4"},\
})

configs["episodes"].append(\
{ "title": "Faster RAM",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:30.6" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_R5_2400g_platform.mp4"},\
"isChapter" : False,\
})

####################### end of intro ###############################


####################### gaming section ###############################
configs["episodes"].append(\
{ "title": "Marvel Rivals",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:51" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Marvel Rivals'",\
              scriptedvided.r6sText('1280x720, low settings'                       , 37 ,32 ),\
              scriptedvided.r6sText('1280x720, performance upscaling, low settings',  72, 56),\
]}, \
})

configs["episodes"].append(\
{ "title": "Marvel Rivals both",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:14.7" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : "Vega7 - Marvel Rivals, 1280x720, 100% scale, low settings.png"}\
}, \
"video" : {"file" : "Marvel-Win64-Shipping_2025_03_15_08_00_31_860-converted.mp4"},\
"isChapter" : False,\
})

# needs redone
configs["episodes"].append(\
{ "title": "Cyberpunk 2077",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:41.1" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Cyberpunk 2077'",\
              scriptedvided.r6sText('1280x720, low settings'            , 35 , 23),\
              scriptedvided.r6sText('1280x720,FSR quality, low settings', 44 , 32),\
]}, \
})

configs["episodes"].append(\
{ "title": "Cyberpunk 2077 both",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:58.7" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : "Vega7 - Cyberpunk 2077, 1280x720, low settings.png"}\
}, \
"video" : {"file" : "Cyberpunk2077_2025_04_03_16_39_57_810-converted.mp4"},\
"isChapter" : False,\
})

# single resolution
configs["episodes"].append(\
{ "title": "The Finals",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:30.6" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : "Vega7 - The Finals, 1280x720, low settings.png"}\
}, \
})

# needs redone
configs["episodes"].append(\
{ "title": "Robocop",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:57.4" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Robocop'",\
              scriptedvided.r6sText('1280x720, low settings'                     , 23 , 20),\
              scriptedvided.r6sText('1280x720, 75% rendering scale, low settings', 32 , 27),\
]}, \
})

configs["episodes"].append(\
{ "title": "Robocop both",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:08.2" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : "Vega7 - Robocop, 1280x720, low settings.png"}\
}, \
"video" : {"file" : "RoboCop-Win64-Shipping_2025_02_24_23_18_20_139.mp4"},\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Fortnite",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:30.3" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Fortnite'",\
              scriptedvided.r6sText('1920x1080, performance mode', 84 ,60),\
              scriptedvided.r6sText('1600x900, performance mode',  105 , 72 ),\
              scriptedvided.r6sText('1280x720, performance mode', 117  , 76 ),\
]}, \
"video" : {"file" : "FortniteClient-Win64-Shipping_2025_12_01_15_55_26_661.mp4"}\
})

configs["episodes"].append(\
{ "title": "Fortnite both",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:46.8" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : "Vega7 - Fortnite, 1920x1080, performance mode.png"}\
}, \
"video" : {"file" : "FortniteClient-Win64-Shipping_2025_12_01_15_55_26_661.mp4"},\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Terminator",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:07.2" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Terminator\: Resistance'",\
              scriptedvided.r6sText('1920x1080, low settings'   ,  51, 38),\
              scriptedvided.r6sText('1920x1080, medium settings',  39, 29 ),\
              scriptedvided.r6sText('1600x900, medium settings' , 53 , 40 ),\
]}, \
})

configs["episodes"].append(\
{ "title": "Terminator both",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:19.1" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : "Vega7 - Terminator, 1920x1080, low settings.png"}\
}, \
"video" : {"file" : "Terminator-Win64-Shipping_2024_07_21_01_07_50_759-converted.mp4"},\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Counter-Strike 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:42.4" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Counter-Strike 2'",\
              scriptedvided.r6sText('1920x1080, low settings', 77,  61),\
              scriptedvided.r6sText('1600x900, low settings',  94,  67),\
              scriptedvided.r6sText('1280x720, low settings',  115,  82),\
]}, \
})

configs["episodes"].append(\
{ "title": "CS2 both",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:57.7" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : "Vega7 - Counter-Strike 2, 1920x1080, low settings.png"}\
}, \
"video" : {"file" : "stock_cs2_R9_270_ct.mp4"},\
"isChapter" : False,\
})


configs["episodes"].append(\
{ "title": "FC6",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:13.6" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Far Cry 6'",\
              scriptedvided.r6sText('1600x900, low settings',  36,  32),\
              scriptedvided.r6sText('1280x720, low settings',  48, 42  ),\
]}, \
})

configs["episodes"].append(\
{ "title": "FC6 both",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:29" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : "Vega7 - Far Cry 6, 1280x720, low settings.png"}\
}, \
"video" : {"file" : "stock_FarCry6_benchmark.mp4"},\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Apex Legends",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:53.3" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Apex Legends'",\
              scriptedvided.r6sText('1920x1080, low settings',  62, 50),\
              scriptedvided.r6sText('1600x900, low settings',   73, 56),\
              scriptedvided.r6sText('1280x720, low settings',   95, 73),\
]}, \
})

configs["episodes"].append(\
{ "title": "Apex both",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:07.3" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : "Vega7 - Apex Legends, 1920x1080, low settings.png"}\
}, \
"video" : {"file" : "r5apex_bot_royale.mp4"},\
"isChapter" : False,\
})

# single resolution
configs["episodes"].append(\
{ "title": "Doom",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:45.8" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : "Vega7 - Doom Eternal, 1280x720, low settings.png"}\
}, \
})

configs["episodes"].append(\
{ "title": "Rainbow Six: Siege",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:02.2"), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Rainbow Six\: Siege'",\
              scriptedvided.r6sText('1920x1080, low settings, 100% scale',  38, 32 ),\
              scriptedvided.r6sText('1280x720, low settings, 100% scale',   74, 60 ),\
              scriptedvided.r6sText('1920x1080, low settings, 50% scale',   59,  49),\
              scriptedvided.r6sText('1280x720, low settings, 50% scale',   106 , 83 ),\
]}, \
})

configs["episodes"].append(\
{ "title": "r6s both",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:13" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : "Vega7 - Rainbow 6_ Siege, 1920x1080, low settings.png"}\
}, \
"video" : {"file" : "stock_RainbowSixSiege_benchmark3.mp4"},\
"isChapter" : False,\
})

# single resolution
configs["episodes"].append(\
{ "title": "Control",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:43.6" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : "Vega7 - Control, 1280x720, lowest settings.png"}\
}, \
})

configs["episodes"].append(\
{ "title": "Overwatch 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "09:10.7" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Overwatch 2'",\
              scriptedvided.r6sText('1920x1080, low settings',  72, 52 ),\
              scriptedvided.r6sText('1600x900, low settings',   98,  72),\
              scriptedvided.r6sText('1280x720, low settings',   144,  103),\
]}, \
})

configs["episodes"].append(\
{ "title": "Overwatch both",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "09:20.4" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : "Vega7 - Overwatch 2, 1920x1080, low settings.png"}\
}, \
"video" : {"file" : "stock_Overwatch2_gameplay_5770.mp4"},\
"isChapter" : False,\
})

# single resolution
configs["episodes"].append(\
{ "title": "RE4",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "09:52.5" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : "Vega7 - Resident Evil 4, 1280x720, low settings.png"}\
}, \
})

# single resolution
configs["episodes"].append(\
{ "title": "DOTA 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "10:23.5" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : "Vega7 - DOTA2, 1920x1080, low settings.png"}\
}, \
"video" : "stock_dota2_1080pLow_scale100.mp4"\
})


#redo and specify a smoother video
configs["episodes"].append(\
{ "title": "Shadow of the Tomb Raider",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "10:45.3" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Shadow of the Tomb Raider'",\
              scriptedvided.r6sText('1920x1080, very low settings', 31 , 26 ),\
              scriptedvided.r6sText('1600x900, very low settings' , 40 , 33 ),\
              scriptedvided.r6sText('1280x720, very low settings' , 52 , 35 ),\
]}, \
"video" : {"file" : "SOTTR_gaming_highest.mp4", "start" : "04:53"}\
})

configs["episodes"].append(\
{ "title": "SOTTR both",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "10:55.4" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : "Vega7 - Shadow of the Tomb Raider, 1920x1080, lowest settings.png"}\
}, \
"video" : {"file" : "SOTTR_gaming_highest.mp4"},\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Borderlands 3",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "11:21.5" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Borderlands 3'",\
              scriptedvided.r6sText('1920x1080, very low settings', 37, 25),\
              scriptedvided.r6sText('1600x900, low settings'      , 40, 28),\
              scriptedvided.r6sText('1280x720, medium settings'   , 41, 34),\
]}, \
})

configs["episodes"].append(\
{ "title": "BL3 both",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "11:40.5" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : "Vega7 - Borderlands 3, 1920x1080, very low settings.png"}\
}, \
"video" : {"file" : "Borderlands3_2024_05_03_22_37_22_347.mp4"},\
"isChapter" : False,\
})


####################### end of gaming section ###############################


####################### conclusion ###############################
# sum of all fps
configs["episodes"].append(\
{ "title": "Conclusions",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "12:10" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Cyberpunk2077_2025_04_03_07_03_32_039-converted.mp4"},\
"overlay" : { \
    "image" : {"file" : "Vega7 - SUM of all FPS.png"}\
}, \
})

configs["episodes"].append(\
{ "title": "space is a premium",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "12:28.2" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "mini-PC.mkv"},\
})

configs["episodes"].append(\
{ "title": "not for full towers",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "12:45.4" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_R5_2400g_platform.mp4"},\
})

configs["episodes"].append(\
{ "title": "sell the DGPU",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "12:52.5" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "1050Ti_olx_2025.mkv"},\
})

configs["episodes"].append(\
{ "title": "DGPU better option",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "13:05.3" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "R5_4600G_vs_3600AndDGPU_barred.mp4"},\
})

configs["episodes"].append(\
{ "title": "bye",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "13:12" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_R5_4600G_opened_barred.mp4"},\
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

