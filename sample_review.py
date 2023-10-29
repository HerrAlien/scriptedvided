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
"audio" : {"timestamps" : ("", "" ), "volume" : 0.999, "padding" : 0.25 },\
"video" : {"file": "breel_r9_290x_outside.mp4"}\
})

configs["episodes"].append(\
{ "title": "The GPU",\
"audio" : {"timestamps" : ("", "" ), "volume" : 0.999, "padding" : 0.25 },\
"video" : {"file" : "R9_290X_noFanCurve_idle.mp4"}\
})

configs["episodes"].append(\
{ "title": "Cooling and thermals",\
"audio" : {"timestamps" : ("", "" ), "volume" : 0.999, "padding" : 0.25 },\
"video" : {"file": "R9_290X_coolerWeight-converted.mp4"}\
})

configs["episodes"].append(\
{ "title": "fan curve",\
"isChapter" : False, \
"audio" : {"timestamps" : ("", "" ), "volume" : 0.999, "padding" : 0.25 },\
"video" : {"file": "custom_fan_curve.mp4"}\
})

configs["episodes"].append(\
{ "title": "The test system",\
"audio" : {"timestamps" : ("", "" ), "volume" : 0.999, "padding" : 0.25 },\
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
"audio" : {"timestamps" : ("", "" ), "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, ultra settings", \
    }\
}, \
})

