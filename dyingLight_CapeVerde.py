import scriptedvided

configs = { "defaultAudioFile" : "DyingLight_CapeVerde.ogg",\
"mediaFolder" : "F:\\Videos\\dyingLight_CapeVerde", \
"stockFolder" : "F:\\Videos\\stock",\
"outputFolder" : "F:\\Videos\\dyingLight_CapeVerde\\output", \
"outputFile" : "DyingLight_CapeVerde.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3",\
"timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "Just because Halloween passed ...", "until" : "1920x1080 results"}}, \
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
{ "title": "Just because Halloween passed ...",\
"audio" : {"timestamps" : ("00:00", "00:14" ), "volume" : 0.999, "padAudio" : 0.25 },\
"video" : {"file" : "stock_DyingLight_r7_265_includesBenchmarkRun.mp4" , "start" : "02:00"},\
})

configs["episodes"].append(\
{ "title": "EGS",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:14", "00:26" ), "volume" : 0.999, "padAudio" : 0.25 },\
"video" : {"file" : "dying_light_free_2.mkv", "start" : "00:14"},\
})

# this will be split up
configs["episodes"].append(\
{ "title": "The GPUs and test system",\
"audio" : {"timestamps" : ("00:26", "00:32.5" ), "volume" : 0.999, "padAudio" : 0.25 },\
"video" : {"file" : "stock_CapeVerde_family.mp4", "start" : "00:00", "rotation" : 90}\
})

configs["episodes"].append(\
{ "title": "R7 250",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:32.5", "00:38.5" ), "volume" : 0.999, "padAudio" : 0.25 },\
"video" : {"file" : "stock_CapeVerde_family.mp4", "start" : "02:24", "rotation" : 90}\
})

# 7770 - 51, 7750 - 01:40 

configs["episodes"].append(\
{ "title": "HD 7750",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:38.5", "00:49" ), "volume" : 0.999, "padAudio" : 0.25 },\
"video" : {"file" : "stock_CapeVerde_family.mp4", "start" : "01:40", "rotation" : 90}\
})

configs["episodes"].append(\
{ "title": "HD 7770",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:49", "00:57" ), "volume" : 0.999, "padAudio" : 0.25 },\
"video" : {"file" : "stock_CapeVerde_family.mp4", "start" : "00:51", "rotation" : 90}\
})

configs["episodes"].append(\
{ "title": "Z230",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:57", "01:13" ), "volume" : 0.999, "padAudio" : 0.25 },\
"overlay" : { \
    "text" : ["'Z230 workstation from HP'",\
              "'CPU\: E3-1241v3 Xeon (i7 4770 equivalent)'",\
              "'RAM\: 32GB DDR3 at 1600 MHz, dual channel'",\
    ]\
}, \
"video" : {"file" : "Z230_closed.mp4" , "rotation" : 180}\
})

configs["episodes"].append(\
{ "title": "settings",\
"isChapter" : False,\
"audio" : {"timestamps" : ("01:13", "01:24" ), "volume" : 0.999, "padAudio" : 0.25 },\
"video" : {"file" : "stock_DyingLight_testbench.mp4"}\
})

configs["episodes"].append(\
{ "title": "1920x1080 results",\
"audio" : {"timestamps" : ("01:24", "02:09" ), "padAudio" : 0.25 },\
"video" : {"file" : "stock_DyingLight_r7_265_includesBenchmarkRun.mp4", "start" : "04:00"},\
"overlay" : { \
    "image" : {"file" : "1080, low settings.png", "chromaColor" : "0x00FF00"}\
}, \
})

configs["episodes"].append(\
{ "title": "1600x900 results",\
"audio" : {"timestamps" : ("02:09", "02:55" ), "padAudio" : 0.25 },\
"video" : {"file" : "stock_DyingLight_r7_265_includesBenchmarkRun.mp4", "start" : "06:10"},\
"overlay" : { \
    "image" : {"file" : "900, low settings.png", "chromaColor" : "0x00FF00"}\
}, \
})

configs["episodes"].append(\
{ "title": "1280x720 results",\
"audio" : {"timestamps" : ("02:55", "03:48" ), "padAudio" : 0.25 },\
"video" : {"file" : "stock_DyingLight_GAMEPLAY_2.mp4"},\
"overlay" : { \
    "image" : {"file" : "720, low settings.png", "chromaColor" : "0x00FF00"}\
}, \
})

configs["episodes"].append(\
{ "title": "Conclusion",\
"audio" : {"timestamps" : ("03:48", "03:58.5" ), "volume" : 0.999, "padAudio" : 0.25 },\
"video" : {"file" : "stock_CapeVerde_family.mp4", "start" : "00:00", "rotation" : 90}\
})

configs["episodes"].append(\
{ "title": "good gameplay",\
"isChapter" : False,\
"audio" : {"timestamps" : ("03:58.5", "04:14" ), "volume" : 0.999, "padAudio" : 0.25 },\
"video" : {"file" : "stock_DyingLight_r7_265_includesBenchmarkRun.mp4", "start" : "07:00"},\
})

configs["episodes"].append(\
{ "title": "GCN family - mid level",\
"isChapter" : False,\
"audio" : {"timestamps" : ("04:14", "04:22.5" ), "volume" : 0.999, "padAudio" : 0.25 },\
"video" : {"file" : "stock_midGCNs_family.mp4", "start" : "00:00"}\
})

configs["episodes"].append(\
{ "title": "Bye",\
"isChapter" : False,\
"audio" : {"timestamps" : ("04:22.5", "04:29" ), "volume" : 0.999, "padAudio" : 0.25 },\
"video" : {"file" : "stock_CapeVerde_family.mp4", "start" : "00:00", "rotation" : 90}\
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
