import scriptedvided

configs = { "defaultAudioFile" : "R7 265.ogg",\
"mediaFolder" : "C:\\Users\\Admin\\Videos\\R7 265", \
"stockFolder" : "C:\\Users\\Admin\\Videos\stock",\
"benchmarkFile" : "C:\\Users\\Admin\\Videos\\R7 265\\Benchmark_r7_265.txt",\
"outputFolder" : "C:\\Users\\Admin\\Videos\\R7 265\\output", \
"outputFile" : "R7 265.mp4", \
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "H:\\Muzica\\royalty free\\Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3",\
"timestamps" : ("00:30", None ), "destinationTimestamp" : {"title" : "Context of the launch", "until" : "Apex Legends"}}, \
{"file" : "H:\\Muzica\\royalty free\\bensound-summer.mp3", "timestamps" : ("00:00", None ), "destinationTimestamp" : { "title": "Usefulness of used GPUs", "until" : "end of the video" }}, \
], "volume" : 0.03 },\
"episodes" : [],\
"youtube" : {"title" : "The AMD Radeon R7 265 in 2022", \
"description" : '''The Radeon R7 265, a rename of the HD 7850, was a higher end mid-range card released in February 2014. Like all GCN based cards, it had game ready drivers released for it up until 2021, and in this video, we'll see how it handles games in 2022.''',\
"links" : '''
More games tested with the R7 265 / HD 7850:
https://www.youtube.com/playlist?list=PLH6sLgdc_uJ7skjWpnm3zAzz0_vLY8De2

TechPowerup entries (both R7 265 and HD 7850):
https://www.techpowerup.com/gpu-specs/sapphire-dual-x-r7-265.b2749
https://www.techpowerup.com/gpu-specs/radeon-hd-7850.c1055

Intel 11th gen processors:
The core i5 11400 (has an IGPU): https://ark.intel.com/content/www/us/en/ark/products/212270/intel-core-i511400-processor-12m-cache-up-to-4-40-ghz.html
The core i5 11400F (no IGPU): https://ark.intel.com/content/www/us/en/ark/products/212271/intel-core-i511400f-processor-12m-cache-up-to-4-40-ghz.html

Other resources used:
Electronic Arts at AMD Radeon Graphics Tech Day: https://www.youtube.com/watch?v=pVFp1aamKyM
''', \
"tags" : "AMD,Radeon,R7 265,HD 7850, HD7850,GCN,GCN 1.0",\
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
"audio" : {"timestamps" : ("00:00", "00:45" ), "volume" : 0.999 },\
"video" : "hd_6800_EA.mp4"\
})

configs["episodes"].append(\
{ "title": "The GPU",\
"audio" : {"timestamps" : ("00:45", "01:28" ), "volume" : 0.999 },\
"video" : "6850_techpowerup.mp4",\
})

configs["episodes"].append(\
{ "title": "Power consumption and cooling",\
"audio" : {"timestamps" : ("01:28", "01:46" ), "volume" : 0.999 },\
"video" : "hd6850.mov",\
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
"audio" : {"timestamps" : ("03:18", "04:01" ), "volume" : 0.97  },\
"overlay" : { \
    "text" : ["'Apex Legends'",\
              "'1080p, low setings - Average\: 60fps, 1\\\% lows\: 33fps'",\
              "'720p, low setings - Average\: 81fps, 1\\\% lows\: 55fps'"]\
}, \
})

