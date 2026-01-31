import scriptedvided

configs = { "defaultAudioFile" : "ARCRaiders-Intel.ogg",\
"mediaFolder" : "F:\\Videos\\ARCRaiders-Intel", \
"stockFolder" : "F:\\Videos\\stock",\
"outputFolder" : "F:\\Videos\\ARCRaiders-Intel\\output", \
"outputFile" : "ARCRaiders-Intel.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#00800080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "System requirements, again", "until" : "Test system and settings"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Test system and settings", "until" : "Conclusions"}}, \
{"file" : "Inspired - MaikonMusic  Free Background Music  Audio Library Release.mp3", "timestamps" : ("00:00", None ), "destinationTimestamp" : {"title" : "Conclusions", "until" : "EOF"}}, \
], "volume" : 0.045 },\
"episodes" : [],\
"youtube" : {"title" : " ", \
"description" : ''' ''',\
"links" : '''
Track: Bliss Of Heaven - SOMM [Audio Library Release]
Music provided by Audio Library Plus
Watch: https://www.youtube.com/watch?v=JQ6mKeQLZak&t=0s
Free Download / Stream: https://alplus.io/blisss-heaven

Track: Far Far Away - Ferco [Audio Library Release]
Music provided by Audio Library Plus
Watch: https://www.youtube.com/watch?v=SrkQ3K1umlc&t=0s 
Free Download / Stream: https://alplus.io/far-far-away

Track: Inspired - MaikonMusic [Audio Library Release]
Music provided by Audio Library Plus
Watch: https://www.youtube.com/watch?v=RUkdTkk_52o&t=0s
Free Download / Stream: https://alplus.io/inspired

''', \
"tags" : "ARC,ARC Raiders,AMD,Ryzen 5 5600,R5 5600,Ryzen 5 3600,R5 3600,Ryzen 5 2600,R5 2600,APU,Ryzen,Ryzen 5,Ryzen 3,Ryzen 3 3200G,Ryzen 5 2400G,Ryzen 5 4600G,R6 2400G,R5 4600G,R3 3200G",\
"language" : "EN", \
"Caption certification" : "None",\
"recording date" : None,\
"video location" : None, \
"category" : "Gaming", \
"subtitles" : None, \
"endscreen" : None, \
"cards" : None, \
}\
}

