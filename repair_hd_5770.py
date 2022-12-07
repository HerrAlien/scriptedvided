import scriptedvided

configs = { "defaultAudioFile" : "repair_hd5770_reference.ogg",\
"mediaFolder" : "C:\\Users\\Admin\\Videos\\repair HD 5770", \
"stockFolder" : "C:\\Users\\Admin\\Videos\stock",\
"benchmarkFile" : None,\
"outputFolder" : "C:\\Users\\Admin\\Videos\\repair HD 5770\\output", \
"outputFile" : "repair_hd_5770.mp4", \
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "H:\\Muzica\\royalty free\\Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3",\
"timestamps" : ("00:30", None ), "destinationTimestamp" : {"title" : "The TLDW", "until" : "Power-up sequence needs work"}}, \
{"file" : "H:\\Muzica\\royalty free\\Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3",\
"timestamps" : ("00:30", None ), "destinationTimestamp" : {"title" : "Power-up sequence needs work", "until" : "Does it work now?"}}, \
{"file" : "H:\\Muzica\\royalty free\\bensound-summer.mp3", "timestamps" : ("00:00", None ), "destinationTimestamp" : { "title": "Does it work now?", "until" : "Blooper" }}, \
], "volume" : 0.05 },\
"episodes" : [],\
"youtube" : {"title" : "Reviving and old DX11 video card (AMD Radeon HD 5770)", \
"description" : '''We used just two resistors to get another video card to work, by fixing the PEX_RESET and power up sequencing circuits.''',\
"links" : '''


Repair channels:
https://www.youtube.com/c/LearnElectronicsRepair
https://www.youtube.com/channel/UCKU5nwSWYXa3xfXGBlKyvdw
https://www.youtube.com/c/TechCemetery
https://www.youtube.com/c/TheCod3r
''', \
"tags" : "AMD,ATI,Radeon,TeraScale 2,HD5770,HD 5770,PEX_RESET,PEX RESET,RESET",\
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
{ "title": "The TLDW",\
"audio" : {"timestamps" : ("00:00", "00:20" ), "volume" : 0.999 },\
"video" : "hd5770_refDesign_breel.mp4"\
})

configs["episodes"].append(\
{ "title": "The adventure starts with the auction site",\
"audio" : {"timestamps" : ("00:20", "00:39.7" ), "volume" : 0.999 },\
"video" : {"file": "olx_ad_gtx770_hd5770.mkv"},\
})

configs["episodes"].append(\
{ "title": "The GTX 770",\
"isChapter" : False, \
"audio" : {"timestamps" : ("00:39.7", "00:48.6"), "volume" : 0.999 },\
"video" : {"file" : "gtx770_bb_V_alorant.mp4", "start" : "00:00" }\
})

configs["episodes"].append(\
{ "title": "The Radeon",\
"isChapter" : False, \
"audio" : {"timestamps" : ("00:48.6", "00:52"), "volume" : 0.999 },\
"video" : {"file" : "hd5770_refDesign_breel.mp4"}\
})

configs["episodes"].append(\
{ "title": "Visual inspection of the board",\
"audio" : {"timestamps" : ("00:52", "01:05" ), "volume" : 0.999 },\
"video" : "initial_visual_inspection.mp4",\
})

configs["episodes"].append(\
{ "title": "Resistance checks",\
"audio" : {"timestamps" : ( "01:05" , "01:22.3"), "volume" : 0.999 },\
"video" : {"file" : "hd5770_resistance_measurements.mkv"}\
})


configs["episodes"].append(\
{ "title": "First time powering it up",\
"audio" : {"timestamps" : ( "01:22.3", "01:37.2"), "volume" : 0.999 },\
"video" : {"file" : "hd5770_powerupAfterResetFix-nogo.mp4", "start": "00:25"}\
})

configs["episodes"].append(\
{ "title": "PEX_RESET woes",\
"audio" : {"timestamps" : ("01:37.2", "01:51" ), "volume" : 0.999 },\
"video" : {"file" : "gt_1030_ddr4_missing_components.mkv", "start":"00:14"},\
})

configs["episodes"].append(\
{ "title": "the PEX_RESET circuitry",\
"isChapter" : False, \
"audio" : {"timestamps" : ("01:51", "02:06.8"), "volume" : 0.999 },\
"video" : {"file" : "comparison_pex_resets.mp4"}\
})

configs["episodes"].append(\
{ "title": "pads for the alternative circuit",\
"isChapter" : False, \
"audio" : {"timestamps" : ("02:06.8", "02:30.5"), "volume" : 0.999 },\
"video" : {"file" : "r104_nicepads.mkv"}\
})

configs["episodes"].append(\
{ "title": "the donor boards",\
"isChapter" : False, \
"audio" : {"timestamps" : ("02:30.5", "02:39"), "volume" : 0.999 },\
"video" : {"file" : "960_volunteer_compressed.mp4"}\
})

