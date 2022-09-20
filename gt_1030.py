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
More games tested with the GT 1030:
https://www.youtube.com/watch?v=6GplcZaKbW8
https://www.youtube.com/watch?v=LZMuVTUvT7I

TechPowerup entries:
https://www.techpowerup.com/gpu-specs/kfa2-gt-1030.b4633
https://www.techpowerup.com/gpu-specs/geforce-gt-1030.c2954

Intel 11th gen processors:
The core i5 11400 (has an IGPU): https://ark.intel.com/content/www/us/en/ark/products/212270/intel-core-i511400-processor-12m-cache-up-to-4-40-ghz.html
The core i5 11400F (no IGPU): https://ark.intel.com/content/www/us/en/ark/products/212271/intel-core-i511400f-processor-12m-cache-up-to-4-40-ghz.html

NVidia Special Event (Pascal): https://www.youtube.com/watch?v=0xnzwjPyx8A
Office PC and GT 1030: https://www.youtube.com/watch?v=yP4z2Vdmf1o
R7 250 review: https://youtu.be/L4oFUVoxIzs
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

configs["episodes"].append(\
{ "title": "Context of the launch",\
"audio" : {"timestamps" : ("00:00", "00:22" ), "volume" : 0.999 },\
"video" : "nvidia_Pascal.mkv"\
})

configs["episodes"].append(\
{ "title": "GDDR5 vs DDR4",\
"audio" : {"timestamps" : ("00:22", "00:31" ), "volume" : 0.999 },\
"isChapter" : False,\
"video" : "gddr5_ddr4_gt_1030.mkv"\
})


configs["episodes"].append(\
{ "title": "The GPU",\
"audio" : {"timestamps" : ("00:31", "01:04" ), "volume" : 0.999 },\
"video" : "gt_1030_pcie_x4.mkv",\
})

configs["episodes"].append(\
{ "title": "Similar restrictions as R7 250",\
"audio" : {"timestamps" : ( "01:04", "01:25" ), "volume" : 0.999 },\
"isChapter" : False,\
"video" : "r7_250_pcie_bandwidth_limitations.mkv",\
})

configs["episodes"].append(\
{ "title": "KFA2 GT 1030",\
"audio" : {"timestamps" : ( "01:25", "02:08" ), "volume" : 0.999 },\
"isChapter" : False,\
"video" : "GT1030_techpowerup.mkv",\
})


configs["episodes"].append(\
{ "title": "Cooling and thermals",\
"audio" : {"timestamps" : ( "02:08", "02:24" ), "volume" : 0.999 },\
"video" : {"file" : "GT1030_cooling.MOV", "rotation" : -90},\
})

configs["episodes"].append(\
{ "title": "Cooling and thermals - thermals only",\
"audio" : {"timestamps" : ( "02:24", "02:53" ), "volume" : 0.999 },\
"video" : "fixed_GT1030_heaven.MOV",\
"isChapter" : False,\
})


## this can be copy-pasted, it uses a stock video with the audio already
## overlayed. Pass in a fake audio stream, at -60dB
configs["episodes"].append(\
{ "title": "Video capturing will impact performance",\
"audio" : {"timestamps" : ( "00:00", "00:24" ), "volume" : 0.001 },\
"video" : "Video capturing will impact performance.mkv",\
})


##configs["episodes"].append(\
##{ "title": "Cooling solution - axial",\
##"audio" : {"timestamps" : ("01:46", "02:07" ), "volume" : 0.9 },\
##"video" : "r7_260_1.mov",\
##"overlay" : { \
##    "text" : ["'Example of a cooler using axial fans'",\
##              "'(ASUS Radeon R7 260)'"]\
##}, \
##"isChapter" : False,\
##})


configs["episodes"].append(\
{ "title": "Apex Legends",\
"audio" : {"timestamps" : ("02:53", "03:21.3" ), "volume" : 0.97  },\
"overlay" : { \
    "text" : ["'Apex Legends'",\
              "'1080p, low settings - Average\: 60fps, 1\\\% lows\: 44fps'",\
              "'720p, low settings - Average\: 70fps, 1\\\% lows\: 54fps'"]\
}, \
})

