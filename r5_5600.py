import scriptedvided

configs = { "defaultAudioFile" : "R5_5600.ogg",\
"mediaFolder" : "F:\\Videos\\R5_5600", \
"stockFolder" : "F:\\Videos\\stock",\
"benchmarkFile" : "F:\\Videos\\R5_5600\\Benchmark_R5_5600.txt",\
"outputFolder" : "F:\\Videos\\R5_5600\\output", \
"outputFile" : "R5_5600.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "Last architecture for AM4", "until" : "Marvel Rivals"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Marvel Rivals", "until" : "DOTA2"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "DOTA2", "until" : "Video rendering test (The GigASUS)"}}, \
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
{ "title": "Last architecture for AM4",\
"audio" : {"timestamps" : ("00:00", "00:18"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "R5_5600_boxed_barred.mp4"},\
})

# focus on PCIE lanes
configs["episodes"].append(\
{ "title": "The CPU",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:33.7" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "R5_5600_TechPowerup.mkv"},\
})

configs["episodes"].append(\
{ "title": "will have gigasus",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:50.6" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Gigasus_ffwd10.mp4"},\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "The test system",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:08.7" ), "volume" : 0.999, "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Custom PC'",\
              "'CPU\: Ryzen 5 5600'",\
              "'RAM\: 32GB DDR4, 3600MHz, dual channel'",\
              "'GPU\: Radeon RX 580'",\
    ]\
}, \
"video" : {"file" : "test_system_RX580.mp4" }\
})

####################### end of intro ###############################


####################### gaming section ###############################
configs["episodes"].append(\
{ "title": "Marvel Rivals",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:32" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, 30% render scale, low settings", \
    }\
}, \
})

# needs redone
configs["episodes"].append(\
{ "title": "Cyberpunk 2077",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:48.6" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, FSR performance, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Fortnite",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:08.4" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, 50% render scale, performance mode", \
    }\
}, \
"video" : {"file" : "FortniteClient-Win64-Shipping_2025_12_01_15_55_26_661.mp4"}\
})


configs["episodes"].append(\
{ "title": "Rainbow Six: Siege",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:37.7"), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1024x768, 25% scale, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Apex Legends",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:01.2" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
},
})

# single resolution
configs["episodes"].append(\
{ "title": "Doom Eternal",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:18.8" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
}\
})

configs["episodes"].append(\
{ "title": "Overwatch 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:39.1" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, 50% render scale, low settings", \
    }\
}\
})

configs["episodes"].append(\
{ "title": "Far Cry 6",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:57.2" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, 50% render scale, low settings", \
    }\
}\
})


configs["episodes"].append(\
{ "title": "Counter-Strike 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:19.1" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, performance FSR, low settings", \
    }\
}\
})

configs["episodes"].append(\
{ "title": "RE4",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:40.5" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, performance FSR, low settings", \
    }\
}\
})

configs["episodes"].append(\
{ "title": "DOTA 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:02" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
},\
"video" : "stock_dota2_1080pLow_scale100.mp4"\
})


configs["episodes"].append(\
{ "title": "The Finals",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:18.3" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, 50% scale, low settings", \
    }\
}, \
"video" : "Discovery_2025_03_15_22_55_07_819.mp4"\
})


#redo and specify a smoother video
configs["episodes"].append(\
{ "title": "Shadow of the Tomb Raider",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:36.2" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, 50% scale, low settings", \
    }\
},\
"video" : {"file" : "SOTTR_gaming_highest.mp4", "start" : "04:53"}\
})

configs["episodes"].append(\
{ "title": "Borderlands 3",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:55.8" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, 50% render scale, lowest settings", \
    }\
},\
})

configs["episodes"].append(\
{ "title": "Control",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:13.4" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "960x540, lowest settings", \
    }\
},\
"video" : {"file" : "GTX970_Control_DX11_medium.mp4"},\
})


####################### end of gaming section ###############################


############################ productivity #################################

# this is both time and cycles, for both SMT on and off
configs["episodes"].append(\
{ "title": "Video rendering test (The GigASUS)",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:24.9" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Gigasus_ffwd10.mp4"},\
})

configs["episodes"].append(\
{ "title": "By itself",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:37.6" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "blurred_dimmed_gigasus.mp4", "start" : "01:00"},\
"isChapter" : False,\
"overlay" : { \
    "image" : {"file" : "R5_5600_ipc.png"}\
}, \
})

configs["episodes"].append(\
{ "title": "Compared with others",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:00.6" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "blurred_dimmed_gigasus.mp4", "start" : "00:30"},\
"isChapter" : False,\
"overlay" : { \
    "image" : {"file" : "R5_5600_ipc_vs_others.png"}\
}, \
})

#############################################################################



####################### conclusion ###############################
# sum of all fps
configs["episodes"].append(\
{ "title": "Conclusions",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:20.5" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "olx_r5_5600_3600.mkv"},\
})

configs["episodes"].append(\
{ "title": "3600 also pcie gen 4",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:34.5" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "R5_5600_boxContents_barred.mp4"},\
})

configs["episodes"].append(\
{ "title": "5600 - not much IPC",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:52" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "r5_5600_3600.mp4"},\
})

configs["episodes"].append(\
{ "title": "bye",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:59" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "R5_5600_inHand_barred.mp4"},\
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

