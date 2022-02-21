import scriptedvided

configs = { "defaultAudioFile" : "hd5770_4.ogg",\
"mediaFolder" : "C:\\Users\\Admin\\Videos\\hd5770", \
"stockFolder" : "C:\\Users\\Admin\\Videos\stock",\
"outputFolder" : "C:\\Users\\Admin\\Videos\\hd5770\\output", \
"outputFile" : "hd5770.mp4", \
"episodes" : []}

configs["episodes"].append(\
{ "title": "Context of the launch",\
"audio" : {"timestamps" : ("00:00", "00:24" ) },\
})

configs["episodes"].append(\
{ "title": "The GPU",\
"audio" : {"timestamps" : ("00:24", "00:55" ) },\
})

configs["episodes"].append(\
{ "title": "The video card",\
"audio" : {"timestamps" : ("00:55", "01:34" ) },\
})

configs["episodes"].append(\
{ "title": "Better thermal solutions",\
"audio" : {"timestamps" : ("01:34", "02:02" ) },\
})

configs["episodes"].append(\
{ "title": "Apex Legends",\
"audio" : {"timestamps" : ("02:02", "02:14" ) },\
"video" : "stock_ApexLegends_1080p.mp4", \
"overlay" : { \
    "benchmark" : { \
        "FPS values" : [0, 0, 0], \
        "settings" : "1080p, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "CoD Warzone, Hyperscape",\
"audio" : {"timestamps" : ("02:14", "02:25" ) },\
"overlay" : { \
    "benchmark" : { \
        "FPS values" : [0, 0, 0], \
        "settings" : "1080p, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Battlefield V",\
"audio" : {"timestamps" : ("02:25","02:42" ) },\
"video" : {"file" : "hd5770_bfv_allIntro_720pLow.mp4", "start" : "03:33" },\
"overlay" : { \
    "benchmark" : { \
        "FPS values" : [38, 23, 18], \
        "settings" : "720p, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Control",\
"audio" : {"timestamps" : ("02:42", "02:54") },\
"overlay" : { \
    "benchmark" : { \
        "FPS values" : [18, 11, 10], \
        "settings" : "720p, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Rainbow Six: Siege",\
"audio" : {"timestamps" : ("02:54", "03:19") },\
"overlay" : { \
    "text" : ["'Rainbow Six\: Siege'",\
              "'1080p, low setings, 50\\\% render scale - Average\: 46fps, 1\\\% lows\: 25fps'",\
              "'720p, low setings, 50\\\% render scale - Average\: 71fps, 1\\\% lows\: 32fps'"]\
}, \
})

configs["episodes"].append(\
{ "title": "Alien: Isolation",\
"audio" : {"timestamps" : ("03:19","03:38") },\
"overlay" : { \
    "benchmark" : { \
        "FPS values" : [39, 26, 16], \
        "settings" : "1080p, ultra settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Counter Strike: Global Offensive",\
"audio" : {"timestamps" : ("03:38", "03:47.5") },\
"overlay" : { \
    "text" : ["'Counter Strike\: Global Offensive'",\
              "'Capturing with MSI Afterburner decreases the FPS in CSGO.'", \
              "'1080p, low settings - Average\: 68fps, 1\\\% lows\: 29fps, 0.1\\\% lows\: 26fps'"]\
}, \
})

configs["episodes"].append(\
{ "title": "DOTA2",\
"audio" : {"timestamps" : ("03:47.5", "04:02") },\
"overlay" : { \
    "benchmark" : { \
        "FPS values" : [77, 38, 24], \
        "settings" : "1080p, low settings, 100% render scale", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Fortnite",\
"audio" : {"timestamps" : ("04:02", "04:19") },\
"overlay" : { \
    "benchmark" : { \
        "FPS values" : [65, 29, 18], \
        "settings" : "1080p, performance mode, view distance FAR, 100% render scale", \
    }\
}, \
})



configs["episodes"].append(\
{ "title": "Rocket League",\
"audio" : {"timestamps" : ("04:19", "04:27") },\
"overlay" : { \
    "benchmark" : { \
        "FPS values" : [63, 24, 22], \
        "settings" : "1080p, low settings, 100% render scale", \
    }\
}, \
})


configs["episodes"].append(\
{ "title": "Splitgate",\
"audio" : {"timestamps" : ("04:27", "04:37") },\
"overlay" : { \
    "text" : ["'Splitgate'",\
              "'1080p, low setings - Average\: 41fps, 1\\\% lows\: 25fps, 0.1\\\% lows\: 16fps'",\
              "'720p, low setings - Average\: 68fps, 1\\\% lows\: 25fps, 0.1\\\% lows\: 16fps'"]\
}, \
})

configs["episodes"].append(\
{ "title": "Valorant",\
"audio" : {"timestamps" : ("04:37", "04:50") },\
"overlay" : { \
    "benchmark" : { \
        "FPS values" : [132, 44, 10], \
        "settings" : "1080p, low settings", \
    }\
}, \
})


configs["episodes"].append(\
{ "title": "Genshin Impact",\
"audio" : {"timestamps" : ("04:51", "05:17") },\
"overlay" : { \
    "benchmark" : { \
        "FPS values" : [58, 30, 30], \
        "settings" : "1080p, low settings, 0.8 render scale", \
    }\
}, \
})


configs["episodes"].append(\
{ "title": "Paladins",\
"audio" : {"timestamps" : ("05:17", "05:33") },\
"overlay" : { \
    "benchmark" : { \
        "FPS values" : [82, 31, 11], \
        "settings" : "1080p, high settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Realm Royale",\
"audio" : {"timestamps" : ("05:33", "05:52") },\
"overlay" : { \
    "benchmark" : { \
        "FPS values" : [56, 30, 10], \
        "settings" : "1080p, high settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Rogue Company",\
"audio" : {"timestamps" : ("05:52", "06:12") },\
"overlay" : { \
    "benchmark" : { \
        "FPS values" : [66, 24, 13], \
        "settings" : "1080p, high settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "World of Tanks Blitz",\
"audio" : {"timestamps" : ("06:12", "06:36") },\
"overlay" : { \
    "benchmark" : { \
        "FPS values" : [60, 52, 42], \
        "settings" : "1080p, high settings", \
    }\
}, \
})


configs["episodes"].append(\
{ "title": "Warframe",\
"video" : "hd5770_Warframe_armsDealer_1080pLow.mp4",\
"audio" : {"timestamps" : ("06:36", "06:57") },\
"overlay" : { \
    "benchmark" : { \
        "FPS values" : [121, 51, 3], \
        "settings" : "1080p, high settings", \
    }\
}, \
})


configs["episodes"].append(\
{ "title": "Usefullness of used GPUs",\
"audio" : {"timestamps" : ("06:57", "08:13") },\
})

configs["episodes"].append(\
{ "title": "Usefullness of the HD 5770",\
"audio" : {"timestamps" : ("08:13", "08:32") },\
})

configs["episodes"].append(\
{ "title": "HD 5770 for geeks",\
"audio" : {"timestamps" : ("08:32", "09:07") },\
})

for episode in configs["episodes"]:
    try:
        scriptedvided.makeVideoForEpisode(episode, configs)
    except:
        print ("One error ...")
#print (str(scriptedvided.makeVideoForEpisode(configs["episodes"][10], configs)) + "\n")