configs["episodes"].append(\
{ "title": "CoD Warzone",\
"audio" : {"timestamps" : ("03:21.3", "03:49" ) , "volume" : 0.97 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "720p, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Battlefield V",\
"audio" : {"timestamps" : ("03:49", "04:20.6" ) , "volume" : 0.97 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "720p, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Control",\
"audio" : {"timestamps" : ("04:20.6", "04:44.13") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "720p, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Rainbow Six: Siege",\
"audio" : {"timestamps" : ("04:44.13", "05:18.5") },\
"overlay" : { \
    "text" : ["'Rainbow Six\: Siege'",\
              "'1080p, low settings, 100\\\% render scale - Average\: 54fps, 1\\\% lows\: 45ps'",\
              "'720p, low settings, 100\\\% render scale - Average\: 103fps, 1\\\% lows\: 81fps'",\
              "'1080p, low settings, 50\\\% render scale - Average\: 77fps, 1\\\% lows\: 63fps'",\
              "'720p, low settings, 50\\\% render scale - Average\: 137fps, 1\\\% lows\: 101fps'"]\
}, \
})

configs["episodes"].append(\
{ "title": "Alien: Isolation",\
"audio" : {"timestamps" : ("05:18.5","05:36.1") },\
"video" : "stock_Alien_Isolation_1080p.mp4",\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1080p, ultra settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Counter Strike: Global Offensive",\
"audio" : {"timestamps" : ("05:36.1", "06:28.3") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1080p, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "DOTA2",\
"audio" : {"timestamps" : ("06:28.3", "06:50.4"), "volume" : 0.97 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1080p, low settings, 100% render scale", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Fortnite",\
"audio" : {"timestamps" : ("06:50.4", "07:29.5") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1080p, performance mode, view distance FAR, 100% render scale", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Rocket League",\
"audio" : {"timestamps" : ("07:29.5", "07:53.4") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1080p, low settings, 100% render scale", \
    }\
}, \
})


configs["episodes"].append(\
{ "title": "Splitgate",\
"audio" : {"timestamps" : ("07:53.4", "08:16") },\
"overlay" : { \
    "text" : ["'Splitgate'",\
              "'1080p, low settings - Average\: 64fps, 1\\\% lows\: 31fps'",\
              "'720p, low settings - Average\: 107fps, 1\\\% lows\: 52fps'"]\
}, \
})

configs["episodes"].append(\
{ "title": "Valorant",\
"audio" : {"timestamps" : ("08:16", "08:53") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1080p, low settings", \
    }\
}, \
})


configs["episodes"].append(\
{ "title": "Genshin Impact",\
"audio" : {"timestamps" : ("08:53", "09:16") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1080p, low settings, 1.0 render scale", \
    }\
}, \
})


configs["episodes"].append(\
{ "title": "Paladins",\
"audio" : {"timestamps" : ("09:16", "09:35.5") , "volume" : 0.97 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1080p, high settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Realm Royale",\
"audio" : {"timestamps" : ("09:35.5", "09:55") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1080p, high settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Rogue Company",\
"audio" : {"timestamps" : ("09:55", "10:19.4") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1080p, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "World of Tanks Blitz",\
"audio" : {"timestamps" : ("10:19.4", "10:35") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1080p, high settings", \
    }\
}, \
})


configs["episodes"].append(\
{ "title": "Warframe",\
"audio" : {"timestamps" : ("10:35", "10:58.7") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1080p, low settings", \
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
{ "title": "Usefulness of the GT 1030",\
"audio" : {"timestamps" : ("10:58.7", "11:30.45"), "volume" : 0.999 },\
"video" : "office_pc_gt_1030.mkv"\
})

#configs["episodes"].append(\
#{ "title": "Usefulness of the R7 250",\
#"audio" : {"timestamps" : ("12:11.06", "12:53.27") },\
#"video" : {"file" : "", "start":""}\
#})

configs["episodes"].append(\
{ "title": "Inconsistent performance, maybe an issue with this sample",\
"audio" : {"timestamps" : ("11:30.45", "11:46") },\
"video" : "stock_bfv_tobruk_720pLow.mp4",\
"isChapter" : False,\
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

