import scriptedvided

configs = { "defaultAudioFile" : "r5_2600_v2_cpu.ogg",\
"mediaFolder" : "F:\\Videos\\R5_2600", \
"stockFolder" : "F:\\Videos\\stock",\
"benchmarkFile" : "F:\\Videos\\R5_2600\\Benchmark_R5_2600.txt",\
"outputFolder" : "F:\\Videos\\R5_2600\\output", \
"outputFile" : "R5_2600_CPU.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "", "until" : ""}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "", "until" : ""}}, \
{"file" : "Ferco - Inquisitiveness.ogg", "timestamps" : ("01:01", None ), "destinationTimestamp" : {"title" : "", "until" : "Conclusions"}}, \
{"file" : "Inspired - MaikonMusic  Free Background Music  Audio Library Release.mp3", "timestamps" : ("00:00", None ), "destinationTimestamp" : {"title" : "Conclusions", "until" : "EOF"}}, \
], "volume" : 0.05 },\
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

Our 2023 review of the HD 7770: 
Our 2022 review of the HD 7770: https://youtu.be/4rEcNy2YC0I

TechPowerup entries: https://www.techpowerup.com/gpu-specs/radeon-r7-260.c2511
TechPowerup entries: https://www.techpowerup.com/gpu-specs/asus-r7-260-1-gb.b2732
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
#  scriptedvided.r6sText\('.*' *\, *[0-9]*\, *[0-9]*\)
#   "timestamps" *\: *\( *"[0-9\:\.]*" *\, *"[0-9\:\.]*" *\)
#configs["episodes"].append(\
#{ "title": "A favorite of miners and gamers alike",\
#"audio" : {"timestamps" : "", "", "volume" : 0.999, "padAudio" : 0.05 },\
#"video" : {"file" : ""},\
#})

configs["episodes"].append(\
{ "title": "Better than Sandy",\
"audio" : {"timestamps" : "", "", "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "The CPU",\
"audio" : {"timestamps" : (scriptedvided.nextTSconfigs,  "" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

# needs a side by side video
configs["episodes"].append(\
{ "title": "The TDP is real",\
"audio" : {"timestamps" : (scriptedvided.nextTSconfigs,  "" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "bundled cooler",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTSconfigs,  "" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "better cooler",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTSconfigs,  "" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "The games and test system",\
"audio" : {"timestamps" : (scriptedvided.nextTSconfigs,  "" ), "volume" : 0.999, "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Custom build'",\
              "'CPU\: Ryzen 5 2600'",\
              "'RAM\: 32GB DDR4 at 3000 MHz, dual channel'",\
              "'GPU\: EVGA GTX 970'",\
    ]\
}, \
"video" : {"file" : "test_system_noGPU.mp4" }\
})

configs["episodes"].append(\
{ "title": "Selected games",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTSconfigs,  "" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})


####################### end of intro ###############################




####################### gaming section ###############################
configs["episodes"].append(\
{ "title": "Marvel Rivals",\
"audio" : {"timestamps" : (scriptedvided.nextTSconfigs,  "" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, 30% render scale, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Cyberpunk 2077",\
"audio" : {"timestamps" : (scriptedvided.nextTSconfigs,  "" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, 30% render scale, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Fortnite",\
"audio" : {"timestamps" : (scriptedvided.nextTSconfigs,  "" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Fortnite'",\
              scriptedvided.r6sText('1280x720, performance mode',  , ,)\
]}, \
"video" : "rx580_high_FortniteClient-Win64.mp4"\
})

configs["episodes"].append(\
{ "title": "Fortnite Haswell",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTSconfigs,  "" ), "padAudio" : 0.05 },\
"video" : "",\
"overlay" : { \
    "image" : {"file" : ""}\
}, \
})

configs["episodes"].append(\
{ "title": "Fortnite Reload results",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTSconfigs,  "" ), "padAudio" : 0.05 },\
"video" : "FortniteClient-bench_reload_2024_07_01.mp4",\
"overlay" : { \
    "text" : ["'Fortnite Reload'",\
              scriptedvided.r6sText('1280x720, performance mode',  , ,)\
]}, \
})

configs["episodes"].append(\
{ "title": "Rainbow Six: Siege",\
"audio" : {"timestamps" : "", "", "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, 25% render scale, low settings", \
    }\
},
})

configs["episodes"].append(\
{ "title": "r6s Haswell",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTSconfigs,  "" ), "padAudio" : 0.05 },\
"video" : "",\
"overlay" : { \
    "image" : {"file" : ""}\
}, \
})

configs["episodes"].append(\
{ "title": "Apex Legends",\
"audio" : {"timestamps" : (scriptedvided.nextTSconfigs,  "" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
},
"video" : "rx580_r5apex_2024_07_26_22_34_08_382-converted.mp4" \
})

configs["episodes"].append(\
{ "title": "Apex Haswell",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTSconfigs,  "" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : ""}\
}, \
"video" : "rx580_r5apex_2024_07_26_22_34_08_382-converted.mp4" \
})

configs["episodes"].append(\
{ "title": "Overwatch 2",\
"audio" : {"timestamps" : (scriptedvided.nextTSconfigs,  "" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, 50% render scale, low settings", \
    }\
}\
})

configs["episodes"].append(\
{ "title": "Overwatch Haswell",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTSconfigs,  "" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : ""}\
}, \
})

configs["episodes"].append(\
{ "title": "Counter-Strike 2",\
"audio" : {"timestamps" : "", "", "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
},\
})

configs["episodes"].append(\
{ "title": "cs2 haswell",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTSconfigs,  "" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : ""}\
}, \
})

configs["episodes"].append(\
{ "title": "DOTA 2",\
"audio" : {"timestamps" : "", "", "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
},\
})

configs["episodes"].append(\
{ "title": "dota2 haswell",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTSconfigs,  "" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : ""}\
}, \
})

configs["episodes"].append(\
{ "title": "The Finals",\
"audio" : {"timestamps" : (scriptedvided.nextTSconfigs,  "" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
},\
"video" : "rx580_Discovery_2024_07_26_23_03_56_417-converted.mp4" \
})

configs["episodes"].append(\
{ "title": "The Final Haswell",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTSconfigs,  "" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : ""}\
}, \
"video" : "rx580_Discovery_2024_07_26_23_03_56_417-converted.mp4" \
})

