import scriptedvided

configs = { "defaultAudioFile" : "TeraScale2_Fortnite.ogg",\
"mediaFolder" : "C:\\Users\\Admin\\Videos\\TeraScale2_endOf2022", \
"stockFolder" : "C:\\Users\\Admin\\Videos\stock",\
"outputFolder" : "C:\\Users\\Admin\\Videos\\TeraScale2_endOf2022\\output", \
"outputFile" : "TeraScale2_Fortnite.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "H:\\Muzica\\royalty free\\Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3",\
"timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "The TLDW", "until" : "1600x900 - training"}}, \
], "volume" : 0.06 },\
"episodes" : [],\
"youtube" : {"title" : "Can older Radeon cards play Overwatch 2?", \
"description" : '''In this video, we'll take a closer look on how the old TeraScale 2 video cards (Radeon HD 5770, HD 6850, HD 5870) run Fortnite.
As usual, we're pairing the cards with the i7 4770 equivalent Xeon (E3-1241 v3), and 32 GB DDR3 @1600MHz, in dual channel.''',\
"links" : '''
More games tested with the TeraScale 2 cards:
https://www.youtube.com/watch?v=9ZrKAwA6MbQ&list=PLgBGV4K3p2_YhzgbzcQ6kdgfGpzdq6cRD

Intel 4th gen core i7 review:
https://www.youtube.com/watch?v=ClxqfeoFZgw
''', \
"tags" : "Fortnite,AMD,ATI,Radeon,TeraScale 2,HD 5770,HD5770,HD 6850,HD6850,HD 5870,HD5870",\
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
{ "title": "The TLDW",\
"audio" : {"timestamps" : ("00:00", "00:17" ), "volume" : 0.999, "padAudio" : 0.25 },\
"video" : "TeraScale2_family1.mp4"\
})

