import scriptedvided

configs = { "defaultAudioFile" : "ARCRaiders-IGPUs.ogg",\
"mediaFolder" : "F:\\Videos\\ARCRaiders-IGPUs", \
"stockFolder" : "F:\\Videos\\stock",\
"outputFolder" : "F:\\Videos\\ARCRaiders-IGPUs\\output", \
"outputFile" : "ARCRaiders-IGPUs.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "System requirements, again", "until" : "settngs and gameplay video"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "settngs and gameplay video", "until" : "Conclusions"}}, \
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
"tags" : "ARC,ARC Raiders,AMD,Radeon,Vega,Radeon Graphics,RX Vega,Vega 7,Vega 8,Vega 11,Radeon Graphics 448SP,APU,Ryzen,Ryzen 5,Ryzen 3,Ryzen 3 3200G,Ryzen 5 2400G,Ryzen 5 4600G",\
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
{ "title": "System requirements, again",\
"audio" : {"timestamps" : ("00:00", "00:17.4" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "PioneerGame_SpacePort2.mp4", "start" : "03:00"},\
"overlay" : { \
    "image" : {"file" : "ARC_overlay_requirements.png"}\
}, \
})

configs["episodes"].append(\
{ "title": "Need more than 2 GB",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:29.1" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "ARCRaiders__R9_270_1_quadrant2.mp4"},\
})

configs["episodes"].append(\
{ "title": "The IGPUs",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:32.3" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "breel_Ryzens_barred.mp4"},\
})

configs["episodes"].append(\
{ "title": "Vega 7 4600G",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:50.3" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "breel_R5_4600G_inHand_barred.mp4"},\
})

configs["episodes"].append(\
{ "title": "Vega 11 2400G",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:02.6" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "breel_R5_2400G_inHand_barred.mp4"},\
})

configs["episodes"].append(\
{ "title": "Vega 8 3200G",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:13" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "breel_R3_3200G_inHand_barred.mp4"},\
})

# black screen
configs["episodes"].append(\
{ "title": "Test system and settings",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:23.5" ), "volume" : 0.999, "padAudio" : 0.1 },\
"overlay" : { \
    "text" : ["'Custom PC'",\
              "'APUs\: Ryzen 3 3200G, Ryzen 5 2400G, Ryzen 5 4600G'",\
              "'RAM\: 32GB DDR4, 3000MHz, dual channel'",\
    ]\
}, \
"video" : {"file" : "breel_R5_2400g_platform.mp4"},\
})

# capture with settings
configs["episodes"].append(\
{ "title": "settngs and gameplay video",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:35.8" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "PioneerGame_SpacePort2.mp4",  "start" : "03:17"},\
})


# capture with settings
configs["episodes"].append(\
{ "title": "breel 1080",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:43" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "PioneerGame_SpacePort2.mp4", "start" : "03:29.3"},\
})

configs["episodes"].append(\
{ "title": "1920x1080 results",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:19.7" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "PioneerGame_SpacePort2.mp4", "start" : "03:36.5"},\
"overlay" : { \
    "image" : {"file" : "ARC Raiders, 1920x1080, low settings.png"}\
}, \
})

configs["episodes"].append(\
{ "title": "1600x900 results",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:59.6" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "PioneerGame_SpacePort2.mp4", "start" : "04:13.2"},\
"overlay" : { \
    "image" : {"file" : "ARC Raiders, 1600x900, low settings.png"}\
}, \
})

configs["episodes"].append(\
{ "title": "Ready up for 1280x720",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:09.2" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "PioneerGame_SpacePort2.mp4", "start" : "04:53.1"},\
"isChapter" : False, \
})

configs["episodes"].append(\
{ "title": "1280x720 results",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:38.5" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "PioneerGame_SpacePort2.mp4", "start" : "05:22.8"},\
"overlay" : { \
    "image" : {"file" : "ARC Raiders, 1280x720, low settings.png"}\
}, \
})

# breel with APUs
configs["episodes"].append(\
{ "title": "Conclusions",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:58.9" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "breel_Ryzens_barred.mp4"},\
})

#R9 270 breel
configs["episodes"].append(\
{ "title": "breel and specs performance explained",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:23.6" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "breel_R5_2400G_inHand_barred.mp4"},\
})

#R9 270 breel
configs["episodes"].append(\
{ "title": "diff in specs performance explained",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:35.9" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "Vega7vsVega11.mkv", "start" : "00:38"},\
})

#R9 270 breel
configs["episodes"].append(\
{ "title": "APU breels, in vacuum",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:43.6" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "breel_R5_4600G_inHand_barred.mp4"},\
})

#R9 270 breel
configs["episodes"].append(\
{ "title": "1050 ti breel dgpus better",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:52" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "broll_GTX1050Ti_outside.mp4"},\
})

#R9 270 breel
configs["episodes"].append(\
{ "title": "R9 family",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:58" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "breel_R9Family2026_barred.mp4"},\
})

# gameplay
configs["episodes"].append(\
{ "title": "bye with gameplay",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:04.6" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "PioneerGame_SpacePort2.mp4", "start" : "10:20"},\
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