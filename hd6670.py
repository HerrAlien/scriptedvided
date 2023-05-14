import scriptedvided

configs = { "defaultAudioFile" : "hd6670.ogg",\
"mediaFolder" : "F:\\Videos\\hd6670", \
"stockFolder" : "F:\\Videos\\stock",\
"benchmarkFile" : "F:\\Videos\\hd6670\\Benchmark_hd6670_ref.txt",\
"outputFolder" : "F:\\Videos\\hd6670\\output", \
"outputFile" : "hd6670.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3",\
"timestamps" : ("00:30", None ), "destinationTimestamp" : {"title" : "The 720p budget card", "until" : "Alien: Isolation"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3",\
"timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Alien: Isolation", "until" : "DOTA2"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3",\
"timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "DOTA2", "until" : "Genshin Impact"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3",\
"timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Genshin Impact", "until" : "Usefulness of an old (D)GPU"}}, \
{"file" : "Guide You Home - Ferco and Andie - Free Background Music - Audio Library Release.ogg", "timestamps" : ("00:20", None ), "destinationTimestamp" : { "title": "Usefulness of an old (D)GPU", "until" : "Blooper" }}, \
], "volume" : 0.05 },\
"episodes" : [],\
"youtube" : {"title" : "How does  a budget video card from 2009 play games in 2023?", \
"description" : '''In this video we're reviewing a TeraScale 2 budget card - the HD 6670.''',\
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

TechPowerup entry: https://www.techpowerup.com/gpu-specs/radeon-hd-6670.c406
''', \
"tags" : "AMD,ATI,Radeon,HD6670,HD 6670,TeraScale 2",\
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
{ "title": "The 720p budget card",\
"audio" : {"timestamps" : ("00:00", "00:18" ), "volume" : 0.999, "padding" : 0.25 },\
"video" : "hd6670_usable_standing_2.mp4"\
})

configs["episodes"].append(\
{ "title": "The GPU",\
"audio" : {"timestamps" : ("00:18", "00:58" ), "volume" : 0.999, "padding" : 0.25 },\
"video" : {"file" : "hd6670_techpowerup.mkv"}\
})

configs["episodes"].append(\
{ "title": "Test system",\
"audio" : {"timestamps" : ("00:58" , "01:28"), "volume" : 0.999, "padding" : 0.25 },\
"video" : {"file" : "Z230_closed.mp4", "rotation" : 180}\
})

configs["episodes"].append(\
{ "title": "Cooling and thermals",\
"audio" : {"timestamps" : ("01:28" , "01:47.6"), "volume" : 0.999, "padding" : 0.25 },\
"video" : "hd6670_usable_cooling.mp4"\
})

configs["episodes"].append(\
{ "title": "Heatsinks",\
"isChapter" : False, \
"audio" : {"timestamps" : ("01:47.6", "02:03"), "volume" : 0.999, "padding" : 0.25 },\
"video" : "heatsinks.mkv"\
})

configs["episodes"].append(\
{ "title": "Thermals",\
"isChapter" : False, \
"audio" : {"timestamps" : ("02:03", "02:22"), "volume" : 0.999, "padding" : 0.25 },\
"video" : "hd6670_Heaven.mp4"\
})

####################### end of intro ###############################




####################### gaming section ###############################
configs["episodes"].append(\
{ "title": "Alien: Isolation",\
"audio" : {"timestamps" : ("02:22","03:03") },\
"overlay" : { \
    "text" : ["'Alien\: Isolation'",\
              scriptedvided.r6sText('1920x1080, ultra settings', 26, 18 ),\
              scriptedvided.r6sText('1280x720, ultra settings', 45, 32 ),\
    ]\
}, \
"video" : "stock_Alien_Isolation_1080p.mp4"\
})


configs["episodes"].append(\
{ "title": "Apex Legends",\
"audio" : {"timestamps" : ("03:03", "03:29" )  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "CoD Warzone",\
"audio" : {"timestamps" : ("03:29", "03:49" )  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
}, \
"video" : "TeraScale2_vs_W_arzone_2.mkv"\
})

configs["episodes"].append(\
{ "title": "Battlefield V",\
"audio" : {"timestamps" : ("03:49", "04:11" ) },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
}, \
"video" : "stock_bfv_tobruk_720pLow.mp4",\
})

configs["episodes"].append(\
{ "title": "Control",\
"audio" : {"timestamps" : ("04:11", "04:35") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Rainbow Six: Siege",\
"audio" : {"timestamps" : ("04:35", "04:56.5") },\
"overlay" : { \
    "text" : ["'Rainbow Six\: Siege'",\
              scriptedvided.r6sText('1920x1080, low settings, 100% render scale', 15, 11), \
              scriptedvided.r6sText('1280x720, low settings, 100% render scale', 28, 18),\
              scriptedvided.r6sText('1920x1080, low settings, 50% render scale', 21, 14),\
              scriptedvided.r6sText('1280x720, low settings, 50% render scale', 32, 17)]\
}, \
})

configs["episodes"].append(\
{ "title": "Grand Theft Auto V",\
"audio" : {"timestamps" : ("04:56.5",  "05:18") },\
"overlay" : { \
    "text" : ["'Grand Theft Auto V'",\
              scriptedvided.r6sText('1920x1080, low settings', 34,  22),\
              scriptedvided.r6sText('1280x720, low settings', 49,  28),\
    ]\
}, \
"video" : "stock_gta5_1080p.mp4" \
})

configs["episodes"].append(\
{ "title": "Counter Strike: Global Offensive",\
"audio" : {"timestamps" : ( "05:18" , "05:44" ) },\
"overlay" : { \
    "text" : ["'Counter Strike\: Global Offensive'",\
              scriptedvided.r6sText('1920x1080, low settings', 67,  31),\
              scriptedvided.r6sText('1280x720, low settings', 84, 54),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "DOTA2",\
"audio" : {"timestamps" : ("05:44", "06:19") },\
"overlay" : { \
    "text" : ["'DOTA 2'",\
              scriptedvided.r6sText('1920x1080, low settings', 48, 35 ),\
              scriptedvided.r6sText('1280x720, low settings', 78, 52),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "Fortnite",\
"audio" : {"timestamps" : ("06:19", "06:54") },\
"overlay" : { \
    "text" : ["'Fortnite'",\
              scriptedvided.r6sText('1920x1080, low settings', 41, 26 ),\
              scriptedvided.r6sText('1280x720, low settings', 66,  47),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "Overwatch 2",\
"audio" : {"timestamps" : ( "06:54", "07:21") },\
"overlay" : { \
    "text" : ["'Overwatch 2'",\
              scriptedvided.r6sText('1920x1080, low settings', 37,  29),\
              scriptedvided.r6sText('1280x720, low settings', 71,  57),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "Rocket League",\
"audio" : {"timestamps" : ("07:21", "07:51") },\
"overlay" : { \
    "text" : ["'Rocket League'",\
              scriptedvided.r6sText('1920x1080, low settings', 53,  22),\
              scriptedvided.r6sText('1280x720, low settings', 65, 28 ),\
    ]\
}, \
"video" : "stock_RocketLeague_1080pLower.mp4",\
})

configs["episodes"].append(\
{ "title": "Splitgate",\
"audio" : {"timestamps" : ("07:51", "08:24") },\
"overlay" : { \
    "text" : ["'Splitgate'",\
              scriptedvided.r6sText('1920x1080, low settings, 100% render scale', 30,  15),\
              scriptedvided.r6sText('1280x720, low settings, 100% render scale', 55,  28),\
    ]\
}, \
"video" : "stock_Splitgate_1080pLow.mp4",\
})

configs["episodes"].append(\
{ "title": "Valorant",\
"audio" : {"timestamps" : ("08:24", "09:04") },\
"overlay" : { \
    "text" : ["'Valorant'",\
              scriptedvided.r6sText('1920x1080, low settings', 80,  0),\
              scriptedvided.r6sText('1280x720, low settings', 140,  0),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "Genshin Impact",\
"audio" : {"timestamps" : ("09:04", "09:28") },\
"overlay" : { \
    "text" : ["'Genshin Impact'",\
              scriptedvided.r6sText('1920x1080, low settings, 1.0 render scale', 18,  16),\
              scriptedvided.r6sText('1280x720, low settings, 1.0 render scale', 24,  19),\
    ]\
}, \
})


configs["episodes"].append(\
{ "title": "HiRez Studios trio (Paladins, Realm Royale, Rogue Company)",\
"audio" : {"timestamps" : ("09:28", "09:45" ), "volume" : 0.999, "padding" : 0.25 },\
"video" : {"file":"HiRezTrio-P_aladins_R_ealmRoyale_R_ogueCompany.mp4"}\
})



configs["episodes"].append(\
{ "title": "Paladins",\
"isChapter" : False,\
"audio" : {"timestamps" : ("09:45", "10:04") },\
"overlay" : { \
    "text" : ["'Paladins'",\
              scriptedvided.r6sText('1920x1080, high settings', 70,  25),\
              scriptedvided.r6sText('1280x720, high settings', 93,  52),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "Realm Royale",\
"isChapter" : False,\
"audio" : {"timestamps" : ("10:04", "10:21") },\
"overlay" : { \
    "text" : ["'Realm Royale'",\
              scriptedvided.r6sText('1920x1080, high settings', 46,  29),\
              scriptedvided.r6sText('1280x720, high settings', 61,  39),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "Rogue Company",\
"isChapter" : False,\
"audio" : {"timestamps" : ("10:21", "10:45") },\
"overlay" : { \
    "text" : ["'Rogue Company'",\
              scriptedvided.r6sText('1920x1080, low settings', 41,  20),\
              scriptedvided.r6sText('1280x720, low settings', 69, 43 ),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "World of Tanks Blitz",\
"audio" : {"timestamps" : ("10:45", "11:04") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, high settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Warframe",\
"audio" : {"timestamps" : ("11:04", "11:48") },\
"overlay" : { \
    "text" : ["'Warframe'",\
              scriptedvided.r6sText('1920x1080, low settings', 80,  43),\
              scriptedvided.r6sText('1280x720, low settings', 150,  69),\
    ]\
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
{ "title": "Is the HD 6670 worth it?",\
"audio" : {"timestamps" : ( "11:48", "12:12.5"), "volume" : 0.999 },\
"video" : {"file" : "hd6670_olx_ad.mkv"}\
})

configs["episodes"].append(\
{ "title": "GT 730 drivers",\
"isChapter" : False,\
"audio" : {"timestamps" : ( "12:12.5", "12:38"), "volume" : 0.999, "padding" : 0.25  },\
"video" : {"file" : "GF108_install_kepler_driver.mkv", "start" : "00:40"} \
})

configs["episodes"].append(\
{ "title": "Pricing",\
"isChapter" : False,\
"audio" : {"timestamps" : ( "12:38", "13:06.5"), "volume" : 0.999, "padding" : 0.25  },\
"video" : {"file" : "6670 prices.mkv"} \
})

configs["episodes"].append(\
{ "title": "Performance",\
"isChapter" : False,\
"audio" : {"timestamps" : ("13:06.5", "13:22.5"), "volume" : 0.999, "padding" : 0.25  },\
"video" : {"file" : "relative_performance_730_6670.mkv"} \
})

configs["episodes"].append(\
{ "title": "GT730 close to 6670",\
"isChapter" : False,\
"audio" : {"timestamps" : ("13:22.5", "13:34.8"), "volume" : 0.999, "padding" : 0.25  },\
"video" : {"file" : "gt730_hd6670.mp4"} \
})

configs["episodes"].append(\
{ "title": "It just works",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:00", "00:05"), "volume" : 0.001, "padding" : 0.5  },\
"video" : {"file" : "just works.mp4", "start" : "00:25"} \
})

configs["episodes"].append(\
{ "title": "list of games 730",\
"isChapter" : False,\
"audio" : {"timestamps" : ("13:40", "13:53.5"), "volume" : 0.999, "padding" : 0.25  },\
"video" : {"file" : "730_games.mkv", "start" :"00:10"} \
})

configs["episodes"].append(\
{ "title": "6670 better",\
"isChapter" : False,\
"audio" : {"timestamps" : ("13:53.5", "14:06"), "volume" : 0.999, "padding" : 0.25  },\
"video" : {"file" : "broll_hd6670_horizontal.mp4"} \
})

configs["episodes"].append(\
{ "title": "R7 250",\
"isChapter" : False,\
"audio" : {"timestamps" : ("14:06", "14:14"), "volume" : 0.999, "padding" : 0.25  },\
"video" : {"file" : "r7_250.mp4"} \
})

configs["episodes"].append(\
{ "title": "bye",\
"isChapter" : False,\
"audio" : {"timestamps" : ( "14:14", "14:21"), "volume" : 0.999, "padding" : 1  },\
"video" : {"file" : "broll_hd6670_horizontal.mp4", "rotation" : 180} \
})

configs["episodes"].append(\
{ "title": "Blooper",\
"isChapter" : False,\
"audio" : {"timestamps" : ("14:21", "14:32.6"), "volume" : 0.999, "padding" : 0.25  },\
"video" : {"file" : "V_alorant_720p.mp4"} \
})


##configs["episodes"].append(\
##{ "title": "Blooper",\
##"isChapter" : False,\
##"audio" : {"timestamps" : ( "13:40.5", "14:04.2") },\
##"video" : {"file":"HiRezTrio-P_aladins_R_ealmRoyale_R_ogueCompany.mp4"}\
##})

#scriptedvided.makeVideoForEpisode(configs["episodes"][16], configs)
#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "Apex Legends"][0], configs)
scriptedvided.makeVideo(configs)

