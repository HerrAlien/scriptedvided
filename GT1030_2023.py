import scriptedvided

configs = { "defaultAudioFile" : "GT1030_2023.ogg",\
"mediaFolder" : "F:\\Videos\\GT1030_2023", \
"stockFolder" : "F:\\Videos\\stock",\
"benchmarkFile" : "F:\\Videos\\GT1030_2023\\Benchmark_GT_1030_2023.txt",\
"outputFolder" : "F:\\Videos\\GT1030_2023\\output", \
"outputFile" : "GT1030_2023.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#00800080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3",\
"timestamps" : ("00:30", None ), "destinationTimestamp" : {"title" : "What 30W TDP can get you", "until" : "Alien: Isolation"}}, \
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
"youtube" : {"title" : "Playing games on the little Pascal that could (GT 1030)", \
"description" : '''In this video we're testing the 30W TDP tiny GT 1030.
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

Previous reviews for the GPU:
KFA2 version (GDDR5): https://youtu.be/_E-pguX_fJc
Asus Phoenix (DDR4 variant): https://youtu.be/gI98DutuIis

Techpowerup entry: https://www.techpowerup.com/gpu-specs/asus-gt-1030.b5707
Office PC and GT 1030 (Tech Yes City): https://www.youtube.com/watch?v=yP4z2Vdmf1o

''', \
"tags" : "NVidia,Pascal,GT1030,GT 1030,GP108",\
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
{ "title": "What 30W TDP can get you",\
"audio" : {"timestamps" : ("00:00", "00:13" ), "volume" : 0.999, "padding" : 0.25 },\
"video" : {"file": "breel_AsusLP_GT1030_outside.mp4"}\
})

configs["episodes"].append(\
{ "title": "The GPU",\
"audio" : {"timestamps" : ("00:13", "00:30.5" ), "volume" : 0.999, "padding" : 0.25 },\
"video" : {"file" : "AsusLP_GT1030_HeavenGpuZ_2.mp4"}\
})

configs["episodes"].append(\
{ "title": "Cooling and thermals",\
"audio" : {"timestamps" : ("00:30.5", "00:49" ), "volume" : 0.999, "padding" : 0.25 },\
"video" : {"file": "breel_Gt1030_family_outside.mp4"}\
})

configs["episodes"].append(\
{ "title": "Temperatures",\
"isChapter" : False, \
"audio" : {"timestamps" : ("00:49", "01:02" ), "volume" : 0.999, "padding" : 0.25 },\
"overlay" : { \
    "text" : ["'Thermals'",\
              "'Heaven\: 65C (40C delta over ambient)'",\
              "'Warframe\: 65C (40C delta over ambient)'",\
    ]\
}, \
"video" : {"file": "AsusGt1030LP_cooling.mp4", "rotation" : 90}\
})

configs["episodes"].append(\
{ "title": "The test system",\
"audio" : {"timestamps" : ("01:02", "01:15" ), "volume" : 0.999, "padding" : 0.25 },\
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
"audio" : {"timestamps" : ("01:15", "01:31" ), "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, ultra settings", \
    }\
}, \
})

