import scriptedvided

configs = { "defaultAudioFile" : "rx570.ogg",\
"mediaFolder" : "F:\\Videos\\rx570", \
"stockFolder" : "F:\\Videos\\stock",\
"outputFolder" : "F:\\Videos\\rx570\\output", \
"outputFile" : "rx570.mp4", \
"benchmarkFile" : "F:\\Videos\\rx570\\Benchmark_rx570.txt",\
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "Going full potato", "until" : "Alien Isolation"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Alien Isolation", "until" : "Counter-Strike 2"}}, \
{"file" : "Inspired - MaikonMusic  Free Background Music  Audio Library Release.mp3", "timestamps" : ("00:00", None ), "destinationTimestamp" : {"title" : "Counter-Strike 2", "until" : "Splitgate"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Splitgate", "until" : "After disabling SPECTRE and MELTDOWN patches"}}, \
{"file" : "Wait For Me  Jeff The Second (No Copyright Music).mp3", "timestamps" : ("00:35", None ), "destinationTimestamp" : {"title" : "After disabling SPECTRE and MELTDOWN patches", "until" : "Is it worth buying?"}}, \
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
{ "title": "Compact card",\
"audio" : {"timestamps" : (lastTS, "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "The Polaris GPU",\
"audio" : {"timestamps" : (lastTS, "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "TDP",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Cooling and thermals",\
"audio" : {"timestamps" : (lastTS, "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Temps",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "The test system",\
"audio" : {"timestamps" : (lastTS, "" ), "volume" : 0.999, "padAudio" : 0.1 },\
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
"audio" : {"timestamps" : (lastTS, "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]


#########################################


configs["episodes"].append(\
{ "title": "Alien Isolation",\
"audio" : {"timestamps" : (lastTS, "" ), "padAudio" : 0.1 },\
"overlay" : {  "benchmark" : { \
        "settings" : "1920x1080, ultra settings", \
}}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Apex Legends",\
"audio" : {"timestamps" : (lastTS, "" ), "padAudio" : 0.1 },\
"overlay" : { \
    "text" : ["'Apex Legends'",\
              scriptedvided.r6sText('1920x1080, low settings',  ,  ),\
              scriptedvided.r6sText('1600x900, low settings',  ,   ),\
              scriptedvided.r6sText('1280x720, low settings',  ,   ),\
    ]\
}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]


configs["episodes"].append(\
{ "title": "Resident Evil 4 (Remake)",\
"audio" : {"timestamps" : (lastTS, "" ), "padAudio" : 0.1 },\
"overlay" : {  "benchmark" : { \
        "settings" : "1920x1080, low settings", \
}}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Battlefield V",\
"audio" : {"timestamps" : (lastTS, "" ), "padAudio" : 0.1 },\
"video" : {"file" : "" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Battlefield V - results",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "" ), "padAudio" : 0.1 },\
"overlay" : {  "benchmark" : { \
        "settings" : "1920x1080, low settings", \
}}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Control",\
"audio" : {"timestamps" : (lastTS, "" ), "padAudio" : 0.1 },\
"video" : {"file" : "" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Control - results",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "" ), "padAudio" : 0.1 },\
"overlay" : { \
    "text" : ["'Control'",\
              scriptedvided.r6sText('1920x1080, low settings', , ),\
              scriptedvided.r6sText('1280x720, low settings', , ),\
    ]\
}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]


configs["episodes"].append(\
{ "title": "Rainbow Six: Siege",\
"audio" : {"timestamps" : (lastTS, "" ), "padAudio" : 0.1 },\
"video" : {"file" : "" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Rainbow Six: Siege - results",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "" ), "padAudio" : 0.1 },\
"overlay" : { \
    "text" : ["'Rainbow Six\: Siege'",\
              scriptedvided.r6sText('1920x1080, low settings, 100% render scale', , ), \
              scriptedvided.r6sText('1280x720, low settings, 100% render scale', , ),\
}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]


configs["episodes"].append(\
{ "title": "Grand Theft Auto V",\
"audio" : {"timestamps" : (lastTS, "" ), "padAudio" : 0.1 },\
"overlay" : {  "benchmark" : { \
        "settings" : "1920x1080, low settings", \
}}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]


configs["episodes"].append(\
{ "title": "The Finals",\
"audio" : {"timestamps" : (lastTS, "" ), "padAudio" : 0.1 },\
"overlay" : { \
    "text" : ["'The Finals'",\
              scriptedvided.r6sText('1920x1080, low settings, 100% render scale', , ), \
              scriptedvided.r6sText('1280x720, low settings, 100% render scale', , ),\
}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]


configs["episodes"].append(\
{ "title": "Counter-Strike 2",\
"audio" : {"timestamps" : (lastTS, "" ), "padAudio" : 0.1 },\
"overlay" : { \
    "text" : ["'Counter-Strike 2'",\
              scriptedvided.r6sText('1920x1080, low settings', , ),\
              scriptedvided.r6sText('1600x900, low settings', , ),\
              scriptedvided.r6sText('1280x720, low settings', ,  ),\
    ]\
}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "DOTA2",\
"audio" : {"timestamps" : (lastTS, "" ), "padAudio" : 0.1 },\
"overlay" : {  "benchmark" : { \
        "settings" : "1920x1080, low settings", \
}}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Fortnite",\
"audio" : {"timestamps" : (lastTS, "" ), "padAudio" : 0.1 },\
"overlay" : {  "benchmark" : { \
        "settings" : "1920x1080, performance mode, FAR render distance", \
}}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Overwatch 2",\
"audio" : {"timestamps" : (lastTS, "" ), "padAudio" : 0.1 },\
"video" : {"file" : "" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Overwatch 2 - results",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "" ), "padAudio" : 0.1 },\
"overlay" : {  "benchmark" : { \
        "settings" : "1920x1080, low settings", \
}}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]


configs["episodes"].append(\
{ "title": "Rocket League",\
"audio" : {"timestamps" : (lastTS, "" ), "padAudio" : 0.1 },\
"overlay" : {  "benchmark" : { \
        "settings" : "1920x1080, low settings, 100% render scale", \
}}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]


configs["episodes"].append(\
{ "title": "Splitgate",\
"audio" : {"timestamps" : (lastTS, "" ), "padAudio" : 0.1 },\
"video" : {"file" : "" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Splitgate - results",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "" ), "padAudio" : 0.1 },\
"overlay" : {  "benchmark" : { \
        "settings" : "1920x1080, low settings, 100% render scale", \
}}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Valorant",\
"audio" : {"timestamps" : (lastTS, "" ), "padAudio" : 0.1 },\
"overlay" : {  "benchmark" : { \
        "settings" : "1920x1080, low settings", \
}}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Paladins, Realm Royale and Rogue Company",\
"video" : {"file":"HiRezTrio-P_aladins_R_ealmRoyale_R_ogueCompany.mp4"},\
"audio" : {"timestamps" : (lastTS, "" ), "padAudio" : 0.1 },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Paladins",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "" ), "padAudio" : 0.1 },\
"overlay" : {  "benchmark" : { \
        "settings" : "1920x1080, high settings", \
}}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Realm Royale",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "" ), "padAudio" : 0.1 },\
"overlay" : {  "benchmark" : { \
        "settings" : "1920x1080, high settings", \
}}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Rogue Company",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "" ), "padAudio" : 0.1 },\
"overlay" : {  "benchmark" : { \
        "settings" : "1920x1080, low settings", \
}}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "World of Tanks Blitz",\
"audio" : {"timestamps" : (lastTS, "" ), "padAudio" : 0.1 },\
"overlay" : {  "benchmark" : { \
        "settings" : "1920x1080, low settings", \
}}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Warframe",\
"audio" : {"timestamps" : (lastTS, "" ), "padAudio" : 0.1 },\
"overlay" : {  "benchmark" : { \
        "settings" : "1920x1080, low settings", \
}}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]


##################################################################

configs["episodes"].append(\
{ "title": "Is it worth buying?",\
"audio" : {"timestamps" : (lastTS, "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "miner background",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

## might need a longer video file
configs["episodes"].append(\
{ "title": "Driver support is dwindling",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "matches the PSU",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]


configs["episodes"].append(\
{ "title": "bye",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "" },\
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