import scriptedvided

configs = { "defaultAudioFile" : "rx460.ogg",\
"mediaFolder" : "F:\\Videos\\RX460", \
"stockFolder" : "F:\\Videos\\stock",\
"benchmarkFile" : "F:\\Videos\\RX460\\Benchmark_RX460.txt",\
"outputFolder" : "F:\\Videos\\RX460\\output", \
"outputFile" : "RX460.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3",\
"timestamps" : ("00:30", None ), "destinationTimestamp" : {"title" : "Why testing the RX 460", "until" : "Alien: Isolation"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3",\
"timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Alien: Isolation", "until" : "Counter Strike: Global Offensive"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3",\
"timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Counter Strike: Global Offensive", "until" : "Genshin Impact"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3",\
"timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Genshin Impact", "until" : "Conclusions"}}, \
{"file" : "Guide You Home - Ferco and Andie - Free Background Music - Audio Library Release.ogg", "timestamps" : ("00:20", None ), "destinationTimestamp" : { "title": "Conclusions", "until" : "end of video" }}, \
], "volume" : 0.04 },\
"episodes" : [],\
"youtube" : {"title" : "OEM Radeon card tested in 2023 (RX 460)", \
"description" : '''In this video we're checking out the RX 460 - one of the least power hungry GPUs from the Polaris family. 
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

TechPowerup entry: https://www.techpowerup.com/gpu-specs/msi-r7-260x-ocv1.b3094
''', \
"tags" : "AMD,ATI,Radeon,RX460,RX 460,Polaris,GCN4,GCN 4,GCN",\
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
{ "title": "Why testing the RX 460",\
"audio" : {"timestamps" : ("00:00", "00:20.5" ), "volume" : 0.999, "padding" : 0.25 },\
"video" : {"file": "breel_rx460_outside.mp4"}\
})

configs["episodes"].append(\
{ "title": "vs 260x",\
"isChapter" : False, \
"audio" : {"timestamps" : ("00:20.5", "00:36" ), "volume" : 0.999, "padding" : 0.25 },\
"video" : {"file": "breel_R7_260X_RX460_outside.mp4"}\
})


configs["episodes"].append(\
{ "title": "The GPU",\
"audio" : {"timestamps" : ("00:36", "01:09" ), "volume" : 0.999, "padding" : 0.25 },\
"video" : {"file": "rx460_gpuz.mp4"}\
})

configs["episodes"].append(\
{ "title": "Cooling and thermals",\
"audio" : {"timestamps" : ("01:09", "01:32" ), "volume" : 0.999, "padding" : 0.25 },\
"video" : {"file": "breel_rx460_outside.mp4"}\
})

configs["episodes"].append(\
{ "title": "thermals",\
"isChapter" : False, \
"audio" : {"timestamps" : ("01:32", "01:49" ), "volume" : 0.999, "padding" : 0.25 },\
"video" : {"file": "rx460_heaven.mp4"}\
})

configs["episodes"].append(\
{ "title": "The test system",\
"audio" : {"timestamps" : ("01:49", "02:03" ), "volume" : 0.999, "padding" : 0.25 },\
"video" : {"file" : "Z230_closed.mp4", "rotation" : 180}\
})

####################### end of intro ###############################



####################### gaming section ###############################
configs["episodes"].append(\
{ "title": "Alien: Isolation",\
"audio" : {"timestamps" : ("02:03", "02:29" ), "padding" : 0.25 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, ultra settings", \
    }\
}, \
})

# this needs a longer stock video
configs["episodes"].append(\
{ "title": "Apex Legends",\
"audio" : {"timestamps" : ("02:29", "02:56" ), "padding" : 0.25 },\
"overlay" : { \
    "text" : ["'Apex Legends'",\
              scriptedvided.r6sText('1920x1080, low settings', 94, 65),\
              scriptedvided.r6sText('1600x900, low settings', 120, 82),\
              scriptedvided.r6sText('1280x720, low settings', 137, 107),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "CoD Warzone",\
"audio" : {"timestamps" : ("02:56", "03:22.5" ), "padding" : 0.25 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Battlefield V",\
"audio" : {"timestamps" : ("03:22.5", "03:48.5" ), "padding" : 0.25 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Control",\
"audio" : {"timestamps" : ("03:48.5", "04:24.5" ), "padding" : 0.25 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Rainbow Six: Siege",\
"audio" : {"timestamps" : ("04:24.5", "04:58" ), "padding" : 0.25 },\
"overlay" : { \
    "text" : ["'Rainbow Six\: Siege'",\
              scriptedvided.r6sText('1920x1080, low settings, 100% render scale', 91, 78), \
              scriptedvided.r6sText('1280x720, low settings, 100% render scale', 173, 139),\
              scriptedvided.r6sText('1920x1080, low settings, 50% render scale', 130, 108),\
              scriptedvided.r6sText('1280x720, low settings, 50% render scale', 208, 139)]\
}, \
})

configs["episodes"].append(\
{ "title": "Grand Theft Auto V",\
"audio" : {"timestamps" : ("04:58", "05:33.6" ), "padding" : 0.25 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Counter Strike: Global Offensive",\
"audio" : {"timestamps" : ("05:33.6", "05:57" ), "padding" : 0.25 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "DOTA2",\
"audio" : {"timestamps" : ("05:57", "06:23.5" ), "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Fortnite",\
"audio" : {"timestamps" : ("06:23.5", "07:12" ), "padding" : 0.25  },\
"overlay" : { \
    "text" : ["'Fortnite'",\
              scriptedvided.r6sText('1920x1080, performance mode', 104, 31), \
              scriptedvided.r6sText('1600x900, performance mode', 122, 46),\
              scriptedvided.r6sText('1280x720, performance mode', 126, 27)]\
}, \
})


configs["episodes"].append(\
{ "title": "Overwatch 2",\
"audio" : {"timestamps" : ("07:12", "07:42" ), "padding" : 0.25 },\
"overlay" : { \
    "text" : ["'Overwatch 2'",\
              scriptedvided.r6sText('1920x1080, low settings', 130, 97),\
              scriptedvided.r6sText('1600x900, low settings', 178,  135),\
              scriptedvided.r6sText('1280x720, low settings', 260, 201),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "Rocket League",\
"audio" : {"timestamps" : ("07:42", "08:13" ), "padding" : 0.25 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings, 100% render scale", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Splitgate",\
"audio" : {"timestamps" : ("08:13", "09:01.5" ), "padding" : 0.25 },\
"overlay" : { \
    "text" : ["'Splitgate'",\
              scriptedvided.r6sText('1920x1080, low settings, 100% render scale', 128,  36),\
              scriptedvided.r6sText('1280x720, low settings, 100% render scale', 210, 132 ),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "Valorant",\
"audio" : {"timestamps" : ("09:01.5", "09:28" ), "padding" : 0.25 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Genshin Impact",\
"audio" : {"timestamps" : ("09:28", "09:53" ), "padding" : 0.25 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings, 1.0 render scale", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "HiRez Studios trio (Paladins, Realm Royale, Rogue Company)",\
"audio" : {"timestamps" : ("09:53", "10:09.2" ), "volume" : 0.999 , "padding" : 0.25  },\
"video" : {"file":"HiRezTrio-P_aladins_R_ealmRoyale_R_ogueCompany.mp4"}\
})



configs["episodes"].append(\
{ "title": "Paladins",\
"isChapter" : False,\
"audio" : {"timestamps" : ("10:09.2", "10:16.35" ), "padding" : 0.25 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, high settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Realm Royale",\
"isChapter" : False,\
"audio" : {"timestamps" : ("10:16.35", "10:24.4" ), "padding" : 0.25 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, high settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Rogue Company",\
"isChapter" : False,\
"audio" : {"timestamps" : ("10:24.4", "10:32.5" ), "padding" : 0.25 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "World of Tanks Blitz",\
"audio" : {"timestamps" : ("10:32.5", "10:52" ), "padding" : 0.25 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, high settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Warframe",\
"audio" : {"timestamps" : ("10:52", "11:24" ), "padding" : 0.25 },\
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
"audio" : {"timestamps" : ("11:24", "11:56.5" ), "volume" : 0.999 , "padding" : 0.25  },\
"video" : {"file" : "breel_GCN_families.mp4"}\
})

configs["episodes"].append(\
{ "title": "rx460 - like it though",\
"isChapter" : False,\
"audio" : {"timestamps" : ("11:56.5", "12:19.6" ), "volume" : 0.999 , "padding" : 0.25  },\
"video" : {"file" : "breel_rx460_outside.mp4"}\
})


configs["episodes"].append(\
{ "title": "No power connectors",\
"isChapter" : False,\
"audio" : {"timestamps" : ("12:19.6", "12:36.4" ), "volume" : 0.999 , "padding" : 0.25  },\
"video" : {"file" : "breel_noPowerConnector_vsPowerConnectors.mp4"}\
})

configs["episodes"].append(\
{ "title": "R7 265 next",\
"isChapter" : False,\
"audio" : {"timestamps" : ("12:36.4", "12:46" ), "volume" : 0.999 , "padding" : 0.25  },\
"video" : {"file" : "breel_r7_265_outside.mp4"}\
})

configs["episodes"].append(\
{ "title": "Bye",\
"isChapter" : False,\
"audio" : {"timestamps" : ("12:46", "12.55" ), "volume" : 0.999 , "padding" : 0.25  },\
"video" : {"file" : "breel_rx460_outside.mp4"}\
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