# this needs a longer stock video
configs["episodes"].append(\
{ "title": "Apex Legends",\
"audio" : {"timestamps" : ("01:31", "02:09" ), "padding" : 0.25  },\
"overlay" : { \
    "text" : ["'Apex Legends'",\
              scriptedvided.r6sText('1920x1080, low settings', 62, 45),\
              scriptedvided.r6sText('1600x900, low settings', 79, 55 ),\
              scriptedvided.r6sText('1280x720, low settings', 102, 71 ),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "Resident Evil 4 (Remake)",\
"audio" : {"timestamps" : ("02:09", "02:29" ), "padding" : 0.25  },\
"video" : {"file": "stock_re4demo_choppyExceptCutscenes.mp4", "start" : "03:07"},\
"overlay" : { \
    "text" : ["'Resident Evil 4 (Remake)'",\
              scriptedvided.r6sText('1920x1080, low settings', 19, 12),\
              scriptedvided.r6sText('1280x720, low settings', 31, 18 ),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "Battlefield V",\
"audio" : {"timestamps" : ("02:29", "02:57" ), "padding" : 0.25  },\
"overlay" : { \
    "text" : ["'Battlefield V'",\
              scriptedvided.r6sText('1920x1080, low settings', 32, 24),\
              scriptedvided.r6sText('1600x900, low settings', 39, 31),\
              scriptedvided.r6sText('1280x720, low settings', 51, 41),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "Control",\
"audio" : {"timestamps" : ("02:57", "03:24" ), "padding" : 0.25  },\
"overlay" : { \
    "text" : ["'Control'",\
              scriptedvided.r6sText('1920x1080, low settings', 25, 20),\
              scriptedvided.r6sText('1280x720, low settings', 51, 41),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "Rainbow Six: Siege",\
"audio" : {"timestamps" : ("03:24", "04:07" ), "padding" : 0.25  },\
"overlay" : { \
    "text" : ["'Rainbow Six\: Siege'",\
              scriptedvided.r6sText('1920x1080, low settings, 100% render scale', 61, 51), \
              scriptedvided.r6sText('1280x720, low settings, 100% render scale', 115, 82),\
              scriptedvided.r6sText('1920x1080, low settings, 50% render scale', 85, 66),\
              scriptedvided.r6sText('1280x720, low settings, 50% render scale', 134, 75)]\
}, \
})

configs["episodes"].append(\
{ "title": "Grand Theft Auto V",\
"audio" : {"timestamps" : ("04:07", "04:25" ), "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Counter-Strike 2",\
"audio" : {"timestamps" : ("04:25", "04:49" ), "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "DOTA2",\
"audio" : {"timestamps" : ("04:49", "05:09" ), "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Fortnite",\
"audio" : {"timestamps" : ("05:09", "05:43.5" ), "padding" : 0.25  },\
"overlay" : { \
    "text" : ["'Fortnite'",\
              scriptedvided.r6sText('1920x1080, performance mode', 103, 17), \
              scriptedvided.r6sText('1600x900, performance mode', 131, 84),\
              scriptedvided.r6sText('1280x720, performance mode', 153, 95)]\
}, \
})


configs["episodes"].append(\
{ "title": "Overwatch 2",\
"audio" : {"timestamps" : ("05:43.5", "06:20.6" ), "padding" : 0.25  },\
"overlay" : { \
    "text" : ["'Overwatch 2'",\
              scriptedvided.r6sText('1920x1080, low settings', 98, 76 ),\
              scriptedvided.r6sText('1600x900, low settings', 132,  105),\
              scriptedvided.r6sText('1280x720, low settings', 193 ,  148),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "Rocket League",\
"audio" : {"timestamps" : ("06:20.6", "06:37" ), "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings, 100% render scale", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Splitgate",\
"audio" : {"timestamps" : ("06:37", "07:00" ), "padding" : 0.25  },\
"video" : "stock_Splitgate_2023_06_17.mp4",\
"overlay" : { \
    "text" : ["'Splitgate'",\
              scriptedvided.r6sText('1920x1080, low settings, 100% render scale', 85,  46),\
              scriptedvided.r6sText('1280x720, low settings, 100% render scale', 143, 57 ),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "Valorant",\
"audio" : {"timestamps" : ("07:00", "07:18" ), "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "HiRez Studios trio (Paladins, Realm Royale, Rogue Company)",\
"audio" : {"timestamps" : ("07:18", "07:28" ), "volume" : 0.999 , "padding" : 0.25  },\
"video" : {"file":"HiRezTrio-P_aladins_R_ealmRoyale_R_ogueCompany.mp4"}\
})



configs["episodes"].append(\
{ "title": "Paladins",\
"isChapter" : False,\
"audio" : {"timestamps" : ("07:28", "07:35.7" ), "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, high settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Realm Royale",\
"isChapter" : False,\
"audio" : {"timestamps" : ("07:35.7", "07:43.7" ), "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, high settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Rogue Company",\
"isChapter" : False,\
"audio" : {"timestamps" : ("07:43.7", "07:51.5" ), "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "World of Tanks Blitz",\
"audio" : {"timestamps" : ("07:51.5", "08:07" ), "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, high settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Warframe",\
"audio" : {"timestamps" : ("08:07", "08:26" ), "padding" : 0.25  },\
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
"audio" : {"timestamps" : ("08:26", "08:36.3" ), "volume" : 0.999 , "padding" : 0.25  },\
"video" : {"file" : "office_pc_gt_1030.mkv", "start" : "00:00"}\
})

configs["episodes"].append(\
{ "title": "feels cheap",\
"isChapter" : False,\
"audio" : {"timestamps" : ("08:36.3", "08:45" ), "volume" : 0.999 , "padding" : 0.25  },\
"video" : {"file" : "breel_AsusLP_GT1030_outside.mp4"}\
})

configs["episodes"].append(\
{ "title": "soft spot for under 75W cards",\
"isChapter" : False,\
"audio" : {"timestamps" : ("08:45", "09:04" ), "volume" : 0.999 , "padding" : 0.25  },\
"video" : {"file" : "breel_Gt1030_family_outside.mp4"}\
})


configs["episodes"].append(\
{ "title": "bye",\
"isChapter" : False,\
"audio" : {"timestamps" : ("09:04", "09:11" ), "volume" : 0.999 , "padding" : 0.25  },\
"video" : {"file" : "breel_AsusLP_GT1030_outside.mp4"}\
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

