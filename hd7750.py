import scriptedvided

configs = { "defaultAudioFile" : "hd7750.ogg",\
"mediaFolder" : "F:\\Videos\\hd7750", \
"stockFolder" : "F:\\Videos\\stock",\
"benchmarkFile" : "F:\\Videos\\hd7750\\Benchmark_hd7750.txt",\
"outputFolder" : "F:\\Videos\\hd7750\\output", \
"outputFile" : "hd7750.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3",\
"timestamps" : ("00:30", None ), "destinationTimestamp" : {"title" : "One more reason for retesting", "until" : "Alien: Isolation"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3",\
"timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Alien: Isolation", "until" : "DOTA2"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3",\
"timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "DOTA2", "until" : "Genshin Impact"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3",\
"timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Genshin Impact", "until" : "Usefulness of an old (D)GPU"}}, \
{"file" : "Guide You Home - Ferco and Andie - Free Background Music - Audio Library Release.ogg", "timestamps" : ("00:20", None ), "destinationTimestamp" : { "title": "Usefulness of an old (D)GPU", "until" : "Blooper" }}, \
], "volume" : 0.04 },\
"episodes" : [],\
"youtube" : {"title" : "10 years old budget Radeon playing games in 2023", \
"description" : '''In this video we're checking out the HD7750 (AKA R7 250E, or R7 250 512SP). 
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

Iceberg Tech's review of UHD 730: https://www.youtube.com/watch?v=5xvRPxVMQ1k
Our 2022 review of the R7 250: https://youtu.be/61OYLI9ym3s

TechPowerup entry: https://www.techpowerup.com/gpu-specs/asus-hd-7750.b614
''', \
"tags" : "AMD,ATI,Radeon,HD7750,HD 7750,R7 250E,R7 250 512SP,Cape Verde,GCN,GCN1,GCN 1",\
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
{ "title": "Between the R7 250 and HD7770?",\
"audio" : {"timestamps" : ("00:00", "00:13" ), "volume" : 0.999, "padding" : 0.25 },\
"video" : {"file": "gcn_entry_level_cards_asus.mp4"}\
})

configs["episodes"].append(\
{ "title": "The GPU",\
"audio" : {"timestamps" : ("00:13", "00:43" ), "volume" : 0.999, "padding" : 0.25 },\
"video" : {"file" : "hd7750_gpuz.mp4"}\
})

configs["episodes"].append(\
{ "title": "A hidden agenda",\
"audio" : {"timestamps" : ("00:43", "01:08" ), "volume" : 0.999, "padding" : 0.25 },\
"video" : {"file" : "stock_WatchDogsLegion_Dalton.mp4", "start" : "01:00"}\
})

configs["episodes"].append(\
{ "title": "Test system",\
"audio" : {"timestamps" : ("01:08", "01:22" ), "volume" : 0.999, "padding" : 0.25 },\
"video" : {"file" : "Z230_closed.mp4", "rotation" : 180}\
})


configs["episodes"].append(\
{ "title": "Cooling and thermals",\
"audio" : {"timestamps" : ("01:22", "01:34" ), "volume" : 0.999, "padding" : 0.25 },\
"video" : "breel_hd7750_outside.mp4"\
})

configs["episodes"].append(\
{ "title": "Thermals",\
"isChapter" : False, \
"audio" : {"timestamps" : ("01:34", "01:45" ), "volume" : 0.999, "padding" : 0.25 },\
"video" : "hd7750_heaven.mp4"\
})

####################### end of intro ###############################




####################### gaming section ###############################
configs["episodes"].append(\
{ "title": "Alien: Isolation",\
"audio" : {"timestamps" : ("01:45", "02:17.5" ), "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, ultra settings", \
    }\
}, \
})


