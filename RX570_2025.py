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
{ "title": "The card to test",\
"audio" : {"timestamps" : ("00:00", "00:07.5" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_autumn_RX570.mp4"},\
})

configs["episodes"].append(\
{ "title": "The test system",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:17.3" ), "volume" : 0.999, "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Custom build'",\
              "'CPU\: Ryzen 5 3600'",\
              "'RAM\: 32GB DDR4 at 3000 MHz, dual channel'",\
    ]\
}, \
"video" : {"file" : "test_system_noGPU.mp4" }\
})


configs["episodes"].append(\
{ "title": "The GPU",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:34.9" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "RX570_GPUZ_Heaven.mp4"},\
})

configs["episodes"].append(\
{ "title": "Cooling and thermals",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:45.4" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "rx570_itx_cooling.mp4"},\
"overlay" : { \
    "text" : ["'Heaven Benchmark, looping'",\
              "'Max. temp\: 67C, delta over ambient\: 45C'",\
    ]\
}, \
})


configs["episodes"].append(\
{ "title": "Methodology - some game footage",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:57" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Marvel-Win64-Shipping_2025_03_15_07_57_44_978-converted.mp4", "start" : "00:01"},\
})

####################### end of intro ###############################




####################### gaming section ###############################
configs["episodes"].append(\
{ "title": "Marvel Rivals",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:22.7" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Marvel Rivals'",\
              scriptedvided.r6sText('1920x1080, low settings, training', 55, 44),\
              scriptedvided.r6sText('1280x720, low settings, training' , 84, 59),\
              scriptedvided.r6sText('1920x1080, low settings, in game' , 69, 48),\
              scriptedvided.r6sText('1280x720, low settings, in game'  , 101, 73),\
]}, \
"video" : {"file" : "Marvel-Win64-Shipping_2025_03_15_07_57_44_978-converted.mp4", "start" : "00:13"},\
})
})

configs["episodes"].append(\
{ "title": "The Finals",\
"video" : "Discovery_2025_03_15_22_55_07_819.mp4",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:39.8" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'The Finals'",\
              scriptedvided.r6sText('1920x1080, low settings', 76, 58), \
              scriptedvided.r6sText('1600x900, low settings' , 95, 71), \
              scriptedvided.r6sText('1280x720, low settings' , 103, 72), \
]}, \
})

configs["episodes"].append(\
{ "title": "Apex Legends",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:57.6" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Apex Legends'",\
              scriptedvided.r6sText('1920x1080, low settings', 144, 106), \
              scriptedvided.r6sText('1600x900, low settings' , 176, 126), \
              scriptedvided.r6sText('1280x720, low settings' , 211, 149), \
]}, \
"video" : "rx580_r5apex_2024_07_26_22_34_08_382-converted.mp4" \
})

configs["episodes"].append(\
{ "title": "Counter-Strike 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:21.5" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Counter-Strike 2'",\
              scriptedvided.r6sText('1920x1080, low settings', 189, 140),\
              scriptedvided.r6sText('1600x900, low settings' ,217 , 121),\
              scriptedvided.r6sText('1280x720, low settings' , 232, 103),\
]}, \
})

configs["episodes"].append(\
{ "title": "DOTA2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:34.3" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})


configs["episodes"].append(\
{ "title": "Fortnite",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:54.8" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Fortnite'",\
              scriptedvided.r6sText('1920x1080, performance mode', 232,138 ),\
              scriptedvided.r6sText('1600x900, performance mode',  240,145 ),\
              scriptedvided.r6sText('1280x720, performance mode' ,238 , 139),\
]}, \
"video" : "FortniteClient-Win64-Shipping_2025_03_15_06_53_56_749-converted.mp4"\
})

configs["episodes"].append(\
{ "title": "Fortnite Reload results",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:09.8" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Fortnite Reload'",\
              scriptedvided.r6sText('1920x1080, performance mode',247 ,138 ),\
              scriptedvided.r6sText('1600x900, performance mode', 244 , 136),\
              scriptedvided.r6sText('1280x720, performance mode' , 247, 140),\
]}, \
"video" : "FortniteClient-Win64-Shipping_2025_03_15_07_03_21_337-converted.mp4",\
})

configs["episodes"].append(\
{ "title": "Overwatch 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:26.5" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Overwatch 2'",\
              scriptedvided.r6sText('1920x1080, low settings', 259,219 ),\
              scriptedvided.r6sText('1600x900, low settings' , 341, 293),\
              scriptedvided.r6sText('1280x720, low settings' ,488 ,425 ),\
]}, \
})


configs["episodes"].append(\
{ "title": "XDefiant",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:45.8" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'XDefiant'",\
              scriptedvided.r6sText('1920x1080, low settings', 180, 130),\
              scriptedvided.r6sText('1600x900, low settings' ,232 ,155),\
              scriptedvided.r6sText('1280x720, low settings' , 292, 188),\
]}, \
})

