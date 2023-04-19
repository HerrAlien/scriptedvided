import scriptedvided

configs = { "defaultAudioFile" : "gta5_vs_ts2.ogg",\
"mediaFolder" : "F:\\Videos\\gta5_vs_ts2", \
"stockFolder" : "F:\\Videos\\stock",\
"outputFolder" : "F:\\Videos\\gta5_vs_ts2\\output", \
"outputFile" : "TeraScale2_gta5.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3",\
"timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "TLDW", "until" : "1920x1080 results"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3",\
"timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "1920x1080 results", "until" : "Conclusion"}}, \
{"file" : "bensound-summer.mp3",\
"timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Conclusion", "until" : "bye - gta5"}}, \
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
{ "title": "TLDW",\
"audio" : {"timestamps" : ("00:00", "00:12" ), "volume" : 0.999, "padAudio" : 0.25 },\
"video" : {"file" : "broll_ts2family_outside.mp4"}\
})

configs["episodes"].append(\
{ "title": "Minimum specs",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:12", "00:27" ), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : "requirements.mkv"\
})

# this will be split up
configs["episodes"].append(\
{ "title": "family1",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:27", "00:41" ), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "broll_ts2family_outside.mp4"}\
})

configs["episodes"].append(\
{ "title": "GPUs, test system and benchmark",\
"audio" : {"timestamps" : ("00:41", "00:47" ), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "broll_ts2_family_outside_takingTurns.mp4", "start" : "00:02"}\
})

configs["episodes"].append(\
{ "title": "hd5770 6850",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:47", "00:52.5" ), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "broll_ts2_family_outside_takingTurns.mp4", "start" : "00:20"}\
})

configs["episodes"].append(\
{ "title": "hd6670",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:52.5" , "00:57"), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "broll_ts2_family_outside_takingTurns.mp4", "start" : "00:40"}\
})

configs["episodes"].append(\
{ "title": "Z230",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:57" , "01:09.5"), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "Z230_closed.mp4" , "rotation" : 180}\
})

configs["episodes"].append(\
{ "title": "benchmark",\
"isChapter" : False,\
"audio" : {"timestamps" : ("01:09.5", "01:23.5"), "volume" : 0.999 , "padAudio" : 0.25 },\
"video" : {"file" : "stock_gta5_1080p.mp4" }\
})

### needs video
configs["episodes"].append(\
{ "title": "1920x1080 results",\
"audio" : {"timestamps" : ("00:00", "00:08"), "volume" : 0.001 , "padAudio" : 0.25 },\
"video" : {"file" : "stock_gtaV_tutorial.mp4", "start" : "01:20"}\
})

configs["episodes"].append(\
{ "title": "actual 1080 results",\
"isChapter" : False,\
"audio" : {"timestamps" : ("01:23.5", "02:31"), "volume" : 0.95 , "padAudio" : 0.25 },\
"video" : {"file" : "1080_firefight.mp4"}\
})


### needs video
configs["episodes"].append(\
{ "title": "1600x900 results",\
"audio" : {"timestamps" : ("00:00", "00:06"), "volume" : 0.001 , "padAudio" : 0.25 },\
"video" : {"file" : "stock_gtaV_tutorial.mp4", "start" : "02:44"}\
})

configs["episodes"].append(\
{ "title": "actual 900 results",\
"isChapter" : False,\
"audio" : {"timestamps" : ("02:31", "03:46"), "volume" : 0.95 , "padAudio" : 0.25 },\
"video" : {"file" : "900_driving.mp4"}\
})



### needs video
configs["episodes"].append(\
{ "title": "1280x720 results",\
"audio" : {"timestamps" : ("00:00", "00:08"), "volume" : 0.001 , "padAudio" : 0.25 },\
"video" : {"file" : "stock_gtaV_tutorial2.mp4", "start" : "03:00"}\
})

configs["episodes"].append(\
{ "title": "actual 720 results",\
"isChapter" : False,\
"audio" : {"timestamps" : ("03:46", "04:29.5"), "volume" : 0.95 , "padAudio" : 0.25 },\
"video" : {"file" : "720_standoff.mp4"}\
})



configs["episodes"].append(\
{ "title": "Conclusion",\
"audio" : {"timestamps" : ("00:00", "00:09"), "volume" : 0.001 , "padAudio" : 0.25 },\
"video" : {"file" : "stock_gtaV_tutorial2.mp4", "start" : "07:30"}\
})

configs["episodes"].append(\
{ "title": "family 2",\
"isChapter" : False,\
"audio" : {"timestamps" : ( "04:29.5",  "05:01"), "volume" : 0.999 , "padAudio" : 1 },\
"video" : {"file" : "broll_ts2family_outside.mp4"}\
})


configs["episodes"].append(\
{ "title": "bye - gta5",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:00", "00:12"), "volume" : 0.001 , "padAudio" : 0.25 },\
"video" : {"file" : "stock_gtaV_tutorial2.mp4", "start" : "08:30"}\
})


configs["episodes"].append(\
{ "title": "ending",\
"isChapter" : False,\
"audio" : {"timestamps" : ( "05:01", "05:09"), "volume" : 0.8 , "padAudio" : 0.25 },\
"video" : {"file" : "stock_gtaV_tutorial2.mp4", "start" : "08:59"}\
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
