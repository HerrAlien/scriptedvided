import scriptedvided

configs = { "defaultAudioFile" : "TS2_CS2.ogg",\
"mediaFolder" : "F:\\Videos\\TS2_CS2", \
"stockFolder" : "F:\\Videos\\stock",\
"outputFolder" : "F:\\Videos\\TS2_CS2\\output", \
"outputFile" : "TS2_CS2.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3",\
"timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "1GB VRAM for minimum specs", "until" : "1920x1080 results"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3",\
"timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "1920x1080 results", "until" : "The cake is a lie"}}, \
{"file" : "Guide You Home - Ferco and Andie - Free Background Music - Audio Library Release.ogg", "timestamps" : ("00:20", None ), "destinationTimestamp" : { "title": "The cake is a lie", "until" : "Blooper" }}, \
], "volume" : 0.06 },\
"episodes" : [],\
"youtube" : {"title" : "Can I play CS2 on old Radeons? (spoiler: not on all of them)", \
"description" : '''In this video, we'll take a closer look on how the old TeraScale 2 video cards (Radeon HD 6670, HD 5770, HD 6850) run Counter Strike 2.
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
"tags" : "Counter Strike 2,CS2,Radeon,AMD,1GB,SM5,TeraScale2,TeraScale 2,HD6670,HD 6670,HD5770,HD 5770,HD6770,HD 6770,HD6850,HD 6850,60 FPS,60FPS",\
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
{ "title": "1GB VRAM for minimum specs",\
"audio" : {"timestamps" : ("00:00", "00:11" ), "volume" : 0.999, "padAudio" : 0.25 },\
"video" : {"file" : "stock_cs2_R9_270_ct.mp4"},\
"overlay" : { \
    "image" : {"file" : "minimum_specs_all.PNG", "chromaColor" : "0x00FF00"}\
}, \
})

# this will be split up
configs["episodes"].append(\
{ "title": "Meet the GPUs and test system (again)",\
"audio" : {"timestamps" : ("00:11", "00:18.4" ), "volume" : 0.999, "padAudio" : 0.25 },\
"video" : {"file" : "broll_ts2family_outside.mp4"}\
})

configs["episodes"].append(\
{ "title": "hd5770 6850",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:18.4", "00:25.7" ), "volume" : 0.999, "padAudio" : 0.25 },\
"video" : {"file" : "broll_ts2_family_outside_takingTurns.mp4", "start" : "00:20"}\
})

configs["episodes"].append(\
{ "title": "hd6670",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:25.7", "00:32.5" ), "volume" : 0.999, "padAudio" : 0.25 },\
"video" : {"file" : "broll_ts2_family_outside_takingTurns.mp4", "start" : "00:40"}\
})

configs["episodes"].append(\
{ "title": "hd5870",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:32.5", "00:40" ), "volume" : 0.999, "padAudio" : 0.25 },\
"video" : {"file" : "broll_ts2_family_outside_takingTurns.mp4", "start" : "00:02"}\
})

configs["episodes"].append(\
{ "title": "Z230",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:40", "00:55" ), "volume" : 0.999, "padAudio" : 0.25 },\
"video" : {"file" : "Z230_closed.mp4" , "rotation" : 180}\
})

configs["episodes"].append(\
{ "title": "GT 1030",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:55", "01:03.6" ), "volume" : 0.999, "padAudio" : 0.25 },\
"video" : {"file" : "breel_Gt1030LP_outside.mp4"}\
})



configs["episodes"].append(\
{ "title": "1920x1080 results",\
"audio" : {"timestamps" : ("01:03.6", "02:04" )  },\
"video" : {"file": "stock_cs2_CT_gt1030lp.mp4"},\
"overlay" : { \
    "image" : {"file" : "1080, low settings.png", "chromaColor" : "0x00FF00"}\
}, \
})

configs["episodes"].append(\
{ "title": "1280x720 results",\
"audio" : {"timestamps" : ("02:04", "02:56" )  },\
"video" : {"file": "stock_cs2_T_gt1030lp.mp4"},\
"overlay" : { \
    "image" : {"file" : "720, low settings.png", "chromaColor" : "0x00FF00"}\
}, \
})

configs["episodes"].append(\
{ "title": "The cake is a lie",\
"audio" : {"timestamps" : ("02:56", "03:16"), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file": "Gigabyte_HD5770_GpuZ_phone.mp4"},\
})

configs["episodes"].append(\
{ "title": "family 2",\
"isChapter" : False,\
"audio" : {"timestamps" : ("03:16", "03:31.5"), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "broll_ts2family_outside.mp4"}\
})

configs["episodes"].append(\
{ "title": "Counter Strike 2",\
"isChapter" : False,\
"audio" : {"timestamps" : ("03:31.5", "04:01"), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "stock_cs2_T_gt1030lp.mp4"},\
"overlay" : { \
    "text" : ["'Counter Strike 2 on a GT 1030'",\
              scriptedvided.r6sText('1920x1080, low settings, 100% render scale', 88, 48), \
]}, \
})

configs["episodes"].append(\
{ "title": "GCN family - entry level",\
"isChapter" : False,\
"audio" : {"timestamps" : ("04:01", "04:14.8"), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "gcn_entry_level_cards_asus.mp4"}\
})

configs["episodes"].append(\
{ "title": "Bye",\
"isChapter" : False,\
"audio" : {"timestamps" : ("04:14.8", "04:23"), "volume" : 0.999 , "padAudio" : 0.25 },\
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
