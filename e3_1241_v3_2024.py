import scriptedvided

configs = { "defaultAudioFile" : "e3_1241_v3_2024.ogg",\
"mediaFolder" : "F:\\Videos\\E3_1241_v3_2024", \
"stockFolder" : "F:\\Videos\\stock",\
"outputFolder" : "F:\\Videos\\E3_1241_v3_2024\\output", \
"outputFile" : "E3_1241_v3_2024.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#00008080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "Which one to pick", "until" : "Doom Eternal"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Doom Eternal", "until" : "Performance values (important)"}}, \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "Performance values (important)", "until" : "Conclusions"}}, \
{"file" : "Guide You Home - Ferco and Andie - Free Background Music - Audio Library Release.ogg", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "Conclusions", "until" : "Blooper"}}, \
], "volume" : 0.08 },\
"episodes" : [],\
"youtube" : {"title" : "How well do Intel 4th Gen CPUs run games today?", \
"description" : '''We'll be exploring how the 4th gen Intel core i7 and i5 equivalents run today.''',\
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
"tags" : "Haswell,Intel,i7 4770,i5 4570,e3 1241 v3,Spectre,Meltdown,Inspectre",\
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
{ "title": "4th gen, 4 core CPUs",\
"audio" : {"timestamps" : (lastTS, "00:12.4" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : ""},\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"](1)

configs["episodes"].append(\
{ "title": "BIOS and inspectre",\
"audio" : {"timestamps" : (lastTS, "00:24.8" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : ""},\
"isChapter" : False, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"](1)

# meeds better video, or maybe break it up
configs["episodes"].append(\
{ "title": "hint at games",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "00:37.6" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : ""},\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"](1)

#this is not the Z230
configs["episodes"].append(\
{ "title": "Test system and settings",\
"audio" : {"timestamps" : (lastTS, "00:54.3" ), "volume" : 0.999, "padAudio" : 0.1 },\
"overlay" : { \
    "text" : ["'Z230 workstation from HP'",\
              "'CPU\: E3-1241v3 Xeon (i7 4770 equivalent)'",\
              "'RAM\: 32GB DDR3 at 1600 MHz, dual channel'",\
    ]\
}, \
"video" : {"file" : "Z230_closed.mp4", "rotation" : 180}\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"](1)

configs["episodes"].append(\
{ "title": "More details on the 4 configurations",\
"audio" : {"timestamps" : (lastTS, "01:28" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : ""},\
"isChapter" : False, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"](1)


configs["episodes"].append(\
{ "title": "Apex Legends",\
"audio" : {"timestamps" : (lastTS, "01:56.7" ), "padAudio" : 0.1 },\
"overlay" : { \
    "image" : {"file" : "Apex Legends.png", "chromaColor" : "0x00FF00"}\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"](1)

configs["episodes"].append(\
{ "title": "Counter Strike 2",\
"audio" : {"timestamps" : (lastTS, "02:24" ), "padAudio" : 0.1 },\
"overlay" : { \
    "image" : {"file" : "Counter Strike 2.png", "chromaColor" : "0x00FF00"}\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"](1)

configs["episodes"].append(\
{ "title": "Rainbow Six: Siege",\
"audio" : {"timestamps" : (lastTS, "02:53.3" ), "padAudio" : 0.1 },\
"overlay" : { \
    "image" : {"file" : "Rainbow Six Siege.png", "chromaColor" : "0x00FF00"}\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"](1)

configs["episodes"].append(\
{ "title": "The Finals",\
"audio" : {"timestamps" : (lastTS, "03:18.7" ), "padAudio" : 0.1 },\
"video" : {"file" : "stock_Finals_2023_12_27_winners.mp4" , "start" : "02:37"},\
"overlay" : { \
    "image" : {"file" : "The Finals.png", "chromaColor" : "0x00FF00"}\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"](1)

configs["episodes"].append(\
{ "title": "Fortnite",\
"audio" : {"timestamps" : (lastTS, "03:46" ), "padAudio" : 0.1 },\
"video" : {"file" : "stock_FortniteClient-Win_2023_12_24.mp4", "start" : "08:40"},\
"overlay" : { \
    "image" : {"file" : "Fortnite.png", "chromaColor" : "0x00FF00"}\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"](1)

configs["episodes"].append(\
{ "title": "Valorant",\
"audio" : {"timestamps" : (lastTS, "04:13.4" ), "padAudio" : 0.1 },\
"overlay" : { \
    "image" : {"file" : "Valorant.png", "chromaColor" : "0x00FF00"}\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"](1)



configs["episodes"].append(\
{ "title": "Hyperthreading, average FPS and the 1 percent lows",\
"audio" : {"timestamps" : (lastTS, "04:48.9" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : ""},\
"overlay" : { \
    "image" : {"file" : "Total FPS.png", "chromaColor" : "0x00FF00"}\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"](1)

configs["episodes"].append(\
{ "title": "BIOS",\
"audio" : {"timestamps" : (lastTS, "05:00" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : ""},\
"isChapter" : False,\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"](1)

configs["episodes"].append(\
{ "title": "Disable security patches, or not",\
"audio" : {"timestamps" : (lastTS, "05:16.8" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : ""},\
"overlay" : { \
    "image" : {"file" : "Total FPS.png", "chromaColor" : "0x00FF00"}\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"](1)

configs["episodes"].append(\
{ "title": "Conclusions",\
"audio" : {"timestamps" : (lastTS, "05:25.2" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : ""},\
"isChapter" : False,\
})
lastTS = "05:37.8"

configs["episodes"].append(\
{ "title": "Bye",\
"audio" : {"timestamps" : (lastTS, "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : ""},\
"isChapter" : False,\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"](1)

#scriptedvided.makeVideoForEpisode(configs["episodes"][15], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][9], configs)
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