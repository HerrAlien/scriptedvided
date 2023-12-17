import scriptedvided

configs = { "defaultAudioFile" : "Doom_R7_26N.ogg",\
"mediaFolder" : "F:\\Videos\\Doom_R7_26N", \
"stockFolder" : "F:\\Videos\\stock",\
"outputFolder" : "F:\\Videos\\Doom_R7_26N\\output", \
"outputFile" : "Doom_R7_26N.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3",\
"timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "DOOM, 3 GPUs and a test system", "until" : "1920x1080 results"}}, \
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
"tags" : "DOOM,Radeon,AMD,1GB,2GB,SM5,GCN,GCN 1.0,GCN 2.0,GCN2,R7 260,HD7790,HD 7790,R7 260X,HD7850,HD 7850,R7 265,R7 370,MSI,ASUS,Sapphire,60 FPS,60FPS",\
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
{ "title": "DOOM, 3 GPUs and a test system",\
"audio" : {"timestamps" : ("00:00", "00:08.5" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "stock_Doom_2016.mp4", "start" : "02:45"},\
})

# this will be split up
configs["episodes"].append(\
{ "title": "Intro",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:08.5", "00:17.15" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "stock_midGCNs_family.mp4", "start" : "00:00"},\
})

configs["episodes"].append(\
{ "title": "R7 260",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:17.15", "00:23" ), "volume" : 0.999, "padAudio" : 0.25 },\
"video" : {"file" : "stock_midGCNs_family.mp4", "start" : "00:40"}\
})

# 7770 - 51, 7750 - 01:40 

configs["episodes"].append(\
{ "title": "R7 260X",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:23", "00:29.6" ), "volume" : 0.999, "padAudio" : 0.25 },\
"video" : {"file" : "stock_midGCNs_family.mp4", "start" : "01:05"}\
})

configs["episodes"].append(\
{ "title": "R7 265",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:29.6", "00:37" ), "volume" : 0.999, "padAudio" : 0.25 },\
"video" : {"file" : "stock_midGCNs_family.mp4", "start" : "01:38"}\
})

configs["episodes"].append(\
{ "title": "Z230",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:37", "00:53" ), "volume" : 0.999, "padAudio" : 0.25 },\
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
"audio" : {"timestamps" : ("00:53", "01:50" ), "padAudio" : 0.1 },\
"video" : {"file" : "stock_DOOMx64vk_2023_11_19_22_20_35_317-converted.mp4", "start" : "05:50"},\
"overlay" : { \
    "image" : {"file" : "1080, low settings.png", "chromaColor" : "0x00FF00"}\
}, \
})

configs["episodes"].append(\
{ "title": "1600x900 results",\
"audio" : {"timestamps" : ("01:50", "02:37" ), "padAudio" : 0.1 },\
"video" : {"file" : "stock_DOOMx64vk_2023_11_19_22_20_35_317-converted.mp4", "start" : "11:00"},\
"overlay" : { \
    "image" : {"file" : "900, low settings.png", "chromaColor" : "0x00FF00"}\
}, \
})

configs["episodes"].append(\
{ "title": "1280x720 results",\
"audio" : {"timestamps" : ("02:37", "03:22.7" ), "padAudio" : 0.1 },\
"video" : {"file" : "stock_DOOMx64vk_2023_11_25_16_20_54_735.mp4", "start" : "04:00"},\
"overlay" : { \
    "image" : {"file" : "720, low settings.png", "chromaColor" : "0x00FF00"}\
}, \
})

configs["episodes"].append(\
{ "title": "Conclusion",\
"audio" : {"timestamps" : ("03:22.7", "03:36.5" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "stock_midGCNs_family.mp4", "start" : "00:00" },\
})

# need a better video for this one; will be needed anyway for the following one.
configs["episodes"].append(\
{ "title": "GCN family - entry level",\
"isChapter" : False,\
"audio" : {"timestamps" : ("03:36.5", "03:44.2" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "stock_CapeVerde_family.mp4", "start" : "00:00", "rotation" : 90}\
})

configs["episodes"].append(\
{ "title": "Bye",\
"isChapter" : False,\
"audio" : {"timestamps" : ("03:44.2", "03:51" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "stock_midGCNs_family.mp4", "start" : "00:00" },\
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
