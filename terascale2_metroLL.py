import scriptedvided

configs = { "defaultAudioFile" : "ts2_vs_metroLL.ogg",\
"mediaFolder" : "F:\\Videos\\ts2_vs_metroLL", \
"stockFolder" : "F:\\Videos\\stock",\
"outputFolder" : "F:\\Videos\\ts2_vs_metroLL\\output", \
"outputFile" : "ts2_vs_metroLL.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3",\
"timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "Metro - Last Light, free until May 25th", "until" : "1920x1080 results"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3",\
"timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "1920x1080 results", "until" : "1600x900 results"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3",\
"timestamps" : ("01:33", None ), "destinationTimestamp" : {"title" : "1600x900 results", "until" : "1280x720 results"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3",\
"timestamps" : ("02:33", None ), "destinationTimestamp" : {"title" : "1280x720 results", "until" : "Conclusion"}}, \
{"file" : "Guide You Home - Ferco and Andie - Free Background Music - Audio Library Release.ogg", "timestamps" : ("00:20", None ), "destinationTimestamp" : { "title": "Conclusion", "until" : "Blooper" }}, \
], "volume" : 0.06 },\
"episodes" : [],\
"youtube" : {"title" : "Playing Overwatch 2 on unsupported old Radeons", \
"description" : '''In this video, we'll take a closer look on how the old TeraScale 2 video cards (Radeon HD 6670, HD 5770, HD 6850, HD 5870) run Metro: Last Light.
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
"tags" : "Metro: Last Light,Metro,AMD,ATI,Radeon,TeraScale 2,HD 5770,HD5770,HD 6850,HD6850,HD 5870,HD5870,HD 6670,HD6670",\
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
{ "title": "Metro - Last Light, free until May 25th",\
"audio" : {"timestamps" : ("00:00", "00:18" ), "volume" : 0.999, "padAudio" : 0.25 },\
"video" : {"file" : "stock_MetroLL_benchmark_veryHigh.mp4"}\
})

configs["episodes"].append(\
{ "title": "Minimum specs",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:18", "00:34" ), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : "metroLL_requirements.mkv"\
})

# this will be split up
configs["episodes"].append(\
{ "title": "GPUs, test system and benchmark",\
"audio" : {"timestamps" : ("00:34", "00:43" ), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "broll_ts2family_outside.mp4"}\
})

configs["episodes"].append(\
{ "title": "hd5870",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:43", "00:48" ), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "broll_ts2_family_outside_takingTurns.mp4", "start" : "00:02"}\
})

configs["episodes"].append(\
{ "title": "hd5770 6850",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:48", "00:53.4" ), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "broll_ts2_family_outside_takingTurns.mp4", "start" : "00:20"}\
})

configs["episodes"].append(\
{ "title": "hd6670",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:53.4" , "00:58"), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "broll_ts2_family_outside_takingTurns.mp4", "start" : "00:40"}\
})

configs["episodes"].append(\
{ "title": "Z230",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:58" , "01:12.4"), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "Z230_closed.mp4" , "rotation" : 180}\
})

### maybe do a versus video here?
configs["episodes"].append(\
{ "title": "benchmark",\
"isChapter" : False,\
"audio" : {"timestamps" : ("01:12.4", "01:25"), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "stock_MetroLL_benchmark_low.mp4", "start" :"00:00" }\
})


configs["episodes"].append(\
{ "title": "1920x1080 results",\
"audio" : {"timestamps" : ("01:25", "02:17" )  },\
"video" : {"file": "stock_MetroLL_benchmark_low.mp4", "start" : "00:00"},\
"overlay" : { \
    "image" : {"file" : "1080, low settings.png", "chromaColor" : "0x00FF00"}\
}, \
})

configs["episodes"].append(\
{ "title": "1600x900 results",\
"audio" : {"timestamps" : ("02:17", "02:58" )  },\
"video" : {"file": "stock_MetroLL_benchmark_low.mp4", "start" : "00:54"},\
"overlay" : { \
    "image" : {"file" : "900, low settings.png", "chromaColor" : "0x00FF00"}\
}, \
})

configs["episodes"].append(\
{ "title": "1280x720 results",\
"audio" : {"timestamps" : ("02:58" , "03:41" )  },\
"video" : {"file": "stock_MetroLL_benchmark_low.mp4", "start" : "01:39"},\
"overlay" : { \
    "image" : {"file" : "720, low settings.png", "chromaColor" : "0x00FF00"}\
}, \
})


configs["episodes"].append(\
{ "title": "Conclusion",\
"audio" : {"timestamps" : ("03:41", "04:06"), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file": "stock_MetroLL_benchmark_veryHigh.mp4"},\
"overlay" : { \
    "image" : {"file" : "sideBySide, low settings.png", "chromaColor" : "0x00FF00"}\
}, \
})

configs["episodes"].append(\
{ "title": "family 2",\
"isChapter" : False,\
"audio" : {"timestamps" : ( "04:06",  "04:23.6"), "volume" : 0.999 , "padAudio" : 1 },\
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
