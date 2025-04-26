import scriptedvided

configs = { "defaultAudioFile" : "GTX970_2025.ogg",\
"mediaFolder" : "F:\\Videos\\GTX970_2025", \
"stockFolder" : "F:\\Videos\\stock",\
"benchmarkFile" : "F:\\Videos\\GTX970_2025\\Benchmark_GTX970_2025.txt",\
"outputFolder" : "F:\\Videos\\GTX970_2025\\output", \
"outputFile" : "GTX970_2025.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#00800080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "Heart 4 Maxwell", "until" : "Marvel Rivals"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Marvel Rivals", "until" : "Rainbow Six: Siege"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Rainbow Six: Siege", "until" : "Conclusions"}}, \
{"file" : "Inspired - MaikonMusic  Free Background Music  Audio Library Release.mp3", "timestamps" : ("00:00", None ), "destinationTimestamp" : {"title" : "Conclusions", "until" : "EOF"}}, \
], "volume" : 0.05 },\
"episodes" : [],\
"youtube" : {"title" : "GTX 970: a 10 years old GPU tested today", \
"description" : '''The GTX 970 gets another close look, this time using the Ryzen 5 3600 based test system, and a few extra games.''',\
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
"tags" : "Maxwell,GTX 970,GeForce,NVidia,GTX970",\
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
"video" : {"file" : "breel_autumn_GTX970.mp4"},\
})

configs["episodes"].append(\
{ "title": "The GPU",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:34.1" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GTX970_GPUZ_Valley.mkv"},\
})

configs["episodes"].append(\
{ "title": "The lawsuit",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:48.6" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GTX970_lawsuit.mkv"},\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Cooling and thermals",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:04.1" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GTX970_cooling.mp4", "start" : "00:00"},\
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
              scriptedvided.r6sText('1920x1080, low settings', 54 , 46),\
              scriptedvided.r6sText('1280x720, low settings', 89 , 69),\
]}, \
})

configs["episodes"].append(\
{ "title": "Cyberpunk 2077",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:15.1" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Cyberpunk 2077'",\
              scriptedvided.r6sText('1920x1080, lowest settings', 42 , 29),\
              scriptedvided.r6sText('1600x900, lowest settings', 53 , 36),\
              scriptedvided.r6sText('1280x720, lowest settings', 68 , 45),\
]}, \
})

configs["episodes"].append(\
{ "title": "The Finals",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:35.4" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'The Finals'",\
              scriptedvided.r6sText('1920x1080, low settings', 62 , 47 ), \
              scriptedvided.r6sText('1600x900, low settings', 88 , 70), \
              scriptedvided.r6sText('1280x720, low settings',  105, 73), \
]}, \
})

configs["episodes"].append(\
{ "title": "Robocop",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:02.8" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Robocop'",\
              scriptedvided.r6sText('1920x1080, low settings', 30, 22)\
              scriptedvided.r6sText('1600x900, low settings',39 , 32)\
              scriptedvided.r6sText('1600x900, medium settings', 34, 25 )\
              scriptedvided.r6sText('1280x720, high settings', 45,33 )\
]}, \
})

configs["episodes"].append(\
{ "title": "Fortnite",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:19.3" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Fortnite'",\
              scriptedvided.r6sText('1920x1080, performance mode', 215, 119)\
              scriptedvided.r6sText('1600x900, performance mode', 236, 125 )\
              scriptedvided.r6sText('1280x720, performance mode', 233, 123)\
]}, \
"video" : "Fortnite_2025_04_03_win.mp4"\
})

configs["episodes"].append(\
{ "title": "Fortnite Reload results",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:35.1" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Fortnite Reload'",\
              scriptedvided.r6sText('1920x1080, performance mode', 268, 146)\
              scriptedvided.r6sText('1600x900, performance mode', 267, 154)\
              scriptedvided.r6sText('1280x720, performance mode', 265 , 157)\
]}, \
"video" : "Fortnite_Reload_2024_11_01.mp4",\
})

configs["episodes"].append(\
{ "title": "Terminator: Resistance",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:52" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Terminator\: Resistance'",\
              scriptedvided.r6sText('2560x1440, epic settings', 87 , 61),\
]}, \
})

