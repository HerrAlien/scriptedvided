import scriptedvided

configs = { "defaultAudioFile" : "i5_4570.ogg",\
"mediaFolder" : "F:\\Videos\\i5_4570", \
"stockFolder" : "F:\\Videos\\stock",\
"benchmarkFile" : "F:\\Videos\\i5_4570\\Benchmark_i5_4570.txt",\
"outputFolder" : "F:\\Videos\\i5_4570\\output", \
"outputFile" : "i5_4570.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#00008080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "The upcoming teenager", "until" : "Marvel Rivals"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Marvel Rivals", "until" : "Shadow of the Tomb Raider"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Shadow of the Tomb Raider", "until" : "Video rendering test (The GigASUS)"}}, \
{"file" : "Ferco - Inquisitiveness.ogg", "timestamps" : ("01:01", None ), "destinationTimestamp" : {"title" : "Video rendering test (The GigASUS)", "until" : "Conclusions"}}, \
{"file" : "Inspired - MaikonMusic  Free Background Music  Audio Library Release.mp3", "timestamps" : ("00:00", None ), "destinationTimestamp" : {"title" : "Conclusions", "until" : "EOF"}}, \
], "volume" : 0.05 },\
"episodes" : [],\
"youtube" : {"title" : "", \
"description" : '''''',\
"links" : '''
Track: Bliss Of Heaven - SOMM [Audio Library Release]
Music provided by Audio Library Plus
Watch: https://www.youtube.com/watch?v=JQ6mKeQLZak&t=0s
Free Download / Stream: https://alplus.io/blisss-heaven

Track: Far Far Away - Ferco [Audio Library Release]
Music provided by Audio Library Plus
Watch: https://www.youtube.com/watch?v=SrkQ3K1umlc&t=0s 
Free Download / Stream: https://alplus.io/far-far-away

Track: Ferco - Inquisitiveness
Creative Commons - Attribution 3.0 Unported (CC BY 3.0)
Free Download: https://hypeddit.com/mlsvxq
Streams: https://share.amuse.io/track/ferco-inquisitiveness
Video: https://www.youtube.com/watch?v=dhJdmwLWtFM&t=0s


Track: Inspired - MaikonMusic [Audio Library Release]
Music provided by Audio Library Plus
Watch: https://www.youtube.com/watch?v=RUkdTkk_52o&t=0s
Free Download / Stream: https://alplus.io/inspired

''', \
"tags" : "",\
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

#"isChapter" : False, \

####################### intro ###############################

# this is the hook 
#  scriptedvided.nextTS\(configs\)\, *\"[0-9][0-9]\:[0-9][0-9]\.?[0-9]?[0-9]?\"
#  \"file\" *\: *\".*\"
#  scriptedvided.r6sText\('.*' *\, *[0-9]*\, *[0-9]*\)
#   "timestamps" *\: *\( *"[0-9\:\.]*" *\, *"[0-9\:\.]*" *\)
#configs["episodes"].append(\
#{ "title": "A favorite of miners and gamers alike",\
#"audio" : {"timestamps" : (scriptedvided.nextTS(configs),  "" ), "volume" : 0.999, "padAudio" : 0.05 },\
#"video" : {"file" : ""},\
#})

configs["episodes"].append(\
{ "title": "The upcoming teenager",\
"audio" : {"timestamps" : ("00:00", "00:12.2"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA_H81_S2V_withCPU.mp4"},\
})

configs["episodes"].append(\
{ "title": "The CPU",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:25.3" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Ark_i5_4570.mkv", "start" : "00:03"},\
})

configs["episodes"].append(\
{ "title": "AVX2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:32" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Ark_i5_4570.mkv", "start" : "00:55"},\
})

# broll with the H81 mobo from GA
configs["episodes"].append(\
{ "title": "The test system",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:43" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA_H81_S2V_withCPU.mp4"}\
})

configs["episodes"].append(\
{ "title": "The actual test system",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:00.2" ), "volume" : 0.999, "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Custom build'",\
              "'CPU\: Core i5 3470'",\
              "'RAM\: 16GB DDR3, 1600MHz, dual channel'",\
              "'GPU\: EVGA GTX 970'",\
    ]\
}, \
"video" : {"file" : "GA_H81_S2V_withCooler.mp4"},\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Gigasus for IPC",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:09.1" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Gigasus_ffwd10.mp4"},\
})

####################### end of intro ###############################


####################### gaming section ###############################
configs["episodes"].append(\
{ "title": "Marvel Rivals",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:28.8" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, 30% render scale, low settings", \
    }\
}, \
})

# needs redone
configs["episodes"].append(\
{ "title": "Cyberpunk 2077",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:49" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1024x768, FSR disabled, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Fortnite",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:14.7" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, performance mode", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Rainbow Six: Siege",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:35.8"), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, 50% scale, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Apex Legends",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:01.1" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
},
})

configs["episodes"].append(\
{ "title": "Overwatch 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:26.9" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
}\
})

configs["episodes"].append(\
{ "title": "Counter-Strike 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:52.9" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
}\
})

configs["episodes"].append(\
{ "title": "DOTA 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:18.6" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
},\
"video" : "stock_dota2_1080pLow_scale100.mp4"\
})

configs["episodes"].append(\
{ "title": "Robocop",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:43" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, 50% render scale, low settings", \
    }\
},\
})

configs["episodes"].append(\
{ "title": "The Finals",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:05.4" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
},\
})

#redo and specify a smoother video
configs["episodes"].append(\
{ "title": "Shadow of the Tomb Raider",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:26.3" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "800x600, low settings", \
    }\
},\
"video" : {"file" : "SOTTR_gaming_highest.mp4", "start" : "04:53"}\
})

configs["episodes"].append(\
{ "title": "Borderlands 3",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:42.1" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, 50% render scale, lowest settings", \
    }\
},\
})

configs["episodes"].append(\
{ "title": "Control",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:06.8" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "960x540, lowest settings", \
    }\
},\
})

####################### end of gaming section ###############################


############################ productivity #################################

# this is both time and cycles, for both SMT on and off
configs["episodes"].append(\
{ "title": "Video rendering test (The GigASUS)",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:27.1" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Gigasus_ffwd10.mp4"},\
})

configs["episodes"].append(\
{ "title": "By itself",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:41" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "blurred_dimmed_gigasus.mp4", "start" : "00:30"},\
"isChapter" : False,\
"overlay" : { \
    "image" : {"file" : "overlays_i5_4570.png"}\
}, \
})

configs["episodes"].append(\
{ "title": "Compared with others",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:55.2" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "blurred_dimmed_gigasus.mp4", "start" : "01:00"},\
"isChapter" : False,\
"overlay" : { \
    "image" : {"file" : "ipc_others.png"}\
}, \
})

#############################################################################



####################### conclusion ###############################
# similar ro 4th gen i7
configs["episodes"].append(\
{ "title": "Conclusions",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:10.1" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA_H81_S2V_withCPU.mp4"},\
})

configs["episodes"].append(\
{ "title": "Pricing OLX vs i7",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:28.1" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "olx_4thGen_i5_i7.mkv"},\
})

configs["episodes"].append(\
{ "title": "Z230 footage",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:34.8" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "system_b351_z230.mp4", "start" : "00:00"},\
})

configs["episodes"].append(\
{ "title": "bye",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:41" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA_H81_S2V_withCPU.mp4"},\
})


##configs["episodes"].append(\
##{ "title": "Blooper",\
##"isChapter" : False,\
##"audio" : {"timestamps" : (scriptedvided.nextTS(configs),  "" ) },\
##"video" : {"file" : ""}\
##})

#scriptedvided.makeVideoForEpisode(configs["episodes"][8], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][9], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][13], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][15], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][16], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][17], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][18], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][19], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][21], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][22], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][24], configs)
#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "Borderlands 3"][0], configs)
#scriptedvided.makeVideo(configs)

#for x in range(19,26):
#    scriptedvided.makeVideoForEpisode(configs["episodes"][x], configs)
#
scriptedvided.makeVideo(configs)

