import scriptedvided

configs = { "defaultAudioFile" : "repair_gt730.ogg",\
"mediaFolder" : "C:\\Users\\Admin\\Videos\\repair_FermiGT730", \
"stockFolder" : "C:\\Users\\Admin\\Videos\stock",\
"benchmarkFile" : None,\
"outputFolder" : "C:\\Users\\Admin\\Videos\\repair_FermiGT730\\output", \
"outputFile" : "repair_FermiGT730.mp4", \
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "H:\\Muzica\\royalty free\\Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3",\
"timestamps" : ("00:30", None ), "destinationTimestamp" : {"title" : "TLDW: a dead GTX 960 saved a GT 730", "until" : "Fixing PCIE lane 11 (going PCIE x16)"}}, \
{"file" : "H:\\Muzica\\royalty free\\Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3",\
"timestamps" : ("00:30", None ), "destinationTimestamp" : {"title" : "Fixing PCIE lane 11 (going PCIE x16)", "until" : "A working card"}}, \
{"file" : "H:\\Muzica\\royalty free\\bensound-summer.mp3", "timestamps" : ("00:00", None ), "destinationTimestamp" : { "title": "A working card", "until" : "Blooper" }}, \
], "volume" : 0.03 },\
"episodes" : [],\
"youtube" : {"title" : "Doing board repair for a Fermi GT 730", \
"description" : '''Fixed PCIE traces and placed back ripped components on a Fermi GF-108 based GT 730.''',\
"links" : '''
Our review of the Fermi-based GT 730: 
https://youtu.be/-1eIjIxfx0k

Repair channels:
https://www.youtube.com/c/LearnElectronicsRepair
https://www.youtube.com/channel/UCKU5nwSWYXa3xfXGBlKyvdw
https://www.youtube.com/c/TechCemetery
https://www.youtube.com/c/TheCod3r
''', \
"tags" : "NVidia,GT 730,GT730,GeForce,Fermi,Kepler,PCB,trace repair,GPU repair",\
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
{ "title": "TLDW: a dead GTX 960 saved a GT 730",\
"audio" : {"timestamps" : ("00:00", "00:18" ), "volume" : 0.999 },\
"video" : "FermiGT730_breel_wGame.mp4"\
})

configs["episodes"].append(\
{ "title": "The adventure starts with an ad",\
"audio" : {"timestamps" : ("00:18", "00:29.5" ), "volume" : 0.999 },\
"video" : {"file": "gt730_ad.mkv", "rotation" : 0},\
})

configs["episodes"].append(\
{ "title": "Fermi? In a GT 730?",\
"audio" : {"timestamps" : ("00:29.5", "00:48" ), "volume" : 0.999 },\
"video" : "730_family_2.mkv",\
})

configs["episodes"].append(\
{ "title": "Visual inspection",\
"audio" : {"timestamps" : ("00:48" , "01:27.5"), "volume" : 0.999 },\
"video" : {"file" : "card_and_issues_on_it.mp4", "start" : "01:00"}\
})

configs["episodes"].append(\
{ "title": "Schematic with inductor beads",\
"isChapter" : False, \
"audio" : {"timestamps" : ("01:27.5", "01:41"), "volume" : 0.999 },\
"video" : {"file" : "usage_of_inductors.mkv", "start" : "00:20"}\
})

configs["episodes"].append(\
{ "title": "pcie lanes issues",\
"isChapter" : False, \
"audio" : {"timestamps" : ( "01:41", "02:10"), "volume" : 0.999 },\
"video" : {"file" : "card_and_issues_on_it.mp4", "start" : "00:40"}\
})

configs["episodes"].append(\
{ "title": "Resistance measurements",\
"audio" : {"timestamps" : ( "02:10", "02:28"), "volume" : 0.999 },\
"video" : {"file" : "gt730_voltageRails.mkv", }\
})

configs["episodes"].append(\
{ "title": "Fixes for the back of the GPU area",\
"audio" : {"timestamps" : ( "02:28", "03:01"), "volume" : 0.999 },\
"video" : {"file" : "gt730_back_gpu_fixes.mkv", "start" : "00:00"}\
})

configs["episodes"].append(\
{ "title": "First picture, PCIE x4",\
"audio" : {"timestamps" : ("03:01", "03:35"), "volume" : 0.999 },\
"video" : {"file" : "gt730_first_image.mp4", "start" : "00:40"}\
})

