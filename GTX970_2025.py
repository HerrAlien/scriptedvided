import scriptedvided

configs = { "defaultAudioFile" : "RX570_2025.ogg",\
"mediaFolder" : "F:\\Videos\\RX570_2025", \
"stockFolder" : "F:\\Videos\\stock",\
"benchmarkFile" : "F:\\Videos\\RX570_2025\\Benchmark_RX570_2025.txt",\
"outputFolder" : "F:\\Videos\\RX570_2025\\output", \
"outputFile" : "RX570_2025.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "The card to test", "until" : "Marvel Rivals"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Marvel Rivals", "until" : "Robocop"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Robocop", "until" : "Conclusions"}}, \
{"file" : "Inspired - MaikonMusic  Free Background Music  Audio Library Release.mp3", "timestamps" : ("00:00", None ), "destinationTimestamp" : {"title" : "Conclusions", "until" : "EOF"}}, \
], "volume" : 0.05 },\
"episodes" : [],\
"youtube" : {"title" : "", \
"description" : ''' GPU Hook 
We're using the same Z230 workstation with an i7 4770 equivalent CPU and 32 GB of DDR3 running in dual channel at 1600MHz.''',\
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
#configs["episodes"].append(\
#{ "title": "A favorite of miners and gamers alike",\
#"audio" : {"timestamps" : ("09:37.3", "09:46" ), "volume" : 0.999, "padAudio" : 0.05 },\
#"video" : {"file" : "rx580_ethereumDust.mp4", "start" : "00:00"},\
#})

configs["episodes"].append(\
{ "title": "Heart 4 Maxwell",\
"audio" : {"timestamps" : ("00:00", "00:13.2" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "The GPU",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:34.1" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "", "start" : "00:00"},\
})

configs["episodes"].append(\
{ "title": "The lawsuit",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:48.6" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "", "start" : "00:00"},\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Cooling and thermals",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:04.1" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "", "start" : "00:00"},\
})

configs["episodes"].append(\
{ "title": "The test system",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:19" ), "volume" : 0.999, "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Custom build'",\
              "'CPU\: Ryzen 5 3600'",\
              "'RAM\: 32GB DDR4 at 3000 MHz, dual channel'",\
    ]\
}, \
"video" : {"file" : "test_system_noGPU.mp4" }\
})

####################### end of intro ###############################


####################### gaming section ###############################
configs["episodes"].append(\
{ "title": "Marvel Rivals",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:45.3" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Marvel Rivals'",\
              scriptedvided.r6sText('',  , ),\
              scriptedvided.r6sText('',  , ),\
              scriptedvided.r6sText('',  , ),\
              scriptedvided.r6sText('',  , ),\
]}, \
})

configs["episodes"].append(\
{ "title": "Cyberpunk 2077",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:15.1" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Marvel Rivals'",\
              scriptedvided.r6sText('',  , ),\
              scriptedvided.r6sText('',  , ),\
              scriptedvided.r6sText('',  , ),\
              scriptedvided.r6sText('',  , ),\
]}, \
})

configs["episodes"].append(\
{ "title": "The Finals",\
"video" : "Discovery_2025_03_15_22_55_07_819.mp4",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:35.4" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'The Finals'",\
              scriptedvided.r6sText('',  , ), \
              scriptedvided.r6sText('',  , ), \
              scriptedvided.r6sText('',  , ), \
]}, \
})

configs["episodes"].append(\
{ "title": "Robocop",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:02.8" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Robocop'",\
              scriptedvided.r6sText('', , )\
              scriptedvided.r6sText('', , )\
              scriptedvided.r6sText('', , )\
]}, \
})

configs["episodes"].append(\
{ "title": "Fortnite",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:19.3" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Fortnite'",\
              scriptedvided.r6sText('', , )\
              scriptedvided.r6sText('', , )\
              scriptedvided.r6sText('', , )\
]}, \
"video" : ""\
})

