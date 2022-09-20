import scriptedvided

configs = { "defaultAudioFile" : "R9_290X.ogg",\
"mediaFolder" : "C:\\Users\\Admin\\Videos\\R9_290X", \
"stockFolder" : "C:\\Users\\Admin\\Videos\stock",\
"benchmarkFile" : "C:\\Users\\Admin\\Videos\\R9_290X\\Benchmark_R9_290X.txt",\
"outputFolder" : "C:\\Users\\Admin\\Videos\\R9_290X\\output", \
"outputFile" : "R9_290X.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "H:\\Muzica\\royalty free\\Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3",\
"timestamps" : ("00:30", None ), "destinationTimestamp" : {"title" : "Context of the launch", "until" : "Apex Legends"}}, \
{"file" : "H:\\Muzica\\royalty free\\bensound-summer.mp3", "timestamps" : ("00:00", None ), "destinationTimestamp" : { "title": "Usefulness of used GPUs", "until" : "Blooper" }}, \
], "volume" : 0.03 },\
"episodes" : [],\
"youtube" : {"title" : "Reviewing the R9 290X in 2022", \
"description" : '''In this video, we'll take a closer look to Sapphire's R9 290X Battlefield 4 edition.

As usual, we'll use the E3-1241 v3 CPU (i7 4770 equivalent) and 32 GB DDR3 at 1600 MHz to pair it with.''',\
"links" : '''
More games tested with the R9 290X:
https://www.youtube.com/watch?v=hz7fv_qTZCw

TechPowerup entry:
https://www.techpowerup.com/gpu-specs/sapphire-r9-290x.b2458

Phillip's HD 7000 series video:
https://www.youtube.com/watch?v=wsuP_9afO9c

GDDR6 memory temperatures videos:
https://www.youtube.com/watch?v=ph4_Sr8YNXI
https://www.youtube.com/watch?v=f8f6ZHCPVpw

Sapphire Tri-X segment:
https://www.youtube.com/watch?v=Xy2NqJ3MeGY

''', \
"tags" : "AMD,ATI,Radeon,GCN,R9 290X",\
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
"audio" : {"timestamps" : ("00:00", "00:17" ), "volume" : 0.999 },\
"video" : {"file":"r7_r9_gcn_launch.mp4", "start" : "02:14"} \
})

configs["episodes"].append(\
{ "title": "Context of the launch - Phillip",\
"audio" : {"timestamps" : ("00:17", "00:30" ), "volume" : 0.999 },\
"isChapter" : False,\
"video" : "Phillip_HD7000.mkv"\
})


configs["episodes"].append(\
{ "title": "The GPU",\
"audio" : {"timestamps" : ("00:30", "01:07.3" ), "volume" : 0.999 },\
"video" : "sapphire_r9_290x_techpowerup.mkv",\
})

