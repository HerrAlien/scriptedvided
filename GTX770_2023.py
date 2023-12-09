import scriptedvided

configs = { "defaultAudioFile" : "GTX770_2023.ogg",\
"mediaFolder" : "F:\\Videos\\GTX770_2023", \
"stockFolder" : "F:\\Videos\\stock",\
"benchmarkFile" : "F:\\Videos\\GTX770_2023\\Benchmark_GTX770_2023.txt",\
"outputFolder" : "F:\\Videos\\GTX770_2023\\output", \
"outputFile" : "GTX770_2023.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#00800080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3",\
"timestamps" : ("00:30", None ), "destinationTimestamp" : {"title" : "The shocking Kepler", "until" : "Alien: Isolation"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3",\
"timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Alien: Isolation", "until" : "Control"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3",\
"timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Control", "until" : "DOTA2"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3",\
"timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "DOTA2", "until" : "Rocket League"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3",\
"timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Rocket League", "until" : "Rogue Company"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3",\
"timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Rogue Company", "until" : "Conclusions"}}, \
{"file" : "Guide You Home - Ferco and Andie - Free Background Music - Audio Library Release.ogg", "timestamps" : ("00:20", None ), "destinationTimestamp" : { "title": "Conclusions", "until" : "Blooper" }}, \
], "volume" : 0.04 },\
"episodes" : [],\
"youtube" : {"title" : "Cheapest DX12 Radeon video card tested in 2023", \
"description" : '''In this video we're checking out the GTX 770. 
As usual, we're using the Z230 workstation with an i7 4770 equivalent CPU and 32 GB of DDR3 running in dual channel at 1600MHz.''',\
"links" : '''
Track: Bliss Of Heaven — SOMM [Audio Library Release]
Music provided by Audio Library Plus
Watch: https://www.youtube.com/watch?v=JQ6mKeQLZak&t=0s
Free Download / Stream: https://alplus.io/blisss-heaven

Track: Far Far Away — Ferco [Audio Library Release]
Music provided by Audio Library Plus
Watch: https://www.youtube.com/watch?v=SrkQ3K1umlc&t=0s 
Free Download / Stream: https://alplus.io/far-far-away

Track: Guide You Home — Ferco & Andie [Audio Library Release]
Music provided by Audio Library Plus
Watch: https://www.youtube.com/watch?v=16eNerPDIsU&t=0s
Free Download / Stream: https://alplus.io/guide-you-home

Our 2022 review of the GTX 770: https://youtu.be/DhvJv9Ea5WE

TechPowerup entry: https://www.techpowerup.com/gpu-specs/inno3d-gtx-770-herculez-2000.b2029
''', \
"tags" : "NVidia,Kepler,GeForce,GTX,GTX770,GTX 770",\
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

configs["episodes"].append(\
{ "title": "The shocking Kepler",\
"audio" : {"timestamps" : ("00:00", "00:13.4" ), "volume" : 0.999, "padding" : 0.1 },\
"video" : {"file": "breel_GTX770_outside.mp4"}\
})

configs["episodes"].append(\
{ "title": "The GPU",\
"audio" : {"timestamps" : ("00:13.4", "00:28.5" ), "volume" : 0.999, "padding" : 0.1 },\
"video" : {"file" : "gtx770_gpuz.mp4"}\
})

configs["episodes"].append(\
{ "title": "DX support",\
"isChapter" : False, \
"audio" : {"timestamps" : ("00:28.5" , "00:43.5" ), "volume" : 0.999, "padding" : 0.1 },\
"video" : {"file" : "breel_GTX770_outside.mp4"}\
})

configs["episodes"].append(\
{ "title": "Cooling and thermals",\
"audio" : {"timestamps" : ("00:43.5", "00:56" ), "volume" : 0.999, "padding" : 0.1 },\
"video" : {"file": "gtx770_cooling.mp4"}\
})

configs["episodes"].append(\
{ "title": "Temperatures",\
"isChapter" : False, \
"audio" : {"timestamps" : ("00:56", "01:18.2" ), "volume" : 0.999, "padding" : 0.1 },\
"video" : {"file": "gtx770_W_arframe_temps.mp4" , "start" : "02:00"}\
"overlay" : { \
    "text" : ["'Thermals'",\
              "'Heaven\: 74C (49C delta over ambient)'",\
              "'Warframe\: 80C (56C delta over ambient)'",\
              "'Warframe, fan at MAX\: 75C (51C delta over ambient)'",\
    ]\
}, \
})


configs["episodes"].append(\
{ "title": "The test system",\
"audio" : {"timestamps" : ("01:18.2", "01:32.5" ), "volume" : 0.999, "padding" : 0.1 },\
"overlay" : { \
    "text" : ["'Z230 workstation from HP'",\
              "'CPU\: E3-1241v3 Xeon (i7 4770 equivalent)'",\
              "'RAM\: 32GB DDR3 at 1600 MHz, dual channel'",\
    ]\
}, \
"video" : {"file" : "Z230_closed.mp4", "rotation" : 180}\
})

####################### end of intro ###############################



####################### gaming section ###############################
configs["episodes"].append(\
{ "title": "Alien: Isolation",\
"audio" : {"timestamps" : ("01:32.5", "02:03.6" ), "padding" : 0.1  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, ultra settings", \
    }\
}, \
})

# this needs a longer stock video
configs["episodes"].append(\
{ "title": "Apex Legends",\
"audio" : {"timestamps" : ("02:03.6", "02:28.15" ), "padding" : 0.1  },\
"overlay" : { \
    "text" : ["'Apex Legends'",\
              scriptedvided.r6sText('1920x1080, low settings', 79 , 52),\
              scriptedvided.r6sText('1600x900, low settings', 86,  59),\
              scriptedvided.r6sText('1280x720, low settings', 95, 65 ),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "Resident Evil 4 (Remake)",\
"audio" : {"timestamps" : ("02:28.15", "02:51.4" ), "padding" : 0.1  },\
"video" : {"file": "stock_re4demo_choppyExceptCutscenes.mp4", "start" : "03:07"},\
"overlay" : { \
    "text" : ["'Resident Evil 4 (Remake)'",\
              scriptedvided.r6sText('1920x1080, low settings', 0, 0),\
              scriptedvided.r6sText('1280x720, low settings', 0,  0),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "Battlefield V",\
"audio" : {"timestamps" : ("02:51.4", "03:19" ), "padding" : 0.1  },\
"overlay" : { \
    "text" : ["'Battlefield V'",\
              scriptedvided.r6sText('1920x1080, low settings', 56, 43),\
              scriptedvided.r6sText('1600x900, low settings', 65, 49),\
              scriptedvided.r6sText('1280x720, low settings', 79, 58),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "Control",\
"audio" : {"timestamps" : ("03:19", "03:42.3" ), "padding" : 0.1  },\
"overlay" : { \
    "text" : ["'Control'",\
              scriptedvided.r6sText('1920x1080, low settings', 48, 33),\
              scriptedvided.r6sText('1280x720, low settings', 92, 66),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "Rainbow Six: Siege",\
"audio" : {"timestamps" : ("03:42.3", "04:11.3" ), "padding" : 0.1  },\
"overlay" : { \
    "text" : ["'Rainbow Six\: Siege'",\
              scriptedvided.r6sText('1920x1080, low settings, 100% render scale', 117, 90), \
              scriptedvided.r6sText('1280x720, low settings, 100% render scale', 178, 128),\
              scriptedvided.r6sText('1920x1080, low settings, 50% render scale', 147, 108),\
              scriptedvided.r6sText('1280x720, low settings, 50% render scale', 206, 143)]\
}, \
})

configs["episodes"].append(\
{ "title": "Grand Theft Auto V",\
"audio" : {"timestamps" : ("04:11.3", "04:35.15" ), "padding" : 0.1  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Counter-Strike 2",\
"audio" : {"timestamps" : ("04:35.15", "05:00" ), "padding" : 0.1  },\
"overlay" : { \
    "text" : ["'Counter-Strike 2'",\
              scriptedvided.r6sText('1920x1080, low settings', 129, 62),\
              scriptedvided.r6sText('1600x900, low settings', 146, 71),\
              scriptedvided.r6sText('1280x720, low settings', 134,  74),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "DOTA2",\
"audio" : {"timestamps" : ("05:00", "05:17" ), "padding" : 0.1  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Fortnite",\
"audio" : {"timestamps" : ("05:17", "06:01" ), "padding" : 0.1  },\
"overlay" : { \
    "text" : ["'Fortnite'",\
              scriptedvided.r6sText('1920x1080, performance mode', 118, 23), \
              scriptedvided.r6sText('1600x900, performance mode', 124, 68),\
              scriptedvided.r6sText('1280x720, performance mode', 131, 71)]\
}, \
})


configs["episodes"].append(\
{ "title": "Overwatch 2",\
"audio" : {"timestamps" : ("06:01", "06:29.3" ), "padding" : 0.1  },\
"overlay" : { \
    "text" : ["'Overwatch 2'",\
              scriptedvided.r6sText('1920x1080, low settings', 210,  157),\
              scriptedvided.r6sText('1600x900, low settings', 281,  215),\
              scriptedvided.r6sText('1280x720, low settings', 384, 264 ),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "Rocket League",\
"audio" : {"timestamps" : ("06:29.3", "06:49.8" ), "padding" : 0.1  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings, 100% render scale", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Splitgate",\
"audio" : {"timestamps" : ("06:49.8", "07:29.3" ), "padding" : 0.1  },\
"video" : "stock_Splitgate_2023_06_17.mp4",\
"overlay" : { \
    "text" : ["'Splitgate'",\
              scriptedvided.r6sText('1920x1080, low settings, 100% render scale', 195,  17),\
              scriptedvided.r6sText('1280x720, low settings, 100% render scale', 228,  78),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "Valorant",\
"audio" : {"timestamps" : ("07:29.3", "07:30" ), "padding" : 0.1  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "HiRez Studios trio (Paladins, Realm Royale, Rogue Company)",\
"audio" : {"timestamps" : ("07:30", "07:38.7" ), "volume" : 0.999 , "padding" : 0.1  },\
"video" : {"file":"HiRezTrio-P_aladins_R_ealmRoyale_R_ogueCompany.mp4"}\
})



configs["episodes"].append(\
{ "title": "Paladins",\
"isChapter" : False,\
"audio" : {"timestamps" : ("07:38.7", "07:47.1" ), "padding" : 0.1  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, high settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Realm Royale",\
"isChapter" : False,\
"audio" : {"timestamps" : ("07:47.1", "07:56.6" ), "padding" : 0.1  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, high settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Rogue Company",\
"isChapter" : False,\
"audio" : {"timestamps" : ("07:56.6", "08:05" ), "padding" : 0.1  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "World of Tanks Blitz",\
"audio" : {"timestamps" : ("08:05", "08:20.6" ), "padding" : 0.1  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, high settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Warframe",\
"audio" : {"timestamps" : ("08:20.6", "08:41.8" ), "padding" : 0.1  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})
####################### end of gaming section ###############################


####################### conclusion ###############################

configs["episodes"].append(\
{ "title": "Conclusions",\
"audio" : {"timestamps" : ("08:41.8", "08:53.7" ), "volume" : 0.999 , "padding" : 0.1  },\
"video" : {"file" : "breel_GTX770_R9_280_attic.mp4"}\
})

configs["episodes"].append(\
{ "title": "r9 280 recommended",\
"isChapter" : False,\
"audio" : {"timestamps" : ("08:53.7", "09:13" ), "volume" : 0.999 , "padding" : 0.1  },\
"video" : {"file" : "breel_r9_280_outside.mp4"}\
})



configs["episodes"].append(\
{ "title": "GTX960",\
"isChapter" : False,\
"audio" : {"timestamps" : ("09:13", "09:28.5" ), "volume" : 0.999 , "padding" : 0.1  },\
"video" : {"file" : "breel_GTX770_GTX960_attic.mp4", "start" : "00:18"}\
})

configs["episodes"].append(\
{ "title": "bye",\
"isChapter" : False,\
"audio" : {"timestamps" : ("09:28.5", "09:36" ), "volume" : 0.999 , "padding" : 0.1  },\
"video" : {"file" : "breel_GTX770_outside.mp4"}\
})


##configs["episodes"].append(\
##{ "title": "Blooper",\
##"isChapter" : False,\
##"audio" : {"timestamps" : ( "13:40.5", "14:04.2") },\
##"video" : {"file":"HiRezTrio-P_aladins_R_ealmRoyale_R_ogueCompany.mp4"}\
##})

#scriptedvided.makeVideoForEpisode(configs["episodes"][28], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][29], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][30], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][31], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][32], configs)
#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "Splitgate"][0], configs)
scriptedvided.makeVideo(configs)

