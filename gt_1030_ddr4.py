import scriptedvided

configs = { "defaultAudioFile" : "gt_1030.ogg",\
"mediaFolder" : "C:\\Users\\Admin\\Videos\\gt_1030", \
"stockFolder" : "C:\\Users\\Admin\\Videos\stock",\
"benchmarkFile" : "C:\\Users\\Admin\\Videos\\gt_1030\\Benchmark_gt1030.txt",\
"outputFolder" : "C:\\Users\\Admin\\Videos\\gt_1030\\output", \
"outputFile" : "gt_1030.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#00800080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "H:\\Muzica\\royalty free\\Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3",\
"timestamps" : ("00:30", None ), "destinationTimestamp" : {"title" : "Context of the launch", "until" : "Apex Legends"}}, \
{"file" : "H:\\Muzica\\royalty free\\bensound-summer.mp3", "timestamps" : ("00:00", None ), "destinationTimestamp" : { "title": "Usefulness of used GPUs", "until" : "Blooper" }}, \
], "volume" : 0.03 },\
"episodes" : [],\
"youtube" : {"title" : "The NVidia GT 1030 in 2022", \
"description" : '''The GT 1030 was a budget card from the Pascal series that was launched twice, first time with GDDR5, and the second time around with DDR4. Let's see how the GDDR5 KFA2 card behaves in 2022.''',\
"links" : '''
More games tested with the GT 1030 DDR4:
https://www.youtube.com/watch?v=dzQNAsrHEDs
https://www.youtube.com/watch?v=r0aD25yFj9o

TechPowerup entry: https://www.techpowerup.com/gpu-specs/geforce-gt-1030-ddr4.c3187

Intel 11th gen processors:
The core i5 11400 (has an IGPU): https://ark.intel.com/content/www/us/en/ark/products/212270/intel-core-i511400-processor-12m-cache-up-to-4-40-ghz.html
The core i5 11400F (no IGPU): https://ark.intel.com/content/www/us/en/ark/products/212271/intel-core-i511400f-processor-12m-cache-up-to-4-40-ghz.html

NVidia Special Event (Pascal): https://www.youtube.com/watch?v=0xnzwjPyx8A
GT 1030 GDDR5 variant review: https://www.youtube.com/watch?v=_E-pguX_fJc
R7 250 review: https://youtu.be/L4oFUVoxIzs
Fermi GT 430 review: https://www.youtube.com/watch?v=-1eIjIxfx0k
''', \
"tags" : "NVidia,GeForce,Pascal,GT1030,GT 1030,CUDA,KFA2",\
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
{ "title": "TLDW",\
"audio" : {"timestamps" : ("00:00", "00:22" ), "volume" : 0.999 },\
"video" : "nvidia_Pascal.mkv"\
})

''' Go for the bandwidth values. Maybe a BROLL with the kfa2 and asus ? '''
configs["episodes"].append(\
{ "title": "GDDR5 vs DDR4",\
"audio" : {"timestamps" : ("00:22", "00:31" ), "volume" : 0.999 },\
"isChapter" : False,\
"video" : "gddr5_ddr4_gt_1030.mkv"\
})


configs["episodes"].append(\
{ "title": "Cooling and thermals",\
"audio" : {"timestamps" : ( "02:08", "02:24" ), "volume" : 0.999 },\
"video" : {"file" : "GT1030_cooling.MOV", "rotation" : -90},\
})

configs["episodes"].append(\
{ "title": "Cooling and thermals - thermals Heaven",\
"audio" : {"timestamps" : ( "02:24", "02:53" ), "volume" : 0.999 },\
"video" : "fixed_GT1030_heaven.MOV",\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Cooling and thermals - thermals Warframe",\
"audio" : {"timestamps" : ( "02:24", "02:53" ), "volume" : 0.999 },\
"video" : "fixed_GT1030_heaven.MOV",\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Apex Legends",\
"audio" : {"timestamps" : ("03:14", "03:44" ), "volume" : 0.97  },\
"overlay" : { \
    "text" : ["'Apex Legends'",\
              scriptedvided.r6sText('1920x1080, low settings',35, 28),\
              scriptedvided.r6sText('1280x720, low settings',64, 50),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "CoD Warzone",\
"audio" : {"timestamps" : ("03:44", "04:08" ) , "volume" : 0.97 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Battlefield V",\
"audio" : {"timestamps" : ("04:08", "04:31" ) , "volume" : 0.97 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Control",\
"audio" : {"timestamps" : ("04:31", "05:03.5") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Rainbow Six: Siege",\
"audio" : {"timestamps" : ("05:03.5", "05:45"), "padAudio" : 5},\
"overlay" : { \
    "text" : ["'Rainbow Six\: Siege'",\
              scriptedvided.r6sText('1920x1080, low settings, 100% render scale', 34, 30), \
              scriptedvided.r6sText('1280x720, low settings, 100% render scale', 67, 53),\
              scriptedvided.r6sText('1920x1080, low settings, 50% render scale', 51, 42),\
              scriptedvided.r6sText('1280x720, low settings, 50% render scale', 94, 70)]\
}, \
})

configs["episodes"].append(\
{ "title": "Alien: Isolation",\
"audio" : {"timestamps" : ("05:45","06:09") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, ultra settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Counter Strike: Global Offensive",\
"audio" : {"timestamps" : ("06:09", "06:32") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "DOTA2",\
"audio" : {"timestamps" : ("06:32", "06:54.5"), "volume" : 0.97 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings, 100% render scale", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Fortnite",\
"audio" : {"timestamps" : ("06:54.5", "07:20") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, performance mode, view distance FAR, 100% render scale", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Rocket League",\
"audio" : {"timestamps" : ("07:20", "07:42") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings, 100% render scale", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Splitgate",\
"audio" : {"timestamps" : ("07:42", "08:14") },\
"overlay" : { \
    "text" : ["'Splitgate'",\
              scriptedvided.r6sText('1920x1080, low settings',39, 5),\
              scriptedvided.r6sText('1280x720, low settings',75, 48),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "Valorant",\
"audio" : {"timestamps" : ("08:14", "08:44") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Genshin Impact",\
"audio" : {"timestamps" : ("08:44", "09:07") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings, 1.0 render scale", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Overwatch 2",\
"audio" : {"timestamps" : ("09:07", "09:35.5") },\
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
"audio" : {"timestamps" : ("09:35.5", "09:59") , "volume" : 0.97 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, high settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Realm Royale",\
"audio" : {"timestamps" : ("09:59", "10:30" ) },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, high settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Rogue Company",\
"audio" : {"timestamps" : ("10:30", "10:53") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "World of Tanks Blitz",\
"audio" : {"timestamps" : ("10:53", "11:11") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, high settings", \
    }\
}, \
})


configs["episodes"].append(\
{ "title": "Warframe",\
"audio" : {"timestamps" : ("11:11", "11:45") },\
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
"audio" : {"timestamps" : ("10:58.7", "11:30.45"), "volume" : 0.999 },\
"video" : "office_pc_gt_1030.mkv"\
})

configs["episodes"].append(\
{ "title": "pricing new",\
"audio" : {"timestamps" : ("11:46", "12:00") },\
"video" : "gt_1030_emag.mkv",
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "pricing OLX",\
"audio" : {"timestamps" : ( "12:00", "12:08.2") },\
"video" : "gt_1030_olx.mkv",
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Personal notes for the KFA2 GT 1030",\
"audio" : {"timestamps" : ("12:08.2", "12:30"), "volume" : 0.999},\
"video" : "stock_GenshinImpact_1080pLow.mp4"\
})

configs["episodes"].append(\
{ "title": "Blooper",\
"audio" : {"timestamps" : ("00:00", "00:15"), "volume" : 0.001},\
"video" : "gt1030_blooper.MOV",
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
#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "Warframe"][0], configs)
scriptedvided.makeVideo(configs)

