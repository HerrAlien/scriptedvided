import scriptedvided

configs = { "defaultAudioFile" : "GTX1050Ti2.ogg",\
"mediaFolder" : "F:\\Videos\\GTX1050Ti", \
"stockFolder" : "F:\\Videos\\stock",\
"benchmarkFile" : "F:\\Videos\\GTX1050Ti\\Benchmark_GTX_1050_Ti.txt",\
"outputFolder" : "F:\\Videos\\GTX1050Ti\\output", \
"outputFile" : "GTX1050Ti.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#00800080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3",\
"timestamps" : ("00:30", None ), "destinationTimestamp" : {"title" : "A Christmas miracle", "until" : "Alien: Isolation"}}, \
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
"youtube" : {"title" : "A card that refused to die (GTX 1050 Ti)", \
"description" : '''In this video we're checking out a GTX 1050 Ti, low profile, from MSI. 
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

TechPowerup entry: https://www.techpowerup.com/gpu-specs/msi-gtx-1050-ti-lp.b4033
''', \
"tags" : "NVidia,Pascal,GeForce,GTX,GTX1050Ti,GTX 1050Ti,GTX 1050 Ti",\
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
{ "title": "A Christmas miracle",\
"audio" : {"timestamps" : ("00:00", "00:16.5" ), "volume" : 0.999, "padding" : 0.1 },\
"video" : {"file": "broll_GTX1050Ti_outside.mp4"}\
})

configs["episodes"].append(\
{ "title": "The GPU",\
"audio" : {"timestamps" : ("00:16.5", "00:29.3" ), "volume" : 0.999, "padding" : 0.1 },\
"video" : {"file": "GTX1050Ti_Heaven_GPUz_Temps.mp4", "start" : "00:00"}\
})

configs["episodes"].append(\
{ "title": "Office to gaming",\
"isChapter" : False, \
"audio" : {"timestamps" : ("00:29.3", "00:40.2" ), "volume" : 0.999, "padding" : 0.1 },\
"video" : {"file": "office_pc_gt_1030.mkv"}\
})

configs["episodes"].append(\
{ "title": "Cooling and thermals",\
"audio" : {"timestamps" : ("00:40.2", "01:02.9" ), "volume" : 0.999, "padding" : 0.1 },\
"video" : {"file": "gtx1050Ti_cooling.mp4"}\
})

configs["episodes"].append(\
{ "title": "Temperatures",\
"isChapter" : False, \
"audio" : {"timestamps" : ("01:02.9", "01:23.4" ), "volume" : 0.999, "padding" : 0.1 },\
"overlay" : { \
    "text" : ["'Thermals'",\
              "'Heaven\: 64C (40C delta over ambient)'",\
              "'Warframe\: 65C (41C delta over ambient)'",\
    ]\
}, \
"video" : {"file": "W_a_rframe_temps.mp4"}\
})

