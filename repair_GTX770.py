import scriptedvided

configs = { "defaultAudioFile" : "repair_gtx770.ogg",\
"mediaFolder" : "F:\\Videos\\repair_gtx770", \
"stockFolder" : "F:\\Videos\\stock",\
"benchmarkFile" : None,\
"outputFolder" : "F:\\Videos\\repair_gtx770\\output", \
"outputFile" : "repair_gtx770.mp4", \
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3",\
"timestamps" : ("00:30", None ), "destinationTimestamp" : {"title" : "TLDW: a dead GTX 960 saved a GT 730", "until" : "Fixing PCIE lane 11 (going PCIE x16)"}}, \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3",\
"timestamps" : ("00:30", None ), "destinationTimestamp" : {"title" : "Fixing PCIE lane 11 (going PCIE x16)", "until" : "The card powered up fine"}}, \
{"file" : "bensound-summer.mp3", "timestamps" : ("00:00", None ), "destinationTimestamp" : { "title": "The card powered up fine", "until" : "Blooper" }}, \
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
"audio" : {"timestamps" : ("", "" ), "volume" : 0.999 },\
"video" : "gtx770_bb_W_arzone.mp4"\
})


configs["episodes"].append(\
{ "title": "Everything started like usual, with an ad",\
"audio" : {"timestamps" : ("", ""), "volume" : 0.999 },\
"video" : {"file" : "olx_ad_gtx770_hd5770.mkv", "start" : "00:20"}\
})


configs["episodes"].append(\
{ "title": "Packaging",\
"isChapter" : False, \
"audio" : {"timestamps" : ("01:27.5", "01:41"), "volume" : 0.999 },\
"video" : {"file" : "usage_of_inductors.mkv", "start" : "00:20"}\
})

configs["episodes"].append(\
{ "title": "Resistance measurements",\
"audio" : {"timestamps" : ("01:27.5", "01:41"), "volume" : 0.999 },\
"video" : {"file" : "usage_of_inductors.mkv", "start" : "00:20"}\
})

configs["episodes"].append(\
{ "title": "Voltage measurements",\
"audio" : {"timestamps" : ("01:27.5", "01:41"), "volume" : 0.999 },\
"video" : {"file" : "usage_of_inductors.mkv", "start" : "00:20"}\
})

configs["episodes"].append(\
{ "title": "Visual inspection of the PCB",\
"audio" : {"timestamps" : ("01:27.5", "01:41"), "volume" : 0.999 },\
"video" : {"file" : "usage_of_inductors.mkv", "start" : "00:20"}\
})

configs["episodes"].append(\
{ "title": "visual inspection - closer look",\
"isChapter" : False, \
"audio" : {"timestamps" : ("01:27.5", "01:41"), "volume" : 0.999 },\
"video" : {"file" : "usage_of_inductors.mkv", "start" : "00:20"}\
})

configs["episodes"].append(\
{ "title": "Identify the missing components",\
"audio" : {"timestamps" : ("01:27.5", "01:41"), "volume" : 0.999 },\
"video" : {"file" : "usage_of_inductors.mkv", "start" : "00:20"}\
})

configs["episodes"].append(\
{ "title": "GPU phase controller woes",\
"isChapter" : False, \
"audio" : {"timestamps" : ("01:27.5", "01:41"), "volume" : 0.999 },\
"video" : {"file" : "usage_of_inductors.mkv", "start" : "00:20"}\
})

configs["episodes"].append(\
{ "title": "Add back the components",\
"audio" : {"timestamps" : ("01:27.5", "01:41"), "volume" : 0.999 },\
"video" : {"file" : "usage_of_inductors.mkv", "start" : "00:20"}\
})

configs["episodes"].append(\
{ "title": "Repair the trace for the 10 nF cap",\
"isChapter" : False, \
"audio" : {"timestamps" : ("01:27.5", "01:41"), "volume" : 0.999 },\
"video" : {"file" : "usage_of_inductors.mkv", "start" : "00:20"}\
})

configs["episodes"].append(\
{ "title": "The 10k resistors",\
"isChapter" : False, \
"audio" : {"timestamps" : ("01:27.5", "01:41"), "volume" : 0.999 },\
"video" : {"file" : "usage_of_inductors.mkv", "start" : "00:20"}\
})

configs["episodes"].append(\
{ "title": "The daughter board",\
"isChapter" : False, \
"audio" : {"timestamps" : ("01:27.5", "01:41"), "volume" : 0.999 },\
"video" : {"file" : "usage_of_inductors.mkv", "start" : "00:20"}\
})