configs["episodes"].append(\
{ "title": "Shadow of the Tomb Raider",\
"audio" : {"timestamps" : (scriptedvided.nextTSconfigs,  "" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
},\
"video" : "rx580_Discovery_2024_07_26_23_03_56_417-converted.mp4" \
})

configs["episodes"].append(\
{ "title": "SOTTR CPU usage",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTSconfigs,  "" ), "padAudio" : 0.05 },\
"video" : ""\
})

# maybe a mash-up of all CPU usages?
configs["episodes"].append(\
{ "title": "CPU usage in games is rather low",\
"audio" : {"timestamps" : "", "", "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

####################### end of gaming section ###############################


############################ productivity #################################

# this is both time and cycles, for both SMT on and off
configs["episodes"].append(\
{ "title": "Video rendering test (The GigASUS)",\
"audio" : {"timestamps" : "", "", "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
"overlay" : { \
    "image" : {"file" : ""}\
}, \
})

configs["episodes"].append(\
{ "title": "SMT on compared to SMT off and power",\
"audio" : {"timestamps" : (scriptedvided.nextTSconfigs,  "" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
"isChapter" : False,\
"overlay" : { \
    "image" : {"file" : ""}\
}, \
})

configs["episodes"].append(\
{ "title": "IPC compared to 3600",\
"audio" : {"timestamps" : (scriptedvided.nextTSconfigs,  "" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
"isChapter" : False,\
})

#############################################################################



####################### conclusion ###############################
# similar ro 4th gen i7
configs["episodes"].append(\
{ "title": "Conclusions",\
"audio" : {"timestamps" : (scriptedvided.nextTSconfigs,  "" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "Marvel Rivals, cpu usage",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTSconfigs,  "" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "Finals does better - reuse video and overlay",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTSconfigs,  "" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "pricing",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTSconfigs,  "" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "odd piece",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTSconfigs,  "" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "anybody still using it",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTSconfigs,  "" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "bye",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTSconfigs,  "" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})


##configs["episodes"].append(\
##{ "title": "Blooper",\
##"isChapter" : False,\
##"audio" : {"timestamps" : "", "" },\
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

