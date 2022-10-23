import scriptedvided

configs = { "defaultAudioFile" : "gtx_770.ogg",\
"mediaFolder" : "C:\\Users\\Admin\\Videos\\gtx770", \
"stockFolder" : "C:\\Users\\Admin\\Videos\stock",\
"benchmarkFile" : "C:\\Users\\Admin\\Videos\\gtx770\\Benchmark_gtx770.txt",\
"outputFolder" : "C:\\Users\\Admin\\Videos\\gtx770\\output", \
"outputFile" : "gtx_770.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#00800080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "H:\\Muzica\\royalty free\\Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3",\
"timestamps" : ("00:30", None ), "destinationTimestamp" : {"title" : "TLDW", "until" : "Apex Legends"}}, \
{"file" : "H:\\Muzica\\royalty free\\bensound-summer.mp3", "timestamps" : ("00:00", None ), "destinationTimestamp" : { "title": "Usefulness of used GPUs", "until" : "Blooper" }}, \
], "volume" : 0.03 },\
"episodes" : [],\
"youtube" : {"title" : "Review of a limping GTX 770", \
"description" : '''This GTX 770 was sold as defective; I was able to get it to work, and now we can see how it behaves in 2022.''',\
"links" : '''
More games tested with the GTX 770:
https://www.youtube.com/watch?v=VOPkXSfxHJ8
https://www.youtube.com/watch?v=q_7iS0QkfJQ
https://www.youtube.com/watch?v=fPO6AM2BLGs

TechPowerup entry:
https://www.techpowerup.com/gpu-specs/inno3d-gtx-770-herculez-2000.b2029
''', \
"tags" : "NVidia,GeForce,Kepler,GTX770,GTX 770",\
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
{ "title": "TLDW",\
"audio" : {"timestamps" : ("00:00", "00:16" ), "volume" : 0.999 },\
"video" : {"file" : "gtx770_bb_O_verwatch2.mp4", "start" : "00:40" }\
})

configs["episodes"].append(\
{ "title": "Context of the launch",\
"audio" : {"timestamps" : ("00:16", "00:36" ), "volume" : 0.999 },\
"video" : "nvidia_kepler_launch.mp4",\
})

configs["episodes"].append(\
{ "title": "The GPU",\
"audio" : {"timestamps" : ("00:16", "00:36" ), "volume" : 0.999 },\
"video" : "gtx770_gpuz.mp4",\
})

configs["episodes"].append(\
{ "title": "Cooling and thermals",\
"audio" : {"timestamps" : ( "00:36", "00:47" ), "volume" : 0.999 },\
"video" : {"file" : "gtx770_cooling.mp4"},\
})

configs["episodes"].append(\
{ "title": "Cooling and thermals - thermals only - Heaven",\
"audio" : {"timestamps" : ( "00:47", "01:08" ), "volume" : 0.999 },\
"video" : "gtx_770_finishedHeaven.mp4",\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Cooling and thermals - thermals only - Warframe",\
"audio" : {"timestamps" : ( "00:47", "01:08" ), "volume" : 0.999 },\
"video" : {"file" : "gtc770_Warframe_temps.mp4" , "start" : "04:10"},\
"isChapter" : False,\
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
              scriptedvided.r6sText('1920x1080, low settings',85, 57),\
              scriptedvided.r6sText('1280x720, low settings',125, 87),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "CoD Warzone",\
"audio" : {"timestamps" : ("03:21.3", "03:49" ) , "volume" : 0.97 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Battlefield V",\
"audio" : {"timestamps" : ("03:49", "04:20.6" ) , "volume" : 0.97 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Control",\
"audio" : {"timestamps" : ("04:20.6", "04:44.13") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Rainbow Six: Siege",\
"audio" : {"timestamps" : ("02:23", "02:44"), "padAudio" : 5},\
"overlay" : { \
    "text" : ["'Rainbow Six\: Siege'",\
              scriptedvided.r6sText('1920x1080, low settings, 100% render scale', 121, 88), \
              scriptedvided.r6sText('1280x720, low settings, 100% render scale', 185, 124),\
              scriptedvided.r6sText('1920x1080, low settings, 50% render scale', 145, 94),\
              scriptedvided.r6sText('1280x720, low settings, 50% render scale', 198, 137)]\
}, \
})

configs["episodes"].append(\
{ "title": "Alien: Isolation",\
"audio" : {"timestamps" : ("05:18.5","05:36.1") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, ultra settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Counter Strike: Global Offensive",\
"audio" : {"timestamps" : ("05:36.1", "06:28.3") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "DOTA2",\
"audio" : {"timestamps" : ("06:28.3", "06:50.4"), "volume" : 0.97 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings, 100% render scale", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Fortnite",\
"audio" : {"timestamps" : ("06:50.4", "07:29.5") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, performance mode, view distance FAR, 100% render scale", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Rocket League",\
"audio" : {"timestamps" : ("07:29.5", "07:53.4") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings, 100% render scale", \
    }\
}, \
})


configs["episodes"].append(\
{ "title": "Splitgate",\
"audio" : {"timestamps" : ("07:53.4", "08:16") },\
"overlay" : { \
    "text" : ["'Splitgate'",\
              scriptedvided.r6sText('1920x1080, low settings',180, 71),\
              scriptedvided.r6sText('1280x720, low settings',229, 100),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "Valorant",\
"audio" : {"timestamps" : ("08:16", "08:53") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})


configs["episodes"].append(\
{ "title": "Genshin Impact",\
"audio" : {"timestamps" : ("08:53", "09:16") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings, 1.0 render scale", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Overwatch 2",\
"audio" : {"timestamps" : ("08:53", "09:16") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings, 100% render scale", \
    }\
}, \
})



configs["episodes"].append(\
{ "title": "Paladins",\
"audio" : {"timestamps" : ("09:16", "09:35.5") , "volume" : 0.97 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, high settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Realm Royale",\
"audio" : {"timestamps" : ("09:35.5", "09:55") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, high settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Rogue Company",\
"audio" : {"timestamps" : ("09:55", "10:19.4") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "World of Tanks Blitz",\
"audio" : {"timestamps" : ("10:19.4", "10:35") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, high settings", \
    }\
}, \
})


configs["episodes"].append(\
{ "title": "Warframe",\
"audio" : {"timestamps" : ("10:35", "10:58.7") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})


configs["episodes"].append(\
{ "title": "Usefulness of used GPUs",\
"audio" : {"timestamps" : ("00:00", "01:17"), "volume" : 0.001 },\
"video" : "Usefulness of used GPUs.mp4"\
})

configs["episodes"].append(\
{ "title": "Usefulness of the GTX 770",\
"isChapter" : False,\
"audio" : {"timestamps" : ("10:58.7", "11:30.45"), "volume" : 0.999 },\
"video" : "gtx770_bb_F_ortnite.mp4"\
})

configs["episodes"].append(\
{ "title": "GTX 770 or R9 280",\
"isChapter" : False,\
"audio" : {"timestamps" : ("12:08.2", "12:30"), "volume" : 0.999},\
"video" : "gtx770_r9_280_bb_F_ortnite.mp4"\
})

configs["episodes"].append(\
{ "title": "GTX 770 personal notes",\
"isChapter" : False,\
"audio" : {"timestamps" : ("12:08.2", "12:30"), "volume" : 0.999},\
"video" : "gtx770_bb_F_ortnite.mp4"\
})

configs["episodes"].append(\
{ "title": "Blooper",\
"audio" : {"timestamps" : ("00:00", "00:15"), "volume" : 0.001},\
"video" : "gtx770_artefacts_windows.mp4",
"isChapter" : False,\
})



#configs["episodes"].append(\
#{ "title": "Usefulness of the R7 250",\
#"audio" : {"timestamps" : ("12:11.06", "12:53.27") },\
#"video" : {"file" : "", "start":""}\
#})


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

