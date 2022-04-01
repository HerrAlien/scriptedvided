import scriptedvided

configs = { "defaultAudioFile" : "hd7770.ogg",\
"mediaFolder" : "C:\\Users\\Admin\\Videos\\hd7770", \
"stockFolder" : "C:\\Users\\Admin\\Videos\stock",\
"outputFolder" : "C:\\Users\\Admin\\Videos\\hd7770\\output", \
"outputFile" : "hd7770.mp4", \
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "H:\\Muzica\\royalty free\\Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3",\
"timestamps" : ("00:30", "03:09" ), "destinationTimestamp" : "00:00"}, \
{"file" : "H:\\Muzica\\royalty free\\bensound-summer.mp3", "timestamps" : ("00:00", "02:40" ), "destinationTimestamp" : { "title": "Usefulness of used GPUs"}}, \
], "volume" : 0.05 },\
"episodes" : [],\
"youtube" : {"title" : "The AMD Radeon HD 7770 in 2022", \
"description" : '''The Radeon HD 7770 was the first mid-range offering from AMD on their (back then) new GCN architecture. Because GCN was also used in the XBox One console, it enjoyed support for quite a while. In this video, we'll see how that translates to the 7770, when putting it through its paces.''',\
"links" : '''
More games tested with the HD 7770:
https://www.youtube.com/watch?v=D28UKXSlyZw
https://www.youtube.com/watch?v=_QQrmprYyI8

TechPowerup entries:
https://www.techpowerup.com/gpu-specs/radeon-hd-7770-ghz-edition.c308
https://www.techpowerup.com/gpu-specs/asus-hd-7770.b609

Intel 11th gen processors:
The core i5 11400 (has an IGPU): https://ark.intel.com/content/www/us/en/ark/products/212270/intel-core-i511400-processor-12m-cache-up-to-4-40-ghz.html
The core i5 11400F (no IGPU): https://ark.intel.com/content/www/us/en/ark/products/212271/intel-core-i511400f-processor-12m-cache-up-to-4-40-ghz.html

Other resources used:
RX 6500xt review: https://www.youtube.com/watch?v=M5_oM3Ow_CI
AMD Video Compression Engine presentation: https://www.youtube.com/watch?v=piUZJjdxqHA
AMD GCN architecture: https://www.youtube.com/watch?v=lLCCGS5vUx4
''', \
"tags" : "AMD,Radeon,HD 7770,HD7770,GCN",\
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
"audio" : {"timestamps" : ("00:00", "00:30" ), "volume" : 0.999 },\
"video" : "amd_gcn.mp4"\
})

