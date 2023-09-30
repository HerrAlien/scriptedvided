import scriptedvided

configs = { "defaultAudioFile" : "r7_265_2023.ogg",\
"mediaFolder" : "F:\\Videos\\R7_265_2023", \
"stockFolder" : "F:\\Videos\\stock",\
"benchmarkFile" : "F:\\Videos\\R7_265_2023\\Benchmark_R7_265_2023.txt",\
"outputFolder" : "F:\\Videos\\R7_265_2023\\output", \
"outputFile" : "R7_265_2023.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3",\
"timestamps" : ("00:30", None ), "destinationTimestamp" : {"title" : "Reasons to revisit the R7 265", "until" : "Alien: Isolation"}}, \
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
"description" : '''In this video we're checking out the R7 265 (AKA R7 370. aka HD 7850). 
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

Our 2022 review of the R7 265: 

TechPowerup entry: https://www.techpowerup.com/gpu-specs/sapphire-dual-x-r7-265.b2749
''', \
"tags" : "AMD,ATI,Radeon,HD7850,HD 7850,R7 265,R7 370,Pitcairn,GCN,GCN1,GCN 1",\
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
{ "title": "Reasons to revisit the R7 265",\
"audio" : {"timestamps" : ("00:00", "00:11" ), "volume" : 0.999, "padding" : 0.25 },\
"video" : {"file": "breel_r7_265_outside.mp4"}\
})

configs["episodes"].append(\
{ "title": "Comparison card",\
"isChapter" : False, \
"audio" : {"timestamps" : ("00:11", "00:33" ), "volume" : 0.999, "padding" : 0.25 },\
"video" : {"file": "r7_260x_breel_outside.mp4"},\
"overlay" : { \
    "image" : {"file" : "comment_R7_370.png", "chromaColor" : "0x00FF00"}\
}, \
})

configs["episodes"].append(\
{ "title": "DX 12 support",\
"isChapter" : False, \
"audio" : {"timestamps" : ("00:33", "00:52" ), "volume" : 0.999, "padding" : 0.25 },\
"video" : {"file": "stock_re4demo_choppyExceptCutscenes.mp4", "start" : "03:07"}\
})

configs["episodes"].append(\
{ "title": "The GPU",\
"audio" : {"timestamps" : ("00:52", "01:10" ), "volume" : 0.999, "padding" : 0.25 },\
"video" : {"file" : "r7_265_GPUZ.mp4"}\
})

configs["episodes"].append(\
{ "title": "Cooling and thermals",\
"audio" : {"timestamps" : ("01:10", "01:24" ), "volume" : 0.999, "padding" : 0.25 },\
"video" : {"file": "r7_265_Heaven.mp4", "start" : "00:10"}\
})

configs["episodes"].append(\
{ "title": "The test system",\
"audio" : {"timestamps" : ("01:24", "01:39" ), "volume" : 0.999, "padding" : 0.25 },\
"video" : {"file" : "Z230_closed.mp4", "rotation" : 180}\
})

####################### end of intro ###############################



####################### gaming section ###############################
configs["episodes"].append(\
{ "title": "Alien: Isolation",\
"audio" : {"timestamps" : ("01:39", "02:13" ), "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, ultra settings", \
    }\
}, \
})