configs["episodes"].append(\
{ "title": "GDDR6 temps",\
"audio" : {"timestamps" : ("01:07.3", "01:20.3" ), "volume" : 0.999 },\
"video" : "gddr6-datasheet.mkv",\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Drivers and features",\
"audio" : {"timestamps" : ("01:20.3", "01:41.6" ), "volume" : 0.999 },\
"video" : "sapphire_r9_290x_techpowerup.mkv",\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Dual bios",\
"audio" : {"timestamps" : ("01:41.6", "02:01" ), "volume" : 0.999 },\
"video" : "r9_290x_dualbios.mkv",\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Cooling and thermals",\
"audio" : {"timestamps" : ( "02:01", "02:15.2" ), "volume" : 0.999 },\
"video" : {"file" : "Sapphire-tri-x.mkv", "start" : "00:22" },\
})

configs["episodes"].append(\
{ "title": "Cooling and thermals - blower fan",\
"audio" : {"timestamps" : ( "02:15.2", "02:37" ), "volume" : 0.999 },\
"video" : "R9_290X_cooling-converted.mp4",\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Cooling and thermals - massive cooler",\
"audio" : {"timestamps" : ( "02:37", "02:45.9" ), "volume" : 0.999 },\
"video" : {"file" : "R9_290X_coolerWeight-converted.mp4", "rotation" : 90}, \
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Cooling and thermals - idle, no curve",\
"audio" : {"timestamps" : ( "02:45.9", "02:54.3" ), "volume" : 0.999 },\
"video" : "R9_290X_noFanCurve_idle.mp4",\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Cooling and thermals - Heaven no curve",\
"audio" : {"timestamps" : ( "02:54.3", "03:09" ), "volume" : 0.999 },\
"video" : "R9_290X_Heaven_noFanCurve.mp4",\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Cooling and thermals - repair link",\
"audio" : {"timestamps" : ( "03:09", "03:23.8" ), "volume" : 0.999 },\
"video" : {"file":"R9_290X_blownCaps2-converted.mp4", "rotation" : 180},\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Cooling and thermals - fan curve",\
"audio" : {"timestamps" : ( "03:23.8", "03:30.5" ), "volume" : 0.75 },\
"video" : "custom_fan_curve.mp4",\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Cooling and thermals - temps fan curve",\
"audio" : {"timestamps" : ( "03:30.5", "03:44.5" ), "volume" : 0.999 },\
"video" : "R9_290X_HeavenOnly.mp4",\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "It has video encoding",\
"audio" : {"timestamps" : ( "03:44.5", "04:04.2" ), "volume" : 0.999 },\
"video" : {"file":"AMD VCE.mkv", "start":"00:06"},\
})


configs["episodes"].append(\
{ "title": "Apex Legends",\
"audio" : {"timestamps" : ("04:04.2", "04:42.6" )  },\
"overlay" : { \
    "text" : ["'Apex Legends'",\
              "'1080p, low settings - Average\: 128fps, 1\\\% lows\: 87fps'",\
              "'720p, low settings - Average\: 144fps, 1\\\% lows\: 107fps'"]\
}, \
})

configs["episodes"].append(\
{ "title": "CoD Warzone",\
"audio" : {"timestamps" : ("04:42.6", "05:13" )  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "720p, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Battlefield V",\
"audio" : {"timestamps" : ("05:13", "05:40.4" ) },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "720p, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Control",\
"audio" : {"timestamps" : ("05:40.4", "06:06") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "720p, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Rainbow Six: Siege",\
"audio" : {"timestamps" : ("06:06", "06:46") },\
"overlay" : { \
    "text" : ["'Rainbow Six\: Siege'",\
              "'1080p, low settings, 100\\\% render scale - Average\: 161fps, 1\\\% lows\: 118ps'",\
              "'720p, low settings, 100\\\% render scale - Average\: 202fps, 1\\\% lows\: 133fps'",\
              "'1080p, low settings, 50\\\% render scale - Average\: 198fps, 1\\\% lows\: 135fps'",\
              "'720p, low settings, 50\\\% render scale - Average\: 220fps, 1\\\% lows\: 141fps'"]\
}, \
})

configs["episodes"].append(\
{ "title": "Alien: Isolation",\
"audio" : {"timestamps" : ("06:46","07:19") },\
"video" : "stock_Alien_Isolation_1080p.mp4",\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1080p, ultra settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Counter Strike: Global Offensive",\
"audio" : {"timestamps" : ("07:19", "07:46.3") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1080p, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "DOTA2",\
"audio" : {"timestamps" : ("07:46.3", "08:14"), "volume" : 0.97 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1080p, low settings, 100% render scale", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Fortnite",\
"audio" : {"timestamps" : ("08:14", "08:45") },\
"video" : {"file":"R9_290X_Fortnite.mp4", "start":"01:30"},\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1080p, performance mode, view distance FAR, 100% render scale", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Rocket League",\
"audio" : {"timestamps" : ("08:45", "09:09.7") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1080p, low settings, 100% render scale", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Splitgate",\
"audio" : {"timestamps" : ("09:09.7", "09:39.7") },\
"overlay" : { \
    "text" : ["'Splitgate'",\
              "'1080p, low settings - Average\: 207fps, 1\\\% lows\: 127fps'",\
              "'720p, low settings - Average\: 220fps, 1\\\% lows\: 117fps'"]\
}, \
})

configs["episodes"].append(\
{ "title": "Valorant",\
"audio" : {"timestamps" : ("09:39.7", "10:26.2") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1080p, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Genshin Impact",\
"audio" : {"timestamps" : ("10:26.2", "10:47") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1080p, low settings, 1.0 render scale", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Paladins",\
"audio" : {"timestamps" : ("10:47", "11:11.7") , "volume" : 0.97 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1080p, high settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Realm Royale",\
"audio" : {"timestamps" : ("11:11.7", "11:44") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1080p, high settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Rogue Company",\
"audio" : {"timestamps" : ("11:44", "12:18") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1080p, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "World of Tanks Blitz",\
"audio" : {"timestamps" : ("12:18", "12:38") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1080p, high settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Warframe",\
"audio" : {"timestamps" : ("12:38", "13:01") },\
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
{ "title": "Usefulness of the R9 290X",\
"audio" : {"timestamps" : ("13:01", "13:36.4"), "volume" : 0.999 },\
"video" : "R9_290X_bb_B_FV.mp4", \
})

configs["episodes"].append(\
{ "title": "Good performance",\
"isChapter" : False,\
"audio" : {"timestamps" : ("13:36.4", "13:48.4"), "volume" : 0.999 },\
"video" : "R9_290X_card.mp4",\
})

configs["episodes"].append(\
{ "title": "iffy pricing",\
"isChapter" : False,\
"audio" : {"timestamps" : ( "13:48.4", "14:19"), "volume" : 0.999 },\
"video" : "R9_290X_bb_A_pex.mp4", \
})


configs["episodes"].append(\
{ "title": "Blooper",\
"isChapter" : False,\
"audio" : {"timestamps" : ( "15:51.1", "16:02.1"), "volume" : 0.999},\
"video" : "R9_290X_bb_G_enshinImpact.mp4",\
})


#scriptedvided.makeVideoForEpisode(configs["episodes"][27], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][9], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][8], configs)
#print(scriptedvided.makeVideoForEpisode(configs["episodes"][9], configs))
#print(scriptedvided.getSuitableVideoStream(configs["episodes"][9], configs))
#print (configs["youtube"])
#print(scriptedvided.getMusicCreditsString(configs["backgroundTrack"]))
#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "Usefulness of the HD 6850"][0], configs)
#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "Battlefield V"][0], configs)
scriptedvided.makeVideo(configs)

