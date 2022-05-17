import scriptedvided

configs = { "defaultAudioFile" : "msi_hd7770.ogg",\
"mediaFolder" : "C:\\Users\\Admin\\Videos\\msi_hd7770", \
"stockFolder" : "C:\\Users\\Admin\\Videos\stock",\
"benchmarkFile" : None,\
"outputFolder" : "C:\\Users\\Admin\\Videos\\msi_hd7770\\output", \
"outputFile" : "msi_hd7770.mp4", \
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "H:\\Muzica\\royalty free\\Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3",\
"timestamps" : ("00:30", None ), "destinationTimestamp" : {"title" : "TLDW: we baked it in the oven", "until" : "Apex Legends"}}, \
{"file" : "H:\\Muzica\\royalty free\\bensound-summer.mp3", "timestamps" : ("00:00", None ), "destinationTimestamp" : { "title": "Usefulness of used GPUs", "until" : "end of the video" }}, \
], "volume" : 0.03 },\
"episodes" : [],\
"youtube" : {"title" : "The dead MSI HD 7770 was not so dead after all", \
"description" : '''This MSI HD 7770 had a few issues; while the diagnostics was performed properly, the fix ended up being rudimentary.''',\
"links" : '''
Our review of the HD 7770: https://www.youtube.com/watch?v=4rEcNy2YC0I

Repair channels:
https://www.youtube.com/c/LearnElectronicsRepair
https://www.youtube.com/channel/UCKU5nwSWYXa3xfXGBlKyvdw
https://www.youtube.com/c/TechCemetery
https://www.youtube.com/c/TheCod3r


Intel 11th gen processors:
The core i5 11400 (has an IGPU): https://ark.intel.com/content/www/us/en/ark/products/212270/intel-core-i511400-processor-12m-cache-up-to-4-40-ghz.html
The core i5 11400F (no IGPU): https://ark.intel.com/content/www/us/en/ark/products/212271/intel-core-i511400f-processor-12m-cache-up-to-4-40-ghz.html

Other resources used:
Electronic Arts at AMD Radeon Graphics Tech Day: https://www.youtube.com/watch?v=pVFp1aamKyM
Oiling fans https://www.youtube.com/watch?v=jtK62UPKgdY
LER https://www.youtube.com/watch?v=vPFo5XHuQkQ
Superglue baking soda https://www.youtube.com/watch?v=Av2GqHxCA2Q
https://www.youtube.com/watch?v=VZqf5rOJNCE
''', \
"tags" : "AMD,Radeon,R7 250X,HD 7770, HD7770,GCN,GCN 1.0",\
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
"audio" : {"timestamps" : ("00:00", "00:45" ), "volume" : 0.999 },\
"video" : "msi_hd7770_heaven.mp4"\
})

configs["episodes"].append(\
{ "title": "The adventure starts",\
"audio" : {"timestamps" : ("00:45", "01:28" ), "volume" : 0.999 },\
"video" : "R7770-PMD1GD5-product-page.mkv",\
})

configs["episodes"].append(\
{ "title": "The ad",\
"audio" : {"timestamps" : ("01:28", "01:46" ), "volume" : 0.999 },\
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
"audio" : {"timestamps" : ("03:18", "04:01" ), "volume" : 0.97  },\
"video" : "msi_not_detected2.MOV",\
})

configs["episodes"].append(\
{ "title": "Symptom - fan twitch",\
"audio" : {"timestamps" : ("03:18", "04:01" ), "volume" : 0.97  },\
"isChapter" : False, \
"video" : "Fan twitches.MOV",\
})

configs["episodes"].append(\
{ "title": "Learn Electronics Repair",\
"audio" : {"timestamps" : ("03:18", "04:01" ), "volume" : 0.97  },\
"isChapter" : False, \
"video" : "LER.mkv",\
})

configs["episodes"].append(\
{ "title": "Diagnosis 1 - measure resistances on power rails",\
"audio" : {"timestamps" : ("03:18", "04:01" ), "volume" : 0.97  },\
"video" : "r7770-pmd1gd5_power.mkv",\
})

configs["episodes"].append(\
{ "title": "Diagnosis 2 - check for voltages and control signals",\
"audio" : {"timestamps" : ("03:18", "04:01" ), "volume" : 0.97  },\
"video" : "r7770-pmd1gd5_labeled_signals.mkv",\
})

configs["episodes"].append(\
{ "title": "Surprise! It powers up!",\
"audio" : {"timestamps" : ("03:18", "04:01" ), "volume" : 0.97  },\
"video" : "Fan twitches.MOV",\
})


configs["episodes"].append(\
{ "title": "Diagnosis 3 - fan not running",\
"audio" : {"timestamps" : ("03:18", "04:01" ), "volume" : 0.97  },\
"video" : "PWM_signal_on_diagram.mkv",\
})