configs["episodes"].append(\
{ "title": "CoD Warzone",\
"audio" : {"timestamps" : ("04:01", "04:15" ) , "volume" : 0.97 },\
"video" : {"file":"TerraScale2_W_a_r_z_o_n_e.mp4", "start" : "00:30"}, \
"overlay" : { \
    "benchmark" : { \
        "settings" : "720p, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Battlefield V",\
"audio" : {"timestamps" : ("04:15", "04:48" ) , "volume" : 0.97 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "720p, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Control",\
"audio" : {"timestamps" : ("04:48", "05:16") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "720p, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Rainbow Six: Siege",\
"audio" : {"timestamps" : ("05:16", "05:44") },\
"overlay" : { \
    "text" : ["'Rainbow Six\: Siege'",\
              "'1080p, low setings, 100\\\% render scale - Average\: 77fps, 1\\\% lows\: 59ps'",\
              "'720p, low setings, 100\\\% render scale - Average\: 136fps, 1\\\% lows\: 90fps'",\
              "'1080p, low setings, 50\\\% render scale - Average\: 105fps, 1\\\% lows\: 77fps'",\
              "'720p, low setings, 50\\\% render scale - Average\: 163fps, 1\\\% lows\: 99fps'"]\
}, \
})

configs["episodes"].append(\
{ "title": "Alien: Isolation",\
"audio" : {"timestamps" : ("05:44","06:08") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1080p, ultra settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Counter Strike: Global Offensive",\
"audio" : {"timestamps" : ("06:08", "06:30") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1080p, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "DOTA2",\
"audio" : {"timestamps" : ("06:30", "06:51"), "volume" : 0.97 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1080p, low settings, 100% render scale", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Fortnite",\
"audio" : {"timestamps" : ("06:51", "07:11") },\
"video" : "R7 265 Fortnite C3S2 1080p.mp4",
"overlay" : { \
    "benchmark" : { \
        "settings" : "1080p, performance mode, view distance FAR, 100% render scale", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Rocket League",\
"audio" : {"timestamps" : ("07:11", "07:32") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1080p, low settings, 100% render scale", \
    }\
}, \
})


configs["episodes"].append(\
{ "title": "Splitgate",\
"audio" : {"timestamps" : ("07:32", "08:07") },\
"overlay" : { \
    "text" : ["'Splitgate'",\
              "'1080p, low setings - Average\: 73fps, 1\\\% lows\: 33fps'",\
              "'720p, low setings - Average\: 119fps, 1\\\% lows\: 42fps'"]\
}, \
})

configs["episodes"].append(\
{ "title": "Valorant",\
"audio" : {"timestamps" : ("08:07", "08:34") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1080p, low settings", \
    }\
}, \
})


configs["episodes"].append(\
{ "title": "Genshin Impact",\
"audio" : {"timestamps" : ("08:34", "08:55") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1080p, low settings, 1.0 render scale", \
    }\
}, \
})


configs["episodes"].append(\
{ "title": "Paladins",\
"audio" : {"timestamps" : ("08:55", "09:21") , "volume" : 0.97 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1080p, high settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Realm Royale",\
"audio" : {"timestamps" : ("09:21", "09:50") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1080p, high settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Rogue Company",\
"audio" : {"timestamps" : ("09:50", "10:17") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1080p, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "World of Tanks Blitz",\
"audio" : {"timestamps" : ("10:17", "10:37") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1080p, high settings", \
    }\
}, \
})


configs["episodes"].append(\
{ "title": "Warframe",\
"audio" : {"timestamps" : ("10:37", "10:56") },\
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
{ "title": "Usefulness of the R7 265",\
"audio" : {"timestamps" : ("10:56", "11:53") },\
"video" : "6850_fortnite_win.mp4"\
})

configs["episodes"].append(\
{ "title": "Personal notes for the R7 265",\
"audio" : {"timestamps" : ("11:53", "12:32"), "volume" : 0.999},\
"video" : "6850_fortnite_win_with_card.mp4"\
})

#scriptedvided.makeVideoForEpisode(configs["episodes"][27], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][9], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][8], configs)
#print(scriptedvided.makeVideoForEpisode(configs["episodes"][9], configs))
#print(scriptedvided.getSuitableVideoStream(configs["episodes"][9], configs))
#print (configs["youtube"])
#print(scriptedvided.getMusicCreditsString(configs["backgroundTrack"]))
#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "Usefulness of the HD 6850"][0], configs)
scriptedvided.makeVideo(configs)