configs["episodes"].append(\
{ "title": "Counter-Strike 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:11" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Counter-Strike 2'",\
              scriptedvided.r6sText('1920x1080, low settings', 212 , 88),\
              scriptedvided.r6sText('1600x900, low settings', 204 , 94),\
              scriptedvided.r6sText('1280x720, low settings', 219 , 97),\
]}, \
})

configs["episodes"].append(\
{ "title": "Far Cry 6",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:29" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Far Cry 6'",\
              scriptedvided.r6sText('2560x1440, ultra settings', 30 , 26),\
              scriptedvided.r6sText('2560x1440, high settings', 37 ,31),\
              scriptedvided.r6sText('1920x1080, ultra settings', 43 , 35),\
]}, \
})

configs["episodes"].append(\
{ "title": "Apex Legends",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:50" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Apex Legends'",\
              scriptedvided.r6sText('1920x1080, low settings', 156 , 112), \
              scriptedvided.r6sText('1600x900, low settings',  198 , 134 ), \
              scriptedvided.r6sText('1280x720, low settings',  242 , 166), \
]}, \
"video" : "" \
})

configs["episodes"].append(\
{ "title": "Doom Eternal",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:13.6" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Doom Eternal'",\
              scriptedvided.r6sText('1920x1080, low settings', 99, 70)\
              scriptedvided.r6sText('1920x1080, medium settings', 86, 58)\
              scriptedvided.r6sText('1600x900, high settings', 96, 68)\
]}, \
})

configs["episodes"].append(\
{ "title": "Rainbow Six: Siege",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:51.3" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Rainbow Six\: Siege'",\
              scriptedvided.r6sText('1920x1080, low settings, 100% scale', 123 , 97),\
              scriptedvided.r6sText('1280x720, low settings, 100% scale',  209, 161),\
              scriptedvided.r6sText('1920x1080, low settings, 50% scale', 176 , 137),\
              scriptedvided.r6sText('1280x720, low settings, 50% scale', 190 , 147),\
]}, \
})

configs["episodes"].append(\
{ "title": "Control",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:09.5" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Control'",\
              scriptedvided.r6sText('1920x1080, high settings', 31 , 26),\
              scriptedvided.r6sText('1920x1080, medium settings', 43 , 35),\
]}, \
})

configs["episodes"].append(\
{ "title": "Overwatch 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:37.1" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Overwatch 2'",\
              scriptedvided.r6sText('1920x1080, low settings', 276, 230), \
              scriptedvided.r6sText('1600x900, low settings',  366,  311), \
              scriptedvided.r6sText('1280x720, low settings',  493, 361 ), \
]}, \
})

configs["episodes"].append(\
{ "title": "Resident Evil 4 (Remake)", \
"video" : "stock_re4demo_phoneCall.mp4", \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:07.5" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Resident Evil 4 (Remake)'",\
              scriptedvided.r6sText('1920x1080, balanced profile', 37 , 28),\
              scriptedvided.r6sText('1600x900, balanced profile', 50 , 31),\
              scriptedvided.r6sText('1920x1080, performance profile, no FSR', 57 , 40),\
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
              scriptedvided.r6sText('2560x1440, highest settings', 34 , 25),\
              scriptedvided.r6sText('2560x1440, high settings', 38 , 28),\
              scriptedvided.r6sText('2560x1440, medium settings', 40 , 29),\
              scriptedvided.r6sText('1920x1080, highest settings', 52 , 31),\
]}, \
"video" : {"file" : ""}\
})

configs["episodes"].append(\
{ "title": "Borderlands 3",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:01" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Borderlands 3'",\
              scriptedvided.r6sText('1920x1080, badass settings', 35 , 29),\
              scriptedvided.r6sText('1920x1080, ultra settings', 37 , 31),\
]}, \
})

####################### end of gaming section ###############################

####################### conclusion ###############################
#
configs["episodes"].append(\
{ "title": "Conclusions",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:21" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_autumn_GTX970.mp4"},\
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
"video" : {"file" : "breel_R9_290_RX570_GTX970_attic.mp4"},\
})

configs["episodes"].append(\
{ "title": "olx pricing",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "09:00.5" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GTX970_olx.mkv"},\
})

configs["episodes"].append(\
{ "title": "bye",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "09:07.2" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_autumn_GTX970.mp4"},\
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