configs["episodes"].append(\
{ "title": "searched for a 0 ohm resistor",\
"isChapter" : False, \
"audio" : {"timestamps" : ("02:39", "02:50"), "volume" : 0.999 },\
"video" : {"file" : "0Ohm_donor.mkv"}\
})

configs["episodes"].append(\
{ "title": "the 0 ohm resistor in place",\
"isChapter" : False, \
"audio" : {"timestamps" : ("02:50", "03:09.5"), "volume" : 0.999 },\
"video" : {"file" : "hd5770_reset_now_goes_to_gpu.mp4", "start" : "00:00"}\
})

configs["episodes"].append(\
{ "title": "check the voltage drop",\
"isChapter" : False, \
"audio" : {"timestamps" : ("03:09.5", "03:20"), "volume" : 0.999 },\
"video" : {"file" : "hd5770_reset_now_goes_to_gpu.mp4", "start" : "00:10"}\
})

configs["episodes"].append(\
{ "title": "PEX_RESET fixed, but does it work?",\
"audio" : {"timestamps" : ( "03:20", "03:49.5"), "volume" : 0.999 },\
"video" : {"file" : "hd5770_powerupAfterResetFix-nogo.mp4", "start" : "00:30"}\
})

configs["episodes"].append(\
{ "title": "Power-up sequence needs work",\
"audio" : {"timestamps" : ( "03:49.5", "04:08.8"), "volume" : 0.999 },\
"video" : {"file" : "power_gating.mkv"}\
})

configs["episodes"].append(\
{ "title": "the phase controller",\
"isChapter" : False, \
"audio" : {"timestamps" : ("04:08.8", "04:26"), "volume" : 0.999 },\
"video" : {"file" : "powerup_schematics_and_pcb.mkv"}\
})

configs["episodes"].append(\
{ "title": "the power up circuitry",\
"isChapter" : False, \
"audio" : {"timestamps" : ("04:26", "05:00.2"), "volume" : 0.999 },\
"video" : {"file" : "vddc_en_suspects.mkv"}\
})

configs["episodes"].append(\
{ "title": "powered up the card again measuring",\
"isChapter" : False, \
"audio" : {"timestamps" : ("05:00.2", "06:15.5"), "volume" : 0.999 },\
"video" : {"file" : "3v3_does_npot_open_q1017.mkv"}\
})

configs["episodes"].append(\
{ "title": "resistance between the base of Q1017 and the 3V3 input",\
"isChapter" : False, \
"audio" : {"timestamps" : ("06:15.5", "06:35.3"), "volume" : 0.999 },\
"video" : {"file" : "3v3_pu_measures_6k.mkv"}\
})

configs["episodes"].append(\
{ "title": "a pair of empty pads",\
"isChapter" : False, \
"audio" : {"timestamps" : ("06:35.3", "07:03"), "volume" : 0.999 },\
"video" : {"file" : "hd5770_missingPUResistor-zoomed.mp4"}\
})

configs["episodes"].append(\
{ "title": "any value between 1k and 2k7",\
"isChapter" : False, \
"audio" : {"timestamps" : ( "07:03", "07:20"), "volume" : 0.999 },\
"video" : {"file" : "vddc_en_suspects.mkv"}\
})

configs["episodes"].append(\
{ "title": "2k2 resistors in the DVI output circuitry",\
"isChapter" : False, \
"audio" : {"timestamps" : ( "07:20", "07:36"), "volume" : 0.999 },\
"video" : {"file" : "2k2_resistor.mkv"}\
})

configs["episodes"].append(\
{ "title": "placed the 2k2 resistor",\
"isChapter" : False, \
"audio" : {"timestamps" : ( "07:36", "07:48"), "volume" : 0.999 },\
"video" : {"file" : "2k2_resistor_soldered.mp4", "rotate":"180"}\
})

configs["episodes"].append(\
{ "title": "Does it work now?",\
"audio" : {"timestamps" : ("07:48", "08:01"), "volume" : 0.999 },\
"video" : {"file" : "hd5770_refDesign_itWorks.mp4", "start":"00:13"}\
})

configs["episodes"].append(\
{ "title": "Heaven",\
"isChapter" : False, \
"audio" : {"timestamps" : ( "08:01", "08:15"), "volume" : 0.999 },\
"video" : {"file" : "hd5770_refDesign_gpuz_specs_heaven.mp4","start":"01:00"}\
})

configs["episodes"].append(\
{ "title": "Happy ending",\
"isChapter" : False, \
"audio" : {"timestamps" : ( "08:15", "08:37"), "volume" : 0.999 },\
"video" : {"file" : "hd5770_refDesign_breel.mp4"}\
})

configs["episodes"].append(\
{ "title": "Blooper",\
"isChapter" : False, \
"audio" : {"timestamps" : ("08:37", "08:47.2"), "volume" : 0.999 },\
"video" : {"file" : "hd5770_missingPUResistor-zoomed.mp4"}\
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


