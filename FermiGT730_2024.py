import scriptedvided

configs = { "defaultAudioFile" : "FermigtGT730_2024.ogg",\
"mediaFolder" : "F:\\Videos\\Fermi_GT730_2024", \
"stockFolder" : "F:\\Videos\\stock",\
"benchmarkFile" : "F:\\Videos\\Fermi_GT730_2024\\Benchmark_GT_730_2024.txt",\
"outputFolder" : "F:\\Videos\\Fermi_GT730_2024\\output", \
"outputFile" : "Fermi_GT730_2024.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#00800080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3",\
"timestamps" : ("00:30", None ), "destinationTimestamp" : {"title" : "History repeats itself", "until" : "Resident Evil 4 (Remake)"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3",\
"timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Resident Evil 4 (Remake)", "until" : "Fortnite"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3",\
"timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Fortnite", "until" : "DOTA2"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3",\
"timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "DOTA2", "until" : "Conclusions"}}, \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3",\
"timestamps" : ("00:30", None ), "destinationTimestamp" : {"title" : "Conclusions", "until" : "htpc card"}}, \
{"file" : "Guide You Home - Ferco and Andie - Free Background Music - Audio Library Release.ogg", "timestamps" : ("00:20", None ), "destinationTimestamp" : { "title": "htpc card", "until" : "Blooper" }}, \
], "volume" : 0.04 },\
"episodes" : [],\
"youtube" : {"title" : "History repeats itself (Fermi GT 730)", \
"description" : '''In this video we're using the Fermi GT 730 to point out the frequent bait and switch games played in the GPU market.''',\
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

