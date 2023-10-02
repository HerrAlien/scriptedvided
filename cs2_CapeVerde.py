import scriptedvided

configs = { "defaultAudioFile" : "CapeVerde_CS2.ogg",\
"mediaFolder" : "F:\\Videos\\CapeVerde_CS2", \
"stockFolder" : "F:\\Videos\\stock",\
"outputFolder" : "F:\\Videos\\CapeVerde_CS2\\output", \
"outputFile" : "CapeVerde_CS2.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3",\
"timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "Not all 1GB cards are the same", "until" : "1920x1080 results"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3",\
"timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "1920x1080 results", "until" : "Conclusions"}}, \
{"file" : "Guide You Home - Ferco and Andie - Free Background Music - Audio Library Release.ogg", "timestamps" : ("00:20", None ), "destinationTimestamp" : { "title": "Conclusions", "until" : "Blooper" }}, \
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
"tags" : "Counter Strike 2,CS2,Radeon,AMD,1GB,SM5,GCN,GCN 1.0,R7 250,HD7750,HD 7750,HD7770,HD 7770,R7 250E,R7 250 512SP,R7 250X,60 FPS,60FPS",\
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
{ "title": "Not all 1GB cards are the same",\
"audio" : {"timestamps" : ("00:00", "00:14" ), "volume" : 0.999, "padAudio" : 0.25 },\
"video" : {"file" : "TS2_CS2.mp4", "start" : "01:10"},\
})

# this will be split up
configs["episodes"].append(\
{ "title": "Meet the GPUs and test system (again)",\
"audio" : {"timestamps" : ("00:14", "00:25.7" ), "volume" : 0.999, "padAudio" : 0.25 },\
"video" : {"file" : "stock_CapeVerde_family.mp4", "start" : "00:00", "rotation" : 180}\
})

configs["episodes"].append(\
{ "title": "R7 250",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:25.7", "00:34" ), "volume" : 0.999, "padAudio" : 0.25 },\
"video" : {"file" : "stock_CapeVerde_family.mp4", "start" : "02:24", "rotation" : 180}\
})

# 7770 - 51, 7750 - 01:40 

configs["episodes"].append(\
{ "title": "HD 7750",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:34", "00:49" ), "volume" : 0.999, "padAudio" : 0.25 },\
"video" : {"file" : "stock_CapeVerde_family.mp4", "start" : "01:40", "rotation" : 180}\
})

configs["episodes"].append(\
{ "title": "HD 7770",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:49", "00:57" ), "volume" : 0.999, "padAudio" : 0.25 },\
"video" : {"file" : "stock_CapeVerde_family.mp4", "start" : "00:51", "rotation" : 180}\
})

configs["episodes"].append(\
{ "title": "Z230",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:57", "01:13" ), "volume" : 0.999, "padAudio" : 0.25 },\
"video" : {"file" : "Z230_closed.mp4" , "rotation" : 180}\
})

configs["episodes"].append(\
{ "title": "1920x1080 results",\
"audio" : {"timestamps" : ("01:13", "02:14" )  },\
"video" : {"file": "stock_cs2_T_R7_250.mp4"},\
"overlay" : { \
    "image" : {"file" : "1080, low settings.png", "chromaColor" : "0x00FF00"}\
}, \
})

configs["episodes"].append(\
{ "title": "1280x720 results",\
"audio" : {"timestamps" : ("02:14", "03:08" )  },\
"video" : {"file": "stock_cs2_CT_hd7770.mp4"},\
"overlay" : { \
    "image" : {"file" : "720, low settings.png", "chromaColor" : "0x00FF00"}\
}, \
})

configs["episodes"].append(\
{ "title": "Conclusion",\
"audio" : {"timestamps" : ("03:08", "03:26.33"), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "stock_CapeVerde_family.mp4", "start" : "00:43", "rotation" : 180}\
})

configs["episodes"].append(\
{ "title": "7770",\
"isChapter" : False,\
"audio" : {"timestamps" : ("03:26.33", "03:43"), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "stock_CapeVerde_family.mp4", "start" : "00:56", "rotation" : 180}\
})

configs["episodes"].append(\
{ "title": "no 1080",\
"isChapter" : False,\
"audio" : {"timestamps" : ("03:43", "04:03"), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "stock_cs2_T_gt1030lp.mp4"},\
})

configs["episodes"].append(\
{ "title": "GCN family - mid level",\
"isChapter" : False,\
"audio" : {"timestamps" : ("04:03", "04:13.5"), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "stock_midGCNs_family.mp4", "start" : "00:00" , "rotation" : 180}\
})

configs["episodes"].append(\
{ "title": "Bye",\
"isChapter" : False,\
"audio" : {"timestamps" : ("04:13.5", "04:21"), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "stock_CapeVerde_family.mp4", "start" : "00:00", "rotation" : 180}\
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
