import scriptedvided

configs = { "defaultAudioFile" : "RX_580.ogg",\
"mediaFolder" : "F:\\Videos\\RX_580", \
"stockFolder" : "F:\\Videos\\stock",\
"benchmarkFile" : "F:\\Videos\\RX_580\\Benchmark_RX_580.txt",\
"outputFolder" : "F:\\Videos\\RX_580\\output", \
"outputFile" : "RX_580.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "A favorite of miners and gamers alike", "until" : "Rainbow Six: Siege"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Rainbow Six: Siege", "until" : "XDefiant"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "XDefiant", "until" : "DOTA2"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "DOTA2", "until" : "Conclusions"}}, \
{"file" : "Inspired - MaikonMusic  Free Background Music  Audio Library Release.mp3", "timestamps" : ("00:00", None ), "destinationTimestamp" : {"title" : "Conclusions", "until" : "EOF"}}, \
], "volume" : 0.06 },\
"episodes" : [],\
"youtube" : {"title" : "R7 260: 11 years old, DX 12 capable tested in 2024", \
"description" : '''We're revisiting the R7 260, but using different games though. 
We're using the same Z230 workstation with an i7 4770 equivalent CPU and 32 GB of DDR3 running in dual channel at 1600MHz.''',\
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
"tags" : "AMD,ATI,Radeon,R7 260,Bonaire,GCN,GCN2,GCN 2,GCN 2.0",\
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
configs["episodes"].append(\
{ "title": "A favorite of miners and gamers alike",\
"audio" : {"timestamps" : ("09:37.3", "09:46" ), "volume" : 0.999, "padAudio" : 0.0 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "The vega box",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:00", "00:09.8" ), "volume" : 0.999, "padAudio" : 0.0 },\
"video" : ""\
})

configs["episodes"].append(\
{ "title": "holds an RX580",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:27" ), "volume" : 0.999, "padAudio" : 0.0 },\
"video" : ""\
})


configs["episodes"].append(\
{ "title": "The GPU",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:45.2" ), "volume" : 0.999, "padAudio" : 0.0 },\
"video" : ""\
})

configs["episodes"].append(\
{ "title": "Cooling and thermals",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:06" ), "volume" : 0.999, "padAudio" : 0.0 },\
"video" : {"file" : "", "rotation" : 90},\
})

configs["episodes"].append(\
{ "title": "temps",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:19.9" ), "volume" : 0.999, "padAudio" : 0.0 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "The test system: Z230 workstation (HP)",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:32.9" ), "volume" : 0.999, "padAudio" : 0.0 },\
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
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:02" ), "padAudio" : 0.0 },\
"overlay" : { \
    "text" : ["'Rainbow Six\: Siege'",\
              scriptedvided.r6sText('1920x1080, low settings, 100% render scale', 190,138 ), \
              scriptedvided.r6sText('1280x720, low settings, 100% render scale', 185 , 121),\
]}, \
})

configs["episodes"].append(\
{ "title": "Doom Eternal",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:28.7" ), "padAudio" : 0.0 },\
"overlay" : { \
    "text" : ["'Doom Eternal'",\
              scriptedvided.r6sText('1920x1080, ultra nightmare settings', 109, 81), \
              scriptedvided.r6sText('1920x1080, low settings', 149, 105), \
]}, \
})

configs["episodes"].append(\
{ "title": "The Finals",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:49.5" ), "padAudio" : 0.0 },\
"overlay" : { \
    "text" : ["'The Finals'",\
              scriptedvided.r6sText('1920x1080, medium settings, ', 61, 31), \
              scriptedvided.r6sText('1920x1080, low settings'     , 62, 29), \
              scriptedvided.r6sText('1280x720, medium settings'   , 64, 30), \
]}, \
})

configs["episodes"].append(\
{ "title": "Fallout 4",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:10.8" ), "padAudio" : 0.0 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, ultra settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Apex Legends",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:37.5" ), "padAudio" : 0.0 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, highest settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Shadow of the Tomb Raider",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:51" ), "padAudio" : 0.0 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, highest settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Counter-Strike 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:12.2" ), "padAudio" : 0.0 },\
"overlay" : { \
    "text" : ["'Counter-Strike 2'",\
              scriptedvided.r6sText('1920x1080, low settings', 117, 68),\
              scriptedvided.r6sText('1600x900, low settings' , 114, 67),\
              scriptedvided.r6sText('1280x720, low settings' , 125, 73),\
]}, \
})

configs["episodes"].append(\
{ "title": "Borderlands 3",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:28" ), "padAudio" : 0.0 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, badass settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "XDefiant",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:01.9" ), "padAudio" : 0.0 },\
"overlay" : { \
    "text" : ["'XDefiant'",\
              scriptedvided.r6sText('1920x1080, ultra settings', 77, 58),\
              scriptedvided.r6sText('1920x1080, high settings',  123, 92),\
              scriptedvided.r6sText('1920x1080, low settings',   190, 107),\
]}, \
})

configs["episodes"].append(\
{ "title": "Resident Evil 4 (Remake)",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:22.9" ), "padAudio" : 0.0 },\
"overlay" : { \
    "text" : ["'Resident Evil 4 (Remake)'",\
              scriptedvided.r6sText('1920x1080, prioritize performance', 94, 59),\
              scriptedvided.r6sText('1920x1080, balanced'              , 56, 34),\
]}, \
})

configs["episodes"].append(\
{ "title": "Fortnite",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:43.3" ), "padAudio" : 0.0 },\
"overlay" : { \
    "text" : ["'Fortnite'",\
              scriptedvided.r6sText('1920x1080, DX12, high settings'  , 69, 56),\
              scriptedvided.r6sText('1920x1080, DX12, medium settings', 100, 72),\
              scriptedvided.r6sText('1920x1080, performance mode'     , 195, 84),\
]}, \
})

configs["episodes"].append(\
{ "title": "Fortnite performance",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:04.1" ), "padAudio" : 0.0 },\
"overlay" : { \
    "text" : ["'Fortnite'",\
              scriptedvided.r6sText('1920x1080, DX12, high settings'  , 69, 56),\
              scriptedvided.r6sText('1920x1080, DX12, medium settings', 100, 72),\
              scriptedvided.r6sText('1920x1080, performance mode'     , 195, 84),\
]}, \
"video" : "FNiteDX12VsPerformance.mp4",
})

configs["episodes"].append(\
{ "title": "Fortnite Reload results",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:24.6" ), "padAudio" : 0.0 },\
"video" : "FortniteClient-bench_reload_2024_07_01.mp4",\
"overlay" : { \
    "text" : ["'Fortnite Reload'",\
              scriptedvided.r6sText('1920x1080, DX12, medium settings',57 , 48),\
              scriptedvided.r6sText('1920x1080, performance mode'     , 218,148 ),\
]}, \
})

configs["episodes"].append(\
{ "title": "Terminator: Resistance",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:46.3" ), "padAudio" : 0.0 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, highest settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Overwatch 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:13.4" ), "padAudio" : 0.0 },\
"overlay" : { \
    "text" : ["'Overwatch 2'",\
              scriptedvided.r6sText('1920x1080, low settings', 302, 243),\
              scriptedvided.r6sText('1600x900, low settings' , 393, 278),\
              scriptedvided.r6sText('1280x720, low settings' , 475, 265),\
]}, \
})

configs["episodes"].append(\
{ "title": "Far Cry 6",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:34.7" ), "padAudio" : 0.0 },\
"overlay" : { \
    "text" : ["'Far Cry 6'",\
              scriptedvided.r6sText('1920x1080, ultra settings' , 54, 42),\
              scriptedvided.r6sText('1920x1080, high settings'  , 65, 52),\
              scriptedvided.r6sText('1920x1080, medium settings', 73, 57),\
              scriptedvided.r6sText('1920x1080, low settings'   , 81, 59),\
]}, \
})

configs["episodes"].append(\
{ "title": "DOTA2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:56.2" ), "padAudio" : 0.0 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Control",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:13.4" ), "padAudio" : 0.0 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, high settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Grand Theft Auto V",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:29" ), "padAudio" : 0.0 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, high settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Warframe",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:47" ), "padAudio" : 0.0 },\
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
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:56.1" ),  "volume" : 0.999, "padAudio" : 0.0 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "CPU bottleneck - finals",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "09:10.1" ),  "volume" : 0.999, "padAudio" : 0.0 },\
"video" : "",\
})

# reviews back in the day
configs["episodes"].append(\
{ "title": "Cheap card",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "09:19.6" ),  "volume" : 0.999, "padAudio" : 0.0 },\
"video" : {"file" : ""},\
})

# reviews back in the day
configs["episodes"].append(\
{ "title": "bought deffective, with issues",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "09:37.3" ),  "volume" : 0.999, "padAudio" : 0.0 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "hook, end",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "09:46" ),  "volume" : 0.999, "padAudio" : 0.0 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "bye",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "09:56" ),  "volume" : 0.999, "padAudio" : 0.0 },\
"video" : {"file" : ""},\
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
scriptedvided.makeVideo(configs)

