import scriptedvided

configs = { "defaultAudioFile" : "Tahiti_level_1.ogg",\
"mediaFolder" : "F:\\Videos\\Tahiti_level_1", \
"stockFolder" : "F:\\Videos\\stock",\
"outputFolder" : "F:\\Videos\\Tahiti_level_1\\output", \
"outputFile" : "Tahiti_level_1.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "Which one to pick", "until" : "Doom Eternal"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Doom Eternal", "until" : "Performance values (important)"}}, \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "Performance values (important)", "until" : "Conclusions"}}, \
{"file" : "Guide You Home - Ferco and Andie - Free Background Music - Audio Library Release.ogg", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "Conclusions", "until" : "Blooper"}}, \
], "volume" : 0.06 },\
"episodes" : [],\
"youtube" : {"title" : "How I would pick an used GPU (GTX 1050 Ti, GTX 960, GTX 770, R9 280)", \
"description" : '''In this video, I'm doing a bit of a dive into my local used parts market, and provide a method to navigate it.''',\
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
"tags" : "Doom Eternal,Far Cry 6,Resident Evil 4,Control,Battlefield V,Apex Legends,Counter Strike 2,Fortnite,The Finals,GTX960,GTX 960,GTX1050Ti,GTX 1050Ti,GTX 1050 Ti,GTX770,GTX 770,R9 280,AMD,NVidia,Radeon,GeForce",\
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
{ "title": "Which one to pick",\
"audio" : {"timestamps" : ("00:00", "00:19.7" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "broll_GTX1050Ti_960_770_R9_280.mp4", "start":"00:00", "rotation" : 90},\
})

# meeds better video, or maybe break it up
configs["episodes"].append(\
{ "title": "Value - the metric to choose by",\
"audio" : {"timestamps" : ("00:19.7", "00:50.5" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "stock_DOOMEternal_2023_12_26.mp4", "start" : "00:22"},\
"overlay" : { \
    "image" : {"file" : "definition of performance.png", "chromaColor" : "0x00FF00"}\
}})

#this is not the Z230
configs["episodes"].append(\
{ "title": "Z230",\
"audio" : {"timestamps" : ("00:50.5", "01:01.75" ), "volume" : 0.999, "padAudio" : 0.1 },\
"overlay" : { \
    "text" : ["'Z230 workstation from HP'",\
              "'CPU\: E3-1241v3 Xeon (i7 4770 equivalent)'",\
              "'RAM\: 32GB DDR3 at 1600 MHz, dual channel'",\
    ]\
}, \
"isChapter" : False, \
"video" : {"file" : "Z230_closed.mp4", "rotation" : 180}\
})

configs["episodes"].append(\
{ "title": "settings",\
"isChapter" : False, \
"audio" : {"timestamps" : ("01:01.75", "01:11" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "stock_DOOMEternal_2023_12_26.mp4", "start" : "01:22"},\
})

configs["episodes"].append(\
{ "title": "Doom Eternal",\
"audio" : {"timestamps" : ("01:11", "01:32.7" ), "padAudio" : 0.1 },\
"video" : {"file" : "stock_DOOMEternal_2023_12_26.mp4", "start" : "03:35"},\
"overlay" : { \
    "image" : {"file" : "Doom Eternal - 1080, low settings.png", "chromaColor" : "0x00FF00"}\
}, \
})

configs["episodes"].append(\
{ "title": "Resident Evil 4",\
"audio" : {"timestamps" : ("01:32.7", "01:48.3" ), "padAudio" : 0.1 },\
"video" : {"file": "stock_re4demo_choppyExceptCutscenes.mp4", "start" : "03:07"},\
"overlay" : { \
    "image" : {"file" : "Resident Evil 4 (remake) - 1080, low settings.png", "chromaColor" : "0x00FF00"}\
}, \
})

configs["episodes"].append(\
{ "title": "Far Cry 6",\
"audio" : {"timestamps" : ("01:48.3", "02:05.2" ), "padAudio" : 0.1 },\
"video" : {"file" : "stock_FarCry6_benchmark.mp4"},\
"overlay" : { \
    "image" : {"file" : "Far Cry 6 - 1080, low settings.png", "chromaColor" : "0x00FF00"}\
}, \
})

configs["episodes"].append(\
{ "title": "Control",\
"audio" : {"timestamps" : ("02:05.2", "02:18.3" ), "padAudio" : 0.1 },\
"video" : {"file" : "stock_Control_R9_270.mp4", "start" : "01:55"},\
"overlay" : { \
    "image" : {"file" : "Control - 1080, low settings.png", "chromaColor" : "0x00FF00"}\
}, \
})

configs["episodes"].append(\
{ "title": "DX11 quite alive in multi player",\
"audio" : {"timestamps" : ("02:18.3", "02:38.6" ), "padAudio" : 0.1 },\
"video" : {"file" : "Victory_leaderboard_W-O-T.mp4"},\
})

configs["episodes"].append(\
{ "title": "Battlefield V",\
"audio" : {"timestamps" : ("02:38.6", "02:51.8" ), "padAudio" : 0.1 },\
"video" : {"file" : "stock_bfv_MpTraining.mp4"},\
"overlay" : { \
    "image" : {"file" : "Battlefield V - 1080, low settings.png", "chromaColor" : "0x00FF00"}\
}, \
})

configs["episodes"].append(\
{ "title": "Apex Legends",\
"audio" : {"timestamps" : ("02:51.8", "03:05.4" ), "padAudio" : 0.1 },\
"video" : {"file" : "stock_ApexLegends_720p.mp4"},\
"overlay" : { \
    "image" : {"file" : "Apex Legends - 1080, low settings.png", "chromaColor" : "0x00FF00"}\
}, \
})

configs["episodes"].append(\
{ "title": "Counter Strike 2",\
"audio" : {"timestamps" : ("03:05.4", "03:24" ), "padAudio" : 0.1 },\
"video" : {"file" : "stock_cs2_R9_270_ct.mp4"},\
"overlay" : { \
    "image" : {"file" : "Counter Strike 2 - 1080, low settings.png", "chromaColor" : "0x00FF00"}\
}, \
})

configs["episodes"].append(\
{ "title": "Fortnite",\
"audio" : {"timestamps" : ("03:24", "03:40.7" ), "padAudio" : 0.1 },\
"video" : {"file" : "stock_Fortnite_c5s1.mp4", "start" : "01:00"},\
"overlay" : { \
    "image" : {"file" : "Fortnite - 1080, low settings.png", "chromaColor" : "0x00FF00"}\
}, \
})

configs["episodes"].append(\
{ "title": "The Finals",\
"audio" : {"timestamps" : ("03:40.7", "03:58.2" ), "padAudio" : 0.1 },\
"video" : {"file" : "stock_Finals_2023_12_27_winners.mp4" , "start" : "02:37"},\
"overlay" : { \
    "image" : {"file" : "low settings.png", "chromaColor" : "0x00FF00"}\
}, \
})

configs["episodes"].append(\
{ "title": "Performance values (important)",\
"audio" : {"timestamps" : ("03:58.2", "04:27.9" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "broll_GTX1050Ti_960_770_R9_280.mp4", "start":"00:00", "rotation" : 90},\
"overlay" : { \
    "image" : {"file" : "Total average FPS.png", "chromaColor" : "0x00FF00"}\
}, \
})

configs["episodes"].append(\
{ "title": "Pricing",\
"audio" : {"timestamps" : ("04:27.9", "04:48.35" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "olx-search-R9-280-converted.mp4", "start":"00:00"},\
})

configs["episodes"].append(\
{ "title": "Pricing - values",\
"isChapter" : False,\
"audio" : {"timestamps" : ("04:48.35", "05:13.5" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "broll_GTX1050Ti_960_770_R9_280.mp4", "start":"00:00", "rotation" : 90},\
"overlay" : { \
    "image" : {"file" : "Average price  [USD].png", "chromaColor" : "0x00FF00"}\
}, \
})

configs["episodes"].append(\
{ "title": "Value metric (FPS per USD)",\
"audio" : {"timestamps" : ("05:13.5", "05:46.6" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "stock_DOOMEternal_2023_12_26.mp4"},\
"overlay" : { \
    "image" : {"file" : "Value (Average FPS per USD) - higher is better.png", "chromaColor" : "0x00FF00"}\
}, \
})

configs["episodes"].append(\
{ "title": "Overvalued or a good deal",\
"audio" : {"timestamps" : ("05:46.6", "06:26" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "breel_GTX770_GTX960_R9280_attic.mp4"},\
"overlay" : { \
    "image" : {"file" : "Actual price vs. expected price [USD].png", "chromaColor" : "0x00FF00"}\
}, \
})

configs["episodes"].append(\
{ "title": "Conclusions",\
"audio" : {"timestamps" : ("06:26", "06:57" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "gtx960_R9_280_OLX.mkv"},\
})

configs["episodes"].append(\
{ "title": "sub and bye",\
"audio" : {"timestamps" : ("06:57", "07:10" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "broll_GTX1050Ti_960_770_R9_280.mp4", "start":"00:00", "rotation" : 90},\
"isChapter" : False,\
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


