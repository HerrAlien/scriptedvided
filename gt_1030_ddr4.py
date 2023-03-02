import scriptedvided

configs = { "defaultAudioFile" : "ddr4_1030.ogg",\
"mediaFolder" : "C:\\Users\\Admin\\Videos\\gt_1030_ddr4", \
"stockFolder" : "C:\\Users\\Admin\\Videos\stock",\
"benchmarkFile" : "C:\\Users\\Admin\\Videos\\gt_1030_ddr4\\Benchmark_gt_1030_ddr4.txt",\
"outputFolder" : "C:\\Users\\Admin\\Videos\\gt_1030_ddr4\\output", \
"outputFile" : "gt_1030_ddr4.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#00800080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "H:\\Muzica\\royalty free\\Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3",\
"timestamps" : ("00:30", None ), "destinationTimestamp" : {"title" : "The TLDW", "until" : "Apex Legends"}}, \
{"file" : "H:\\Muzica\\royalty free\\bensound-summer.mp3", "timestamps" : ("00:00", None ), "destinationTimestamp" : { "title": "Usefulness of used GPUs", "until" : "Blooper" }}, \
], "volume" : 0.03 },\
"episodes" : [],\
"youtube" : {"title" : "Is the DDR4 GT 1030 good for gaming?", \
"description" : '''The GT 1030 was a budget card from the Pascal series that was launched twice, first time with GDDR5, and the second time around with DDR4. This time, we're testing the DDR4 version.''',\
"links" : '''
More games tested with the GT 1030 DDR4:
https://www.youtube.com/watch?v=dzQNAsrHEDs
https://www.youtube.com/watch?v=r0aD25yFj9o

GT 1030 GDDR5 variant review: https://www.youtube.com/watch?v=_E-pguX_fJc
R7 250 review: https://youtu.be/L4oFUVoxIzs
Fermi GT 430 review: https://www.youtube.com/watch?v=-1eIjIxfx0k

TechPowerup entry: https://www.techpowerup.com/gpu-specs/geforce-gt-1030-ddr4.c3187

Intel 11th gen processors:
The core i5 11400 (has an IGPU): https://ark.intel.com/content/www/us/en/ark/products/212270/intel-core-i511400-processor-12m-cache-up-to-4-40-ghz.html
The core i5 11400F (no IGPU): https://ark.intel.com/content/www/us/en/ark/products/212271/intel-core-i511400f-processor-12m-cache-up-to-4-40-ghz.html
''', \
"tags" : "NVidia,GeForce,Pascal,GT1030,GT 1030,CUDA,ASUS",\
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

''' Go for the Phoenix name + Hollow from dark souls. Broll with the asus?'''
configs["episodes"].append(\
{ "title": "The TLDW",\
"audio" : {"timestamps" : ("00:00", "00:13.5" ), "volume" : 0.999 },\
"video" : "gt_1030_ddr4_bb_card_only.mp4"\
})

configs["episodes"].append(\
{ "title": "(Shorter) Rant: the old trick - use the same name",\
"audio" : {"timestamps" : ( "00:13.5", "00:29" ), "volume" : 0.999 },\
"video" : "710_family_2.mkv"\
})

configs["episodes"].append(\
{ "title": "(Shorter) Rant: the protagonists",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:29", "00:40.5" ), "volume" : 0.999 },\
"video" : "1030_family.mkv"\
})

''' Go for the bandwidth values. Maybe a BROLL with the kfa2 and asus ? '''
configs["episodes"].append(\
{ "title": "GDDR5 vs DDR4",\
"audio" : {"timestamps" : ("00:40.5", "00:59" ), "volume" : 0.999 },\
"isChapter" : False,\
"video" : "gt_1030_side_by_side.mp4"\
})

''' Go for the bandwidth values. Maybe a BROLL with the kfa2 and asus ? '''
configs["episodes"].append(\
{ "title": "GPU",\
"audio" : {"timestamps" : ("00:59", "01:36" ), "volume" : 0.999 },\
"video" : "gt_1030_ddr4_techpowerup.mkv"\
})

configs["episodes"].append(\
{ "title": "Cooling and thermals",\
"audio" : {"timestamps" : ( "01:36", "02:02" ), "volume" : 0.999 },\
"video" : "gt_1030_ddr4_bb_card_only.mp4",\
})

configs["episodes"].append(\
{ "title": "Cooling and thermals - thermals",\
"audio" : {"timestamps" : ( "02:02", "02:20" ), "volume" : 0.999 },\
"video" : "stock_heaven720p_noTessellation.mp4",\
"isChapter" : False,\
})


configs["episodes"].append(\
{ "title": "Apex Legends",\
"audio" : {"timestamps" : ("02:20", "02:56.7" ), "volume" : 0.97  },\
"overlay" : { \
    "text" : ["'Apex Legends'",\
              scriptedvided.r6sText('1920x1080, low settings',35, 28),\
              scriptedvided.r6sText('1280x720, low settings',64, 50),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "CoD Warzone",\
"audio" : {"timestamps" : ( "02:56.7", "03:17" ) , "volume" : 0.97 },\
"video" : "gt_1030_ddr4_Warzone_Lobby.mp4",\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Battlefield V",\
"audio" : {"timestamps" : ("03:17", "03:39.5" ) , "volume" : 0.97 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Control",\
"video" : "stock_Control_720p.mp4",\
"audio" : {"timestamps" : ("03:39.5", "04:06.5") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
}, \
})

####### this needs to be recorded!!
configs["episodes"].append(\
{ "title": "Rainbow Six: Siege",\
"audio" : {"timestamps" : ("13:04", "13:26.5"), "padAudio" : 5},\
"overlay" : { \
    "text" : ["'Rainbow Six\: Siege'",\
              scriptedvided.r6sText('1920x1080, low settings, 100% render scale', 34, 30), \
              scriptedvided.r6sText('1280x720, low settings, 100% render scale', 51, 42),\
              scriptedvided.r6sText('1920x1080, low settings, 50% render scale', 67, 53),\
              scriptedvided.r6sText('1280x720, low settings, 50% render scale', 94, 70)]\
}, \
})

configs["episodes"].append(\
{ "title": "Alien: Isolation",\
"audio" : {"timestamps" : ("04:06.5","04:34") },\
"video" : "stock_Alien_Isolation_1080p.mp4",\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, ultra settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Counter Strike: Global Offensive",\
"audio" : {"timestamps" : ("04:34", "05:01.5") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "DOTA2",\
"audio" : {"timestamps" : ("05:01.5", "05:32"), "volume" : 0.97 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings, 100% render scale", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Fortnite",\
"audio" : {"timestamps" : ("05:32", "06:04.5") },\
"video" : "stock_Fortnite_c3s1.mp4",\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, performance mode, view distance FAR, 100% render scale", \
    }\
}, \
})


configs["episodes"].append(\
{ "title": "Rocket League",\
"audio" : {"timestamps" : ("06:04.5", "06:36") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings, 100% render scale", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Splitgate",\
"audio" : {"timestamps" : ("06:36", "07:11") },\
"overlay" : { \
    "text" : ["'Splitgate'",\
              scriptedvided.r6sText('1920x1080, low settings',39, 5),\
              scriptedvided.r6sText('1280x720, low settings',69, 34),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "Valorant",\
"audio" : {"timestamps" : ("07:11", "08:08") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Genshin Impact",\
"audio" : {"timestamps" : ("08:08", "08:30") , "volume" : 0.99 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings, 1.0 render scale", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Overwatch 2",\
"audio" : {"timestamps" : ("08:30", "09:13") },\
"overlay" : { \
    "text" : ["'Overwatch 2'",\
              scriptedvided.r6sText('1920x1080, low settings',41, 33),\
              scriptedvided.r6sText('1600x900, low settings',57, 45),\
              scriptedvided.r6sText('1280x720, low settings',83, 64),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "Paladins",\
"audio" : {"timestamps" : ("09:13", "09:39.2") , "volume" : 0.97 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, high settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Realm Royale",\
"audio" : {"timestamps" : ( "09:39.2", "10:03.5" ) },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, high settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Rogue Company",\
"audio" : {"timestamps" : ("10:03.5", "10:30") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "World of Tanks Blitz",\
"audio" : {"timestamps" : ("10:30", "10:50.5") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, high settings", \
    }\
}, \
})


configs["episodes"].append(\
{ "title": "Warframe",\
"audio" : {"timestamps" : ("10:50.5", "11:11.5") },\
"video" : "stock_Warframe_training_720pLow.mp4",\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

## this can be copy-pasted, it uses a stock video with the audio already
## overlayed. Pass in a fake audio stream, at -60dB
configs["episodes"].append(\
{ "title": "Usefulness of used GPUs",\
"audio" : {"timestamps" : ("00:00", "01:17"), "volume" : 0.001 },\
"video" : "Usefulness of used GPUs.mp4"\
})

configs["episodes"].append(\
{ "title": "Usefulness of the GT 1030 DDR4",\
"audio" : {"timestamps" : ("11:11.5", "11:37.5"), "volume" : 0.999 },\
"video" : "gt_1030_ddr4_bb_card_only.mp4"\
})

configs["episodes"].append(\
{ "title": "pricing new",\
"audio" : {"timestamps" : ("11:37.5", "11:52.5") },\
"video" : "gt_1030_emag.mkv",
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Display adapter",\
"audio" : {"timestamps" : ("11:52.5", "12:13.7"), "volume" : 0.999 },\
"video" :  "FermiGT730_breel_card.mp4",\
"isChapter" : False,\
})



configs["episodes"].append(\
{ "title": "Personal notes for the ASUS GT 1030",\
"audio" : {"timestamps" : ("12:13.7", "12:27"), "volume" : 0.999},\
"video" : "gt_1030_ddr4_bb_card_only.mp4"\
})

configs["episodes"].append(\
{ "title": "1030 new vs 1060 used",\
"audio" : {"timestamps" : ( "12:27", "12:49"), "volume" : 0.999 },\
"video" : "1030_new_vs_1060_used.mkv",
"isChapter" : False,\
})


configs["episodes"].append(\
{ "title": "Blooper",\
"audio" : {"timestamps" : ("12:49", "13:04"), "volume" : 0.999},\
"video" : "1030_gddr5_dominating.mp4",
"isChapter" : False,\
})

#scriptedvided.makeVideoForEpisode(configs["episodes"][27], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][9], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][8], configs)
#print(scriptedvided.makeVideoForEpisode(configs["episodes"][9], configs))
#print(scriptedvided.getSuitableVideoStream(configs["episodes"][9], configs))
#print (configs["youtube"])
#print(scriptedvided.getMusicCreditsString(configs["backgroundTrack"]))
#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "Usefulness of the HD 6850"][0], configs)
#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "CoD Warzone"][0], configs)
scriptedvided.makeVideo(configs)