# this needs a longer stock video
configs["episodes"].append(\
{ "title": "Apex Legends",\
"audio" : {"timestamps" : ("02:13", "02:55" ), "padding" : 0.25  },\
"overlay" : { \
    "text" : ["'Apex Legends'",\
              scriptedvided.r6sText('1920x1080, low settings', 79, 51),\
              scriptedvided.r6sText('1600x900, low settings', 93,  62),\
              scriptedvided.r6sText('1280x720, low settings', 109, 72 ),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "CoD Warzone",\
"audio" : {"timestamps" : ("02:55", "03:22.5" ), "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Battlefield V",\
"audio" : {"timestamps" : ("03:22.5", "03:49.5" ), "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Control",\
"audio" : {"timestamps" : ("03:49.5", "04:20" ), "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Rainbow Six: Siege",\
"audio" : {"timestamps" : ("04:20", "05:03" ), "padding" : 0.25  },\
"overlay" : { \
    "text" : ["'Rainbow Six\: Siege'",\
              scriptedvided.r6sText('1920x1080, low settings, 100% render scale', 77, 53), \
              scriptedvided.r6sText('1280x720, low settings, 100% render scale', 117, 71),\
              scriptedvided.r6sText('1920x1080, low settings, 50% render scale', 76, 52),\
              scriptedvided.r6sText('1280x720, low settings, 50% render scale', 115, 70)]\
}, \
})

configs["episodes"].append(\
{ "title": "Grand Theft Auto V",\
"audio" : {"timestamps" : ("05:03", "05:32.3" ), "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Counter Strike: Global Offensive",\
"audio" : {"timestamps" : ("05:32.3", "06:15" ), "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "DOTA2",\
"audio" : {"timestamps" : ("06:15", "06:52.5" ), "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Fortnite",\
"audio" : {"timestamps" : ("06:52.5", "07:39" ), "padding" : 0.25  },\
"overlay" : { \
    "text" : ["'Fortnite'",\
              scriptedvided.r6sText('1920x1080, performance mode', 90, 60), \
              scriptedvided.r6sText('1600x900, performance mode', 94, 66),\
              scriptedvided.r6sText('1280x720, performance mode', 116, 71)]\
}, \
})


configs["episodes"].append(\
{ "title": "Overwatch 2",\
"audio" : {"timestamps" : ("07:39", "08:14" ), "padding" : 0.25  },\
"overlay" : { \
    "text" : ["'Overwatch 2'",\
              scriptedvided.r6sText('1920x1080, low settings', 136,  101),\
              scriptedvided.r6sText('1600x900, low settings', 186,  145),\
              scriptedvided.r6sText('1280x720, low settings', 260,  207),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "Rocket League",\
"audio" : {"timestamps" : ("08:14", "08:42" ), "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings, 100% render scale", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Splitgate",\
"audio" : {"timestamps" : ("08:42", "09:22" ), "padding" : 0.25  },\
"video" : "stock_Splitgate_2023_06_17.mp4",\
"overlay" : { \
    "text" : ["'Splitgate'",\
              scriptedvided.r6sText('1920x1080, low settings, 100% render scale', 106,  71),\
              scriptedvided.r6sText('1280x720, low settings, 100% render scale', 161, 104 ),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "Valorant",\
"audio" : {"timestamps" : ("09:22", "09:50" ), "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Genshin Impact",\
"audio" : {"timestamps" : ("09:50", "10:12.5" ), "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings, 1.0 render scale", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "HiRez Studios trio (Paladins, Realm Royale, Rogue Company)",\
"audio" : {"timestamps" : ("10:12.5", "10:23.3" ), "volume" : 0.999 , "padding" : 0.25  },\
"video" : {"file":"HiRezTrio-P_aladins_R_ealmRoyale_R_ogueCompany.mp4"}\
})

configs["episodes"].append(\
{ "title": "Paladins",\
"isChapter" : False,\
"audio" : {"timestamps" : ("10:23.3", "10:31.7" ), "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, high settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Realm Royale",\
"isChapter" : False,\
"audio" : {"timestamps" : ("10:31.7", "10:40.5" ), "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, high settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Rogue Company",\
"isChapter" : False,\
"audio" : {"timestamps" : ("10:40.5", "10:48" ), "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})


configs["episodes"].append(\
{ "title": "HiRez Studios conclusions",\
"audio" : {"timestamps" : ("10:48", "11:09.4" ), "volume" : 0.999 , "padding" : 0.25  },\
"isChapter" : False,\
"video" : {"file":"HiRezTrio-P_aladins_R_ealmRoyale_R_ogueCompany.mp4"}\
})


configs["episodes"].append(\
{ "title": "World of Tanks Blitz",\
"audio" : {"timestamps" : ("11:09.4", "11:34" ), "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, high settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Warframe",\
"audio" : {"timestamps" : ("11:34", "12:25" ), "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
"video" : "stock_Warframe_Mariana.mp4",\
})

configs["episodes"].append(\
{ "title": "Resident Evil 4 (Remake)",\
"audio" : {"timestamps" : ("12:25", "12:46" ), "padding" : 0.25  },\
"video" : {"file": "stock_re4demo_choppyExceptCutscenes.mp4", "start" : "03:07"},\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Resident Evil 4 - data",\
"isChapter" : False,\
"audio" : {"timestamps" : ("12:46", "13:12" ), "padding" : 0.25  },\
"video" : {"file": "stock_re4demo_phoneCall.mp4"},\
"overlay" : { \
    "image" : {"file" : "re4_260x_265.png", "chromaColor" : "0x00FF00"}\
}, \
})
####################### end of gaming section ###############################


####################### conclusion ###############################

configs["episodes"].append(\
{ "title": "Conclusions",\
"audio" : {"timestamps" : ("13:12", "13:29" ), "volume" : 0.999 , "padding" : 0.25  },\
"video" : {"file" : "R7_260x_vs_265.mp4"}\
})

configs["episodes"].append(\
{ "title": "260x for me",\
"isChapter" : False,\
"audio" : {"timestamps" : ("13:29", "13:46" ), "volume" : 0.999 , "padding" : 0.25  },\
"video" : {"file" : "r7_260x_breel_outside.mp4", "start": "00:00"}\
})

configs["episodes"].append(\
{ "title": "265 fine too",\
"isChapter" : False,\
"audio" : {"timestamps" : ("13:46", "14:08" ), "volume" : 0.999 , "padding" : 0.25  },\
"video" : {"file" : "breel_r7_265_outside.mp4", "start": "00:00"}\
})


configs["episodes"].append(\
{ "title": "R9 270",\
"isChapter" : False,\
"audio" : {"timestamps" : ("14:08", "14:18.5" ), "volume" : 0.999 , "padding" : 0.25  },\
"video" : {"file" : "breel_r7_265_270_outside.mp4"}\
})

configs["episodes"].append(\
{ "title": "bye",\
"isChapter" : False,\
"audio" : {"timestamps" : ("14:18.5", "14:26" ), "volume" : 0.999 , "padding" : 0.25  },\
"video" : {"file" : "breel_r7_265_outside.mp4"}\
})


##configs["episodes"].append(\
##{ "title": "Blooper",\
##"isChapter" : False,\
##"audio" : {"timestamps" : ( "13:40.5", "14:04.2") },\
##"video" : {"file":"HiRezTrio-P_aladins_R_ealmRoyale_R_ogueCompany.mp4"}\
##})

#scriptedvided.makeVideoForEpisode(configs["episodes"][27], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][29], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][30], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][31], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][32], configs)
#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "Splitgate"][0], configs)
scriptedvided.makeVideo(configs)

