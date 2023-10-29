import scriptedvided

configs = { "defaultAudioFile" : "R9_280_2023.ogg",\
"mediaFolder" : "F:\\Videos\\R9_280_2023", \
"stockFolder" : "F:\\Videos\\stock",\
"benchmarkFile" : "F:\\Videos\\R9_280_2023\\Benchmark_R9_280_2023.txt",\
"outputFolder" : "F:\\Videos\\R9_280_2023\\output", \
"outputFile" : "R9_280_2023.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3",\
"timestamps" : ("00:30", None ), "destinationTimestamp" : {"title" : "Welcome to Tahiti", "until" : "Alien: Isolation"}}, \
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
"youtube" : {"title" : "Are 3GB of VRAM *that* bad?", \
"description" : '''We'll be checking out the R9 280 - a card that was previously released under the name of HD 7950.
The test system consists of a Z230 workstation, running the E3-1241v3 Xeon CPU (the equivalent of the i7 4770) and 32GB of DDR3 RAM at 1600MHz in dual channel.''',\
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
"tags" : "AMD,ATI,Radeon,HD7950,HD 7950,R7 280,Tahiti,GCN,GCN1,GCN 1",\
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
{ "title": "Welcome to Tahiti",\
"audio" : {"timestamps" : ("00:00", "00:29" ), "volume" : 0.999, "padding" : 0.25 },\
"video" : {"file": "breel_r9_280_outside.mp4"}\
})

configs["episodes"].append(\
{ "title": "The GPU",\
"audio" : {"timestamps" : ("00:29", "00:44" ), "volume" : 0.999, "padding" : 0.25 },\
"video" : {"file" : "R9_280_Heaven_GPUZ"}\
})

configs["episodes"].append(\
{ "title": "Cooling and thermals",\
"audio" : {"timestamps" : ("00:44", "01:04" ), "volume" : 0.999, "padding" : 0.25 },\
"overlay" : { \
    "text" : ["'Thermals'",\
              "'Heaven\: 78C (53C delta over ambient)'",\
              "'Warframe\: 79C (54C delta over ambient)'",\
    ]\
}, \
"video" : {"file": "r9_280_thermals.mp4"}\
})

configs["episodes"].append(\
{ "title": "The test system",\
"audio" : {"timestamps" : ("01:04", "01:23" ), "volume" : 0.999, "padding" : 0.25 },\
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
"audio" : {"timestamps" : ("01:23", "01:43.5" ), "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, ultra settings", \
    }\
}, \
})

