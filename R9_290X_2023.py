import scriptedvided

configs = { "defaultAudioFile" : "R9_290X_2023.ogg",\
"mediaFolder" : "F:\\Videos\\R9_290X_2023", \
"stockFolder" : "F:\\Videos\\stock",\
"benchmarkFile" : "F:\\Videos\\R9_290X_2023\\Benchmark_R9_290X_2023.txt",\
"outputFolder" : "F:\\Videos\\R9_290X_2023\\output", \
"outputFile" : "R9_290X_2023.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3",\
"timestamps" : ("00:30", None ), "destinationTimestamp" : {"title" : "I got lucky with my 10 USD", "until" : "Alien: Isolation"}}, \
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
"tags" : "AMD,ATI,Radeon,R9 290X,Hawaii,GCN,GCN2,GCN 2",\
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
{ "title": "I got lucky with my 10 USD",\
"audio" : {"timestamps" : ("00:00", "00:14.5" ), "volume" : 0.999, "padding" : 0.25 },\
"video" : {"file": "breel_r9_290x_outside.mp4"}\
})

configs["episodes"].append(\
{ "title": "The GPU",\
"audio" : {"timestamps" : ("00:14.5", "00:28" ), "volume" : 0.999, "padding" : 0.25 },\
"video" : {"file" : "R9_290X_noFanCurve_idle.mp4"}\
})

configs["episodes"].append(\
{ "title": "Cooling and thermals",\
"audio" : {"timestamps" : ("00:28", "00:43" ), "volume" : 0.999, "padding" : 0.25 },\
"video" : {"file": "R9_290X_coolerWeight-converted.mp4"}\
})

configs["episodes"].append(\
{ "title": "fan curve",\
"isChapter" : False, \
"audio" : {"timestamps" : ("00:43", "00:55.5" ), "volume" : 0.999, "padding" : 0.25 },\
"video" : {"file": "custom_fan_curve.mp4"}\
})

configs["episodes"].append(\
{ "title": "The test system",\
"audio" : {"timestamps" : ("00:55.5", "01:12" ), "volume" : 0.999, "padding" : 0.25 },\
"video" : {"file" : "Z230_closed.mp4", "rotation" : 180}\
})

configs["episodes"].append(\
{ "title": "bottlenecks",\
"isChapter" : False, \
"audio" : {"timestamps" : ("01:12", "01:20.6" ), "volume" : 0.999, "padding" : 0.25 },\
"video" : {"file": "sysBottleneck_B_F_V.mp4"}\
})

####################### end of intro ###############################



####################### gaming section ###############################
configs["episodes"].append(\
{ "title": "Alien: Isolation",\
"audio" : {"timestamps" : ("01:20.6", "01:45" ), "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, ultra settings", \
    }\
}, \
})

