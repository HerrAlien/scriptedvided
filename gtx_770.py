import scriptedvided

configs = { "defaultAudioFile" : "gtx770.ogg",\
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

Phillip's HD 7000 series video:
https://www.youtube.com/watch?v=wsuP_9afO9c
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
"audio" : {"timestamps" : ("00:00", "00:27" ), "volume" : 0.999 },\
"video" : {"file" : "gtx770_bb_O_verwatch2.mp4", "start" : "00:40" }\
})

configs["episodes"].append(\
{ "title": "Context of the launch",\
"audio" : {"timestamps" : ("00:27", "00:53" ), "volume" : 0.999 },\
"video" : "nvidia_kepler_launch.mp4",\
})

configs["episodes"].append(\
{ "title": "The GPU",\
"audio" : {"timestamps" : ("00:53", "01:48" ), "volume" : 0.999 },\
"video" : "gtx770_gpuz.mp4",\
})

configs["episodes"].append(\
{ "title": "The GPU - nvenc",\
"audio" : {"timestamps" : ( "02:56", "03:14" ), "volume" : 0.999 },\
"video" : "nvenc.mkv",\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Cooling and thermals",\
"audio" : {"timestamps" : ( "01:48", "02:19" ), "volume" : 0.999 },\
"video" : {"file" : "gtx770_cooling.mp4", "start" : "01:40"},\
})

configs["episodes"].append(\
{ "title": "Cooling and thermals - thermals only - Heaven",\
"audio" : {"timestamps" : ( "02:19", "02:41" ), "volume" : 0.999 },\
"video" : "gtx_770_finishedHeaven.mp4",\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Cooling and thermals - thermals only - Warframe",\
"audio" : {"timestamps" : ( "02:41", "02:56" ), "volume" : 0.999 },\
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
"audio" : {"timestamps" : ("03:14", "03:44" ), "volume" : 0.97  },\
"overlay" : { \
    "text" : ["'Apex Legends'",\
              scriptedvided.r6sText('1920x1080, low settings',85, 57),\
              scriptedvided.r6sText('1280x720, low settings',125, 87),\
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
              scriptedvided.r6sText('1920x1080, low settings, 100% render scale', 121, 88), \
              scriptedvided.r6sText('1280x720, low settings, 100% render scale', 185, 124),\
              scriptedvided.r6sText('1920x1080, low settings, 50% render scale', 145, 94),\
              scriptedvided.r6sText('1280x720, low settings, 50% render scale', 198, 137)]\
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
              scriptedvided.r6sText('1920x1080, low settings',180, 71),\
              scriptedvided.r6sText('1280x720, low settings',229, 100),\
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
    "benchmark" : { \
        "settings" : "1920x1080, low settings, 100% render scale", \
    }\
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


configs["episodes"].append(\
{ "title": "Usefulness of used GPUs",\
"audio" : {"timestamps" : ("00:00", "01:17"), "volume" : 0.001 },\
"video" : "Usefulness of used GPUs.mp4"\
})


configs["episodes"].append(\
{ "title": "Usefulness of the GTX 770",\
"audio" : {"timestamps" : ("11:45", "11:59.5"), "volume" : 0.999 },\
"video" : "nvidia_kepler_launch.mp4"\
})


configs["episodes"].append(\
{ "title": "Usefulness of the GTX 770 - card itself",\
"audio" : {"timestamps" : ("11:59.5", "12:09"), "volume" : 0.999 },\
"isChapter" : False,\
"video" : {"file" : "gtx770_bb_G_enshinImpact.mp4", "start" : "00:22"}\
})

configs["episodes"].append(\
{ "title": "GTX 770 or R9 280",\
"isChapter" : False,\
"audio" : {"timestamps" : ("12:09", "12:22"), "volume" : 0.999},\
"video" : {"file": "gtx770_r9_280_bb_F_ortnite.mp4", "start" : "00:27" }\
})


configs["episodes"].append(\
{ "title": "HerculeZ repair",\
"isChapter" : False,\
"audio" : {"timestamps" : ( "12:22", "12:38" ), "volume" : 0.999},\
"video" : "gtx770_unbalancedLoads.mp4"\
})


configs["episodes"].append(\
{ "title": "GTX 770 personal notes",\
"isChapter" : False,\
"audio" : {"timestamps" : ("12:38", "13:00"), "volume" : 0.999},\
"video" : {"file" : "gtx770_bb_F_ortnite.mp4", "start" : "01:06"}\
})


configs["episodes"].append(\
{ "title": "Blooper",\
"audio" : {"timestamps" : ("13:00", "13:04.7"), "volume" : 0.999},\
"video" : "gtx770_artefacts_windows.mp4",
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

