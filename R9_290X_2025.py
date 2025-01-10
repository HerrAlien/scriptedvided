import scriptedvided

configs = { "defaultAudioFile" : "R9_290X_2025.ogg",\
"mediaFolder" : "F:\\Videos\\R9_290X_2025", \
"stockFolder" : "F:\\Videos\\stock",\
"benchmarkFile" : "F:\\Videos\\R9_290X_2025\\Benchmark_R9_290X_2025.txt",\
"outputFolder" : "F:\\Videos\\R9_290X_2025\\output", \
"outputFile" : "R9_290X_2025.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "A hot card", "until" : "Delta Force"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Delta Force", "until" : "Counter-Strike 2"}}, \
{"file" : "Inspired - MaikonMusic  Free Background Music  Audio Library Release.mp3", "timestamps" : ("00:00", None ), "destinationTimestamp" : {"title" : "Counter-Strike 2", "until" : "Fortnite Reload results"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Fortnite Reload results", "until" : "Conclusions"}}, \
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
{ "title": "A hot card",\
"audio" : {"timestamps" : ("00:00", "00:12.6" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_r9_290x_outside.mp4"},\
})

configs["episodes"].append(\
{ "title": "The GPU",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:28.9" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "r9_290X_GPUZ_Valley.mkv"},\
})

configs["episodes"].append(\
{ "title": "Cooling and thermals",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:39" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "R9_290_X_and_nonX.mp4", "start" : "00:00", "rotation" : -90},\
})

configs["episodes"].append(\
{ "title": "Blower cooler",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:49.55" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "R9_290X_cooling-converted.mp4"},\
})

configs["episodes"].append(\
{ "title": "Default fan curve means 90C",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:04.8" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "R9_290X_Heaven_noFanCurve.mp4"},\
})

configs["episodes"].append(\
{ "title": "Custom fan curve means 70C",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:18.9" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "R9_290X-blooper-custom-fan-curve.mp4"},\
})


configs["episodes"].append(\
{ "title": "The test system",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:36.7" ), "volume" : 0.999, "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Custom build'",\
              "'CPU\: Ryzen 5 3600'",\
              "'RAM\: 32GB DDR4 at 3000 MHz, dual channel'",\
    ]\
}, \
"video" : {"file" : "test_system_noGPU.mp4" }\
})

configs["episodes"].append(\
{ "title": "Methodology - some game footage",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:47.35" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "DeltaForceClient_2025_01_06.mp4"},\
})

####################### end of intro ###############################




####################### gaming section ###############################
configs["episodes"].append(\
{ "title": "Delta Force",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:25.1" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Delta Force'",\
              scriptedvided.r6sText('1920x1080, low settings', 77, 59),\
              scriptedvided.r6sText('1600x900, low settings' , 99, 77),\
              scriptedvided.r6sText('1280x720, low settings' ,115, 87),\
]}, \
})

configs["episodes"].append(\
{ "title": "XDefiant",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:55.7" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'XDefiant'",\
              scriptedvided.r6sText('1920x1080, low settings', 160, 104),\
              scriptedvided.r6sText('1600x900, low settings' , 198, 120),\
              scriptedvided.r6sText('1280x720, low settings' , 247, 136),\
]}, \
})

configs["episodes"].append(\
{ "title": "Rainbow Six: Siege",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:24.4" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Rainbow Six\: Siege'",\
              scriptedvided.r6sText('1920x1080, low settings, 100% render scale', 146, 119),\
              scriptedvided.r6sText('1280x720, low settings, 100% render scale',  230, 177),\
              scriptedvided.r6sText('1920x1080, low settings, 50% render scale',  198, 157),\
              scriptedvided.r6sText('1280x720, low settings, 50% render scale',   279, 209),\
]}, \
})

configs["episodes"].append(\
{ "title": "Doom Eternal",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:50.5" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Doom Eternal'",\
              scriptedvided.r6sText('1920x1080, medium settings', 90, 69),\
              scriptedvided.r6sText('1600x900, high settings'   , 75, 58),\
]}, \
})

configs["episodes"].append(\
{ "title": "The Finals",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:19.5" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'The Finals'",\
              scriptedvided.r6sText('1920x1080, low settings', 77, 54), \
              scriptedvided.r6sText('1600x900, low settings' , 78, 55), \
              scriptedvided.r6sText('1280x720, low settings' , 84, 60), \
]}, \
})

configs["episodes"].append(\
{ "title": "Fallout 4", \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:45.1" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Fallout 4'",\
              scriptedvided.r6sText('1920x1080, ultra settings, Diamond City', 60, 59), \
              scriptedvided.r6sText('1920x1080, ultra settings, outside'     , 58, 49), \
]}, \
})

configs["episodes"].append(\
{ "title": "Apex Legends",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:11.6" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Apex Legends'",\
              scriptedvided.r6sText('1920x1080, low settings', 140, 94), \
              scriptedvided.r6sText('1600x900, low settings' , 168,107), \
              scriptedvided.r6sText('1280x720, low settings' , 188,121), \
]}, \
"video" : "rx580_r5apex_2024_07_26_22_34_08_382-converted.mp4" \
})

configs["episodes"].append(\
{ "title": "Shadow of the Tomb Raider",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:27.1" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Shadow of the Tomb Raider'",\
              scriptedvided.r6sText('1920x1080, highest settings', 55, 40), \
              scriptedvided.r6sText('1920x1080, high settings'   , 64, 49), \
]}, \
"video" : {"file" : "rx580_SOTTR_2024_07_27_22_58_17_417-converted.mp4" , "start" : "01:42"}\
})

configs["episodes"].append(\
{ "title": "Counter-Strike 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:56.3" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Counter-Strike 2'",\
              scriptedvided.r6sText('1920x1080, low settings', 207, 164),\
              scriptedvided.r6sText('1600x900, low settings' , 212, 130),\
              scriptedvided.r6sText('1280x720, low settings' , 222, 108),\
]}, \
})

configs["episodes"].append(\
{ "title": "Borderlands 3",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:20.4" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Borderlands 3'",\
              scriptedvided.r6sText('1920x1080, high settings'  , 40, 32), \
              scriptedvided.r6sText('1600x900, ultra settings'  , 39, 31), \
              scriptedvided.r6sText('1280x720, badass settings' , 44, 34), \
]}, \
})

configs["episodes"].append(\
{ "title": "Resident Evil 4 (Remake)", \
"video" : "stock_re4demo_phoneCall.mp4", \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:51.1" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Resident Evil 4 (Remake)'",\
              scriptedvided.r6sText('1920x1080, performance', 71, 42),\
              scriptedvided.r6sText('1920x1080, balanced'   , 48, 26),\
              scriptedvided.r6sText('1600x900, balanced'    , 59, 28),\
]}, \
})

configs["episodes"].append(\
{ "title": "Fortnite",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:25.4" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Fortnite'",\
              scriptedvided.r6sText('1920x1080, performance mode', 184, 127),\
              scriptedvided.r6sText('1600x900, performance mode',  213, 132),\
              scriptedvided.r6sText('1280x720, performance mode' , 227, 133),\
]}, \
"video" : "FortniteClient_2024_12_25.mp4"\
})

