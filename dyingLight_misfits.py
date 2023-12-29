import scriptedvided

configs = { "defaultAudioFile" : "DyingLight_misfits.ogg",\
"mediaFolder" : "F:\\Videos\\DyingLight_misfits", \
"stockFolder" : "F:\\Videos\\stock",\
"outputFolder" : "F:\\Videos\\DyingLight_misfits\\output", \
"outputFile" : "DyingLight_misfits.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#00800080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3",\
"timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "Cheap hardware playing good games", "until" : "1920x1080 results"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3",\
"timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "1920x1080 results", "until" : "Conclusion"}}, \
{"file" : "Guide You Home - Ferco and Andie - Free Background Music - Audio Library Release.ogg", "timestamps" : ("00:20", None ), "destinationTimestamp" : { "title": "Conclusion", "until" : "Blooper" }}, \
], "volume" : 0.06 },\
"episodes" : [],\
"youtube" : {"title" : "How does CS2 run on some old Radeons? (R7 250, HD 7750, HD 7770)", \
"description" : '''In this video, we'll experience some zombie apocalypse survival while playing Dying Light on two GeForce cards (GTX 770 and GT 1030) and one Radeon (RX 460).
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
"tags" : "Dying Light,NVidia,AMD,GeForce,Radeon,Kepler,Pascal,Polaris,GTX770,GTX 770,GT1030,GT 1030,RX460,RX 460",\
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
{ "title": "Cheap hardware playing good games",\
"audio" : {"timestamps" : ("00:00", "00:12.5" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "stock_DyingLightGame_2023_11_19_14_23_33_387-converted.mp4"},\
})

# this will be split up
configs["episodes"].append(\
{ "title": "The GPUs and test system",\
"audio" : {"timestamps" : ("00:12.5", "00:24.5" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "breel_autumn_misfits_GT1030_RX460_GTX770.mp4", "start" : "00:00"},\
})

configs["episodes"].append(\
{ "title": "GTX 770",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:24.5", "00:31.5" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "breel_autumn_misfits_GT1030_RX460_GTX770.mp4", "start" : "01:28"},\
})

# 7770 - 51, 7750 - 01:40 

configs["episodes"].append(\
{ "title": "RX 460",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:31.5", "00:39.7" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "breel_autumn_misfits_GT1030_RX460_GTX770.mp4", "start" : "00:30"},\
})

configs["episodes"].append(\
{ "title": "GT 1030",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:39.7", "00:47.5" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "breel_autumn_misfits_GT1030_RX460_GTX770.mp4", "start" : "00:56"},\
})

configs["episodes"].append(\
{ "title": "Z230",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:47.5", "01:05.7" ), "volume" : 0.999, "padAudio" : 0.1 },\
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
"audio" : {"timestamps" : ("01:05.7", "01:47.5" ), "padAudio" : 0.1 },\
"video" : {"file" : "stock_DyingLightGame_2023_11_19_14_23_33_387-converted.mp4" },\
"overlay" : { \
    "image" : {"file" : "1080, low settings.png", "chromaColor" : "0x00FF00"}\
}, \
})

configs["episodes"].append(\
{ "title": "1600x900 results",\
"audio" : {"timestamps" : ("01:47.5", "02:32.5" ), "padAudio" : 0.1 },\
"video" : {"file" : "stock_DyingLightGame_2023_11_19_14_42_58_777-converted.mp4"},\
"overlay" : { \
    "image" : {"file" : "900, low settings.png", "chromaColor" : "0x00FF00"}\
}, \
})

configs["episodes"].append(\
{ "title": "1280x720 results",\
"audio" : {"timestamps" : ("02:32.5", "03:04.4" ), "padAudio" : 0.1 },\
"video" : {"file" : "stock_DyingLight_r7_265_includesBenchmarkRun.mp4"},\
"overlay" : { \
    "image" : {"file" : "720, low settings.png", "chromaColor" : "0x00FF00"}\
}, \
})

configs["episodes"].append(\
{ "title": "Conclusion",\
"audio" : {"timestamps" : ("03:04.4", "03:11" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "breel_rx460_outside.mp4"},\
})

configs["episodes"].append(\
{ "title": "NVIDIA - good",\
"isChapter" : False,\
"audio" : {"timestamps" : ("03:11", "03:21.3" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "breel_autumn_misfits_GT1030_RX460_GTX770.mp4", "start" : "00:00"},\
})

configs["episodes"].append(\
{ "title": "Bye",\
"isChapter" : False,\
"audio" : {"timestamps" : ("03:21.3", "03:26" ), "padAudio" : 0.1 },\
"video" : {"file" : "stock_DyingLightGame_2023_11_19_14_23_33_387-converted.mp4" },\
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
