import scriptedvided

configs = { "defaultAudioFile" : "ARCRaiders-Maxwell,Pascal.ogg",\
"mediaFolder" : "F:\\Videos\\ARCRaiders-Pascal,Maxwell", \
"stockFolder" : "F:\\Videos\\stock",\
"outputFolder" : "F:\\Videos\\ARCRaiders-Pascal,Maxwell\\output", \
"outputFile" : "ARCRaiders-Pascal,Maxwell.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#00800080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "VRAM, VRAM", "until" : "captures at 720"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "captures at 720", "until" : "Conclusions"}}, \
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
"tags" : "ARC,ARC Raiders,NVidia,GeForce,GTX,GTX960,GTX1050Ti,GTX 960,GTX 1050Ti,GTX 1050 Ti",\
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
{ "title": "VRAM, VRAM",\
"audio" : {"timestamps" : ("00:00", "00:11.9" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "ARCRaiders_success.mp4", "start" : "00:05"},\
})

configs["episodes"].append(\
{ "title": "Hardware requirements still look sus",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:27.1" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "ARCRaiders_success.mp4", "start" : "00:20"},\
"overlay" : { \
    "image" : {"file" : "overlay_requirements.png"}\
}, \
})

configs["episodes"].append(\
{ "title": "The GeForce Family",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:30.7" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "1050Ti_both960s.mp4"},\
})

configs["episodes"].append(\
{ "title": "GTX 1050 Ti",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:38.3" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "broll_GTX1050Ti_outside.mp4"},\
})

configs["episodes"].append(\
{ "title": "GTX 960 4GB",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:47.2" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "breel_GTX960_4GB.mp4"},\
})

configs["episodes"].append(\
{ "title": "GTX 960 2GB",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:58.7" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "breel_GTX960_bars.mp4"},\
})

# black screen
configs["episodes"].append(\
{ "title": "Test system and settings",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:14.3" ), "volume" : 0.999, "padAudio" : 0.1 },\
"overlay" : { \
    "text" : ["'Custom PC'",\
              "'CPU\: Ryzen 5 5600'",\
              "'RAM\: 32GB DDR4, 3600MHz, dual channel'",\
    ]\
}, \
"video" : {"file" : "test_system_noGPU-converted.mp4"},\
})

# capture with settings
configs["episodes"].append(\
{ "title": "settings",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:32.1" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "ARCRaiders_combat_failure.mp4", "start" : "00:25"},\
})

# capture with settings
configs["episodes"].append(\
{ "title": "captures at 720",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:51.6" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "ARCRaiders__R9_270_1.mp4"},\
})

configs["episodes"].append(\
{ "title": "1280x720 results",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:28.5" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "ARCRaiders_success.mp4", "start" : "01:20"},\
"overlay" : { \
    "image" : {"file" : "ARC Raiders, 1280x720, low settings.png"}\
}, \
})

configs["episodes"].append(\
{ "title": "1600x900 results",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:00.1" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "ARCRaiders_runnig_swamp.mp4", "start" : "02:30"},\
"overlay" : { \
    "image" : {"file" : "ARC Raiders, 1600x900, low settings.png"}\
}, \
})


configs["episodes"].append(\
{ "title": "Ready up for 1920x1080",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:17.9" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "ARCRaiders_combat_failure.mp4", "start" : "01:15"},\
"isChapter" : False, \
})

configs["episodes"].append(\
{ "title": "1920x1080 results",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:45.8" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "ARCRaiders_success.mp4", "start" : "02:00"},\
"overlay" : { \
    "image" : {"file" : "ARC Raiders, 1920x1080, low settings.png"}\
}, \
})

#R9 290X breel?
# overlay with FPS for the 290X
configs["episodes"].append(\
{ "title": "Conclusions",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:05.9" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "ARCRaiders_combat_failure.mp4", "start" : "03:00"},\
})

#R9 270 breel
configs["episodes"].append(\
{ "title": "more to come GPU side",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:22.5" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "Vega11-GPUZ.mkv"},\
})

#R9 270 breel
configs["episodes"].append(\
{ "title": "more to come CPU side",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:34.7" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "r5_5600_3600.mp4"},\
})

# gameplay
configs["episodes"].append(\
{ "title": "bye",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:43.3" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "1050Ti_960.mp4"},\
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