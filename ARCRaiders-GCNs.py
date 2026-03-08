import scriptedvided

configs = { "defaultAudioFile" : "ARCRaiders-GCNs.ogg",\
"mediaFolder" : "F:\\Videos\\ARCRaiders-GCNs", \
"stockFolder" : "F:\\Videos\\stock",\
"outputFolder" : "F:\\Videos\\ARCRaiders-GCNs\\output", \
"outputFile" : "ARCRaiders-GCNs.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "We must test even older GPUs", "until" : "1920x1080 results"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "1920x1080 results", "until" : "Conclusions"}}, \
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
"tags" : "ARC,ARC Raiders,AMD,Radeon,GCN,R9 290X,R9 280,R9 370,R7 265,HD 7950,HD 7850,HD7950,HD7850",\
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
{ "title": "We must test even older GPUs",\
"audio" : {"timestamps" : ("00:00", "00:08" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "PioneerGame_2026_01_17_08_01_54_227-converted.mp4", "start" : "05:22"},\
"overlay" : { \
    "image" : {"file" : "ARC_overlay_requirements.png"}\
}, \
})

configs["episodes"].append(\
{ "title": "Need more than 2 GB",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:17.3" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "ARCRaiders__R9_270_1.mp4", "start" : "00:03"},\
})

configs["episodes"].append(\
{ "title": "The GPUs",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:21.5" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "breel_R9Family2026_barred.mp4"},\
})

configs["episodes"].append(\
{ "title": "R9 290X",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:35.3" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "breel_R9Family2026_R9_290X_barred.mp4"},\
})

configs["episodes"].append(\
{ "title": "R9 280",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:51.9" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "breel_R9Family2026_R9_280_barred.mp4"},\
})

configs["episodes"].append(\
{ "title": "r9 370",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:05.9" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "breel_R9Family2026_R9_370_barred.mp4"},\
})

configs["episodes"].append(\
{ "title": "r9 370 vs 265 vs 7850",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:19.5" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "breel_R9_370_inHand_barred.mp4"},\
})

configs["episodes"].append(\
{ "title": "r9 370 GPUZ",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:43.3" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "gpuz_370_265_720.mp4"},\
})

# black screen
configs["episodes"].append(\
{ "title": "Test system",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:54.8" ), "volume" : 0.999, "padAudio" : 0.1 },\
"overlay" : { \
    "text" : ["'Custom PC'",\
              "'CPU\: Ryzen 5 5600'",\
              "'RAM\: 32GB DDR4, 3600MHz, dual channel'",\
              "'GPUs\: Radeon R9 370 1024, Radeon R9 280, Radeon R9 290X'",\
    ]\
}, \
"video" : {"file" : "test_system_noGPU-converted.mp4"},\
})

# r9 370, both frequencies - len is 23.7
configs["episodes"].append(\
{ "title": "1920x1080 results",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:18.5" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "PioneerGame_2026_01_17_08_01_54_227-converted.mp4" , "start": "05:30"},\
"overlay" : { \
    "image" : {"file" : "1080p_370sOnly.png"}\
}, \
})

# len 20.8
configs["episodes"].append(\
{ "title": "1080 plus R9 280",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:39.3" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "PioneerGame_2026_01_17_08_01_54_227-converted.mp4" , "start":"05:53.7"},\
"overlay" : { \
    "image" : {"file" : "1080p_add280.png"}\
}, \
})

#len 20.1
configs["episodes"].append(\
{ "title": "1080 plus R9 290x",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:49.4" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "PioneerGame_2026_01_17_08_01_54_227-converted.mp4" , "start":"06:14.5"},\
"overlay" : { \
    "image" : {"file" : "1080p_all.png"}\
}, \
})

# R9 290X only - LEN 18.3
configs["episodes"].append(\
{ "title": "1600x900 results",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:07.7" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "PioneerGame_2026_01_17_08_01_54_227-converted.mp4" , "start":"06:34.6"},\
"overlay" : { \
    "image" : {"file" : "900p_290xOnly.png"}\
}, \
})

# len 17.9
configs["episodes"].append(\
{ "title": "900p plus r9 280",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:25.6" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "PioneerGame_2026_01_17_08_01_54_227-converted.mp4" , "start":"06:52.9"},\
"overlay" : { \
    "image" : {"file" : "900p_add280.png"}\
}, \
})

# both frequencies len 31
configs["episodes"].append(\
{ "title": "900p plus r9 370",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:56.6" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "PioneerGame_2026_01_17_08_01_54_227-converted.mp4" ,"start": "07:10.8"},\
"overlay" : { \
    "image" : {"file" : "900p_all.png"}\
}, \
})

# r9 290X len 17.6
configs["episodes"].append(\
{ "title": "1280x720 results",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:14.2" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "PioneerGame_2026_01_17_08_01_54_227-converted.mp4" , "start":"07:41.8"},\
"overlay" : { \
    "image" : {"file" : "720p_290xOnly.png"}\
}, \
})

# add R9 280 len 12
configs["episodes"].append(\
{ "title": "720p plus R9 280",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:26.2" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "PioneerGame_2026_01_17_08_01_54_227-converted.mp4" , "start":"07:59.4"},\
"overlay" : { \
    "image" : {"file" : "720p_add280.png"}\
}, \
})

# add R9 370
configs["episodes"].append(\
{ "title": "720p plus R9 370",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:49.6" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "PioneerGame_2026_01_17_08_01_54_227-converted.mp4" , "start":"08:11.4"},\
"overlay" : { \
    "image" : {"file" : "720p_all.png"}\
}, \
})

# breel with APUs
configs["episodes"].append(\
{ "title": "Conclusions",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:57.8" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "breel_R9Family2026_barred.mp4"},\
})

#R9 270 breel
configs["episodes"].append(\
{ "title": "breel 290X",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:04.9" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "breel_r9_290x_outside.mp4"},\
})

#R9 270 breel
configs["episodes"].append(\
{ "title": "breel 280",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:24.8" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "breel_r9_280_outside.mp4"},\
})

#R9 370 breel
configs["episodes"].append(\
{ "title": "breel 370",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:39.8" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "breel_R9_370_barred.mp4"},\
})

#R9 370 breel
configs["episodes"].append(\
{ "title": "gameplay",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:56.7" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "PioneerGame_2026_01_17_08_01_54_227-converted.mp4" , "start":"16:30"},\
})

# gameplay
configs["episodes"].append(\
{ "title": "bye with family breel",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:07" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "breel_R9Family2026_barred.mp4"},\
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