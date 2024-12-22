import scriptedvided

configs = { "defaultAudioFile" : "gtx960_2024_2.ogg",\
"mediaFolder" : "F:\\Videos\\gtx960_2024", \
"stockFolder" : "F:\\Videos\\stock",\
"benchmarkFile" : "F:\\Videos\\gtx960_2024\\Benchmark_GTX_960_2024.txt",\
"outputFolder" : "F:\\Videos\\GTX960_2024\\output", \
"outputFile" : "GTX960_2025.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#00800080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "An old 4GB card", "until" : "Rainbow Six: Siege"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Rainbow Six: Siege", "until" : "XDefiant"}}, \
{"file" : "Inspired - MaikonMusic  Free Background Music  Audio Library Release.mp3", "timestamps" : ("00:00", None ), "destinationTimestamp" : {"title" : "XDefiant", "until" : "Fortnite OG results"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Fortnite OG results", "until" : "Conclusions"}}, \
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

Our 2023 review of the HD 7770: 
Our 2022 review of the HD 7770: https://youtu.be/4rEcNy2YC0I

TechPowerup entries: https://www.techpowerup.com/gpu-specs/radeon-r7-260.c2511
TechPowerup entries: https://www.techpowerup.com/gpu-specs/asus-r7-260-1-gb.b2732
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
{ "title": "An old 4GB card",\
"audio" : {"timestamps" : ("00:00", "00:13.5" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_autumn_GTX960_4G_MSI.mp4"},\
})


configs["episodes"].append(\
{ "title": "The GPU",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:27.1" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GTX960_GPUZ_Valley.mkv"},\
})

configs["episodes"].append(\
{ "title": "Cooling and thermals",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:49.6" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "msi_gtx960_cooling.mp4"},\
})


configs["episodes"].append(\
{ "title": "The test system: Z230 workstation (HP)",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:06.75" ), "volume" : 0.999, "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Z230 workstation from HP'",\
              "'CPU\: E3-1241v3 Xeon (i7 4770 equivalent)'",\
              "'RAM\: 32GB DDR3 at 1600 MHz, dual channel'",\
    ]\
}, \
"video" : {"file" : "Z230_closed.mp4" , "rotation" : 180}\
})

configs["episodes"].append(\
{ "title": "Methodology - some game footage",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:21.55" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GTX970_Control_DX11_ultra.mp4"},\
})

####################### end of intro ###############################




####################### gaming section ###############################
configs["episodes"].append(\
{ "title": "Rainbow Six: Siege",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:06" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Rainbow Six\: Siege'",\
              scriptedvided.r6sText('1920x1080, low settings, 100% render scale', 81, 63),\
              scriptedvided.r6sText('1280x720, low settings, 100% render scale',  149, 108),\
              scriptedvided.r6sText('1920x1080, low settings, 50% render scale',  120, 91),\
              scriptedvided.r6sText('1280x720, low settings, 50% render scale',   181, 125),\
]}, \
})

configs["episodes"].append(\
{ "title": "Doom Eternal",\
"video" : "stock_DOOMEternal_2023_12_26.mp4",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:38.7" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Doom Eternal'",\
              scriptedvided.r6sText('1280x720, high settings'  , 85, 59),\
              scriptedvided.r6sText('1600x900, medium settings', 72, 54),\
              scriptedvided.r6sText('1920x1080, low settings'  , 68, 50),\
]}, \
})

configs["episodes"].append(\
{ "title": "The Finals",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:01.6" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'The Finals'",\
              scriptedvided.r6sText('1920x1080, low settings', 69, 44), \
              scriptedvided.r6sText('1600x900, low settings' , 69, 40), \
              scriptedvided.r6sText('1280x720, low settings' , 77, 47), \
]}, \
"video" : "TheFinals_Discovery_short_W.mp4" \
})

configs["episodes"].append(\
{ "title": "Fallout 4", \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:24.55" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Fallout 4'",\
              scriptedvided.r6sText('1920x1080, ultra settings, Diamond City', 50, 30), \
              scriptedvided.r6sText('1920x1080, ultra settings, outside'     , 59, 30), \
]}, \
})

configs["episodes"].append(\
{ "title": "Apex Legends",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:45.1" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Apex Legends'",\
              scriptedvided.r6sText('1920x1080, low settings', 118, 81), \
              scriptedvided.r6sText('1600x900, low settings' , 144, 98), \
              scriptedvided.r6sText('1280x720, low settings' , 174, 122), \
]}, \
"video" : "r5apex_bot_royale.mp4" \
})

configs["episodes"].append(\
{ "title": "Shadow of the Tomb Raider",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:06" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Shadow of the Tomb Raider'",\
              scriptedvided.r6sText('1920x1080, high settings'   , 44, 30), \
              scriptedvided.r6sText('1920x1080, medium settings' , 45, 30), \
]}, \
"video" : {"file" : "rx580_SOTTR_2024_07_27_22_58_17_417-converted.mp4" , "start" : "01:42"}\
})

