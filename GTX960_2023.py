import scriptedvided

configs = { "defaultAudioFile" : "gtx_960_2023.ogg",\
"mediaFolder" : "F:\\Videos\\GTX960_2023", \
"stockFolder" : "F:\\Videos\\stock",\
"benchmarkFile" : "F:\\Videos\\GTX960_2023\\Benchmark_GTX960_2023.txt",\
"outputFolder" : "F:\\Videos\\GTX960_2023\\output", \
"outputFile" : "GTX960_2023.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#00800080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3",\
"timestamps" : ("00:30", None ), "destinationTimestamp" : {"title" : "MSI Gaming 4G", "until" : "Alien: Isolation"}}, \
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
"description" : '''In this video we're checking out the R9 290X. 
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
"tags" : "NVidia,Maxwell,GeForce,GTX,GTX960,GTX 960",\
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
{ "title": "MSI Gaming 4G",\
"audio" : {"timestamps" : ("00:00", "00:12" ), "volume" : 0.999, "padding" : 0.1 },\
"video" : {"file": "breel_autumn_GTX960_4G_MSI.mp4"}\
})

configs["episodes"].append(\
{ "title": "The GPU",\
"audio" : {"timestamps" : ("00:12", "00:39.7" ), "volume" : 0.999, "padding" : 0.1 },\
"video" : {"file" : "gtx960_4G_GPUZ.mp4"}\
})

configs["episodes"].append(\
{ "title": "TDP",\
"isChapter" : False, \
"audio" : {"timestamps" : ("00:39.7", "00:54.1" ), "volume" : 0.999, "padding" : 0.1 },\
"video" : {"file": "gtx960_MSI_cooling_better.mp4", "start" : "00:05"}\
})


configs["episodes"].append(\
{ "title": "Cooling and thermals",\
"audio" : {"timestamps" : ("00:54.1", "01:14.15" ), "volume" : 0.999, "padding" : 0.1 },\
"video" : {"file": "msi_gtx960_cooling.mp4"}\
})

configs["episodes"].append(\
{ "title": "Backplate",\
"isChapter" : False, \
"audio" : {"timestamps" : ("01:14.15", "01:23.5" ), "volume" : 0.999, "padding" : 0.1 },\
"video" : {"file": "gtx960_MSI_backplate.mp4"}\
})


configs["episodes"].append(\
{ "title": "Temperatures",\
"isChapter" : False, \
"audio" : {"timestamps" : ("01:23.5", "01:41.3" ), "volume" : 0.999, "padding" : 0.1 },\
"overlay" : { \
    "text" : ["'Thermals'",\
              "'Default fan curve\: 65C (43C delta over ambient)'",\
              "'Fans at MAX\: 53C (31C delta over ambient)'",\
    ]\
}, \
"video" : {"file": "gtx960_4G_GPUZ.mp4"}\
})

configs["episodes"].append(\
{ "title": "The test system",\
"audio" : {"timestamps" : ("01:41.3", "02:04.6" ), "volume" : 0.999, "padding" : 0.1 },\
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
"audio" : {"timestamps" : ("02:04.6", "02:26.4" ), "padding" : 0.1  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, ultra settings", \
    }\
}, \
})

# this needs a longer stock video
configs["episodes"].append(\
{ "title": "Apex Legends",\
"audio" : {"timestamps" : ("02:26.4", "02:53" ), "padding" : 0.1  },\
"overlay" : { \
    "text" : ["'Apex Legends'",\
              scriptedvided.r6sText('1920x1080, low settings', 106, 72),\
              scriptedvided.r6sText('1600x900, low settings', 125, 86 ),\
              scriptedvided.r6sText('1280x720, low settings', 139, 103 ),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "Resident Evil 4 (Remake)",\
"audio" : {"timestamps" : ("02:53", "03:26" ), "padding" : 0.1 },\
"video" : {"file": "stock_re4demo_choppyExceptCutscenes.mp4", "start" : "03:07"},\
"overlay" : { \
    "text" : ["'Resident Evil 4 (Remake)'",\
              scriptedvided.r6sText('1920x1080, low settings', 41, 28),\
              scriptedvided.r6sText('1280x720, low settings', 63,  37),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "Battlefield V",\
"audio" : {"timestamps" : ("03:26", "03:48" ), "padding" : 0.1 },\
"overlay" : { \
    "text" : ["'Battlefield V'",\
              scriptedvided.r6sText('1920x1080, low settings', 58, 48),\
              scriptedvided.r6sText('1600x900, low settings', 69, 56),\
              scriptedvided.r6sText('1280x720, low settings', 85, 67),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "Control",\
"audio" : {"timestamps" : ("03:48", "04:09.8" ), "padding" : 0.1 },\
"overlay" : { \
    "text" : ["'Control'",\
              scriptedvided.r6sText('1920x1080, low settings', 57, 49),\
              scriptedvided.r6sText('1280x720, low settings', 111, 69),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "Rainbow Six: Siege",\
"audio" : {"timestamps" : ("04:09.8", "04:31.3" ), "padding" : 0.1  },\
"overlay" : { \
    "text" : ["'Rainbow Six\: Siege'",\
              scriptedvided.r6sText('1920x1080, low settings, 100% render scale', 122, 99), \
              scriptedvided.r6sText('1280x720, low settings, 100% render scale', 196, 134),\
              scriptedvided.r6sText('1920x1080, low settings, 50% render scale', 157, 107),\
              scriptedvided.r6sText('1280x720, low settings, 50% render scale', 214, 144)]\
}, \
})

configs["episodes"].append(\
{ "title": "Grand Theft Auto V",\
"audio" : {"timestamps" : ("04:31.3", "04:48.5" ), "padding" : 0.1  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Counter-Strike 2",\
"audio" : {"timestamps" : ("04:48.5", "05:22.3" ), "padding" : 0.1  },\
"overlay" : { \
    "text" : ["'Counter-Strike 2'",\
              scriptedvided.r6sText('1920x1080, low settings', 113, 64),\
              scriptedvided.r6sText('1600x900, low settings', 126 , 74),\
              scriptedvided.r6sText('1280x720, low settings', 146, 84 ),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "DOTA2",\
"audio" : {"timestamps" : ("05:22.3", "05:36.2" ), "padding" : 0.1  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Fortnite",\
"audio" : {"timestamps" : ("05:36.2", "06:01" ), "padding" : 0.1  },\
"overlay" : { \
    "text" : ["'Fortnite'",\
              scriptedvided.r6sText('1920x1080, performance mode', 125, 70), \
              scriptedvided.r6sText('1600x900, performance mode', 136, 75),\
              scriptedvided.r6sText('1280x720, performance mode', 144, 80)]\
}, \
})


configs["episodes"].append(\
{ "title": "Overwatch 2",\
"audio" : {"timestamps" : ("06:01", "06:22.5" ), "padding" : 0.1  },\
"overlay" : { \
    "text" : ["'Overwatch 2'",\
              scriptedvided.r6sText('1920x1080, low settings', 196,  153),\
              scriptedvided.r6sText('1600x900, low settings', 233, 182),\
              scriptedvided.r6sText('1280x720, low settings', 360, 267 ),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "Rocket League",\
"audio" : {"timestamps" : ("06:22.5", "06:39.7" ), "padding" : 0.1  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings, 100% render scale", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Splitgate",\
"audio" : {"timestamps" : ("06:39.7", "06:58.2" ), "padding" : 0.1  },\
"overlay" : { \
    "text" : ["'Splitgate'",\
              scriptedvided.r6sText('1920x1080, low settings, 100% render scale', 168,  15),\
              scriptedvided.r6sText('1280x720, low settings, 100% render scale', 232, 83 ),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "Valorant",\
"audio" : {"timestamps" : ("06:58.2", "07:17.5" ), "padding" : 0.1  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "HiRez Studios trio (Paladins, Realm Royale, Rogue Company)",\
"audio" : {"timestamps" : ("07:17.5", "07:26.4" ), "volume" : 0.999 , "padding" : 0.1  },\
"video" : {"file":"HiRezTrio-P_aladins_R_ealmRoyale_R_ogueCompany.mp4"}\
})



configs["episodes"].append(\
{ "title": "Paladins",\
"isChapter" : False,\
"audio" : {"timestamps" : ("07:26.4", "07:33.2" ), "padding" : 0.1  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, high settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Realm Royale",\
"isChapter" : False,\
"audio" : {"timestamps" : ("07:33.2", "07:40.7" ), "padding" : 0.1  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, high settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Rogue Company",\
"isChapter" : False,\
"audio" : {"timestamps" : ("07:40.7", "07:49.5" ), "padding" : 0.1  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "World of Tanks Blitz",\
"audio" : {"timestamps" : ("07:49.5", "08:13" ), "padding" : 0.1  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, high settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Warframe",\
"audio" : {"timestamps" : ("08:13", "08:30.3" ), "padding" : 0.1  },\
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
"audio" : {"timestamps" : ("08:30.3", "08:50.1" ), "volume" : 0.999 , "padding" : 0.1  },\
"video" : {"file" : "gtx960_R9_280_OLX.mkv"}\
})


configs["episodes"].append(\
{ "title": "960 all the way",\
"isChapter" : False,\
"audio" : {"timestamps" : ("08:50.1", "09:05.5" ), "volume" : 0.999 , "padding" : 0.1  },\
"video" : {"file" : "breel_gtx960_MSI_attic.mp4"}\
})

configs["episodes"].append(\
{ "title": "960 will be back and bye",\
"isChapter" : False,\
"audio" : {"timestamps" : ("09:05.5", "09:18.5" ), "volume" : 0.999 , "padding" : 0.1  },\
"video" : {"file" : "breel_autumn_GTX960_4G_MSI.mp4"}\
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