configs["episodes"].append(\
{ "title": "Voltage measurements two",\
"audio" : {"timestamps" : ("01:27.5", "01:41"), "volume" : 0.999 },\
"video" : {"file" : "usage_of_inductors.mkv", "start" : "00:20"}\
})

configs["episodes"].append(\
{ "title": "Voltage measurements two - enable",\
"isChapter" : False, \
"audio" : {"timestamps" : ("01:27.5", "01:41"), "volume" : 0.999 },\
"video" : {"file" : "usage_of_inductors.mkv", "start" : "00:20"}\
})

configs["episodes"].append(\
{ "title": "a few transistors involved in generating the enable signal",\
"isChapter" : False, \
"audio" : {"timestamps" : ("01:27.5", "01:41"), "volume" : 0.999 },\
"video" : {"file" : "usage_of_inductors.mkv", "start" : "00:20"}\
})

configs["episodes"].append(\
{ "title": "measure the actual voltages - EN",\
"isChapter" : False, \
"audio" : {"timestamps" : ("01:27.5", "01:41"), "volume" : 0.999 },\
"video" : {"file" : "usage_of_inductors.mkv", "start" : "00:20"}\
})

configs["episodes"].append(\
{ "title": "Hard-wiring the enable",\
"isChapter" : False, \
"audio" : {"timestamps" : ("01:27.5", "01:41"), "volume" : 0.999 },\
"video" : {"file" : "usage_of_inductors.mkv", "start" : "00:20"}\
})

configs["episodes"].append(\
{ "title": "Third power-up",\
"audio" : {"timestamps" : ("01:27.5", "01:41"), "volume" : 0.999 },\
"video" : {"file" : "usage_of_inductors.mkv", "start" : "00:20"}\
})

configs["episodes"].append(\
{ "title": "The MOSFETs get too hot",\
"audio" : {"timestamps" : ("01:27.5", "01:41"), "volume" : 0.999 },\
"video" : {"file" : "usage_of_inductors.mkv", "start" : "00:20"}\
})

configs["episodes"].append(\
{ "title": "searching for another 2.2 nF MLCC",\
"isChapter" : False, \
"audio" : {"timestamps" : ("01:27.5", "01:41"), "volume" : 0.999 },\
"video" : {"file" : "usage_of_inductors.mkv", "start" : "00:20"}\
})

configs["episodes"].append(\
{ "title": "Artefacts. Great.",\
"audio" : {"timestamps" : ("01:27.5", "01:41"), "volume" : 0.999 },\
"video" : {"file" : "usage_of_inductors.mkv", "start" : "00:20"}\
})

configs["episodes"].append(\
{ "title": "Monitoring the voltage during boot",\
"isChapter" : False, \
"audio" : {"timestamps" : ("01:27.5", "01:41"), "volume" : 0.999 },\
"video" : {"file" : "usage_of_inductors.mkv", "start" : "00:20"}\
})

configs["episodes"].append(\
{ "title": "datasheet for the memory phase controller",\
"isChapter" : False, \
"audio" : {"timestamps" : ("01:27.5", "01:41"), "volume" : 0.999 },\
"video" : {"file" : "usage_of_inductors.mkv", "start" : "00:20"}\
})

configs["episodes"].append(\
{ "title": "get an MLCC and solder it in place",\
"isChapter" : False, \
"audio" : {"timestamps" : ("01:27.5", "01:41"), "volume" : 0.999 },\
"video" : {"file" : "usage_of_inductors.mkv", "start" : "00:20"}\
})

configs["episodes"].append(\
{ "title": "no more artifacts",\
"isChapter" : False, \
"audio" : {"timestamps" : ("01:27.5", "01:41"), "volume" : 0.999 },\
"video" : {"file" : "usage_of_inductors.mkv", "start" : "00:20"}\
})

configs["episodes"].append(\
{ "title": "until I played Warframe",\
"isChapter" : False, \
"audio" : {"timestamps" : ("01:27.5", "01:41"), "volume" : 0.999 },\
"video" : {"file" : "usage_of_inductors.mkv", "start" : "00:20"}\
})

configs["episodes"].append(\
{ "title": "Unfair phase loading",\
"audio" : {"timestamps" : ("01:27.5", "01:41"), "volume" : 0.999 },\
"video" : {"file" : "usage_of_inductors.mkv", "start" : "00:20"}\
})

configs["episodes"].append(\
{ "title": "not a 60-40 split",\
"isChapter" : False, \
"audio" : {"timestamps" : ("01:27.5", "01:41"), "volume" : 0.999 },\
"video" : {"file" : "usage_of_inductors.mkv", "start" : "00:20"}\
})

