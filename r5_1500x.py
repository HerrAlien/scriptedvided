import scriptedvided

configs = { "defaultAudioFile" : "R5_1500x.ogg",\
"mediaFolder" : "F:\\Videos\\R5_1500X", \
"stockFolder" : "F:\\Videos\\stock",\
"benchmarkFile" : "F:\\Videos\\R5_1500X\\Benchmark_R5_1500X.txt",\
"outputFolder" : "F:\\Videos\\R5_1500X\\output", \
"outputFile" : "R5_1500X.mp4", \
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
{ "title": "First gen Ryzen quad core, really?",\
"audio" : {"timestamps" : ("00:00", "00:12.4"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_r5_1500x_barred.mp4"},\
})

# focus on PCIE lanes
configs["episodes"].append(\
{ "title": "The CPU",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:32.5" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "r5_1500X_amdPage.mkv"},\
})

configs["episodes"].append(\
{ "title": "The test system",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:41.6" ), "volume" : 0.999, "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Custom PC'",\
              "'CPU\: Ryzen 5 1500X'",\
              "'RAM\: 32GB DDR4, 2933MHz, dual channel'",\
              "'GPU\: Radeon RX 580'",\
    ]\
}, \
"video" : {"file" : "breel_R5_2400g_platform.mp4"},\
})

configs["episodes"].append(\
{ "title": "RX 580 broll",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:55.5" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Polaris_Family_RX580_barred.mp4"},\
"isChapter" : False,\
})


configs["episodes"].append(\
{ "title": "will have gigasus",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:09.6" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Gigasus_ffwd10.mp4"},\
"isChapter" : False,\
})



####################### end of intro ###############################


####################### gaming section ###############################
configs["episodes"].append(\
{ "title": "Marvel Rivals",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:34.2" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, 30% render scale, low settings", \
    }\
}, \
})

# needs redone
configs["episodes"].append(\
{ "title": "Cyberpunk 2077",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:55.7" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1024x768, performance FSR, lowest settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "ARC Raiders",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:21.3" ), "padAudio" : 0.05 },\
"video" : {"file" : "PioneerGame_2026_01_17_08_01_54_227-converted.mp4" , "start": "05:30"},\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, 50% render scale, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Fortnite",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:39.1" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, 50% render scale, performance mode", \
    }\
}, \
"video" : {"file" : "FortniteClient-Win64-Shipping_2026_01_23_23_07_40_730-converted.mp4"}\
})

configs["episodes"].append(\
{ "title": "Control",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:08" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "960x540, lowest settings", \
    }\
},\
"video" : {"file" : "rx580_Control_DX11_2024_07_27_22_47_25_351-converted.mp4"},\
})

configs["episodes"].append(\
{ "title": "Rainbow Six: Siege",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:27.6"), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1024x768, 50% scale, low settings", \
    }\
}, \
})

# single resolution
configs["episodes"].append(\
{ "title": "Doom Eternal",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:53.4" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "800x600, low settings", \
    }\
}\
})

configs["episodes"].append(\
{ "title": "Apex Legends",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:27" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
},
})

configs["episodes"].append(\
{ "title": "Far Cry 6",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:48.7" ), "padAudio" : 0.05 },\
"video" : {"file" : "FarCry6Trial_high.mp4"},\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, 50% render scale, low settings", \
    }\
}\
})

configs["episodes"].append(\
{ "title": "Overwatch 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:21.3" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, 50% render scale, low settings", \
    }\
}\
})

configs["episodes"].append(\
{ "title": "RE4",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:44.2" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "800x600, performance FSR, low settings", \
    }\
}\
})

configs["episodes"].append(\
{ "title": "Counter-Strike 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:03.4" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, balanced FSR, low settings", \
    }\
}\
})

configs["episodes"].append(\
{ "title": "Borderlands 3",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:26" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, 50% render scale, very low settings", \
    }\
},\
})

configs["episodes"].append(\
{ "title": "DOTA 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:48.4" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
},\
"video" : "stock_dota2_1080pLow_scale100.mp4"\
})

configs["episodes"].append(\
{ "title": "Robocop",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:11.4" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, 33% render scale, low settings", \
    }\
},\
})


configs["episodes"].append(\
{ "title": "The Finals",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:36.9" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, 50% scale, low settings", \
    }\
}, \
})


#redo and specify a smoother video
configs["episodes"].append(\
{ "title": "Shadow of the Tomb Raider",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:55.2" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "800x600, lowest settings", \
    }\
},\
})

#redo and specify a smoother video
configs["episodes"].append(\
{ "title": "Terminator",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:17.4" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x1024, 50% scale, low settings", \
    }\
},\
})

####################### end of gaming section ###############################


############################ productivity #################################

# this is both time and cycles, for both SMT on and off
configs["episodes"].append(\
{ "title": "Video rendering test (The GigASUS)",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:31.5" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Gigasus_ffwd10.mp4"},\
})

configs["episodes"].append(\
{ "title": "By itself",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:54.2" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "blurred_dimmed_gigasus.mp4", "start" : "00:30"},\
"isChapter" : False,\
"overlay" : { \
    "image" : {"file" : "overlays.png"}\
}, \
})

configs["episodes"].append(\
{ "title": "Compared with others",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "09:04.9" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "blurred_dimmed_gigasus.mp4", "start" : "01:00"},\
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
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "09:16.2" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_r5_1500x_barred.mp4"},\
})

configs["episodes"].append(\
{ "title": "price olx",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "09:25.2" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "r5_1500x_olx.mkv"},\
})

configs["episodes"].append(\
{ "title": "AM4 mobo breel",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "09:31.9" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "TufX570Gaming+Wifi_overview.MP4"},\
})

configs["episodes"].append(\
{ "title": "side by side with the 3600",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "09:44.6" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_r5_1500x_3600_barred.mp4"},\
})

configs["episodes"].append(\
{ "title": "1500x breel again",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "09:55.7" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_r5_1500x_barred.mp4"},\
})

configs["episodes"].append(\
{ "title": "Skylake breel",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "10:03" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_i5_6400_inMoboInHand_barred.mp4"},\
})

configs["episodes"].append(\
{ "title": "bye with 1500x breel",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "10:10.5" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_r5_1500x_barred.mp4"},\
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

