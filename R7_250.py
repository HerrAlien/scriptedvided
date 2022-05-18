import scriptedvided

configs = { "defaultAudioFile" : "R7_250.ogg",\
"mediaFolder" : "C:\\Users\\Admin\\Videos\\R7_250", \
"stockFolder" : "C:\\Users\\Admin\\Videos\stock",\
"benchmarkFile" : "C:\\Users\\Admin\\Videos\\R7_250\\Benchmark_r7_250.txt",\
"outputFolder" : "C:\\Users\\Admin\\Videos\\R7_250\\output", \
"outputFile" : "R7_250.mp4", \
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "H:\\Muzica\\royalty free\\Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3",\
"timestamps" : ("00:30", None ), "destinationTimestamp" : {"title" : "Context of the launch", "until" : "Apex Legends"}}, \
{"file" : "H:\\Muzica\\royalty free\\bensound-summer.mp3", "timestamps" : ("00:00", None ), "destinationTimestamp" : { "title": "Usefulness of used GPUs", "until" : "end of the video" }}, \
], "volume" : 0.03 },\
"episodes" : [],\
"youtube" : {"title" : "The AMD Radeon R7 250 in 2022", \
"description" : '''The Radeon R7 250, a rename of the HD 7850, was a higher end mid-range card released in February 2014. Like all GCN based cards, it had game ready drivers released for it up until 2021, and in this video, we'll see how it handles games in 2022.''',\
"links" : '''
More games tested with the R7 250:
https://www.youtube.com/watch?v=35OfNvxkxe4

TechPowerup entries:
https://www.techpowerup.com/gpu-specs/asus-r7-250.b2488
https://www.techpowerup.com/gpu-specs/radeon-r7-250.c2459

Intel 11th gen processors:
The core i5 11400 (has an IGPU): https://ark.intel.com/content/www/us/en/ark/products/212270/intel-core-i511400-processor-12m-cache-up-to-4-40-ghz.html
The core i5 11400F (no IGPU): https://ark.intel.com/content/www/us/en/ark/products/212271/intel-core-i511400f-processor-12m-cache-up-to-4-40-ghz.html

Phillip's HD 7000 series video:
https://www.youtube.com/watch?v=wsuP_9afO9c

Other resources used:
https://www.youtube.com/watch?v=45YGDChR4Zc

''', \
"tags" : "AMD,Radeon,R7 250,HD 7850, HD7850,GCN,GCN 1.0",\
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
"audio" : {"timestamps" : ("00:00", "00:26.7" ), "volume" : 0.999 },\
"video" : "R7 R9 series.mp4"\
})

configs["episodes"].append(\
{ "title": "r7 250 - Cape Verde versus Oland XT",\
"audio" : {"timestamps" : ("00:26.7", "01:27.74" ), "volume" : 0.999 },\
"isChapter" : False,\
"video" : "which R7 250.mp4"\
})


configs["episodes"].append(\
{ "title": "The GPU",\
"audio" : {"timestamps" : ("01:27.74", "01:49.71" ), "volume" : 0.999 },\
"video" : "R7_250_gpu_capabilities.mkv",\
})

configs["episodes"].append(\
{ "title": "The GPU - restrictions on Oland",\
"audio" : {"timestamps" : ( "01:49.71", "02:18.55" ), "volume" : 0.999 },\
"isChapter" : False,\
"video" : "R7_250_pciex8.mkv",\
})

configs["episodes"].append(\
{ "title": "Meme on 6500xt",\
"audio" : {"timestamps" : ( "02:18.55", "02:29.23" ), "volume" : 0.999 },\
"isChapter" : False,\
"video" : "poor_pcie_no_encoding.mkv",\
})


