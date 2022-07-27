import scriptedvided

configs = { "defaultAudioFile" : "r9_280_2.ogg",\
"mediaFolder" : "C:\\Users\\Admin\\Videos\\E3_1231_v3_noHT", \
"stockFolder" : "C:\\Users\\Admin\\Videos\stock",\
"benchmarkFile" : "C:\\Users\\Admin\\Videos\\E3_1231_v3_noHT\\Benchmark_R9_280.txt",\
"outputFolder" : "C:\\Users\\Admin\\Videos\\E3_1231_v3_noHT\\output", \
"outputFile" : "r9_280.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#00408080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "H:\\Muzica\\royalty free\\Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3",\
"timestamps" : ("00:30", None ), "destinationTimestamp" : {"title" : "Context of the launch", "until" : "Video capturing leads to CPU bottleneck"}}, \
{"file" : "H:\\Muzica\\royalty free\\bensound-summer.mp3", "timestamps" : ("00:00", None ), "destinationTimestamp" : { "title": "Usefulness of used GPUs", "until" : "Blooper" }}, \
], "volume" : 0.03 },\
"episodes" : [],\
"youtube" : {"title" : "Reviewing Intel's 4th gen i5(-ish) in 2022", \
"description" : '''In this video, we'll take a closer look at Intel's 4th gen i5. Sort of. ''',\
"links" : '''
More games tested with Haswell based i5s:

Specs for the Xeon E3 1231 v3 CPU:

Specs for the Core i5 4690 CPU:


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
"audio" : {"timestamps" : ("00:00", "00:12" ), "volume" : 0.999 },\
"video" : "r7_r9_gcn_launch.mp4"\
})

configs["episodes"].append(\
{ "title": "Why test the 4th gen i5",\
"audio" : {"timestamps" : ("00:12", "00:39.33" ), "volume" : 0.999 },\
"video" : "HD700_R7_R9_renames.mkv"\
})

configs["episodes"].append(\
{ "title": "Multiplayer games FTW",\
"audio" : {"timestamps" : ("00:46", "00:59" ), "volume" : 0.999 },\
"isChapter" : False,\
"video" : "Phillip_HD7000.mkv"\
})

configs["episodes"].append(\
{ "title": "The setup used for these tests",\
"audio" : {"timestamps" : ("00:59", "01:50" ), "volume" : 0.999 },\
"video" : "R9_280_GPU.mkv",\
})

configs["episodes"].append(\
{ "title": "Ram config",\
"audio" : {"timestamps" : ("00:46", "00:59" ), "volume" : 0.999 },\
"isChapter" : False,\
"video" : "Phillip_HD7000.mkv"\
})

configs["episodes"].append(\
{ "title": "Try to bottleneck the CPU",\
"audio" : {"timestamps" : ("00:46", "00:59" ), "volume" : 0.999 },\
"isChapter" : False,\
"video" : "Phillip_HD7000.mkv"\
})



configs["episodes"].append(\
{ "title": "Apex Legends",\
"audio" : {"timestamps" : ("04:18", "04:45" ), "volume" : 0.99  },\
"video" : "i5_4690_A_pexLegends.mp4"\
})

configs["episodes"].append(\
{ "title": "Apex Legends - fps",\
"isChapter" : False,\
"audio" : {"timestamps" : ("04:18", "04:45" ), "volume" : 0.97  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1024 x 768, low settings", \
    }\
})

configs["episodes"].append(\
{ "title": "CoD Warzone",\
"audio" : {"timestamps" : ("04:45", "05:05" ) , "volume" : 0.97 },\
"video" : "i5_4690_W_arzone.mp4"\
})

configs["episodes"].append(\
{ "title": "CoD Warzone - fps",\
"isChapter" : False,\
"audio" : {"timestamps" : ("04:45", "05:05" ) , "volume" : 0.97 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "800 x 600, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Battlefield V",\
"audio" : {"timestamps" : ("05:05", "05:32" ) , "volume" : 0.97 },\
"video" : "i5_4690_B_FV.mp4"\
})

configs["episodes"].append(\
{ "title": "Battlefield V - fps",\
"isChapter" : False,\
"audio" : {"timestamps" : ("05:05", "05:32" ) , "volume" : 0.97 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "720p, 50% 3D scale, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Rainbow Six: Siege",\
"audio" : {"timestamps" : ("05:58", "06:33") },\
"video" : "i5_4690_R_6S.mp4"\
})

configs["episodes"].append(\
{ "title": "Rainbow Six: Siege - fps",\
"isChapter" : False,\
"audio" : {"timestamps" : ("05:58", "06:33") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "720p, 35% 3D scale, low settings", \
    }\
}, \
})


configs["episodes"].append(\
{ "title": "Counter Strike: Global Offensive",\
"audio" : {"timestamps" : ("07:01", "07:21.5") },\
"video" : "i5_4690_C_SGO.mp4"\
})

configs["episodes"].append(\
{ "title": "Counter Strike: Global Offensive - fps",\
"isChapter" : False,\
"audio" : {"timestamps" : ("07:01", "07:21.5") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "640 x 480, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Fortnite",\
"audio" : {"timestamps" : ("07:42", "08:04") },\
"video" : "i5_4690_F_ortnite.mp4"\
})

configs["episodes"].append(\
{ "title": "Fortnite - fps",\
"isChapter" : False,\
"audio" : {"timestamps" : ("07:42", "08:04") },\
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
{ "title": "Valorant",\
"audio" : {"timestamps" : ("08:55", "09:22") },\
"video" : "i5_4690_V_alorant.mp4"\
})

configs["episodes"].append(\
{ "title": "Valorant - fps",\
"isChapter" : False,\
"audio" : {"timestamps" : ("08:55", "09:22") },\
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
"audio" : {"timestamps" : ("11:29", "11:57"), "volume" : 0.999 },\
"video" : "r9_280_f_o_r_t_n_i_t_e_1.mp4"\
})

################################ more chapters needed


configs["episodes"].append(\
{ "title": "Blooper",\
"isChapter" : False,\
"audio" : {"timestamps" : ( "12:49", "12:55"), "volume" : 0.999},\
"video" : "r9_280_f_o_r_t_n_i_t_e_2.mp4"\
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

