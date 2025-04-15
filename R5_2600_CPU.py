import scriptedvided

configs = { "defaultAudioFile" : "r5_2600_v2_cpu.ogg",\
"mediaFolder" : "F:\\Videos\\R5_2600", \
"stockFolder" : "F:\\Videos\\stock",\
"benchmarkFile" : "F:\\Videos\\R5_2600\\Benchmark_R5_2600.txt",\
"outputFolder" : "F:\\Videos\\R5_2600\\output", \
"outputFile" : "R5_2600_CPU.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "Better than Sandy", "until" : "Marvel Rivals"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Marvel Rivals", "until" : "DOTA 2"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "DOTA 2", "until" : "Video rendering test (The GigASUS)"}}, \
{"file" : "Ferco - Inquisitiveness.ogg", "timestamps" : ("01:01", None ), "destinationTimestamp" : {"title" : "Video rendering test (The GigASUS)", "until" : "Conclusions"}}, \
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
#"audio" : {"timestamps" : (scriptedvided.nextTS(configs),  "" ), "volume" : 0.999, "padAudio" : 0.05 },\
#"video" : {"file" : ""},\
#})

configs["episodes"].append(\
{ "title": "Better than Sandy",\
"audio" : {"timestamps" : ("00:00", "00:13.2"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_Ryzen5_2600.MP4", "start" : "03:56"},\
})

configs["episodes"].append(\
{ "title": "The CPU",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs),  "00:22.8" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

# needs a side by side video
configs["episodes"].append(\
{ "title": "The TDP is real",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs),  "00:30.4" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "bundled cooler",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs),  "00:36.2" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_Ryzen5_2600.MP4", "start" : "02:30"},\
})

configs["episodes"].append(\
{ "title": "The games and test system",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs),  "00:51.2" ), "volume" : 0.999, "padAudio" : 0.05 },\
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
"audio" : {"timestamps" : (scriptedvided.nextTS(configs),  "01:04.6" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Marvel-Win64-Shipping_2025_03_15_07_57_44_978-converted.mp4", "start" : "00:15"},\
})


####################### end of intro ###############################




####################### gaming section ###############################
configs["episodes"].append(\
{ "title": "Marvel Rivals",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs),  "01:31.3" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, 30% render scale, low settings", \
    }\
}, \
"video" : {"file" : "Marvel-Win64-Shipping_2025_03_15_07_57_44_978-converted.mp4", "start" : "00:29"},\
})

configs["episodes"].append(\
{ "title": "Cyberpunk 2077",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs),  "01:50.3" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1024x768, FSR ultra performance, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Fortnite",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs),  "02:09" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Fortnite'",\
              scriptedvided.r6sText('1280x720, performance mode',  174, 74)\
]}, \
"video" : "FortniteClient-Win64-Shipping_2025_04_03_22_54_36_904-converted.mp4"\
})

configs["episodes"].append(\
{ "title": "Fortnite Haswell",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs),  "02:28" ), "padAudio" : 0.05 },\
"video" : "CpuUsage_F-ortnite.mp4",\
"overlay" : { \
    "image" : {"file" : ""}\
}, \
})

configs["episodes"].append(\
{ "title": "Fortnite Reload results",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs),  "02:45.9" ), "padAudio" : 0.05 },\
"video" : "FortniteClient-bench_reload_2024_07_01.mp4",\
"overlay" : { \
    "text" : ["'Fortnite Reload'",\
              scriptedvided.r6sText('1280x720, performance mode',  182,87)\
]}, \
})

configs["episodes"].append(\
{ "title": "Rainbow Six: Siege",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:07.2"), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, 25% render scale, low settings", \
    }\
},
})

configs["episodes"].append(\
{ "title": "r6s Haswell",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs),  "03:15.7" ), "padAudio" : 0.05 },\
"video" : "CpuUsage_R-6s_2.mp4",\
"overlay" : { \
    "image" : {"file" : ""}\
}, \
})

configs["episodes"].append(\
{ "title": "Apex Legends",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs),  "03:33.7" ), "padAudio" : 0.05 },\
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
"audio" : {"timestamps" : (scriptedvided.nextTS(configs),  "03:41.3" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : ""}\
}, \
"video" : "rx580_r5apex_2024_07_26_22_34_08_382-converted.mp4" \
})

configs["episodes"].append(\
{ "title": "Overwatch 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs),  "04:01.9" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, 50% render scale, low settings", \
    }\
}\
})

configs["episodes"].append(\
{ "title": "Overwatch Haswell",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs),  "04:20.9" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : ""}\
}, \
"video" : "CpuUsage_O-verwatch.mp4"\
})

configs["episodes"].append(\
{ "title": "Counter-Strike 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs),  "04:38.3" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
},\
})

