import scriptedvided

configs = { "defaultAudioFile" : "hd5870.ogg",\
"mediaFolder" : "C:\\Users\\Admin\\Videos\\hd5870", \
"stockFolder" : "C:\\Users\\Admin\\Videos\stock",\
"benchmarkFile" : "C:\\Users\\Admin\\Videos\\hd5870\\Benchmark_hd5870.txt",\
"outputFolder" : "C:\\Users\\Admin\\Videos\\hd5870\\output", \
"outputFile" : "hd5870.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "H:\\Muzica\\royalty free\\Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3",\
"timestamps" : ("00:30", None ), "destinationTimestamp" : {"title" : "TLDW", "until" : "Apex Legends"}}, \
{"file" : "H:\\Muzica\\royalty free\\bensound-summer.mp3", "timestamps" : ("00:00", None ), "destinationTimestamp" : { "title": "Usefulness of used GPUs", "until" : "Blooper" }}, \
], "volume" : 0.03 },\
"episodes" : [],\
"youtube" : {"title" : "The Radeon HD 5870 in 2022", \
"description" : '''In this video, we'll take a closer look at the XFX variant of the Radeon HD 5870.

As usual, we'll use the E3-1241 v3 CPU (i7 4770 equivalent) and 32 GB DDR3 at 1600 MHz to pair it with.''',\
"links" : '''
More games tested with the Radeon HD 5870:
https://www.youtube.com/watch?v=Q12yzOaJY7s
https://www.youtube.com/watch?v=I2i-Fb-B2HA

The HD 5770 review: https://www.youtube.com/watch?v=9ZrKAwA6MbQ
The HD 6850 review: https://www.youtube.com/watch?v=N_KyY1HSPNk

TechPowerup entry:
https://www.techpowerup.com/gpu-specs/radeon-hd-5870.c253

Intel 11th gen processors:
The core i5 11400 (has an IGPU): https://ark.intel.com/content/www/us/en/ark/products/212270/intel-core-i511400-processor-12m-cache-up-to-4-40-ghz.html
The core i5 11400F (no IGPU): https://ark.intel.com/content/www/us/en/ark/products/212271/intel-core-i511400f-processor-12m-cache-up-to-4-40-ghz.html

''', \
"tags" : "AMD,ATI,Radeon,Terascale 2,HD5870,HD 5870",\
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
"audio" : {"timestamps" : ("00:00", "00:14.5" ), "volume" : 0.999 },\
"video" : {"file":"hd5870_breel_4tnite_2.mp4",} \
})

configs["episodes"].append(\
{ "title": "Context of the launch",\
"audio" : {"timestamps" : ("00:14.5", "00:36" ), "volume" : 0.999 },\
"video" : {"file":"amd_2010.mp4",} \
})

configs["episodes"].append(\
{ "title": "Context of the launch - previous 5770",\
"audio" : {"timestamps" : ("00:36", "00:49.5" ), "volume" : 0.999 },\
"isChapter" : False,\
"video" : "hd5770_fortnite_B-Reel.mp4"\
})


configs["episodes"].append(\
{ "title": "The GPU and video card",\
"audio" : {"timestamps" : ("00:49.5", "01:22" ), "volume" : 0.999 },\
"video" : "hd5870_GPU.mkv",\
})

configs["episodes"].append(\
{ "title": "XFX video card",\
"audio" : {"timestamps" : ("01:22", "01:38.5" ), "volume" : 0.999 },\
"isChapter" : False,\
"video" : "hd5870_breel_card_nobox.mp4"\
})

configs["episodes"].append(\
{ "title": "Cooling and thermals",\
"audio" : {"timestamps" : ( "01:38.5", "02:24" ), "volume" : 0.999 },\
"video" : {"file" : "hd5870_cooling.mp4",  },\
})

