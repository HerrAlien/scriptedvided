import scriptedvided

configs = { "defaultAudioFile" : "i5_2400.ogg",\
"mediaFolder" : "F:\\Videos\\i5_2400", \
"stockFolder" : "F:\\Videos\\stock",\
"outputFolder" : "F:\\Videos\\i5_2400\\output", \
"outputFile" : "i5_2400.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#00008080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "4th gen, 4 core CPUs", "until" : "Apex Legends"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Apex Legends", "until" : "Hyperthreading, average FPS and the 1 percent lows"}}, \
{"file" : "Guide You Home - Ferco and Andie - Free Background Music - Audio Library Release.ogg", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "Hyperthreading, average FPS and the 1 percent lows", "until" : "Blooper"}}, \
], "volume" : 0.06 },\
"episodes" : [],\
"youtube" : {"title" : "Single digit USD price CPU in 2024 (i5 2400)", \
"description" : '''We'll be exploring how the 2nd gen Intel core i5 2400 run today.''',\
"links" : '''
Track: Bliss Of Heaven - SOMM [Audio Library Release]
Music provided by Audio Library Plus
Watch: https://www.youtube.com/watch?v=JQ6mKeQLZak&t=0s
Free Download / Stream: https://alplus.io/blisss-heaven

Track: Far Far Away - Ferco [Audio Library Release]
Music provided by Audio Library Plus
Watch: https://www.youtube.com/watch?v=SrkQ3K1umlc&t=0s 
Free Download / Stream: https://alplus.io/far-far-away

Track: Guide You Home - Ferco & Andie [Audio Library Release]
Music provided by Audio Library Plus
Watch: https://www.youtube.com/watch?v=16eNerPDIsU&t=0s
Free Download / Stream: https://alplus.io/guide-you-home

''', \
"tags" : "Sandy Bridge,Intel,i5 2400,Spectre,Meltdown,Inspectre",\
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
{ "title": "Going full potato",\
"audio" : {"timestamps" : (lastTS, "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "The test platform",\
"audio" : {"timestamps" : (lastTS, "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "The i5 2400",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Downloading extra performance with Inspectre",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "System RAM",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "GPU",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "shot with the case",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Drake meme with the PSUs",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Game settings",\
"audio" : {"timestamps" : (lastTS, "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]


configs["episodes"].append(\
{ "title": "Alien Isolation",\
"audio" : {"timestamps" : (lastTS, "" ), "padAudio" : 0.1 },\
"overlay" : {  "benchmark" : { \
        "settings" : "1280x720, low settings", \
}}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Grand Theft Auto V",\
"audio" : {"timestamps" : (lastTS, "" ), "padAudio" : 0.1 },\
"overlay" : {  "benchmark" : { \
        "settings" : "1280x720, low settings", \
}}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Control",\
"audio" : {"timestamps" : (lastTS, "" ), "padAudio" : 0.1 },\
"overlay" : {  "benchmark" : { \
        "settings" : "1280x720, low settings", \
}}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Resident Evil 4 (Remake)",\
"audio" : {"timestamps" : (lastTS, "" ), "padAudio" : 0.1 },\
"overlay" : {  "benchmark" : { \
        "settings" : "1280x720, 50% render scale, low settings", \
}}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Warframe",\
"audio" : {"timestamps" : (lastTS, "" ), "padAudio" : 0.1 },\
"overlay" : {  "benchmark" : { \
        "settings" : "1280x720, low settings", \
}}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Battlefield V",\
"audio" : {"timestamps" : (lastTS, "" ), "padAudio" : 0.1 },\
"overlay" : {  "benchmark" : { \
        "settings" : "1280x720, 50% render scale, low settings", \
}}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Apex Legends",\
"audio" : {"timestamps" : (lastTS, "" ), "padAudio" : 0.1 },\
"overlay" : { "image" : {"file" : "Apex Legends.png", "chromaColor" : "0x00FF00"}\
}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Fortnite",\
"audio" : {"timestamps" : (lastTS, "" ), "padAudio" : 0.1 },\
"overlay" : {  "benchmark" : { \
        "settings" : "1280x720, 30% 3D scale, FAR render distance, performance mode", \
}}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Rocket League",\
"audio" : {"timestamps" : (lastTS, "" ), "padAudio" : 0.1 },\
"overlay" : {  "benchmark" : { \
        "settings" : "1280x720, low settings", \
}}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "The Finals",\
"audio" : {"timestamps" : (lastTS, "" ), "padAudio" : 0.1 },\
"overlay" : { "image" : {"file" : "The Finals.png", "chromaColor" : "0x00FF00"}\
}})

lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Rainbow Six: Siege",\
"audio" : {"timestamps" : (lastTS, "" ), "padAudio" : 0.1 },\
"overlay" : { "image" : {"file" : "Rainbow Six Siege.png", "chromaColor" : "0x00FF00"}\
}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Counter-Strike 2",\
"audio" : {"timestamps" : (lastTS, "" ), "padAudio" : 0.1 },\
"overlay" : { "image" : {"file" : "Counter Strike 2.png", "chromaColor" : "0x00FF00"}\
}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Valorant",\
"audio" : {"timestamps" : (lastTS, "" ), "padAudio" : 0.1 },\
"overlay" : { "image" : {"file" : "Valorant.png", "chromaColor" : "0x00FF00"}\
}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "DOTA2",\
"audio" : {"timestamps" : (lastTS, "" ), "padAudio" : 0.1 },\
"overlay" : {  "benchmark" : { \
        "settings" : "1280x720, low settings", \
}}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Overwatch 2",\
"audio" : {"timestamps" : (lastTS, "" ), "padAudio" : 0.1 },\
"overlay" : {  "benchmark" : { \
        "settings" : "1280x720, low settings", \
}}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Paladins, Realm Royale and Rogue Company",\
"audio" : {"timestamps" : (lastTS, "" ), "padAudio" : 0.1 },\
"overlay" : {  "benchmark" : { \
        "settings" : "1280x720, low settings", \
}}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Paladins",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "" ), "padAudio" : 0.1 },\
"overlay" : {  "benchmark" : { \
        "settings" : "1280x720, low settings", \
}}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Realm Royale",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "" ), "padAudio" : 0.1 },\
"overlay" : {  "benchmark" : { \
        "settings" : "1280x720, low settings", \
}}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Rogue Company",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "" ), "padAudio" : 0.1 },\
"overlay" : {  "benchmark" : { \
        "settings" : "1280x720, low settings", \
}}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Splitgate",\
"audio" : {"timestamps" : (lastTS, "" ), "padAudio" : 0.1 },\
"overlay" : { \
    "text" : ["'Splitgate'",\
              scriptedvided.r6sText('1280x720, low settings, 100% render scale', 220,  42),\
              scriptedvided.r6sText('1280x720, low settings, 50% render scale', 229,  51),\
    ]\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "World of Tanks Blitz",\
"audio" : {"timestamps" : (lastTS, "" ), "padAudio" : 0.1 },\
"overlay" : {  "benchmark" : { \
        "settings" : "1280x720, low settings", \
}}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]