configs["episodes"].append(\
{ "title": "The test system",\
"audio" : {"timestamps" : ("01:23.4", "01:49" ), "volume" : 0.999, "padding" : 0.1 },\
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
"audio" : {"timestamps" : ("01:49", "02:10.3" ), "padding" : 0.1  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, ultra settings", \
    }\
}, \
})

# this needs a longer stock video
configs["episodes"].append(\
{ "title": "Apex Legends",\
"audio" : {"timestamps" : ("02:10.3", "02:42.9" ), "padding" : 0.1  },\
"overlay" : { \
    "text" : ["'Apex Legends'",\
              scriptedvided.r6sText('1920x1080, low settings', 108, 75),\
              scriptedvided.r6sText('1600x900, low settings', 126,  89),\
              scriptedvided.r6sText('1280x720, low settings', 140,  106),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "Resident Evil 4 (Remake)",\
"audio" : {"timestamps" : ("02:42.9", "03:12.4" ), "padding" : 0.1  },\
"video" : {"file": "stock_re4demo_choppyExceptCutscenes.mp4", "start" : "03:07"},\
"overlay" : { \
    "text" : ["'Resident Evil 4 (Remake)'",\
              scriptedvided.r6sText('1920x1080, low settings', 40, 25),\
              scriptedvided.r6sText('1280x720, low settings', 63, 34),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "Battlefield V",\
"audio" : {"timestamps" : ("03:12.4", "03:43" ), "padding" : 0.1  },\
"overlay" : { \
    "text" : ["'Battlefield V'",\
              scriptedvided.r6sText('1920x1080, low settings', 57, 46),\
              scriptedvided.r6sText('1600x900, low settings', 67, 55),\
              scriptedvided.r6sText('1280x720, low settings', 82, 62),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "Control",\
"audio" : {"timestamps" : ("03:43", "04:07.1" ), "padding" : 0.1  },\
"overlay" : { \
    "text" : ["'Control'",\
              scriptedvided.r6sText('1920x1080, low settings', 57, 36),\
              scriptedvided.r6sText('1280x720, low settings', 111, 89),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "Rainbow Six: Siege",\
"audio" : {"timestamps" : ("04:07.1", "04:42" ), "padding" : 0.1  },\
"overlay" : { \
    "text" : ["'Rainbow Six\: Siege'",\
              scriptedvided.r6sText('1920x1080, low settings, 100% render scale', 123, 88), \
              scriptedvided.r6sText('1280x720, low settings, 100% render scale', 183, 117),\
              scriptedvided.r6sText('1920x1080, low settings, 50% render scale', 160, 109),\
              scriptedvided.r6sText('1280x720, low settings, 50% render scale', 203, 144)]\
}, \
})

configs["episodes"].append(\
{ "title": "Grand Theft Auto V",\
"audio" : {"timestamps" : ("04:42", "05:10" ), "padding" : 0.1  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Counter-Strike 2",\
"audio" : {"timestamps" : ("05:10", "05:39.1" ), "padding" : 0.1  },\
"overlay" : { \
    "image" : {"file" : "A text book system bottleneck.png", "chromaColor" : "0x00FF00"}\
}, \
})

configs["episodes"].append(\
{ "title": "DOTA2",\
"audio" : {"timestamps" : ("05:39.1", "06:00.1" ), "padding" : 0.1  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Fortnite",\
"audio" : {"timestamps" : ("06:00.1", "06:39.6" ), "padding" : 0.1  },\
"video" : {"file" : "stock_FortniteClient-Win_2023_12_24.mp4" , "start" : "19:11"},\
"overlay" : { \
    "text" : ["'Fortnite'",\
              scriptedvided.r6sText('1920x1080, performance mode', 140, 81 ), \
              scriptedvided.r6sText('1600x900, performance mode', 152 , 91),\
              scriptedvided.r6sText('1280x720, performance mode', 167, 92)]\
}, \
})


configs["episodes"].append(\
{ "title": "Overwatch 2",\
"audio" : {"timestamps" : ("06:39.6", "07:08.7" ), "padding" : 0.1  },\
"overlay" : { \
    "text" : ["'Overwatch 2'",\
              scriptedvided.r6sText('1920x1080, low settings', 207, 160 ),\
              scriptedvided.r6sText('1600x900, low settings', 280, 216),\
              scriptedvided.r6sText('1280x720, low settings', 389, 282 ),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "Rocket League",\
"audio" : {"timestamps" : ("07:08.7", "07:36.9" ), "padding" : 0.1  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings, 100% render scale", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Splitgate",\
"audio" : {"timestamps" : ("07:36.9", "08:05.6" ), "padding" : 0.1  },\
"overlay" : { \
    "text" : ["'Splitgate'",\
              scriptedvided.r6sText('1920x1080, low settings, 100% render scale', 169 , 54 ),\
              scriptedvided.r6sText('1280x720, low settings, 100% render scale', 230, 65 ),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "Valorant",\
"audio" : {"timestamps" : ("08:05.6", "08:31.5" ), "padding" : 0.1  },\
"video" : "V_A_LORANT_noLaunch.mp4",\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "HiRez Studios trio (Paladins, Realm Royale, Rogue Company)",\
"audio" : {"timestamps" : ("08:31.5", "08:40.7" ), "volume" : 0.999 , "padding" : 0.1  },\
"video" : {"file":"HiRezTrio-P_aladins_R_ealmRoyale_R_ogueCompany.mp4"}\
})



configs["episodes"].append(\
{ "title": "Paladins",\
"isChapter" : False,\
"audio" : {"timestamps" : ("08:40.7", "08:49.6" ), "padding" : 0.1  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, high settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Realm Royale",\
"isChapter" : False,\
"audio" : {"timestamps" : ("08:49.6", "08:59" ), "padding" : 0.1  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, high settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Rogue Company",\
"isChapter" : False,\
"audio" : {"timestamps" : ("08:59", "09:07.1" ), "padding" : 0.1  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "World of Tanks Blitz",\
"audio" : {"timestamps" : ("09:07.1", "09:28.4" ), "padding" : 0.1  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, high settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Warframe",\
"audio" : {"timestamps" : ("09:28.4", "09:44" ), "padding" : 0.1  },\
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
"audio" : {"timestamps" : ("09:44", "09:53.1" ), "volume" : 0.999 , "padding" : 0.1  },\
"video" : {"file" : "breel_GTX770_R9_280_attic.mp4"}\
})


configs["episodes"].append(\
{ "title": "1050ti all the way",\
"isChapter" : False,\
"audio" : {"timestamps" : ("09:53.1", "10:14" ), "volume" : 0.999 , "padding" : 0.1  },\
"video" : {"file" : "broll_GTX1050Ti_outside.mp4"}\
})

configs["episodes"].append(\
{ "title": "boiling MLCC",\
"isChapter" : False,\
"audio" : {"timestamps" : ("10:14", "10:31" ), "volume" : 0.999 , "padding" : 0.1  },\
"overlay" : { \
    "image" : {"file" : "1050ti list of issues.png", "chromaColor" : "0x00FF00"}\
}, \
"video" : {"file" : "gtx1050Ti_betterBoilingMlccMemory.mp4", "start" : "00:00"}\
})

configs["episodes"].append(\
{ "title": "1050ti and bye",\
"isChapter" : False,\
"audio" : {"timestamps" : ("10:31", "10:43.8" ), "volume" : 0.999 , "padding" : 0.1  },\
"video" : {"file" : "broll_GTX1050Ti_outside.mp4"}\
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
#scriptedvided.makeVideoForEpisode(configs["episodes"][32], configs)
#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "Splitgate"][0], configs)
scriptedvided.makeVideo(configs)

