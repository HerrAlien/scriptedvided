import scriptedvided

configs = { "defaultAudioFile" : "R7_260_2024.ogg",\
"mediaFolder" : "F:\\Videos\\R7_260_2024", \
"stockFolder" : "F:\\Videos\\stock",\
"benchmarkFile" : "F:\\Videos\\R7_260_2024\\Benchmark_hd7770_2024.txt",\
"outputFolder" : "F:\\Videos\\R7_260_2024\\output", \
"outputFile" : "R7_260_2024.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "A lesser known Radeon", "until" : "Fallout 4"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Fallout 4", "until" : "Fortnite"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Fortnite", "until" : "DOTA2"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "DOTA2", "until" : "Conclusions"}}, \
{"file" : "Inspired - MaikonMusic  Free Background Music  Audio Library Release.mp3", "timestamps" : ("00:00", None ), "destinationTimestamp" : {"title" : "Conclusions", "until" : "EOF"}}, \
], "volume" : 0.06 },\
"episodes" : [],\
"youtube" : {"title" : "R7 260: 11 years old, DX 12 capable tested in 2024", \
"description" : '''We're revisiting the R7 260, but using different games though. 
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
"tags" : "AMD,ATI,Radeon,R7 260,Bonaire,GCN,GCN2,GCN 2,GCN 2.0",\
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

configs["episodes"].append(\
{ "title": "A lesser known Radeon",\
"audio" : {"timestamps" : ("00:00", "00:14.9" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : ""\
})

configs["episodes"].append(\
{ "title": "The GPU",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:35.4" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : ""\
})

configs["episodes"].append(\
{ "title": "Cooling and thermals",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:50.7" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : ""\
})

configs["episodes"].append(\
{ "title": "The test system: Z230 workstation (HP)",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:00.9" ), "volume" : 0.999, "padAudio" : 0.1 },\
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
{ "title": "Fallout 4",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:50.9" ), "padAudio" : 0.1 },\
 "overlay" : { \
    "text" : ["'Fallout 4'",\
              scriptedvided.r6sText('1920x1080, low settings', , ),\
              scriptedvided.r6sText('1920x1080, high settings', , ),\
              scriptedvided.r6sText('1600x900, high settings' , , ),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "Apex Legends",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:06" ), "padAudio" : 0.1 },\
"overlay" : { \
    "text" : ["'Apex Legends'",\
              scriptedvided.r6sText('1920x1080, low settings', , ),\
              scriptedvided.r6sText('1600x900, low settings' , , ),\
              scriptedvided.r6sText('1280x720, low settings' , , ),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "Shadow of the Tomb Raider",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:28.4" ), "padAudio" : 0.1 },\
"video" : {"file" : ""},\
"overlay" : { \
    "text" : ["'Shadow of the Tomb Raider'",\
              scriptedvided.r6sText('1920x1080, lowest settings', , ),\
              scriptedvided.r6sText('1600x900, lowest settings' , , ),\
              scriptedvided.r6sText('1280x720, lowest settings' , , ),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "Counter-Strike 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:49.3" ), "padAudio" : 0.1 },\
"overlay" : { \
    "text" : ["'Counter-Strike 2'",\
              scriptedvided.r6sText('1920x1080, low settings', 60, 45),\
              scriptedvided.r6sText('1600x900, low settings' , 74, 55),\
              scriptedvided.r6sText('1280x720, low settings' , 85, 56),\
]}, \
})

configs["episodes"].append(\
{ "title": "Borderlands 3",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:26.3" ), "padAudio" : 0.1 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, very low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Fortnite",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:43.5" ), "padAudio" : 0.1 },\
"overlay" : { \
    "text" : ["'Fortnite'",\
              scriptedvided.r6sText('1920x1080, performance mode',  , ),\
              scriptedvided.r6sText('1600x900, performance mode' ,  , ),\
              scriptedvided.r6sText('1280x720, performance mode' ,  , ),\
]}, \
})

configs["episodes"].append(\
{ "title": "Fortnite Reload results",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:05" ), "padAudio" : 0.1 },\
"video" : "FortniteClient-bench_reload_2024_07_01.mp4",\
"overlay" : { \
    "text" : ["'Fortnite Reload'",\
              scriptedvided.r6sText('1920x1080, performance mode', , ),\
              scriptedvided.r6sText('1600x900, performance mode' , , ),\
              scriptedvided.r6sText('1280x720, performance mode' , , ),\
]}, \
})

configs["episodes"].append(\
{ "title": "Terminator: Resistance",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:35.4" ), "padAudio" : 0.1 },\
"video" : {"file" : ""},\
"overlay" : { \
    "text" : ["'Terminator\: Resistance'",\
              scriptedvided.r6sText('1920x1080, low settings',  ,  ),\
              scriptedvided.r6sText('1280x720, low settings' ,  ,  ),\
]}, \
})

configs["episodes"].append(\
{ "title": "Overwatch 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:08.1" ), "padAudio" : 0.1 },\
"overlay" : { \
    "text" : ["'Overwatch 2'",\
              scriptedvided.r6sText('1920x1080, low settings', ,  ),\
              scriptedvided.r6sText('1600x900, low settings' , ,  ),\
              scriptedvided.r6sText('1280x720, low settings' , ,  ),\
]}, \
})

configs["episodes"].append(\
{ "title": "Zenless Zone Zero",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:33.5" ), "padAudio" : 0.1 },\
"video" : {"file" : "ZenlessZoneZero_2024_07_07_20m.mp4", "start" : "00:40"},\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "DOTA2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:58.2" ), "padAudio" : 0.1 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Control",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:22.3" ), "padAudio" : 0.1 },\
"video" : "stock_Control_720p.mp4",\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Grand Theft Auto V",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:37.9" ), "padAudio" : 0.1 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Warframe",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:01" ), "padAudio" : 0.1 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Rainbow Six: Siege",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:34" ), "padAudio" : 0.1 },\
"overlay" : { \
    "text" : ["'Rainbow Six\: Siege'",\
              scriptedvided.r6sText('1920x1080, low settings, 100% render scale', ,  ), \
              scriptedvided.r6sText('1280x720, low settings, 100% render scale',  ,  ),\
              scriptedvided.r6sText('1920x1080, low settings, 50% render scale',  ,  ),\
              scriptedvided.r6sText('1280x720, low settings, 50% render scale',   ,  )]\
}, \
})
####################### end of gaming section ###############################


####################### conclusion ###############################
# what's with the card?
configs["episodes"].append(\
{ "title": "Conclusions",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:48.7" ),  "volume" : 0.999, "padAudio" : 0.1 },\
"padAudio" : 0.1 },\
"video" : {"file" : ""},\
})

# extra performance over the 7770
configs["episodes"].append(\
{ "title": "only 10 extra watts",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:04.2" ),  "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : ""},\
})

# reviews back in the day
configs["episodes"].append(\
{ "title": "Priced too close to the 260x",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:17.4" ),  "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "removing the 260X",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:26" ),  "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : ""},\
})


configs["episodes"].append(\
{ "title": "bye",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:36" ),  "volume" : 0.999, "padAudio" : 0.1 },\
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
#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "Apex Legends"][0], configs)
scriptedvided.makeVideo(configs)

