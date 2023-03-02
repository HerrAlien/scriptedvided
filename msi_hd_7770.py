import scriptedvided

configs = { "defaultAudioFile" : "r7770-pmd1gd5.ogg",\
"mediaFolder" : "C:\\Users\\Admin\\Videos\\msi_hd7770", \
"stockFolder" : "C:\\Users\\Admin\\Videos\stock",\
"benchmarkFile" : None,\
"outputFolder" : "C:\\Users\\Admin\\Videos\\msi_hd7770\\output", \
"outputFile" : "msi_hd7770.mp4", \
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "H:\\Muzica\\royalty free\\Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3",\
"timestamps" : ("00:30", None ), "destinationTimestamp" : {"title" : "TLDW: it ran after baking it", "until" : "Learn Electronics Repair"}}, \
{"file" : "H:\\Muzica\\royalty free\\Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3",\
"timestamps" : ("00:30", None ), "destinationTimestamp" : {"title" : "Diagnosis 1 - measure resistances on power rails", "until" : "Fan issue: it's mechanical ... right?"}}, \
{"file" : "H:\\Muzica\\royalty free\\Bitters At The Saloon - Bird Creek (No Copyright Music).ogg",\
"timestamps" : ("00:30", None ), "destinationTimestamp" : {"title" : "Fan issue: it's mechanical ... right?", "until" : "Fixed with the superglue and baking soda trick"}}, \
{"file" : "H:\\Muzica\\royalty free\\Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3",\
"timestamps" : ("00:30", None ), "destinationTimestamp" : {"title" : "Fixed with the superglue and baking soda trick", "until" : "Back to a VBIOS issue"}}, \
{"file" : "H:\\Muzica\\royalty free\\Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3",\
"timestamps" : ("00:30", None ), "destinationTimestamp" : {"title" : "Diagnosis 4 - the VBIOS chip", "until" : "Let's bake it."}}, \
{"file" : "H:\\Muzica\\royalty free\\Bitters At The Saloon - Bird Creek (No Copyright Music).ogg",\
"timestamps" : ("00:30", None ), "destinationTimestamp" : {"title" : "Let's bake it.", "until" : "Not the fix I was hoping for"}}, \
{"file" : "H:\\Muzica\\royalty free\\bensound-summer.mp3", "timestamps" : ("00:00", None ), "destinationTimestamp" : { "title": "Not the fix I was hoping for", "until" : "end of the video" }}, \
], "volume" : 0.03 },\
"episodes" : [],\
"youtube" : {"title" : "The story of the not so dead MSI Radeon HD 7770", \
"description" : '''This MSI HD 7770 had a few issues; while the diagnostics was performed properly, the fix ended up being rudimentary.''',\
"links" : '''
Our review of the HD 7770: https://www.youtube.com/watch?v=4rEcNy2YC0I

Repair channels:
https://www.youtube.com/c/LearnElectronicsRepair
https://www.youtube.com/channel/UCKU5nwSWYXa3xfXGBlKyvdw
https://www.youtube.com/c/TechCemetery
https://www.youtube.com/c/TheCod3r


Other resources used:
Oiling fans: https://www.youtube.com/watch?v=jtK62UPKgdY
LER: https://www.youtube.com/watch?v=vPFo5XHuQkQ
Superglue and baking soda: https://www.youtube.com/watch?v=Av2GqHxCA2Q
Jensen promo for new cards: https://www.youtube.com/watch?v=So7TNRhIYJ8
''', \
"tags" : "AMD,Radeon,R7 250X,HD 7770, HD7770,GCN,GCN 1.0,cooking cards,baking card in oven,oven baking method,cooking,PCB,card,oven,GPU repair",\
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
{ "title": "TLDW: it ran after baking it",\
"audio" : {"timestamps" : ("00:00", "00:24.08" ), "volume" : 0.999 },\
"video" : "msi_hd7770_heaven.mp4"\
})

