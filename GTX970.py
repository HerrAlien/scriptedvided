import scriptedvided

configs = { "defaultAudioFile" : "GTX970.ogg",\
"mediaFolder" : "F:\\Videos\\GTX970", \
"stockFolder" : "F:\\Videos\\stock",\
"outputFolder" : "F:\\Videos\\GTX970\\output", \
"outputFile" : "GTX970.mp4", \
"benchmarkFile" : "F:\\Videos\\GTX970\\Benchmark_GTX970.txt",\
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#00800080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "I (heart) Maxwell", "until" : "Alien Isolation"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Alien Isolation", "until" : "Counter-Strike 2"}}, \
{"file" : "Inspired - MaikonMusic  Free Background Music  Audio Library Release.mp3", "timestamps" : ("00:00", None ), "destinationTimestamp" : {"title" : "Counter-Strike 2", "until" : "Overwatch 2"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Overwatch 2", "until" : "Again, (heart) Maxwell ..."}}, \
{"file" : "Guide You Home - Ferco and Andie - Free Background Music - Audio Library Release.ogg", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "Again, (heart) Maxwell ...", "until" : "Blooper"}}, \
], "volume" : 0.06 },\
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
"tags" : "AMD,Radeon,Polaris,GCN,GCN4,GCN 4,GTX970,RX 570,Sapphire,ITX",\
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
{ "title": "I (heart) Maxwell",\
"audio" : {"timestamps" : (lastTS, "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "breel_autumn_GTX970.mp4" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "The GM-204-200-A1 GPU",\
"audio" : {"timestamps" : (lastTS, "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : ""},\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "TDP",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : ""},\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Cooling and thermals",\
"audio" : {"timestamps" : (lastTS, "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : ""},\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Temps",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : ""},\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Dual BIOS card, single BIOS if you are not careful",\
"audio" : {"timestamps" : (lastTS, "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : ""},\
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
              scriptedvided.r6sText('1600x900, low settings' ,  ,  ),\
              scriptedvided.r6sText('1280x720, low settings' ,  ,  ),\
    ]\
}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Resident Evil 4 (Remake)",\
"audio" : {"timestamps" : (lastTS, "" ), "padAudio" : 0.1 },\
"overlay" : { \
    "text" : ["'Resident Evil 4 (Remake)'",\
              scriptedvided.r6sText('1920x1080, low settings',  ,   ),\
              scriptedvided.r6sText('1280x720, low settings',   ,   ),\
    ]\
}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Battlefield V",\
"audio" : {"timestamps" : (lastTS, "" ), "padAudio" : 0.1 },\
"overlay" : { \
    "image" : {"file" : "pay respects.png", "chromaColor" : "0x00FF00"}\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]


configs["episodes"].append(\
{ "title": "Doom Eternal",\
"audio" : {"timestamps" : (lastTS, "" ), "padAudio" : 0.1 },\
"overlay" : {  "benchmark" : { \
        "settings" : "1920x1080, high settings", \
}}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]



configs["episodes"].append(\
{ "title": "Control",\
"audio" : {"timestamps" : (lastTS, "" ), "padAudio" : 0.1 },\
"overlay" : { \
    "text" : ["'Control'",\
              scriptedvided.r6sText('1920x1080, low settings',  ,  ),\
              scriptedvided.r6sText('1280x720, low settings' ,  ,  ),]\
}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]


configs["episodes"].append(\
{ "title": "Rainbow Six: Siege",\
"audio" : {"timestamps" : (lastTS, "" ), "padAudio" : 0.1 },\
"overlay" : { \
    "text" : ["'Rainbow Six\: Siege'",\
              scriptedvided.r6sText('1920x1080, low settings, 100% render scale', , ), \
              scriptedvided.r6sText('1280x720, low settings, 100% render scale' , , ),\
              scriptedvided.r6sText('1920x1080, low settings, 50% render scale' , , ),\
              scriptedvided.r6sText('1280x720, low settings, 50% render scale'  , , )]\
}, \
})
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
              scriptedvided.r6sText('1920x1080, low settings, 100% render scale', , ),\
              scriptedvided.r6sText('1600x900, low settings, 100% render scale' , , ),\
              scriptedvided.r6sText('1280x720, low settings, 100% render scale' , , ),]\
}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]


configs["episodes"].append(\
{ "title": "Counter-Strike 2",\
"audio" : {"timestamps" : (lastTS, "" ), "padAudio" : 0.1 },\
"overlay" : { \
    "text" : ["'Counter-Strike 2'",\
              scriptedvided.r6sText('1920x1080, low settings', , ),\
              scriptedvided.r6sText('1600x900, low settings' , , ),\
              scriptedvided.r6sText('1280x720, low settings' , , ),]\
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
"audio" : {"timestamps" : (lastTS, "" ), "padAudio" : 0.1 },\
"overlay" : { \
    "text" : ["'Fortnite'",\
              scriptedvided.r6sText('1920x1080, performance mode', , ), \
              scriptedvided.r6sText('1600x900, performance mode' , , ),\
              scriptedvided.r6sText('1280x720, performance mode' , , )]\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Overwatch 2",\
"audio" : {"timestamps" : (lastTS, "" ), "padAudio" : 0.1 },\
"overlay" : { \
    "text" : ["'Overwatch 2'",\
              scriptedvided.r6sText('1920x1080, low settings', , ),\
              scriptedvided.r6sText('1600x900, low settings' , , ),\
              scriptedvided.r6sText('1280x720, low settings' , , ),]\
}, \
})
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
"overlay" : { \
    "text" : ["'Splitgate'",\
              scriptedvided.r6sText('1920x1080, low settings, 100% render scale', , ),\
              scriptedvided.r6sText('1280x720, low settings, 100% render scale' , , ),\
    ]\
}, \
})
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
{ "title": "Again, (heart) Maxwell ...",\
"audio" : {"timestamps" : (lastTS, "" ),  "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "But should you buy one?",\
"audio" : {"timestamps" : (lastTS, "" ),  "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

## might need a longer video file
configs["episodes"].append(\
{ "title": "When 4G is not 4G",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "" ),  "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "breel2",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "" ),  "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "peers",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "" ),  "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]


configs["episodes"].append(\
{ "title": "bye",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "" ),  "volume" : 0.999, "padAudio" : 0.1 },\
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