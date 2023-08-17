import scriptedvided

configs = { "defaultAudioFile" : "r7_260_2023.ogg",\
"mediaFolder" : "F:\\Videos\\R7_260_2023", \
"stockFolder" : "F:\\Videos\\stock",\
"benchmarkFile" : "F:\\Videos\\R7_260_2023\\Benchmark_R7_260_2023.txt",\
"outputFolder" : "F:\\Videos\\R7_260_2023\\output", \
"outputFile" : "R7_260_2023.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3",\
"timestamps" : ("00:30", None ), "destinationTimestamp" : {"title" : "Why re-reviewing the R7 260", "until" : "Alien: Isolation"}}, \
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
"description" : '''In this video we're checking out the R7 260 (AKA R7 360). 
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
{ "title": "Why re-reviewing the R7 260",\
"audio" : {"timestamps" : ("00:00", "00:23" ), "volume" : 0.999, "padding" : 0.25 },\
"video" : {"file": "breel_r7_260_outside.mp4"}\
})

configs["episodes"].append(\
{ "title": "Same pixel rate as the HD 7770",\
"isChapter" : False, \
"audio" : {"timestamps" : ("00:23", "00:41" ), "volume" : 0.999, "padding" : 0.25 },\
"video" : {"file": "breel_hd7770_attic.mp4", "start" : "00:10"}\
})

configs["episodes"].append(\
{ "title": "Test system",\
"audio" : {"timestamps" : ("00:41", "00:54" ), "volume" : 0.999, "padding" : 0.25 },\
"video" : {"file" : "Z230_closed.mp4", "rotation" : 180}\
})

configs["episodes"].append(\
{ "title": "The GPU",\
"audio" : {"timestamps" : ("00:54", "01:14.5" ), "volume" : 0.999, "padding" : 0.25 },\
"video" : {"file" : "R7_260_Heaven_GPUZ.mp4"}\
})

configs["episodes"].append(\
{ "title": "DX 12 support",\
"isChapter" : False, \
"audio" : {"timestamps" : ("01:14.5", "01:29" ), "volume" : 0.999, "padding" : 0.25 },\
"video" : {"file": "stock_re4demo_choppyExceptCutscenes.mp4", "start" : "03:07"}\
})


configs["episodes"].append(\
{ "title": "Cooling and thermals",\
"audio" : {"timestamps" : ("01:29", "01:42" ), "volume" : 0.999, "padding" : 0.25 },\
"video" : "r7_260_1.mp4"\
})

####################### end of intro ###############################



####################### gaming section ###############################
configs["episodes"].append(\
{ "title": "Alien: Isolation",\
"audio" : {"timestamps" : ("01:42", "02:33.5" ), "padding" : 0.25  },\
"video" : "stock_AlienIsolation_3.mp4",\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, ultra settings", \
    }\
}, \
})

# this needs a longer stock video
configs["episodes"].append(\
{ "title": "Apex Legends",\
"audio" : {"timestamps" : ("02:33.5", "03:26" ), "padding" : 0.25  },\
"video" : {"file" : "stock_ApexLegends_long.mp4", "start" : "00:02"},\
"overlay" : { \
    "text" : ["'Apex Legends'",\
              scriptedvided.r6sText('1920x1080, low settings', 59,  41),\
              scriptedvided.r6sText('1600x900, low settings', 76,  51),\
              scriptedvided.r6sText('1280x720, low settings', 101,  68),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "CoD Warzone",\
"audio" : {"timestamps" : ("03:26", "04:03" ), "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Battlefield V",\
"audio" : {"timestamps" : ("04:03", "04:31" ), "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Control",\
"audio" : {"timestamps" : ("04:31", "04:54.5" ), "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Rainbow Six: Siege",\
"audio" : {"timestamps" : ("04:54.5", "05:52" ), "padding" : 0.25  },\
"overlay" : { \
    "text" : ["'Rainbow Six\: Siege'",\
              scriptedvided.r6sText('1920x1080, low settings, 100% render scale', 62, 50), \
              scriptedvided.r6sText('1280x720, low settings, 100% render scale', 118, 87),\
              scriptedvided.r6sText('1920x1080, low settings, 50% render scale', 89, 61),\
              scriptedvided.r6sText('1280x720, low settings, 50% render scale', 153, 105)]\
}, \
})

configs["episodes"].append(\
{ "title": "Grand Theft Auto V",\
"audio" : {"timestamps" : ("05:52", "06:23" ), "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Counter Strike: Global Offensive",\
"audio" : {"timestamps" : ("06:23", "06:52" ), "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "DOTA2",\
"audio" : {"timestamps" : ("06:52", "07:39" ), "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Fortnite",\
"audio" : {"timestamps" : ("07:39", "08:35" ), "padding" : 0.25  },\
"overlay" : { \
    "text" : ["'Fortnite'",\
              scriptedvided.r6sText('1920x1080, performance mode', 84, 25), \
              scriptedvided.r6sText('1600x900, performance mode', 94, 27),\
              scriptedvided.r6sText('1280x720, performance mode', 96, 30)]\
}, \
})


configs["episodes"].append(\
{ "title": "Overwatch 2",\
"audio" : {"timestamps" : ("08:35", "09:26" ), "padding" : 0.25  },\
"overlay" : { \
    "text" : ["'Overwatch 2'",\
              scriptedvided.r6sText('1920x1080, low settings', 96,  68),\
              scriptedvided.r6sText('1600x900, low settings', 134,  97),\
              scriptedvided.r6sText('1280x720, low settings', 198,  144),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "Rocket League",\
"audio" : {"timestamps" : ("09:26", "10:14" ), "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings, 100% render scale", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Splitgate",\
"audio" : {"timestamps" : ("10:14", "10:46" ), "padding" : 0.25  },\
"video" : "stock_Splitgate_2023_06_17.mp4",\
"overlay" : { \
    "text" : ["'Splitgate'",\
              scriptedvided.r6sText('1920x1080, low settings, 100% render scale', 101,  69),\
              scriptedvided.r6sText('1280x720, low settings, 100% render scale', 181,  122),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "Valorant",\
"audio" : {"timestamps" : ("10:46", "11:25" ), "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Genshin Impact",\
"audio" : {"timestamps" : ("11:25", "12:01" ), "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings, 1.0 render scale", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "HiRez Studios trio (Paladins, Realm Royale, Rogue Company)",\
"audio" : {"timestamps" : ("12:01", "12:11" ), "volume" : 0.999 , "padding" : 0.25  },\
"video" : {"file":"HiRezTrio-P_aladins_R_ealmRoyale_R_ogueCompany.mp4"}\
})



configs["episodes"].append(\
{ "title": "Paladins",\
"isChapter" : False,\
"audio" : {"timestamps" : ("12:11", "12:19.5" ), "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, high settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Realm Royale",\
"isChapter" : False,\
"audio" : {"timestamps" : ("12:19.5", "12:27.2" ), "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, high settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Rogue Company",\
"isChapter" : False,\
"audio" : {"timestamps" : ("12:27.2", "12:52.5" ), "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "World of Tanks Blitz",\
"audio" : {"timestamps" : ("12:52.5", "13:16" ), "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, high settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Warframe",\
"audio" : {"timestamps" : ("13:16", "13:56" ), "padding" : 0.25  },\
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
"audio" : {"timestamps" : ("13:56", "14:20.5" ), "volume" : 0.999 , "padding" : 0.25  },\
"video" : {"file" : "r7_260_ropsVsShaders.mkv"}\
})

configs["episodes"].append(\
{ "title": "bottlenecks on either side are avoided",\
"isChapter" : False,\
"audio" : {"timestamps" : ("14:20.5", "14:49.3" ), "volume" : 0.999 , "padding" : 0.25  },\
"video" : {"file": "breel_hd7770_attic.mp4", "start" : "00:10"}\
})


configs["episodes"].append(\
{ "title": "pricing",\
"isChapter" : False,\
"audio" : {"timestamps" : ("14:49.3", "15:14" ), "volume" : 0.999 , "padding" : 0.25  },\
"video" : {"file" : "breel_R7_260_and_260X.mp4"}\
})

configs["episodes"].append(\
{ "title": "olx searches",\
"isChapter" : False,\
"audio" : {"timestamps" : ("15:14", "15:36.5" ), "volume" : 0.999 , "padding" : 0.25  },\
"video" : {"file" : "r7_260x_and_260_OLX.mkv"}\
})


configs["episodes"].append(\
{ "title": "R7 260X",\
"isChapter" : False,\
"audio" : {"timestamps" : ("15:36.5", "15:57.5" ), "volume" : 0.999 , "padding" : 0.25  },\
"video" : {"file" : "r7_260x_breel_outside.mp4"} \
})

configs["episodes"].append(\
{ "title": "bye",\
"isChapter" : False,\
"audio" : {"timestamps" : ("15:57.5", "16:07" ), "volume" : 0.999 , "padding" : 0.25  },\
"video" : {"file" : "breel_r7_260_outside.mp4"} \
})

configs["episodes"].append(\
{ "title": "Blooper",\
"isChapter" : False,\
"audio" : {"timestamps" : ("16:07", "16:15.8" ), "volume" : 0.999 , "padding" : 0.25  },\
"video" : {"file": "breel_hd7770_attic.mp4", "start" : "00:18"}\
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