configs["episodes"].append(\
{ "title": "cs2 haswell",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs),  "04:54" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : ""}\
}, \
"video" : "stock_CS2_CT_R7_260X.mp4"\
})

configs["episodes"].append(\
{ "title": "DOTA 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs),  "05:09.9" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
},\
"video" : "stock_dota2_1080pLow_scale100.mp4"\
})

configs["episodes"].append(\
{ "title": "dota2 haswell",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs),  "05:18.6" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : ""}\
}, \
"video" : "stock_dota2_1080pLow_scale100.mp4"\
})

configs["episodes"].append(\
{ "title": "The Finals",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs),  "05:33.4" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
},\
"video" : "Discovery_2025_03_15_22_55_07_819.mp4" \
})

configs["episodes"].append(\
{ "title": "The Final Haswell",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs),  "05:42.3" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : ""}\
}, \
"video" : "Discovery_2025_03_15_22_55_07_819.mp4" \
})

configs["episodes"].append(\
{ "title": "Shadow of the Tomb Raider",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs),  "06:01.3" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
},\
})

configs["episodes"].append(\
{ "title": "SOTTR CPU usage",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs),  "06:09.8" ), "padAudio" : 0.05 },\
"video" : "CpuUsage_S-ottr_village.mp4"\
})

configs["episodes"].append(\
{ "title": "Borderlands 3",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs),  "06:27.5" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
},\
})

configs["episodes"].append(\
{ "title": "Borderlands CPU usage",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs),  "06:35.7" ), "padAudio" : 0.05 },\
"video" : "CpuUsage_B-orderlands3.mp4"\
})

configs["episodes"].append(\
{ "title": "Control",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs),  "06:55.8" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
},\
})

configs["episodes"].append(\
{ "title": "Control CPU usage",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs),  "07:06.4" ), "padAudio" : 0.05 },\
"video" : "CpuUsage_C-ontrol.mp4"\
})

configs["episodes"].append(\
{ "title": "Doom Eternal",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs),  "07:21.83" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
},\
})

configs["episodes"].append(\
{ "title": "Doom CPU usage",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs),  "07:32.8" ), "padAudio" : 0.05 },\
"video" : "CpuUsage_D-oomEternal.mp4"\
})

# maybe a mash-up of all CPU usages?
configs["episodes"].append(\
{ "title": "CPU usage in games is rather low",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs),  "07:45.2" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "cpu_usage_merged.mp4"},\
})

####################### end of gaming section ###############################


############################ productivity #################################

# this is both time and cycles, for both SMT on and off
configs["episodes"].append(\
{ "title": "Video rendering test (The GigASUS)",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs),  "07:58.4" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "blurred_gigasus.mp4"},\
"overlay" : { \
    "image" : {"file" : ""}\
}, \
})

configs["episodes"].append(\
{ "title": "Cycles",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs),  "08:12.3" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "r5_3600_blurred.mp4"},\
"isChapter" : False,\
"overlay" : { \
    "image" : {"file" : ""}\
}, \
})

configs["episodes"].append(\
{ "title": "SMT on compared to SMT off and power",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs),  "08:22.4" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "blurred_gigasus.mp4"},\
"isChapter" : False,\
"overlay" : { \
    "image" : {"file" : ""}\
}, \
})

configs["episodes"].append(\
{ "title": "IPC compared to 3600",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs),  "08:40" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "r5_3600_blurred.mp4"},\
"isChapter" : False,\
"overlay" : { \
    "image" : {"file" : ""}\
}, \
})

#############################################################################



####################### conclusion ###############################
# similar ro 4th gen i7
configs["episodes"].append(\
{ "title": "Conclusions",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs),  "08:51.1" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_Ryzen5_2600.MP4", "start" : "03:56"},\
})

configs["episodes"].append(\
{ "title": "Marvel Rivals, cpu usage",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs),  "09:07.8" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "CpuUsage_M-arvelRivals.mp4"},\
})

configs["episodes"].append(\
{ "title": "Finals does better - reuse video and overlay",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs),  "09:20.8" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : "Discovery_2025_03_15_22_55_07_819.mp4" \
})

configs["episodes"].append(\
{ "title": "pricing",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs),  "09:38.3" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "R5_2600_olx.mkv"},\
})

configs["episodes"].append(\
{ "title": "odd piece",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs),  "09:51.8" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_Ryzen5_2600.MP4", "start" : "03:56"},\
})

configs["episodes"].append(\
{ "title": "anybody still using it",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs),  "10:00.6" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "SteamSurvey_CPU.mkv"},\
})

configs["episodes"].append(\
{ "title": "bye",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs),  "10.08.7" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_Ryzen5_2600.MP4", "start" : "03:56"},\
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