configs["episodes"].append(\
{ "title": "Problems piled up",\
"audio" : {"timestamps" : ("01:27.5", "01:41"), "volume" : 0.999 },\
"video" : {"file" : "usage_of_inductors.mkv", "start" : "00:20"}\
})

configs["episodes"].append(\
{ "title": "Tackling the power balance issue",\
"audio" : {"timestamps" : ("01:27.5", "01:41"), "volume" : 0.999 },\
"video" : {"file" : "usage_of_inductors.mkv", "start" : "00:20"}\
})

configs["episodes"].append(\
{ "title": "Tackling the power balance issue - nope",\
"isChapter" : False, \
"audio" : {"timestamps" : ("01:27.5", "01:41"), "volume" : 0.999 },\
"video" : {"file" : "usage_of_inductors.mkv", "start" : "00:20"}\
})

configs["episodes"].append(\
{ "title": "Finding a fix for the artifacting",\
"audio" : {"timestamps" : ("01:27.5", "01:41"), "volume" : 0.999 },\
"video" : {"file" : "usage_of_inductors.mkv", "start" : "00:20"}\
})

configs["episodes"].append(\
{ "title": "Put up a review video for the card",\
"audio" : {"timestamps" : ("01:27.5", "01:41"), "volume" : 0.999 },\
"video" : {"file" : "usage_of_inductors.mkv", "start" : "00:20"}\
})

configs["episodes"].append(\
{ "title": "Again with the artefacts",\
"audio" : {"timestamps" : ("01:27.5", "01:41"), "volume" : 0.999 },\
"video" : {"file" : "usage_of_inductors.mkv", "start" : "00:20"}\
})

configs["episodes"].append(\
{ "title": "The power sequence circuit issue",\
"audio" : {"timestamps" : ("01:27.5", "01:41"), "volume" : 0.999 },\
"video" : {"file" : "usage_of_inductors.mkv", "start" : "00:20"}\
})

configs["episodes"].append(\
{ "title": "No resistor at all",\
"isChapter" : False, \
"audio" : {"timestamps" : ("01:27.5", "01:41"), "volume" : 0.999 },\
"video" : {"file" : "usage_of_inductors.mkv", "start" : "00:20"}\
})

configs["episodes"].append(\
{ "title": "8K resistor from the Lenovo IH61M motherboard",\
"isChapter" : False, \
"audio" : {"timestamps" : ("01:27.5", "01:41"), "volume" : 0.999 },\
"video" : {"file" : "usage_of_inductors.mkv", "start" : "00:20"}\
})

configs["episodes"].append(\
{ "title": "Undervolting the VRAM",\
"audio" : {"timestamps" : ("01:27.5", "01:41"), "volume" : 0.999 },\
"video" : {"file" : "usage_of_inductors.mkv", "start" : "00:20"}\
})

configs["episodes"].append(\
{ "title": "lower this in-load voltage",\
"isChapter" : False, \
"audio" : {"timestamps" : ("01:27.5", "01:41"), "volume" : 0.999 },\
"video" : {"file" : "usage_of_inductors.mkv", "start" : "00:20"}\
})

configs["episodes"].append(\
{ "title": "Only one way to find out",\
"isChapter" : False, \
"audio" : {"timestamps" : ("01:27.5", "01:41"), "volume" : 0.999 },\
"video" : {"file" : "usage_of_inductors.mkv", "start" : "00:20"}\
})

configs["episodes"].append(\
{ "title": "The card powered up fine",\
"audio" : {"timestamps" : ("01:27.5", "01:41"), "volume" : 0.999 },\
"video" : {"file" : "usage_of_inductors.mkv", "start" : "00:20"}\
})

configs["episodes"].append(\
{ "title": "No artefacts - desktop",\
"isChapter" : False, \
"audio" : {"timestamps" : ("01:27.5", "01:41"), "volume" : 0.999 },\
"video" : {"file" : "usage_of_inductors.mkv", "start" : "00:20"}\
})

configs["episodes"].append(\
{ "title": "No artefacts - Heaven",\
"isChapter" : False, \
"audio" : {"timestamps" : ("01:27.5", "01:41"), "volume" : 0.999 },\
"video" : {"file" : "usage_of_inductors.mkv", "start" : "00:20"}\
})

configs["episodes"].append(\
{ "title": "Blooper",\
"isChapter" : False, \
"audio" : {"timestamps" : ("01:27.5", "01:41"), "volume" : 0.999 },\
"video" : {"file" : "usage_of_inductors.mkv", "start" : "00:20"}\
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


