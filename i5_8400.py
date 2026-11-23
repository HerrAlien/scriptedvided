import scriptedvided
import sv_ffutils

configs = { "defaultAudioFile" : "i5-8400.ogg",\
"mediaFolder" : "F:\\Videos\\i5_8400", \
"stockFolder" : "F:\\Videos\\stock",\
"benchmarkFile" : "F:\\Videos\\i5_8400\\Benchmark_i5_8400.txt",\
"outputFolder" : "F:\\Videos\\i5_8400\\output", \
"outputFile" : "i5_8400.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#00008080"},\
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
#  scriptedvided.nextTS\(configs\)\, \"\"
#  \"file\" *\: *\".*\"
#  \"video\" *: *\{\"file\" *: *\".* \"\}
# \"video\" *: *\{ *\"file\" *: *\".*\" *\}
#  scriptedvided.r6sText\('.*' *\, *[0-9]*\, *[0-9]*\)
#   "timestamps" *\: *\( *"[0-9\:\.]*" *\, *"[0-9\:\.]*" *\)
#configs["episodes"].append(\
#{ "title": "A favorite of miners and gamers alike",\
#"audio" : {"timestamps" : (scriptedvided.nextTS(configs),  "" ), "volume" : 0.999, "padAudio" : 0.05 },\
#"video" : {"file" : ""},\
#})

configs["episodes"].append(\
{ "title": "What is stagnation",\
"audio" : {"timestamps" : ("00:00", "00:12"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_i5-8400_inHand_barred.mp4"},\
})

configs["episodes"].append(\
{ "title": "CS 2 preview",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:25.2" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "IPC preview",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:31.4" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
"isChapter" : False,\
})

# Maybe add overlay with parameters.
configs["episodes"].append(\
{ "title": "Quad cores - not enough",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:47.1" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_i5-8400_inGrass_barred.mp4"},\
})

configs["episodes"].append(\
{ "title": "intel stock cooler",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:55.4" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
"isChapter" : False,\
})

# breel with CPU in mobo
configs["episodes"].append(\
{ "title": "New motherboard required",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:11.1" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "i5_8400_mobo_barred.mp4"},\
})

# breel with cooler
configs["episodes"].append(\
{ "title": "The test system",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:17.5" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "UT45Cooler_onGrass2.MP4"},\
})

configs["episodes"].append(\
{ "title": "mobo and cooler",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:23.6" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "i5_8400_moboCpuCooler_barred.mp4"},\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "RAM sticks alone",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:31.6" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "DDR4_mixed_barred.mp4"},\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "system with RAM",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:39.9" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "i5_8400_moboCpuRamCooler_barred.mp4"},\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "full system",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:49.2" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "i5_8400_testSysInCase_barred.mp4"},\
"overlay" : { \
    "text" : ["'Custom PC'",\
              "'CPU\: Intel Core i5 8400'",\
              "'RAM\: 32GB DDR4, 26666 MHz, dual channel'",\
              "'GPU\: Strix GTX 980'",\
    ]\
}, \
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "video at actual res",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:01.2" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
"isChapter" : False,\
})


configs["episodes"].append(\
{ "title": "IPC test preview",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:10" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Gigasus_ffwd10.mp4", "start" : "00:00"},\
"isChapter" : False,\
})

####################### end of intro ###############################


####################### gaming section ###############################
configs["episodes"].append(\
{ "title": "Marvel Rivals",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:29.6" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, 30% render scale, low settings", \
    }\
}, \
"video" : {"file" : "i5_8400_marvelrivals.mkv"},\
})

# needs redone
configs["episodes"].append(\
{ "title": "Cyberpunk 2077",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:57.4" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, performance FSR, lowest settings, high crowd density", \
    }\
}, \
"video" : {"file" : "i5_8400_cp2077.mkv"},\
})

# needs redone
configs["episodes"].append(\
{ "title": "Helldivers 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:20.1" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, performance FSR, lowest settings", \
    }\
}, \
"video" : "i5_8400_helldivers2.mkv"\
})

configs["episodes"].append(\
{ "title": "ARC Raiders",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:48.1" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
}, \
"video" : "i5_8400_arcraiders.mkv"\
})

# single resolution
configs["episodes"].append(\
{ "title": "Doom Eternal",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:11.3" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
},\
"video" : "i5_8400_doometernal.mkv"\
})

configs["episodes"].append(\
{ "title": "Apex Legends",\
"audio" : {"timestamps" : ("00:00", "00:17.7" ), "padAudio" : 0.05, "file" : "i5-8400_extras.ogg" },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
},\
"video" : "i5_8400_apexlegends.mkv",\
})