# this needs a longer stock video
configs["episodes"].append(\
{ "title": "Apex Legends",\
"audio" : {"timestamps" : ("01:43.5", "02:14" ), "padding" : 0.25  },\
"overlay" : { \
    "text" : ["'Apex Legends'",\
              scriptedvided.r6sText('1920x1080, low settings', 94, 62),\
              scriptedvided.r6sText('1600x900, low settings', 111,  71),\
              scriptedvided.r6sText('1280x720, low settings', 121,  82),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "PUBG",\
"audio" : {"timestamps" : ("02:14", "02:35" ), "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Battlefield V",\
"audio" : {"timestamps" : ("02:35", "03:14" ), "padding" : 0.25  },\
"overlay" : { \
    "text" : ["'Battlefield V'",\
              scriptedvided.r6sText('1920x1080, low settings', 68, 51),\
              scriptedvided.r6sText('1600x900, low settings', 79, 60),\
              scriptedvided.r6sText('1280x720, low settings', 91, 65),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "Control",\
"audio" : {"timestamps" : ("03:14", "03:39" ), "padding" : 0.25  },\
"overlay" : { \
    "text" : ["'Control'",\
              scriptedvided.r6sText('1920x1080, low settings', 66, 42),\
              scriptedvided.r6sText('1280x720, low settings', 131, 85),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "Rainbow Six: Siege",\
"audio" : {"timestamps" : ("03:39", "04:06" ), "padding" : 0.25  },\
"overlay" : { \
    "text" : ["'Rainbow Six\: Siege'",\
              scriptedvided.r6sText('1920x1080, low settings, 100% render scale', 119, 92), \
              scriptedvided.r6sText('1280x720, low settings, 100% render scale', 185, 128),\
              scriptedvided.r6sText('1920x1080, low settings, 50% render scale', 154, 111),\
              scriptedvided.r6sText('1280x720, low settings, 50% render scale', 206, 137)]\
}, \
})

configs["episodes"].append(\
{ "title": "Grand Theft Auto V",\
"audio" : {"timestamps" : ("04:06", "04:27" ), "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "CS2",\
"audio" : {"timestamps" : ("04:27", "05:04" ), "padding" : 0.25  },\
"overlay" : { \
    "text" : ["'Counter-Strike 2'",\
              scriptedvided.r6sText('1920x1080, low settings', 125, 62),\
              scriptedvided.r6sText('1280x720, low settings', 143,  64),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "DOTA2",\
"audio" : {"timestamps" : ("05:04", "05:23" ), "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Fortnite",\
"audio" : {"timestamps" : ("05:23", "06:02" ), "padding" : 0.25  },\
"overlay" : { \
    "text" : ["'Fortnite'",\
              scriptedvided.r6sText('1920x1080, performance mode', 122, 28),\
              scriptedvided.r6sText('1600x900, performance mode',  133, 47),\
              scriptedvided.r6sText('1280x720, performance mode',  145, 80)]\
}, \
})


configs["episodes"].append(\
{ "title": "Overwatch 2",\
"audio" : {"timestamps" : ("06:02", "06:45" ), "padding" : 0.25  },\
"overlay" : { \
    "text" : ["'Overwatch 2'",\
              scriptedvided.r6sText('1920x1080, low settings', 185, 140),\
              scriptedvided.r6sText('1600x900, low settings', 254 , 197),\
              scriptedvided.r6sText('1280x720, low settings',  351, 270),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "Rocket League",\
"audio" : {"timestamps" : ("06:45", "07:08" ), "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings, 100% render scale", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Splitgate",\
"audio" : {"timestamps" : ("07:08", "07:33" ), "padding" : 0.25  },\
"overlay" : { \
    "text" : ["'Splitgate'",\
              scriptedvided.r6sText('1920x1080, low settings, 100% render scale', 137, 89),\
              scriptedvided.r6sText('1280x720, low settings, 100% render scale', 196 , 118),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "Valorant",\
"audio" : {"timestamps" : ("07:33", "08:02" ), "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Genshin Impact",\
"audio" : {"timestamps" : ("08:02", "08:42" ), "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings, 1.0 render scale", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "HiRez Studios trio (Paladins, Realm Royale, Rogue Company)",\
"audio" : {"timestamps" : ("08:42", "08:53" ), "volume" : 0.999 , "padding" : 0.25  },\
"video" : {"file":"HiRezTrio-P_aladins_R_ealmRoyale_R_ogueCompany.mp4"}\
})

configs["episodes"].append(\
{ "title": "Paladins",\
"isChapter" : False,\
"audio" : {"timestamps" : ("08:53", "09:00.5" ), "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, high settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Realm Royale",\
"isChapter" : False,\
"audio" : {"timestamps" : ("09:00.5", "09:09" ), "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, high settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Rogue Company",\
"isChapter" : False,\
"audio" : {"timestamps" : ("09:09", "09:18" ), "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})


configs["episodes"].append(\
{ "title": "World of Tanks Blitz",\
"audio" : {"timestamps" : ("09:18", "09:46" ), "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, high settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Warframe",\
"audio" : {"timestamps" : ("09:46", "10:12" ), "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
"video" : "stock_Warframe_Mariana.mp4",\
})

configs["episodes"].append(\
{ "title": "Resident Evil 4 (Remake)",\
"audio" : {"timestamps" : ("10:12", "10:46" ), "padding" : 0.25  },\
"video" : {"file": "stock_re4demo_choppyExceptCutscenes.mp4", "start" : "03:07"},\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
}, \
})
####################### end of gaming section ###############################


####################### conclusion ###############################

configs["episodes"].append(\
{ "title": "Conclusions",\
"audio" : {"timestamps" : ("10:46", "11:07.7" ), "volume" : 0.999 , "padding" : 0.25  },\
"video" : {"file" : "breel_r9_280_outside.mp4"}\
})

configs["episodes"].append(\
{ "title": "280 prices on OLX",\
"isChapter" : False,\
"audio" : {"timestamps" : ("11:07.7", "11:25" ), "volume" : 0.999 , "padding" : 0.25  },\
"video" : {"file" : "R9_280_breelAndPricing.mp4"}\
})

configs["episodes"].append(\
{ "title": "Robocop fails to launch",\
"isChapter" : False,\
"audio" : {"timestamps" : ("11:25", "11:34.5" ), "volume" : 0.999 , "padding" : 0.25  },\
"video" : {"file" : "r9_280_Robocop.mp4"}\
})


configs["episodes"].append(\
{ "title": "R9 290X",\
"isChapter" : False,\
"audio" : {"timestamps" : ("11:34.5", "11:45" ), "volume" : 0.999 , "padding" : 0.25  },\
"video" : {"file" : "breel_r9_290x_outside_dog.mp4"}\
})

configs["episodes"].append(\
{ "title": "bye",\
"isChapter" : False,\
"audio" : {"timestamps" : ("11:45", "11:52" ), "volume" : 0.999 , "padding" : 0.25  },\
"video" : {"file" : "breel_r9_280_outside.mp4"}\
})


##configs["episodes"].append(\
##{ "title": "Blooper",\
##"isChapter" : False,\
##"audio" : {"timestamps" : ( "13:40.5", "14:04.2") },\
##"video" : {"file":"HiRezTrio-P_aladins_R_ealmRoyale_R_ogueCompany.mp4"}\
##})

#scriptedvided.makeVideoForEpisode(configs["episodes"][25], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][29], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][30], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][31], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][32], configs)
#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "Splitgate"][0], configs)
scriptedvided.makeVideo(configs)

