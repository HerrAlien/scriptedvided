import scriptedvided

configs = { "defaultAudioFile" : "Doom_misfits.ogg",\
"mediaFolder" : "F:\\Videos\\Doom_misfits", \
"stockFolder" : "F:\\Videos\\stock",\
"outputFolder" : "F:\\Videos\\Doom_misfits\\output", \
"outputFile" : "Doom_misfits.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3",\
"timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "DOOM, other 3 GPUs and a test system", "until" : "1920x1080 results"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3",\
"timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "1920x1080 results", "until" : "Conclusion"}}, \
{"file" : "Guide You Home - Ferco and Andie - Free Background Music - Audio Library Release.ogg", "timestamps" : ("00:20", None ), "destinationTimestamp" : { "title": "Conclusion", "until" : "Blooper" }}, \
], "volume" : 0.06 },\
"episodes" : [],\
"youtube" : {"title" : " think of a title ", \
"description" : '''In this video, we'll take a closer look on how the mid-range GCN cards run the 2016 reboot of DOOM.
As usual, we're pairing the cards with the i7 4770 equivalent Xeon (E3-1241 v3), and 32 GB DDR3 @1600MHz, in dual channel.''',\
"links" : '''
Track: Bliss Of Heaven — SOMM [Audio Library Release]
Music provided by Audio Library Plus
Watch: https://www.youtube.com/watch?v=JQ6mKeQLZak&t=0s
Free Download / Stream: https://alplus.io/blisss-heaven

Track: Far Far Away — Ferco [Audio Library Release]
Music provided by Audio Library Plus
Watch: https://www.youtube.com/watch?v=SrkQ3K1umlc&t=0s 
Free Download / Stream: https://alplus.io/far-far-away

Track: Guide You Home — Ferco & Andie [Audio Library Release]
Music provided by Audio Library Plus
Watch: https://www.youtube.com/watch?v=16eNerPDIsU&t=0s
Free Download / Stream: https://alplus.io/guide-you-home

''', \
"tags" : "DOOM,Radeon,AMD,NVidia,GeForce,GTX,RX460,RX 460,GT1030,GT 1030,GTX770,GTX 770",\
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


configs["episodes"].append(\
{ "title": "DOOM, other 3 GPUs and a test system",\
"audio" : {"timestamps" : ("00:00", "00:13.5" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "stock_Doom_2016.mp4", "start":"00:03"},\
})

# this will be split up
configs["episodes"].append(\
{ "title": "Family",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:13.5", "00:18.3" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "breel_autumn_misfits_GT1030_RX460_GTX770.mp4", "start" : "00:00"},\
})

configs["episodes"].append(\
{ "title": "GT 1030",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:18.3", "00:23.3" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "breel_autumn_misfits_GT1030_RX460_GTX770.mp4", "start" : "00:56"},\
})

# 7770 - 51, 7750 - 01:40 

configs["episodes"].append(\
{ "title": "RX 460",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:23.3", "00:29.7" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "breel_autumn_misfits_GT1030_RX460_GTX770.mp4", "start" : "00:30"},\
})

configs["episodes"].append(\
{ "title": "GTX 770",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:29.7", "00:34.6" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "breel_autumn_misfits_GT1030_RX460_GTX770.mp4", "start" : "01:28"},\
})

configs["episodes"].append(\
{ "title": "Z230",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:34.6", "00:50.2" ), "volume" : 0.999, "padAudio" : 0.1 },\
"overlay" : { \
    "text" : ["'Z230 workstation from HP'",\
              "'CPU\: E3-1241v3 Xeon (i7 4770 equivalent)'",\
              "'RAM\: 32GB DDR3 at 1600 MHz, dual channel'",\
    ]\
}, \
"video" : {"file" : "Z230_closed.mp4" , "rotation" : 180}\
})

configs["episodes"].append(\
{ "title": "1920x1080 results",\
"audio" : {"timestamps" : ("00:50.2", "01:37.3" ),  "padAudio" : 0.1 },\
"video" : {"file" : "stock_DOOMx64vk_2023_11_19_22_20_35_317-converted.mp4", "start" : "10:58"},\
"overlay" : { \
    "image" : {"file" : "1080, low settings.png", "chromaColor" : "0x00FF00"}\
}, \
})

configs["episodes"].append(\
{ "title": "1600x900 results",\
"audio" : {"timestamps" : ("01:37.3", "02:34.7" ),  "padAudio" : 0.1 },\
"video" : {"file" : "stock_DOOMx64vk_2023_11_30_07_58_15_949.mp4", "start" : "26:16"},\
"overlay" : { \
    "image" : {"file" : "900, low settings.png", "chromaColor" : "0x00FF00"}\
}, \
})

configs["episodes"].append(\
{ "title": "1280x720 results",\
"audio" : {"timestamps" : ("02:34.7", "03:13.4" ),  "padAudio" : 0.1 },\
"video" : {"file" : "stock_DOOMvk_2023-12-01 07-45-02.mp4", "start" : "19:00"},\
"overlay" : { \
    "image" : {"file" : "720, low settings.png", "chromaColor" : "0x00FF00"}\
}, \
})

configs["episodes"].append(\
{ "title": "Conclusion",\
"audio" : {"timestamps" : ("03:13.4", "03:24.7" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "breel_autumn_GTX770_HerculeZ.mp4"},\
})

# need a better video for this one; will be needed anyway for the following one.
configs["episodes"].append(\
{ "title": "RX 460",\
"isChapter" : False,\
"audio" : {"timestamps" : ("03:24.7", "03:35.4" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "breel_autumn_RX460.mp4"},\
})

configs["episodes"].append(\
{ "title": "GT 1030",\
"isChapter" : False,\
"audio" : {"timestamps" : ("03:35.4", "03:47.8" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "breel_AsusLP_GT1030_outside.mp4"},\
})

configs["episodes"].append(\
{ "title": "Family 2 and Bye",\
"isChapter" : False,\
"audio" : {"timestamps" : ("03:47.8", "04:02" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "breel_autumn_misfits_GT1030_RX460_GTX770.mp4", "start" : "00:00"},\
})

#scriptedvided.makeVideoForEpisode(configs["episodes"][15], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][9], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][8], configs)
#print(scriptedvided.makeVideoForEpisode(configs["episodes"][9], configs))
#print(scriptedvided.getSuitableVideoStream(configs["episodes"][9], configs))
#print (configs["youtube"])
#print(scriptedvided.getMusicCreditsString(configs["backgroundTrack"]))
#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "Usefulness of the HD 6850"][0], configs)
#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "actual 1080 results"][0], configs)
#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "actual 900 results"][0], configs)
#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "actual 720 results"][0], configs)
#print (scriptedvided.getSuitableImage([x for x in configs["episodes"] if x["title"] == "actual 1080 results"][0], configs))

scriptedvided.makeVideo(configs)
