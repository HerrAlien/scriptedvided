import scriptedvided

configs = { "defaultAudioFile" : "r7_260.ogg",\
"mediaFolder" : "C:\\Users\\Admin\\Videos\\r7 260", \
"stockFolder" : "C:\\Users\\Admin\\Videos\stock",\
"outputFolder" : "C:\\Users\\Admin\\Videos\\r7 260\\output", \
"outputFile" : "r7_260.mp4", \
"benchmarkFile" : "C:\\Users\\Admin\\Videos\\r7 260\\Benchmark_r7_260.txt",\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "H:\\Muzica\\royalty free\\Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3",\
"timestamps" : ("00:30", "03:02" ), "destinationTimestamp" : "00:00"}, \
{"file" : "H:\\Muzica\\royalty free\\bensound-summer.mp3", "timestamps" : ("00:00", "02:46" ), "destinationTimestamp" : { "title": "Usefulness of used GPUs"}}, \
], "volume" : 0.05 },\
"episodes" : [],\
"youtube" : {"title" : "The AMD Radeon R7 260 in 2022", \
"description" : '''The Radeon R7 260 was another GCN mid-range card, released after the HD7000 series got renamed to the R7/R9 200 series.''',\
"links" : '''
More games tested with the R7 260/r7 360:
https://www.youtube.com/watch?v=tVQyUkfJnbU

TechPowerup entry:
https://www.techpowerup.com/gpu-specs/asus-r7-260-1-gb.b2732

Intel 11th gen processors:
The core i5 11400 (has an IGPU): https://ark.intel.com/content/www/us/en/ark/products/212270/intel-core-i511400-processor-12m-cache-up-to-4-40-ghz.html
The core i5 11400F (no IGPU): https://ark.intel.com/content/www/us/en/ark/products/212271/intel-core-i511400f-processor-12m-cache-up-to-4-40-ghz.html

Other resources used:
RX 6500xt review: https://www.youtube.com/watch?v=M5_oM3Ow_CI
AMD Press Conference, Sydney 2013: https://www.youtube.com/watch?v=gbDO9Zz-MQ8
''', \
"tags" : "AMD,Radeon,R7 260, R7 360,GCN",\
"language" : "EN", \
"Caption certification" : "None",\
"recording date" : None,\
"video location" : None, \
"category" : "Science & Technology", \
"subtitles" : None, \
"endscreen" : None, \
"cards" : None, \
}\
}

configs["episodes"].append(\
{ "title": "Context of the launch",\
"audio" : {"timestamps" : ("00:00", "00:46" ), "volume" : 0.999 },\
"video" : "r7_r9_gcn_launch.mp4"\
})

configs["episodes"].append(\
{ "title": "VCE rant",\
"audio" : { "file": "has_video_encoding.ogg", "volume" : 0.999 },\
"video" : "6500xt_rant.mkv",\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "The GPU",\
"audio" : {"timestamps" : ("00:46", "01:27" ), "volume" : 0.999 },\
"video" : "r7_260_techpowerup.mp4"\
})

configs["episodes"].append(\
{ "title": "Thermal results",\
"audio" : {"timestamps" : ("01:27", "01:50" ), "volume" : 0.999 },\
"video" : "r7_260_1.MOV"\
})

configs["episodes"].append(\
{ "title": "Apex Legends",\
"audio" : {"timestamps" : ("01:50", "02:26" ), "volume" : 0.97  },\
"video" : "stock_ApexLegends_1080p.mp4", \
"overlay" : { \
    "text" : ["'Apex Legends'",\
              "'1080p, low settings - Average\: 57fps, 1\\\% lows\: 35fps'",\
              "'720p, low settings - Average\: 75fps, 1\\\% lows\: 50fps'"]\
}, \
})

configs["episodes"].append(\
{ "title": "CoD Warzone",\
"audio" : {"timestamps" : ("02:26", "02:52" ) , "volume" : 0.97 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "720p, low settings", \
    }\
}, \
})


