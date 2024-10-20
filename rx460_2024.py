import scriptedvided

configs = { "defaultAudioFile" : "rx460_2024.ogg",\
"mediaFolder" : "F:\\Videos\\RX460_2024", \
"stockFolder" : "F:\\Videos\\stock",\
"benchmarkFile" : "F:\\Videos\\RX460_2024\\Benchmark_RX460_2024.txt",\
"outputFolder" : "F:\\Videos\\RX460_2024\\output", \
"outputFile" : "RX460_2024.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "", "until" : "Rainbow Six: Siege"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Rainbow Six: Siege", "until" : "Fortnite"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Fortnite", "until" : "Conclusions"}}, \
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
{ "title": "",\
"audio" : {"timestamps" : ("00:00", "00:13.2" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "a bit late - 750 ti 1",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:00", "00:24.4" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})


configs["episodes"].append(\
{ "title": "The GPU",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:40.9" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "Cooling and thermals",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:59.6" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "The test system: Z230 workstation (HP)",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:13" ), "volume" : 0.999, "padAudio" : 0.05 },\
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
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:41" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Rainbow Six\: Siege'",\
              scriptedvided.r6sText('1920x1080, low settings, 100% render scale', , ), \
              scriptedvided.r6sText('1280x720, low settings, 100% render scale',  , ),\
              scriptedvided.r6sText('1920x1080, low settings, 50% render scale',  , ), \
              scriptedvided.r6sText('1280x720, low settings, 50% render scale',   , ),\
]}, \
})

configs["episodes"].append(\
{ "title": "Doom Eternal",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:13" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Doom Eternal'",\
              scriptedvided.r6sText('1920x1080, ultra nightmare settings', , ), \
              scriptedvided.r6sText('1920x1080, low settings', , ), \
]}, \
})

configs["episodes"].append(\
{ "title": "Fallout 4", \
"video" : {"file":"GTX970_Fallout4_2024_04_20_23_20_24_502.mp4", "start":"00:05"},\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:38.3" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, ultra settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Apex Legends",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:01.7" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Apex Legends'",\
              scriptedvided.r6sText('1920x1080, low settings'     , , ), \
              scriptedvided.r6sText('1600x900, low settings'      , , ), \
              scriptedvided.r6sText('1280x720, low settings'      , , ), \
]}, \
"video" : "rx580_r5apex_2024_07_26_22_34_08_382-converted.mp4" \
})

configs["episodes"].append(\
{ "title": "Shadow of the Tomb Raider",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:40.2" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, highest settings", \
    }\
}, \
"video" : {"file" : "rx580_SOTTR_2024_07_27_22_58_17_417-converted.mp4" , "start" : "01:42"}\
})

configs["episodes"].append(\
{ "title": "Counter-Strike 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:12.7" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Counter-Strike 2'",\
              scriptedvided.r6sText('1920x1080, low settings', , ),\
              scriptedvided.r6sText('1600x900, low settings' , , ),\
              scriptedvided.r6sText('1280x720, low settings' , , ),\
]}, \
})

configs["episodes"].append(\
{ "title": "Borderlands 3",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:43.5" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, badass settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "XDefiant",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:12.1" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'XDefiant'",\
              scriptedvided.r6sText('1920x1080, ultra settings', ,  ),\
              scriptedvided.r6sText('1920x1080, high settings',  ,  ),\
              scriptedvided.r6sText('1920x1080, low settings',   ,  ),\
]}, \
})

configs["episodes"].append(\
{ "title": "Resident Evil 4 (Remake)", "video" : "stock_re4demo_phoneCall.mp4", \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:37.9" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Resident Evil 4 (Remake)'",\
              scriptedvided.r6sText('1920x1080, prioritize performance', , ),\
              scriptedvided.r6sText('1920x1080, balanced'              , , ),\
]}, \
})

configs["episodes"].append(\
{ "title": "Fortnite",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:40.3" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Fortnite'",\
              scriptedvided.r6sText('1920x1080, performance mode',  ,  ),\
              scriptedvided.r6sText('1600x900, performance mode',   ,  ),\
              scriptedvided.r6sText('1280x720, performance mode' ,  ,  ),\
]}, \
"video" : "rx580_high_FortniteClient-Win64.mp4"\
})

configs["episodes"].append(\
{ "title": "Fortnite Reload results",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:24" ), "padAudio" : 0.05 },\
"video" : "FortniteClient-bench_reload_2024_07_01.mp4",\
"overlay" : { \
    "text" : ["'Fortnite Reload'",\
              scriptedvided.r6sText('1920x1080, performance mode',  ,  ),\
              scriptedvided.r6sText('1600x900, performance mode',   ,  ),\
              scriptedvided.r6sText('1280x720, performance mode' ,  ,  ),\
]}, \
})

configs["episodes"].append(\
{ "title": "Terminator: Resistance",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:48.5" ), "padAudio" : 0.05 },\
"video" : {"file" : "Terminator-Win64-Shipping_2024_07_20_23_51_41_842-converted.mp4", "start" : "33:54"},\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, highest settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Overwatch 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:11.5" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Overwatch 2'",\
              scriptedvided.r6sText('1920x1080, low settings',  ,  ),\
              scriptedvided.r6sText('1600x900, low settings' ,  ,  ),\
              scriptedvided.r6sText('1280x720, low settings' ,  ,  ),\
]}, \
})

configs["episodes"].append(\
{ "title": "DOTA2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Control",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, high settings", \
    }\
}, \
"video" : "rx580_Control_DX11_2024_07_27_22_47_25_351-converted.mp4" \
})

configs["episodes"].append(\
{ "title": "Grand Theft Auto V",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Warframe",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

####################### end of gaming section ###############################

####################### conclusion ###############################
# really need an upgrade
configs["episodes"].append(\
{ "title": "Conclusions",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})



configs["episodes"].append(\
{ "title": "bye",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
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