configs["episodes"].append(\
{ "title": "Control",\
"audio" : {"timestamps" : ("04:11.3", "04:30.5" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, lowest settings", \
    }\
},\
"video" : "i5_8400_control.mkv",\
})

configs["episodes"].append(\
{ "title": "Counter-Strike 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:58.3" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, balanced FSR, low settings", \
    }\
},\
"video" : "i5_8400_cs2.mkv"\
})

configs["episodes"].append(\
{ "title": "Fortnite",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:25.7" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, performance mode", \
    }\
}, \
"video" : "i5_8400_fortnite.mkv"\
})

configs["episodes"].append(\
{ "title": "The Finals",\
"audio" : {"timestamps" : ("00:36.7", "00:56.1" ), "padAudio" : 0.05 , "file" : "i5-8400_extras.ogg" },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, 50% scale, lowest settings", \
    }\
}, \
"video" : "i5_8400_thefinals.mkv"\
})

configs["episodes"].append(\
{ "title": "RE4",\
"audio" : {"timestamps" : ("00:17.8", "00:36.2" ), "padAudio" : 0.05 , "file" : "i5-8400_extras.ogg" },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, 50% render scale, low settings", \
    }\
},\
"video" : "i5_8400-RE4.mkv"\
})


configs["episodes"].append(\
{ "title": "Overwatch 2",\
"audio" : {"timestamps" : ("05:25.7", "05:54.9" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, 50% render scale, low settings", \
    }\
},\
"video" : "i5_8400_overwatch2.mkv"\
})

configs["episodes"].append(\
{ "title": "Shadow of the Tomb Raider",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:17.4" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, 50% render scale, lowest settings", \
    }\
},\
"video" : "i5_8400_sottr.mkv"\
})

configs["episodes"].append(\
{ "title": "Borderlands 3",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:35" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, 50% render scale, very low settings", \
    }\
},\
"video" : "i5_8400_borderlands3.mkv"\
})

####################### end of gaming section ###############################


############################ productivity #################################

# this is both time and cycles, for both SMT on and off
configs["episodes"].append(\
{ "title": "Checking the IPC",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:48.5" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Gigasus_ffwd10.mp4", "start" : "00:00"},\
})

configs["episodes"].append(\
{ "title": "time",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:01.1" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "blurred_dimmed_gigasus.mp4"},\
"isChapter" : False,\
"overlay" : { \
    "image" : {"file" : "i5-8400-Time-HL2.png"}\
}, \
})

configs["episodes"].append(\
{ "title": "ipc alone",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:15.3" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Gigasus_ffwd10.mp4", "start" : "00:30"},\
"isChapter" : False,\
"overlay" : { \
    "image" : {"file" : "overlays.png"}\
}, \
})

configs["episodes"].append(\
{ "title": "ipc",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:31.4" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "blurred_dimmed_gigasus.mp4"},\
"isChapter" : False,\
"overlay" : { \
    "image" : {"file" : "i5-8400-IPC-HL2.png"}\
}, \
})

#############################################################################



####################### conclusion ###############################
# conclusion and pricing
configs["episodes"].append(\
{ "title": "Conclusions",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:47.7" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_i5-8400_inGrass_barred.mp4"},\
})

configs["episodes"].append(\
{ "title": "mobo incompatibility",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:55.3" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Asus-PrimeQ370M-C_overview.MP4"},\
})

configs["episodes"].append(\
{ "title": "mobo modding",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:05.4" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Z170_inHand_barred.mp4"},\
})

configs["episodes"].append(\
{ "title": "H110 mobo",\
"isChapter" : False,\
"audio" : {"timestamps" : ("08:06.9", "08:16" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "ASUS-H110M-A_overview.MP4"},\
})

configs["episodes"].append(\
{ "title": "AM4 mobo",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:30.7" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "ASUS-PrimeX370Pro-Overview_bright.mp4"},\
})

configs["episodes"].append(\
{ "title": "mobo and cpu",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:38.3" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "R7_2700_testSystem_CpuMobo_2_barred.mp4"},\
})

configs["episodes"].append(\
{ "title": "ryzen hook",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:44.1" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_R5_1600_zoomed_barred.mp4"},\
})

configs["episodes"].append(\
{ "title": "bye",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:54" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_i5-8400_inHand_barred.mp4"},\
})


configs["backgroundTrack"] = { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : configs["episodes"][0]["title"], "until" : "Marvel Rivals"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Marvel Rivals", "until" : "The Finals"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "The Finals", "until" : "Checking the IPC"}}, \
{"file" : "Ferco - Inquisitiveness.ogg", "timestamps" : ("01:01", None ), "destinationTimestamp" : {"title" : "Checking the IPC", "until" : "Conclusions"}}, \
{"file" : "Inspired - MaikonMusic  Free Background Music  Audio Library Release.mp3", "timestamps" : ("00:00", None ), "destinationTimestamp" : {"title" : "Conclusions", "until" : "EOF"}}, \
], "volume" : 0.038 }

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