configs["episodes"].append(\
{ "title": "After disabling SPECTRE and MELTDOWN patches",\
"audio" : {"timestamps" : (lastTS, "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Fortnite",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "" ), "padAudio" : 0.1 },\
"overlay" : { "image" : {"file" : "Fortnite_inspectre.png", "chromaColor" : "0x00FF00"}\
}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]


configs["episodes"].append(\
{ "title": "Rainbow Six: Siege",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "" ), "padAudio" : 0.1 },\
"overlay" : { "image" : {"file" : "Rainbow Six Siege_inspectre.png", "chromaColor" : "0x00FF00"}\
}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Apex Legends",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "" ), "padAudio" : 0.1 },\
"overlay" : { "image" : {"file" : "Apex Legends_inspectre.png", "chromaColor" : "0x00FF00"}\
}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Valorant",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "" ), "padAudio" : 0.1 },\
"overlay" : { "image" : {"file" : "Valorant_inspectre.png", "chromaColor" : "0x00FF00"}\
}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Counter-Strike 2",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "" ), "padAudio" : 0.1 },\
"overlay" : { "image" : {"file" : "Counter Strike 2_inspectre.png", "chromaColor" : "0x00FF00"}\
}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Is it worth buying?",\
"audio" : {"timestamps" : (lastTS, "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "very cheap - price",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Comparison to Haswell",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "" },\
"overlay" : { "image" : {"file" : "MORE_THAN_FREQUENCIES.png", "chromaColor" : "0x00FF00"}\
}})
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
#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "Usefulness of the HD 6850"][0], configs)
#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "actual 1080 results"][0], configs)
#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "actual 900 results"][0], configs)
#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "actual 720 results"][0], configs)
#print (scriptedvided.getSuitableImage([x for x in configs["episodes"] if x["title"] == "actual 1080 results"][0], configs))

scriptedvided.makeVideo(configs)

# meeds better video, or maybe break it up