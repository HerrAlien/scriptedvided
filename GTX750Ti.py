import scriptedvided

configs = { "defaultAudioFile" : "GTX750Ti.ogg",\
"mediaFolder" : "F:\\Videos\\GTX750Ti", \
"stockFolder" : "F:\\Videos\\stock",\
"benchmarkFile" : "F:\\Videos\\GTX750Ti\\Benchmark_GTX750Ti.txt",\
"outputFolder" : "F:\\Videos\\GTX750Ti\\output", \
"outputFile" : "GTX750Ti.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#00800080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "A cheap 50 Ti card", "until" : "Games that went NOPE"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Games that went NOPE", "until" : "Control"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Control", "until" : "Conclusions"}}, \
{"file" : "Inspired - MaikonMusic  Free Background Music  Audio Library Release.mp3", "timestamps" : ("00:00", None ), "destinationTimestamp" : {"title" : "Conclusions", "until" : "EOF"}}, \
], "volume" : 0.05 },\
"episodes" : [],\
"youtube" : {"title" : "", \
"description" : '''In this one we see what abandoning DX11 by game devs in 2025 did to the GTX 750 Ti. Or how the baked in obsolescence by NVidia doomed an otherwise ok card. Or both.''',\
"links" : '''
Track: Bliss Of Heaven - SOMM [Audio Library Release]
Music provided by Audio Library Plus
Watch: https://www.youtube.com/watch?v=JQ6mKeQLZak&t=0s
Free Download / Stream: https://alplus.io/blisss-heaven

Track: Far Far Away - Ferco [Audio Library Release]
Music provided by Audio Library Plus
Watch: https://www.youtube.com/watch?v=SrkQ3K1umlc&t=0s 
Free Download / Stream: https://alplus.io/far-far-away

Track: Inspired - MaikonMusic [Audio Library Release]
Music provided by Audio Library Plus
Watch: https://www.youtube.com/watch?v=RUkdTkk_52o&t=0s
Free Download / Stream: https://alplus.io/inspired

''', \
"tags" : "Maxwell,GTX 750 Ti,GeForce,NVidia,GTX750Ti",\
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
#"video" : {"file" : " "},\
# \"video\" *: *\{\"file\" *: *\".*\"\}
#})

configs["episodes"].append(\
{ "title": "A cheap 50 Ti card",\
"audio" : {"timestamps" : ("00:00", "00:19.3" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "bared_GTX750Ti.mp4"},\
})

configs["episodes"].append(\
{ "title": "The GPU",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:35.4" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GTX750Ti_GpuZ_Valley.mkv"},\
})

configs["episodes"].append(\
{ "title": "The GPU - power efficient",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:48" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "bared_GTX750Ti_moving.mp4"},\
})

configs["episodes"].append(\
{ "title": "TDP",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:01" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GTX750Ti_Techpowerup.mkv", "start" : "00:10"},\
})

configs["episodes"].append(\
{ "title": "Cooling and thermals",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:18.6" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GTX750Ti_cooling.mp4"},\
"overlay" : { \
    "text" : ["'Temperatures (Heaven)\: 64C (39C delta over ambient)'"]}, \
})

configs["episodes"].append(\
{ "title": "The test system",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:35.6" ), "volume" : 0.999, "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Custom build'",\
              "'CPU\: Ryzen 5 3600'",\
              "'RAM\: 32GB DDR4 at 3000 MHz, dual channel'",\
    ]\
}, \
"video" : {"file" : "system_b351_z230.mp4", "start" : "00:15" }\
})

####################### end of intro ###############################


####################### gaming section ###############################

configs["episodes"].append(\
{ "title": "Games that went NOPE",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:50.8" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "r5apex_bot_royale.mp4"},\
})

configs["episodes"].append(\
{ "title": "Cyberpunk 2077",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:12" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Cyberpunk 2077'",\
              scriptedvided.r6sText('1280x720, low settings' , 34, 23),\
              scriptedvided.r6sText('1280x720, low settings, FSR disabled' , 27, 18),\
]}, \
})

configs["episodes"].append(\
{ "title": "The Finals",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:33.7" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'The Finals'",\
              scriptedvided.r6sText('1280x720, low settings, tutorial' , 54, 36), \
              scriptedvided.r6sText('1280x720, low settings, match' , 52, 40), \
]}, \
"video" : "Discovery_2025_03_15_22_55_07_819.mp4"\
})

configs["episodes"].append(\
{ "title": "Fortnite",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:57.5" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Fortnite'",\
              scriptedvided.r6sText('1920x1080, performance mode' , 106, 69),\
              scriptedvided.r6sText('1600x900, performance mode' , 139, 95),\
              scriptedvided.r6sText('1280x720, performance mode' , 186, 107),\
]}, \
})

configs["episodes"].append(\
{ "title": "Terminator: Resistance",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:27.5" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Terminator\: Resistance'",\
              scriptedvided.r6sText('1920x1080, low settings' , 70, 53),\
              scriptedvided.r6sText('1920x1080, medium settings' , 54, 41),\
              scriptedvided.r6sText('1920x1080, high settings' , 42, 28),\
]}, \
})

configs["episodes"].append(\
{ "title": "Counter-Strike 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:47.8" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Counter-Strike 2'",\
              scriptedvided.r6sText('1920x1080, low settings' , 115, 84),\
              scriptedvided.r6sText('1600x900, low settings' , 122, 80),\
              scriptedvided.r6sText('1280x720, low settings' , 139, 95),\
]}, \
})

configs["episodes"].append(\
{ "title": "Far Cry 6",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:14.2" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Far Cry 6'",\
              scriptedvided.r6sText('1600x900, lowest settings' , 33, 29),\
              scriptedvided.r6sText('1280x720, lowest settings' , 47, 39),\
]}, \
})

configs["episodes"].append(\
{ "title": "Control",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:34.6" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Control'",\
              scriptedvided.r6sText('1280x720, lowest settings' , 53, 38),\
              scriptedvided.r6sText('1280x720, low settings' , 42, 31),\
]}, \
})

configs["episodes"].append(\
{ "title": "Overwatch 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:58.2" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Overwatch 2'",\
              scriptedvided.r6sText('1920x1080, low settings' , 107, 89),\
              scriptedvided.r6sText('1600x900, low settings' , 144, 120),\
              scriptedvided.r6sText('1280x720, low settings' , 212, 180),\
]}, \
})

configs["episodes"].append(\
{ "title": "Resident Evil 4 (Remake)", \
"video" : "stock_re4demo_phoneCall.mp4", \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:28.6" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Resident Evil 4 \(Remake\)'",\
              scriptedvided.r6sText('1280x720, prioritize performance' , 54, 29),\
              scriptedvided.r6sText('1280x720, prioritize performance, no FSR' , 35, 21),\
]}, \
})

configs["episodes"].append(\
{ "title": "DOTA2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:45.5" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Shadow of the Tomb Raider",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:13.5" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Shadow of the Tomb Raider'",\
              scriptedvided.r6sText('1920x1080, lowest settings' , 39, 29),\
              scriptedvided.r6sText('1600x900, low settings' , 38, 27),\
              scriptedvided.r6sText('1600x900, lowest settings' , 49, 35),\
              scriptedvided.r6sText('1280x720, medium settings' ,40 , 27),\
              scriptedvided.r6sText('1280x720, low settings' , 48, 32),\
]}, \
"video" : {"file" : "SOTTR_gaming_highest.mp4", "start" : "04:53"}\
})

configs["episodes"].append(\
{ "title": "Borderlands 3",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:31.3" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Borderlands 3'",\
              scriptedvided.r6sText('1920x1080, very low settings' , 40, 33),\
              scriptedvided.r6sText('1600x900, low settings' , 42, 34),\
              scriptedvided.r6sText('1280x720, low settings' , 43, 34),\
]}, \
})

####################### end of gaming section ###############################

####################### conclusion ###############################
#
configs["episodes"].append(\
{ "title": "Conclusions",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:44.5" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GTX750Ti_Techpowerup.mkv", "start" : "01:00"},\
})

configs["episodes"].append(\
{ "title": "Leads to games not playing",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:59.8" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "bared_GTX750Ti_moving.mp4"},\
})

configs["episodes"].append(\
{ "title": "The blame game - NVidia",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:09" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "nvidia_Pascal.mkv", "start" : "00:00"},\
})

configs["episodes"].append(\
{ "title": "The blame game - Game devs",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:18.6" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "hd_6800_EA.mp4", "start" : "00:00"},\
})

configs["episodes"].append(\
{ "title": "The blame game 2 - NVidia",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:28.3" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "jensen_oven.mkv"},\
})

configs["episodes"].append(\
{ "title": "Pricing",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:47.2" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GTX750Ti_OLX.mkv"},\
})

configs["episodes"].append(\
{ "title": "RGHD",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:55.7" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GTX750Ti_RGHD.mkv"},\
})

configs["episodes"].append(\
{ "title": "bye",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:03" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "bared_GTX750Ti.mp4"},\
})


##configs["episodes"].append(\
##{ "title": "Blooper",\
##"isChapter" : False,\
##"audio" : {"timestamps" : ( "13:40.5", "14:04.2") },\
##"video" : {"file" : " "}\
##})

#scriptedvided.makeVideoForEpisode(configs["episodes"][2], configs)
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

#for x in range(2,28):
#    scriptedvided.makeVideoForEpisode(configs["episodes"][x], configs)

scriptedvided.makeVideo(configs)