configs["episodes"].append(\
{ "title": "Cooling and thermals - temps",\
"audio" : {"timestamps" : ( "02:24", "02:39" ), "volume" : 0.999 },\
"video" : "hd5870_heaven.mp4",\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Cooling and thermals - warframe",\
"audio" : {"timestamps" : ( "02:39" , "02:54" ), "volume" : 0.999 },\
"video" : "hd5870_Warframe.mp4",\
"isChapter" : False,\
})


configs["episodes"].append(\
{ "title": "Apex Legends",\
"audio" : {"timestamps" : ("02:54", "03:23" )  },\
"video" : "hd5870_Amernime_A_p_e_x.mkv",\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1080p, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "CoD Warzone",\
"audio" : {"timestamps" : ("12:10.5", "12:24.2" )  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "720p, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Battlefield V",\
"audio" : {"timestamps" : ("03:23", "03:48" ) },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "720p, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Control",\
"audio" : {"timestamps" : ("03:48", "04:16.5") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "720p, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Rainbow Six: Siege",\
"audio" : {"timestamps" : ("04:16.5", "04:49") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "720p, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Alien: Isolation",\
"audio" : {"timestamps" : ("04:49","05:22") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1080p, ultra settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Counter Strike: Global Offensive",\
"audio" : {"timestamps" : ("05:22", "05:48") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1080p, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "DOTA2",\
"audio" : {"timestamps" : ("05:48", "06:08.5"), "volume" : 0.97 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1080p, low settings, 100% render scale", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Fortnite",\
"audio" : {"timestamps" : ("06:08.5", "06:31") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1080p, performance mode, view distance FAR, 100% render scale", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Rocket League",\
"audio" : {"timestamps" : ("06:31", "06:59") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1080p, low settings, 100% render scale", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Splitgate",\
"audio" : {"timestamps" : ("06:59", "07:30") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1080p, low settings, 100% render scale", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Valorant",\
"audio" : {"timestamps" : ("07:30", "07:57") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1080p, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Genshin Impact",\
"audio" : {"timestamps" : ("07:57", "08:27") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1080p, low settings, 1.0 render scale", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Paladins",\
"audio" : {"timestamps" : ("08:27", "09:01") , "volume" : 0.97 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1080p, high settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Realm Royale",\
"audio" : {"timestamps" : ("09:01", "09:29.5") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1080p, high settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Rogue Company",\
"audio" : {"timestamps" : ("09:29.5", "09:51") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1080p, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "World of Tanks Blitz",\
"audio" : {"timestamps" : ("09:51", "10:13.8") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1080p, high settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Warframe",\
"audio" : {"timestamps" : ("10:13.8", "10:44") },\
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
{ "title": "Usefulness of the HD 5870",\
"audio" : {"timestamps" : ("10:44", "11:04"), "volume" : 0.999 },\
"video" : {"file" : "hd5870_breel_card_nobox.mp4", },\
})

configs["episodes"].append(\
{ "title": "Good performance",\
"isChapter" : False,\
"audio" : {"timestamps" : ("11:04", "11:56"), "volume" : 0.999 },\
"video" : "hd5870_breel_4tnite.mp4",\
})


configs["episodes"].append(\
{ "title": "Blooper",\
"isChapter" : False,\
"audio" : {"timestamps" : ( "11:56", "12:10"), "volume" : 0.999},\
"video" : "hd5870_breel_R_o_g_ue.mp4",\
})


#scriptedvided.makeVideoForEpisode(configs["episodes"][27], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][9], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][8], configs)
#print(scriptedvided.makeVideoForEpisode(configs["episodes"][9], configs))
#print(scriptedvided.getSuitableVideoStream(configs["episodes"][9], configs))
#print (configs["youtube"])
#print(scriptedvided.getMusicCreditsString(configs["backgroundTrack"]))
#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "Usefulness of the HD 6850"][0], configs)
#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "CoD Warzone"][0], configs)
scriptedvided.makeVideo(configs)