# this needs a longer stock video
configs["episodes"].append(\
{ "title": "Apex Legends",\
"audio" : {"timestamps" : ("01:45", "02:10" ), "padding" : 0.25  },\
"overlay" : { \
    "text" : ["'Apex Legends'",\
              scriptedvided.r6sText('1920x1080, low settings',129 ,82 ),\
              scriptedvided.r6sText('1600x900, low settings',136 ,  100),\
              scriptedvided.r6sText('1280x720, low settings', 141, 105 ),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "Resident Evil 4 (Remake)",\
"audio" : {"timestamps" : ("02:10", "02:39" ), "padding" : 0.25  },\
"video" : {"file": "stock_re4demo_choppyExceptCutscenes.mp4", "start" : "03:07"},\
"overlay" : { \
    "text" : ["'Resident Evil 4 (Remake)'",\
              scriptedvided.r6sText('1920x1080, low settings',72, 45),\
              scriptedvided.r6sText('1280x720, low settings',91 ,54 ),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "Battlefield V",\
"audio" : {"timestamps" : ("02:39", "03:12" ), "padding" : 0.25  },\
"overlay" : { \
    "text" : ["'Battlefield V'",\
              scriptedvided.r6sText('1920x1080, low settings', 85, 60),\
              scriptedvided.r6sText('1600x900, low settings', 95, 67),\
              scriptedvided.r6sText('1280x720, low settings', 107, 69),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "Control",\
"audio" : {"timestamps" : ("03:12", "03:40" ), "padding" : 0.25  },\
"overlay" : { \
    "text" : ["'Control'",\
              scriptedvided.r6sText('1920x1080, low settings', 104, 66),\
              scriptedvided.r6sText('1280x720, low settings', 182,97 ),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "Rainbow Six: Siege",\
"audio" : {"timestamps" : ("03:40", "04:09" ), "padding" : 0.25  },\
"overlay" : { \
    "text" : ["'Rainbow Six\: Siege'",\
              scriptedvided.r6sText('1920x1080, low settings, 100% render scale', 156, 118), \
              scriptedvided.r6sText('1280x720, low settings, 100% render scale', 191, 127),\
              scriptedvided.r6sText('1920x1080, low settings, 50% render scale', 174, 107),\
              scriptedvided.r6sText('1280x720, low settings, 50% render scale', 216, 138)]\
}, \
})

configs["episodes"].append(\
{ "title": "Grand Theft Auto V",\
"audio" : {"timestamps" : ("04:09", "04:35" ), "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Counter-Strike 2",\
"audio" : {"timestamps" : ("04:35", "05:12" ), "padding" : 0.25  },\
"overlay" : { \
    "text" : ["'Counter-Strike 2'",\
              scriptedvided.r6sText('1920x1080, low settings', 136, 72),\
              scriptedvided.r6sText('1600x900, low settings', 140, 78),\
              scriptedvided.r6sText('1280x720, low settings', 167, 86 ),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "DOTA2",\
"audio" : {"timestamps" : ("05:12", "05:36" ), "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Fortnite",\
"audio" : {"timestamps" : ("05:36", "06:08" ), "padding" : 0.25  },\
"overlay" : { \
    "text" : ["'Fortnite'",\
              scriptedvided.r6sText('1920x1080, performance mode', , ), \
              scriptedvided.r6sText('1600x900, performance mode', , ),\
              scriptedvided.r6sText('1280x720, performance mode', , )]\
}, \
})


configs["episodes"].append(\
{ "title": "Overwatch 2",\
"audio" : {"timestamps" : ("06:08", "06:44.5" ), "padding" : 0.25  },\
"overlay" : { \
    "text" : ["'Overwatch 2'",\
              scriptedvided.r6sText('1920x1080, low settings', 124, 66),\
              scriptedvided.r6sText('1600x900, low settings', 131,  67),\
              scriptedvided.r6sText('1280x720, low settings', 137, 68),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "Rocket League",\
"audio" : {"timestamps" : ("06:44.5", "07:07" ), "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings, 100% render scale", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Splitgate",\
"audio" : {"timestamps" : ("07:07", "07:37" ), "padding" : 0.25  },\
"video" : "stock_Splitgate_2023_06_17.mp4",\
"overlay" : { \
    "text" : ["'Splitgate'",\
              scriptedvided.r6sText('1920x1080, low settings, 100% render scale', 221,  121),\
              scriptedvided.r6sText('1280x720, low settings, 100% render scale', 232,  136),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "Valorant",\
"audio" : {"timestamps" : ("07:37", "07:59" ), "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "HiRez Studios trio (Paladins, Realm Royale, Rogue Company)",\
"audio" : {"timestamps" : ("07:59", "08:08.75" ), "volume" : 0.999 , "padding" : 0.25  },\
"video" : {"file":"HiRezTrio-P_aladins_R_ealmRoyale_R_ogueCompany.mp4"}\
})



configs["episodes"].append(\
{ "title": "Paladins",\
"isChapter" : False,\
"audio" : {"timestamps" : ("08:08.75", "08:17.2" ), "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, high settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Realm Royale",\
"isChapter" : False,\
"audio" : {"timestamps" : ("08:17.2", "08:25" ), "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, high settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Rogue Company",\
"isChapter" : False,\
"audio" : {"timestamps" : ("08:25", "08:33" ), "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "World of Tanks Blitz",\
"audio" : {"timestamps" : ("08:33", "08:54.5" ), "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, high settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Warframe",\
"audio" : {"timestamps" : ("08:54.5", "09:21" ), "padding" : 0.25  },\
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
"audio" : {"timestamps" : ("09:21", "09:41" ), "volume" : 0.999 , "padding" : 0.25  },\
"video" : {"file" : "breel_r9_290x_outside_dog.mp4"}\
})

configs["episodes"].append(\
{ "title": "repair segment",\
"isChapter" : False,\
"audio" : {"timestamps" : ("09:41", "09:59" ), "volume" : 0.999 , "padding" : 0.25  },\
"video" : {"file" : "R9_290X_blownCaps2-converted.mp4" , "start" : "00:00"}\
})

configs["episodes"].append(\
{ "title": "more deffective on OLX",\
"isChapter" : False,\
"audio" : {"timestamps" : ("09:59", "10:16.5" ), "volume" : 0.999 , "padding" : 0.25  },\
"video" : {"file" : "olx_r9_290X.mp4", "start" : "00:00"}\
})

configs["episodes"].append(\
{ "title": "working condition on OLX",\
"isChapter" : False,\
"audio" : {"timestamps" : ("10:16.5", "10:26.4" ), "volume" : 0.999 , "padding" : 0.25  },\
"video" : {"file" : "olx_r9_290X.mp4", "start" : "00:40"}\
})


configs["episodes"].append(\
{ "title": "how about other cards",\
"isChapter" : False,\
"audio" : {"timestamps" : ("10:26.4", "10:45.3" ), "volume" : 0.999 , "padding" : 0.25  },\
"video" : {"file" : "olx_gtx_1060.mp4", "start" : "01:00"}\
})

configs["episodes"].append(\
{ "title": "GT 1030",\
"isChapter" : False,\
"audio" : {"timestamps" : ("10:45.3", "10:55" ), "volume" : 0.999 , "padding" : 0.25  },\
"video" : {"file" : "breel_r9_290X_gt1030.mp4"}\
})

configs["episodes"].append(\
{ "title": "bye",\
"isChapter" : False,\
"audio" : {"timestamps" : ("10:55", "11:02" ), "volume" : 0.999 , "padding" : 0.25  },\
"video" : {"file" : "breel_r9_290x_outside_dog.mp4"}\
})

configs["episodes"].append(\
{ "title": "Blooper",\
"isChapter" : False,\
"audio" : {"timestamps" : ("11:02", "11:19.6" ), "volume" : 0.999 , "padding" : 0.25  },\
"video" : {"file" : "never_stop_evolving.mp4"}\
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