configs["episodes"].append(\
{ "title": "The adventure starts",\
"audio" : {"timestamps" : ("00:24.08", "00:42.03" ), "volume" : 0.999 },\
"video" : {"file": "r7770-pmd1gd5-fanspin.MOV", "rotation" : 180},\
})

configs["episodes"].append(\
{ "title": "The ad",\
"audio" : {"timestamps" : ("00:42.03", "01:19.91" ), "volume" : 0.999 },\
"isChapter" : False, \
"video" : "olx_ad.mkv",\
})

##configs["episodes"].append(\
##{ "title": "Cooling solution - axial",\
##"audio" : {"timestamps" : ("01:46", "02:07" ), "volume" : 0.9 },\
##"video" : "r7_260_1.mov",\
##"overlay" : { \
##    "text" : ["'Example of a cooler using axial fans'",\
##              "'(ASUS Radeon R7 260)'"]\
##}, \
##"isChapter" : False,\
##})


configs["episodes"].append(\
{ "title": "Checking the symptoms as mentioned in the ad",\
"audio" : {"timestamps" : ("01:19.91", "01:29.12" ), "volume" : 0.999  },\
"video" : "msi_not_detected2.MOV",\
})

configs["episodes"].append(\
{ "title": "Symptom - fan twitch",\
"audio" : {"timestamps" : ("01:29.12", "01:47.33" ), "volume" : 0.999  },\
"isChapter" : False, \
"video" : {"file": "Fan twitches.MOV", "start": "00:00"},\
})

configs["episodes"].append(\
{ "title": "Learn Electronics Repair",\
"audio" : {"timestamps" : ("01:47.33", "02:01.16" ), "volume" : 0.999  },\
"isChapter" : False, \
"video" : "LER.mkv",\
})

configs["episodes"].append(\
{ "title": "Diagnosis 1 - measure resistances on power rails",\
"audio" : {"timestamps" : ("02:01.16", "02:24.62" ), "volume" : 0.999  },\
"video" : "r7770-pmd1gd5_power.mkv",\
})

configs["episodes"].append(\
{ "title": "Diagnosis 2 - check for voltages and control signals",\
"audio" : {"timestamps" : ("02:24.62", "02:38" ), "volume" : 0.999  },\
"video" : "r7770-pmd1gd5_labeled_signals.mkv",\
})

configs["episodes"].append(\
{ "title": "Surprise! It powers up!",\
"audio" : {"timestamps" : ("02:38", "03:14.91" ), "volume" : 0.999  },\
"video" : "Fan twitches.MOV",\
})


configs["episodes"].append(\
{ "title": "Diagnosis 3 - fan not running",\
"audio" : {"timestamps" : ("03:14.91", "03:29.11" ), "volume" : 0.999  },\
"video" : "PWM_signal_on_diagram.mkv",\
})


configs["episodes"].append(\
{ "title": "Diagnosis 3 - PWM is there",\
"audio" : {"timestamps" : ("03:29.11", "03:46.2" ), "volume" : 0.999  },\
"video" : "PWM is there.MOV",\
"isChapter" : False, \
})

configs["episodes"].append(\
{ "title": "Diagnosis 3 - MSI Afterburner manual fan control",\
"audio" : {"timestamps" : ("03:46.2", "04:05.95" ), "volume" : 0.999  },\
"video" : "MSI Afterburner manual fan c_ontrol.mkv",\
"isChapter" : False, \
})

configs["episodes"].append(\
{ "title": "Fan issue: it's mechanical ... right?",\
"audio" : {"timestamps" : ("04:05.95", "04:46.91" ), "volume" : 0.999  },\
"video" : "fan_oiling.mkv",\
})


configs["episodes"].append(\
{ "title": "Fixed with the superglue and baking soda trick",\
"audio" : {"timestamps" : ("04:46.91", "05:01.5" ), "volume" : 0.999  },\
"video" : "superglue baking soda.mkv",\
"isChapter" : False, \
})


