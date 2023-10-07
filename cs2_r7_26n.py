import scriptedvided

configs = { "defaultAudioFile" : "R7_26N_CS2.ogg",\
"mediaFolder" : "F:\\Videos\\R7_26N_CS2", \
"stockFolder" : "F:\\Videos\\stock",\
"outputFolder" : "F:\\Videos\\R7_26N_CS2\\output", \
"outputFile" : "R7_26N_CS2.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3",\
"timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "60 FPS at 1080?", "until" : "1920x1080 results"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3",\
"timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "1920x1080 results", "until" : "Conclusion"}}, \
{"file" : "Guide You Home - Ferco and Andie - Free Background Music - Audio Library Release.ogg", "timestamps" : ("00:20", None ), "destinationTimestamp" : { "title": "Conclusion", "until" : "Blooper" }}, \
], "volume" : 0.06 },\
"episodes" : [],\
"youtube" : {"title" : "How does CS2 run on some old Radeons? (R7 250, HD 7750, HD 7770)", \
"description" : '''In this video, we'll take a closer look on how the old TeraScale 2 video cards (Radeon HD 7750, HD 7770, R7 250) run Counter Strike 2.
As usual, we're pairing the cards with the i7 4770 equivalent Xeon (E3-1241 v3), and 32 GB DDR3 @1600MHz, in dual channel.''',\
"links" : '''
Track: Bliss Of Heaven — SOMM [Audio Library Release]
Music provided by Audio Library Plus
Watch: https://www.youtube.com/watch?v=JQ6mKeQLZak&t=0s
Free Download / Stream: https://alplus.io/blisss-heaven

Track: Far Far Away — Ferco [Audio Library Release]
Music provided by Audio Library Plus
Watch: https://www.youtube.com/watch?v=SrkQ3K1umlc&t=0s 
Free Download / Stream: https://alplus.io/far-far-away

Track: Guide You Home — Ferco & Andie [Audio Library Release]
Music provided by Audio Library Plus
Watch: https://www.youtube.com/watch?v=16eNerPDIsU&t=0s
Free Download / Stream: https://alplus.io/guide-you-home

More games tested with the TeraScale 2 cards:
https://www.youtube.com/watch?v=9ZrKAwA6MbQ&list=PLgBGV4K3p2_YhzgbzcQ6kdgfGpzdq6cRD
''', \
"tags" : "Counter Strike 2,CS2,Radeon,AMD,1GB,2GB,SM5,GCN,GCN 1.0,GCN 2.0,GCN2,R7 260,HD7790,HD 7790,R7 260X,HD7850,HD 7850,R7 265,R7 370,MSI,ASUS,Sapphire,60 FPS,60FPS",\
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


configs["episodes"].append(\
{ "title": "60 FPS at 1080?",\
"audio" : {"timestamps" : ("00:00", "00:08.5"), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "CapeVerde_CS2.mp4", "start" : "02:30"},\
})

# this will be split up
configs["episodes"].append(\
{ "title": "The GPUs and test system",\
"audio" : {"timestamps" : ("00:08.5", "00:15"), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "stock_midGCNs_family.mp4", "start" : "00:00"}\
})

configs["episodes"].append(\
{ "title": "R7 260",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:15", "00:20.5"), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "stock_midGCNs_family.mp4", "start" : "00:40"}\
})

# 7770 - 51, 7750 - 01:40 

configs["episodes"].append(\
{ "title": "R7 260X",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:20.5", "00:28.2"), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "stock_midGCNs_family.mp4", "start" : "01:05"}\
})

configs["episodes"].append(\
{ "title": "R7 265",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:28.2", "00:40.5"), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "stock_midGCNs_family.mp4", "start" : "01:38"}\
})

configs["episodes"].append(\
{ "title": "Z230",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:40.5", "00:54.5"), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "Z230_closed.mp4" , "rotation" : 180}\
})

configs["episodes"].append(\
{ "title": "1920x1080 results",\
"audio" : {"timestamps" : ("00:54.5", "02:01.3") , "padAudio" : 0.25 },\
"video" : {"file": "stock_CS2_CT_R7_260.mp4"},\
"overlay" : { \
    "image" : {"file" : "1080, low settings.png", "chromaColor" : "0x00FF00"}\
}, \
})

configs["episodes"].append(\
{ "title": "1280x720 results",\
"audio" : {"timestamps" : ("02:01.3", "02:49.5"), "padAudio" : 0.25 },\
"video" : {"file": "stock_CS2_T_R7_265.mp4"},\
"overlay" : { \
    "image" : {"file" : "720, low settings.png", "chromaColor" : "0x00FF00"}\
}, \
})

configs["episodes"].append(\
{ "title": "Conclusion",\
"audio" : {"timestamps" : ("02:49.5", "03:03.25"), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "stock_midGCNs_family.mp4", "start" : "00:00"}\
})

configs["episodes"].append(\
{ "title": "win",\
"isChapter" : False,\
"audio" : {"timestamps" : ("03:03.25", "03:15.7"), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "stock_CS2_CT_R7_260.mp4", "start" : "07:13"}\
})

configs["episodes"].append(\
{ "title": "High end GCN",\
"isChapter" : False,\
"audio" : {"timestamps" : ("03:15.7", "03:28"), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "breel_r9_290x_outside_dog.mp4", "start" : "00:20"},\
})

configs["episodes"].append(\
{ "title": "End of the series",\
"isChapter" : False,\
"audio" : {"timestamps" : ("03:28", "03:41.25"), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "stock_CS2_CT_R7_260.mp4"}\
})

configs["episodes"].append(\
{ "title": "Bye",\
"isChapter" : False,\
"audio" : {"timestamps" : ("03:41.25", "03:50"), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "stock_midGCNs_family.mp4", "start" : "00:00"}\
})



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
