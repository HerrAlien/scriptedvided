import scriptedvided

configs = { "defaultAudioFile" : "FermiGT730_notch97.ogg",\
"mediaFolder" : "C:\\Users\\Admin\\Videos\\FermiGT730", \
"stockFolder" : "C:\\Users\\Admin\\Videos\stock",\
"benchmarkFile" : "C:\\Users\\Admin\\Videos\\FermiGT730\\Benchmark_FermiGT730.txt",\
"outputFolder" : "C:\\Users\\Admin\\Videos\\FermiGT730\\output", \
"outputFile" : "FermiGT730.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "H:\\Muzica\\royalty free\\Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3",\
"timestamps" : ("00:30", None ), "destinationTimestamp" : {"title" : "TLDW", "until" : "Cooling and thermals"}}, \
{"file" : "H:\\Muzica\\royalty free\\Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3",\
"timestamps" : ("00:30", None ), "destinationTimestamp" : {"title" : "Cooling and thermals", "until" : "Apex Legends"}}, \
{"file" : "H:\\Muzica\\royalty free\\bensound-summer.mp3", "timestamps" : ("00:00", None ), "destinationTimestamp" : { "title": "Fermi GT 730 - what is it good for", "until" : "Blooper" }}, \
], "volume" : 0.03 },\
"episodes" : [],\
"youtube" : {"title" : "Reviewing the R9 290X in 2022", \
"description" : '''Slapping a new label on an old card is apparently OK, judging by this Fermi GT 730.
But what can one do when using this card?

As usual, we'll use the E3-1241 v3 CPU (i7 4770 equivalent) and 32 GB DDR3 at 1600 MHz to pair it with.''',\
"links" : '''

NVidia Kepler architecture:
https://www.youtube.com/watch?v=TxtZwW2Lf-w

Gamers Nexus take on the DDR4 GT 1030:
https://www.youtube.com/watch?v=1CazEXejPCU

More games tested with the R9 290X:
https://www.youtube.com/watch?v=hz7fv_qTZCw

TechPowerup entries:
https://www.techpowerup.com/gpu-specs/geforce-gt-1030-ddr4.c3187
https://www.techpowerup.com/gpu-specs/geforce-gt-1030-gk107.c3454
https://www.techpowerup.com/gpu-specs/geforce-gt-1030.c2954

https://www.techpowerup.com/gpu-specs/asus-gt-710-silent-2-gb.b8230
https://www.techpowerup.com/gpu-specs/geforce-gt-710.c1990
https://www.techpowerup.com/gpu-specs/geforce-gt-710.c2614

https://www.techpowerup.com/gpu-specs/geforce-gt-430.c603
https://www.techpowerup.com/gpu-specs/geforce-gt-530-oem.c630
https://www.techpowerup.com/gpu-specs/geforce-gt-630.c816
https://www.techpowerup.com/gpu-specs/geforce-gt-730.c2590
''', \
"tags" : "NVidia,Asus,Fermi,Kepler,GeForce,GT 730,GT730,730",\
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
"audio" : {"timestamps" : ("00:00", "00:21.1" ), "volume" : 0.999 },\
"video" : {"file":"nvidia_kepler_launch.mp4", "start" : "00:00"} \
})