# this needs a longer stock video
configs["episodes"].append(\
{ "title": "Apex Legends",\
"audio" : {"timestamps" : ("", "" ), "padding" : 0.25  },\
"overlay" : { \
    "text" : ["'Apex Legends'",\
              scriptedvided.r6sText('1920x1080, low settings', , ),\
              scriptedvided.r6sText('1600x900, low settings', ,  ),\
              scriptedvided.r6sText('1280x720, low settings', ,  ),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "Resident Evil 4 (Remake)",\
"audio" : {"timestamps" : ("10:12", "10:46" ), "padding" : 0.25  },\
"video" : {"file": "stock_re4demo_choppyExceptCutscenes.mp4", "start" : "03:07"},\
"overlay" : { \
    "text" : ["'Resident Evil 4 (Remake)'",\
              scriptedvided.r6sText('1920x1080, low settings', , ),\
              scriptedvided.r6sText('1280x720, low settings', ,  ),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "Battlefield V",\
"audio" : {"timestamps" : ("02:35", "03:14" ), "padding" : 0.25  },\
"overlay" : { \
    "text" : ["'Battlefield V'",\
              scriptedvided.r6sText('1920x1080, low settings', , ),\
              scriptedvided.r6sText('1600x900, low settings', , ),\
              scriptedvided.r6sText('1280x720, low settings', , ),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "Control",\
"audio" : {"timestamps" : ("03:14", "03:39" ), "padding" : 0.25  },\
"overlay" : { \
    "text" : ["'Control'",\
              scriptedvided.r6sText('1920x1080, low settings', , ),\
              scriptedvided.r6sText('1280x720, low settings', , ),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "Rainbow Six: Siege",\
"audio" : {"timestamps" : ("", "" ), "padding" : 0.25  },\
"overlay" : { \
    "text" : ["'Rainbow Six\: Siege'",\
              scriptedvided.r6sText('1920x1080, low settings, 100% render scale', , ), \
              scriptedvided.r6sText('1280x720, low settings, 100% render scale', , ),\
              scriptedvided.r6sText('1920x1080, low settings, 50% render scale', , ),\
              scriptedvided.r6sText('1280x720, low settings, 50% render scale', , )]\
}, \
})

configs["episodes"].append(\
{ "title": "Grand Theft Auto V",\
"audio" : {"timestamps" : ("", "" ), "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Counter-Strike 2",\
"audio" : {"timestamps" : ("", "" ), "padding" : 0.25  },\
"overlay" : { \
    "text" : ["'Counter-Strike 2'",\
              scriptedvided.r6sText('1920x1080, low settings', , ),\
              scriptedvided.r6sText('1600x900, low settings', , ),\
              scriptedvided.r6sText('1280x720, low settings', ,  ),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "DOTA2",\
"audio" : {"timestamps" : ("", "" ), "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Fortnite",\
"audio" : {"timestamps" : ("", "" ), "padding" : 0.25  },\
"overlay" : { \
    "text" : ["'Fortnite'",\
              scriptedvided.r6sText('1920x1080, performance mode', , ), \
              scriptedvided.r6sText('1600x900, performance mode', , ),\
              scriptedvided.r6sText('1280x720, performance mode', , )]\
}, \
})


configs["episodes"].append(\
{ "title": "Overwatch 2",\
"audio" : {"timestamps" : ("", "" ), "padding" : 0.25  },\
"overlay" : { \
    "text" : ["'Overwatch 2'",\
              scriptedvided.r6sText('1920x1080, low settings', ,  ),\
              scriptedvided.r6sText('1600x900, low settings', ,  ),\
              scriptedvided.r6sText('1280x720, low settings', ,  ),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "Rocket League",\
"audio" : {"timestamps" : ("", "" ), "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings, 100% render scale", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Splitgate",\
"audio" : {"timestamps" : ("", "" ), "padding" : 0.25  },\
"video" : "stock_Splitgate_2023_06_17.mp4",\
"overlay" : { \
    "text" : ["'Splitgate'",\
              scriptedvided.r6sText('1920x1080, low settings, 100% render scale', ,  ),\
              scriptedvided.r6sText('1280x720, low settings, 100% render scale', ,  ),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "Valorant",\
"audio" : {"timestamps" : ("", "" ), "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "HiRez Studios trio (Paladins, Realm Royale, Rogue Company)",\
"audio" : {"timestamps" : ("", "" ), "volume" : 0.999 , "padding" : 0.25  },\
"video" : {"file":"HiRezTrio-P_aladins_R_ealmRoyale_R_ogueCompany.mp4"}\
})



configs["episodes"].append(\
{ "title": "Paladins",\
"isChapter" : False,\
"audio" : {"timestamps" : ("", "" ), "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, high settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Realm Royale",\
"isChapter" : False,\
"audio" : {"timestamps" : ("", "" ), "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, high settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Rogue Company",\
"isChapter" : False,\
"audio" : {"timestamps" : ("", "" ), "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "World of Tanks Blitz",\
"audio" : {"timestamps" : ("", "" ), "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, high settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Warframe",\
"audio" : {"timestamps" : ("", "" ), "padding" : 0.25  },\
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
"audio" : {"timestamps" : ("", "" ), "volume" : 0.999 , "padding" : 0.25  },\
"video" : {"file" : ""}\
})

configs["episodes"].append(\
{ "title": "repair segment",\
"isChapter" : False,\
"audio" : {"timestamps" : ("", "" ), "volume" : 0.999 , "padding" : 0.25  },\
"video" : {"file" : ""}\
})

configs["episodes"].append(\
{ "title": "more deffective on OLX",\
"isChapter" : False,\
"audio" : {"timestamps" : ("", "" ), "volume" : 0.999 , "padding" : 0.25  },\
"video" : {"file" : ""}\
})

configs["episodes"].append(\
{ "title": "working condition on OLX",\
"isChapter" : False,\
"audio" : {"timestamps" : ("", "" ), "volume" : 0.999 , "padding" : 0.25  },\
"video" : {"file" : ""}\
})


configs["episodes"].append(\
{ "title": "how about other cards",\
"isChapter" : False,\
"audio" : {"timestamps" : ("", "" ), "volume" : 0.999 , "padding" : 0.25  },\
"video" : {"file" : ""}\
})

configs["episodes"].append(\
{ "title": "GT 1030",\
"isChapter" : False,\
"audio" : {"timestamps" : ("", "" ), "volume" : 0.999 , "padding" : 0.25  },\
"video" : {"file" : ""}\
})

configs["episodes"].append(\
{ "title": "bye",\
"isChapter" : False,\
"audio" : {"timestamps" : ("", "" ), "volume" : 0.999 , "padding" : 0.25  },\
"video" : {"file" : ""}\
})

configs["episodes"].append(\
{ "title": "Blooper",\
"isChapter" : False,\
"audio" : {"timestamps" : ("", "" ), "volume" : 0.999 , "padding" : 0.25  },\
"video" : {"file" : ""}\
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

