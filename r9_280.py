import scriptedvided

configs = { "defaultAudioFile" : "r9_280.ogg",\
"mediaFolder" : "C:\\Users\\Admin\\Videos\\r9_280", \
"stockFolder" : "C:\\Users\\Admin\\Videos\stock",\
"benchmarkFile" : "C:\\Users\\Admin\\Videos\\r9_280\\Benchmark_R9_280.txt",\
"outputFolder" : "C:\\Users\\Admin\\Videos\\r9_280\\output", \
"outputFile" : "r9_280.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "H:\\Muzica\\royalty free\\Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3",\
"timestamps" : ("00:30", None ), "destinationTimestamp" : {"title" : "Context of the launch", "until" : "Video capturing leads to CPU bottleneck"}}, \
{"file" : "H:\\Muzica\\royalty free\\bensound-summer.mp3", "timestamps" : ("00:00", None ), "destinationTimestamp" : { "title": "Usefulness of the GTX 960", "until" : "end-of-video" }}, \
], "volume" : 0.03 },\
"episodes" : [],\
"youtube" : {"title" : "Reviewing the R9 280 in 2022", \
"description" : '''In this video, we'll take a closer look to Sapphire's R9 280 Dual-X OC with boost.''',\
"links" : '''
More games tested with the R9 280:
https://www.youtube.com/playlist?list=PLH6sLgdc_uJ6cLPtH9eylU5IXbHJ3QpQc

TechPowerup entry:
https://www.techpowerup.com/gpu-specs/sapphire-dual-x-r9-280-oc-with-boost.b2845
''', \
"tags" : "AMD,ATI,Radeon,GCN,R9 280,HD7950,HD 7950",\
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
"audio" : {"timestamps" : ("00:00", "00:12" ), "volume" : 0.999 },\
"video" : "r7_r9_gcn_launch.mp4"\
})

configs["episodes"].append(\
{ "title": "Context of the launch - renames",\
"audio" : {"timestamps" : ("00:12", "00:39.33" ), "volume" : 0.999 },\
"isChapter" : False,\
"video" : "HD700_R7_R9_renames.mkv"\
})

configs["episodes"].append(\
{ "title": "Context of the launch - phillip",\
"audio" : {"timestamps" : ("00:46", "00:59" ), "volume" : 0.999 },\
"isChapter" : False,\
"video" : "Phillip_HD7000.mkv"\
})


configs["episodes"].append(\
{ "title": "The GPU",\
"audio" : {"timestamps" : ("00:59", "01:50" ), "volume" : 0.999 },\
"video" : "R9_280_GPU.mkv",\
})

configs["episodes"].append(\
{ "title": "Video encoding rant",\
"audio" : "",\
"video" : "",\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "API",\
"audio" : {"timestamps" : ( "01:50", "02:08" ), "volume" : 0.999 },\
"isChapter" : False,\
"video" : "",\
})

configs["episodes"].append(\
{ "title": "Dual BIOS",\
"audio" : {"timestamps" : ( "02:08", "02:27" ), "volume" : 0.999 },\
"isChapter" : False,\
"video" : "",\
})


configs["episodes"].append(\
{ "title": "Cooling and thermals",\
"audio" : {"timestamps" : ( "02:27", "03:06" ), "volume" : 0.999 },\
"video" : {"file" : "", "rotation" : 0},\
})

configs["episodes"].append(\
{ "title": "Cooling and thermals - thermals only",\
"audio" : {"timestamps" : ( "03:06", "03:39" ), "volume" : 0.999 },\
"video" : "r9_280_thermals.mp4",\
"isChapter" : False,\
})


## this can be copy-pasted, it uses a stock video with the audio already
## overlayed. Pass in a fake audio stream, at -60dB
configs["episodes"].append(\
{ "title": "Video capturing leads to CPU bottleneck",\
"audio" : {"timestamps" : ( "03:39", "04:18" ), "volume" : 0.001 },\
"video" : "r9_280_F_o_rtnite.mp4",\
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
"audio" : {"timestamps" : ("04:18", "04:45" ), "volume" : 0.97  },\
"overlay" : { \
    "text" : ["'Apex Legends'",\
              "'1080p, low setings - Average\: 85fps, 1\\\% lows\: 65fps'",\
              "'720p, low setings - Average\: 128fps, 1\\\% lows\: 91fps'"]\
}, \
})

configs["episodes"].append(\
{ "title": "CoD Warzone",\
"audio" : {"timestamps" : ("04:45", "05:05" ) , "volume" : 0.97 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "720p, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Battlefield V",\
"audio" : {"timestamps" : ("05:05", "05:32" ) , "volume" : 0.97 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "720p, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Control",\
"audio" : {"timestamps" : ("05:32", "05:58") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "720p, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Rainbow Six: Siege",\
"audio" : {"timestamps" : ("05:58", "06:33") },\
"overlay" : { \
    "text" : ["'Rainbow Six\: Siege'",\
              "'1080p, low setings, 100\\\% render scale - Average\: 114fps, 1\\\% lows\: 82ps'",\
              "'720p, low setings, 100\\\% render scale - Average\: 189fps, 1\\\% lows\: 114fps'",\
              "'1080p, low setings, 50\\\% render scale - Average\: 152fps, 1\\\% lows\: 100fps'",\
              "'720p, low setings, 50\\\% render scale - Average\: 205fps, 1\\\% lows\: 124fps'"]\
}, \
})

configs["episodes"].append(\
{ "title": "Alien: Isolation",\
"audio" : {"timestamps" : ("06:33","07:01") },\
"video" : "stock_Alien_Isolation_1080p.mp4",\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1080p, ultra settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Counter Strike: Global Offensive",\
"audio" : {"timestamps" : ("07:01", "07:21.5") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1080p, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "DOTA2",\
"audio" : {"timestamps" : ("07:21.5", "07:42"), "volume" : 0.97 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1080p, low settings, 100% render scale", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Fortnite",\
"audio" : {"timestamps" : ("07:42", "08:04") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1080p, performance mode, view distance FAR, 100% render scale", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Rocket League",\
"audio" : {"timestamps" : ("08:04", "08:24.5") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1080p, low settings, 100% render scale", \
    }\
}, \
})


configs["episodes"].append(\
{ "title": "Splitgate",\
"audio" : {"timestamps" : ("08:24.5", "08:55") },\
"overlay" : { \
    "text" : ["'Splitgate'",\
              "'1080p, low setings - Average\: 64fps, 1\\\% lows\: 31fps'",\
              "'720p, low setings - Average\: 107fps, 1\\\% lows\: 52fps'"]\
}, \
})

configs["episodes"].append(\
{ "title": "Valorant",\
"audio" : {"timestamps" : ("08:55", "09:22") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1080p, low settings", \
    }\
}, \
})


configs["episodes"].append(\
{ "title": "Genshin Impact",\
"audio" : {"timestamps" : ("09:22", "09:40") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1080p, low settings, 1.0 render scale", \
    }\
}, \
})


configs["episodes"].append(\
{ "title": "Paladins",\
"audio" : {"timestamps" : ("09:40", "10:01") , "volume" : 0.97 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1080p, high settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Realm Royale",\
"audio" : {"timestamps" : ("10:01", "10:20") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1080p, high settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Rogue Company",\
"audio" : {"timestamps" : ("10:20", "10:43.2") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1080p, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "World of Tanks Blitz",\
"audio" : {"timestamps" : ("10:43.2", "11:01.5") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1080p, high settings", \
    }\
}, \
})


configs["episodes"].append(\
{ "title": "Warframe",\
"audio" : {"timestamps" : ("11:01.5", "11:29") },\
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
{ "title": "Usefulness of the R9 280",\
"audio" : {"timestamps" : ("11:29", "11:57"), "volume" : 0.999 },\
"video" : ""\
})


configs["episodes"].append(\
{ "title": "Personal notes for the Sapphire R9 280 Dual-X OC with boost",\
"audio" : {"timestamps" : ("11:57", "12:24.5"), "volume" : 0.999},\
"video" : "stock_GenshinImpact_1080pLow.mp4"\
})

configs["episodes"].append(\
{ "title": "Hint to repair video",\
"isChapter" : False,\
"audio" : {"timestamps" : ( "12:24.5", "12:49"), "volume" : 0.999},\
"video" : "stock_GenshinImpact_1080pLow.mp4"\
})

configs["episodes"].append(\
{ "title": "Blooper",\
"isChapter" : False,\
"audio" : {"timestamps" : ( "12:49", "12:55"), "volume" : 0.999},\
"video" : "stock_GenshinImpact_1080pLow.mp4"\
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

