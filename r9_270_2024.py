import scriptedvided

configs = { "defaultAudioFile" : "r9_270_2024",\
"mediaFolder" : "F:\\Videos\\r9_270_2024", \
"stockFolder" : "F:\\Videos\\stock",\
"benchmarkFile" : "F:\\Videos\\r9_270_2024\\Benchmark_r9_270_2024.txt",\
"outputFolder" : "F:\\Videos\\r9_270_2024\\output", \
"outputFile" : "r9_270_2024.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "", "until" : "Rainbow Six: Siege"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Rainbow Six: Siege", "until" : "Resident Evil 4 (Remake)"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Resident Evil 4 (Remake)", "until" : "Conclusions"}}, \
{"file" : "Inspired - MaikonMusic  Free Background Music  Audio Library Release.mp3", "timestamps" : ("00:00", None ), "destinationTimestamp" : {"title" : "Conclusions", "until" : "EOF"}}, \
], "volume" : 0.05 },\
"episodes" : [],\
"youtube" : {"title" : "The GigASUS R9 270 tested in 2024", \
"description" : '''Gigabyte and ASUS do play along - at least when it comes to this revived R9 270.
We're using the same Z230 workstation to test it, with an i7 4770 equivalent CPU and 32 GB of DDR3 running in dual channel at 1600MHz.''',\
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

configs["episodes"].append(\
{ "title": "Not an ASUS card",\
"audio" : {"timestamps" : ("00:00", "00:12.6" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_GigASUS_R9_270.mp4", "start" : "00:25", "rotation" : 180},\
})


configs["episodes"].append(\
{ "title": "The GPU",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:33" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "need a record for gigasus"},\
})

configs["episodes"].append(\
{ "title": "Cooling and thermals",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:48.6" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GigASUS_r9_270_DCUII_cooling.mp4"},\
})

configs["episodes"].append(\
{ "title": "pipe gap",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:56.5" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GigASUS_r9_270_DCUII_heatpipes.mp4"},\
})

configs["episodes"].append(\
{ "title": "temps",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:10.8" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "same recording, maybe without GPUZ"},\
})

configs["episodes"].append(\
{ "title": "The test system: Z230 workstation (HP)",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:30" ), "volume" : 0.999, "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Z230 workstation from HP'",\
              "'CPU\: E3-1241v3 Xeon (i7 4770 equivalent)'",\
              "'RAM\: 32GB DDR3 at 1600 MHz, dual channel'",\
    ]\
}, \
"video" : {"file" : "Z230_closed.mp4" , "rotation" : 180}\
})

####################### end of intro ###############################




####################### gaming section ###############################
configs["episodes"].append(\
{ "title": "Rainbow Six: Siege",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:06.6" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Rainbow Six\: Siege'",\
              scriptedvided.r6sText('1920x1080, low settings, 100% render scale',61 , 45), \
              scriptedvided.r6sText('1280x720, low settings, 100% render scale',  107, 70),\
              scriptedvided.r6sText('1920x1080, low settings, 50% render scale', 86 ,60 ), \
              scriptedvided.r6sText('1280x720, low settings, 50% render scale',  135 , 81),\
]}, \
})

configs["episodes"].append(\
{ "title": "Doom Eternal", "video" : "R9_270_DOOMEternalx64vk.mp4",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:33.5" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Doom Eternal - nope'",\
]}, \
})

configs["episodes"].append(\
{ "title": "Fallout 4", "video" : "GTX970_Fallout4_2024_04_21_22_06_49_725.mp4",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:07.4" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Fallout 4'",\
              scriptedvided.r6sText('1920x1080, ultra settings',36 , 33), \
              scriptedvided.r6sText('1920x1080, high settings', 39 ,35 ), \
]}, \
})

configs["episodes"].append(\
{ "title": "Apex Legends",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:35" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Apex Legends'",\
              scriptedvided.r6sText('1920x1080, low settings'     , 84,59 ), \
              scriptedvided.r6sText('1600x900, low settings'      , 101, 70), \
              scriptedvided.r6sText('1280x720, low settings'      , 125, 83), \
]}, \
"video" : "rx580_r5apex_2024_07_26_22_34_08_382-converted.mp4" \
})

configs["episodes"].append(\
{ "title": "Shadow of the Tomb Raider",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:03.9" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Shadow of the Tomb Raider'",\
              scriptedvided.r6sText('1920x1080, lowest settings',63 , 43), \
              scriptedvided.r6sText('1920x1080, low settings', 47 ,30 ), \
              scriptedvided.r6sText('1920x1080, medium settings', 37 ,24 ), \
              scriptedvided.r6sText('1600x900, medium settings', 44 ,27 ), \
]}, \
"video" : {"file" : "rx580_SOTTR_2024_07_27_22_58_17_417-converted.mp4" , "start" : "01:42"}\
})

