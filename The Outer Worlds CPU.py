import scriptedvided

configs = { "defaultAudioFile" : "TOW CPUs.ogg",\
"mediaFolder" : "F:\\Videos\\TheOuterWorlds_CPUs", \
"stockFolder" : "F:\\Videos\\stock",\
"outputFolder" : "F:\\Videos\\TheOuterWorlds_CPUs\\output", \
"outputFile" : "The Outer Worlds CPUs.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#00008080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "The game is free until Apr 11", "until" : "Out of the box results"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Out of the box results", "until" : "Conclusions"}}, \
{"file" : "Inspired - MaikonMusic  Free Background Music  Audio Library Release.mp3", "timestamps" : ("00:00", None ), "destinationTimestamp" : {"title" : "Conclusions", "until" : "EOF"}}, \
], "volume" : 0.06 },\
"episodes" : [],\
"youtube" : {"title" : " ", \
"description" : ''' ''',\
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
"tags" : "The Outer Worlds,Intel,E3-1241v3,Haswell,Sandy Bridge,4th gen,2nd gen,core i5,i5,core i7,i7,i5 2400,i5 4570,i7 4770,Inspectre,Spectre,Meltdown",\
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

# gameplay
lastTS = "00:00"
configs["episodes"].append(\
{ "title": "The game is free until Apr 11",\
"audio" : {"timestamps" : (lastTS, "00:11.1" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "IndianaEpicGameStore-Win64-Shipping_2024_03_31_07_58_52_988-converted.mp4"},\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

#"isChapter" : False, \
configs["episodes"].append(\
{ "title": "The CPUs",\
"audio" : {"timestamps" : (lastTS, "00:21.5" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "Z230_closed.mp4", "rotation" : 180}\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "INSPECTRE",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "00:40.4" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "inspectre_off.mp4" , "start" : "00:00" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "emmulate i5",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "00:55.7" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "HyperThreading.mkv"},\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "i52400",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "01:14.75" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "breel_SandyBridge_outside.mp4" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]


#"isChapter" : False, \
# website screenshot
configs["episodes"].append(\
{ "title": "Settings",\
"audio" : {"timestamps" : (lastTS, "01:24" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "IndianaEpicGameStore-Win64-Shipping_2024_03_31_17_17_58_163-converted.mp4"},\
"overlay" : { \
    "image" : {"file" : "six_configs.png", "chromaColor" : "0x00FF00"}\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Out of the box results",\
"audio" : {"timestamps" : (lastTS, "01:55.8" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "IndianaEpicGameStore-Win64-Shipping_2024_03_31_17_22_41_226-converted.mp4"},\
"overlay" : { \
    "image" : {"file" : "SAFE.png", "chromaColor" : "0x00FF00"}\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Turning off security patches",\
"audio" : {"timestamps" : (lastTS, "02:29.7" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "IndianaEpicGameStore-Win64-Shipping_2024_03_31_17_22_41_226-converted.mp4"},\
"overlay" : { \
    "image" : {"file" : "UNSAFE.png", "chromaColor" : "0x00FF00"}\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Conclusions",\
"audio" : {"timestamps" : (lastTS, "02:58.7" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "HyperThreading.mkv", "start" : "00:45"},\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "bye",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "03:13.8" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "IndianaEpicGameStore-Win64-Shipping_2024_03_31_07_58_52_988-converted.mp4"},\
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