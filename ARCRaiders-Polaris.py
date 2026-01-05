import scriptedvided

configs = { "defaultAudioFile" : "ARCRaiders-Polaris.ogg",\
"mediaFolder" : "F:\\Videos\\ARCRaiders-Polaris", \
"stockFolder" : "F:\\Videos\\stock",\
"outputFolder" : "F:\\Videos\\ARCRaiders-Polaris\\output", \
"outputFile" : "ARCRaiders-Polaris.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "Money well spent, maybe", "until" : "captures at 720"}}, \
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
"tags" : "ARC,ARC Raiders,AMD,Radeon,Polaris,RX 460,RX 560,RX 470,RX 570,RX 480,RX 580,RX460,RX560,RX470,RX570,RX480,RX580,",\
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
{ "title": "Money well spent, maybe",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:14.9" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "ARCRaiders_combat_failure.mp4", "start" : "00:05"},\
})

configs["episodes"].append(\
{ "title": "Hardware requirements look sus",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:31.6" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "ARCRaiders_combat_failure.mp4", "start" : "00:20"},\
"overlay" : { \
    "image" : {"file" : "overlay_requirements.png"}\
}, \
})

configs["episodes"].append(\
{ "title": "The Polaris Family",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:39" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "Polaris_Family_barred.mp4"},\
})

configs["episodes"].append(\
{ "title": "RX 580",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:51.2" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "Polaris_Family_RX580_barred.mp4"},\
})

configs["episodes"].append(\
{ "title": "RX 570",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:00.7 ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "Polaris_Family_RX570_barred.mp4"},\
})

configs["episodes"].append(\
{ "title": "RX 460",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:12" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "Polaris_Family_RX460_barred.mp4"},\
})

# black screen
configs["episodes"].append(\
{ "title": "Test system and settings",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:34.2" ), "volume" : 0.999, "padAudio" : 0.1 },\
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
{ "title": "captures at 720",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:56.8" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "ARCRaiders__R9_270_1.mp4"},\
})

configs["episodes"].append(\
{ "title": "1280x720 results",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:39.1" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "ARCRaiders_success.mp4", "start" : "01:00"},\
"overlay" : { \
    "image" : {"file" : "720, low settings.png"}\
}, \
})

configs["episodes"].append(\
{ "title": "1600x900 results",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:04.9" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "ARCRaiders_runnig_swamp.mp4", "start" : "03:30"},\
"overlay" : { \
    "image" : {"file" : "900, low settings.png"}\
}, \
})


configs["episodes"].append(\
{ "title": "Ready up for 1920x1080",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:23.4" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "ARCRaiders_combat_failure.mp4", "start" : "00:35"},\
"isChapter" : False, \
})

configs["episodes"].append(\
{ "title": "1920x1080 results",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:40.4" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "ARCRaiders_success.mp4", "start" : "01:40"},\
"overlay" : { \
    "image" : {"file" : "1080, low settings.png"}\
}, \
})

#R9 290X breel?
# overlay with FPS for the 290X
configs["episodes"].append(\
{ "title": "Conclusions",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:56.3" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "ARCRaiders_combat_failure.mp4", "start" : "04:00"},\
})

#R9 270 breel
configs["episodes"].append(\
{ "title": "more to come",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:06.2" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "breel_GTX960_both.mp4"},\
})

# gameplay
configs["episodes"].append(\
{ "title": "bye",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:16" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "ARCRaiders_success.mp4", "start" : "04:40"},\
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