configs["episodes"].append(\
{ "title": "Battlefield V",\
"audio" : {"timestamps" : ("02:52","03:20" ) },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "720p, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Control",\
"audio" : {"timestamps" : ("03:20", "03:47") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "720p, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Rainbow Six: Siege",\
"audio" : {"timestamps" : ("03:47", "04:39") },\
"overlay" : { \
    "text" : ["'Rainbow Six\: Siege'",\
              "'1080p, low settings, 100\\\% render scale - Average\: 61fps, 1\\\% lows\: 49fps'",\
              "'720p, low settings, 100\\\% render scale - Average\: 120fps, 1\\\% lows\: 86fps'",\
              "'1080p, low settings, 50\\\% render scale - Average\: 88fps, 1\\\% lows\: 67fps'",\
              "'720p, low settings, 50\\\% render scale - Average\: 156fps, 1\\\% lows\: 103fps'"]\
}, \
})

configs["episodes"].append(\
{ "title": "Alien: Isolation",\
"audio" : {"timestamps" : ("04:39","04:59") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1080p, ultra settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Counter Strike: Global Offensive",\
"audio" : {"timestamps" : ("04:59", "05:30") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1080p, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "DOTA2",\
"audio" : {"timestamps" : ("05:30", "05:57"), "volume" : 0.97 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1080p, low settings, 100% render scale", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Fortnite",\
"audio" : {"timestamps" : ("05:57", "06:24") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1080p, performance mode, view distance FAR, 100% render scale", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Rocket League",\
"audio" : {"timestamps" : ("06:24", "06:44") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1080p, low settings, 100% render scale", \
    }\
}, \
})


configs["episodes"].append(\
{ "title": "Splitgate",\
"audio" : {"timestamps" : ("06:45", "07:19") },\
"overlay" : { \
    "text" : ["'Splitgate'",\
              "'1080p, low settings - Average\: 83fps, 1\\\% lows\: 38fps'",\
              "'720p, low settings - Average\: 119fps, 1\\\% lows\: 56fps'"]\
}, \
})

configs["episodes"].append(\
{ "title": "Valorant",\
"audio" : {"timestamps" : ("07:19", "07:44") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1080p, low settings", \
    }\
}, \
})


configs["episodes"].append(\
{ "title": "Genshin Impact",\
"audio" : {"timestamps" : ("07:44", "08:00") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1080p, low settings, 1.0 render scale", \
    }\
}, \
})


configs["episodes"].append(\
{ "title": "Paladins",\
"audio" : {"timestamps" : ("08:00", "08:20") , "volume" : 0.97 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1080p, high settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Realm Royale",\
"audio" : {"timestamps" : ("08:20", "08:43") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1080p, high settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Rogue Company",\
"audio" : {"timestamps" : ("08:43", "09:08") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1080p, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "World of Tanks Blitz",\
"audio" : {"timestamps" : ("09:08", "09:28") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1080p, high settings", \
    }\
}, \
})


configs["episodes"].append(\
{ "title": "Warframe",\
"audio" : {"timestamps" : ("09:28", "09:52") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1080p, high settings", \
    }\
}, \
})


configs["episodes"].append(\
{ "title": "Usefulness of used GPUs",\
})

configs["episodes"].append(\
{ "title": "Usefulness of the R7 260",\
"audio" : {"timestamps" : ("09:52", "10:46") },\
"video" : "r7_260_Control.mp4"\
})

configs["episodes"].append(\
{ "title": "Personal notes for the R7 260",\
"audio" : {"timestamps" : ("10:46", "11:17"), "volume" : 0.999},\
"video" : "r7_260_1.MOV"\
})

#scriptedvided.makeVideoForEpisode(configs["episodes"][1], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][9], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][8], configs)
#print(scriptedvided.makeVideoForEpisode(configs["episodes"][9], configs))
#print(scriptedvided.getSuitableVideoStream(configs["episodes"][9], configs))
#print (configs["youtube"])
#print(scriptedvided.getMusicCreditsString(configs["backgroundTrack"]))
scriptedvided.makeVideo(configs)

