import scriptedvided

configs = { "defaultAudioFile" : "R9_270.ogg",\
"mediaFolder" : "F:\\Videos\\R9 270", \
"stockFolder" : "F:\\Videos\\stock",\
"benchmarkFile" : "F:\\Videos\\R9 270\\Benchmark_R9_270.txt",\
"outputFolder" : "F:\\Videos\\R9 270\\output", \
"outputFile" : "R9_270.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3",\
"timestamps" : ("00:30", None ), "destinationTimestamp" : {"title" : "R9 270 joins the match", "until" : "Alien: Isolation"}}, \
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
"description" : '''In this video we're checking out the R9 270; the chip was a refresh of the HD 7870, and would end up used again in R9 270X and R9 370. 
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

TechPowerup entry: https://www.techpowerup.com/gpu-specs/radeon-r9-270.c2458
''', \
"tags" : "AMD,ATI,Radeon,HD7870,HD 7870,R9 270,R9 270X,R9 370,Curacao,Trinidad,Pitcairn,GCN,GCN1,GCN 1",\
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
{ "title": "R9 270 joins the match",\
"audio" : {"timestamps" : ("00:00", "00:14" ), "volume" : 0.999, "padding" : 0.25 },\
"video" : {"file": "breel_r9_270_outside.mp4"}\
})

configs["episodes"].append(\
{ "title": "The GPU",\
"audio" : {"timestamps" : ("00:14", "00:31.5" ), "volume" : 0.999, "padding" : 0.25 },\
"video" : {"file": "broll_R9_270_HPPN.mp4", "start" : "00:00"},\
})

configs["episodes"].append(\
{ "title": "GPUZ",\
"isChapter" : False, \
"audio" : {"timestamps" : ("00:31.5", "00:59" ), "volume" : 0.999, "padding" : 0.25 },\
"video" : {"file": "r9_270_heaven_950MHz.mp4", "start" : "00:00"}\
})

configs["episodes"].append(\
{ "title": "Boosts 920",\
"isChapter" : False, \
"audio" : {"timestamps" : ("00:59", "01:17" ), "volume" : 0.999, "padding" : 0.25 },\
"video" : {"file": "r9_270_GPUZ.mp4", "start" : "00:00"}\
})

configs["episodes"].append(\
{ "title": "Cooling and thermals",\
"audio" : {"timestamps" : ("01:17", "01:28.5" ), "volume" : 0.999, "padding" : 0.25 },\
"video" : {"file": "r9_270_coolerMounted.mp4", "start" : "00:00"}\
})

configs["episodes"].append(\
{ "title": "Thermals",\
"isChapter" : False, \
"audio" : {"timestamps" : ("01:28.5", "01:46" ), "volume" : 0.999, "padding" : 0.25 },\
"overlay" : { \
    "text" : ["'Thermals'",\
              "'Heaven\: 73C (49C delta over ambient)'",\
              "'Warframe\: 74C (50C delta over ambient)'",\
    ]\
}, \
"video" : {"file": "stock_heaven720p_noTessellation.mp4", "start" : "00:00"}\
})

configs["episodes"].append(\
{ "title": "The test system",\
"audio" : {"timestamps" : ("01:46", "02:08.5" ), "volume" : 0.999, "padding" : 0.25 },\
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
"audio" : {"timestamps" : ("02:08.5", "02:34" ), "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, ultra settings", \
    }\
}, \
})

