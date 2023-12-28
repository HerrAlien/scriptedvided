import scriptedvided

configs = { "defaultAudioFile" : "Finals_gtx770,960,1050Ti,R9_280.ogg",\
"mediaFolder" : "F:\\Videos\\Finals_R9_280_GTX770_960_1050Ti", \
"stockFolder" : "F:\\Videos\\stock",\
"outputFolder" : "F:\\Videos\\Finals_R9_280_GTX770_960_1050Ti\\output", \
"outputFile" : "Finals_R9_280_GTX770_960_1050Ti.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#00008080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3",\
"timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "The Finals - weird minimum specs", "until" : "1920x1080 results"}}, \
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
{ "title": "The Finals - weird minimum specs",\
"audio" : {"timestamps" : ("00:00", "00:20.3" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "stock_Finals_2023_12_27_winners.mp4", "start":"05:11"},\
"overlay" : { \
    "image" : {"file" : "requirements.PNG", "chromaColor" : "0x00FF00"}\
}, \
})

# this will be split up
configs["episodes"].append(\
{ "title": "Family",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:20.3", "00:32.3" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "broll_GTX1050Ti_960_770_R9_280.mp4", "start":"00:00"},\
})

configs["episodes"].append(\
{ "title": "GTX 1050Ti",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:32.3", "00:44.2" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "broll_GTX1050Ti_960_770_R9_280.mp4", "start":"02:30"},\
})

# 7770 - 51, 7750 - 01:40 

configs["episodes"].append(\
{ "title": "GTX 960",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:44.2", "00:55.6" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "broll_GTX1050Ti_960_770_R9_280.mp4", "start":"01:59"},\
})

configs["episodes"].append(\
{ "title": "R9 280",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:55.6", "01:04.7" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "broll_GTX1050Ti_960_770_R9_280.mp4", "start":"01:24"},\
})

configs["episodes"].append(\
{ "title": "GTX 770",\
"isChapter" : False,\
"audio" : {"timestamps" : ("01:04.7", "01:15" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "broll_GTX1050Ti_960_770_R9_280.mp4", "start":"00:40"},\
})

configs["episodes"].append(\
{ "title": "Test system and settings",\
"audio" : {"timestamps" : ("01:15", "01:40.3" ), "volume" : 0.999, "padAudio" : 0.1 },\
"overlay" : { \
    "text" : ["'Z230 workstation from HP'",\
              "'CPU\: E3-1241v3 Xeon (i7 4770 equivalent)'",\
              "'RAM\: 32GB DDR3 at 1600 MHz, dual channel'",\
              "'... but Simon says i5-6600K or Ryzen 5 1600 ...'",\
    ]\
}, \
"video" : {"file" : "Z230_closed.mp4" , "rotation" : 180}\
})

configs["episodes"].append(\
{ "title": "settings",\
"isChapter" : False,\
"audio" : {"timestamps" : ("01:40.3", "01:47.7" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "stock_Finals_2023_12_27_winners.mp4", "start":"00:36"},\
})

configs["episodes"].append(\
{ "title": "1920x1080 results",\
"audio" : {"timestamps" : ("01:47.7", "03:02.5" ),  "padAudio" : 0.1 },\
"video" : {"file" : "stock_Finals_2023_12_27_winners.mp4", "start" : "02:05"},\
"overlay" : { \
    "image" : {"file" : "1080, low settings.png", "chromaColor" : "0x00FF00"}\
}, \
})

configs["episodes"].append(\
{ "title": "1600x900 results",\
"audio" : {"timestamps" : ("03:02.5", "03:41.4" ),  "padAudio" : 0.1 },\
"video" : {"file" : "stock_Finals_2023_12_27_winners.mp4", "start" : "04:05"},\
"overlay" : { \
    "image" : {"file" : "900, low settings.png", "chromaColor" : "0x00FF00"}\
}, \
})

configs["episodes"].append(\
{ "title": "1280x720 results",\
"audio" : {"timestamps" : ("03:41.4", "04:33" ),  "padAudio" : 0.1 },\
"video" : {"file" : "stock_Finals_2023_12_26_long.mp4", "start" : "07:30"},\
"overlay" : { \
    "image" : {"file" : "720, low settings.png", "chromaColor" : "0x00FF00"}\
}, \
})

configs["episodes"].append(\
{ "title": "Conclusion",\
"audio" : {"timestamps" : ("04:33", "04:49" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "breel_r9_280_outside.mp4"},\
})

# need a better video for this one; will be needed anyway for the following one.
configs["episodes"].append(\
{ "title": "GTX 770 - not better",\
"isChapter" : False,\
"audio" : {"timestamps" : ("04:49", "05:07" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "breel_autumn_GTX770_HerculeZ.mp4"},\
})

configs["episodes"].append(\
{ "title": "Neither 770 nor 280",\
"isChapter" : False,\
"audio" : {"timestamps" : ("05:07", "05:17.7" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "breel_GTX770_R9_280_attic.mp4"},\
})

configs["episodes"].append(\
{ "title": "1050Ti and 960 do better",\
"isChapter" : False,\
"audio" : {"timestamps" : ("05:17.7", "05:30.5" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "broll_GTX1050Ti_outside.mp4"},\
})

configs["episodes"].append(\
{ "title": "What about that CPU",\
"isChapter" : False,\
"audio" : {"timestamps" : ("05:30.5", "05:39.9" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "stock_Finals_2023_12_27_winners.mp4"},\
})

configs["episodes"].append(\
{ "title": "Family again and bye",\
"isChapter" : False,\
"audio" : {"timestamps" : ("05:39.9", "05:53" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "broll_GTX1050Ti_960_770_R9_280.mp4", "start":"00:00"},\
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
