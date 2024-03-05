import scriptedvided

configs = { "defaultAudioFile" : "hd5870_2023.ogg",\
"mediaFolder" : "F:\\Videos\\hd5870_2023", \
"stockFolder" : "F:\\Videos\\stock",\
"benchmarkFile" : "F:\\Videos\\hd5870_2023\\Benchmark_hd5870_2023.txt",\
"outputFolder" : "F:\\Videos\\hd5870_2023\\output", \
"outputFile" : "hd5870_2023.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3",\
"timestamps" : ("00:30", None ), "destinationTimestamp" : {"title" : "Can a 2009 flagship still game?", "until" : "Alien: Isolation"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3",\
"timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Alien: Isolation", "until" : "Control"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3",\
"timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Control", "until" : "Rocket League"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3",\
"timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Rocket League", "until" : "Usefulness of an old (D)GPU"}}, \
{"file" : "Guide You Home - Ferco and Andie - Free Background Music - Audio Library Release.ogg", "timestamps" : ("00:20", None ), "destinationTimestamp" : { "title": "Usefulness of an old (D)GPU", "until" : "Blooper" }}, \
], "volume" : 0.05 },\
"episodes" : [],\
"youtube" : {"title" : "Testing the older AMD Radeon HD 6850 in popular games (2023)", \
"description" : '''In this video, we’ll take a second look at the performance of the 2009 flagship from AMD - the HD 5870.
''',\
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

Our review of the HD 5870 from a year ago (2022): https://youtu.be/RGXJdRJkStE

Iceberg Tech's review of UHD 730: https://www.youtube.com/watch?v=5xvRPxVMQ1k

TechPowerup entry: https://www.techpowerup.com/gpu-specs/radeon-hd-5870.c253
''', \
"tags" : "AMD,ATI,Radeon,HD5870,HD 5870,TeraScale 2",\
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
{ "title": "Can a 2009 flagship still game?",\
"audio" : {"timestamps" : ("00:00", "00:09.5" ), "volume" : 0.999, "padding" : 0.25 },\
"video" : "4090_launch.mp4"\
})

configs["episodes"].append(\
{ "title": "XFX HD 5870",\
"isChapter" : False, \
"audio" : {"timestamps" : ("00:09.5", "00:25" ), "volume" : 0.999, "padding" : 0.25 },\
"video" : {"file" : "broll_hd5870_outside.mp4"}\
})

configs["episodes"].append(\
{ "title": "Test system",\
"audio" : {"timestamps" : ("00:25" , "00:37"), "volume" : 0.999, "padding" : 0.25 },\
"video" : {"file" : "z230_inside_shot.mov", "rotation" : 180}\
})

configs["episodes"].append(\
{ "title": "The GPU",\
"audio" : {"timestamps" : ("00:37", "00:57" ), "volume" : 0.999, "padding" : 0.25 },\
"video" : "hd5870_idle_gpuz.mkv"\
})


configs["episodes"].append(\
{ "title": "(very brief) Cooling and thermals",\
"audio" : {"timestamps" : ("00:57", "01:14"), "volume" : 0.999, "padding" : 0.25 },\
"video" : {"file" : "hd5870_cooling.mp4", "start" : "00:00"}\
})

####################### end of intro ###############################




####################### gaming section ###############################
configs["episodes"].append(\
{ "title": "Alien: Isolation",\
"audio" : {"timestamps" : ("01:14","01:33") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, ultra settings", \
    }\
}, \
"video" : "stock_Alien_Isolation_1080p.mp4"\
})


configs["episodes"].append(\
{ "title": "Apex Legends",\
"audio" : {"timestamps" : ("01:33", "02:09" )  },\
"overlay" : { \
    "text" : ["'Apex Legends'",\
              scriptedvided.r6sText('1920x1080, low settings', 41, 10), \
              scriptedvided.r6sText('1280x720, low settings', 54, 39)],\
},\
})

configs["episodes"].append(\
{ "title": "CoD Warzone",\
"audio" : {"timestamps" : ("02:09", "02:21" )  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
}, \
"video" : "TeraScale2_vs_W_arzone_2.mkv"\
})

configs["episodes"].append(\
{ "title": "Battlefield V",\
"audio" : {"timestamps" : ("02:21", "02:45" ) },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
}, \
"video" : "stock_bfv_tobruk_720pLow.mp4",\
})

configs["episodes"].append(\
{ "title": "Control",\
"audio" : {"timestamps" : ("02:45", "03:06") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Rainbow Six: Siege",\
"audio" : {"timestamps" : ("03:06", "03:37") },\
"overlay" : { \
    "text" : ["'Rainbow Six\: Siege'",\
              scriptedvided.r6sText('1920x1080, low settings, 100% render scale', 38, 25), \
              scriptedvided.r6sText('1280x720, low settings, 100% render scale', 55, 31),\
              scriptedvided.r6sText('1920x1080, low settings, 50% render scale', 50, 30),\
              scriptedvided.r6sText('1280x720, low settings, 50% render scale', 66, 34)]\
}, \
})

configs["episodes"].append(\
{ "title": "Grand Theft Auto V",\
"audio" : {"timestamps" : ("03:37",  "03:58") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Counter Strike: Global Offensive",\
"audio" : {"timestamps" : ( "03:58" , "04:21.5" ) },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "DOTA2",\
"audio" : {"timestamps" : ("04:21.5", "04:47") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings, 100% render scale", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Fortnite",\
"audio" : {"timestamps" : ("04:47", "05:16") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, performance mode, view distance FAR, 100% render scale", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Overwatch 2",\
"audio" : {"timestamps" : ( "05:16", "05:33") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings, 100% render scale", \
    }\
}, \
"video" : "stock_Overwatch2_gameplay_5770.mp4"
})

configs["episodes"].append(\
{ "title": "Rocket League",\
"audio" : {"timestamps" : ("05:33", "05:59") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings, 100% render scale", \
    }\
}, \
"video" : "stock_RocketLeague_1080pLower.mp4",\
})

configs["episodes"].append(\
{ "title": "Splitgate",\
"audio" : {"timestamps" : ("05:59", "06:24") },\
"overlay" : { \
    "text" : ["'Splitgate'",\
              scriptedvided.r6sText('1920x1080, low settings, 100% render scale',80, 43),\
              scriptedvided.r6sText('1280x720, low settings, 100% render scale',139, 81),\
    ]\
}, \
"video" : "stock_Splitgate_1080pLow.mp4",\
})

configs["episodes"].append(\
{ "title": "Valorant",\
"audio" : {"timestamps" : ("06:24", "06:42") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Genshin Impact",\
"audio" : {"timestamps" : ("06:42", "07:11") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings, 1.0 render scale", \
    }\
}, \
})


configs["episodes"].append(\
{ "title": "HiRez Studios trio (Paladins, Realm Royale, Rogue Company)",\
"audio" : {"timestamps" : ("07:11", "07:27.4" ), "volume" : 0.999, "padding" : 0.25 },\
"video" : {"file":"HiRezTrio-P_aladins_R_ealmRoyale_R_ogueCompany.mp4"}\
})



configs["episodes"].append(\
{ "title": "Paladins",\
"isChapter" : False,\
"audio" : {"timestamps" : ("07:27.4", "07:34.3") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, high settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Realm Royale",\
"isChapter" : False,\
"audio" : {"timestamps" : ("07:34.3", "07:43") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, high settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Rogue Company",\
"isChapter" : False,\
"audio" : {"timestamps" : ("07:43", "07:50") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "World of Tanks Blitz",\
"audio" : {"timestamps" : ("07:50", "08:11") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, high settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Warframe",\
"audio" : {"timestamps" : ("08:11", "08:34") },\
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
"audio" : {"timestamps" : ("00:00", "01:13"), "volume" : 0.001 },\
"video" : "dgpu_over_igpu.mp4"\
})
###########################

configs["episodes"].append(\
{ "title": "Is the HD 5870 worth it?",\
"audio" : {"timestamps" : ( "08:34", "08:51"), "volume" : 0.999 },\
"video" : {"file" : "hd5870_breel_4tnite_2.mp4", "start":"00:14"}\
})

configs["episodes"].append(\
{ "title": "Pricing",\
"isChapter" : False,\
"audio" : {"timestamps" : ( "08:51", "09:14.4"), "volume" : 0.999, "padding" : 0.25  },\
"video" : {"file" : "pricing_hd5870.mkv"} \
})

configs["episodes"].append(\
{ "title": "Competition - HD 7770",\
"isChapter" : False,\
"audio" : {"timestamps" : ( "09:14.4", "09:28"), "volume" : 0.999, "padding" : 0.25  },\
"video" : {"file" : "hd7770_20USD.mkv"} \
})

configs["episodes"].append(\
{ "title": "6670 hint",\
"isChapter" : False,\
"audio" : {"timestamps" : ("09:28", "09:49"), "volume" : 0.999, "padding" : 0.25  },\
"video" : {"file" : "broll_ts2family_outside.mp4"} \
})

configs["episodes"].append(\
{ "title": "Blooper",\
"isChapter" : False,\
"audio" : {"timestamps" : ("09:49", "09:59"), "volume" : 0.999, "padding" : 0.25  },\
"video" : {"file" : "hd5870_breel_R_e_a_l_m.mp4", "start":"00:20"} \
})


##configs["episodes"].append(\
##{ "title": "Blooper",\
##"isChapter" : False,\
##"audio" : {"timestamps" : ( "13:40.5", "14:04.2") },\
##"video" : {"file":"HiRezTrio-P_aladins_R_ealmRoyale_R_ogueCompany.mp4"}\
##})

#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "Alien: Isolation"][0], configs)
scriptedvided.makeVideo(configs)