configs["episodes"].append(\
{ "title": "The GPU configuration",\
"audio" : {"timestamps" : ("02:29.23", "03:09.36" ), "volume" : 0.999 },\
"video" : "Asus_r7_250_techpowerup.mkv",
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Cooling and thermals",\
"audio" : {"timestamps" : ( "03:09.36", "03:36.73" ), "volume" : 0.999 },\
"video" : "r7_250.MOV",\
})

configs["episodes"].append(\
{ "title": "Cooling and thermals - thermals only",\
"audio" : {"timestamps" : ( "03:36.73", "04:23.19" ), "volume" : 0.999 },\
"video" : "r7_250_Heaven.mkv",\
"isChapter" : False,\
})


## this can be copy-pasted, it uses a stock video with the audio already
## overlayed. Pass in a fake audio stream, at -60dB
configs["episodes"].append(\
{ "title": "Video capturing will impact performance",\
"audio" : {"timestamps" : ( "04:23.19", "04:45.11" ), "volume" : 0.999 },\
"video" : "r7_250_choppy_recording.mkv",\
"isChapter" : "true",\
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
"audio" : {"timestamps" : ("04:45.11", "05:23.94" ), "volume" : 0.97  },\
"overlay" : { \
    "text" : ["'Apex Legends'",\
              "'1080p, low setings - Average\: 44fps, 1\\\% lows\: 33fps'",\
              "'720p, low setings - Average\: 62fps, 1\\\% lows\: 47fps'"]\
}, \
})

configs["episodes"].append(\
{ "title": "CoD Warzone",\
"audio" : {"timestamps" : ("05:23.94", "05:52.44" ) , "volume" : 0.97 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "720p, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Battlefield V",\
"audio" : {"timestamps" : ("05:52.44", "06:08.81" ) , "volume" : 0.97 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "720p, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Control",\
"audio" : {"timestamps" : ("06:08.81", "06:35.73") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "720p, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Rainbow Six: Siege",\
"audio" : {"timestamps" : ("06:35.73", "07:00.36") },\
"overlay" : { \
    "text" : ["'Rainbow Six\: Siege'",\
              "'1080p, low setings, 100\\\% render scale - Average\: 36fps, 1\\\% lows\: 28ps'",\
              "'720p, low setings, 100\\\% render scale - Average\: 70fps, 1\\\% lows\: 47fps'",\
              "'1080p, low setings, 50\\\% render scale - Average\: 51fps, 1\\\% lows\: 39fps'",\
              "'720p, low setings, 50\\\% render scale - Average\: 91fps, 1\\\% lows\: 57fps'"]\
}, \
})

configs["episodes"].append(\
{ "title": "Alien: Isolation",\
"audio" : {"timestamps" : ("07:00.36","07:31.4") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1080p, ultra settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Counter Strike: Global Offensive",\
"audio" : {"timestamps" : ("07:31.4", "07:55.36") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1080p, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "DOTA2",\
"audio" : {"timestamps" : ("07:55.36", "08:14.15"), "volume" : 0.97 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1080p, low settings, 100% render scale", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Fortnite",\
"audio" : {"timestamps" : ("08:14.15", "08:42.44") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1080p, performance mode, view distance FAR, 100% render scale", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Rocket League",\
"audio" : {"timestamps" : ("08:42.44", "09:04.73") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1080p, low settings, 100% render scale", \
    }\
}, \
})


configs["episodes"].append(\
{ "title": "Splitgate",\
"audio" : {"timestamps" : ("09:04.73", "09:29.81") },\
"overlay" : { \
    "text" : ["'Splitgate'",\
              "'1080p, low setings - Average\: 38fps, 1\\\% lows\: 17fps'",\
              "'720p, low setings - Average\: 74fps, 1\\\% lows\: 54fps'"]\
}, \
})

configs["episodes"].append(\
{ "title": "Valorant",\
"audio" : {"timestamps" : ("09:29.81", "09:50.11") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1080p, low settings", \
    }\
}, \
})


configs["episodes"].append(\
{ "title": "Genshin Impact",\
"audio" : {"timestamps" : ("09:50.11", "10:07.94") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1080p, low settings, 1.0 render scale", \
    }\
}, \
})


configs["episodes"].append(\
{ "title": "Paladins",\
"audio" : {"timestamps" : ("10:07.94", "10:32.56") , "volume" : 0.97 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1080p, high settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Realm Royale",\
"audio" : {"timestamps" : ("10:32.56", "11:03.48") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1080p, high settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Rogue Company",\
"audio" : {"timestamps" : ("11:03.48", "11:29.52") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1080p, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "World of Tanks Blitz",\
"audio" : {"timestamps" : ("11:29.52", "11:47.52") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1080p, high settings", \
    }\
}, \
})


configs["episodes"].append(\
{ "title": "Warframe",\
"audio" : {"timestamps" : ("11:47.52", "12:11.06") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1080p, high settings", \
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
{ "title": "Usefulness of the R7 250",\
"audio" : {"timestamps" : ("12:11.06", "12:53.27") },\
"video" : "r7_250_breel_game.MOV"\
})

#configs["episodes"].append(\
#{ "title": "Usefulness of the R7 250",\
#"audio" : {"timestamps" : ("12:11.06", "12:53.27") },\
#"video" : {"file" : "", "start":""}\
#})

configs["episodes"].append(\
{ "title": "2kliksPhillip GCN analysis",\
"audio" : {"timestamps" : ("12:53.27", "13:20.81") },\
"video" : "Phillip_HD7000.mkv",\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Personal notes for the R7 250",\
"audio" : {"timestamps" : ("13:20.81", "14:07"), "volume" : 0.999},\
"video" : "stock_Alien_Isolation_1080p.mp4"\
})

#scriptedvided.makeVideoForEpisode(configs["episodes"][27], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][9], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][8], configs)
#print(scriptedvided.makeVideoForEpisode(configs["episodes"][9], configs))
#print(scriptedvided.getSuitableVideoStream(configs["episodes"][9], configs))
#print (configs["youtube"])
#print(scriptedvided.getMusicCreditsString(configs["backgroundTrack"]))
#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "Usefulness of the HD 6850"][0], configs)
#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "Context of the launch"][0], configs)
scriptedvided.makeVideo(configs)

