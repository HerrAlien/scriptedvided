import scriptedvided

configs = { "defaultAudioFile" : "DyingLight_midGCN.ogg",\
"mediaFolder" : "F:\\Videos\\DyingLight_midGCN", \
"stockFolder" : "F:\\Videos\\stock",\
"outputFolder" : "F:\\Videos\\DyingLight_midGCN\\output", \
"outputFile" : "DyingLight_midGCN.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3",\
"timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "Good morning, Harran", "until" : "1920x1080 results"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3",\
"timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "1920x1080 results", "until" : "Conclusion"}}, \
{"file" : "Guide You Home - Ferco and Andie - Free Background Music - Audio Library Release.ogg", "timestamps" : ("00:20", None ), "destinationTimestamp" : { "title": "Conclusion", "until" : "Blooper" }}, \
], "volume" : 0.06 },\
"episodes" : [],\
"youtube" : {"title" : " think of a title ", \
"description" : '''In this video, we'll take a closer look on how the mid-range GCN cards run the first Dying Light game.
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

''', \
"tags" : "Dying Light,zombie,Radeon,AMD,1GB,2GB,SM5,GCN,GCN 1.0,GCN 2.0,GCN2,R7 260,HD7790,HD 7790,R7 260X,HD7850,HD 7850,R7 265,R7 370,MSI,ASUS,Sapphire,60 FPS,60FPS",\
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
{ "title": "Good morning, Harran",\
"audio" : {"timestamps" : ("00:00", "00:10.5" ), "volume" : 0.999, "padAudio" : 0.25 },\
"video" : {"file" : "stock_DyingLight_antizen.mp4", "start" : "02:01"},\
})

configs["episodes"].append(\
{ "title": "EGS",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:10.5", "00:22" ), "volume" : 0.999, "padAudio" : 0.25 },\
"video" : {"file" : "dying_light_free_2.mkv", "start" : "00:07"},\
})

# this will be split up
configs["episodes"].append(\
{ "title": "The GPUs and test system",\
"audio" : {"timestamps" : ("00:22", "00:28.25" ), "volume" : 0.999, "padAudio" : 0.25 },\
"video" : {"file" : "stock_midGCNs_family.mp4", "start" : "00:00"},\
})

configs["episodes"].append(\
{ "title": "R7 260",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:28.25", "00:33.33" ), "volume" : 0.999, "padAudio" : 0.25 },\
"video" : {"file" : "stock_midGCNs_family.mp4", "start" : "00:40"}\
})

# 7770 - 51, 7750 - 01:40 

configs["episodes"].append(\
{ "title": "R7 260X",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:33.33", "00:42" ), "volume" : 0.999, "padAudio" : 0.25 },\
"video" : {"file" : "stock_midGCNs_family.mp4", "start" : "01:05"}\
})

configs["episodes"].append(\
{ "title": "R7 265",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:42", "00:50" ), "volume" : 0.999, "padAudio" : 0.25 },\
"video" : {"file" : "stock_midGCNs_family.mp4", "start" : "01:38"}\
})

configs["episodes"].append(\
{ "title": "Z230",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:50", "01:06" ), "volume" : 0.999, "padAudio" : 0.25 },\
"overlay" : { \
    "text" : ["'Z230 workstation from HP'",\
              "'CPU\: E3-1241v3 Xeon (i7 4770 equivalent)'",\
              "'RAM\: 32GB DDR3 at 1600 MHz, dual channel'",\
    ]\
}, \
"video" : {"file" : "Z230_closed.mp4" , "rotation" : 180}\
})

configs["episodes"].append(\
{ "title": "1920x1080 results",\
"audio" : {"timestamps" : ("01:06", "02:03" ), "padAudio" : 0.25 },\
"video" : {"file" : "stock_DyingLight_r7_265_includesBenchmarkRun.mp4", "start" : "01:44" },\
"overlay" : { \
    "image" : {"file" : "1080, low settings.png", "chromaColor" : "0x00FF00"}\
}, \
})

configs["episodes"].append(\
{ "title": "1600x900 results",\
"audio" : {"timestamps" : ("02:03", "02:46" ), "padAudio" : 0.25 },\
"video" : {"file" : "stock_DyingLight_drZere.mp4"},\
"overlay" : { \
    "image" : {"file" : "900, low settings.png", "chromaColor" : "0x00FF00"}\
}, \
})

configs["episodes"].append(\
{ "title": "1280x720 results",\
"audio" : {"timestamps" : ("02:46", "03:31" ), "padAudio" : 0.25 },\
"video" : {"file" : "stock_DyingLight_GAMEPLAY_2.mp4", "start" : "09:00"},\
"overlay" : { \
    "image" : {"file" : "720, low settings.png", "chromaColor" : "0x00FF00"}\
}, \
})

configs["episodes"].append(\
{ "title": "Conclusion",\
"audio" : {"timestamps" : ("03:31", "03:58.5" ), "volume" : 0.999, "padAudio" : 0.25 },\
"video" : {"file" : "stock_midGCNs_family.mp4", "start" : "00:00" },\
})

configs["episodes"].append(\
{ "title": "GCN family - high level",\
"isChapter" : False,\
"audio" : {"timestamps" : ("03:58.5", "04:08.4" ), "volume" : 0.999, "padAudio" : 0.25 },\
"video" : {"file" : "breel_r9_290x_outside.mp4"},\
})

configs["episodes"].append(\
{ "title": "Bye",\
"isChapter" : False,\
"audio" : {"timestamps" : ("04:08.4", "04:15.5" ), "volume" : 0.999, "padAudio" : 0.25 },\
"video" : {"file" : "stock_midGCNs_family.mp4", "start" : "00:00" },\
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