configs["episodes"].append(\
{ "title": "Apex Legends",\
"audio" : {"timestamps" : ("02:17.5", "02:50" ) , "padding" : 0.25  },\
"overlay" : { \
    "text" : ["'Apex Legends'",\
              scriptedvided.r6sText('1920x1080, low settings', 37,  24),\
              scriptedvided.r6sText('1280x720, low settings', 58,  39),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "CoD Warzone",\
"audio" : {"timestamps" : ("02:50", "03:19.5" ) , "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Battlefield V",\
"audio" : {"timestamps" : ("03:19.5", "03:54" ) , "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Control",\
"audio" : {"timestamps" : ("03:54", "04:28" ) , "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Rainbow Six: Siege",\
"audio" : {"timestamps" : ("04:28", "05:13" ) , "padding" : 0.25  },\
"overlay" : { \
    "text" : ["'Rainbow Six\: Siege'",\
              scriptedvided.r6sText('1920x1080, low settings, 100% render scale', 39, 30), \
              scriptedvided.r6sText('1280x720, low settings, 100% render scale', 72, 52),\
              scriptedvided.r6sText('1920x1080, low settings, 50% render scale', 54, 40),\
              scriptedvided.r6sText('1280x720, low settings, 50% render scale', 94, 64)]\
}, \
})

configs["episodes"].append(\
{ "title": "Grand Theft Auto V",\
"audio" : {"timestamps" : ("05:13", "05:42" ) , "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Counter Strike: Global Offensive",\
"audio" : {"timestamps" : ("05:42", "06:16" ) , "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "DOTA2",\
"audio" : {"timestamps" : ("06:16", "06:53" ) , "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Fortnite",\
"audio" : {"timestamps" : ("06:53", "07:42" ) , "padding" : 0.25  },\
"overlay" : { \
    "text" : ["'Fortnite'",\
              scriptedvided.r6sText('1920x1080, performance mode', 59, 17), \
              scriptedvided.r6sText('1600x900, performance mode', 74, 21),\
              scriptedvided.r6sText('1280x720, performance mode', 92, 26)]\
}, \
})

configs["episodes"].append(\
{ "title": "Mid-break results",\
"audio" : {"timestamps" : ("07:42" , "07:56" ) , "padding" : 0.25  },\
"video" : { "file" : "---" }\
})

configs["episodes"].append(\
{ "title": "Overwatch 2",\
"audio" : {"timestamps" : ("07:56", "08:45" ) , "padding" : 0.25  },\
"overlay" : { \
    "text" : ["'Overwatch 2'",\
              scriptedvided.r6sText('1920x1080, low settings', 62,  47),\
              scriptedvided.r6sText('1600x900, low settings', 84,  67),\
              scriptedvided.r6sText('1280x720, low settings', 124,  100),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "Rocket League",\
"audio" : {"timestamps" : ("08:45", "09:18" ) , "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings, 100% render scale", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Splitgate",\
"audio" : {"timestamps" : ("09:18", "09:56" ) , "padding" : 0.25  },\
"overlay" : { \
    "text" : ["'Splitgate'",\
              scriptedvided.r6sText('1920x1080, low settings, 100% render scale', 59,  45),\
              scriptedvided.r6sText('1280x720, low settings, 100% render scale', 91,  69),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "Valorant",\
"audio" : {"timestamps" : ("09:56", "10:32" ) , "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Genshin Impact",\
"audio" : {"timestamps" : ("10:32", "11:05" ) , "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings, 1.0 render scale", \
    }\
}, \
})


configs["episodes"].append(\
{ "title": "HiRez Studios trio (Paladins, Realm Royale, Rogue Company)",\
"audio" : {"timestamps" : ("11:05", "11:23" ), "volume" : 0.999, "padding" : 0.25 },\
"video" : {"file":"HiRezTrio-P_aladins_R_ealmRoyale_R_ogueCompany.mp4"}\
})



configs["episodes"].append(\
{ "title": "Paladins",\
"isChapter" : False,\
"audio" : {"timestamps" : ("11:23", "11:40" ) , "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, high settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Realm Royale",\
"isChapter" : False,\
"audio" : {"timestamps" : ("11:40", "12:08" ) , "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, high settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Rogue Company",\
"isChapter" : False,\
"audio" : {"timestamps" : ("12:08", "12:34" ) , "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "World of Tanks Blitz",\
"audio" : {"timestamps" :("12:34", "12:56" ) , "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, high settings", \
    }\
}, \
})


configs["episodes"].append(\
{ "title": "DGPU or IGPU",\
"audio" : {"timestamps" : ("12:56", "13:20" ) ,  "volume" : 0.999, "padding" : 0.25  },\
"video" : {"file":"HiRezTrio-P_aladins_R_ealmRoyale_R_ogueCompany.mp4"},\
"isChapter" : False,\
})


configs["episodes"].append(\
{ "title": "Warframe",\
"audio" : {"timestamps" : ("13:20", "13:56" ) , "padding" : 0.25  },\
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
"audio" : {"timestamps" : ("13:56", "14:11" ), "volume" : 0.999 , "padding" : 0.25  },\
"video" : {"file" : "complete list of games"}\
})

configs["episodes"].append(\
{ "title": "Shattered expectations",\
"isChapter" : False,\
"audio" : {"timestamps" : ("14:11", "14:36" ), "volume" : 0.999 , "padding" : 0.25  },\
"video" : {"file" : "gcn_entry_level_cards_asus.mp4", "start" : "00:30"}\
})


configs["episodes"].append(\
{ "title": "HD 7750 pricing",\
"isChapter" : False,\
"audio" : {"timestamps" : ("14:36", "14:52.7" ), "volume" : 0.999, "padding" : 0.25  },\
"video" : {"file" : "---- olx seraches -----"}\
})

configs["episodes"].append(\
{ "title": "HD 7750 and MSI 7770",\
"isChapter" : False,\
"audio" : {"timestamps" : ("14:52.7" , "15:12" ), "volume" : 0.999, "padding" : 0.25  },\
"video" : {"file" : " ---- 7750 and 7770 ----"}\
})


configs["episodes"].append(\
{ "title": "bye",\
"isChapter" : False,\
"audio" : {"timestamps" : ("15:12", "15:21" ), "volume" : 0.999, "padding" : 1  },\
"video" : {"file" : "breel_hd7750_outside.mp4"} \
})

configs["episodes"].append(\
{ "title": "Blooper",\
"isChapter" : False,\
"audio" : {"timestamps" : ("15:21", "15:32.5" ), "volume" : 0.999, "padding" : 0.25  },\
"video" : {"file" : "hd7750_cannotHold820.mp4", "start" : "00:42"} \
})


##configs["episodes"].append(\
##{ "title": "Blooper",\
##"isChapter" : False,\
##"audio" : {"timestamps" : ( "13:40.5", "14:04.2") },\
##"video" : {"file":"HiRezTrio-P_aladins_R_ealmRoyale_R_ogueCompany.mp4"}\
##})

#scriptedvided.makeVideoForEpisode(configs["episodes"][3], configs)
#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "Apex Legends"][0], configs)
scriptedvided.makeVideo(configs)

