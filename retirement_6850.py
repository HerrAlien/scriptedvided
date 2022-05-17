import scriptedvided

configs = { "defaultAudioFile" : "6850_retirement.ogg",\
"mediaFolder" : "C:\\Users\\Admin\\Videos\\hd6850_adventures", \
"stockFolder" : "C:\\Users\\Admin\\Videos\stock",\
"outputFolder" : "C:\\Users\\Admin\\Videos\\hd6850_adventures\\output", \
"outputFile" : "hd6850_adventures.mp4", \
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "H:\\Muzica\\royalty free\\Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3",\
"timestamps" : ("00:30", None ), "destinationTimestamp" : {"title":"Bought a known non working card", "until" : "Mistake #1"}}, \
{"file" : "H:\\Muzica\\royalty free\\Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3",\
"timestamps" : ("00:30", None ), "destinationTimestamp" : {"title":"Symptoms - crash at installing the driver", "until" : "Ominous black screen"}}, \
{"file" : "H:\\Muzica\\royalty free\\Bitters At The Saloon - Bird Creek (No Copyright Music).ogg", \
"timestamps" : ("00:00", None ), "destinationTimestamp" : { "title": "VBios tool, download vbioses", "until" : "Black screen - vbios fail"}}, \
{"file" : "H:\\Muzica\\royalty free\\Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3",\
"timestamps" : ("00:30", None ), "destinationTimestamp" : {"title" : "Recovering from the first mistake", "until" : "Mistake #2"}}, \
{"file" : "H:\\Muzica\\royalty free\\Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3",\
"timestamps" : ("00:30", None ), "destinationTimestamp" : {"title" : "brooll, prepare for baking", "until" : "jensen pulling out cards"}}, \
{"file" : "H:\\Muzica\\royalty free\\Bitters At The Saloon - Bird Creek (No Copyright Music).ogg", \
"timestamps" : ("00:00", None ), "destinationTimestamp" : { "title": "jensen pulling out cards", "until":"New caps 470 micro too large"}}, \
{"file" : "H:\\Muzica\\royalty free\\Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3",\
"timestamps" : ("00:30", None ),  "destinationTimestamp" : { "title": "New caps 470 micro too large", "until" : "Conclusions"}}, \
{"file" : "H:\\Muzica\\royalty free\\bensound-summer.mp3", "timestamps" : ("00:00", "02:31" ), "destinationTimestamp" : { "title": "Conclusions"}}, \
], "volume" : 0.03 },\
"episodes" : [],\
"youtube" : {"title" : "The tumultuous retirement of an HD 6850", \
"description" : '''Buying and trying to repair an used and known non-working card can turn out into an adventure.''',\
"links" : '''
Jensen promo for new cards: https://www.youtube.com/watch?v=So7TNRhIYJ8
''', \
"tags" : "AMD,Radeon,HD 6850,HD6850,Terascale 2,Sapphire,cooking cards,baking card in oven,oven baking method,cooking,PCB,card,oven",\
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
{ "title": "Bought a known non working card",\
"audio" : {"timestamps" : ("00:00.5", "00:34" ), "volume" : 0.999 },\
"video" : "hd6850.MOV"\
})

configs["episodes"].append(\
{ "title": "Mistake #1",\
"video" : {"file" : "slides.mkv", "start" : "00:06", "length" : "00:13"},\
"audio" : {"file" : "silence_30min.ogg", "start" : "00:00", "length" : "00:07"},\
})

configs["episodes"].append(\
{ "title": "Symptoms - crash at installing the driver",\
"audio" : {"timestamps" : ("00:34", "00:52" ), "volume" : 0.999 },\
"video" : {"file":"vga_bios_work.mp4", "start" : "03:34"},\
})

