import scriptedvided

configs = { "defaultAudioFile" : "hd6850_2023_2.ogg",\
"mediaFolder" : "F:\\Videos\\hd6850_2023", \
"stockFolder" : "F:\\Videos\\stock",\
"benchmarkFile" : "F:\\Videos\\hd6850_2023\\Benchmark_hd6850_2023.txt",\
"outputFolder" : "F:\\Videos\\hd6850_2023\\output", \
"outputFile" : "hd6850_2023.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3",\
"timestamps" : ("00:30", None ), "destinationTimestamp" : {"title" : "Why retesting the HD 5770", "until" : "Alien: Isolation"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3",\
"timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Alien: Isolation", "until" : "Control"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3",\
"timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Control", "until" : "Rocket League"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3",\
"timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Rocket League", "until" : "Usefulness of an old (D)GPU"}}, \
{"file" : "bensound-summer.mp3", "timestamps" : ("00:00", None ), "destinationTimestamp" : { "title": "Usefulness of an old (D)GPU", "until" : "Blooper" }}, \
], "volume" : 0.05 },\
"episodes" : [],\
"youtube" : {"title" : "Testing the older AMD Radeon HD 6850 in popular games (2023)", \
"description" : '''I wanted to revisit the HD6850 in 2023; as I mentioned already, a lot of things can happen in a year, from Windows updates to games updates, and the numbers obtained a year ago may not reflect the current performance of the card.
This time around, the 6850 variant that we’re looking at is from XFX
''',\
"links" : '''
Our review of the HD 6850 from a year ago (2022): https://www.youtube.com/watch?v=-1eIjIxfx0k

Iceberg Tech's review of UHD 730: https://www.youtube.com/watch?v=5xvRPxVMQ1k

TechPowerup entry: https://www.techpowerup.com/gpu-specs/xfx-hd-6850-xxx-edition.b1046

Intel 11th gen processors, to illustrate the costs of an IGPU:
The core i5 11400 (has an IGPU): https://ark.intel.com/content/www/us/en/ark/products/212270/intel-core-i511400-processor-12m-cache-up-to-4-40-ghz.html
The core i5 11400F (no IGPU): https://ark.intel.com/content/www/us/en/ark/products/212271/intel-core-i511400f-processor-12m-cache-up-to-4-40-ghz.html
''', \
"tags" : "AMD,ATI,Radeon,HD6850,HD 6850,TeraScale 2",\
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
{ "title": "Why retesting the HD 6850",\
"audio" : {"timestamps" : ("00:00", "00:15.7" ), "volume" : 0.999, "padding" : 0.5 },\
"video" : "hd6850_family.mp4"\
})

configs["episodes"].append(\
{ "title": "XFX HD 6850",\
"isChapter" : False, \
"audio" : {"timestamps" : ("00:15.7", "00:22.2" ), "volume" : 0.999, "padding" : 0.5 },\
"video" : {"file" : "xfx_hd6850_bb_card.mp4", "rotation" : 180}\
})

configs["episodes"].append(\
{ "title": "The GPU",\
"audio" : {"timestamps" : ("00:22.2", "00:35.8" ), "volume" : 0.999, "padding" : 0.5 },\
"video" : "xfx_hd6850_heaven-gpuz-repair.mp4"\
})

configs["episodes"].append(\
{ "title": "Test system",\
"audio" : {"timestamps" : ("00:35.8" , "00:49.7"), "volume" : 0.999, "padding" : 0.5 },\
"video" : "z230_cpuz_taskManager.mkv"\
})

configs["episodes"].append(\
{ "title": "Cooling and thermals",\
"audio" : {"timestamps" : ("00:49.7", "01:14.5"), "volume" : 0.999, "padding" : 0.5 },\
"video" : "xfx_hd6850_cooling.mp4"\
})

configs["episodes"].append(\
{ "title": "Cooling - sapphire",\
"isChapter" : False, \
"audio" : {"timestamps" : ("01:14.5", "01:24.4"), "volume" : 0.999, "padding" : 0.5 },\
"video" : {"file":"hd6850_cooling_solution.mp4", "start" : "00:00"}\
})

configs["episodes"].append(\
{ "title": "Thermals",\
"isChapter" : False, \
"audio" : {"timestamps" : ( "01:24.4", "01:41"), "volume" : 0.999, "padding" : 0.5 },\
"video" : {"file":"xfx_hd6850_temps_W_arframe.mp4"}\
})

####################### end of intro ###############################




####################### gaming section ###############################
configs["episodes"].append(\
{ "title": "Alien: Isolation",\
"audio" : {"timestamps" : ("01:41","02:00") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, ultra settings", \
    }\
}, \
})


configs["episodes"].append(\
{ "title": "Apex Legends",\
"audio" : {"timestamps" : ("02:00", "02:27.4" )  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "CoD Warzone",\
"audio" : {"timestamps" : ("02:27.4", "02:36" )  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
}, \
"video" : "TeraScale2_vs_W_arzone_2.mkv"\
})

configs["episodes"].append(\
{ "title": "Battlefield V",\
"audio" : {"timestamps" : ("02:36", "02:54" ) },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
}, \
"video" : "stock_bfv_tobruk_720pLow.mp4",\
})

configs["episodes"].append(\
{ "title": "Control",\
"audio" : {"timestamps" : ("02:54", "03:14") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Rainbow Six: Siege",\
"audio" : {"timestamps" : ("03:14", "03:54") },\
"overlay" : { \
    "text" : ["'Rainbow Six\: Siege'",\
              scriptedvided.r6sText('1920x1080, low settings, 100% render scale', 27, 19), \
              scriptedvided.r6sText('1280x720, low settings, 100% render scale', 42, 25),\
              scriptedvided.r6sText('1920x1080, low settings, 50% render scale', 37, 23),\
              scriptedvided.r6sText('1280x720, low settings, 50% render scale', 53, 30)]\
}, \
})

configs["episodes"].append(\
{ "title": "Grand Theft Auto V",\
"audio" : {"timestamps" : ("03:54",  "04:15") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Counter Strike: Global Offensive",\
"audio" : {"timestamps" : ( "04:15" , "04:39" ) },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "DOTA2",\
"audio" : {"timestamps" : ("04:39", "04:59") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings, 100% render scale", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Fortnite",\
"audio" : {"timestamps" : ("04:59", "05:28") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, performance mode, view distance FAR, 100% render scale", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Overwatch 2",\
"audio" : {"timestamps" : ( "05:28", "05:57") },\
"overlay" : { \
    "text" : ["'Overwatch 2'",\
              scriptedvided.r6sText('1920x1080, low settings, 100% render scale',84, 66),\
              scriptedvided.r6sText('1280x720, low settings, 100% render scale',150, 118),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "Rocket League",\
"audio" : {"timestamps" : ("05:57", "06:19") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings, 100% render scale", \
    }\
}, \
"video" : "stock_RocketLeague_1080pLower.mp4",\
})

configs["episodes"].append(\
{ "title": "Splitgate",\
"audio" : {"timestamps" : ("06:19", "06:44") },\
"overlay" : { \
    "text" : ["'Splitgate'",\
              scriptedvided.r6sText('1920x1080, low settings, 100% render scale',52, 34),\
              scriptedvided.r6sText('1280x720, low settings, 100% render scale',83, 41),\
    ]\
}, \
"video" : "stock_Splitgate_1080pLow.mp4",\
})

configs["episodes"].append(\
{ "title": "Valorant",\
"audio" : {"timestamps" : ("06:44", "07:11") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Genshin Impact",\
"audio" : {"timestamps" : ("07:11", "07:34.5") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings, 1.0 render scale", \
    }\
}, \
})


configs["episodes"].append(\
{ "title": "HiRez Studios trio (Paladins, Realm Royale, Rogue Company)",\
"audio" : {"timestamps" : ("07:34.5", "07:51" ), "volume" : 0.999, "padding" : 0.25 },\
"video" : {"file":"HiRezTrio-P_aladins_R_ealmRoyale_R_ogueCompany.mp4"}\
})



configs["episodes"].append(\
{ "title": "Paladins",\
"isChapter" : False,\
"audio" : {"timestamps" : ("07:51", "07:57") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, high settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Realm Royale",\
"isChapter" : False,\
"audio" : {"timestamps" : ("07:57", "08:03") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, high settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Rogue Company",\
"isChapter" : False,\
"audio" : {"timestamps" : ("08:03", "08:09") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "World of Tanks Blitz",\
"audio" : {"timestamps" : ("08:09", "08:28") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, high settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Warframe",\
"audio" : {"timestamps" : ("08:28", "08:59") },\
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
"video" : "dgpu_over_igpu.mp4"
})
###########################

configs["episodes"].append(\
{ "title": "Is the HD 6850 worth it?",\
"audio" : {"timestamps" : ( "08:59", "09:23"), "volume" : 0.999 },\
"video" : {"file" : "hd6850_pricing_prices.mkv"}
})

configs["episodes"].append(\
{ "title": "Competition - HD 7770",\
"isChapter" : False,\
"audio" : {"timestamps" : ( "09:23", "09:46"), "volume" : 0.999 },\
"video" : {"file" : "hd6850_family.mp4"}
})


##configs["episodes"].append(\
##{ "title": "Blooper",\
##"isChapter" : False,\
##"audio" : {"timestamps" : ( "13:40.5", "14:04.2") },\
##"video" : {"file":"HiRezTrio-P_aladins_R_ealmRoyale_R_ogueCompany.mp4"}\
##})

#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "Splitgate"][0], configs)
scriptedvided.makeVideo(configs)

