import scriptedvided

configs = { "defaultAudioFile" : "r7_260X_2024.ogg",\
"mediaFolder" : "F:\\Videos\\R7_260X_2024", \
"stockFolder" : "F:\\Videos\\stock",\
"benchmarkFile" : "F:\\Videos\\R7_260X_2024\\Benchmark_R7_260X_2024.txt",\
"outputFolder" : "F:\\Videos\\R7_260X_2024\\output", \
"outputFile" : "R7_260X_2024.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "Bonaire - the XTX one", "until" : "Rainbow Six: Siege"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Rainbow Six: Siege", "until" : "Resident Evil 4 (Remake)"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Resident Evil 4 (Remake)", "until" : "Conclusions"}}, \
{"file" : "Inspired - MaikonMusic  Free Background Music  Audio Library Release.mp3", "timestamps" : ("00:00", None ), "destinationTimestamp" : {"title" : "Conclusions", "until" : "EOF"}}, \
], "volume" : 0.06 },\
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

TechPowerup entry: https://www.techpowerup.com/gpu-specs/msi-r7-260x-ocv1.b3094

''', \
"tags" : "AMD,ATI,Radeon,R7 260X,Bonaire,Bonaire XTX,GCN,GCN2,GCN 2,GCN 2.0",\
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
configs["episodes"].append(\
{ "title": "Bonaire - the XTX one",\
"audio" : {"timestamps" : ("00:00", "00:21" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "r7_260x_breel_outside.mp4"},\
})

configs["episodes"].append(\
{ "title": "The GPU",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:34.7" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "r7_260x_Heaven_16lanes.mp4"},\
})


configs["episodes"].append(\
{ "title": "Cooling and thermals",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:58.5" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "r7_260x_cooling.mp4"},\
})

configs["episodes"].append(\
{ "title": "The test system: Z230 workstation (HP)",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:13.5" ), "volume" : 0.999, "padAudio" : 0.05 },\
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
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:44" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Rainbow Six\: Siege'",\
              scriptedvided.r6sText('1920x1080, low settings, 100% render scale', 66, 55), \
              scriptedvided.r6sText('1280x720, low settings, 100% render scale', 125 , 99),\
              scriptedvided.r6sText('1920x1080, low settings, 50% render scale', 98, 80), \
              scriptedvided.r6sText('1280x720, low settings, 50% render scale',  167, 121),\
]}, \
})

configs["episodes"].append(\
{ "title": "Doom Eternal",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:11.75" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Doom Eternal'",\
              scriptedvided.r6sText('1920x1080, low settings', 49, 35), \
              scriptedvided.r6sText('1600x900, low settings', 63, 46), \
              scriptedvided.r6sText('1280x720, low settings', 82, 61), \
]}, \
})

configs["episodes"].append(\
{ "title": "The Finals",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:33.9" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, lowest settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Fallout 4", \
"video" : {"file" : "GTX970_Fallout4_2024_04_21_21_55_58_601.mp4", "start" : "02:40"},\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:02.9" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Fallout 4'",\
              scriptedvided.r6sText('1920x1080, high settings', 32, 30), \
              scriptedvided.r6sText('1600x900, high settings', 40, 37), \
]}, \
})

configs["episodes"].append(\
{ "title": "Apex Legends",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:42" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Apex Legends'",\
              scriptedvided.r6sText('1920x1080, low settings', 73, 52), \
              scriptedvided.r6sText('1600x900, low settings', 94, 65), \
              scriptedvided.r6sText('1280x720, low settings', 121, 76), \
]}, \
})

configs["episodes"].append(\
{ "title": "Shadow of the Tomb Raider",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:05" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Shadow of the Tomb Raider'",\
              scriptedvided.r6sText('1920x1080, lowest settings', 50, 37), \
              scriptedvided.r6sText('1600x900, lowest settings', 62, 43), \
              scriptedvided.r6sText('1280x720, lowest settings', 75, 43), \
]}, \
"video" : {"file" : "rx580_SOTTR_2024_07_27_22_58_17_417-converted.mp4" , "start" : "01:42"}\
})

configs["episodes"].append(\
{ "title": "Counter-Strike 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:35.1" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Counter-Strike 2'",\
              scriptedvided.r6sText('1920x1080, low settings', 95, 76),\
              scriptedvided.r6sText('1600x900, low settings' , 98, 78),\
              scriptedvided.r6sText('1280x720, low settings' , 121, 71),\
]}, \
})

configs["episodes"].append(\
{ "title": "Borderlands 3",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:50.7" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, very low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "XDefiant",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:12.4" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'XDefiant'",\
              scriptedvided.r6sText('1920x1080, lowest settings', 75,  53),\
              scriptedvided.r6sText('1600x900, lowest settings',  100,  71),\
              scriptedvided.r6sText('1280x720, lowest settings',  138 ,  91),\
]}, \
})

configs["episodes"].append(\
{ "title": "Resident Evil 4 (Remake)", "video" : "stock_re4demo_phoneCall.mp4", \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:33.8" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, prioritize performance", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Fortnite",\
"video" : {"file" : "FortniteClient-Win64-Shipping_2024_06_24_07_59_39_389-converted.mp4", "start" : "04:00"},\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:56.4" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Fortnite'",\
              scriptedvided.r6sText('1920x1080, performance mode', 83, 57),\
              scriptedvided.r6sText('1600x900, performance mode' ,107, 53),\
              scriptedvided.r6sText('1280x720, performance mode' ,141, 70),\
]}, \
})

configs["episodes"].append(\
{ "title": "Fortnite Reload results",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:17.4" ), "padAudio" : 0.05 },\
"video" : "FortniteClient-bench_reload_2024_07_01.mp4",\
"overlay" : { \
    "text" : ["'Fortnite Reload'",\
              scriptedvided.r6sText('1920x1080, performance mode', 173, 60),\
              scriptedvided.r6sText('1600x900, performance mode' , 203, 78),\
              scriptedvided.r6sText('1280x720, performance mode' , 222, 88),\
]}, \
})

configs["episodes"].append(\
{ "title": "Terminator: Resistance",\
"video" : {"file" : "Terminator-Win64-Shipping_2024_07_20_23_51_41_842-converted.mp4", "start" : "28:00"},\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:46.2" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Terminator\: Resistance'",\
              scriptedvided.r6sText('1920x1080, low settings', 56, 43),\
              scriptedvided.r6sText('1280x720, low settings' , 105, 77),\
]}, \
})

configs["episodes"].append(\
{ "title": "Overwatch 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:15.3" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Overwatch 2'",\
              scriptedvided.r6sText('1920x1080, low settings', 97, 74),\
              scriptedvided.r6sText('1600x900, low settings' , 134, 104),\
              scriptedvided.r6sText('1280x720, low settings' , 196, 154),\
]}, \
})

configs["episodes"].append(\
{ "title": "Far Cry 6",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:35.3" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, lowest settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "DOTA2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:56.15" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Control",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:15.5" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Control'",\
              scriptedvided.r6sText('1920x1080, lowest settings', 38, 31),\
              scriptedvided.r6sText('1280x720, lowest settings' , 74, 57),\
]}, \
})

configs["episodes"].append(\
{ "title": "Grand Theft Auto V",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:36.5" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Warframe",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:58" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

####################### end of gaming section ###############################

####################### conclusion ###############################
# breel with the card, maybe showing the 6 pin
configs["episodes"].append(\
{ "title": "Conclusions",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "09:20.2" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "r7_260x_breel_outside.mp4"},\
})

configs["episodes"].append(\
{ "title": "price",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "09:33.5" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : "cheap_r7_260X.mkv",\
})

configs["episodes"].append(\
{ "title": "long bye",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "09:57" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "r7_260x_breel_outside.mp4"},\
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