configs["episodes"].append(\
{ "title": "GCN in XBox One",\
"audio" : {"timestamps" : ("00:30", "00:37.5" ), "volume" : 0.999 },\
"video" : "xbox_one_gpu.mp4",\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Media encoding engine",\
"audio" : {"timestamps" : ("00:37.5", "00:51" ), "volume" : 0.999 },\
"video" : "gcn_vce.mp4",\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "RX 6500xt Rant",\
"audio" : {"timestamps" : ("00:51", "00:57" ), "volume" : 0.9 },\
"video" : "6500xt_no_video_encoding.avi",\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "HD 7770 - the mid range card",\
"audio" : {"timestamps" : ("00:57", "01:25" ), "volume" : 0.999 },\
"video" : "IMG_0027.MOV"\
})

configs["episodes"].append(\
{ "title": "The GPU",\
"audio" : {"timestamps" : ("01:25", "01:58.5" ), "volume" : 0.999 },\
"video" : "tech_powerup_video_card.mp4"\
})

configs["episodes"].append(\
{ "title": "The video card and thermal results",\
"audio" : {"timestamps" : ("01:58.5", "02:16" ), "volume" : 0.999 },\
"video" : "IMG_0024.MOV"\
})

configs["episodes"].append(\
{ "title": "Thermal results - values",\
"audio" : {"timestamps" : ("02:16", "02:29" ), "volume" : 0.999 },\
"video" : "stock_heaven_720p_tesselationModerate.mp4",\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Apex Legends",\
"audio" : {"timestamps" : ("02:29", "02:55" ), "volume" : 0.97  },\
"video" : "stock_ApexLegends_1080p.mp4", \
"overlay" : { \
    "text" : ["'Apex Legends'",\
              "'1080p, low setings - Average\: 57fps, 1\\\% lows\: 39fps'",\
              "'720p, low setings - Average\: 65fps, 1\\\% lows\: 49fps'"]\
}, \
})

configs["episodes"].append(\
{ "title": "CoD Warzone",\
"audio" : {"timestamps" : ("02:55", "03:13" ) , "volume" : 0.97 },\
"overlay" : { \
    "benchmark" : { \
        "FPS values" : [44, 33], \
        "settings" : "720p, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Hyperscape",\
"audio" : {"timestamps" : ("03:13", "03:30" ) , "volume" : 0.97 },\
"overlay" : { \
    "benchmark" : { \
        "FPS values" : [0, 0], \
        "settings" : "720p, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Battlefield V",\
"audio" : {"timestamps" : ("03:30","04:03" ) },\
"overlay" : { \
    "benchmark" : { \
        "FPS values" : [54, 30], \
        "settings" : "720p, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Control",\
"audio" : {"timestamps" : ("04:03", "04:28") },\
"overlay" : { \
    "benchmark" : { \
        "FPS values" : [45, 14], \
        "settings" : "720p, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Rainbow Six: Siege",\
"audio" : {"timestamps" : ("04:28", "05:08") },\
"overlay" : { \
    "text" : ["'Rainbow Six\: Siege'",\
              "'1080p, low setings, 100\\\% render scale - Average\: 50fps, 1\\\% lows\: 39fps'",\
              "'720p, low setings, 100\\\% render scale - Average\: 96fps, 1\\\% lows\: 64fps'",\
              "'1080p, low setings, 50\\\% render scale - Average\: 84fps, 1\\\% lows\: 71fps'",\
              "'720p, low setings, 50\\\% render scale - Average\: 125fps, 1\\\% lows\: 76fps'"]\
}, \
})

configs["episodes"].append(\
{ "title": "Alien: Isolation",\
"audio" : {"timestamps" : ("05:08","05:33") },\
"overlay" : { \
    "benchmark" : { \
        "FPS values" : [51, 30], \
        "settings" : "1080p, ultra settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Counter Strike: Global Offensive",\
"audio" : {"timestamps" : ("05:33", "05:56") },\
"overlay" : { \
    "text" : ["'Counter Strike\: Global Offensive'",\
              "'Capturing with MSI Afterburner decreases the FPS in CSGO.'", \
              "'1080p, low settings - Average\: 107fps, 1\\\% lows\: 54fps'"]\
}, \
})

configs["episodes"].append(\
{ "title": "DOTA2",\
"audio" : {"timestamps" : ("05:56", "06:10"), "volume" : 0.97 },\
"overlay" : { \
    "benchmark" : { \
        "FPS values" : [87, 42], \
        "settings" : "1080p, low settings, 100% render scale", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Fortnite",\
"audio" : {"timestamps" : ("06:10", "06:34") },\
"overlay" : { \
    "benchmark" : { \
        "FPS values" : [76, 41, 41], \
        "settings" : "1080p, performance mode, view distance FAR, 100% render scale", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Rocket League",\
"audio" : {"timestamps" : ("06:34", "06:45") },\
"overlay" : { \
    "benchmark" : { \
        "FPS values" : [85, 30, 25], \
        "settings" : "1080p, low settings, 100% render scale", \
    }\
}, \
})


configs["episodes"].append(\
{ "title": "Splitgate",\
"audio" : {"timestamps" : ("06:45", "07:18") },\
"overlay" : { \
    "text" : ["'Splitgate'",\
              "'1080p, low setings - Average\: 73fps, 1\\\% lows\: 39fps, 0.1\\\% lows\: 17fps'",\
              "'720p, low setings - Average\: 119fps, 1\\\% lows\: 61fps, 0.1\\\% lows\: 11fps'"]\
}, \
})

configs["episodes"].append(\
{ "title": "Valorant",\
"audio" : {"timestamps" : ("07:18", "07:42") },\
"overlay" : { \
    "benchmark" : { \
        "FPS values" : [143, 91, 29], \
        "settings" : "1080p, low settings", \
    }\
}, \
})


configs["episodes"].append(\
{ "title": "Genshin Impact",\
"audio" : {"timestamps" : ("07:42", "08:04") },\
"overlay" : { \
    "benchmark" : { \
        "FPS values" : [57, 40], \
        "settings" : "1080p, low settings, 1.0 render scale", \
    }\
}, \
})


configs["episodes"].append(\
{ "title": "Paladins",\
"audio" : {"timestamps" : ("08:04", "08:18") , "volume" : 0.97 },\
"overlay" : { \
    "benchmark" : { \
        "FPS values" : [102, 52, 12], \
        "settings" : "1080p, high settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Realm Royale",\
"audio" : {"timestamps" : ("08:18", "08:32") },\
"overlay" : { \
    "benchmark" : { \
        "FPS values" : [92, 25], \
        "settings" : "1080p, high settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Rogue Company",\
"audio" : {"timestamps" : ("08:32", "08:46") },\
"overlay" : { \
    "benchmark" : { \
        "FPS values" : [85, 43, 12], \
        "settings" : "1080p, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "World of Tanks Blitz",\
"audio" : {"timestamps" : ("08:46", "09:10") },\
"overlay" : { \
    "benchmark" : { \
        "FPS values" : [60, 43, 28], \
        "settings" : "1080p, high settings", \
    }\
}, \
})


configs["episodes"].append(\
{ "title": "Warframe",\
"audio" : {"timestamps" : ("09:10", "09:32") },\
"overlay" : { \
    "benchmark" : { \
        "FPS values" : [81, 50, 38], \
        "settings" : "1080p, high settings", \
    }\
}, \
})


configs["episodes"].append(\
{ "title": "Usefulness of used GPUs",\
"audio" : {"timestamps" : ("09:32", "10:47"), "volume" : 0.999 },\
"video" : "Intel_igp_11thGen.mp4"\
})

configs["episodes"].append(\
{ "title": "Usefulness of the HD 7770",\
"audio" : {"timestamps" : ("10:47", "11:24") },\
"video" : "stock_Control_720p.mp4"\
})

configs["episodes"].append(\
{ "title": "Personal notes for the HD 7770",\
"audio" : {"timestamps" : ("11:24", "12:05"), "volume" : 0.999},\
"video" : "IMG_0027.MOV"\
})

scriptedvided.makeVideoForEpisode(configs["episodes"][27], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][9], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][8], configs)
#print(scriptedvided.makeVideoForEpisode(configs["episodes"][9], configs))
#print(scriptedvided.getSuitableVideoStream(configs["episodes"][9], configs))
#print (configs["youtube"])
#print(scriptedvided.getMusicCreditsString(configs["backgroundTrack"]))
#scriptedvided.makeVideo(configs)

