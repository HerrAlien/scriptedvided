import scriptedvided

configs = { "defaultAudioFile" : "r7_250_2023.ogg",\
"mediaFolder" : "F:\\Videos\\R7_250_2023", \
"stockFolder" : "F:\\Videos\\stock",\
"benchmarkFile" : "F:\\Videos\\R7_250_2023\\Benchmark_R7_250_2023.txt",\
"outputFolder" : "F:\\Videos\\R7_250_2023\\output", \
"outputFile" : "R7_250_2023.mp4", \
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
"youtube" : {"title" : "10 years old budget Radeon versus 2023 games", \
"description" : '''In this video we're revisiting the R7 250. 
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

TechPowerup entry: https://www.techpowerup.com/gpu-specs/asus-r7-250.b2488
''', \
"tags" : "AMD,ATI,Radeon,R7 250,Oland,Oland XT,GCN,GCN1,GCN 1",\
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
{ "title": "One more reason for retesting",\
"audio" : {"timestamps" : ("00:00", "00:24" ), "volume" : 0.999, "padding" : 0.25 },\
"video" : {"file": "r7_250_broll_boxLandscape.mp4"}\
})

configs["episodes"].append(\
{ "title": "Test system",\
"audio" : {"timestamps" : ("00:24", "00:42" ), "volume" : 0.999, "padding" : 0.25 },\
"video" : {"file" : "Z230_closed.mp4", "rotation" : 180}\
})

configs["episodes"].append(\
{ "title": "The GPU",\
"audio" : {"timestamps" : ("00:42", "00:59" ), "volume" : 0.999, "padding" : 0.25 },\
"video" : {"file" : "R7_250_gpu_capabilities.mkv"}\
})

configs["episodes"].append(\
{ "title": "Cooling and thermals",\
"audio" : {"timestamps" : ("00:59", "01:14" ), "volume" : 0.999, "padding" : 0.25 },\
"video" : "r7_250.mp4"\
})

configs["episodes"].append(\
{ "title": "Thermals",\
"isChapter" : False, \
"audio" : {"timestamps" : ("01:14", "01:27.5" ), "volume" : 0.999, "padding" : 0.25 },\
"video" : "r7_250_Heaven.mkv"\
})

####################### end of intro ###############################




####################### gaming section ###############################
configs["episodes"].append(\
{ "title": "Alien: Isolation",\
"audio" : {"timestamps" : ("01:27.5", "01:46" ), "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, ultra settings", \
    }\
}, \
})


