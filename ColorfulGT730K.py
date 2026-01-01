import scriptedvided

configs = { "defaultAudioFile" : "Colorful_GT730_Kepler_DDR3.ogg",\
"mediaFolder" : "F:\\Videos\\Colorful_GT730K_DDR3", \
"stockFolder" : "F:\\Videos\\stock",\
"benchmarkFile" : "F:\\Videos\\Colorful_GT730K_DDR3\\Benchmark_GT730_KeplerDDR3.txt",\
"outputFolder" : "F:\\Videos\\Colorful_GT730K_DDR3\\output", \
"outputFile" : "GT730_KeplerDDR3.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#00800080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "Potehto, potahto", "until" : "Cyberpunk 2077"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Cyberpunk 2077", "until" : "Conclusions"}}, \
{"file" : "Inspired - MaikonMusic  Free Background Music  Audio Library Release.mp3", "timestamps" : ("00:00", None ), "destinationTimestamp" : {"title" : "Conclusions", "until" : "EOF"}}, \
], "volume" : 0.038 },\
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
#  \"video\" *: *\{\"file\" *: *\".* \"\}
#  scriptedvided.r6sText\('.*' *\, *[0-9]*\, *[0-9]*\)
#   "timestamps" *\: *\( *"[0-9\:\.]*" *\, *"[0-9\:\.]*" *\)
#configs["episodes"].append(\
#{ "title": "A favorite of miners and gamers alike",\
#"audio" : {"timestamps" : (scriptedvided.nextTS(configs),  "" ), "volume" : 0.999, "padAudio" : 0.05 },\
#"video" : {"file" : " "},\
#})

configs["episodes"].append(\
{ "title": "Potehto, potahto",\
"audio" : {"timestamps" : ("00:00", "00:17"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_ColorfulGt730K_alone2_barred.mp4"},\
})

# GPU-Z
configs["episodes"].append(\
{ "title": "The GPU",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:32" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Colorful_GT730_GPUZ.mkv"},\
})

configs["episodes"].append(\
{ "title": "Copmarisons Fermi",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:49.1" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_FermiGT730_outside.mp4"},\
"overlay" : { \
    "image" : {"file" : "Family_overlay_Fermi.png"}\
}, \
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Copmarisons Kepler GDDR5",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:09.1" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Zotac_GT730_GDDR5.mkv", "start" : "00:30"},\
"overlay" : { \
    "image" : {"file" : "Family_overlay_Fermi_Kepler_GDDR5.png"}\
}, \
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Copmarisons Kepler DDR3",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:22.9" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_ColorfulGt730K_lookingAround_barred.mp4"},\
"overlay" : { \
    "image" : {"file" : "Family_overlay_all.png"}\
}, \
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Cooling and thermals",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:41.5" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_ColorfulGt730K_cooling2_barred.mp4"},\
"overlay" : { \
    "text" : ["'Temperatures (Valley)\: 39C (16C delta over ambient)'"]}, \
})

configs["episodes"].append(\
{ "title": "The test system",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:56.2" ), "volume" : 0.999, "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Custom PC'",\
              "'CPU\: Ryzen 5 5600'",\
              "'RAM\: 32GB DDR4, 3600MHz, dual channel'",\
    ]\
}, \
"video" : {"file" : "test_system_noGPU-converted.mp4"},\
})

####################### end of intro ###############################


####################### gaming section ###############################
# needs redone
configs["episodes"].append(\
{ "title": "Cyberpunk 2077",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:18" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, lowest settings", \
    }\
}, \
})

# single resolution
configs["episodes"].append(\
{ "title": "The Finals",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:30.7" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, lowest settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Overwatch 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:46.6" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : "Overwatch 2, 1280x720, low settings.png"}\
}, \
})

configs["episodes"].append(\
{ "title": "Fortnite",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:10.9" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : "Fortnite, 1280x720, 67% render scale, performance mode.png"}\
}, \
"video" : {"file" : "FortniteClient-Win64-Shipping_2025_12_13_22_22_36_353.mkv"}\
})

configs["episodes"].append(\
{ "title": "Terminator",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:26.1" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : "Terminator, 1024x768, low settings.png"}\
}, \
})

configs["episodes"].append(\
{ "title": "Counter-Strike 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:51.4" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : "Counter-Strike 2, 1024x768, balanced FSR, low settings.png"}\
}, \
})

configs["episodes"].append(\
{ "title": "Doom Eternal",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:07.4" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Rainbow Six: Siege",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:22.3"), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, lowest settings", \
    }\
}, \
})

# single resolution
configs["episodes"].append(\
{ "title": "Control",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:39.6" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : "Control, 1280x720, lowest settings.png"}\
}, \
})

# single resolution
configs["episodes"].append(\
{ "title": "DOTA 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:57.4" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : "DOTA2, 1920x1080, low settings.png"}\
}, \
"video" : "stock_dota2_1080pLow_scale100.mp4"\
})


#redo and specify a smoother video
configs["episodes"].append(\
{ "title": "Shadow of the Tomb Raider",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:16.1" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : "Shadow of the Tomb Raider, 1280x720, 50% scale, lowest settings.png"}\
}, \
"video" : {"file" : "SOTTR_gaming_highest.mp4", "start" : "04:53"}\
})

#configs["episodes"].append(\
#{ "title": "Borderlands 3",\
#"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "padAudio" : 0.05 },\
#"overlay" : { \
#    "image" : {"file" : "Borderlands 3, 1280x720, 50% render scale, very low settings.png"}\
#}, \
#})

####################### end of gaming section ###############################


####################### conclusion ###############################
# sum of all fps
configs["episodes"].append(\
{ "title": "Conclusions",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:32.7" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_ColorfulGt730K_alone_barred.mp4"},\
})

configs["episodes"].append(\
{ "title": "GTAV",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:47.2"), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, lowest settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Warframe",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:03"), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, lowest settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Not for gaming",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:13.5" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_ColorfulGt730K_alone2_barred.mp4"},\
})

configs["episodes"].append(\
{ "title": "OLX pricing",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:22.9" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GT730_OLX_2026.mkv"},\
})

configs["episodes"].append(\
{ "title": "bye",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:31.3" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_ColorfulGt730K_lookingAround_barred.mp4"},\
})


##configs["episodes"].append(\
##{ "title": "Blooper",\
##"isChapter" : False,\
##"audio" : {"timestamps" : (scriptedvided.nextTS(configs),  "" ) },\
##"video" : {"file" : " "}\
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

