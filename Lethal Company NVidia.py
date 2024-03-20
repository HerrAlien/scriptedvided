import scriptedvided

configs = { "defaultAudioFile" : "lethal company nvidia.ogg",\
"mediaFolder" : "F:\\Videos\\Lethal Company NVidia", \
"stockFolder" : "F:\\Videos\\stock",\
"outputFolder" : "F:\\Videos\\Lethal Company NVidia\\output", \
"outputFile" : "Lethal Company NVidia.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#00800080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "Did I miss something in the last video ...", "until" : "1920x1080 results"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "1920x1080 results", "until" : "Conclusions"}}, \
{"file" : "Inspired - MaikonMusic  Free Background Music  Audio Library Release.mp3", "timestamps" : ("00:00", None ), "destinationTimestamp" : {"title" : "Conclusions", "until" : "EOF"}}, \
], "volume" : 0.06 },\
"episodes" : [],\
"youtube" : {"title" : "Lethal Company under the minimum requirements", \
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
"tags" : "Lethal Company,GeForce,NVidia,Fermi,Pascal,GT730,GT 730,GT1030,GT 1030,GTX1050Ti,GTX 1050Ti,GTX 1050 Ti",\
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
{ "title": "Did I miss something in the last video ...",\
"audio" : {"timestamps" : (lastTS, "00:19" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "stock_Lethal Company_2024_03_10_3.mp4"},\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "GT 730",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "00:25" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "breel_FermiGT730_outside.mp4"},\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]


configs["episodes"].append(\
{ "title": "GT 1030",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "00:29.5" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "breel_gt1030_outside.mp4"},\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]


configs["episodes"].append(\
{ "title": "GTX 1050Ti",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "00:36.5" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "broll_GTX1050Ti_outside.mp4"},\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Game settings",\
"audio" : {"timestamps" : (lastTS, "00:45.4" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "stock_Lethal Company_2024_03_10_2.mp4"},\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Test system",\
"audio" : {"timestamps" : (lastTS, "01:05" ), "volume" : 0.999, "padAudio" : 0.1 },\
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
{ "title": "1920x1080 results",\
"audio" : {"timestamps" : (lastTS, "01:24.1" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "Lethal Company_2024_03_09_22_22_06_104-converted.mp4"},\
"overlay" : { \
    "image" : {"file" : "1920x1080.png", "chromaColor" : "0x00FF00"}\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "1080 GT 730",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "01:42.5" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "L_ethal Company_FermiGT730.mp4", "start" : "02:50"},\
"overlay" : { \
    "image" : {"file" : "1920x1080.png", "chromaColor" : "0x00FF00"}\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "1280x720 results",\
"audio" : {"timestamps" : (lastTS, "01:57.4" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "Lethal Company_2024_03_09_22_25_45_404-converted.mp4"},\
"overlay" : { \
    "image" : {"file" : "1280x720.png", "chromaColor" : "0x00FF00"}\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

# gpu limited
configs["episodes"].append(\
{ "title": "Conclusions",\
"audio" : {"timestamps" : (lastTS, "02:16.5" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "stock_Lethal Company_2024_03_10_3.mp4"},\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Fermi better than TS2",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "02:36.7" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "gt730_hd6670.mp4"},\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "bye",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "02:44.4" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "L_ethal Company_GT1030.mp4"},\
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