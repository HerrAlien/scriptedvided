import scriptedvided

configs = { "defaultAudioFile" : "repair_r9_280.ogg",\
"mediaFolder" : "C:\\Users\\Admin\\Videos\\repair_r9_280", \
"stockFolder" : "C:\\Users\\Admin\\Videos\stock",\
"benchmarkFile" : None,\
"outputFolder" : "C:\\Users\\Admin\\Videos\\repair_r9_280\\output", \
"outputFile" : "repair_r9_280.mp4", \
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "H:\\Muzica\\royalty free\\Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3",\
"timestamps" : ("00:00", None ), "destinationTimestamp" : {"title" : "TLDW", "until" : "R9 280 runs as good as new"}}, \
{"file" : "H:\\Muzica\\royalty free\\bensound-summer.mp3", "timestamps" : ("00:00", None ), "destinationTimestamp" : { "title": "R9 280 runs as good as new", "until" : "end of the video" }}, \
], "volume" : 0.05 },\
"episodes" : [],\
"youtube" : {"title" : "Getting an R9 280 to run as new", \
"description" : '''This R9 280 decided to throw a few surprises at me after doing maintenance on it, but we managed to get it to run as good as new.''',\
"links" : '''
Our review of the R9 280: https://www.youtube.com/watch?v=9e9vjrRv5ho

Repairing the MSI HD 7770: https://www.youtube.com/watch?v=eqpQWX8f4Nw

Repair channels:
https://www.youtube.com/c/LearnElectronicsRepair
https://www.youtube.com/channel/UCKU5nwSWYXa3xfXGBlKyvdw
https://www.youtube.com/c/TechCemetery
https://www.youtube.com/c/TheCod3r

''', \
"tags" : "AMD,Radeon,R9 280,Sapphire,MLCC,artifacting,crashes,PWM,controller,fan,cooling",\
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
"audio" : {"timestamps" : ("00:00", "00:10.6" ), "volume" : 0.999 },\
"video" : "R9_280_r7r9_background.mp4",\
})

configs["episodes"].append(\
{ "title": "Short history of the card",\
"audio" : {"timestamps" : ( "00:10.6", "00:29" ), "volume" : 0.999 },\
"video" : {"file" : "r9_280_solo.MOV", "rotation" : 180},\
})

configs["episodes"].append(\
{ "title": "Symptoms after performing maintenance",\
"audio" : {"timestamps" : ( "00:29", "00:42.8" ), "volume" : 0.999 },\
"video" : "R9_280_PINK_TRAY.mp4",\
})

configs["episodes"].append(\
{ "title": "Symptoms - artefacts",\
"audio" : {"timestamps" : ("00:42.8", "00:57.1" ), "volume" : 0.999 },\
"video" : "GPU_artifacts.mkv",\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Step 1 - Resistance measurements",\
"audio" : {"timestamps" : ( "00:57.1", "01:29" ), "volume" : 0.999 },\
"video" : "r9_280_resistance_measurementrs.mkv",\
})

configs["episodes"].append(\
{ "title": "Step 2 - Measure voltages",\
"audio" : {"timestamps" : ( "01:29", "01:51" ), "volume" : 0.999 },\
"video" : {"file" : "r9_280_voltage_measurements.mp4", "start" : "00:10"},\
})

configs["episodes"].append(\
{ "title": "Everything is fine - but with artefacts",\
"audio" : {"timestamps" : (  "01:51", "01:56" ), "volume" : 0.999 },\
"video" : "GPU_artifacts.mkv",\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Should have been step 1 - visual inspection",\
"audio" : {"timestamps" : ( "01:56", "02:21.2" ), "volume" : 0.999 },\
"video" : "r9_280_bad_mlcc.mkv",\
})

configs["episodes"].append(\
{ "title": "First fix attempt",\
"audio" : {"timestamps" : ( "02:21.2", "02:36" ), "volume" : 0.999 },\
"video" : "r9_280_bad_mlcc_removed.mkv",\
})

configs["episodes"].append(\
{ "title": "Behavior after MLCC removed",\
"audio" : {"timestamps" : ( "02:36", "02:48.3" ), "volume" : 0.999 },\
"video" : "r9_280_heaven_phone.mp4",\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Symptoms - bad thermals",\
"audio" : {"timestamps" : ( "02:48.3", "03:00" ), "volume" : 0.999 },\
"video" : "r9_280_thermals.mp4",\
})

configs["episodes"].append(\
{ "title": "Cause of thermal issues",\
"audio" : {"timestamps" : ( "03:00", "03:23.8" ), "volume" : 0.999 },\
"video" : "r9_280_r_6_s.mp4",\
})

configs["episodes"].append(\
{ "title": "A case of deja vu",\
"audio" : {"timestamps" : ( "03:23.8", "03:40" ), "volume" : 0.999 },\
"video" : "external_pwm_circuit_fix_fans.mkv",\
})

configs["episodes"].append(\
{ "title": "msi afterburner",\
"audio" : {"timestamps" : ( "03:40", "03:55.2" ), "volume" : 0.999 },\
"video" : "MSI Afterburner manual fan c_ontrol.mkv",\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "LTSPICE",\
"audio" : {"timestamps" : ("03:55.2", "04:07.3" ), "volume" : 0.999 },\
"video" : "pwm_circuit_spice.mkv",\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Reusing one of my tricks",\
"audio" : {"timestamps" : ("04:07.3", "04:31.5" ), "volume" : 0.999 },\
"video" : "external_PWM_circuit.mkv",\
})

configs["episodes"].append(\
{ "title": "R9 280 runs as good as new",\
"audio" : {"timestamps" : ( "04:31.5", "04:52" ), "volume" : 0.999 },\
"video" : "r9_280_c_o_n_t_r_o_l.mp4",\
})

configs["episodes"].append(\
{ "title": "Testing and conclusion",\
"audio" : {"timestamps" : ( "04:52" , "05:16" ), "volume" : 0.999 },\
"video" : "r9_280_r_6_s.mp4",\
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