configs["episodes"].append(\
{ "title": "Apex Legends",\
"audio" : {"timestamps" : ("01:46", "02:13" ) , "padding" : 0.25  },\
"overlay" : { \
    "text" : ["'Apex Legends'",\
              scriptedvided.r6sText('1920x1080, low settings', 35,  24),\
              scriptedvided.r6sText('1280x720, low settings', 55,  37),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "CoD Warzone",\
"audio" : {"timestamps" : ("02:13", "02:51" ) , "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Battlefield V",\
"audio" : {"timestamps" : ("02:51", "03:17" ) , "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Control",\
"audio" : {"timestamps" : ("03:17", "03:57.5" ) , "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Rainbow Six: Siege",\
"audio" : {"timestamps" : ("03:57.5", "04:36" ) , "padding" : 0.25  },\
"overlay" : { \
    "text" : ["'Rainbow Six\: Siege'",\
              scriptedvided.r6sText('1920x1080, low settings, 100% render scale', 34, 28), \
              scriptedvided.r6sText('1280x720, low settings, 100% render scale', 69, 50),\
              scriptedvided.r6sText('1920x1080, low settings, 50% render scale', 51, 37),\
              scriptedvided.r6sText('1280x720, low settings, 50% render scale', 92, 61)]\
}, \
})

configs["episodes"].append(\
{ "title": "Grand Theft Auto V",\
"audio" : {"timestamps" : ("04:36", "05:01" ) , "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Counter Strike: Global Offensive",\
"audio" : {"timestamps" : ("05:01", "05:28" ) , "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "DOTA2",\
"audio" : {"timestamps" : ("05:28", "06:04" ) , "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Fortnite",\
"audio" : {"timestamps" : ("06:04", "06:35.5" ) , "padding" : 0.25  },\
"overlay" : { \
    "text" : ["'Fortnite'",\
              scriptedvided.r6sText('1920x1080, performance mode', 52, 20), \
              scriptedvided.r6sText('1600x900, performance mode', 64, 25),\
              scriptedvided.r6sText('1280x720, performance mode', 82, 28)]\
}, \
})

configs["episodes"].append(\
{ "title": "Overwatch 2",\
"audio" : {"timestamps" : ("06:35.5", "07:12" ) , "padding" : 0.25  },\
"overlay" : { \
    "text" : ["'Overwatch 2'",\
              scriptedvided.r6sText('1920x1080, low settings', 55,  41),\
              scriptedvided.r6sText('1600x900, low settings', 78,  61),\
              scriptedvided.r6sText('1280x720, low settings', 114,  89),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "Rocket League",\
"audio" : {"timestamps" : ("07:12", "07:30" ) , "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings, 100% render scale", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Splitgate",\
"audio" : {"timestamps" : ("07:30", "07:57" ) , "padding" : 0.25  },\
"overlay" : { \
    "text" : ["'Splitgate'",\
              scriptedvided.r6sText('1920x1080, low settings, 100% render scale', 48,  30),\
              scriptedvided.r6sText('1280x720, low settings, 100% render scale', 91,  67),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "Valorant",\
"audio" : {"timestamps" : ("07:57", "08:23" ) , "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Genshin Impact",\
"audio" : {"timestamps" : ("08:23", "08:46" ) , "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings, 1.0 render scale", \
    }\
}, \
})


configs["episodes"].append(\
{ "title": "HiRez Studios trio (Paladins, Realm Royale, Rogue Company)",\
"audio" : {"timestamps" : ("08:46", "08:57" ), "volume" : 0.999, "padding" : 0.25 },\
"video" : {"file":"HiRezTrio-P_aladins_R_ealmRoyale_R_ogueCompany.mp4"}\
})



configs["episodes"].append(\
{ "title": "Paladins",\
"isChapter" : False,\
"audio" : {"timestamps" : ("08:57", "09:04.5" ) , "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, high settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Realm Royale",\
"isChapter" : False,\
"audio" : {"timestamps" : ("09:04.5", "09:11.6" ) , "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, high settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Rogue Company",\
"isChapter" : False,\
"audio" : {"timestamps" : ("09:11.6", "09:19.5" ) , "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "trio close",\
"audio" : {"timestamps" : ("09:19.5", "09:32" ) ,  "volume" : 0.999, "padding" : 0.25  },\
"video" : {"file":"HiRezTrio-P_aladins_R_ealmRoyale_R_ogueCompany.mp4"},\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "World of Tanks Blitz",\
"audio" : {"timestamps" :("09:32", "09:51.3" ) , "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, high settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Warframe",\
"audio" : {"timestamps" : ("09:51.3", "10:12" ) , "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})
####################### end of gaming section ###############################


####################### conclusion ###############################
### old DGPUs over IGPUs ###
configs["episodes"].append(\
{ "title": "Usefulness of an old (D)GPU",\
"audio" : {"timestamps" : ("00:00", "01:13"), "volume" : 0.001 , "padding" : 0.25  },\
"video" : "dgpu_over_igpu.mp4"\
})
###########################

configs["episodes"].append(\
{ "title": "How much is the R7 250 worth?",\
"audio" : {"timestamps" : ("10:12", "10:39" ), "volume" : 0.999 , "padding" : 0.25  },\
"video" : {"file" : "r7_250_broll_boxPortrait.mp4"}\
})

configs["episodes"].append(\
{ "title": "HD7770 as rival",\
"isChapter" : False,\
"audio" : {"timestamps" : ("10:39", "10:57.2" ), "volume" : 0.999 , "padding" : 0.25  },\
"video" : {"file" : "gcn_entry_level_cards_asus.mp4", "start" : "00:00"}\
})


configs["episodes"].append(\
{ "title": "HD 7750 preview",\
"isChapter" : False,\
"audio" : {"timestamps" : ("10:57.2", "11:15" ), "volume" : 0.999, "padding" : 0.25  },\
"video" : {"file" : "gcn_entry_level_cards_asus.mp4", "start" : "00:30"}\
})


configs["episodes"].append(\
{ "title": "bye",\
"isChapter" : False,\
"audio" : {"timestamps" : ("11:15", "11:22" ), "volume" : 0.999, "padding" : 1  },\
"video" : {"file" : "r7_250_broll_boxPortrait.mp4"} \
})

configs["episodes"].append(\
{ "title": "Blooper",\
"isChapter" : False,\
"audio" : {"timestamps" : ("11:22", "11:37" ), "volume" : 0.999, "padding" : 0.25  },\
"video" : {"file" : "r7_250_broll_dog.mp4"} \
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