configs["episodes"].append(\
{ "title": "Counter-Strike 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:30.5" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Counter-Strike 2'",\
              scriptedvided.r6sText('1920x1080, low settings', 118, 99),\
              scriptedvided.r6sText('1600x900, low settings' , 123, 86),\
              scriptedvided.r6sText('1280x720, low settings' , 121, 71),\
]}, \
})

configs["episodes"].append(\
{ "title": "Borderlands 3",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:02.9" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Borderlands 3'",\
              scriptedvided.r6sText('1920x1080, very low settings',53 , 41), \
              scriptedvided.r6sText('1920x1080, low settings', 46 ,32 ), \
              scriptedvided.r6sText('1600x900, medium settings', 41 ,30 ), \
              scriptedvided.r6sText('1280x720, high settings', 28 ,20 ), \
]}, \
})

configs["episodes"].append(\
{ "title": "XDefiant",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:28.1" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'XDefiant'",\
              scriptedvided.r6sText('1920x1080, ultra settings', 91, 62 ),\
              scriptedvided.r6sText('1920x1080, high settings',  119, 79 ),\
              scriptedvided.r6sText('1920x1080, low settings',   154, 95 ),\
]}, \
})

configs["episodes"].append(\
{ "title": "Resident Evil 4 (Remake)", "video" : "stock_re4demo_phoneCall.mp4", \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:48.6" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, prioritize performance", \
    }\
},\
})

configs["episodes"].append(\
{ "title": "Fortnite",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:22.1" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Fortnite'",\
              scriptedvided.r6sText('1920x1080, performance mode', 113 , 73 ),\
              scriptedvided.r6sText('1600x900, performance mode',  131 , 64 ),\
              scriptedvided.r6sText('1280x720, performance mode' , 148 , 70 ),\
]}, \
"video" : "rx580_high_FortniteClient-Win64.mp4"\
})

configs["episodes"].append(\
{ "title": "Fortnite Reload results",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:46.9" ), "padAudio" : 0.05 },\
"video" : "FortniteClient-bench_reload_2024_07_01.mp4",\
"overlay" : { \
    "text" : ["'Fortnite Reload'",\
              scriptedvided.r6sText('1920x1080, performance mode', 202 , 103 ),\
              scriptedvided.r6sText('1600x900, performance mode',  219 , 97 ),\
              scriptedvided.r6sText('1280x720, performance mode' , 222 , 88 ),\
]}, \
})

configs["episodes"].append(\
{ "title": "Terminator: Resistance",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:06.9" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Terminator\: Resistance'",\
              scriptedvided.r6sText('1920x1080, high settings', 49 , 35 ),\
              scriptedvided.r6sText('1920x1080, low settings', 77 , 57 ),\
              scriptedvided.r6sText('1280x720, low settings' , 125 , 88 ),\
]}, \
})

configs["episodes"].append(\
{ "title": "Overwatch 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:30.5" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Overwatch 2'",\
              scriptedvided.r6sText('1920x1080, low settings',  149,  117),\
              scriptedvided.r6sText('1600x900, low settings' , 203 , 162 ),\
              scriptedvided.r6sText('1280x720, low settings' ,  284, 232 ),\
]}, \
})

configs["episodes"].append(\
{ "title": "DOTA2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:50" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Control",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:15.2" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Control'",\
              scriptedvided.r6sText('1920x1080, lowest settings',  53,  43),\
              scriptedvided.r6sText('1280x720, lowest settings' ,  99, 75 ),\
]}, \
"video" : "rx580_Control_DX11_2024_07_27_22_47_25_351-converted.mp4" \
})

configs["episodes"].append(\
{ "title": "Grand Theft Auto V",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:37.8" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Warframe",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:58.5" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

####################### end of gaming section ###############################

####################### conclusion ###############################
# really need an upgrade
configs["episodes"].append(\
{ "title": "Conclusions",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "09:06.1" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "record the package, or what's left of it"},\
})


configs["episodes"].append(\
{ "title": "heatsink from the 270x",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "09:18.4" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "record it side by side with the ASUS one"},\
})

configs["episodes"].append(\
{ "title": "gigasus is born",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "09:34" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_GigASUS_R9_270.mp4", "start" : "00:00", "rotation" : 180},\
})

configs["episodes"].append(\
{ "title": "cheap",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "09:51" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "olx"},\
})

configs["episodes"].append(\
{ "title": "drivers",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "10:08.8" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "error_182.mp4"},\
})

configs["episodes"].append(\
{ "title": "subscribe",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "10:15.8" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_GigASUS_R9_270.mp4", "start" : "00:00", "rotation" : 180},\
})

configs["episodes"].append(\
{ "title": "bye",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "10:28.8" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_GigASUS_R9_270.mp4", "rotation" : 180},\
})


##configs["episodes"].append(\
##{ "title": "Blooper",\
##"isChapter" : False,\
##"audio" : {"timestamps" : ( "13:40.5", "14:04.2") },\
##"video" : {"file":"HiRezTrio-P_aladins_R_ealmRoyale_R_ogueCompany.mp4"}\
##})

#scriptedvided.makeVideoForEpisode(configs["episodes"][7], configs)
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