configs["episodes"].append(\
{ "title": "Counter-Strike 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:31.9" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Counter-Strike 2'",\
              scriptedvided.r6sText('1920x1080, low settings', 114, 61),\
              scriptedvided.r6sText('1600x900, low settings' , 118, 65),\
              scriptedvided.r6sText('1280x720, low settings' , 135, 63),\
]}, \
})

configs["episodes"].append(\
{ "title": "Borderlands 3",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:04.6" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Borderlands 3'",\
              scriptedvided.r6sText('1920x1080, very low settings', 67, 51), \
              scriptedvided.r6sText('1920x1080, medium settings'  , 46, 36), \
              scriptedvided.r6sText('1600x900, high settings'     , 38, 29), \
]}, \
})
# 10:56.7 => 11:07 => 10.3 sec less
configs["episodes"].append(\
{ "title": "XDefiant",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:30.5" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'XDefiant'",\
              scriptedvided.r6sText('1920x1080, low settings', 119, 74),\
              scriptedvided.r6sText('1600x900, low settings' , 154, 94),\
              scriptedvided.r6sText('1280x720, low settings' , 201, 105),\
]}, \
})

configs["episodes"].append(\
{ "title": "Resident Evil 4 (Remake)", "video" : "stock_re4demo_phoneCall.mp4", \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:00.8" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Resident Evil 4 (Remake)'",\
              scriptedvided.r6sText('1920x1080, low settings', 42, 26),\
              scriptedvided.r6sText('1600x900, low settings' , 53, 33),\
              scriptedvided.r6sText('1280x720, low settings' , 64, 38),\
]}, \
})

configs["episodes"].append(\
{ "title": "Fortnite",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:25.2" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Fortnite'",\
              scriptedvided.r6sText('1920x1080, performance mode', 166, 53),\
              scriptedvided.r6sText('1600x900, performance mode', 173 , 58),\
              scriptedvided.r6sText('1280x720, performance mode' , 167, 54),\
]}, \
"video" : "Fortnite_C6S1_short.mp4"\
})

configs["episodes"].append(\
{ "title": "Fortnite Reload results",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:44.84" ), "padAudio" : 0.05 },\
"video" : "FortniteReload_2024_12_21.mp4",\
"overlay" : { \
    "text" : ["'Fortnite Reload'",\
              scriptedvided.r6sText('1920x1080, performance mode', 155, 75),\
              scriptedvided.r6sText('1600x900, performance mode',  155, 73),\
              scriptedvided.r6sText('1280x720, performance mode' , 159, 80),\
]}, \
})

configs["episodes"].append(\
{ "title": "Fortnite OG results",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:10.04" ), "padAudio" : 0.05 },\
"video" : "OG_F_ortnite.mp4",\
"overlay" : { \
    "text" : ["'Fortnite OG'",\
              scriptedvided.r6sText('1920x1080, performance mode', 179, 115),\
              scriptedvided.r6sText('1600x900, performance mode',  214, 134),\
              scriptedvided.r6sText('1280x720, performance mode' , 217, 136),\
]}, \
})

configs["episodes"].append(\
{ "title": "Terminator: Resistance",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:29.1" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, epic settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Overwatch 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "7:49.84" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Overwatch 2'",\
              scriptedvided.r6sText('1920x1080, low settings', 182, 143),\
              scriptedvided.r6sText('1600x900, low settings' , 244, 196),\
              scriptedvided.r6sText('1280x720, low settings' , 346, 275),\
]}, \
})

configs["episodes"].append(\
{ "title": "Far Cry 6",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:11.3" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Far Cry 6'",\
              scriptedvided.r6sText('1920x1080, low settings'   , 51, 43),\
              scriptedvided.r6sText('1920x1080, medium settings', 43, 37),\
              scriptedvided.r6sText('1920x1080, high settings'  , 37, 32),\
              scriptedvided.r6sText('1600x900, ultra settings'  , 37, 31),\
]}, \
})

configs["episodes"].append(\
{ "title": "DOTA2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:27.35" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Control",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:58.6" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Control'",\
              scriptedvided.r6sText('1920x1080, lowest settings' , 55, 41),\
              scriptedvided.r6sText('1920x1080, low settings'    , 47, 40),\
              scriptedvided.r6sText('1280x720, medium settings'  , 58, 47),\
              scriptedvided.r6sText('1280x720, high settings'    , 35, 27),\
]}, \
"video" : "GTX970_Control_DX11_medium.mp4" \
})

configs["episodes"].append(\
{ "title": "Grand Theft Auto V",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "09:26.7" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Grand Theft Auto V'",\
              scriptedvided.r6sText('1920x1080, low settings'     , 119, 60),\
              scriptedvided.r6sText('1920x1080, high(?) settings' , 83, 54),\
]}, \
})

configs["episodes"].append(\
{ "title": "Warframe",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "09:45.8" ), "padAudio" : 0.05 },\
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
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "10:02.9" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_autumn_GTX960_4G_MSI.mp4"},\
})

configs["episodes"].append(\
{ "title": "pricing",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "10:19.1" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GTX960_olx_2024.mkv"},\
})

configs["episodes"].append(\
{ "title": "Pascal is better",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "10:34.7" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "1050Ti_960_R9_280.mp4", "start" : "00:15"},\
})



configs["episodes"].append(\
{ "title": "teabaging",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "10:44.7" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "1050Ti_teabaging.mp4", "start" : "00:00"},\
})


configs["episodes"].append(\
{ "title": "bye",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "10:54.55" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_autumn_GTX960_4G_MSI.mp4"},\
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