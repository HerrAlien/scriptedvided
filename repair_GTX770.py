import scriptedvided

configs = { "defaultAudioFile" : "repair_gtx770.ogg",\
"mediaFolder" : "F:\\Videos\\repair_gtx770", \
"stockFolder" : "F:\\Videos\\stock",\
"benchmarkFile" : None,\
"outputFolder" : "F:\\Videos\\repair_gtx770\\output", \
"outputFile" : "repair_gtx770.mp4", \
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3",\
"timestamps" : ("00:30", None ), "destinationTimestamp" : {"title" : "TLDW", "until" : "Add back the components"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3",\
"timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Add back the components", "until" : "The MOSFETs get too hot"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3",\
"timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "The MOSFETs get too hot", "until" : "no more artifacts"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3",\
"timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "no more artifacts", "until" : "The power sequence circuit issue"}}, \
{"file" : "Soulful - Dave Osorio [Audio Library Release]-Free Copyright-safe Music.mp3",\
"timestamps" : ("00:30", None ), "destinationTimestamp" : {"title" : "The power sequence circuit issue", "until" : "Final power-up"}}, \
{"file" : "bensound-summer.mp3", "timestamps" : ("00:00", None ), "destinationTimestamp" : { "title": "Final power-up", "until" : "Blooper" }}, \
], "volume" : 0.03 },\
"episodes" : [],\
"youtube" : {"title" : "Repairing the power delivery and undervolting the VRAM on an NVidia GTX 770", \
"description" : '''This HerculeZ 2000 version of the GTX 770 required trace repair work, putting back a handful of components, and even undervolting the VRAM to get it to work properly.
This was an adventure filled with lessons for me: I learned about why using filtering capacitors for the internal reference voltages in phase controllers is a good idea, why doing proper compensation on phase controllers is a good idea and so on.
So, grab your favourite snack, a hot beverage and a blanket, and curl in a comfortable armchair or couch - this story is long.
''',\
"links" : '''
Our review of the GTX 770: 
https://www.youtube.com/watch?v=DhvJv9Ea5WE

Other repair channels that I like:
https://www.youtube.com/c/LearnElectronicsRepair
https://www.youtube.com/channel/UCKU5nwSWYXa3xfXGBlKyvdw
https://www.youtube.com/c/TechCemetery
https://www.youtube.com/@northwestrepair
''', \
"tags" : "NVidia,GTX 770,GTX730,GeForce,Kepler,PCB,trace repair,GPU repair",\
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
{ "title": "TLDW",\
"audio" : {"timestamps" : ("00:00", "00:42" ), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : "gtx770_bb_W_arzone.mp4"\
})


configs["episodes"].append(\
{ "title": "Everything started like usual, with an ad",\
"audio" : {"timestamps" : ("00:42", "01:40"), "volume" : 0.999, "padAudio" : 0.25 },\
"video" : {"file" : "olx_ad_gtx770_hd5770.mkv"}\
})


configs["episodes"].append(\
{ "title": "Resistance measurements",\
"audio" : {"timestamps" : ("01:40", "02:04"), "volume" : 0.999, "padAudio" : 0.25 },\
"video" : {"file" : "gtx770_resistance_measurement.mkv"}\
})

##### set a better start for video below
configs["episodes"].append(\
{ "title": "Voltage measurements and visual inspection",\
"audio" : {"timestamps" : ("02:04", "02:35"), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "visual_inspection.mp4", "rotation" : 90, "start" : "00:55"}\
})

configs["episodes"].append(\
{ "title": "visual inspection - closer look",\
"isChapter" : False, \
"audio" : {"timestamps" : ("02:35", "02:58"), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "most_missing_components.mkv"}\
})

configs["episodes"].append(\
{ "title": "Identify the missing components",\
"audio" : {"timestamps" : ("02:58", "03:45"), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "missing_components_ppt.mkv"}\
})

configs["episodes"].append(\
{ "title": "GPU phase controller woes",\
"isChapter" : False, \
"audio" : {"timestamps" : ("03:45", "04:10"), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "missing_components_daughterboard_ppt.mkv"}\
})

configs["episodes"].append(\
{ "title": "Add back the components",\
"audio" : {"timestamps" : ("04:10", "04:42.1"), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "gtx770_traceFixForResistor.mp4"}\
})

configs["episodes"].append(\
{ "title": "Repair the trace for the 10 nF cap",\
"isChapter" : False, \
"audio" : {"timestamps" : ("04:42.1", "04:56"), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "gtx770_placedResistorOnFixedTrace.mp4"}\
})

configs["episodes"].append(\
{ "title": "The 10k resistors",\
"isChapter" : False, \
"audio" : {"timestamps" : ("04:56", "05:12.1"), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "main_pcb_all_in_place.mp4"}\
})

configs["episodes"].append(\
{ "title": "The daughter board",\
"isChapter" : False, \
"audio" : {"timestamps" : ("05:12.1", "05:24.5"), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "daughter_board_all_in_place.mp4"}\
})

configs["episodes"].append(\
{ "title": "sorceForFirstCap",\
"isChapter" : False, \
"audio" : {"timestamps" : ("05:24.5", "05:44.8"), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "gtx770_sorceForFirstCap.mp4"}\
})

configs["episodes"].append(\
{ "title": "Voltage measurements two",\
"audio" : {"timestamps" : ("05:44.8", "06:19"), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "rt8802A_and_pcb.mkv"}\
})

configs["episodes"].append(\
{ "title": "Voltage measurements two - enable",\
"isChapter" : False, \
"audio" : {"timestamps" : ("06:19", "07:02"), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "schematics with the enable.mkv"}\
})

configs["episodes"].append(\
{ "title": "measure the actual voltages - EN",\
"isChapter" : False, \
"audio" : {"timestamps" : ("07:02", "07:19"), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "video with slide with actual values.mkv"}\
})

configs["episodes"].append(\
{ "title": "Hard-wiring the enable",\
"audio" : {"timestamps" : ("07:19", "07:48"), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "back to the diagram.mkv"}\
})


configs["episodes"].append(\
{ "title": "Third power-up",\
"audio" : {"timestamps" : ("07:48", "08:09.3"), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "gtx770_noSignalDVI.mp4"}\
})

configs["episodes"].append(\
{ "title": "The MOSFETs get too hot",\
"audio" : {"timestamps" : ("08:09.3", "08:37.4"), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "gtx770_driverInstall.mp4"}\
})

configs["episodes"].append(\
{ "title": "Bad 2.2 nF MLCC",\
"isChapter" : False, \
"audio" : {"timestamps" : ("08:37.4", "09:06.4"), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "back to the daughter board.mkv"}\
})

configs["episodes"].append(\
{ "title": "searching for another 2.2 nF MLCC",\
"isChapter" : False, \
"audio" : {"timestamps" : ("09:06.4", "10:06.8"), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "search for 2n2 mlcc.mkv"}\
})

configs["episodes"].append(\
{ "title": "Artefacts. Great.",\
"audio" : {"timestamps" : ("10:06.8", "10:34"), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "gtx770_artefacts_windows.mp4"}\
})

configs["episodes"].append(\
{ "title": "Monitoring the voltage during boot",\
"isChapter" : False, \
"audio" : {"timestamps" : ("10:34", "11:00"), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "artefacting_allowed_vram_voltage.mkv"}\
})

configs["episodes"].append(\
{ "title": "datasheet for the memory phase controller",\
"isChapter" : False, \
"audio" : {"timestamps" : ("11:00", "11:27.6"), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "missing_5v_decopling_mlcc.mkv"}\
})

configs["episodes"].append(\
{ "title": "get an MLCC and solder it in place",\
"isChapter" : False, \
"audio" : {"timestamps" : ("11:27.6", "11:53"), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "gtx770_lift10uF_Mlcc_From960_better.mp4"}\
})

configs["episodes"].append(\
{ "title": "no more artifacts",\
"isChapter" : False, \
"audio" : {"timestamps" : ("11:53", "12:12.5"), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "gtx770_crashInHeaven.mp4"}\
})

configs["episodes"].append(\
{ "title": "until I played Warframe",\
"isChapter" : False, \
"audio" : {"timestamps" : ("12:12.5", "12:23.3"), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "gtx770_W_arframe_temps.mp4"}\
})

configs["episodes"].append(\
{ "title": "Yet again artefacts",\
"isChapter" : False, \
"audio" : {"timestamps" : ("12:23.3", "12:33"), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "gtx770_artefacts_windows.mp4"}\
})

configs["episodes"].append(\
{ "title": "Unfair phase loading",\
"audio" : {"timestamps" : ("12:33", "13:05.4"), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "gtx770_heaven_3.mp4"}\
})

configs["episodes"].append(\
{ "title": "not a 60-40 split",\
"isChapter" : False, \
"audio" : {"timestamps" : ("13:05.4", "13:21.3"), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "gtx770_unbalancedLoads.mp4"}\
})

configs["episodes"].append(\
{ "title": "Problems piled up",\
"audio" : {"timestamps" : ("13:21.3", "13:52"), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "issues_piling_up_start_34.mkv"}\
})

configs["episodes"].append(\
{ "title": "Tackling the power balance issue",\
"audio" : {"timestamps" : ("13:52", "14:31.6"), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "power balancing issue 2R2 resistor.mkv"}\
})

configs["episodes"].append(\
{ "title": "Tackling the power balance issue - nope",\
"isChapter" : False, \
"audio" : {"timestamps" : ("14:31.6", "14:37"), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "gtx770_unbalancedLoads.mp4"}\
})

configs["episodes"].append(\
{ "title": "Finding a fix for the artifacting",\
"audio" : {"timestamps" : ("14:37", "15:05"), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "gtx770_cooling.mp4"}\
})

configs["episodes"].append(\
{ "title": "Put up a review video for the card",\
"audio" : {"timestamps" : ("15:05", "15:19"), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "review_gtx770.mkv"}\
})

configs["episodes"].append(\
{ "title": "Again with the artefacts",\
"audio" : {"timestamps" : ("15:19", "15:38"), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "gtx770_noArtefactsUntilDriverLoad.mp4", "start" : -20, "rotation" : 180 }\
})

configs["episodes"].append(\
{ "title": "The power sequence circuit issue",\
"audio" : {"timestamps" : ("15:38", "16:00"), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "hd5770_refDesign_itWorks.mp4"}\
})

configs["episodes"].append(\
{ "title": "No resistor at all",\
"isChapter" : False, \
"audio" : {"timestamps" : ("16:00", "16:28"), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "no resistor at all.mkv"}\
})

configs["episodes"].append(\
{ "title": "8K resistor from the Lenovo IH61M motherboard",\
"isChapter" : False, \
"audio" : {"timestamps" : ("16:28", "16:48"), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "powerup_adding_missing_resistor.mp4"}\
})

configs["episodes"].append(\
{ "title": "Undervolting the VRAM",\
"audio" : {"timestamps" : ("16:48", "18:17.5"), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "design_different_mem_voltage.mkv"}\
})

configs["episodes"].append(\
{ "title": "lower this in-load voltage",\
"isChapter" : False, \
"audio" : {"timestamps" : ("18:17.5", "18:39.5"), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "Only one way to find out.mkv"}\
})

configs["episodes"].append(\
{ "title": "Final power-up",\
"audio" : {"timestamps" : ("18:39.5", "19:04"), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "gtx770_driverInstall.mp4", "start" : "01:26"}\
})

configs["episodes"].append(\
{ "title": "The card powered up fine",\
"isChapter" : False, \
"audio" : {"timestamps" : ("19:04", "19:26"), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "gtx770_Heaven_after_fix.mp4"}\
})

configs["episodes"].append(\
{ "title": "Blooper",\
"isChapter" : False, \
"audio" : {"timestamps" : ("19:26", "19:48"), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "gtx770_artefacts_windows.mp4"}\
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


