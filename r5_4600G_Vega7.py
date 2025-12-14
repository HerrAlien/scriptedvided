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
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "DOTA2 both", "until" : "Video rendering test (The GigASUS)"}}, \
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
#"video" : {"file" : ""},\
#})

configs["episodes"].append(\
{ "title": "Vega 7 better be worth it",\
"audio" : {"timestamps" : ("00:00", ""), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_R5_4600G_CpuAlone_barred.mp4"},\
})

# GPU-Z
configs["episodes"].append(\
{ "title": "The GPU",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:46.6" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "r5_4600G_3600_TPU_Lanes.mkv"},\
"overlay" : { \
    "image" : {"file" : "side_by_side_overlay.png"}\
}, \
})

configs["episodes"].append(\
{ "title": "IGPU price",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:56.4" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "r5_4600G_3600_TPU_Cache.mkv"},\
"overlay" : { \
    "image" : {"file" : "side_by_side_overlay.png"}\
}, \
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "DGPUs",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:03.5" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "R5_4600G_TechPowerup.mkv"},\
"isChapter" : False,\
})

# broll with the H81 mobo from GA
configs["episodes"].append(\
{ "title": "The test system",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:15" ), "volume" : 0.999, "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Custom PC'",\
              "'CPU\: Ryzen 5 4600G'",\
              "'RAM\: 32GB DDR4, 3000MHz, dual channel'",\
              "'GPU\: Radeon RX 580'",\
    ]\
}, \
"video" : {"file" : "breel_R5_2400g_platform.mp4"},\
})

####################### end of intro ###############################


####################### gaming section ###############################
configs["episodes"].append(\
{ "title": "Marvel Rivals",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:42.4" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, performance upscaling, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Marvel Rivals both",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:58.4" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : "Marvel Rivals, 1280x720, 50% scale, low settings.png"}\
}, \
"video" : {"file" : "Marvel-Win64-Shipping_2025_03_15_07_57_44_978-converted.mp4"},\
"isChapter" : False,\
})

# needs redone
configs["episodes"].append(\
{ "title": "Cyberpunk 2077",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:22.3" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, FSR performance, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Cyberpunk 2077 both",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:22.3" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : ""}\
}, \
"video" : {"file" : ""},\
"isChapter" : False,\
})

# needs redone
configs["episodes"].append(\
{ "title": "The Finals",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:22.3" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, FSR performance, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "The Finals both",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:22.3" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : ""}\
}, \
"video" : {"file" : ""},\
"isChapter" : False,\
})

# needs redone
configs["episodes"].append(\
{ "title": "Robocop",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:22.3" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, FSR performance, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Robocop both",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:22.3" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : ""}\
}, \
"video" : {"file" : ""},\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Fortnite",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:47" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, performance mode", \
    }\
}, \
"video" : {"file" : "FortniteClient-Win64-Shipping_2025_12_01_15_55_26_661.mp4"}\
})

configs["episodes"].append(\
{ "title": "Fortnite both",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:22.3" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : ""}\
}, \
"video" : {"file" : ""},\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Terminator",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:47" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, performance mode", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Terminator both",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:22.3" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : ""}\
}, \
"video" : {"file" : ""},\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Counter-Strike 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:49.6" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
}\
})

configs["episodes"].append(\
{ "title": "CS2 both",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:22.3" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : ""}\
}, \
"video" : {"file" : ""},\
"isChapter" : False,\
})


configs["episodes"].append(\
{ "title": "FC6",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:49.6" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
}\
})

configs["episodes"].append(\
{ "title": "FC6 both",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:22.3" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : ""}\
}, \
"video" : {"file" : ""},\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Apex Legends",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:28.1" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
},
})

configs["episodes"].append(\
{ "title": "Apex both",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:51.5" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : "Apex Legends, 1280x720, low settings.png"}\
}, \
"video" : {"file" : "r5apex_bot_royale.mp4"},\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Doom",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:28.1" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
},
})

configs["episodes"].append(\
{ "title": "Doom both",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:51.5" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : "Apex Legends, 1280x720, low settings.png"}\
}, \
"video" : {"file" : "r5apex_bot_royale.mp4"},\
"isChapter" : False,\
})


configs["episodes"].append(\
{ "title": "Rainbow Six: Siege",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:07.9"), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, 50% scale, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "r6s both",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:51.5" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : "Apex Legends, 1280x720, low settings.png"}\
}, \
"video" : {"file" : "r5apex_bot_royale.mp4"},\
"isChapter" : False,\
})


configs["episodes"].append(\
{ "title": "Control",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:54.7" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "960x540, lowest settings", \
    }\
},\
"video" : {"file" : "GTX970_Control_DX11_medium.mp4"},\
})

configs["episodes"].append(\
{ "title": "Control both",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:51.5" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : "Apex Legends, 1280x720, low settings.png"}\
}, \
"video" : {"file" : "r5apex_bot_royale.mp4"},\
"isChapter" : False,\
})


configs["episodes"].append(\
{ "title": "Overwatch 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:15.8" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
}\
})

configs["episodes"].append(\
{ "title": "Overwatch both",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:26" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : ""}\
}, \
"video" : {"file" : "stock_Overwatch2_gameplay.mp4"},\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "RE4",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:15.8" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
}\
})

configs["episodes"].append(\
{ "title": "RE4 both",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:26" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : ""}\
}, \
"video" : {"file" : "stock_Overwatch2_gameplay.mp4"},\
"isChapter" : False,\
})



configs["episodes"].append(\
{ "title": "DOTA 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:07.9" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
},\
"video" : "stock_dota2_1080pLow_scale100.mp4"\
})

configs["episodes"].append(\
{ "title": "DOTA2 both",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:20.8" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : ""}\
}, \
"video" : {"file" : "stock_dota2_1080pLow_scale100.mp4"},\
"isChapter" : False,\
})

#redo and specify a smoother video
configs["episodes"].append(\
{ "title": "Shadow of the Tomb Raider",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:18.2" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "800x600, low settings", \
    }\
},\
"video" : {"file" : "SOTTR_gaming_highest.mp4"}\
})

configs["episodes"].append(\
{ "title": "SOTTR both",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:20.8" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : ""}\
}, \
"video" : {"file" : ""},\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Borderlands 3",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:36.6" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, 100% render scale, lowest settings", \
    }\
},\
})

configs["episodes"].append(\
{ "title": "BL3 both",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:20.8" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : ""}\
}, \
"video" : {"file" : ""},\
"isChapter" : False,\
})


####################### end of gaming section ###############################


####################### conclusion ###############################
# sum of all fps
configs["episodes"].append(\
{ "title": "Conclusions",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:45.7" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "r5apex_bot_royale.mp4"},\
"overlay" : { \
    "image" : {"file" : "Sum of FPS.png"}\
}, \
})

configs["episodes"].append(\
{ "title": "space is a premium",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:54.5" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_R5_4600G_inBox_barred.mp4"},\
})

configs["episodes"].append(\
{ "title": "not for full towers",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "09:10.1" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_R5_4600G_opened_barred.mp4"},\
})

configs["episodes"].append(\
{ "title": "sell the DGPU",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "09:10.1" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_R5_4600G_opened_barred.mp4"},\
})

configs["episodes"].append(\
{ "title": "DGPU better option",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "09:10.1" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_R5_4600G_opened_barred.mp4"},\
})

configs["episodes"].append(\
{ "title": "bye",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "09:15.6" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_R5_4600G_CpuAlone_barred.mp4"},\
})


##configs["episodes"].append(\
##{ "title": "Blooper",\
##"isChapter" : False,\
##"audio" : {"timestamps" : (scriptedvided.nextTS(configs),  "" ) },\
##"video" : {"file" : ""}\
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

