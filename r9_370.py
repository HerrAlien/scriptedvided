import scriptedvided

configs = { "defaultAudioFile" : "R9_370.ogg",\
"mediaFolder" : "F:\\Videos\\R9_370", \
"stockFolder" : "F:\\Videos\\stock",\
"benchmarkFile" : "F:\\Videos\\R9_370\\Benchmark_R9_370.txt",\
"outputFolder" : "F:\\Videos\\R9_370\\output", \
"outputFile" : "R9_370.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "It Plays Arc Raiders?", "until" : "These games will not run"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "These games will not run", "until" : "CS2 both"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "CS2 both", "until" : "Conclusions"}}, \
{"file" : "Inspired - MaikonMusic  Free Background Music  Audio Library Release.mp3", "timestamps" : ("00:00", None ), "destinationTimestamp" : {"title" : "Conclusions", "until" : "Used market has better prices rx 580"}}, \
{"file" : "Inspired - MaikonMusic  Free Background Music  Audio Library Release.mp3", "timestamps" : ("00:00", None ), "destinationTimestamp" : {"title" : "Used market has better prices rx 580", "until" : "EOF"}}, \
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
#  scriptedvided.nextTS\(configs\)\, \"\"
#  \"file\" *\: *\".*\"
#  \"video\" : \{\"file\" : \" \"\}
#  scriptedvided.r6sText\('.*' *\, *[0-9]*\, *[0-9]*\)
#   "timestamps" *\: *\( *"[0-9\:\.]*" *\, *"[0-9\:\.]*" *\)
#configs["episodes"].append(\
#{ "title": "A favorite of miners and gamers alike",\
#"audio" : {"timestamps" : (scriptedvided.nextTS(configs),  "" ), "volume" : 0.999, "padAudio" : 0.05 },\
#"video" : {"file" : " "},\
#})

configs["episodes"].append(\
{ "title": "It Plays Arc Raiders?",\
"audio" : {"timestamps" : ("00:00", "00:14"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : " "},\
})

# GPU-Z
configs["episodes"].append(\
{ "title": "The GPU",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:21.3" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : " "},\
})

configs["episodes"].append(\
{ "title": "cut down version ",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:35.6" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : " "},\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Copmarisons, shaders, frequency",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:53.6" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : " "},\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Copmarisons mem freq",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:06.2" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Cooling and thermals",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:26.1" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "compared with the RX 580 cooler"},\
"overlay" : { \
    "text" : ["'Temperatures (Valley)\: 39C (16C delta over ambient)'"]}, \
})

configs["episodes"].append(\
{ "title": "2 pin fans",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:40" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "temps and weights",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:57.9" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
"isChapter" : False,\
})


configs["episodes"].append(\
{ "title": "The test system",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:20.8" ), "volume" : 0.999, "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Custom PC'",\
              "'CPU\: Ryzen 5 5600'",\
              "'RAM\: 32GB DDR4, 3600MHz, dual channel'",\
    ]\
}, \
"video" : {"file" : " "},\
})

configs["episodes"].append(\
{ "title": "will be compared to the 265",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:30.1" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
"isChapter" : False,\
})



####################### end of intro ###############################


####################### gaming section ###############################
# needs redone

configs["episodes"].append(\
{ "title": "These games will not run",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:38.4" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "Marvel Robocop Legends",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:45.8" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Doom Eternal",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:51.4" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
"isChapter" : False,\
})


configs["episodes"].append(\
{ "title": "ARC Raiders",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:19.5" ), "padAudio" : 0.05 },\
"overlay" : {"benchmark" : {"settings" : "1280x720, lowest settings", } }, \
})

configs["episodes"].append(\
{ "title": "Cyberpunk 2077",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:35.4" ), "padAudio" : 0.05 },\
"overlay" : {"benchmark" : {"settings" : "1280x720, lowest settings", } }, \
})

configs["episodes"].append(\
{ "title": "Cyberpunk 2077 both",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:49.4" ), "padAudio" : 0.05 },\
"overlay" : { "image" : {"file" : ""} }, \
"isChapter" : False,\
})

# single resolution
configs["episodes"].append(\
{ "title": "The Finals",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:06.7" ), "padAudio" : 0.05 },\
"overlay" : {"benchmark" : {"settings" : "1280x720, lowest settings", } }, \
})

configs["episodes"].append(\
{ "title": "Finals both",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:16.3" ), "padAudio" : 0.05 },\
"overlay" : { "image" : {"file" : ""} }, \
"isChapter" : False,\
})

# single resolution
configs["episodes"].append(\
{ "title": "RE4",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:50.3" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Resident Evil 4'",\
              scriptedvided.r6sText('1280x720, performance preset, no FSR'         , 33 , 19),\
              scriptedvided.r6sText('1280x720, performance preset, performance FSR',  42, 22),\
]}, \
})

configs["episodes"].append(\
{ "title": "Fortnite",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:16.4" ), "padAudio" : 0.05 },\
"video" : {"file" : " "}\
"overlay" : { \
    "text" : ["'Fortnite'",\
              scriptedvided.r6sText('1920x1080, legacy performance mode', 85, 61),\
              scriptedvided.r6sText('1600x900, legacy performance mode', 108 , 75),\
              scriptedvided.r6sText('1280x720, legacy performance mode',137, 93),\
]}, \
})

configs["episodes"].append(\
{ "title": "Fortnite both",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:32.3" ), "padAudio" : 0.05 },\
"overlay" : { "image" : {"file" : ""} }, \
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Terminator",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:47.3" ), "padAudio" : 0.05 },\
"overlay" : {"benchmark" : {"settings" : "1920x1080, high settings", } }, \
})

configs["episodes"].append(\
{ "title": "Terminator both",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:57.2" ), "padAudio" : 0.05 },\
"overlay" : { "image" : {"file" : ""} }, \
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Counter-Strike 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:16.6" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Counter-Strike 2'",\
              scriptedvided.r6sText('1920x1080, low settings', 93,63),\
              scriptedvided.r6sText('1600x900, low settings' , 112, 83),\
              scriptedvided.r6sText('1280x720, low settings' ,129,82 ),\
]}, \
})

configs["episodes"].append(\
{ "title": "CS2 both",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:33.6" ), "padAudio" : 0.05 },\
"overlay" : { "image" : {"file" : ""} }, \
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "FC6",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:58.6" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Far Cry 6'",\
              scriptedvided.r6sText('1920x1080, low settings'   , 32, 27),\
              scriptedvided.r6sText('1600x900, medium settings' , 40, 34),\
              scriptedvided.r6sText('1280x720, high settings'   , 43, 37),\
              scriptedvided.r6sText('1280x720, low settings'    , 51,42),\
]}, \
})

configs["episodes"].append(\
{ "title": "FC6 both",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:08.9" ), "padAudio" : 0.05 },\
"overlay" : { "image" : {"file" : ""} }, \
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Rainbow Six: Siege",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:37"), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Rainbow Six\: Siege'",\
              scriptedvided.r6sText('1920x1080, low settings, 100% scale' , 37, 26),\
              scriptedvided.r6sText('1280x720, low settings, 100% scale'  , 66, 40),\
              scriptedvided.r6sText('1920x1080, low settings, 50% scale'  , 53, 35),\
              scriptedvided.r6sText('1280x720, low settings, 50% scale'   , 86, 47),\
]}, \
})

configs["episodes"].append(\
{ "title": "r6s both",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:49" ), "padAudio" : 0.05 },\
"overlay" : { "image" : {"file" : ""} }, \
"isChapter" : False,\
})

# single resolution
configs["episodes"].append(\
{ "title": "Control",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:19.2" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Control'",\
              scriptedvided.r6sText('1920x1080, lowest settings', 37, 25),\
              scriptedvided.r6sText('1280x720, lowest settings' , 60, 36),\
]}, \
})

configs["episodes"].append(\
{ "title": "Control both",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:36.6" ), "padAudio" : 0.05 },\
"overlay" : { "image" : {"file" : ""} }, \
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Overwatch 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "09:01.2" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Overwatch 2'",\
              scriptedvided.r6sText('1920x1080, low settings', 115, 75),\
              scriptedvided.r6sText('1600x900, low settings' , 157,110),\
              scriptedvided.r6sText('1280x720, low settings' , 223, 162),\
]}, \
})

configs["episodes"].append(\
{ "title": "overwatch both",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "09:19" ), "padAudio" : 0.05 },\
"overlay" : { "image" : {"file" : ""} }, \
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Borderlands 3",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "09:45.1" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Borderlands 3'",\
              scriptedvided.r6sText('1920x1080, very low settings', 42, 36),\
              scriptedvided.r6sText('1600x900, low settings'      ,45 , 36),\
              scriptedvided.r6sText('1280x720, medium settings'   , 43, 34),\
]}, \
})

configs["episodes"].append(\
{ "title": "bl3 both",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "10:04" ), "padAudio" : 0.05 },\
"overlay" : { "image" : {"file" : ""} }, \
"isChapter" : False,\
})

# single resolution
configs["episodes"].append(\
{ "title": "DOTA 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "10:23.2" ), "padAudio" : 0.05 },\
"video" : "stock_dota2_1080pLow_scale100.mp4"\
"overlay" : {"benchmark" : {"settings" : "1920x1080, low settings", } }, \
})

#redo and specify a smoother video
configs["episodes"].append(\
{ "title": "Shadow of the Tomb Raider",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "10:44" ), "padAudio" : 0.05 },\
"video" : {"file" : " "}\
"overlay" : { \
    "text" : ["'Shadow of the Tomb Raider'",\
              scriptedvided.r6sText('1920x1080, very low settings', 44, 32),\
              scriptedvided.r6sText('1600x900, low settings'      , 42, 28),\
              scriptedvided.r6sText('1280x720, medium settings'   , 43, 28),\
]}, \
})

configs["episodes"].append(\
{ "title": "sottr both",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "10:53.5" ), "padAudio" : 0.05 },\
"overlay" : { "image" : {"file" : ""} }, \
"isChapter" : False,\
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
# repairs, reuse
configs["episodes"].append(\
{ "title": "Conclusions",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "11:08" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : " "},\
})

configs["episodes"].append(\
{ "title": "265 is faster sum all FPS",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "11:24.4" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : " "},\
})

configs["episodes"].append(\
{ "title": "VRAM not properly used, breel with both cards",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "11:41.1" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : " "},\
})

configs["episodes"].append(\
{ "title": "370 can OC",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "11:52.6" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : " "},\
})

configs["episodes"].append(\
{ "title": "FC6 and ARC Raiders love VRAM",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "12:06" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : " "},\
})

configs["episodes"].append(\
{ "title": "Can be a good option for the right price",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "12:13.4" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : " "},\
})

configs["episodes"].append(\
{ "title": "AliExpress pricing",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "12:24" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : " "},\
})

configs["episodes"].append(\
{ "title": "Used market has better prices",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "12:33.9" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : " "},\
})

configs["episodes"].append(\
{ "title": "Used market has better prices rx 580",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "12:39.2" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : " "},\
})

configs["episodes"].append(\
{ "title": "Who is this GPU for",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "12.51.7" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : " "},\
})

configs["episodes"].append(\
{ "title": "breel next GPU",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "13:02" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : " "},\
})

configs["episodes"].append(\
{ "title": "bye",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "13:16" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : " "},\
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

