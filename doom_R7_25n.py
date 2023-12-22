import scriptedvided

configs = { "defaultAudioFile" : "Doom_R7_25N.ogg",\
"mediaFolder" : "F:\\Videos\\Doom_r7_25N", \
"stockFolder" : "F:\\Videos\\stock",\
"outputFolder" : "F:\\Videos\\Doom_r7_25N\\output", \
"outputFile" : "Doom_r7_25N.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "Going even lower in performance", "until" : "1920x1080 results"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "1920x1080 results", "until" : "Is this the end for Cape Verde?"}}, \
{"file" : "Guide You Home - Ferco and Andie - Free Background Music - Audio Library Release.ogg", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "Is this the end for Cape Verde?", "until" : "Introduce the trick"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "The trick - explained", "until" : "Conclusion"}}, \
{"file" : "Guide You Home - Ferco and Andie - Free Background Music - Audio Library Release.ogg", "timestamps" : ("00:20", None ), "destinationTimestamp" : { "title": "Conclusion", "until" : "Blooper" }}, \
], "volume" : 0.06 },\
"episodes" : [],\
"youtube" : {"title" : "Old Radeon GPUs - DOOMed to obsolescence?", \
"description" : '''In this video, we'll see if 3 of the AMD Radeon entry level R7 cards handle 2016's DOOM.
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
"tags" : "Doom,Doom 2016,GCN,AMD,Radeon,CapeVerde,Cape Verde,R7 250,R7 250E,R7 250 E,R7 250 512SP,HD7750,HD 7750,R7 250X,R7 250 X,HD7770,HD 7770",\
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
{ "title": "Going even lower in performance",\
"audio" : {"timestamps" : ("00:00", "00:13" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "stock_DOOMx64vk_2023_11_25_16_20_54_735.mp4", "start" : "04:00"},\
})


# this will be split up
configs["episodes"].append(\
{ "title": "The GPUs and test system",\
"audio" : {"timestamps" : ("00:13", "00:19" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "stock_CapeVerde_family.mp4", "start" : "00:00", "rotation" : 90}\
})

configs["episodes"].append(\
{ "title": "R7 250",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:19", "00:24.33" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "stock_CapeVerde_family.mp4", "start" : "02:24", "rotation" : 90}\
})

configs["episodes"].append(\
{ "title": "HD 7750",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:24.33", "00:33" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "stock_CapeVerde_family.mp4", "start" : "01:40", "rotation" : 90}\
})

configs["episodes"].append(\
{ "title": "HD 7770",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:33", "00:40" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "stock_CapeVerde_family.mp4", "start" : "00:51", "rotation" : 90}\
})

configs["episodes"].append(\
{ "title": "Z230",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:40", "00:55.3" ), "volume" : 0.999, "padAudio" : 0.1 },\
"overlay" : { \
    "text" : ["'Z230 workstation from HP'",\
              "'CPU\: E3-1241v3 Xeon (i7 4770 equivalent)'",\
              "'RAM\: 32GB DDR3 at 1600 MHz, dual channel'",\
    ]\
}, \
"video" : {"file" : "Z230_closed.mp4" , "rotation" : 180}\
})


configs["episodes"].append(\
{ "title": "The trick",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:55.3", "01:02.4" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "stock_DOOMx64vk_RX460_r_shadowAtlasWidth_8.mp4", "start" : "00:00"},\
})

configs["episodes"].append(\
{ "title": "1920x1080 results",\
"audio" : {"timestamps" : ("01:02.4", "01:39.8" ), "padAudio" : 0.1 },\
"video" : {"file" : "stock_DOOMx64vk_2023_11_30_07_58_15_949.mp4" , "start" : "06:50"},\
"overlay" : { \
    "image" : {"file" : "1080, low settings.png", "chromaColor" : "0x00FF00"}\
}, \
})

configs["episodes"].append(\
{ "title": "1600x900 results",\
"audio" : {"timestamps" : ("01:39.8", "02:14.9" ), "padAudio" : 0.1 },\
"video" : {"file" : "stock_DOOMx64vk_2023_11_30_07_58_15_949.mp4" , "start" : "12:00"},\
"overlay" : { \
    "image" : {"file" : "900, low settings.png", "chromaColor" : "0x00FF00"}\
}, \
})

configs["episodes"].append(\
{ "title": "1280x720 results",\
"audio" : {"timestamps" : ("02:14.9", "02:43.7" ), "padAudio" : 0.1 },\
"video" : {"file" : "stock_DOOMx64vk_2023_12_01_15_08_59_653.mp4" , "start" : "32:50"},\
"overlay" : { \
    "image" : {"file" : "720, low settings.png", "chromaColor" : "0x00FF00"}\
}, \
})

# this will be split up
configs["episodes"].append(\
{ "title": "Is this the end for Cape Verde?",\
"audio" : {"timestamps" : ("02:43.7", "02:58.5" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "stock_CapeVerde_family.mp4", "start" : "00:00", "rotation" : 90}\
})

configs["episodes"].append(\
{ "title": "Introduce the trick",\
"isChapter" : False,\
"audio" : {"timestamps" : ("02:58.5", "03:04.2" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "stock_CapeVerde_family.mp4", "start" : "00:00", "rotation" : 90}\
})

configs["episodes"].append(\
{ "title": "The trick - explained",\
"isChapter" : False,\
"audio" : {"timestamps" : ("03:04.2", "03:21.2" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "stock_noShadowD-O-O-M.mp4" , "start" : "00:03"},\
})

configs["episodes"].append(\
{ "title": "1280x720 results (no shadows)",\
"audio" : {"timestamps" : ("03:21.2", "04:06.8" ), "padAudio" : 0.1 },\
"video" : {"file" : "stock_DOOMx64vk_RX460_r_shadowAtlasWidth_8.mp4", "start" : "02:45"},\
"overlay" : { \
    "image" : {"file" : "720, low settings, no shadows.png", "chromaColor" : "0x00FF00"}\
}, \
})


configs["episodes"].append(\
{ "title": "Conclusion",\
"audio" : {"timestamps" : ("04:06.8", "04:15.9" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "stock_CapeVerde_family.mp4", "start" : "00:00", "rotation" : 90}\
})

configs["episodes"].append(\
{ "title": "misfits",\
"isChapter" : False,\
"audio" : {"timestamps" : ("04:15.9", "04:27.6" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "breel_autumn_misfits_GT1030_RX460_GTX770.mp4" , "start" : "00:00"},\
})

configs["episodes"].append(\
{ "title": "Bye",\
"isChapter" : False,\
"audio" : {"timestamps" : ("04:27.6", "04:34.2" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "stock_CapeVerde_family.mp4", "start" : "00:00", "rotation" : 90}\
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
