import scriptedvided

configs = { "defaultAudioFile" : "hd5770_2024_v2.ogg",\
"mediaFolder" : "F:\\Videos\\hd5770_2024", \
"stockFolder" : "F:\\Videos\\stock",\
"outputFolder" : "F:\\Videos\\hd5770_2024\\output", \
"outputFile" : "hd5770_2024.mp4", \
"benchmarkFile" : "F:\\Videos\\hd5770_2024\\Benchmark_HD5770_2024.txt",\
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "A feeling of deja vu", "until" : "Apex Legends"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Apex Legends", "until" : "DOTA2"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "DOTA2", "until" : "Conclusions"}}, \
{"file" : "Inspired - MaikonMusic  Free Background Music  Audio Library Release.mp3", "timestamps" : ("00:00", None ), "destinationTimestamp" : {"title" : "Conclusions", "until" : "EOF"}}, \
], "volume" : 0.045 },\
"episodes" : [],\
"youtube" : {"title" : "  ...  ... ", \
"description" : '''In this one we're testing the 4(?)GB GTX 970 using some games from today.''',\
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
"tags" : "NVidia,GeForce,GTX,GTX970,GTX 970,Maxwell,Maxwell 2.0,AMD,Radeon,GCN,Polaris,R9 290X,RX570,RX 570",\
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

lastTS = "00:00"
configs["episodes"].append(\
{ "title": "A feeling of deja vu",\
"audio" : {"timestamps" : (lastTS, "00:20" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "breel_gigabyte_hd5770_juniper.mp4" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Juniper, but not the plant",\
"audio" : {"timestamps" : (lastTS, "00:31.9" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "Gigabyte_HD5770_GpuZ_phone.mp4" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

##needs overlay
#configs["episodes"].append(\
#{ "title": "Games added, games removed",\
#"isChapter" : False, \
#"audio" : {"timestamps" : (lastTS, "00:54" ), "volume" : 0.999, "padAudio" : 0.1 },\
#"video" : {"file" : "Gigabyte_HD5770_GpuZ_phone.mp4" },\
#})
#lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Cooling and thermals",\
"audio" : {"timestamps" : (lastTS, "00:53" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "GigabyteHd5770Cooling.mp4" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Temps",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "01:05" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "Gigabyte_HD5770_HeavenGpuZ_phone.mp4" },\
"overlay" : { \
    "text" : ["'Thermals'",\
              "'Heaven\: 63C (38C delta over ambient)'",\
    ]\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "The brand old (!) Z230",\
"audio" : {"timestamps" : (lastTS, "01:22.6" ), "volume" : 0.999, "padAudio" : 0.1 },\
"overlay" : { \
    "text" : ["'Z230 workstation from HP'",\
              "'CPU\: E3-1241v3 Xeon (i7 4770 equivalent)'",\
              "'RAM\: 32GB DDR3 at 1600 MHz, dual channel'",\
    ]\
}, \
"video" : {"file" : "Z230_closed.mp4", "rotation" : 180}\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

#########################################

# ===========================================================================
configs["episodes"].append(\
{ "title": "Apex Legends",\
"audio" : {"timestamps" : (lastTS, "01:55.1" ), "volume" : 0.999, "padAudio" : 0.1 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Fortnite",\
"audio" : {"timestamps" : (lastTS, "02:27" ), "padAudio" : 0.1 },\
"overlay" : { \
    "text" : ["'Fortnite, performance mode'",\
              scriptedvided.r6sText('1920x1080, borderless', 60, 36), \
              scriptedvided.r6sText('1280x720, windowed' , 86, 40)]\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]


configs["episodes"].append(\
{ "title": "Fallout 4",\
"audio" : {"timestamps" : (lastTS, "02:43.7" ), "padAudio" : 0.1 },\
"overlay" : { \
    "text" : ["'Fallout 4, low settings, windowed'",\
              scriptedvided.r6sText('1280x720, regular environment' , 48, 28),\
              scriptedvided.r6sText('1280x720, Diamond City' , 27, 25)]\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]


configs["episodes"].append(\
{ "title": "Prey",\
"audio" : {"timestamps" : (lastTS, "03:03.7" ), "padAudio" : 0.1 },\
"overlay" : { \
    "text" : ["'Prey'",\
              scriptedvided.r6sText('1920x1080, low settings', 32, 22), \
              scriptedvided.r6sText('1280x720, low settings' , 70, 44)]\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Grand Theft Auto V",\
"audio" : {"timestamps" : (lastTS, "03:36.2" ), "padAudio" : 0.1 },\
"overlay" : { \
    "text" : ["'Grand Theft Auto V'",\
              scriptedvided.r6sText('1920x1080, low settings', 48, 32),\
              scriptedvided.r6sText('794x571 (wtf?), low settings', 94, 58)]\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Counter-Strike 2",\
"audio" : {"timestamps" : (lastTS, "03:54.6" ), "padAudio" : 0.1 },\
"overlay" : { \
    "text" : ["'Counter-Strike 2'",\
              scriptedvided.r6sText('1280x720, low settings' , 37, 20),\
              scriptedvided.r6sText('1280x720, low settings, FSR Quality' , 53, 27)]\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "DOTA2",\
"audio" : {"timestamps" : (lastTS, "04:16.5" ), "padAudio" : 0.1 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]


configs["episodes"].append(\
{ "title": "HiRez Studios trio (Paladins, Realm Royale, Rogue Company)",\
"audio" : {"timestamps" : (lastTS, "04:22.8" ), "volume" : 0.999 , "padding" : 0.25  },\
"video" : {"file":"HiRezTrio-P_aladins_R_ealmRoyale_R_ogueCompany.mp4"}\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Paladins",\
"isChapter" : False,\
"audio" : {"timestamps" : (lastTS, "04:29.4" ), "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, high settings", \
    }\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Realm Royale",\
"isChapter" : False,\
"audio" : {"timestamps" : (lastTS, "04:40.45" ), "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, high settings", \
    }\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Rogue Company",\
"isChapter" : False,\
"audio" : {"timestamps" : (lastTS, "04:48.2" ), "padding" : 0.25  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]


configs["episodes"].append(\
{ "title": "Rainbow Six: Siege",\
"audio" : {"timestamps" : (lastTS, "05:01.9" ), "padAudio" : 0.1 },\
"overlay" : { \
    "text" : ["'Rainbow Six\: Siege'",\
              scriptedvided.r6sText('1920x1080, low settings, 100% render scale', 22, 15), \
              scriptedvided.r6sText('1920x1080, low settings, 50% render scale' , 43, 24)]\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Splitgate",\
"audio" : {"timestamps" : (lastTS, "05:12" ), "padAudio" : 0.1 },\
"overlay" : { \
    "text" : ["'Splitgate'",\
              scriptedvided.r6sText('1920x1080, low settings, 100% render scale', 40, 29), \
              scriptedvided.r6sText('1920x1080, low settings, 50% render scale' , 56, 40)]\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Valorant",\
"audio" : {"timestamps" : (lastTS, "05:29.5" ), "padAudio" : 0.1 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Warframe",\
"audio" : {"timestamps" : (lastTS, "05:44.6" ), "padAudio" : 0.1 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "World of Tanks Blitz",\
"audio" : {"timestamps" : (lastTS, "06:08.3" ), "padAudio" : 0.1 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]


# average FPS
configs["episodes"].append(\
{ "title": "Conclusions",\
"audio" : {"timestamps" : (lastTS, "06:16.6" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "HD5770_F_allout4_windowed.mp4" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "full screen troubles",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "06:31.4" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "HD5770_O_verwatch2.mkv" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Fix",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "06:54.2" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "TS2_fix_FS.mkv" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Games updated",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "07:13" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "stock_F_ortnite_performance.mp4" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]


configs["episodes"].append(\
{ "title": "Not cheap enough",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "07:37" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "olx_5770_7770.mkv", "start" : "00:55" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Not the sunset I had in mind",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "07:53.4" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "HD5770_P_rey_issues.mp4" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]


configs["episodes"].append(\
{ "title": "Sentimental values",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "08:13" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "HD5770_both_breel.mp4" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Bye",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "08:20.9" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "Gigabyte_HD5770_breel.mp4" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]



#scriptedvided.makeVideoForEpisode(configs["episodes"][1], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][4], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][11], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][12], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][13], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][8], configs)
#print(scriptedvided.makeVideoForEpisode(configs["episodes"][9], configs))
#print(scriptedvided.getSuitableVideoStream(configs["episodes"][9], configs))
#print (configs["youtube"])
#print(scriptedvided.getMusicCreditsString(configs["backgroundTrack"]))
#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "DOTA2"][0], configs)
#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "actual 1080 results"][0], configs)
#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "actual 900 results"][0], configs)
#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "actual 720 results"][0], configs)
#print (scriptedvided.getSuitableImage([x for x in configs["episodes"] if x["title"] == "actual 1080 results"][0], configs))

scriptedvided.makeVideo(configs)

# meeds better video, or maybe break it up