configs["episodes"].append(\
{ "title": "Fortnite Reload results",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:47.8" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Fortnite Reload'",\
              scriptedvided.r6sText('1920x1080, performance mode', 210, 102),\
              scriptedvided.r6sText('1600x900, performance mode',  214, 96),\
              scriptedvided.r6sText('1280x720, performance mode' , 217, 95),\
]}, \
"video" : "FortniteReload_2024_12_21.mp4",\
})

configs["episodes"].append(\
{ "title": "Terminator: Resistance",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:12.5" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Terminator\: Resistance'",\
              scriptedvided.r6sText('1920x1080, epic settings', 76, 57),\
              scriptedvided.r6sText('2560x1440, epic settings', 50, 36),\
]}, \
})

configs["episodes"].append(\
{ "title": "Overwatch 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:32.4" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Overwatch 2'",\
              scriptedvided.r6sText('1920x1080, low settings', 275, 218),\
              scriptedvided.r6sText('1600x900, low settings' , 371, 299),\
              scriptedvided.r6sText('1280x720, low settings' , 501, 411),\
]}, \
})

configs["episodes"].append(\
{ "title": "Far Cry 6",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:51.4" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Far Cry 6'",\
              scriptedvided.r6sText('1920x1080, medium settings' , 65, 55),\
              scriptedvided.r6sText('1920x1080, high settings'   , 54, 43),\
              scriptedvided.r6sText('1920x1080, ultra settings'  , 44, 36),\
]}, \
})

configs["episodes"].append(\
{ "title": "DOTA2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "09:11" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Control",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "09:30.5" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Control'",\
              scriptedvided.r6sText('1920x1080, lowest settings' , 107, 83),\
              scriptedvided.r6sText('1920x1080, low settings'    , 85, 60),\
              scriptedvided.r6sText('1920x1080, medium settings' , 54, 33),\
]}, \
})

configs["episodes"].append(\
{ "title": "Grand Theft Auto V",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "09:58" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Grand Theft Auto V'",\
              scriptedvided.r6sText('1920x1080, high(?) settings' , 115, 83),\
              scriptedvided.r6sText('2560x1440, high(?) settings' , 83, 63),\
]}, \
})

configs["episodes"].append(\
{ "title": "Warframe",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "10:16.2" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

####################### end of gaming section ###############################

####################### conclusion ###############################
# better than the 280
configs["episodes"].append(\
{ "title": "Conclusions",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "10:28" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_r9_290x_outside.mp4"},\
})

configs["episodes"].append(\
{ "title": "TDP is high",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "10:46.8" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "R9_290X_baseline_temps.mp4"},\
})

configs["episodes"].append(\
{ "title": "price about the RX 570",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "11:01" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "R9_290X_RX570_olx.mkv"},\
})

configs["episodes"].append(\
{ "title": "alternatives",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "11:12.2" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_R9_290_RX570_GTX970_attic.mp4", "start" : "00:34", "rotation" : 90},\
})

configs["episodes"].append(\
{ "title": "bye",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "11:18.8" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_r9_290x_outside.mp4"},\
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