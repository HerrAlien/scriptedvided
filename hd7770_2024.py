import scriptedvided

configs = { "defaultAudioFile" : "hd7770_2024.ogg",\
"mediaFolder" : "F:\\Videos\\hd7770_2024", \
"stockFolder" : "F:\\Videos\\stock",\
"benchmarkFile" : "F:\\Videos\\hd7770_2024\\Benchmark_hd7770_2024.txt",\
"outputFolder" : "F:\\Videos\\hd7770_2024\\output", \
"outputFile" : "hd7770_2024.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \

], "volume" : 0.06 },\
"episodes" : [],\
"youtube" : {"title" : "", \
"description" : '''We're revisiting the HD7770. Again. Different games though. 
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

TechPowerup entries: https://www.techpowerup.com/gpu-specs/msi-hd-7770-ghz-edition.b2295
TechPowerup entries: https://www.techpowerup.com/gpu-specs/asus-hd-7770.b609
''', \
"tags" : "AMD,ATI,Radeon,HD7770,HD 7770,GCN,GCN1,GCN 1",\
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
{ "title": "Is a 12 years old GPU still of any use",\
"audio" : {"timestamps" : ("00:00", "00:20" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : ""\
})

configs["episodes"].append(\
{ "title": "Different games",\
"audio" : {"timestamps" : (nextTS(configs), "00:43" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : "removed_games.mp4"\
})

configs["episodes"].append(\
{ "title": "The GPU",\
"audio" : {"timestamps" : (nextTS(configs), "00:56.7" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : "hd7770_heaven_gpuz.mp4"\
})

configs["episodes"].append(\
{ "title": "Cooling and thermals",\
"audio" : {"timestamps" : (nextTS(configs), "01:16" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "asus_hd7770.MOV", "start" : "00:00" }\
})

configs["episodes"].append(\
{ "title": "The test system: Z230 workstation (HP)",\
"audio" : {"timestamps" : (nextTS(configs), "01:29.6" ), "volume" : 0.999, "padAudio" : 0.1 },\
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
"audio" : {"timestamps" : (nextTS(configs), "02:10.8" ), "padAudio" : 0.1 },\
"overlay" : { \
    "text" : ["'Fallout 4'",\
              scriptedvided.r6sText('1920x1080, low settings', 33, 31),\
              scriptedvided.r6sText('1280x720, low settings' , 51, 47),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "Apex Legends",\
"audio" : {"timestamps" : (nextTS(configs), "02:43" ), "padAudio" : 0.1 },\
"overlay" : { \
    "text" : ["'Apex Legends'",\
              scriptedvided.r6sText('1920x1080, low settings', 48, 34),\
              scriptedvided.r6sText('1600x900, low settings' , 61, 42),\
              scriptedvided.r6sText('1280x720, low settings' , 78, 53),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "Shadow of the Tomb Raider",\
"audio" : {"timestamps" : (nextTS(configs), "03:31.3" ), "padAudio" : 0.1 },\
"overlay" : { \
    "text" : ["'Shadow of the Tomb Raider'",\
              scriptedvided.r6sText('1920x1080, lowest settings', 34,25 ),\
              scriptedvided.r6sText('1600x900, lowest settings' , 42, 31),\
              scriptedvided.r6sText('1280x720, lowest settings' , 55, 37),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "Counter-Strike 2",\
"audio" : {"timestamps" : (nextTS(configs), "04:00.3" ), "padAudio" : 0.1 },\
"overlay" : { \
    "text" : ["'Counter-Strike 2'",\
              scriptedvided.r6sText('1920x1080, low settings', 60, 45),\
              scriptedvided.r6sText('1600x900, low settings' , 74, 55),\
              scriptedvided.r6sText('1280x720, low settings' , 85, 56),\
}, \
})

configs["episodes"].append(\
{ "title": "Borderlands 3",\
"audio" : {"timestamps" : (nextTS(configs), "04:34.6" ), "padAudio" : 0.1 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, very low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Fortnite",\
"audio" : {"timestamps" : (nextTS(configs), "04:47" ), "padAudio" : 0.1 },\
}

configs["episodes"].append(\
{ "title": "Fortnite results",\
"isChapter" : False,\
"audio" : {"timestamps" : (nextTS(configs), "05:15.4" ), "padAudio" : 0.1 },\
"overlay" : { \
    "text" : ["'Fortnite'",\
              scriptedvided.r6sText('1920x1080, performance mode', 63, 41),\
              scriptedvided.r6sText('1600x900, performance mode' , 80, 41),\
              scriptedvided.r6sText('1280x720, performance mode' , 111, 68),\
}, \
})

configs["episodes"].append(\
{ "title": "Fortnite Reload results",\
"isChapter" : False,\
"audio" : {"timestamps" : (nextTS(configs), "05:45.5" ), "padAudio" : 0.1 },\
"overlay" : { \
    "text" : ["'Fortnite Reload'",\
              scriptedvided.r6sText('1920x1080, performance mode', 134, 97),\
              scriptedvided.r6sText('1600x900, performance mode' , 168, 121),\
              scriptedvided.r6sText('1280x720, performance mode' , 204, 134),\
}, \
})

configs["episodes"].append(\
{ "title": "Terminator: Resistance",\
"audio" : {"timestamps" : (nextTS(configs), "06:18" ), "padAudio" : 0.1 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Overwatch 2",\
"audio" : {"timestamps" : (nextTS(configs), "06:42.7" ), "padAudio" : 0.1 },\
"overlay" : { \
    "text" : ["'Overwatch 2'",\
              scriptedvided.r6sText('1920x1080, low settings', 73, 55),\
              scriptedvided.r6sText('1600x900, low settings' , 100, 77),\
              scriptedvided.r6sText('1280x720, low settings' , 145, 115),\
}, \
})

configs["episodes"].append(\
{ "title": "Zenless Zone Zero",\
"audio" : {"timestamps" : (nextTS(configs), "07:14.6" ), "padAudio" : 0.1 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "DOTA2",\
"audio" : {"timestamps" : (nextTS(configs), "07:32.6" ), "padAudio" : 0.1 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Control",\
"audio" : {"timestamps" : (nextTS(configs), "07:56" ), "padAudio" : 0.1 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Grand Theft Auto V",\
"audio" : {"timestamps" : (nextTS(configs), "08:13.4" ), "padAudio" : 0.1 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Warframe",\
"audio" : {"timestamps" : (nextTS(configs), "08:36.2" ), "padAudio" : 0.1 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Rainbow Six: Siege",\
"audio" : {"timestamps" : (nextTS(configs), "09:04.9" ), "padAudio" : 0.1 },\
"overlay" : { \
    "text" : ["'Rainbow Six\: Siege'",\
              scriptedvided.r6sText('1920x1080, low settings, 100% render scale', 51,  40), \
              scriptedvided.r6sText('1280x720, low settings, 100% render scale',  93,  65),\
              scriptedvided.r6sText('1920x1080, low settings, 50% render scale',  70,  41),\
              scriptedvided.r6sText('1280x720, low settings, 50% render scale',  121,  79)]\
}, \
})
####################### end of gaming section ###############################


####################### conclusion ###############################
configs["episodes"].append(\
{ "title": "Conclusions",\
"audio" : {"timestamps" : (nextTS(configs), "09:18.8" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : ""\
})

configs["episodes"].append(\
{ "title": "Dedicated feature videos",\
"isChapter" : False,\
"audio" : {"timestamps" : (nextTS(configs), "09:24.4" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : ""\
})


configs["episodes"].append(\
{ "title": "Card is old - breel",\
"isChapter" : False,\
"audio" : {"timestamps" : (nextTS(configs), "09:30.1" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : ""\
})

configs["episodes"].append(\
{ "title": "Card is old - games",\
"isChapter" : False,\
"audio" : {"timestamps" : (nextTS(configs), "09:39" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : ""\
})

configs["episodes"].append(\
{ "title": "not doom and gloom",\
"isChapter" : False,\
"audio" : {"timestamps" : (nextTS(configs), "09:46" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : ""\
})


configs["episodes"].append(\
{ "title": "bye",\
"isChapter" : False,\
"audio" : {"timestamps" : (nextTS(configs), "09:53" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : ""\
})


##configs["episodes"].append(\
##{ "title": "Blooper",\
##"isChapter" : False,\
##"audio" : {"timestamps" : ( "13:40.5", "14:04.2") },\
##"video" : {"file":"HiRezTrio-P_aladins_R_ealmRoyale_R_ogueCompany.mp4"}\
##})

#scriptedvided.makeVideoForEpisode(configs["episodes"][3], configs)
#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "Apex Legends"][0], configs)
scriptedvided.makeVideo(configs)

