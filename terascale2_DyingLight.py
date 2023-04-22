import scriptedvided

configs = { "defaultAudioFile" : "DyingLight_TS2.ogg",\
"mediaFolder" : "F:\\Videos\\DyingLight_TS2", \
"stockFolder" : "F:\\Videos\\stock",\
"outputFolder" : "F:\\Videos\\DyingLight_TS2\\output", \
"outputFile" : "TeraScale2_DyingLight.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3",\
"timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "Dying Light - free until 13th of April", "until" : "1920x1080 results"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3",\
"timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "1920x1080 results", "until" : "Conclusion"}}, \
{"file" : "bensound-summer.mp3",\
"timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Conclusion", "until" : "end of video"}}, \
], "volume" : 0.06 },\
"episodes" : [],\
"youtube" : {"title" : "Can older Radeon cards play Overwatch 2?", \
"description" : '''In this video, we'll take a closer look on how the old TeraScale 2 video cards (Radeon HD 6670, HD 5770, HD 6850, HD 5870) run Dying Light (Enhanced Edition).
As usual, we're pairing the cards with the i7 4770 equivalent Xeon (E3-1241 v3), and 32 GB DDR3 @1600MHz, in dual channel.''',\
"links" : '''
More games tested with the TeraScale 2 cards:
https://www.youtube.com/watch?v=9ZrKAwA6MbQ&list=PLgBGV4K3p2_YhzgbzcQ6kdgfGpzdq6cRD

Intel 4th gen core i7 review:
https://www.youtube.com/watch?v=ClxqfeoFZgw
''', \
"tags" : "Dying Light,AMD,ATI,Radeon,TeraScale 2,HD 5770,HD5770,HD 6850,HD6850,HD 5870,HD5870,HD 6670,HD6670",\
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
{ "title": "Dying Light - free until 13th of April",\
"audio" : {"timestamps" : ("00:00", "00:08.5" ), "volume" : 0.999, "padAudio" : 0.25 },\
"video" : {"file" : "dying_light_free_2.mkv", "start" : "00:06"}\
})

configs["episodes"].append(\
{ "title": "Minimum specs",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:08.5", "00:27" ), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : "dying_light_requirements.mkv"\
})

# this will be split up
configs["episodes"].append(\
{ "title": "expectations based on the 5870",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:27", "00:47" ), "volume" : 0.9 , "padAudio" : 0.25 },\
"video" : {"file" : "stock_DyingLight_antizen.mp4", "start" : "01:55"}\
})

configs["episodes"].append(\
{ "title": "Test, settings and hardware",\
"audio" : {"timestamps" : ("00:47", "00:56" ), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "stock_DyingLight_drZere.mp4", "start" : "00:00"}\
})

configs["episodes"].append(\
{ "title": "hardware",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:56", "01:09.5" ), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "Z230_closed.mp4", "start" : "00:00", "rotation" : 180}\
})

configs["episodes"].append(\
{ "title": "hd5870",\
"isChapter" : False,\
"audio" : {"timestamps" : ("01:09.5", "01:17.5" ), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "broll_ts2_family_outside_takingTurns.mp4", "start" : "00:02"}\
})

configs["episodes"].append(\
{ "title": "hd5770 6850",\
"isChapter" : False,\
"audio" : {"timestamps" : ("01:17.5", "01:24" ), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "broll_ts2_family_outside_takingTurns.mp4", "start" : "00:20"}\
})

configs["episodes"].append(\
{ "title": "hd6670",\
"isChapter" : False,\
"audio" : {"timestamps" : ("01:24" , "01:31.5"), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "broll_ts2_family_outside_takingTurns.mp4", "start" : "00:40"}\
})

### needs video
configs["episodes"].append(\
{ "title": "1920x1080 results",\
"audio" : {"timestamps" : ("01:31.5", "02:11.6"), "volume" : 0.9 , "padAudio" : 0.25 },\
"video" : {"file" : "1080_low_settings.mp4"}\
})


configs["episodes"].append(\
{ "title": "6670 relative to 5870",\
"isChapter" : False,\
"audio" : {"timestamps" : ("02:11.6", "02:31"), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "hd6670_relativePerf_hd5870.mkv"}\
})

### needs video
configs["episodes"].append(\
{ "title": "1600x900 results",\
"audio" : {"timestamps" : ("02:31", "03:11"), "volume" : 0.90 , "padAudio" : 0.25 },\
"video" : {"file" : "900p_low_settings.mp4"}\
})

### needs video
configs["episodes"].append(\
{ "title": "1280x720 results",\
"audio" : {"timestamps" : ("03:11", "03:59"), "volume" : 0.90 , "padAudio" : 0.25 },\
"video" : {"file" : "720p_low_settings.mp4"}\
})

configs["episodes"].append(\
{ "title": "Conclusion",\
"audio" : {"timestamps" : ("03:59", "04:14"), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "dying_light_requirements.mkv"}\
})

configs["episodes"].append(\
{ "title": "free 2",\
"isChapter" : False,\
"audio" : {"timestamps" : ("04:14", "04:23"), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "dying_light_free_1.mkv"}\
})

configs["episodes"].append(\
{ "title": "closing",\
"isChapter" : False,\
"audio" : {"timestamps" : ( "04:23",  "04:30"), "volume" : 0.9 , "padAudio" : 1 },\
"video" : {"file" : "stock_DyingLight_crane.mp4", "start" : "00:30"}\
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