# gameplay
configs["episodes"].append(\
{ "title": "Time to test Intel CPUs",\
"audio" : {"timestamps" : ("00:00", "00:11.4" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "PioneerGame_2026_01_17_07_35_27_380-converted.mp4", "start" : "06:40"},\
})

configs["episodes"].append(\
{ "title": "CPU req and results from Tyzen Quads",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:23" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "PioneerGame_2026_01_17_07_35_27_380-converted.mp4", "start" : "06:51.4"},\
"overlay" : { \
    "image" : {"file" : "overlay_quads_and_requirements.png"}\
}, \
})

configs["episodes"].append(\
{ "title": "The CPUs",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:26.1" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : " "},\
})

configs["episodes"].append(\
{ "title": "i5 6400",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:36.9" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "breel_i5_6400_inHand_barred.mp4"},\
"overlay" : { \
    "text" : ["'4 cores, 4 threads, 6MB L3 cache, up to 3.3 GHz'"]\
}, \
})

configs["episodes"].append(\
{ "title": "i5 4590",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:45.8" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "breel_i5_4590_inHand_barred.mp4"},\
"overlay" : { \
    "text" : ["'4 cores, 4 threads, 6MB L3 cache, up to 3.7 GHz'"]\
}, \
})

configs["episodes"].append(\
{ "title": "i7 4790k",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:57.9" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "breel_i7_4790k_inMoboInHand_barred.mp4"},\
"overlay" : { \
    "text" : ["'4 cores, 8 threads, 8MB L3 cache, up to 4.4 GHz'"]\
}, \
})

configs["episodes"].append(\
{ "title": "i7 6700K",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:14.1" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "breel_i7_6700k_inHand_barred.mp4"},\
"overlay" : { \
    "text" : ["'4 cores, 8 threads, 8MB L3 cache, up to 4.2 GHz'"]\
}, \
})

# capture with settings
configs["episodes"].append(\
{ "title": "Test system and settings",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:26.2" ), "volume" : 0.999, "padAudio" : 0.1 },\
"overlay" : { \
    "text" : ["'Custom PC - Skylake'",\
              "'CPUs\: Core i5 6400, Core i7 6700K'",\
              "'RAM\: 32GB DDR4, 3000MHz, dual channel'",\
              "'Motherboard\: ASUS Z170 Pro Gaming'",\
              "'GPU\: RX 580'",\
    ]\
}, \
"video" : {"file" : "breel_Z170_inHand_barred.mp4"},\
})

configs["episodes"].append(\
{ "title": "Haswell PC",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:39.4" ), "volume" : 0.999, "padAudio" : 0.1 },\
"overlay" : { \
    "text" : ["'Custom PC - Haswell'",\
              "'CPUs\: Core i5 6400, Core i7 6700K'",\
              "'RAM\: 32GB DDR4, 3000MHz, dual channel'",\
              "'Motherboard\: ASUS 97 Pro Gaming'",\
              "'GPU\: RX 580'",\
    ]\
}, \
"video" : {"file" : "breel_Z97InCase_barred.mp4"},\
})

configs["episodes"].append(\
{ "title": "GPU",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:54" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "Polaris_Family_RX580_barred.mp4"},\
"overlay" : { \
    "text" : ["'Test settings\: 1280x720, 50\\\% render scale, low settings'",\
    ]\
}, \
})

# just the i5s
configs["episodes"].append(\
{ "title": "1280x720 results",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:26.4" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "PioneerGame_2026_01_17_07_35_27_380-converted.mp4", "start" : "07:03"},\
"overlay" : { \
    "image" : {"file" : "i5s.png"}\
}, \
})

configs["episodes"].append(\
{ "title": "i7s at stock",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:01.8" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "PioneerGame_2026_01_17_07_35_27_380-converted.mp4", "start" : "07:35.4"},\
"isChapter" : False, \
"overlay" : { \
    "image" : {"file" : "add_i7s.png"}\
}, \
})

configs["episodes"].append(\
{ "title": "with XMP",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:23.1" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "PioneerGame_2026_01_17_07_35_27_380-converted.mp4", "start" : "07:57.7"},\
"isChapter" : False, \
"overlay" : { \
    "image" : {"file" : "xmp_i7.png"}\
}, \
})

# are i5s still useful?
configs["episodes"].append(\
{ "title": "Conclusions",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:27.7" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : " "},\
})

#R9 270 breel
configs["episodes"].append(\
{ "title": "maybe yes maybe no",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:30" ), "volume" : 0.001, "padAudio" : 0.1 },\
"video" : {"file" : " "},\
})

configs["episodes"].append(\
{ "title": "i5 conclusions",\
"isChapter" : False, \
"audio" : {"timestamps" : ("03:30", "03:39.3" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : " "},\
})

configs["episodes"].append(\
{ "title": "i7 conclusions",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:55" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : " "},\
})

configs["episodes"].append(\
{ "title": "AM4 plug",\
"isChapter" : False, \
"audio" : {"timestamps" : ("03:56.4", "04:14.5" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "GA-B450M-DS3H_overview.MP4"},\
})

configs["episodes"].append(\
{ "title": "R9 family breel",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:23" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "breel_R9Family2026_barred.mp4"},\
})

# gameplay
configs["episodes"].append(\
{ "title": "bye with gameplay",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:29" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "PioneerGame_2026_01_17_07_35_27_380-converted.mp4", "start" : "11:52"},\
})


#scriptedvided.makeVideoForEpisode(configs["episodes"][1], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][4], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][11], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][12], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][13], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][8], configs)
#print(scriptedvided.makeVideoForEpisode(configs["episodes"][9], configs))
#print(scriptedvided.getSuitableVideoStream(configs["episodes"][9], configs))
#print (configs["youtube"])
#print(scriptedvided.getMusicCreditsString(configs["backgroundTrack"]))
#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "Alien Isolation"][0], configs)
#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "actual 1080 results"][0], configs)
#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "actual 900 results"][0], configs)
#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "actual 720 results"][0], configs)
#print (scriptedvided.getSuitableImage([x for x in configs["episodes"] if x["title"] == "actual 1080 results"][0], configs))

scriptedvided.makeVideo(configs)

# meeds better video, or maybe break it up