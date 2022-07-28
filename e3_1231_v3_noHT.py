import scriptedvided

configs = { "defaultAudioFile" : "Xeon_E3-1231_V3_noHT.ogg",\
"mediaFolder" : "C:\\Users\\Admin\\Videos\\E3_1231_v3_noHT", \
"stockFolder" : "C:\\Users\\Admin\\Videos\stock",\
"benchmarkFile" : "C:\\Users\\Admin\\Videos\\E3_1231_v3_noHT\\Benchmark_E3_1231_v3_noHT.txt",\
"outputFolder" : "C:\\Users\\Admin\\Videos\\E3_1231_v3_noHT\\output", \
"outputFile" : "r9_280.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#00408080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "H:\\Muzica\\royalty free\\Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3",\
"timestamps" : ("00:30", None ), "destinationTimestamp" : {"title" : "Context of the launch", "until" : " Apex Legends "}}, \
{"file" : "H:\\Muzica\\royalty free\\bensound-summer.mp3", "timestamps" : ("00:00", None ), "destinationTimestamp" : { "title": "Conclusion", "until" : "Blooper" }}, \
], "volume" : 0.03 },\
"episodes" : [],\
"youtube" : {"title" : "Reviewing Intel's 4th gen i5(-ish) in 2022", \
"description" : '''In this video, we'll take a closer look at Intel's 4th gen i5. Sort of. ''',\
"links" : '''
More games tested with Haswell based i5s:

Specs for the Xeon E3 1231 v3 CPU:
https://www.intel.com/content/www/us/en/products/sku/80910/intel-xeon-processor-e31231-v3-8m-cache-3-40-ghz/specifications.html

Specs for the Core i5 4670 CPU:
https://www.intel.com/content/www/us/en/products/sku/75047/intel-core-i54670-processor-6m-cache-up-to-3-80-ghz/specifications.html

''', \
"tags" : "Intel,4th Gen,Haswell,core i5,i5,Xeon",\
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
"audio" : {"timestamps" : ("00:00", "00:10" ), "volume" : 0.999 },\
"video" : "Haswell_i5.mkv"\
})

configs["episodes"].append(\
{ "title": "Why test the 4th gen i5",\
"audio" : {"timestamps" : ("00:10", "00:36.5" ), "volume" : 0.999 },\
"video" : {"file" : "hub_r5_i5.mkv", "start":"00:00"}\
})

configs["episodes"].append(\
{ "title": "Multiplayer games FTW",\
"audio" : {"timestamps" : ("00:36.5", "00:55.6" ), "volume" : 0.999 },\
"isChapter" : False,\
"video" : "stock_RogueCompany_1080pLow.mp4"\
})


# consider inside of the case ...
configs["episodes"].append(\
{ "title": "The setup used for these tests",\
"audio" : {"timestamps" : ("00:55.6", "01:14.5" ), "volume" : 0.999 },\
"video" : {"file": "z230_cpuz_taskManager.mkv", "start":"00:00"},\
})

configs["episodes"].append(\
{ "title": "Ram config",\
"audio" : {"timestamps" : ("01:14.5", "01:22.5" ), "volume" : 0.999 },\
"isChapter" : False,\
"video" : {"file": "z230_cpuz_taskManager.mkv", "start":"00:30"},\
})

configs["episodes"].append(\
{ "title": "Try to bottleneck the CPU",\
"audio" : {"timestamps" : ("01:22.5", "01:42" ), "volume" : 0.999 },\
"isChapter" : False,\
"video" : "i5_4690_F_ortnite.mp4"\
})

configs["episodes"].append(\
{ "title": " Apex Legends ",\
"audio" : {"timestamps" : ("01:42", "02:04.2" ), "volume" : 0.99  },\
"video" : "i5_4690_A_pexLegends.mp4"\
})

configs["episodes"].append(\
{ "title": "Apex Legends",\
"isChapter" : False,\
"audio" : {"timestamps" : ("02:04.2", "02:21" ), "volume" : 0.97  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1024 x 768, low settings", \
    }\
}\
})

configs["episodes"].append(\
{ "title": " CoD Warzone ",\
"audio" : {"timestamps" : ("02:21", "02:42" ) , "volume" : 0.97 },\
"video" : "i5_4690_W_arzone.mp4"\
})

configs["episodes"].append(\
{ "title": "CoD Warzone",\
"isChapter" : False,\
"audio" : {"timestamps" : ("02:42", "03:11.1" ) , "volume" : 0.97 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "800 x 600, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": " Battlefield V ",\
"audio" : {"timestamps" : ("03:11.1", "03:31.3" ) , "volume" : 0.97 },\
"video" : "i5_4690_B_FV.mp4"\
})

configs["episodes"].append(\
{ "title": "Battlefield V",\
"isChapter" : False,\
"audio" : {"timestamps" : ("03:31.3", "03:54" ) , "volume" : 0.97 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "720p, 50% 3D scale, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": " Rainbow Six: Siege ",\
"audio" : {"timestamps" : ("03:54", "04:17.8") },\
"video" : "i5_4690_R_6S.mp4"\
})

configs["episodes"].append(\
{ "title": "Rainbow Six: Siege",\
"isChapter" : False,\
"audio" : {"timestamps" : ("04:17.8", "04:37") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "720p, 35% 3D scale, low settings", \
    }\
}, \
})


configs["episodes"].append(\
{ "title": " Counter Strike: Global Offensive ",\
"audio" : {"timestamps" : ("04:37", "04:57.6") },\
"video" : "i5_4690_C_SGO.mp4"\
})

configs["episodes"].append(\
{ "title": "Counter Strike: Global Offensive",\
"isChapter" : False,\
"audio" : {"timestamps" : ("04:57.6", "05:23") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "640 x 480, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": " Fortnite ",\
"audio" : {"timestamps" : ("05:23", "05:38.4") },\
"video" : "i5_4690_F_ortnite.mp4"\
})

configs["episodes"].append(\
{ "title": "Fortnite",\
"isChapter" : False,\
"audio" : {"timestamps" : ("05:38.4", "05:54") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "720p, performance mode, view distance FAR, 37% render scale", \
    }\
}, \
})

###configs["episodes"].append(\
###{ "title": "Splitgate",\
###"audio" : {"timestamps" : ("08:24.5", "08:55") },\
###"overlay" : { \
###    "text" : ["'Splitgate'",\
###              "'1080p, low setings - Average\: 156fps, 1\\\% lows\: 15fps'",\
###              "'720p, low setings - Average\: 234fps, 1\\\% lows\: 101fps'"]\
###}, \
###})

configs["episodes"].append(\
{ "title": " Valorant ",\
"audio" : {"timestamps" : ("05:54", "06:15") },\
"video" : "i5_4690_V_alorant.mp4"\
})

configs["episodes"].append(\
{ "title": "Valorant",\
"isChapter" : False,\
"audio" : {"timestamps" : ("06:15", "06:37") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1024 x 768, low settings", \
    }\
}, \
})


## this can be copy-pasted, it uses a stock video with the audio already
## overlayed. Pass in a fake audio stream, at -60dB
configs["episodes"].append(\
{ "title": "Conclusion",\
"audio" : {"timestamps" : ("06:37", "07:51.5"), "volume" : 0.999 },\
"video" : "stock_GenshinImpact_1080pLow.mp4"\
})

################################ more chapters needed


configs["episodes"].append(\
{ "title": "Blooper",\
"isChapter" : False,\
"audio" : {"timestamps" : ( "07:51.5", "08:02"), "volume" : 0.999},\
"video" : "r9_280_f_o_r_t_n_i_t_e_2.mp4"\
})


#scriptedvided.makeVideoForEpisode(configs["episodes"][27], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][9], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][8], configs)
#print(scriptedvided.makeVideoForEpisode(configs["episodes"][9], configs))
#print(scriptedvided.getSuitableVideoStream(configs["episodes"][9], configs))
#print (configs["youtube"])
#print(scriptedvided.getMusicCreditsString(configs["backgroundTrack"]))
#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "Apex Legends"][0], configs)
#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "Warframe"][0], configs)
scriptedvided.makeVideo(configs)

