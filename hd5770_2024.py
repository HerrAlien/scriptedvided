import scriptedvided

configs = { "defaultAudioFile" : "hd5770_2024.ogg",\
"mediaFolder" : "F:\\Videos\\hd5770_2024", \
"stockFolder" : "F:\\Videos\\stock",\
"outputFolder" : "F:\\Videos\\hd5770_2024\\output", \
"outputFile" : "hd5770_2024.mp4", \
"benchmarkFile" : "",\
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "(lest) I forget", "until" : "Nope"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Nope", "until" : "DOTA2"}}, \
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
{ "title": "(lest) I forget",\
"audio" : {"timestamps" : (lastTS, "00:10.8" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "breel_gigabyte_hd5770_juniper.mp4" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]


configs["episodes"].append(\
{ "title": "No fullscreen",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "00:30.5" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "HD5770_Fallout4_windowed.mp4" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]


configs["episodes"].append(\
{ "title": "Juniper, but not the plant",\
"audio" : {"timestamps" : (lastTS, "00:42.5" ), "volume" : 0.999, "padAudio" : 0.1 },\
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
lastTS = "00:54"

configs["episodes"].append(\
{ "title": "Cooling and thermals",\
"audio" : {"timestamps" : (lastTS, "01:15" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "GigabyteHd5770Cooling.mp4" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Temps",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "01:27.3" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "Gigabyte_HD5770_HeavenGpuZ_phone.mp4" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "The brand old (!) Z230",\
"audio" : {"timestamps" : (lastTS, "01:44.6" ), "volume" : 0.999, "padAudio" : 0.1 },\
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
{ "title": "Nope",\
"audio" : {"timestamps" : (lastTS, "01:58.6" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "HD5770_Overwatch2.mkv", "start" : "00:21" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Fortnite",\
"audio" : {"timestamps" : (lastTS, "02:37" ), "padAudio" : 0.1 },\
"overlay" : { \
    "text" : ["'Fortnite, performance mode'",\
              scriptedvided.r6sText('1920x1080, borderless', 60, 36), \
              scriptedvided.r6sText('1280x720, windowed' , 86, 40)]\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]


configs["episodes"].append(\
{ "title": "Fallout 4",\
"audio" : {"timestamps" : (lastTS, "02:56.8" ), "padAudio" : 0.1 },\
"overlay" : { \
    "text" : ["'Fallout 4, low settings, windowed'",\
              scriptedvided.r6sText('1280x720, regular environment' , 48, 28),\
              scriptedvided.r6sText('1280x720, Diamond City' , 27, 25)]\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]


configs["episodes"].append(\
{ "title": "Prey",\
"audio" : {"timestamps" : (lastTS, "03:20.3" ), "padAudio" : 0.1 },\
"overlay" : { \
    "text" : ["'Prey'",\
              scriptedvided.r6sText('1920x1080, low settings', 32, 22), \
              scriptedvided.r6sText('1280x720, low settings' , 70, 44)]\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Grand Theft Auto V",\
"audio" : {"timestamps" : (lastTS, "03:48.8" ), "padAudio" : 0.1 },\
"overlay" : { \
    "text" : ["'Grand Theft Auto V'",\
              scriptedvided.r6sText('794x571 (wtf?), low settings', 94, 58)]\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Counter-Strike 2",\
"audio" : {"timestamps" : (lastTS, "04:10.9" ), "padAudio" : 0.1 },\
"overlay" : { \
    "text" : ["'Counter-Strike 2'",\
              scriptedvided.r6sText('1280x720, low settings' , 37, 20),\
              scriptedvided.r6sText('1280x720, low settings, FSR Quality' , 53, 27)]\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "DOTA2",\
"audio" : {"timestamps" : (lastTS, "04:34.6" ), "padAudio" : 0.1 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Rogue Company",\
"audio" : {"timestamps" : (lastTS, "04:52.7" ), "padAudio" : 0.1 },\
"overlay" : { \
    "text" : ["'Rogue Company'",\
              scriptedvided.r6sText('1920x1080, low settings' , 56, 20),\
              scriptedvided.r6sText('1280x720, low settings'  , 80, 53)]\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Rainbow Six: Siege",\
"audio" : {"timestamps" : (lastTS, "05:06.6" ), "padAudio" : 0.1 },\
"overlay" : { \
    "text" : ["'Rainbow Six\: Siege'",\
              scriptedvided.r6sText('1920x1080, low settings, 100% render scale', 22, 15), \
              scriptedvided.r6sText('1920x1080, low settings, 50% render scale' , 43, 24)]\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Splitgate",\
"audio" : {"timestamps" : (lastTS, "05:16.6" ), "padAudio" : 0.1 },\
"overlay" : { \
    "text" : ["'Splitgate'",\
              scriptedvided.r6sText('1920x1080, low settings, 100% render scale', 40, 29), \
              scriptedvided.r6sText('1920x1080, low settings, 50% render scale' , 56, 40)]\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Valorant",\
"audio" : {"timestamps" : (lastTS, "05:34.5" ), "padAudio" : 0.1 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Warframe",\
"audio" : {"timestamps" : (lastTS, "05:48.3" ), "padAudio" : 0.1 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "World of Tanks Blitz",\
"audio" : {"timestamps" : (lastTS, "06:11.7" ), "padAudio" : 0.1 },\
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
"audio" : {"timestamps" : (lastTS, "06:25.7" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "HD5770_Fallout4_windowed.mp4" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Still, they worked again a year ago",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "06:35.9" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Nimez",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "06:44.8" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "HD5770_nimez.mkv" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Not cheap enough",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "07:08.9" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "olx_5770_7770.mkv", "start" : "00:55" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Not the sunset I had in mind",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "07:25.4" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "HD5770_P_rey_issues.mp4" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]


configs["episodes"].append(\
{ "title": "Sentimental values",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "07:40.7" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "HD5770_both_breel.mp4" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Bye",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "07:48.7" ), "volume" : 0.999, "padAudio" : 0.1 },\
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
#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "Alien Isolation"][0], configs)
#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "actual 1080 results"][0], configs)
#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "actual 900 results"][0], configs)
#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "actual 720 results"][0], configs)
#print (scriptedvided.getSuitableImage([x for x in configs["episodes"] if x["title"] == "actual 1080 results"][0], configs))

scriptedvided.makeVideo(configs)

# meeds better video, or maybe break it up