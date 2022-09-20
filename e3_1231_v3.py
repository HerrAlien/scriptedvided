import scriptedvided

configs = { "defaultAudioFile" : "Xeon_E3-1231_V3.ogg",\
"mediaFolder" : "C:\\Users\\Admin\\Videos\\E3_1231_v3", \
"stockFolder" : "C:\\Users\\Admin\\Videos\stock",\
"benchmarkFile" : "C:\\Users\\Admin\\Videos\\E3_1231_v3\\Benchmark_E3_1231_v3.txt",\
"outputFolder" : "C:\\Users\\Admin\\Videos\\E3_1231_v3\\output", \
"outputFile" : "Haswell_4c_8t.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#00408080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "H:\\Muzica\\royalty free\\Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3",\
"timestamps" : ("00:30", None ), "destinationTimestamp" : {"title" : "TLDW", "until" : "Apex Legends"}}, \
{"file" : "H:\\Muzica\\royalty free\\bensound-summer.mp3", "timestamps" : ("00:00", None ), "destinationTimestamp" : { "title": "Conclusion", "until" : "Blooper" }}, \
], "volume" : 0.03 },\
"episodes" : [],\
"youtube" : {"title" : "Reviewing Intel's i7 4770(-ish) in 2022", \
"description" : '''In this video, we'll take a closer look at Intel's 4th gen i7. Sort of - we're using the Xeon equivalent ''',\
"links" : '''
More games tested with Haswell based i7s:
https://www.youtube.com/watch?v=uy5PXnWFllU
https://www.youtube.com/watch?v=YRpIMCOIpi8

Specs for the Xeon E3 1231 v3 CPU:
https://www.intel.com/content/www/us/en/products/sku/80910/intel-xeon-processor-e31231-v3-8m-cache-3-40-ghz/specifications.html

Specs for the Core i7 4770 CPU:
https://www.intel.com/content/www/us/en/products/sku/75122/intel-core-i74770-processor-8m-cache-up-to-3-90-ghz/specifications.html

Other videos used:
Hyper Threading video: https://www.youtube.com/watch?v=VcoVYfDVEww
HUB review of the 12600k: https://www.youtube.com/watch?v=LzhwVLUVork

''', \
"tags" : "Intel,4th Gen,Haswell,core i7,i7,Xeon,4770,i7 4770",\
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
"audio" : {"timestamps" : ("00:00", "00:14" ), "volume" : 0.999 },\
"video" : {"file" : "HyperThreading.mkv", "start" : "00:40"}\
})

configs["episodes"].append(\
{ "title": "Why test the 4th gen i7",\
"audio" : {"timestamps" : ("00:14", "00:53" ), "volume" : 0.999 },\
"video" : {"file" : "hub_r5_i5.mkv", "start":"00:00"}\
})

# consider inside of the case though, or capture done with HT off
configs["episodes"].append(\
{ "title": "The setup used for these tests",\
"audio" : {"timestamps" : ("00:53", "01:14" ), "volume" : 0.999 },\
"video" : {"file": "z230_cpuz_intel_ark.mkv", "start":"00:00"},\
})

configs["episodes"].append(\
{ "title": "Multiplayer games FTW",\
"audio" : {"timestamps" : ("01:14", "01:26" ), "volume" : 0.999 },\
"isChapter" : False,\
"video" : "stock_RogueCompany_1080pLow.mp4"\
})


configs["episodes"].append(\
{ "title": "Ram config",\
"audio" : {"timestamps" : ("01:26", "01:36.5" ), "volume" : 0.999 },\
"isChapter" : False,\
"video" : {"file": "z230_cpuz_intel_ark.mkv", "start":"01:00"},\
})

configs["episodes"].append(\
{ "title": "Try to bottleneck the CPU",\
"audio" : {"timestamps" : ("01:36.5", "02:03" ), "volume" : 0.999 },\
"isChapter" : False,\
"video" : "i5_4690_V_alorant.mp4",\
"overlay" : { \
    "text" : ["'Footage taken with hyperthreading turned OFF'"]\
}, \
})

configs["episodes"].append(\
{ "title": "Apex Legends",\
"audio" : {"timestamps" : ("02:03", "03:04" ), "volume" : 0.97  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1024 x 768, low settings", \
    }\
}\
})

configs["episodes"].append(\
{ "title": " CoD Warzone ",\
"audio" : {"timestamps" : ("03:04", "03:25" ) , "volume" : 0.97 },\
"video" : "wz.mp4"\
})

configs["episodes"].append(\
{ "title": "CoD Warzone",\
"isChapter" : False,\
"audio" : {"timestamps" : ("03:25", "03:56.5" ) , "volume" : 0.97 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "800 x 600, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": " Battlefield V ",\
"audio" : {"timestamps" : ("03:56.5", "04:38" ) , "volume" : 0.97 },\
"video" : "batf5.mp4"\
})

configs["episodes"].append(\
{ "title": "Battlefield V",\
"isChapter" : False,\
"audio" : {"timestamps" : ("04:38", "04:55" ) , "volume" : 0.97 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "720p, 50% 3D scale, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Rainbow Six: Siege",\
"audio" : {"timestamps" : ("04:55", "05:50") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1024 x 768, 35% 3D scale, low settings", \
    }\
}, \
})


configs["episodes"].append(\
{ "title": "Counter Strike: Global Offensive",\
"audio" : {"timestamps" : ("05:50", "06:42.1") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "852 x 480, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Fortnite",\
"audio" : {"timestamps" : ("06:42", "07:23") },\
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
###              "'1080p, low settings - Average\: 156fps, 1\\\% lows\: 15fps'",\
###              "'720p, low settings - Average\: 234fps, 1\\\% lows\: 101fps'"]\
###}, \
###})

configs["episodes"].append(\
{ "title": "Valorant",\
"audio" : {"timestamps" : ("07:23", "08:07") },\
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
"audio" : {"timestamps" : ("08:07", "08:23"), "volume" : 0.999 },\
"video" : {"file" : "HyperThreading.mkv", "start" : "00:40"}\
})


configs["episodes"].append(\
{ "title": "Conclusion - interesting data",\
"isChapter" : False,\
"audio" : {"timestamps" : ("08:23", "08:34"), "volume" : 0.999 },\
"video" : {"file" : "Z230_closed.mp4", "start" : "01:00"} \
})

configs["episodes"].append(\
{ "title": "Conclusion - still good",\
"isChapter" : False,\
"audio" : {"timestamps" : ("08:34" , "08:50.5"), "volume" : 0.999 },\
"video" : "stock_Splitgate_1080pLow.mp4"\
})


################################ more chapters needed


configs["episodes"].append(\
{ "title": "Blooper",\
"isChapter" : False,\
"audio" : {"timestamps" : ( "08:55", "08:59.07"), "volume" : 0.999},\
"video" : {"file" : "HyperThreading.mkv", "start" : "00:40"}\
})


#scriptedvided.makeVideoForEpisode(configs["episodes"][27], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][9], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][8], configs)
#print(scriptedvided.makeVideoForEpisode(configs["episodes"][9], configs))
#print(scriptedvided.getSuitableVideoStream(configs["episodes"][9], configs))
#print (configs["youtube"])
#print(scriptedvided.getMusicCreditsString(configs["backgroundTrack"]))
#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "Apex Legends"][0], configs)
#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "Counter Strike: Global Offensive"][0], configs)
scriptedvided.makeVideo(configs)

