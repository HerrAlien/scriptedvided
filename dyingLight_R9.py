import scriptedvided

configs = { "defaultAudioFile" : "DyingLight_R9.ogg",\
"mediaFolder" : "F:\\Videos\\DyingLight_R9", \
"stockFolder" : "F:\\Videos\\stock",\
"outputFolder" : "F:\\Videos\\DyingLight_R9\\output", \
"outputFile" : "DyingLight_R9.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3",\
"timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "3 GPUs enter a zombie infested city", "until" : "1920x1080 results"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3",\
"timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "1920x1080 results", "until" : "Conclusion"}}, \
{"file" : "Guide You Home - Ferco and Andie - Free Background Music - Audio Library Release.ogg", "timestamps" : ("00:20", None ), "destinationTimestamp" : { "title": "Conclusion", "until" : "Blooper" }}, \
], "volume" : 0.06 },\
"episodes" : [],\
"youtube" : {"title" : "How does CS2 run on some old Radeons? (R7 250, HD 7750, HD 7770)", \
"description" : '''In this video, we'll take a closer look on how the old TeraScale 2 video cards (Radeon HD 7750, HD 7770, R7 250) run Counter Strike 2.
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
"tags" : "Dying Light,Radeon,AMD,R9 280,R9 270,R9 290X,HD7950,HD 7950,HD7870,HD 7870,GCN,GCN1,GCN 1,GCN2,GCN 2",\
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
{ "title": "3 GPUs enter a zombie infested city",\
"audio" : {"timestamps" : ("00:00", "00:08.7" ), "volume" : 0.999, "padAudio" : 0.25 },\
"video" : {"file" : "stock_DyingLightGame_2023_11_19_14_42_58_777-converted.mp4"},\
})

# this will be split up
configs["episodes"].append(\
{ "title": "The GPUs and test system",\
"audio" : {"timestamps" : ("00:08.7", "00:11.4" ), "volume" : 0.999, "padAudio" : 0.25 },\
"video" : {"file" : "R9_family_poor.mkv"},\
})

configs["episodes"].append(\
{ "title": "R9 270",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:11.4", "00:16.2" ), "volume" : 0.999, "padAudio" : 0.25 },\
"video" : {"file" : "breel_r9_270_outside.mp4"},\
})

configs["episodes"].append(\
{ "title": "R9 280",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:16.2", "00:22" ), "volume" : 0.999, "padAudio" : 0.25 },\
"video" : {"file" : "breel_r9_280_outside.mp4"},\
})

configs["episodes"].append(\
{ "title": "R9 290X",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:22", "00:30" ), "volume" : 0.999, "padAudio" : 0.25 },\
"video" : {"file" : "breel_r9_290x_outside.mp4"},\
})

configs["episodes"].append(\
{ "title": "Z230",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:30", "00:47" ), "volume" : 0.999, "padAudio" : 0.25 },\
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
"audio" : {"timestamps" : ("00:47", "01:32" ), "padAudio" : 0.25 },\
"video" : {"file" : "stock_DyingLightGame_2023_11_19_14_23_33_387-converted.mp4", "start" : "00:40"},\
"overlay" : { \
    "image" : {"file" : "1080, low settings.png", "chromaColor" : "0x00FF00"}\
}, \
})

configs["episodes"].append(\
{ "title": "1600x900 results",\
"audio" : {"timestamps" : ("01:32", "02:18" ), "padAudio" : 0.25 },\
"video" : {"file" : "stock_DyingLightGame_2023_11_19_14_42_58_777-converted.mp4" , "start" : "11:52"},\
"overlay" : { \
    "image" : {"file" : "900, low settings.png", "chromaColor" : "0x00FF00"}\
}, \
})

configs["episodes"].append(\
{ "title": "1280x720 results",\
"audio" : {"timestamps" : ("02:18", "02:46" ), "padAudio" : 0.25 },\
"video" : {"file" : "stock_DyingLightGame_2023_11_19_14_23_33_387-converted.mp4", "start" : "11:05"},\
"overlay" : { \
    "image" : {"file" : "720, low settings.png", "chromaColor" : "0x00FF00"}\
}, \
})

configs["episodes"].append(\
{ "title": "1080 high (R9 280)",\
"audio" : {"timestamps" : ("02:46", "03:08" ), "padAudio" : 0.25 },\
"video" : {"file" : "stock_DyingLightGame_2023_11_19_14_42_58_777-converted.mp4" , "start" : "02:35"},\
"overlay" : { \
    "text" : [scriptedvided.r6sText('1920x1080, high settings', 41, 36)]\
}, \
})

configs["episodes"].append(\
{ "title": "Conclusion",\
"audio" : {"timestamps" : ("03:08", "03:17.4" ), "volume" : 0.999, "padAudio" : 0.25 },\
"video" : {"file" : "breel_autumn_misfits_GT1030_RX460_GTX770.mp4", "start" : "00:00"},\
})

configs["episodes"].append(\
{ "title": "Bye",\
"isChapter" : False,\
"audio" : {"timestamps" : ("03:17.4", "03:24.5" ), "volume" : 0.999, "padAudio" : 0.25 },\
"video" : {"file" : "R9_family_poor.mkv"},\
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