configs["episodes"].append(\
{ "title": "TLDW2",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:21.1", "00:39" ), "volume" : 0.999 },\
"video" : {"file":"FermiGT730_breel_card.mp4", "start" : "00:00"} \
})

configs["episodes"].append(\
{ "title": "(long) Rant - the same label, different cards",\
"audio" : {"timestamps" : ("00:39", "01:18.3" ), "volume" : 0.999 },\
"video" : "1030_family.mkv"\
})

configs["episodes"].append(\
{ "title": "710 family",\
"isChapter" : False,\
"audio" : {"timestamps" : ( "01:18.3", "01:57.5" ), "volume" : 0.999 },\
"video" : "710_family_2.mkv"\
})

configs["episodes"].append(\
{ "title": "730 family",\
"isChapter" : False,\
"audio" : {"timestamps" : ( "02:09" , "02:29" ), "volume" : 0.999 },\
"video" : "730_family_2.mkv"\
})

configs["episodes"].append(\
{ "title": "Same GPU, multiple names",\
"isChapter" : False,\
"audio" : {"timestamps" : ( "02:29" , "02:51"), "volume" : 0.999 },\
"video" : "430_530_630_730_same_time.mkv"\
})

configs["episodes"].append(\
{ "title": "Bait and switch",\
"isChapter" : False,\
"audio" : {"timestamps" : ( "02:51", "03:11"), "volume" : 0.999 },\
"video" : "nvidia_kepler_launch.mp4"\
})

configs["episodes"].append(\
{ "title": "History repeats itself",\
"isChapter" : False,\
"audio" : {"timestamps" : ("03:11", "03:49.5"), "volume" : 0.999 },\
"video" : "FermiGT730_breel_card.mp4"\
})

### add more chapters

configs["episodes"].append(\
{ "title": "The GPU",\
"audio" : {"timestamps" : ("03:49.5", "04:05.6" ), "volume" : 0.999 },\
"video" : {"file" : "430_530_630_730_one_by_one_long.mkv", "start" : "00:00"},\
})

configs["episodes"].append(\
{ "title": "The GPU 2",\
"isChapter" : False,\
"audio" : {"timestamps" : ("04:05.6", "04:48" ), "volume" : 0.999 },\
"video" : {"file" : "430_530_630_730_one_by_one_long.mkv", "start" : "01:00"},\
})

configs["episodes"].append(\
{ "title": "Bad driver support",\
"audio" : {"timestamps" : ("04:48" ,"05:05.25" ), "volume" : 0.999 },\
"video" : {"file" : "GF108_download_kepler_driver.mkv", "start" : "00:15"},\
})

configs["episodes"].append(\
{ "title": "Bad driver support - not installing",\
"isChapter" : False,\
"audio" : {"timestamps" : ("05:05.25" , "05:14" ), "volume" : 0.999 },\
"video" : {"file" : "GF108_install_kepler_driver.mkv", "start" : "00:40"},\
})

configs["episodes"].append(\
{ "title": "Bad driver support - use the 430",\
"isChapter" : False,\
"audio" : {"timestamps" : ("05:14" , "05:37.5" ), "volume" : 0.999 },\
"video" : {"file" : "GF108_download_fermi_driver.mkv", "start" : "00:10"},\
})

configs["episodes"].append(\
{ "title": "Cooling and thermals",\
"audio" : {"timestamps" : ( "05:37.5", "05:55.6" ), "volume" : 0.999 },\
"video" : {"file" : "FermiGT730_breel_card.mp4" },\
})

configs["episodes"].append(\
{ "title": "2 pin fan",\
"isChapter" : False,\
"audio" : {"timestamps" : ( "05:55.6" , "06:23.6" ), "volume" : 0.999 },\
"video" : {"file" : "FermiGT730_Heaven.mp4" },\
})

configs["episodes"].append(\
{ "title": "OC temps",\
"isChapter" : False,\
"audio" : {"timestamps" : ( "06:23.6" , "06:42.7"), "volume" : 0.999 },\
"video" : {"file" : "FermiGT730_OC_Warframe.mp4" , "start" : "00:14" },\
})


configs["episodes"].append(\
{ "title": "Apex Legends",\
"audio" : {"timestamps" : ("06:42.7", "07:10.4" )  },\
"overlay" : { \
    "text" : ["'Apex Legends (720p, low settings)'",\
              "'Average\: 16fps, 1\\\% lows\: 11fps'"]\
}, \
})

configs["episodes"].append(\
{ "title": "CoD Warzone",\
"audio" : {"timestamps" : ("07:10.4", "07:28.7" )  },\
"overlay" : { \
    "text" : ["'CoD Warzone (720p, low settings)'",\
              "'Average\: 0fps, 1\\\% lows\: 0fps'"]\
}, \
})

configs["episodes"].append(\
{ "title": "Battlefield V",\
"audio" : {"timestamps" : ("07:28.7", "07:54.7" ) },\
"overlay" : { \
    "text" : ["'Battlefield V (720p, low settings)'",\
              "'Average\: 0fps, 1\\\% lows\: 0fps'"]\
}, \
})

configs["episodes"].append(\
{ "title": "Control",\
"audio" : {"timestamps" : ("07:54.7", "08:14.6") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "720p, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Rainbow Six: Siege",\
"audio" : {"timestamps" : ("08:14.6", "08:39") },\
"overlay" : { \
    "text" : ["'Rainbow Six\: Siege (720p, low settings)'",\
              "'Average\: 0fps, 1\\\% lows\: 0fps'"]\
}, \
})

configs["episodes"].append(\
{ "title": "Alien: Isolation",\
"audio" : {"timestamps" : ("08:39","09:17") },\
"overlay" : { \
    "text" : ["'Alien\: Isolation (720p, ultra settings)'",\
              "'Stock 700MHz GPU, 800MHz RAM - Average\: 29fps, 1\\\% lows\: 21fps'",\
              "'OC 850MHz GPU, 950MHz RAM - Average\: 37fps, 1\\\% lows\: 26fps'",\
              ]\
}, \
})

configs["episodes"].append(\
{ "title": "Counter Strike: Global Offensive",\
"audio" : {"timestamps" : ("09:17", "09:53") },\
"overlay" : { \
    "text" : ["'Counter Strike\: Global Offensive (720p, low settings)'",\
              "'Stock 700MHz GPU, 800MHz RAM - Average\: 49fps, 1\\\% lows\: 19fps'",\
              "'OC 850MHz GPU, 950MHz RAM - Average\: 74fps, 1\\\% lows\: 27fps'",\
              ]\
}, \
})

configs["episodes"].append(\
{ "title": "DOTA2",\
"audio" : {"timestamps" : ("09:53", "10:15"), "volume" : 0.97 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "720p, low settings, 100% render scale", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Fortnite",\
"audio" : {"timestamps" : ("10:15", "10:57") },\
"overlay" : { \
    "text" : ["Fortnite (720p, performance mode, FAR draw distance)'",\
              "'Stock 700MHz GPU, 800MHz RAM - Average\: 55fps, 1\\\% lows\: 28fps'",\
              "'OC 850MHz GPU, 950MHz RAM - Average\: 69fps, 1\\\% lows\: 39fps'",\
              ]\
}, \
})

configs["episodes"].append(\
{ "title": "Rocket League",\
"audio" : {"timestamps" : ("10:57", "12:00") },\
"overlay" : { \
    "text" : ["'Rocket League'",\
              "'Stock 700MHz GPU, 800MHz RAM (1080p, low settings)\: Average\: 47fps, 1\\\% lows\: 17fps'",\
              "'Stock 700MHz GPU, 800MHz RAM (720p, low settings)\: Average\: 67fps, 1\\\% lows\: 23fps'",\
              "'OC 850MHz GPU, 950MHz RAM (720p, low settings)\: Average\: 90fps, 1\\\% lows\: 31fps'",\
              ]\
}, \
})

configs["episodes"].append(\
{ "title": "Splitgate",\
"audio" : {"timestamps" : ("12:00", "12:35") },\
"overlay" : { \
    "text" : ["'Splitgate (720p, low settings)'",\
              "'Stock 700MHz GPU, 800MHz RAM - Average\: 43fps, 1\\\% lows\: 17fps'",\
              "'OC 850MHz GPU, 950MHz RAM - Average\: 52fps, 1\\\% lows\: 20fps'"]
}, \
})

configs["episodes"].append(\
{ "title": "Valorant",\
"audio" : {"timestamps" : ("12:35", "13:13") },\
"overlay" : { \
    "text" : ["'Valorant'",\
              "'1080p, low settings\: Average\: 95fps, 1\\\% lows\: 63fps'",\
              "'720p, low settings\: Average\: 145fps, 1\\\% lows\: 101fps'",\
              ]\
}, \
})

configs["episodes"].append(\
{ "title": "Genshin Impact",\
"audio" : {"timestamps" : ("13:13", "13:48") },\
"overlay" : { \
    "text" : ["'Genshin Impact (720p, low settings)'",\
              "'Stock 700MHz GPU, 800MHz RAM - Average\: 27ps, 1\\\% lows\: 23fps'",\
              "'OC 850MHz GPU, 950MHz RAM - Average\: 29fps, 1\\\% lows\: 23fps'",\
              ]\
}, \
})

configs["episodes"].append(\
{ "title": "Paladins",\
"audio" : {"timestamps" : ("13:48", "14:10") , "volume" : 0.97 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "720p, high settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Realm Royale",\
"audio" : {"timestamps" : ("14:10", "14:42") },\
"overlay" : { \
    "text" : ["'Realm Royale (720p, low settings)'",\
              "'Stock 700MHz GPU, 800MHz RAM - Average\: 42s, 1\\\% lows\: 23fps'",\
              "'OC 850MHz GPU, 950MHz RAM - Average\: 61fps, 1\\\% lows\: 27fps'",\
              ]\
}, \
})

configs["episodes"].append(\
{ "title": "Rogue Company",\
"audio" : {"timestamps" : ("14:42", "15:24") },\
"overlay" : { \
    "text" : ["'Rogue Company (720p, low settings)'",\
              "'Stock 700MHz GPU, 800MHz RAM - Average\: 45s, 1\\\% lows\: 24fps'",\
              "'OC 850MHz GPU, 950MHz RAM - Average\: 54fps, 1\\\% lows\: 26fps'",\
              ]\
}, \
})

configs["episodes"].append(\
{ "title": "World of Tanks Blitz",\
"audio" : {"timestamps" : ("15:24", "15:44") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "720p, high settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Warframe",\
"audio" : {"timestamps" : ("15:44", "16:52") },\
"overlay" : { \
    "text" : ["'Warframe (720p, low settings)'",\
              "'Stock 700MHz GPU, 800MHz RAM - Average\: 39s, 1\\\% lows\: 10fps'",\
              "'OC 850MHz GPU, 950MHz RAM - Average\: 65fps, 1\\\% lows\: 45fps'",\
              ]\
}, \
})

## this can be copy-pasted, it uses a stock video with the audio already
## overlayed. Pass in a fake audio stream, at -60dB

configs["episodes"].append(\
{ "title": "Usefulness of the Fermi GT730",\
"audio" : {"timestamps" : ("16:52", "17:14.5"), "volume" : 0.999 },\
"video" : "FermiGT730_breel_card.mp4", \
})

###### moar on conclusion ####

configs["episodes"].append(\
{ "title": "Blooper",\
"isChapter" : False,\
"audio" : {"timestamps" : ( "18:23", "18:29"), "volume" : 0.999},\
"video" : "730_family_2.mp4",\
})


#scriptedvided.makeVideoForEpisode(configs["episodes"][27], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][9], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][8], configs)
#print(scriptedvided.makeVideoForEpisode(configs["episodes"][9], configs))
#print(scriptedvided.getSuitableVideoStream(configs["episodes"][9], configs))
#print (configs["youtube"])
#print(scriptedvided.getMusicCreditsString(configs["backgroundTrack"]))
#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "Usefulness of the HD 6850"][0], configs)
scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "Fortnite"][0], configs)
#scriptedvided.makeVideo(configs)