configs["episodes"].append(\
{ "title": "Fan issue: it's an electrical issue",\
"audio" : {"timestamps" : ("05:01.5", "05:47" ), "volume" : 0.999  },\
"video" : {"file": "r7770-pmd1gd5-fanspin.MOV", "rotation" : 180},\
})

configs["episodes"].append(\
{ "title": "SPICE",\
"audio" : {"timestamps" : ("05:47", "06:16" ), "volume" : 0.999  },\
"video" : "pwm_circuit_spice.mkv",\
"isChapter" : False, \
})


configs["episodes"].append(\
{ "title": "Fan controller, glued in",\
"audio" : {"timestamps" : ("06:16", "06:54" ), "volume" : 0.999  },\
"video" : {"file" : "fan controller, glued in.mp4", "rotation" : 90},\
"isChapter" : False, \
})

configs["episodes"].append(\
{ "title": "And all was good. Right?",\
"audio" : {"timestamps" : ("06:54", "07:07" ), "volume" : 0.999  },\
"video" : "msi_hd7770_heaven.mp4",\
})

configs["episodes"].append(\
{ "title": "Back to a VBIOS issue",\
"audio" : {"timestamps" : ("07:07", "07:37" ), "volume" : 0.70  },\
"video" : "No video card detected.mkv",\
})

configs["episodes"].append(\
{ "title": "Diagnosis 4 - the VBIOS chip",\
"audio" : {"timestamps" : ("07:37", "07:50" ), "volume" : 0.999  },\
"video" : "w25x20cl_bios_datasheet.mkv",\
})

configs["episodes"].append(\
{ "title": "BIOS chip signals",\
"audio" : {"timestamps" : ("07:50", "07:59.32" ), "volume" : 0.999  },\
"video" : "r7770-pmd1gd5-BIOS chip signals.mkv",\
"isChapter" : False, \
})

configs["episodes"].append(\
{ "title": "msi hd 7770 CS",\
"audio" : {"timestamps" : ("07:59.32", "08:14" ), "volume" : 0.999  },\
"video" : {"file" : "msi hd 7770 #CS.mp4", "rotation" : -90},\
"isChapter" : False, \
})

configs["episodes"].append(\
{ "title": "VBIOS circuit",\
"audio" : {"timestamps" : ("08:14", "09:07" ), "volume" : 0.999  },\
"video" : "VBIOS circuit.mkv",\
"isChapter" : False, \
})

configs["episodes"].append(\
{ "title": "The GPU is not soldered down properly",\
"audio" : {"timestamps" : ("09:07", "09:55" ), "volume" : 0.999  },\
"video" : "r7770-pmd1gd5-tracing #CS.mkv",\
})

configs["episodes"].append(\
{ "title": "Let's bake it.",\
"audio" : {"timestamps" : ("09:55", "10:12.4" ), "volume" : 0.999  },\
"video" : "jensen_oven.mkv",\
})

configs["episodes"].append(\
{ "title": "Prepare the card for baking",\
"audio" : {"timestamps" : ("10:12.4", "10:29" ), "volume" : 0.999  },\
"video" : {"file": "prepared_for_baking.MOV", "rotation" : 90},\
"isChapter" : False, \
})

configs["episodes"].append(\
{ "title": "Not the fix I was hoping for",\
"audio" : {"timestamps" : ("10:29", "10:40.07" ), "volume" : 0.999  },\
"video" : {"file": "IMG_0058.MOV", "rotation" : 90},\
})

configs["episodes"].append(\
{ "title": "Mishaps are a thing, so be careful",\
"audio" : {"timestamps" : ("10:40.07", "10:52" ), "volume" : 0.999  },\
"video" : "hd6850_exploded caps.mp4",\
"isChapter" : False, \
})

configs["episodes"].append(\
{ "title": "The R7770-PMD1GD5 lives",\
"audio" : {"timestamps" : ("10:52", "11:25" ), "volume" : 0.999  },\
"video" : "msi_hd7770_breel.MOV",\
"isChapter" : False, \
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


