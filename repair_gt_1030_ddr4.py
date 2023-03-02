import scriptedvided

configs = { "defaultAudioFile" : "repair_1030_ddr4.ogg",\
"mediaFolder" : "C:\\Users\\Admin\\Videos\\repair_gt_1030_ddr4", \
"stockFolder" : "C:\\Users\\Admin\\Videos\stock",\
"benchmarkFile" : None,\
"outputFolder" : "C:\\Users\\Admin\\Videos\\repair_gt_1030_ddr4\\output", \
"outputFile" : "repair_gt_1030_ddr4.mp4", \
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "H:\\Muzica\\royalty free\\Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3",\
"timestamps" : ("00:30", None ), "destinationTimestamp" : {"title" : "The TLDW: PEX_RESET", "until" : "Soldering done, does it work"}}, \
{"file" : "H:\\Muzica\\royalty free\\bensound-summer.mp3", "timestamps" : ("00:00", None ), "destinationTimestamp" : { "title": "Soldering done, does it work", "until" : "Blooper" }}, \
], "volume" : 0.05 },\
"episodes" : [],\
"youtube" : {"title" : "An easy repair for the DDR4 GT 1030", \
"description" : '''We added a couple of components to this defective DDR4 to bring it back to life.''',\
"links" : '''
Our review of the DDR4 GT 1030: 
https://youtu.be/gI98DutuIis

Repair channels:
https://www.youtube.com/c/LearnElectronicsRepair
https://www.youtube.com/channel/UCKU5nwSWYXa3xfXGBlKyvdw
https://www.youtube.com/c/TechCemetery
https://www.youtube.com/c/TheCod3r
''', \
"tags" : "NVidia,GT 1030,GT1030,GeForce,Pascal,GPU repair,PEX_RESET,PEX RESET,RESET",\
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
{ "title": "The TLDW: PEX_RESET",\
"audio" : {"timestamps" : ("00:00", "00:14" ), "volume" : 0.999 },\
"video" : "gt_1030_ddr4_bb_V_alorant.mp4"\
})

configs["episodes"].append(\
{ "title": "The adventure starts with an ad",\
"audio" : {"timestamps" : ("00:14", "00:26.5" ), "volume" : 0.999 },\
"video" : {"file": "GT1030_ddr4_olx_ad.mkv"},\
})

configs["episodes"].append(\
{ "title": "Visual inspection of the board",\
"audio" : {"timestamps" : ("00:26.5", "00:52" ), "volume" : 0.999 },\
"video" : "gt_1030_ddr4_missing_components.mkv",\
})

configs["episodes"].append(\
{ "title": "Resistance checks",\
"audio" : {"timestamps" : ("00:52" , "01:13.5"), "volume" : 0.999 },\
"video" : {"file" : "ddr4_1030_resistanceCheckOnInputVoltage.mkv", "start" : "00:00"}\
})

configs["episodes"].append(\
{ "title": "PCIE_lanes - fwd voltage drop",\
"isChapter" : False, \
"audio" : {"timestamps" : ("01:13.5", "01:34.5"), "volume" : 0.999 },\
"video" : {"file" : "ddr4_1030_resCheckPCIELanes.mkv"}\
})

configs["episodes"].append(\
{ "title": "GDDR5 and DDR4",\
"isChapter" : False, \
"audio" : {"timestamps" : ("01:34.5", "01:55"), "volume" : 0.999 },\
"video" : {"file" : "gt_1030_side_by_side.mp4"}\
})

configs["episodes"].append(\
{ "title": "Two types of PEX_RESET wiring",\
"audio" : {"timestamps" : ( "01:55", "02:32.65"), "volume" : 0.999 },\
"video" : {"file" : "pex_reset.mkv"}\
})


## keep this one
configs["episodes"].append(\
{ "title": "960 reset",\
"isChapter" : False, \
"audio" : {"timestamps" : ("02:32.65", "02:42.65"), "volume" : 0.999 },\
"video" : {"file" : "gtx_960_pex_reset.mkv", }\
})

configs["episodes"].append(\
{ "title": "Donor board 0 ohm",\
"isChapter" : False, \
"audio" : {"timestamps" : ("02:42.65", "03:08"), "volume" : 0.999 },\
"video" : {"file" : "gtx960_donor_0OhmResistor.mp4", }\
})

configs["episodes"].append(\
{ "title": "Soldering done, does it work",\
"audio" : {"timestamps" : ("03:08", "03:18"), "volume" : 0.999 },\
"video" : {"file" : "gt_1030_ddr4_fixes_notCleaned_zoom.mp4", }\
})

configs["episodes"].append(\
{ "title": "reassembled",\
"isChapter" : False, \
"audio" : {"timestamps" : ("03:18", "03:29"), "volume" : 0.999 },\
"video" : {"file" : "gt_1030_ddr4_bb_card_only.mp4", }\
})


configs["episodes"].append(\
{ "title": "Will it work - powerup",\
"isChapter" : False, \
"audio" : {"timestamps" : ("03:29", "03:42"), "volume" : 0.999 },\
"video" : {"file" : "gt_1030_ddr4_powerup.mp4", "start" : "00:00"}\
})

configs["episodes"].append(\
{ "title": "Will it work - proba",\
"isChapter" : False, \
"audio" : {"timestamps" : ("03:42", "03:48.4"), "volume" : 0.999 },\
"video" : {"file" : "GT_1030_proba_2.mp4", }\
})

configs["episodes"].append(\
{ "title": "Will it work - driver",\
"isChapter" : False, \
"audio" : {"timestamps" : ("03:48.4", "03:52"), "volume" : 0.999 },\
"video" : {"file" : "gtx770_driverInstall.mp4", "start" : "01:19"}\
})

configs["episodes"].append(\
{ "title": "Will it work - gaming",\
"isChapter" : False, \
"audio" : {"timestamps" : ("03:52", "04:04.5"), "volume" : 0.999 },\
"video" : {"file" : "gt_1030_ddr4_bb_O_verwatch2.mp4", }\
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