configs["episodes"].append(\
{ "title": "Fixing PCIE lane 6 (going PCIE x8)",\
"audio" : {"timestamps" : ("03:35", "04:04"), "volume" : 0.999 },\
"video" : {"file" : "scraping_traces_lane6.mp4", "start" : "00:10"}\
})

configs["episodes"].append(\
{ "title": "Tinning PCIE lane 6",\
"isChapter" : False, \
"audio" : {"timestamps" : ("04:04", "04:13.3"), "volume" : 0.999 },\
"video" : {"file" : "tinning_lane6.mp4", "start" : "00:15"}\
})

configs["episodes"].append(\
{ "title": "Lane 6 fixed",\
"isChapter" : False, \
"audio" : {"timestamps" : ( "04:13.3", "04:34"), "volume" : 0.999 },\
"video" : {"file" : "fixes_macro.mp4", "start" : "00:00"}\
})

configs["episodes"].append(\
{ "title": "Fixing PCIE lane 11 (going PCIE x16)",\
"audio" : {"timestamps" : ( "04:34", "05:03.9"), "volume" : 0.999 },\
"video" : {"file" : "scraping_traces_lane11.mp4", "start" : "01:10"}\
})

configs["episodes"].append(\
{ "title": "Tinning PCIE lane 11",\
"isChapter" : False, \
"audio" : {"timestamps" : ("05:03.9", "05:32"), "volume" : 0.999 },\
"video" : {"file" : "tinning_lane11.mp4", "start" : "01:40"}\
})

configs["episodes"].append(\
{ "title": "Check the fixed PCIE lanes",\
"audio" : {"timestamps" : ("05:32", "05:47.8"), "volume" : 0.999 },\
"video" : {"file" : "fixes_macro.mp4", }\
})

configs["episodes"].append(\
{ "title": "voltage drop, lane to ground",\
"isChapter" : False, \
"audio" : {"timestamps" : ("05:47.8", "06:03"), "volume" : 0.999 },\
"video" : {"file" : "gt730_lane2gnd.mkv", "start" : "00:00"}\
})

configs["episodes"].append(\
{ "title": "voltage drop, lane to lane",\
"isChapter" : False, \
"audio" : {"timestamps" : ("06:03", "06:16.5"), "volume" : 0.999 },\
"video" : {"file" : "gt730_lane2lane.mkv", "start" : "00:00" }\
})

configs["episodes"].append(\
{ "title": "Sanity checks 2",\
"isChapter" : False, \
"audio" : {"timestamps" : ("06:16.5", "06:25.7"), "volume" : 0.999 },\
"video" : {"file" : "gt730_voltageRails.mkv", }\
})

configs["episodes"].append(\
{ "title": "A working card",\
"audio" : {"timestamps" : ("06:25.7", "07:17"), "volume" : 0.999 },\
"video" : "Fermi_GT730_GPU_Z.mkv"\
})

configs["episodes"].append(\
{ "title": "Final touches",\
"isChapter" : False, \
"audio" : {"timestamps" : ("07:17", "07:31"), "volume" : 0.999 },\
"video" : {"file" : "GT730_finishing_touches_2.mp4", "start" : "00:21" }\
})

configs["episodes"].append(\
{ "title": "Heaven",\
"isChapter" : False, \
"audio" : {"timestamps" : ("07:31", "07:49"), "volume" : 0.999 },\
"video" : {"file" : "FermiGT730_Heaven.mp4", }\
})

configs["episodes"].append(\
{ "title": "Blooper",\
"isChapter" : False, \
"audio" : {"timestamps" : ("07:49", "08:04.45"), "volume" : 0.999 },\
"video" : {"file" : "gt730_fermi_gpu.mp4", }\
})


#scriptedvided.makeVideoForEpisode(configs["episodes"][27], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][9], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][8], configs)
#print(scriptedvided.makeVideoForEpisode(configs["episodes"][9], configs))
#print(scriptedvided.getSuitableVideoStream(configs["episodes"][9], configs))
#print (configs["youtube"])
#print(scriptedvided.getMusicCreditsString(configs["backgroundTrack"]))
#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "Lane 6 fixed"][0], configs)
scriptedvided.makeVideo(configs)