configs["episodes"].append(\
{ "title": "Fortnite Reload results",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:35.1" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Fortnite Reload'",\
              scriptedvided.r6sText('', , )\
              scriptedvided.r6sText('', , )\
              scriptedvided.r6sText('', , )\
]}, \
"video" : "",\
})

configs["episodes"].append(\
{ "title": "Terminator: Resistance",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:52" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Terminator\: Resistance'",\
              scriptedvided.r6sText('',  , ),\
              scriptedvided.r6sText('',  , ),\
]}, \
})

configs["episodes"].append(\
{ "title": "Counter-Strike 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:11" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Counter-Strike 2'",\
              scriptedvided.r6sText('',  , ),\
              scriptedvided.r6sText('',  , ),\
              scriptedvided.r6sText('',  , ),\
]}, \
})

configs["episodes"].append(\
{ "title": "Far Cry 6",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:29" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Far Cry 6'",\
              scriptedvided.r6sText('',  , ),\
              scriptedvided.r6sText('',  , ),\
              scriptedvided.r6sText('',  , ),\
]}, \
})

configs["episodes"].append(\
{ "title": "Apex Legends",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:50" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Apex Legends'",\
              scriptedvided.r6sText('',  , ), \
              scriptedvided.r6sText('',  , ), \
              scriptedvided.r6sText('',  , ), \
]}, \
"video" : "" \
})

configs["episodes"].append(\
{ "title": "Doom Eternal",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:13.6" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Doom Eternal'",\
              scriptedvided.r6sText('', , )\
              scriptedvided.r6sText('', , )\
              scriptedvided.r6sText('', , )\
]}, \
})

configs["episodes"].append(\
{ "title": "Rainbow Six: Siege",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:51.3" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Rainbow Six\: Siege'",\
              scriptedvided.r6sText('',  , ),\
              scriptedvided.r6sText('',  , ),\
              scriptedvided.r6sText('',  , ),\
              scriptedvided.r6sText('',  , ),\
]}, \
})

configs["episodes"].append(\
{ "title": "Control",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:09.5" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Control'",\
              scriptedvided.r6sText('',  , ),\
              scriptedvided.r6sText('',  , ),\
]}, \
})

configs["episodes"].append(\
{ "title": "Overwatch 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:37.1" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Overwatch 2'",\
              scriptedvided.r6sText('', , )\
              scriptedvided.r6sText('', , )\
              scriptedvided.r6sText('', , )\
]}, \
})

configs["episodes"].append(\
{ "title": "Resident Evil 4 (Remake)", \
"video" : "stock_re4demo_phoneCall.mp4", \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:07.5" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Resident Evil 4 (Remake)'",\
              scriptedvided.r6sText('',  , ),\
              scriptedvided.r6sText('',  , ),\
              scriptedvided.r6sText('',  , ),\
]}, \
})

configs["episodes"].append(\
{ "title": "DOTA2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:22.6" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Shadow of the Tomb Raider",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:45.1" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Shadow of the Tomb Raider'",\
              scriptedvided.r6sText('',  , ),\
              scriptedvided.r6sText('',  , ),\
              scriptedvided.r6sText('',  , ),\
]}, \
"video" : {"file" : ""}\
})

configs["episodes"].append(\
{ "title": "Borderlands 3",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:01" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Borderlands 3'",\
              scriptedvided.r6sText('',  , ), \
              scriptedvided.r6sText('',  , ), \
              scriptedvided.r6sText('',  , ), \
]}, \
})

####################### end of gaming section ###############################

####################### conclusion ###############################
#
configs["episodes"].append(\
{ "title": "Conclusions",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:21" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "VRAM not much of an issue",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:31.7" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "with r9 290 and rx 570",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:45.1" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "olx pricing",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "09:00.5" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "bye",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "09:07.2" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})


##configs["episodes"].append(\
##{ "title": "Blooper",\
##"isChapter" : False,\
##"audio" : {"timestamps" : ( "13:40.5", "14:04.2") },\
##"video" : {"file":"HiRezTrio-P_aladins_R_ealmRoyale_R_ogueCompany.mp4"}\
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