TechPowerup entry: https://www.techpowerup.com/gpu-specs/msi-gtx-1050-ti-lp.b4033
''', \
"tags" : "NVidia,Fermi,GeForce,GT430,GT 430,GT730,GT 730",\
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
{ "title": "History repeats itself",\
"audio" : {"timestamps" : ("00:00", "00:17" ), "volume" : 0.999, "padding" : 0.1 },\
"video" : {"file": "breel_FermiGT730_outside.mp4"}\
})

configs["episodes"].append(\
{ "title": "Bait and switch",\
"isChapter" : False, \
"audio" : {"timestamps" : ("00:17", "00:30" ), "volume" : 0.999, "padding" : 0.1 },\
"video" : {"file": "baitandswitch.mp4", "start" : "00:01"}\
})

configs["episodes"].append(\
{ "title": "GF4",\
"isChapter" : False, \
"audio" : {"timestamps" : ("00:30", "00:42.6" ), "volume" : 0.999, "padding" : 0.1 },\
"video" : {"file": "GeForce4_series.mkv"}\
})

configs["episodes"].append(\
{ "title": "Bitten by the 730",\
"isChapter" : False, \
"audio" : {"timestamps" : ("00:42.6", "00:54" ), "volume" : 0.999, "padding" : 0.1 },\
"video" : {"file": "breel_FermiGT730_slomo_outside.mp4"}\
})

configs["episodes"].append(\
{ "title": "Did not do homework",\
"isChapter" : False, \
"audio" : {"timestamps" : ("00:54", "01:05.3" ), "volume" : 0.999, "padding" : 0.1 },\
"video" : {"file": "GT730_announcement.mkv"}\
})

configs["episodes"].append(\
{ "title": "The GPU",\
"audio" : {"timestamps" : ("01:05.3", "01:27.3" ), "volume" : 0.999, "padding" : 0.1 },\
"video" : {"file": "FermiGT730_Heaven_GPUZ_long.mp4"}\
})

configs["episodes"].append(\
{ "title": "Where are the drivers",\
"audio" : {"timestamps" : ("01:27.3", "01:49.4" ), "volume" : 0.999, "padding" : 0.1 },\
"video" : {"file": "GF108_download_kepler_driver.mkv", "start" : "00:20"}\
})

configs["episodes"].append(\
{ "title": "The test system",\
"audio" : {"timestamps" : ("01:49.4", "02:11.2" ), "volume" : 0.999, "padding" : 0.1 },\
"overlay" : { \
    "text" : ["'Z230 workstation from HP'",\
              "'CPU\: E3-1241v3 Xeon (i7 4770 equivalent)'",\
              "'RAM\: 32GB DDR3 at 1600 MHz, dual channel'",\
    ]\
}, \
"video" : {"file" : "Z230_closed.mp4", "rotation" : 180}\
})

configs["episodes"].append(\
{ "title": "Settings",\
"isChapter" : False, \
"audio" : {"timestamps" : ("02:11.2", "02:22.3" ), "volume" : 0.999, "padding" : 0.1 },\
"video" : {"file": "stock_AlienIsolation_3.mp4" , "start" : "01:00"}\
})


####################### end of intro ###############################



####################### gaming section ###############################

configs["episodes"].append(\
{ "title": "Resident Evil 4 (Remake)",\
"audio" : {"timestamps" : ("02:22.3", "02:36.5" ), "padding" : 0.1  },\
"video" : {"file" : "FermiGT730_RE4.mp4", "start" : "00:04"}, \
"overlay" : { \
    "text" : ["'Resident Evil 4 (Remake)'",\
              scriptedvided.r6sText('1280x720, low settings', 0, 0),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "Battlefield V",\
"audio" : {"timestamps" : ("02:36.5", "02:43.8" ), "padding" : 0.1  },\
"overlay" : { \
    "text" : ["'Battlefield V'",\
              scriptedvided.r6sText('1280x720, low settings', 0, 0),\
    ]\
}, \
"video" : {"file" : "FermiGT730_BFV.mp4", "start" : "00:04"}, \
})

configs["episodes"].append(\
{ "title": "Control",\
"audio" : {"timestamps" : ("02:43.8", "02:58.4" ), "padding" : 0.1  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
}, \
})

# this needs a longer stock video
configs["episodes"].append(\
{ "title": "Apex Legends",\
"audio" : {"timestamps" : ("02:58.4", "03:12.2" ), "padding" : 0.1  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Rainbow Six: Siege",\
"audio" : {"timestamps" : ("03:12.2", "03:31" ), "padding" : 0.1  },\
"overlay" : { \
    "text" : ["'Rainbow Six\: Siege'",\
              scriptedvided.r6sText('1280x720, low settings, 100% render scale', 24, 18),\
              scriptedvided.r6sText('1280x720, low settings, 50% render scale', 32, 22)]\
}, \
})

configs["episodes"].append(\
{ "title": "Counter-Strike 2",\
"audio" : {"timestamps" : ("03:31", "03:45.7" ), "padding" : 0.1  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Splitgate",\
"audio" : {"timestamps" : ("03:45.7", "03:57.3" ), "padding" : 0.1  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Overwatch 2",\
"audio" : {"timestamps" : ("03:57.3", "04:17.3" ), "padding" : 0.1  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Fortnite",\
"audio" : {"timestamps" : ("04:17.3", "04:42" ), "padding" : 0.1  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
}, \
})



configs["episodes"].append(\
{ "title": "Alien: Isolation",\
"audio" : {"timestamps" : ("04:42", "05:04.3" ), "padding" : 0.1  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, ultra settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Grand Theft Auto V",\
"audio" : {"timestamps" : ("05:04.3", "05:20" ), "padding" : 0.1  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Warframe",\
"audio" : {"timestamps" : ("05:20", "05:33" ), "padding" : 0.1  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
}, \
})


configs["episodes"].append(\
{ "title": "HiRez Studios trio (Paladins, Realm Royale, Rogue Company)",\
"audio" : {"timestamps" : ("05:33", "05:42.4" ), "padding" : 0.1  },\
"video" : {"file":"HiRezTrio-P_aladins_R_ealmRoyale_R_ogueCompany.mp4"}\
})

configs["episodes"].append(\
{ "title": "Paladins",\
"isChapter" : False,\
"audio" : {"timestamps" : ("05:42.4", "05:50" ), "padding" : 0.1  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Realm Royale",\
"isChapter" : False,\
"audio" : {"timestamps" : ("05:50", "06:00" ), "padding" : 0.1  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Rogue Company",\
"isChapter" : False,\
"audio" : {"timestamps" : ("06:00", "06:07" ), "padding" : 0.1  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "DOTA2",\
"audio" : {"timestamps" : ("06:07", "06:21" ), "padding" : 0.1  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
}, \
})


configs["episodes"].append(\
{ "title": "Rocket League",\
"audio" : {"timestamps" : ("06:21", "06:28.3" ), "padding" : 0.1  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Valorant",\
"audio" : {"timestamps" : ("06:28.3", "06:39.6" ), "padding" : 0.1  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "World of Tanks Blitz",\
"audio" : {"timestamps" : ("06:39.6", "06:50.6" ), "padding" : 0.1  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, high settings", \
    }\
}, \
})


####################### end of gaming section ###############################


####################### conclusion ###############################

configs["episodes"].append(\
{ "title": "Conclusions",\
"audio" : {"timestamps" : ("06:50.6", "07:06.8" ), "volume" : 0.999 , "padding" : 0.1  },\
"video" : {"file" : "Fermi_legacy.mkv"}\
})


configs["episodes"].append(\
{ "title": "Drivers page",\
"isChapter" : False,\
"audio" : {"timestamps" : ("07:06.8", "07:17.35" ), "volume" : 0.999 , "padding" : 0.1  },\
"video" : {"file": "GF108_download_kepler_driver.mkv", "start" : "00:21"}\
})

configs["episodes"].append(\
{ "title": "Attempt to install",\
"isChapter" : False,\
"audio" : {"timestamps" : ("07:17.35" , "07:28.3"), "volume" : 0.999 , "padding" : 0.1  },\
"video" : {"file" : "GF108_install_kepler_driver.mkv", "start" : "00:42"}\
})

configs["episodes"].append(\
{ "title": "430 instead",\
"isChapter" : False,\
"audio" : {"timestamps" : ("07:28.3", "07:38.8"), "volume" : 0.999 , "padding" : 0.1  },\
"video" : {"file": "GF108_download_fermi_driver.mkv", "start" : "00:18"}\
})

configs["episodes"].append(\
{ "title": "Magician",\
"isChapter" : False,\
"audio" : {"timestamps" : ( "07:38.8", "08:04.3"), "volume" : 0.999 , "padding" : 0.1  },\
"video" : {"file" : "pick.mp4"}\
})

configs["episodes"].append(\
{ "title": "1060 3g",\
"isChapter" : False,\
"audio" : {"timestamps" : ( "08:04.3", "08:11.9"), "volume" : 0.999 , "padding" : 0.1  },\
"video" : {"file" : "GTX1060_3G.mkv"}\
})

configs["episodes"].append(\
{ "title": "3060 8g",\
"isChapter" : False,\
"audio" : {"timestamps" : ("08:11.9", "08:18.9"), "volume" : 0.999 , "padding" : 0.1  },\
"video" : {"file" : "RTX3060_8G.mkv"}\
})

configs["episodes"].append(\
{ "title": "4080 12g",\
"isChapter" : False,\
"audio" : {"timestamps" : ("08:18.9", "08:40.8"), "volume" : 0.999 , "padding" : 0.1  },\
"video" : {"file" : "RTX4080_12G.mkv"}\
})

configs["episodes"].append(\
{ "title": "good men",\
"isChapter" : False,\
"audio" : {"timestamps" : ( "08:40.8",  "08:54.7"), "volume" : 0.999 , "padding" : 0.1  },\
"video" : {"file" : "evil.mp4", "start" : "00:01"}\
})

configs["episodes"].append(\
{ "title": "good men - mirror",\
"isChapter" : False,\
"audio" : {"timestamps" : ("08:54.7", "09:08.2"), "volume" : 0.999 , "padding" : 0.1  },\
"video" : {"file" : "Wallet.mkv"}, \
"overlay" : { \
    "text" : ["'Google search results for customers'"]\
}, \
})

configs["episodes"].append(\
{ "title": "htpc card",\
"isChapter" : False,\
"audio" : {"timestamps" : ("09:08.2", "09:22.2"), "volume" : 0.999 , "padding" : 0.1  },\
"video" : {"file" : "GF108_HTPC_King.mkv", "start" : "00:05"}\
})

configs["episodes"].append(\
{ "title": "STALKER: Call of Prypiat",\
"audio" : {"timestamps" : ("09:22.2", "09:41.3" ), "padding" : 0.1  },\
"overlay" : { \
    "text" : ["'STALKER\: Call of Prypiat'",\
              scriptedvided.r6sText('1280x720, DX11, medium settings', 42, 30)]\
}, \
"video" : {"file" : "xrEngine_COP.mp4", "start" : "01:50"}, \
})

configs["episodes"].append(\
{ "title": "Wolfenstein",\
"audio" : {"timestamps" : ("09:41.3" , "09:59.5" ), "padding" : 0.1  },\
"overlay" : { \
    "text" : ["'Wolfenstein (2009)'",\
              scriptedvided.r6sText('1280x720, high settings', 56, 38)]\
}, \
"video" : {"file" : "Wolf2_2009.mp4", "start" : "00:40"}, \
})

configs["episodes"].append(\
{ "title": "Quite a few better options, even for a display adapter",\
"audio" : {"timestamps" : ("09:59.5", "10:10.5"), "volume" : 0.999 , "padding" : 0.1  },\
"video" : {"file" : "broll_GTX1050Ti_outside.mp4"}\
})

configs["episodes"].append(\
{ "title": "bye",\
"isChapter" : False,\
"audio" : {"timestamps" : ("10:10.5", "10:15.8"), "volume" : 0.999 , "padding" : 0.1  },\
"video" : {"file" : "breel_FermiGT730_outside.mp4"}\
})


##configs["episodes"].append(\
##{ "title": "Blooper",\
##"isChapter" : False,\
##"audio" : {"timestamps" : ( "13:40.5", "14:04.2") },\
##"video" : {"file":"HiRezTrio-P_aladins_R_ealmRoyale_R_ogueCompany.mp4"}\
##})

#scriptedvided.makeVideoForEpisode(configs["episodes"][9], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][10], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][30], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][31], configs)
scriptedvided.makeVideoForEpisode(configs["episodes"][33], configs)
#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "Splitgate"][0], configs)
#scriptedvided.makeVideo(configs)