configs["episodes"].append(\
{ "title": "Driver downloads",\
"audio" : {"timestamps" : ("00:52", "01:27" ), "volume" : 0.999 },\
"video" : "TeraScale2Drivers.mp4",\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Ominous black screen",\
"audio" : {"timestamps" : ("01:27", "01:32" ), "volume" : 0.999 },\
"video" : "black_screen.mkv",\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "VBios tool, download vbioses",\
"audio" : {"timestamps" : ("01:32", "02:02" ), "volume" : 0.999 },\
"video" : {"file" : "vga_bios_work.mp4", "start" : "00:20"},\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Command line FC",\
"audio" : {"timestamps" : ("02:02", "02:41" ), "volume" : 0.999 },\
"video" : "command_prompt_fc.mp4",\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Black screen - vbios fail",\
"audio" : {"timestamps" : ("02:41", "02:46" ), "volume" : 0.999 },\
"video" : "black_screen.mkv",\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Recovering from the first mistake",\
"audio" : {"timestamps" : ("02:46", "03:03" ), "volume" : 0.999  },\
"video" : "z230_inside_shot.mov", \
})

configs["episodes"].append(\
{ "title": "apu and testbench to the rescue",\
"audio" : {"timestamps" : ("03:05", "03:36" ), "volume" : 0.999  },\
"video" : "testbench.mp4", \
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Mistake #2",\
"video" : {"file" : "slides.mkv", "start" : "00:16", "length" : "00:24"},\
"audio" : {"file" : "silence_30min.ogg", "start" : "00:00", "length" : "00:08"},\
})

configs["episodes"].append(\
{ "title": "brooll, prepare for baking",\
"audio" : {"timestamps" : ("03:36", "04:04" ), "volume" : 0.999  },\
"video" : "hd6850.MOV", \
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "jensen pulling out cards",\
"audio" : {"timestamps" : ("04:04", "04:26" ), "volume" : 0.999  },\
"video" : {"file" : "jensen_oven.mkv", "start" : "00:03"}, \
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Black screen, point out the two differences",\
"audio" : {"timestamps" : ("04:26", "04:47" ), "volume" : 0.999  },\
"video" : {"file" : "slides.mkv", "start" : "00:25", "length" : "00:42"},\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Blown caps",\
"audio" : {"timestamps" : ("04:47", "05:15" ), "volume" : 0.999  },\
"video" : "hd6850_exploded caps.mp4", \
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "New caps 470 micro too large",\
"audio" : {"timestamps" : ("05:15", "05:38" ), "volume" : 0.999  },\
"video" : "capacitors_order.mp4", \
"isChapter" : False,\
})


configs["episodes"].append(\
{ "title": "Soldered the new caps",\
"audio" : {"timestamps" : ("05:38", "05:56" ), "volume" : 0.999  },\
"video" : "hd6850_new_caps.mp4", \
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Conclusions",\
"audio" : {"timestamps" : ("05:56", "06:14" ), "volume" : 0.999  },\
"video" : "hd6850_on_the_bench.mp4", \
})

configs["episodes"].append(\
{ "title": "Conclusions heaven",\
"audio" : {"timestamps" : ("06:14", "06:29" ), "volume" : 0.999  },\
"video" : "hd6850_testbench_heaven.mp4", \
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Some lessons learned",\
"audio" : {"timestamps" : ("06:31", "07:48" ), "volume" : 0.999  },\
"video" : "hd6850_Fortnite_1080p.mp4", \
})

configs["episodes"].append(\
{ "title": "Happy retirement",\
"audio" : {"timestamps" : ("07:48", "08:21" ), "volume" : 0.999  },\
"video" : {"file" : "6850_fortnite_win_with_card_rotaded.mp4", "start" : "00:02"}, \
})


#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "Symptoms - crash at installing the driver"][0], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][9], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][8], configs)
#print(scriptedvided.makeVideoForEpisode(configs["episodes"][9], configs))
#print(scriptedvided.getSuitableVideoStream(configs["episodes"][9], configs))
#print (configs["youtube"])
#print(scriptedvided.getMusicCreditsString(configs["backgroundTrack"]))
scriptedvided.makeVideo(configs)

