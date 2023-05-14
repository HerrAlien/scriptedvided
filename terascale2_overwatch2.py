import scriptedvided

configs = { "defaultAudioFile" : "TS2_Overwatch2.ogg",\
"mediaFolder" : "F:\\Videos\\overwatch2_vs_ts2", \
"stockFolder" : "F:\\Videos\\stock",\
"outputFolder" : "F:\\Videos\\overwatch2_vs_ts2\\output", \
"outputFile" : "TeraScale2_overwatch2.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3",\
"timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "TLDW", "until" : "1920x1080 results"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3",\
"timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "actual 1080 results", "until" : "1600x900 results"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3",\
"timestamps" : ("01:33", None ), "destinationTimestamp" : {"title" : "actual 900 results", "until" : "1280x720 results"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3",\
"timestamps" : ("02:33", None ), "destinationTimestamp" : {"title" : "actual 720 results", "until" : "Conclusion"}}, \
{"file" : "Guide You Home - Ferco and Andie - Free Background Music - Audio Library Release.ogg", "timestamps" : ("00:20", None ), "destinationTimestamp" : { "title": "Conclusion", "until" : "Blooper" }}, \
], "volume" : 0.06 },\
"episodes" : [],\
"youtube" : {"title" : "Playing Overwatch 2 on unsupported old Radeons", \
"description" : '''In this video, we'll take a closer look on how the old TeraScale 2 video cards (Radeon HD 6670, HD 5770, HD 6850, HD 5870) run Overwatch 2.
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
"tags" : "Overwatch,Overwatch2,Overwatch 2,AMD,ATI,Radeon,TeraScale 2,HD 5770,HD5770,HD 6850,HD6850,HD 5870,HD5870,HD 6670,HD6670",\
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
{ "title": "TLDW",\
"audio" : {"timestamps" : ("00:00", "00:20" ), "volume" : 0.999, "padAudio" : 0.25 },\
"video" : {"file" : "stock_Overwatch2_gameplay_5770.mp4"}\
})

configs["episodes"].append(\
{ "title": "Minimum specs",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:20", "00:41" ), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : "o_verwatch2_requirements.mkv"\
})

# this will be split up
configs["episodes"].append(\
{ "title": "GPUs, test system and benchmark",\
"audio" : {"timestamps" : ("00:41", "00:46" ), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "broll_ts2family_outside.mp4"}\
})

configs["episodes"].append(\
{ "title": "hd5870",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:46", "00:54" ), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "broll_ts2_family_outside_takingTurns.mp4", "start" : "00:02"}\
})

configs["episodes"].append(\
{ "title": "hd5770 6850",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:54", "01:03" ), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "broll_ts2_family_outside_takingTurns.mp4", "start" : "00:20"}\
})

configs["episodes"].append(\
{ "title": "hd6670",\
"isChapter" : False,\
"audio" : {"timestamps" : ("01:03" , "01:08"), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "broll_ts2_family_outside_takingTurns.mp4", "start" : "00:40"}\
})

configs["episodes"].append(\
{ "title": "Z230",\
"isChapter" : False,\
"audio" : {"timestamps" : ("01:08" , "01:20.25"), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "Z230_closed.mp4" , "rotation" : 180}\
})

configs["episodes"].append(\
{ "title": "benchmark",\
"isChapter" : False,\
"audio" : {"timestamps" : ("01:20.25", "01:31.5"), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "stock_Overwatch2_training.mp4", "start" :"00:00" }\
})


configs["episodes"].append(\
{ "title": "1920x1080 results",\
"audio" : {"timestamps" : ("00:00", "00:10" ), "volume" : 0.001 },\
"video" : {"file": "stock_Overwatch2_training.mp4", "start" : "04:16"},\
"overlay" : { "text" : ["'1920x1080, low settings, tutorial level'"] },\
})


configs["episodes"].append(\
{ "title": "actual 1080 results",\
"isChapter" : False,\
"audio" : {"timestamps" : ("01:31.5", "02:15"), "volume" : 0.95 , "padAudio" : 0.25 },\
"video" : {"file" : "stock_Overwatch2_gameplay_5770.mp4" , "start" : "01:20"},\
"overlay" : { \
    "image" : {"file" : "1080.png", "chromaColor" : "0x00FF00"}\
}, \
})

configs["episodes"].append(\
{ "title": "1600x900 results",\
"audio" : { "timestamps" : ("00:00", "00:10" ), "volume" : 0.001 },\
"video" : {"file": "stock_Overwatch2_training.mp4", "start" : "00:17"},\
"overlay" : { "text" : ["'1600x900, low settings, tutorial level'"] },\
})


configs["episodes"].append(\
{ "title": "actual 900 results",\
"isChapter" : False,\
"audio" : {"timestamps" : ("02:15", "02:50.5"), "volume" : 0.95 , "padAudio" : 0.25 },\
"overlay" : { \
    "image" : {"file" : "900.png", "chromaColor" : "0x00FF00"}\
}, \
"video" : {"file" : "stock_Overwatch2_gameplay.mp4", "start" : "00:40"},\
})

configs["episodes"].append(\
{ "title": "1280x720 results",\
"audio" : {"timestamps" : ("00:00", "00:10" ), "volume" : 0.001 },\
"video" : {"file": "stock_Overwatch2_training.mp4", "start" : "02:00"},\
"overlay" : { "text" : ["'1280x720, low settings, tutorial level'"] },\
})


### needs video
configs["episodes"].append(\
{ "title": "actual 720 results",\
"isChapter" : False,\
"audio" : {"timestamps" : ("02:50.5", "03:23.7"), "volume" : 0.95 , "padAudio" : 0.25 },\
"overlay" : { \
    "image" : {"file" : "720.png", "chromaColor" : "0x00FF00"}\
}, \
"video" : {"file" : "stock_Overwatch2_gameplay_5770.mp4" , "start" : "03:00"},\
})


configs["episodes"].append(\
{ "title": "Conclusion",\
"audio" : {"timestamps" : ("03:23.7", "03:37"), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "broll_hd5770_outside.mp4"}\
})

configs["episodes"].append(\
{ "title": "bye",\
"audio" : {"file" : "silence_30min.ogg" , "timestamps" : ("00:00", "00:10" ), "volume" : 0.001 },\
"video" : {"file": "stock_Overwatch2_training.mp4", "start" : "01:10"},\
})


configs["episodes"].append(\
{ "title": "family 2",\
"isChapter" : False,\
"audio" : {"timestamps" : ( "03:37",  "03:51"), "volume" : 0.999 , "padAudio" : 1 },\
"video" : {"file" : "broll_ts2family_outside.mp4"}\
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
