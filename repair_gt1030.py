import scriptedvided

configs = { "defaultAudioFile" : "repair_gt_1030.ogg",\
"mediaFolder" : "C:\\Users\\Admin\\Videos\\repair_gt1030", \
"stockFolder" : "C:\\Users\\Admin\\Videos\stock",\
"benchmarkFile" : None,\
"outputFolder" : "C:\\Users\\Admin\\Videos\\repair_gt1030\\output", \
"outputFile" : "repair_gt1030.mp4", \
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "H:\\Muzica\\royalty free\\Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3",\
"timestamps" : ("00:00", None ), "destinationTimestamp" : {"title" : "The adventure starts on the auction site", "until" : "The fix - repaired trace"}}, \
{"file" : "H:\\Muzica\\royalty free\\bensound-summer.mp3", "timestamps" : ("00:00", None ), "destinationTimestamp" : { "title": "The fix - repaired trace", "until" : "end of the video" }}, \
], "volume" : 0.05 },\
"episodes" : [],\
"youtube" : {"title" : "Bringing a GT 1030 back to life", \
"description" : '''This GT 1030 looked like it was used as a donor board. The fix for it turned out to be trivial.''',\
"links" : '''
Our review of the GT 1030: https://youtu.be/6Dmbuq5KZto

Repair channels:
https://www.youtube.com/c/LearnElectronicsRepair
https://www.youtube.com/channel/UCKU5nwSWYXa3xfXGBlKyvdw
https://www.youtube.com/c/TechCemetery
https://www.youtube.com/c/TheCod3r

''', \
"tags" : "NVIDIA,GeForce,GT1030,GT 1030,Pascal,PCB,card,GPU repair,trace repair",\
"language" : "EN", \
"Caption certification" : "None",\
"recording date" : None,\
"video location" : None, \
"category" : "Science & Technology", \
"subtitles" : None, \
"endscreen" : None, \
"cards" : None, \
}\
}

configs["episodes"].append(\
{ "title": "The adventure starts on the auction site",\
"audio" : {"timestamps" : ("00:00", "00:23.42" ), "volume" : 0.999 },\
"video" : "gt1030_olx_ad.mkv",\
})

configs["episodes"].append(\
{ "title": "Visual inspection",\
"audio" : {"timestamps" : ( "00:23.42", "00:40.33" ), "volume" : 0.999 },\
"video" : "gt1030_scratches.mkv",\
})

configs["episodes"].append(\
{ "title": "Visual inspection - resoldered caps",\
"audio" : {"timestamps" : ( "00:40.33", "00:50" ), "volume" : 0.999 },\
"video" : "gt1030_resoldered_caps.mkv",\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Visual inspection - memory caps",\
"audio" : {"timestamps" : ( "00:50", "01:08.5" ), "volume" : 0.999 },\
"video" : "gt1030_memory_caps.mkv",\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Step 1 - Measure resistances",\
"audio" : {"timestamps" : ( "01:08.5", "01:28" ), "volume" : 0.999 },\
"video" : "things to check unpowered.mkv",\
})

configs["episodes"].append(\
{ "title": "Step 1 ok",\
"audio" : {"timestamps" : (  "01:28", "01:44.4" ), "volume" : 0.999 },\
"video" : "resistances ok.mkv",\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Step 2 - Measure voltages",\
"audio" : {"timestamps" : ( "01:44.4", "02:26.3" ), "volume" : 0.999 },\
"video" : "gt1030_voltages.mkv",\
})

configs["episodes"].append(\
{ "title": "Diagnosis for missing voltage",\
"audio" : {"timestamps" : ( "02:26.3", "02:57" ), "volume" : 0.999 },\
"video" : "diagram of the regulator.mkv",\
})

configs["episodes"].append(\
{ "title": "Diagnosis - list of suspects",\
"audio" : {"timestamps" : ( "02:57", "03:33" ), "volume" : 0.999 },\
"video" : "ppt with suspects.mkv",\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Diagnosis - resistors",\
"audio" : {"timestamps" : ( "03:33", "03:51.4" ), "volume" : 0.999 },\
"video" : "feedback resistors.mkv",\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Diagnosis - input voltage",\
"audio" : {"timestamps" : ( "03:51.4", "04:19" ), "volume" : 0.999 },\
"video" : "show the 1117.mkv",\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Diagnosis - trace the EN trace",\
"audio" : {"timestamps" : ( "04:19", "04:58.75" ), "volume" : 0.999 },\
"video" : "trace EN.mkv",\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "The fix - repaired trace",\
"audio" : {"timestamps" : ( "04:58.75", "05:38.63" ), "volume" : 0.999 },\
"video" : {"file":"fixed_trace.MOV", "rotation": 90},\
})

configs["episodes"].append(\
{ "title": "Testing and conclusion",\
"audio" : {"timestamps" : ( "05:38.63" , "05:56" ), "volume" : 0.999 },\
"video" : "gt1030_breel_game.MOV",\
})

configs["episodes"].append(\
{ "title": "GT 1030 running heaven",\
"audio" : {"timestamps" : ( "05:56", "06:14" ), "volume" : 0.999 },\
"video" : "fixed_GT1030_heaven.MOV",\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Unknown past of the GT 1030",\
"audio" : {"timestamps" : ( "06:14", "06:47" ), "volume" : 0.999 },\
"video" : "gt1030_breel_game.MOV",\
"isChapter" : False,\
})


#scriptedvided.makeVideoForEpisode(configs["episodes"][27], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][9], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][8], configs)
#print(scriptedvided.makeVideoForEpisode(configs["episodes"][9], configs))
#print(scriptedvided.getSuitableVideoStream(configs["episodes"][9], configs))
#print (configs["youtube"])
#print(scriptedvided.getMusicCreditsString(configs["backgroundTrack"]))
#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "Fan controller, glued in"][0], configs)
scriptedvided.makeVideo(configs)


