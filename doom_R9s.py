import scriptedvided

configs = { "defaultAudioFile" : "Doom_R9_2.ogg",\
"mediaFolder" : "F:\\Videos\\Doom_R9", \
"stockFolder" : "F:\\Videos\\stock",\
"outputFolder" : "F:\\Videos\\Doom_R9\\output", \
"outputFile" : "Doom_R9.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3",\
"timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "The successful reboot", "until" : "1920x1080 results"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3",\
"timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "1920x1080 results", "until" : "Conclusion"}}, \
{"file" : "Guide You Home - Ferco and Andie - Free Background Music - Audio Library Release.ogg", "timestamps" : ("00:20", None ), "destinationTimestamp" : { "title": "Conclusion", "until" : "Blooper" }}, \
], "volume" : 0.06 },\
"episodes" : [],\
"youtube" : {"title" : "Testing DOOM 2016 on older Radeons (R9 270, R9 280, R9 290X)", \
"description" : '''In this video, we'll see if 3 of the AMD Radeon R9 series are Doomed or not.
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
"tags" : "Doom,Doom 2016,GCN,AMD,Radeon,R9 270,HD 7870,HD7870,R9 280,HD7950,HD 7950,R9 290X,Hawaii,Tahiti,Curacao",\
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
{ "title": "The successful reboot",\
"audio" : {"timestamps" : ("00:00", "00:24" ), "volume" : 0.999, "padAudio" : 0.25 },\
"video" : {"file" : "stock_DOOM_2016_720pLow.mp4", "start" : "02:50"},\
})


# this will be split up
configs["episodes"].append(\
{ "title": "The GPUs and test system",\
"audio" : {"timestamps" : ("00:24", "00:32.6" ), "volume" : 0.999, "padAudio" : 0.25 },\
"video" : {"file" : "R9_family_poor.mkv"},\
})

configs["episodes"].append(\
{ "title": "R9 290X",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:32.6", "00:39.6" ), "volume" : 0.999, "padAudio" : 0.25 },\
"video" : {"file" : "breel_r9_290x_outside.mp4"},\
})

configs["episodes"].append(\
{ "title": "R9 280",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:39.6", "00:46.3" ), "volume" : 0.999, "padAudio" : 0.25 },\
"video" : {"file" : "breel_r9_280_outside.mp4"},\
})

configs["episodes"].append(\
{ "title": "R9 270",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:46.3", "00:52.3" ), "volume" : 0.999, "padAudio" : 0.25 },\
"video" : {"file" : "breel_r9_270_outside.mp4"},\
})

configs["episodes"].append(\
{ "title": "Z230",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:52.3", "01:03" ), "volume" : 0.999, "padAudio" : 0.25 },\
"overlay" : { \
    "text" : ["'Z230 workstation from HP'",\
              "'CPU\: E3-1241v3 Xeon (i7 4770 equivalent)'",\
              "'RAM\: 32GB DDR3 at 1600 MHz, dual channel'",\
    ]\
}, \
"video" : {"file" : "Z230_closed.mp4" , "rotation" : 180}\
})


configs["episodes"].append(\
{ "title": "test settings",\
"isChapter" : False,\
"audio" : {"timestamps" : ("01:03", "01:23" ), "volume" : 0.999, "padAudio" : 0.25 },\
"video" : {"file" : "stock_DOOM_2016_720pLow.mp4", "start" : "05:17"},\
})

configs["episodes"].append(\
{ "title": "1920x1080 results",\
"audio" : {"timestamps" : ("01:23", "02:12" ), "padAudio" : 0.25 },\
"video" : {"file" : "stock_DOOM_2016_720pLow.mp4", "start" : "06:40"},\
"overlay" : { \
    "image" : {"file" : "1080, low settings.png", "chromaColor" : "0x00FF00"}\
}, \
})

configs["episodes"].append(\
{ "title": "1600x900 results",\
"audio" : {"timestamps" : ("02:12", "02:54" ), "padAudio" : 0.25 },\
"video" : {"file" : "stock_DOOM_2016_720pLow.mp4", "start" : "03:30"},\
"overlay" : { \
    "image" : {"file" : "900, low settings.png", "chromaColor" : "0x00FF00"}\
}, \
})

configs["episodes"].append(\
{ "title": "1280x720 results",\
"audio" : {"timestamps" : ("02:54", "03:56" ), "padAudio" : 0.25 },\
"video" : {"file" : "stock_DOOM_2016_720pLow.mp4", "start" : "14:00"},\
"overlay" : { \
    "image" : {"file" : "720, low settings.png", "chromaColor" : "0x00FF00"}\
}, \
})

configs["episodes"].append(\
{ "title": "Conclusion",\
"audio" : {"timestamps" : ("03:56", "04:09" ), "volume" : 0.999, "padAudio" : 0.25 },\
"video" : {"file" : "stock_DOOM_2016_720pLow.mp4", "start" : "09:20"},\
})

configs["episodes"].append(\
{ "title": "R9 280 and 270 are fine, 290X too hot",\
"isChapter" : False,\
"audio" : {"timestamps" : ("04:09", "04:21" ), "volume" : 0.999, "padAudio" : 0.25 },\
"video" : {"file" : "breel_r9_280_outside.mp4"},\
})

configs["episodes"].append(\
{ "title": "GCN family - mid level",\
"isChapter" : False,\
"audio" : {"timestamps" : ("04:21", "04:28.5" ), "volume" : 0.999, "padAudio" : 0.25 },\
"video" : {"file" : "stock_midGCNs_family.mp4" , "start" : "00:00"},\
})

configs["episodes"].append(\
{ "title": "Bye",\
"isChapter" : False,\
"audio" : {"timestamps" : ("04:28.5", "04:34.7" ), "volume" : 0.999, "padAudio" : 0.25 },\
"video" : {"file" : "stock_DOOM_2016_720pLow.mp4"},\
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