# this needs a longer stock video
configs["episodes"].append(\
{ "title": "Apex Legends",\
"audio" : {"timestamps" : ("02:34", "03:09" ), "padding" : 0.25  },\
"overlay" : { \
    "text" : ["'Apex Legends'",\
              scriptedvided.r6sText('1920x1080, low settings', 73, 51),\
              scriptedvided.r6sText('1600x900, low settings', 90,  61),\
              scriptedvided.r6sText('1280x720, low settings', 108, 75 ),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "CoD Warzone",\
"audio" : {"timestamps" : ("03:09", "03:34" ), "padding" : 0.25  },\
"overlay" : { \
    "image" : {"file" : "warzone.png", "chromaColor" : "0x00FF00"}\
}, \
})

configs["episodes"].append(\
{ "title": "PUBG",\
"audio" : {"timestamps" : ("03:34", "04:00" ), "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
},
})

configs["episodes"].append(\
{ "title": "Battlefield V",\
"audio" : {"timestamps" : ("04:00", "04:33.5" ), "padding" : 0.25  },\
"overlay" : { \
    "text" : ["'Battlefield V'",\
              scriptedvided.r6sText('1920x1080, low settings', 53, 43),\
              scriptedvided.r6sText('1600x900, low settings', 66,  53),\
              scriptedvided.r6sText('1280x720, low settings', 81, 60 ),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "Control",\
"audio" : {"timestamps" : ("04:33.5", "04:40.2" ), "padding" : 0.25 },\
"video" : {"file" : "C_ontrol_tamingTheSphere.mp4" , "start" : "00:35"},\
})

configs["episodes"].append(\
{ "title": "cricket",\
"isChapter" : False, \
"audio" : {"timestamps" : ("00:00", "00:02" ), "padding" : 0.25 , "volume" : 0.001  },\
"video" : "cricket-noise-sound-effects.mp4"
})


configs["episodes"].append(\
{ "title": "Control - fps",\
"isChapter" : False, \
"audio" : {"timestamps" : ("04:40.2", "05:01.7"), "padding" : 0.25  },\
"overlay" : { \
    "text" : ["'Control'",\
              scriptedvided.r6sText('1920x1080, low settings', 39, 32),\
              scriptedvided.r6sText('1280x720, low settings', 83, 60 ),\
    ]\
}, \
"video" : {"file" : "stock_Control_R9_270.mp4", "start" : "01:53"},\
})

configs["episodes"].append(\
{ "title": "Rainbow Six: Siege",\
"audio" : {"timestamps" : ("05:01.7", "05:44.6"), "padding" : 0.25  },\
"overlay" : { \
    "text" : ["'Rainbow Six\: Siege'",\
              scriptedvided.r6sText('1920x1080, low settings, 100% render scale', 70, 58), \
              scriptedvided.r6sText('1280x720, low settings, 100% render scale', 133, 88),\
              scriptedvided.r6sText('1920x1080, low settings, 50% render scale', 101, 76),\
              scriptedvided.r6sText('1280x720, low settings, 50% render scale', 171, 102)]\
}, \
})

configs["episodes"].append(\
{ "title": "Grand Theft Auto V",\
"audio" : {"timestamps" : ("05:44.6", "06:13"), "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "CS2",\
"audio" : {"timestamps" : ("06:13", "06:45"), "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "DOTA2",\
"audio" : {"timestamps" : ("06:45", "07:09"), "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Fortnite",\
"audio" : {"timestamps" : ("07:09", "07:46"), "padding" : 0.25  },\
"overlay" : { \
    "text" : ["'Fortnite'",\
              scriptedvided.r6sText('1920x1080, performance mode', 95, 59), \
              scriptedvided.r6sText('1600x900, performance mode', 107, 62),\
              scriptedvided.r6sText('1280x720, performance mode', 131, 58)]\
}, \
})


configs["episodes"].append(\
{ "title": "Overwatch 2",\
"audio" : {"timestamps" : ("07:46", "08:21"), "padding" : 0.25  },\
"overlay" : { \
    "text" : ["'Overwatch 2'",\
              scriptedvided.r6sText('1920x1080, low settings', 107,  76),\
              scriptedvided.r6sText('1600x900, low settings', 147,  105),\
              scriptedvided.r6sText('1280x720, low settings', 215,  159),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "Rocket League",\
"audio" : {"timestamps" : ("08:21", "08:37.5"), "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings, 100% render scale", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Splitgate",\
"audio" : {"timestamps" : ("08:37.5", "09:19.5"), "padding" : 0.25  },\
"video" : "stock_Splitgate_2023_06_17.mp4",\
"overlay" : { \
    "text" : ["'Splitgate'",\
              scriptedvided.r6sText('1920x1080, low settings, 100% render scale', 105,  75),\
              scriptedvided.r6sText('1280x720, low settings, 100% render scale', 171, 112 ),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "Valorant",\
"audio" : {"timestamps" : ("09:19.5", "09:47"), "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Genshin Impact",\
"audio" : {"timestamps" : ("09:47", "10:41.5"), "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings, 1.0 render scale", \
    }\
}, \
"video" : "updatting_GI_2.mp4",\
})

configs["episodes"].append(\
{ "title": "HiRez Studios trio (Paladins, Realm Royale, Rogue Company)",\
"audio" : {"timestamps" : ("10:41.5", "10:56" ), "volume" : 0.999 , "padding" : 0.25  },\
"video" : {"file":"HiRezTrio-P_aladins_R_ealmRoyale_R_ogueCompany.mp4"}\
})

configs["episodes"].append(\
{ "title": "Paladins",\
"isChapter" : False,\
"audio" : {"timestamps" : ("10:56", "11:03.4"), "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, high settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Realm Royale",\
"isChapter" : False,\
"audio" : {"timestamps" : ("11:03.4", "11:11.75"), "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, high settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Rogue Company",\
"isChapter" : False,\
"audio" : {"timestamps" : ("11:11.75", "11:20"), "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "World of Tanks Blitz",\
"audio" : {"timestamps" : ("11:20", "11:40"), "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, high settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Warframe",\
"audio" : {"timestamps" : ("11:40", "12:09"), "padding" : 0.25  },\
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
"audio" : {"timestamps" : ("12:09", "12:35" ), "volume" : 0.999 , "padding" : 0.25  },\
"video" : {"file" : "broll_R9_270_HPPN.mp4", "start" : "00:35"}\
})

configs["episodes"].append(\
{ "title": "pricing",\
"isChapter" : False,\
"audio" : {"timestamps" : ("12:35", "12:52" ), "volume" : 0.999 , "padding" : 0.25  },\
"video" : {"file" : "breel_r9_270_outside.mp4", "start": "00:00"}\
})

configs["episodes"].append(\
{ "title": "R9 280",\
"isChapter" : False,\
"audio" : {"timestamps" : ("12:52", "13:03" ), "volume" : 0.999 , "padding" : 0.25  },\
"video" : {"file" : "breel_r9_280_outside.mp4"}\
})

configs["episodes"].append(\
{ "title": "bye",\
"isChapter" : False,\
"audio" : {"timestamps" : ("13:03", "13:09" ), "volume" : 0.999 , "padding" : 0.25  },\
"video" : {"file": "broll_R9_270_HPPN.mp4", "start" : "00:00"},\
})

configs["episodes"].append(\
{ "title": "Blooper",\
"isChapter" : False,\
"audio" : {"timestamps" : ("13:09", "13:18" ), "volume" : 0.999 , "padding" : 0.25  },\
"video" : {"file": "breel_r9_270_outside.mp4", "start" : "00:00"},\
})

##configs["episodes"].append(\
##{ "title": "Blooper",\
##"isChapter" : False,\
##"audio" : {"timestamps" : ( "13:40.5", "14:04.2") },\
##"video" : {"file":"HiRezTrio-P_aladins_R_ealmRoyale_R_ogueCompany.mp4"}\
##})

#scriptedvided.makeVideoForEpisode(configs["episodes"][8], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][10], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][30], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][31], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][32], configs)
#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "Splitgate"][0], configs)
scriptedvided.makeVideo(configs)

