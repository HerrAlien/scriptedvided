import scriptedvided

configs = { "defaultAudioFile" : "R7_265_2024.ogg",\
"mediaFolder" : "F:\\Videos\\r7_265_2024", \
"stockFolder" : "F:\\Videos\\stock",\
"benchmarkFile" : "F:\\Videos\\r7_265_2024\\Benchmark_R7_265_2024.txt",\
"outputFolder" : "F:\\Videos\\r7_265_2024\\output", \
"outputFile" : "r7_265_2024.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "3 line-ups, one GPU", "until" : "Rainbow Six: Siege"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Rainbow Six: Siege", "until" : "Fortnite"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Fortnite", "until" : "Conclusions"}}, \
{"file" : "Inspired - MaikonMusic  Free Background Music  Audio Library Release.mp3", "timestamps" : ("00:00", None ), "destinationTimestamp" : {"title" : "Conclusions", "until" : "EOF"}}, \
], "volume" : 0.06 },\
"episodes" : [],\
"youtube" : {"title" : "", \
"description" : ''' This GPU served under 3 video card offerings.
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

TechPowerup entries: https://www.techpowerup.com/gpu-specs/sapphire-dual-x-r7-265.b2749
''', \
"tags" : "AMD,Radeon,GCN,Pitcairn,GCN 1.0,HD7850,HD 7850,R7 265,R7 370",\
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
{ "title": "3 line-ups, one GPU",\
"audio" : {"timestamps" : ("00:00", "00:17.9" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_r7_265_outside.mp4"},\
})


configs["episodes"].append(\
{ "title": "The GPU details",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:35.4" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "r7_265_GPUZ.mp4"},\
})

configs["episodes"].append(\
{ "title": "Cooling and thermals",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:49.4" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "r7_265_cooling.mp4"},\
})

configs["episodes"].append(\
{ "title": "The test system: Z230 workstation (HP)",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:01.3" ), "volume" : 0.999, "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Z230 workstation from HP'",\
              "'CPU\: E3-1241v3 Xeon (i7 4770 equivalent)'",\
              "'RAM\: 32GB DDR3 at 1600 MHz, dual channel'",\
    ]\
}, \
"video" : {"file" : "Z230_closed.mp4" , "rotation" : 180}\
})

####################### end of intro ###############################




####################### gaming section ###############################
configs["episodes"].append(\
{ "title": "Rainbow Six: Siege",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:28.6" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Rainbow Six\: Siege'",\
              scriptedvided.r6sText('1920x1080, low settings, 100% render scale', 74,58 ), \
              scriptedvided.r6sText('1280x720, low settings, 100% render scale' , 132, 95),\
              scriptedvided.r6sText('1920x1080, low settings, 50% render scale' , 103, 79), \
              scriptedvided.r6sText('1280x720, low settings, 50% render scale'  , 166, 114),\
]}, \
})

configs["episodes"].append(\
{ "title": "Doom Eternal",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:44.5" ), "padAudio" : 0.05 },\
"video" : "r7_265_DOOMEternalx64vk.mp4",\
})

configs["episodes"].append(\
{ "title": "Fallout 4", \
"video" : {"file" : "GTX970_Fallout4_2024_04_20_08_16_35_879.mp4", "start":"00:00"},\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:03.9" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, high settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Apex Legends",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:31.3" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Apex Legends'",\
              scriptedvided.r6sText('1920x1080, low settings' , 77, 54), \
              scriptedvided.r6sText('1600x900, low settings'  , 96, 65), \
              scriptedvided.r6sText('1280x720, low settings'  ,119, 75), \
]}, \
"video" : "rx580_r5apex_2024_07_26_22_34_08_382-converted.mp4" \
})

configs["episodes"].append(\
{ "title": "Shadow of the Tomb Raider",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:52.4" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Shadow of the Tomb Raider'",\
              scriptedvided.r6sText('1920x1080, lowest settings'  , 54, 37), \
              scriptedvided.r6sText('1600x900, low settings'      , 48, 29), \
]}, \
"video" : {"file" : "SOTTR_gaming_highest.mp4" , "start" : "05:00"}\
})

configs["episodes"].append(\
{ "title": "Counter-Strike 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:15.4" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Counter-Strike 2'",\
              scriptedvided.r6sText('1920x1080, low settings', 114, 92),\
              scriptedvided.r6sText('1600x900, low settings' , 125, 85),\
              scriptedvided.r6sText('1280x720, low settings' , 117, 79),\
]}, \
})

configs["episodes"].append(\
{ "title": "Borderlands 3",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:54.3" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Borderlands 3'",\
              scriptedvided.r6sText('1920x1080, very low settings', 46, 34),\
              scriptedvided.r6sText('1920x1080, low settings'     , 39, 29),\
              scriptedvided.r6sText('1600x900, medium settings'   , 37, 28),\
              scriptedvided.r6sText('1280x720, medium settings'   , 45, 33),\
]}, \
})

configs["episodes"].append(\
{ "title": "XDefiant",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:17" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'XDefiant'",\
              scriptedvided.r6sText('1920x1080, low settings', 84, 59),\
              scriptedvided.r6sText('1600x900, low settings' , 109, 74),\
              scriptedvided.r6sText('1280x720, low settings' , 144, 91),\
]}, \
})

configs["episodes"].append(\
{ "title": "Resident Evil 4 (Remake)", "video" : "stock_re4demo_phoneCall.mp4", \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:38.8" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, prioritize performance", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Fortnite",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:05.5" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Fortnite'",\
              scriptedvided.r6sText('1920x1080, performance mode' ,  93,  63),\
              scriptedvided.r6sText('1600x900, performance mode'  ,  120,  69),\
              scriptedvided.r6sText('1280x720, performance mode'  ,  148,  72),\
]}, \
"video" : "rx580_high_FortniteClient-Win64.mp4"\
})

configs["episodes"].append(\
{ "title": "Fortnite Reload",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:23.2" ), "padAudio" : 0.05 },\
"video" : "FortniteClient-bench_reload_2024_07_01.mp4",\
"overlay" : { \
    "text" : ["'Fortnite Reload'",\
              scriptedvided.r6sText('1920x1080, performance mode',  165,  84),\
              scriptedvided.r6sText('1600x900, performance mode' ,  189,  88),\
              scriptedvided.r6sText('1280x720, performance mode' ,  196,  75),\
]}, \
})

configs["episodes"].append(\
{ "title": "Terminator: Resistance",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:46.4" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Terminator\: Resistance'",\
              scriptedvided.r6sText('1920x1080, low settings',  66,  48),\
              scriptedvided.r6sText('1280x720, low settings' ,  107,  77),\
]}, \
})

configs["episodes"].append(\
{ "title": "Overwatch 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:10.4" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Overwatch 2'",\
              scriptedvided.r6sText('1920x1080, low settings', 126 , 97 ),\
              scriptedvided.r6sText('1600x900, low settings' ,  174, 140 ),\
              scriptedvided.r6sText('1280x720, low settings' , 243 , 199 ),\
]}, \
})

configs["episodes"].append(\
{ "title": "DOTA2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:36.3" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Control",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:58.7" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Control'",\
              scriptedvided.r6sText('1920x1080, lowest settings', 46 ,  35),\
              scriptedvided.r6sText('1280x720, lowest settings' , 86 , 62 ),\
]}, \
"video" : "rx580_Control_DX11_2024_07_27_22_47_25_351-converted.mp4" \
})

configs["episodes"].append(\
{ "title": "Grand Theft Auto V",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:18.8" ), "padAudio" : 0.05 },\
"video" : {"file" : "stock_gtaV_tutorial2.mp4", "start" : "00:20"},\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Warframe",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:34.2" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

####################### end of gaming section ###############################

####################### conclusion ###############################
# second category
configs["episodes"].append(\
{ "title": "Conclusions",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:45.7" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_r7_265_outside_2.mp4"},\
})

# cards from the latter
configs["episodes"].append(\
{ "title": "psu connector",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:56.2" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Z230_PSU.mp4"},\
})

configs["episodes"].append(\
{ "title": "R7 265 compared to GT 1030",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:12.4" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "olx_GT1030_R7_265.mkv"},\
})

configs["episodes"].append(\
{ "title": "R7 270",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:22.7" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_r7_265_270_outside.mp4", "start" : "00:17"},\
})

configs["episodes"].append(\
{ "title": "bye",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:29.3" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_r7_265_outside.mp4"},\
})


##configs["episodes"].append(\
##{ "title": "Blooper",\
##"isChapter" : False,\
##"audio" : {"timestamps" : ( "13:40.5", "14:04.2") },\
##"video" : {"file":"HiRezTrio-P_aladins_R_ealmRoyale_R_ogueCompany.mp4"}\
##})

#scriptedvided.makeVideoForEpisode(configs["episodes"][7], configs)
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