configs["episodes"].append(\
{ "title": "Diagnosis 3 - PWM is there",\
"audio" : {"timestamps" : ("03:18", "04:01" ), "volume" : 0.97  },\
"video" : "PWM is there.MOV",\
"isChapter" : False, \
})

configs["episodes"].append(\
{ "title": "Diagnosis 3 - MSI Afterburner manual fan control",\
"audio" : {"timestamps" : ("03:18", "04:01" ), "volume" : 0.97  },\
"video" : "MSI Afterburner manual fan control.mkv",\
"isChapter" : False, \
})

configs["episodes"].append(\
{ "title": "Fan issue: it's mechanical ... right?",\
"audio" : {"timestamps" : ("03:18", "04:01" ), "volume" : 0.97  },\
"video" : "fan_oiling.mkv",\
})


configs["episodes"].append(\
{ "title": "Fixed with the superglue and baking soda",\
"audio" : {"timestamps" : ("03:18", "04:01" ), "volume" : 0.97  },\
"video" : "superglue baking soda.mkv",\
"isChapter" : False, \
})

configs["episodes"].append(\
{ "title": "Fixed with the superglue and baking soda",\
"audio" : {"timestamps" : ("03:18", "04:01" ), "volume" : 0.97  },\
"video" : "superglue baking soda.mkv",\
"isChapter" : False, \
})

configs["episodes"].append(\
{ "title": "Fan issue: it's an electrical issue",\
"audio" : {"timestamps" : ("03:18", "04:01" ), "volume" : 0.97  },\
"video" : "r7770-pmd1gd5-fanspin.MOV",\
})

configs["episodes"].append(\
{ "title": "Fan controller, glued in",\
"audio" : {"timestamps" : ("03:18", "04:01" ), "volume" : 0.97  },\
"video" : "fan controller, glued in.mp4",\
"isChapter" : False, \
})

configs["episodes"].append(\
{ "title": "And all was good. Right?",\
"audio" : {"timestamps" : ("03:18", "04:01" ), "volume" : 0.97  },\
"video" : "msi_hd7770_heaven.mp4",\
})

configs["episodes"].append(\
{ "title": "Back to a VBIOS issue",\
"audio" : {"timestamps" : ("03:18", "04:01" ), "volume" : 0.97  },\
"video" : "TBD TBD",\
})

configs["episodes"].append(\
{ "title": "Diagnosis 4 - the VBIOS chip",\
"audio" : {"timestamps" : ("03:18", "04:01" ), "volume" : 0.97  },\
"video" : "w25x20cl_bios_datasheet.mkv",\
})

configs["episodes"].append(\
{ "title": "BIOS chip signals",\
"audio" : {"timestamps" : ("03:18", "04:01" ), "volume" : 0.97  },\
"video" : "r7770-pmd1gd5-BIOS chip signals.mkv",\
"isChapter" : False, \
})

configs["episodes"].append(\
{ "title": "msi hd 7770 CS",\
"audio" : {"timestamps" : ("03:18", "04:01" ), "volume" : 0.97  },\
"video" : "msi hd 7770 #CS.mp4",\
"isChapter" : False, \
})

configs["episodes"].append(\
{ "title": "VBIOS circuit",\
"audio" : {"timestamps" : ("03:18", "04:01" ), "volume" : 0.97  },\
"video" : "VBIOS circuit.mkv",\
"isChapter" : False, \
})

configs["episodes"].append(\
{ "title": "The GPU is not soldered down properly",\
"audio" : {"timestamps" : ("03:18", "04:01" ), "volume" : 0.97  },\
"video" : "r7770-pmd1gd5-tracing #CS.mkv",\
})

configs["episodes"].append(\
{ "title": "Let's bake it.",\
"audio" : {"timestamps" : ("03:18", "04:01" ), "volume" : 0.97  },\
"video" : "jensen_oven.mkv",\
})

configs["episodes"].append(\
{ "title": "Prepare the card for baking",\
"audio" : {"timestamps" : ("03:18", "04:01" ), "volume" : 0.97  },\
"video" : "prepared_for_baking.MOV",\
"isChapter" : False, \
})

configs["episodes"].append(\
{ "title": "Not the fix I was hoping for",\
"audio" : {"timestamps" : ("03:18", "04:01" ), "volume" : 0.97  },\
"video" : "IMG_0058.MOV",\
})

configs["episodes"].append(\
{ "title": "Mishaps are a thing, so be careful",\
"audio" : {"timestamps" : ("03:18", "04:01" ), "volume" : 0.97  },\
"video" : "hd6850_exploded caps.mp4",\
"isChapter" : False, \
})

configs["episodes"].append(\
{ "title": "The R7770-PMD1GD5 lives",\
"audio" : {"timestamps" : ("03:18", "04:01" ), "volume" : 0.97  },\
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
#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "Usefulness of the HD 6850"][0], configs)
scriptedvided.makeVideo(configs)