configs["episodes"].append(\
{ "title": "Caution - not out of the box",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:17", "00:52" ), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : "hd5770_fortnite_BReel.mp4"\
})

# this will be split up
configs["episodes"].append(\
{ "title": "Fixing the full-screen issues",\
"audio" : {"timestamps" : ("00:52", "01:04" ), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : "fortnite-not-liking-terascale2.mkv"\
})

configs["episodes"].append(\
{ "title": "Menu - does not draw",\
"isChapter" : False,\
"audio" : {"timestamps" : ("01:04", "01:23" ), "volume" : 0.75 , "padAudio" : 0.25 },\
"video" : {"file" : "lobby2_mp4.mp4", "start" : "00:00"}\
})

configs["episodes"].append(\
{ "title": "F11",\
"isChapter" : False,\
"audio" : {"timestamps" : ("01:23", "01:45" ), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "F_ortnite_lobby_f11.mp4", "start" : "00:28"}\
})

configs["episodes"].append(\
{ "title": "Game settings and PC setup",\
"audio" : {"timestamps" : ("01:45" , "02:16"), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "F_ortnite_settings.mkv" , "start" : "00:10"}\
})

configs["episodes"].append(\
{ "title": "PC setup",\
"isChapter" : False,\
"audio" : {"timestamps" : ("02:16", "02:42"), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "z230_cpuz_intel_ark.mkv" , "start" : "00:10"}\
})


configs["episodes"].append(\
{ "title": "Test results",\
"isChapter" : False,\
"audio" : {"timestamps" : ("02:42", "02:53"), "volume" : 0.95 , "padAudio" : 0.25 },\
"video" : {"file" : "benchmark_FortJoneses_1080_fullScale.mp4" , "start" : "00:10"}\
})

configs["episodes"].append(\
{ "title": "scale 100 percent",\
"isChapter" : False,\
"audio" : {"timestamps" : ("02:53", "03:04"), "volume" : 0.95 , "padAudio" : 0.25 },\
"video" : {"file" : "F_ortnite_TS2_100scale.mp4" , "start" : "00:00"}\
})

configs["episodes"].append(\
{ "title": "scale 100 percent - techpowerup",\
"isChapter" : False,\
"audio" : {"timestamps" : ("03:04", "03:18"), "volume" : 0.95 , "padAudio" : 0.25 },\
"video" : {"file" : "TeraScale2_relativePerformance_hierarchy.mp4"}\
})

configs["episodes"].append(\
{ "title": "scale 100 percent - 3",\
"isChapter" : False,\
"audio" : {"timestamps" : ("03:18", "03:45"), "volume" : 0.95 , "padAudio" : 0.25 },\
"video" : {"file" : "F_ortnite_TS2_100scale.mp4", "start":"00:07"}\
})

configs["episodes"].append(\
{ "title": "1920x1080, render scale 50 percent",\
"audio" : {"timestamps" : ("03:45", "03:54.6"), "volume" : 0.95 , "padAudio" : 0.25 },\
"video" : {"file" : "like.mp4", "start":"00:02"}\
})

configs["episodes"].append(\
{ "title": "scale 50 percent - breel",\
"isChapter" : False,\
"audio" : {"timestamps" : ("03:54.6", "04:05.6"), "volume" : 0.95 , "padAudio" : 0.25 },\
"video" : {"file" : "benchmark_FortJoneses_1080_scale50.mp4"}\
})

configs["episodes"].append(\
{ "title": "scale 50 percent",\
"isChapter" : False,\
"audio" : {"timestamps" : ("04:05.6", "04:20.4"), "volume" : 0.95 , "padAudio" : 0.25 },\
"video" : {"file" : "F_ortnite_TS2_50scale.mp4"}\
})

configs["episodes"].append(\
{ "title": "scale 50 percent vs 100 percent",\
"isChapter" : False,\
"audio" : {"timestamps" : ("04:20.4", "04:37.7"), "volume" : 0.95 , "padAudio" : 0.25 },\
"video" : {"file" : "both_results_2.mp4", "start":"00:22"}\
})

configs["episodes"].append(\
{ "title": "scale 50 percent - hierarchy",\
"isChapter" : False,\
"audio" : {"timestamps" : ( "04:37.7", "04:54"), "volume" : 0.95 , "padAudio" : 0.25 },\
"video" : {"file" : "F_ortnite_TS2_50scale.mp4"}\
})

configs["episodes"].append(\
{ "title": "Conclusions",\
"audio" : {"timestamps" : ("04:54" , "05:00" ), "volume" : 0.95 , "padAudio" : 0.25 },\
"video" : {"file" : "both_results_2.mp4", "start":"00:50"}\
})

configs["episodes"].append(\
{ "title": "Conclusions - 5770",\
"isChapter" : False,\
"audio" : {"timestamps" : ("05:00", "05:26" ), "volume" : 0.999  , "padAudio" : 0.25 },\
"video" : {"file" : "pricing_5870_6850_5770.mkv"}\
})

configs["episodes"].append(\
{ "title": "Conclusions - family",\
"isChapter" : False,\
"audio" : {"timestamps" : ("05:26", "05:50" ), "volume" : 0.999  , "padAudio" : 2 },\
"video" : {"file" : "TeraScale2_family2.mp4", "rotation" : 180}\
})

#scriptedvided.makeVideoForEpisode(configs["episodes"][27], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][9], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][8], configs)
#print(scriptedvided.makeVideoForEpisode(configs["episodes"][9], configs))
#print(scriptedvided.getSuitableVideoStream(configs["episodes"][9], configs))
#print (configs["youtube"])
#print(scriptedvided.getMusicCreditsString(configs["backgroundTrack"]))
#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "Usefulness of the HD 6850"][0], configs)
#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "1280x720"][0], configs)
#print (scriptedvided.getSuitableImage([x for x in configs["episodes"] if x["title"] == "1920x1080"][0], configs))

scriptedvided.makeVideo(configs)