configs["episodes"].append(\
{ "title": "Rainbow Six: Siege",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:01.6" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Rainbow Six\: Siege'",\
              scriptedvided.r6sText('1920x1080, low settings, 100% render scale', 149, 121),\
              scriptedvided.r6sText('1280x720, low settings, 100% render scale',  239, 183),\
              scriptedvided.r6sText('1920x1080, low settings, 50% render scale',  200, 159),\
              scriptedvided.r6sText('1280x720, low settings, 50% render scale',   288, 216),\
]}, \
})

# needs support for aliases!!
configs["episodes"].append(\
{ "title": "Robocop",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:35.5" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Robocop'",\
              scriptedvided.r6sText('1920x1080, medium settings',39, 33),\
              scriptedvided.r6sText('1920x1080, high settings',   38,29 ),\
              scriptedvided.r6sText('1600x900, high settings'   , 36, 28),\
]}, \
})


configs["episodes"].append(\
{ "title": "Doom Eternal",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:47.2" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, medium settings", \
    }\
}, \
})


configs["episodes"].append(\
{ "title": "Terminator: Resistance",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:05.3" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Terminator\: Resistance'",\
              scriptedvided.r6sText('1920x1080, epic settings', 46, 34),\
              scriptedvided.r6sText('2560x1440, epic settings', 70, 42),\
]}, \
})

configs["episodes"].append(\
{ "title": "Control",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:25.7" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Control'",\
              scriptedvided.r6sText('1920x1080, medium settings' ,51, 40),\
              scriptedvided.r6sText('1280x720, ultra settings' ,   34 , 28),\
]}, \
})

configs["episodes"].append(\
{ "title": "Borderlands 3",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:58.7" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Borderlands 3'",\
              scriptedvided.r6sText('1920x1080, high settings'  , 45, 28), \
              scriptedvided.r6sText('1600x900, ultra settings'  , 42, 35), \
              scriptedvided.r6sText('1600x900, badass settings' , 39, 32), \
]}, \
})

configs["episodes"].append(\
{ "title": "Resident Evil 4 (Remake)", \
"video" : "stock_re4demo_phoneCall.mp4", \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:22.6" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Resident Evil 4 (Remake)'",\
              scriptedvided.r6sText('1920x1080, performance'         , 93,58 ),\
              scriptedvided.r6sText('1920x1080, performance, FSR off', 68, 48),\
              scriptedvided.r6sText('1920x1080, balanced'            , 46,29 ),\
]}, \
})


configs["episodes"].append(\
{ "title": "Far Cry 6",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:43.2" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, ultra settings", \
    }\
}, \
})


configs["episodes"].append(\
{ "title": "Warframe",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:10.7" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Shadow of the Tomb Raider",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:33.6" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, highest settings", \
    }\
}, \
"video" : {"file" : "rx580_SOTTR_2024_07_27_22_58_17_417-converted.mp4" , "start" : "01:42"}\
})

####################### end of gaming section ###############################

####################### conclusion ###############################
# better than the 280
configs["episodes"].append(\
{ "title": "Conclusions",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:48.7" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_RX570_R9_270_GTX1050Ti_GT1030.MP4"},\
})

configs["episodes"].append(\
{ "title": "R9 270 and RX 570",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:00.7" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_RX570_R9_270.MP4"},\
})

configs["episodes"].append(\
{ "title": "SP",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:09.8" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "RoboCop-Win64-Shipping_2025_02_24_23_28_48_260.mp4"},\
})

configs["episodes"].append(\
{ "title": "MP",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:21" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Discovery_2025_03_15_22_55_07_819.mp4"},\
})

configs["episodes"].append(\
{ "title": "price about the RX 570",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:42.8" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "RX570_olx.mkv"},\
})

configs["episodes"].append(\
{ "title": "mined and no drivers",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:54.5" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "rx570_mined.mkv"},\
})

configs["episodes"].append(\
{ "title": "alternatives GTX 970",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "09:01.6" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_autumn_GTX970.mp4"},\
})

configs["episodes"].append(\
{ "title": "bye",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "09:09.3" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_autumn_RX570.mp4"},\
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

#for x in range(19,26):
#    scriptedvided.makeVideoForEpisode(configs["episodes"][x], configs)
#
scriptedvided.makeVideo(configs)