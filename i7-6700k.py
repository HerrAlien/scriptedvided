import scriptedvided

configs = { "defaultAudioFile" : "i7-6700k.ogg",\
"mediaFolder" : "F:\\Videos\\i7_6700K", \
"stockFolder" : "F:\\Videos\\stock",\
"benchmarkFile" : "F:\\Videos\\i7_6700K\\Benchmark_i7_6700k.txt",\
"outputFolder" : "F:\\Videos\\i7_6700K\\output", \
"outputFile" : "i7_6700K.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#00008080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "Labeled as eWaste", "until" : "Marvel Rivals"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Marvel Rivals", "until" : "Overwatch 2"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Overwatch 2", "until" : "Checking the IPC"}}, \
{"file" : "Ferco - Inquisitiveness.ogg", "timestamps" : ("01:01", None ), "destinationTimestamp" : {"title" : "Checking the IPC", "until" : "Conclusions"}}, \
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
{ "title": "Labeled as eWaste",\
"audio" : {"timestamps" : ("00:00", "00:09.9"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_Z170_inHand_barred.mp4"},\
})

configs["episodes"].append(\
{ "title": "CPU itself",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:17.9" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_6700k_inHand2_barred.mp4"},\
"isChapter" : False,\
})

# Quad channel
configs["episodes"].append(\
{ "title": "ARC Raiders preview",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:26.9" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "PioneerGame_2026_02_21_Swamp.mp4", "start" : "00:05"},\
"isChapter" : False,\
})

# have some crashes maybe?
configs["episodes"].append(\
{ "title": "cooked",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:37.6" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_6700k_inHand2_barred.mp4"},\
"isChapter" : False,\
})

# this is about the memory. Maybe BIOS screen cap?
configs["episodes"].append(\
{ "title": "The test system",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:53.2" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "More test system",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:09.25" ), "volume" : 0.999, "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Custom PC'",\
              "'CPU\: i7 6700K'",\
              "'RAM\: 32GB DDR4, 2666MHz, quad channel'",\
              "'GPU\: GTX 980'",\
    ]\
}, \
"video" : {"file" : "breel_Z170_inHand_barred.mp4"},\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "GIGASUS preview",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:17.2" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Gigasus_ffwd10.mp4", "start" : "00:00"},\
"isChapter" : False,\
})


####################### end of intro ###############################


####################### gaming section ###############################
configs["episodes"].append(\
{ "title": "Marvel Rivals",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:32.5" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, 30% render scale, low settings", \
    }\
}, \
})

# needs redone
configs["episodes"].append(\
{ "title": "Cyberpunk 2077",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:54.3" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1024x768, performance FSR, lowest settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "ARC Raiders",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:18.7" ), "padAudio" : 0.05 },\
"video" : {"file" : ""},\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, 50% render scale, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Fortnite",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:40.8" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, 50% render scale, performance mode", \
    }\
}, \
"video" : {"file" : "FortniteClient-Win64-Shipping_2026_08_30_08_03_26_860-converted.mp4", "start" : "02:00"}\
})

configs["episodes"].append(\
{ "title": "Control",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:00.9" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "960x540, lowest settings", \
    }\
},\
"video" : "GTX970_Control_DX11_medium.mp4"\
})

configs["episodes"].append(\
{ "title": "Rainbow Six: Siege",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:25.7"), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, 50% scale, low settings", \
    }\
}, \
})

# single resolution
configs["episodes"].append(\
{ "title": "Doom Eternal",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:51.15" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
},\
"video" : {"file" : ""}\
})

configs["episodes"].append(\
{ "title": "Apex Legends",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:11.8" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
},
})

configs["episodes"].append(\
{ "title": "Far Cry 6",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:32.9" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, 50% render scale, low settings", \
    }\
}\
})

configs["episodes"].append(\
{ "title": "Overwatch 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:54.8" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, 50% render scale, low settings", \
    }\
}\
})

configs["episodes"].append(\
{ "title": "RE4",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:20" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, performance FSR, low settings", \
    }\
}\
})

configs["episodes"].append(\
{ "title": "Counter-Strike 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:45.7" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, balanced FSR, low settings", \
    }\
}\
})

configs["episodes"].append(\
{ "title": "Borderlands 3",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:01" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, 50% render scale, very low settings", \
    }\
},\
})

configs["episodes"].append(\
{ "title": "DOTA 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:16.9" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
},\
"video" : "stock_dota2_1080pLow_scale100.mp4"\
})

##configs["episodes"].append(\
##{ "title": "The Finals",\
##"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "padAudio" : 0.05 },\
##"overlay" : { \
##    "benchmark" : { \
##        "settings" : "1280x720, 50% scale, low settings", \
##    }\
##}, \
##})

#redo and specify a smoother video
configs["episodes"].append(\
{ "title": "Shadow of the Tomb Raider",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:40" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "800x600, lowest settings", \
    }\
},\
"video" : {"file" : ""}\
})

#redo and specify a smoother video
configs["episodes"].append(\
{ "title": "Terminator",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:56" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, 20% scale, low settings", \
    }\
},\
})

####################### end of gaming section ###############################


############################ productivity #################################

# this is both time and cycles, for both SMT on and off
configs["episodes"].append(\
{ "title": "Checking the IPC",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:13.4" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Gigasus_ffwd10.mp4", "start" : "01:00"},\
})

configs["episodes"].append(\
{ "title": "By itself",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:26.4" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "blurred_dimmed_gigasus.mp4"},\
"isChapter" : False,\
"overlay" : { \
    "image" : {"file" : "overlays.png"}\
}, \
})

configs["episodes"].append(\
{ "title": "Compared with others",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:34.4" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "blurred_dimmed_gigasus.mp4"},\
"isChapter" : False,\
"overlay" : { \
    "image" : {"file" : "ipc_comparison.png"}\
}, \
})

#############################################################################



####################### conclusion ###############################
# gap in IPC
configs["episodes"].append(\
{ "title": "Conclusions",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:49.1" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "Pricing",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:04.6" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "Competition from AM4",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:20" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "poor value for i7s and Ks",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:36.9" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "move to AM4",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:52.9" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "hint to the E5 2690 v2",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "09:02.6" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "bye",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "09:11.3" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
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

