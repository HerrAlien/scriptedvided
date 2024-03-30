import scriptedvided

configs = { "defaultAudioFile" : "rx570.ogg",\
"mediaFolder" : "F:\\Videos\\rx570", \
"stockFolder" : "F:\\Videos\\stock",\
"outputFolder" : "F:\\Videos\\rx570\\output", \
"outputFile" : "rx570.mp4", \
"benchmarkFile" : "F:\\Videos\\rx570\\Benchmark_rx570.txt",\
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "A (mighty) compact card", "until" : "Alien Isolation"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Alien Isolation", "until" : "The Finals"}}, \
{"file" : "Inspired - MaikonMusic  Free Background Music  Audio Library Release.mp3", "timestamps" : ("00:00", None ), "destinationTimestamp" : {"title" : "The Finals", "until" : "Rocket League"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Rocket League", "until" : "Worth buying"}}, \
{"file" : "Guide You Home - Ferco and Andie - Free Background Music - Audio Library Release.ogg", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "Is it worth buying?", "until" : "Blooper"}}, \
], "volume" : 0.06 },\
"episodes" : [],\
"youtube" : {"title" : "  ...  ... ", \
"description" : '''In this one we're testing the 4 GB AMD Radeon RX 570  using some games from today.''',\
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

Wait For Me - Jeff The Second  https://www.youtube.com/watch?v=YuBBSQI2XDQ&t=0s
Creative Commons Attribution
Free Download / Stream: https://bit.ly/3LLKFj0
Music promoted by Audio Library   
https://www.youtube.com/watch?v=YuBBSQI2XDQ&t=0s

Track: Guide You Home - Ferco & Andie [Audio Library Release]
Music provided by Audio Library Plus
Watch: https://www.youtube.com/watch?v=16eNerPDIsU&t=0s
Free Download / Stream: https://alplus.io/guide-you-home

''', \
"tags" : "AMD,Radeon,Polaris,GCN,GCN4,GCN 4,RX570,RX 570,Sapphire,ITX",\
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
{ "title": "A (mighty) compact card",\
"audio" : {"timestamps" : (lastTS, "00:12.6" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "breel_autumn_RX570.mp4" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "The Polaris GPU",\
"audio" : {"timestamps" : (lastTS, "00:39.24" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "RX570_GPUZ_Heaven.mp4", "start" : "00:00"},\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "TDP",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "00:50.9" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "RX570_TDP_TechPowerup.mkv" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Cooling and thermals",\
"audio" : {"timestamps" : (lastTS, "01:12" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "rx570_itx_cooling.mp4" , "start" : "00:16" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Temps",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "01:37.3" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "RX570_GPUZ_Heaven.mp4", "start" : "00:50"},\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "The test system",\
"audio" : {"timestamps" : (lastTS, "01:51.5" ), "volume" : 0.999, "padAudio" : 0.1 },\
"overlay" : { \
    "text" : ["'Z230 workstation from HP'",\
              "'CPU\: E3-1241v3 Xeon (i7 4770 equivalent)'",\
              "'RAM\: 32GB DDR3 at 1600 MHz, dual channel'",\
    ]\
}, \
"video" : {"file" : "Z230_closed.mp4", "rotation" : 180}\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "CPU bottlenecks",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "01:59.8" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "CPU_bound_R_six_S_720.mp4" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]


#########################################


configs["episodes"].append(\
{ "title": "Alien Isolation",\
"audio" : {"timestamps" : (lastTS, "02:24" ), "padAudio" : 0.1 },\
"overlay" : {  "benchmark" : { \
        "settings" : "1920x1080, ultra settings", \
}}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Apex Legends",\
"audio" : {"timestamps" : ("11:02.6", "11:38.8" ), "padAudio" : 0.1 },\
"overlay" : { \
    "text" : ["'Apex Legends'",\
              scriptedvided.r6sText('1920x1080, low settings', 155 , 110 ),\
              scriptedvided.r6sText('1600x900, low settings', 189 , 132  ),\
              scriptedvided.r6sText('1280x720, low settings', 220 , 134 ),\
    ]\
}})
# do not reassign here lastTS, going out of order for Apex

configs["episodes"].append(\
{ "title": "Resident Evil 4 (Remake)",\
"audio" : {"timestamps" : (lastTS, "02:34.7" ), "padAudio" : 0.1 },\
"overlay" : {  "benchmark" : { \
        "settings" : "1920x1080, low settings", \
}}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Battlefield V",\
"audio" : {"timestamps" : (lastTS, "02:53.8" ), "padAudio" : 0.1 },\
"video" : {"file" : "CPU_bound_B_F_V.mp4" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Battlefield V - results",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "03:09" ), "padAudio" : 0.1 },\
"overlay" : {  "benchmark" : { \
        "settings" : "1920x1080, low settings", \
}}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Control",\
"audio" : {"timestamps" : (lastTS, "03:14.5" ), "padAudio" : 0.1 },\
"video" : {"file" : "CPU_bound_C_ontrol.mp4" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Control - results",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "03:38.5" ), "padAudio" : 0.1 },\
"overlay" : { \
    "text" : ["'Control'",\
              scriptedvided.r6sText('1920x1080, low settings', 99, 58),\
              scriptedvided.r6sText('1280x720, low settings', 148, 64),\
    ]\
}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]


configs["episodes"].append(\
{ "title": "Rainbow Six: Siege",\
"audio" : {"timestamps" : (lastTS, "03:44" ), "padAudio" : 0.1 },\
"video" : {"file" : "CPU_bound_R_six_S_720.mp4" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Rainbow Six: Siege - results",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "04:08.5" ), "padAudio" : 0.1 },\
"overlay" : { \
    "text" : ["'Rainbow Six\: Siege'",\
              scriptedvided.r6sText('1920x1080, low settings, 100% render scale',177 ,114), \
              scriptedvided.r6sText('1280x720, low settings, 100% render scale',208, 127),\
}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]


configs["episodes"].append(\
{ "title": "Grand Theft Auto V",\
"audio" : {"timestamps" : (lastTS, "04:25.3" ), "padAudio" : 0.1 },\
"overlay" : {  "benchmark" : { \
        "settings" : "1920x1080, low settings", \
}}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]


configs["episodes"].append(\
{ "title": "The Finals",\
"audio" : {"timestamps" : (lastTS, "04:55" ), "padAudio" : 0.1 },\
"overlay" : { \
    "text" : ["'The Finals'",\
              scriptedvided.r6sText('1920x1080, low settings, 100% render scale',60 ,21 ), \
              scriptedvided.r6sText('1280x720, low settings, 100% render scale',54 , 16),\
}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]


configs["episodes"].append(\
{ "title": "Counter-Strike 2",\
"audio" : {"timestamps" : (lastTS, "05:19.5" ), "padAudio" : 0.1 },\
"overlay" : { \
    "text" : ["'Counter-Strike 2'",\
              scriptedvided.r6sText('1920x1080, low settings', 132, 78),\
              scriptedvided.r6sText('1600x900, low settings',147,83 ),\
              scriptedvided.r6sText('1280x720, low settings',160 , 90 ),\
    ]\
}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "DOTA2",\
"audio" : {"timestamps" : (lastTS, "05:40.6" ), "padAudio" : 0.1 },\
"overlay" : {  "benchmark" : { \
        "settings" : "1920x1080, low settings", \
}}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Fortnite",\
"audio" : {"timestamps" : (lastTS, "06:15" ), "padAudio" : 0.1 },\
"overlay" : {  "benchmark" : { \
        "settings" : "1920x1080, performance mode, FAR render distance", \
}}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Overwatch 2",\
"audio" : {"timestamps" : (lastTS, "06:22.6" ), "padAudio" : 0.1 },\
"video" : {"file" : "CPU_bound_Over_Watch_2.mp4" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Overwatch 2 - results",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "07:08.4" ), "padAudio" : 0.1 },\
"overlay" : {  "benchmark" : { \
        "settings" : "1920x1080, low settings", \
}}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]


configs["episodes"].append(\
{ "title": "Rocket League",\
"audio" : {"timestamps" : (lastTS, "07:35.3" ), "padAudio" : 0.1 },\
"overlay" : {  "benchmark" : { \
        "settings" : "1920x1080, low settings, 100% render scale", \
}}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]


configs["episodes"].append(\
{ "title": "Splitgate",\
"audio" : {"timestamps" : (lastTS, "07:44.7" ), "padAudio" : 0.1 },\
"video" : {"file" : "CPU_bound_Split_Gate.mp4" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Splitgate - results",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "07:57.1" ), "padAudio" : 0.1 },\
"overlay" : {  "benchmark" : { \
        "settings" : "1920x1080, low settings, 100% render scale", \
}}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Valorant",\
"audio" : {"timestamps" : (lastTS, "08:28.7" ), "padAudio" : 0.1 },\
"overlay" : {  "benchmark" : { \
        "settings" : "1920x1080, low settings", \
}}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Paladins, Realm Royale and Rogue Company",\
"video" : {"file":"HiRezTrio-P_aladins_R_ealmRoyale_R_ogueCompany.mp4"},\
"audio" : {"timestamps" : (lastTS, "08:42.6" ), "padAudio" : 0.1 },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Paladins",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "08:50" ), "padAudio" : 0.1 },\
"overlay" : {  "benchmark" : { \
        "settings" : "1920x1080, high settings", \
}}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Realm Royale",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "08:59.4" ), "padAudio" : 0.1 },\
"overlay" : {  "benchmark" : { \
        "settings" : "1920x1080, high settings", \
}}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Rogue Company",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "09:08.4" ), "padAudio" : 0.1 },\
"overlay" : {  "benchmark" : { \
        "settings" : "1920x1080, low settings", \
}}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "World of Tanks Blitz",\
"audio" : {"timestamps" : (lastTS, "09:24.2" ), "padAudio" : 0.1 },\
"overlay" : {  "benchmark" : { \
        "settings" : "1920x1080, low settings", \
}}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Warframe",\
"audio" : {"timestamps" : (lastTS, "09:47.6" ), "padAudio" : 0.1 },\
"overlay" : {  "benchmark" : { \
        "settings" : "1920x1080, low settings", \
}}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]


##################################################################

configs["episodes"].append(\
{ "title": "Is it worth buying?",\
"audio" : {"timestamps" : (lastTS, "09:57.5" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "RX570_olx.mkv" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "miner background",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "10:14.6" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "rx570_mined.mkv" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

## might need a longer video file
configs["episodes"].append(\
{ "title": "Driver support is dwindling",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "10:29.1" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "anandtech_GCN4_5_support.mkv" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "breel2",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "10:47.5" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "breel_autumn_RX570.mp4" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "matches the PSU",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "10:55.2" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "Z230_PSU.mp4" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]


configs["episodes"].append(\
{ "title": "bye",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "11:02" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "breel_autumn_RX570.mp4" },\
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