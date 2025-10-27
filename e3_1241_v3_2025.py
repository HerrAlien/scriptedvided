import scriptedvided

configs = { "defaultAudioFile" : "e3-1241-v3-2025.ogg",\
"mediaFolder" : "F:\\Videos\\E3_1241_v3_2025", \
"stockFolder" : "F:\\Videos\\stock",\
"benchmarkFile" : "F:\\Videos\\E3_1241_v3_2025\\Benchmark_e3_1241_v3_2025.txt",\
"outputFolder" : "F:\\Videos\\E3_1241_v3_2025\\output", \
"outputFile" : "E3_1241_v3_2025.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#00008080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "The i7 equivalent Xeon", "until" : "Marvel Rivals"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Marvel Rivals", "until" : "Shadow of the Tomb Raider"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Shadow of the Tomb Raider", "until" : "Video rendering test (The GigASUS)"}}, \
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
{ "title": "The i7 equivalent Xeon",\
"audio" : {"timestamps" : ("00:00", "00:16.1"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : " "},\
})

configs["episodes"].append(\
{ "title": "The CPU",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:27.1" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : " "},\
})

configs["episodes"].append(\
{ "title": "TDP and cooling",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:38.7" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : " "},\
"isChapter" : False,\
})

# broll with the H81 mobo from GA
configs["episodes"].append(\
{ "title": "The test system",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:58.6" ), "volume" : 0.999, "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Z230 workstation'",\
              "'CPU\: Xeon E3 1241 v3'",\
              "'RAM\: 32GB DDR3, 1600MHz, dual channel'",\
              "'GPU\: Radeon RX 570'",\
    ]\
}, \
"video" : {"file" : "system_b351_z230.mp4", "start" : "00:00"},\
})

configs["episodes"].append(\
{ "title": "Gigasus for IPC",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:14.4" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : " "},\
})

####################### end of intro ###############################


####################### gaming section ###############################
configs["episodes"].append(\
{ "title": "Marvel Rivals",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:43" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, 30% render scale, low settings", \
    }\
}, \
})

# needs redone
configs["episodes"].append(\
{ "title": "Cyberpunk 2077",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:10.6" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1024x768, FSR disabled, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "The Finals",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:29.9" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, 50% scale, low settings", \
    }\
}, \
"video" : "Discovery_2025_03_15_22_55_07_819.mp4"\
})

configs["episodes"].append(\
{ "title": "Robocop",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:51.9" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, 50% render scale, low settings", \
    }\
},\
})

configs["episodes"].append(\
{ "title": "Fortnite",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:35" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Fortnite, performance mode, FAR view distance'",\
              scriptedvided.r6sText('1280x720'  , 151, 16),\
              scriptedvided.r6sText('1600x900'  , 156, 95),\
]}, \
})

configs["episodes"].append(\
{ "title": "Terminator: Resistance",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:12.7" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, 50% scale, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Counter-Strike 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:31.6" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
}\
})

configs["episodes"].append(\
{ "title": "Far Cry 6",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:53.3" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, 50% scale, low settings", \
    }\
}\
})

configs["episodes"].append(\
{ "title": "Apex Legends",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:22.9" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
},
})

configs["episodes"].append(\
{ "title": "Doom Eternal",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:45.2" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, 50% scale, low settings", \
    }\
},
})


configs["episodes"].append(\
{ "title": "Rainbow Six: Siege",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:08.3"), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, 50% scale, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Control",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:33.6" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "960x540, lowest settings", \
    }\
},\
})

configs["episodes"].append(\
{ "title": "Overwatch 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:50.4" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
}\
})

configs["episodes"].append(\
{ "title": "Resident Evil 4 (Remake)", \
"video" : "stock_re4demo_phoneCall.mp4", \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:14.9" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "640x480, low settings", \
    }\
}\
})

configs["episodes"].append(\
{ "title": "DOTA 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:27.5" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
},\
"video" : "stock_dota2_1080pLow_scale100.mp4"\
})

#redo and specify a smoother video
configs["episodes"].append(\
{ "title": "Shadow of the Tomb Raider",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:50" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "800x600, lowest settings", \
    }\
},\
"video" : {"file" : " "}\
})

configs["episodes"].append(\
{ "title": "Borderlands 3",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:15.5" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, 100% render scale, lowest settings", \
    }\
},\
})

####################### end of gaming section ###############################


############################ productivity #################################

# this is both time and cycles, for both SMT on and off
configs["episodes"].append(\
{ "title": "Video rendering test (The GigASUS)",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:25" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Gigasus_ffwd10.mp4"},\
})

configs["episodes"].append(\
{ "title": "By itself",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:42.4" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "blurred_dimmed_gigasus.mp4", "start" : "01:00"},\
"isChapter" : False,\
"overlay" : { \
    "image" : {"file" : "overlay_e3_1241_v3.png"}\
}, \
})

configs["episodes"].append(\
{ "title": "Compared with others",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:56.2" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "blurred_dimmed_gigasus.mp4", "start" : "00:30"},\
"isChapter" : False,\
"overlay" : { \
    "image" : {"file" : "Clock Cycles emphasis.png"}\
}, \
})

#############################################################################



####################### conclusion ###############################
# similar ro 4th gen i7
configs["episodes"].append(\
{ "title": "Conclusions",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "09:14.7" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : " "},\
})

configs["episodes"].append(\
{ "title": "Still ok for gaming",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "09:27" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : " "},\
})

configs["episodes"].append(\
{ "title": "Pricing OLX",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "09:40" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : " "},\
})

configs["episodes"].append(\
{ "title": "pricing vs r5 2600",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "09:58" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : " "},\
})

configs["episodes"].append(\
{ "title": "bye",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "10:11" ),  "volume" : 0.999, "padAudio" : 0.05 },\
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

