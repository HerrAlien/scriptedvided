import scriptedvided

configs = { "defaultAudioFile" : "GCN_vs_Overwatch2.ogg",\
"mediaFolder" : "C:\\Users\\Admin\\Videos\\overwatch_gcn", \
"stockFolder" : "C:\\Users\\Admin\\Videos\stock",\
"outputFolder" : "C:\\Users\\Admin\\Videos\\overwatch_gcn\\output", \
"outputFile" : "overwatch_gcn.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "H:\\Muzica\\royalty free\\Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3",\
"timestamps" : ("00:30", None ), "destinationTimestamp" : {"title" : "The TLDW", "until" : "1920x1080"}}, \
{"file" : "H:\\Muzica\\royalty free\\Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3",\
"timestamps" : ("00:30", None ), "destinationTimestamp" : {"title" : "1920x1080 - training", "until" : "1920x1080 - in game"}}, \
{"file" : "H:\\Muzica\\royalty free\\Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3",\
"timestamps" : ("00:30", None ), "destinationTimestamp" : {"title" : "1920x1080 - bot match", "until" : "1600x900"}}, \
{"file" : "H:\\Muzica\\royalty free\\Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3",\
"timestamps" : ("00:30", None ), "destinationTimestamp" : {"title" : "1600x900 - training", "until" : "1280x720"}}, \
{"file" : "H:\\Muzica\\royalty free\\Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3",\
"timestamps" : ("00:30", None ), "destinationTimestamp" : {"title" : "1280x720 - training", "until" : "Conclusion"}}, \
{"file" : "H:\\Muzica\\royalty free\\bensound-summer.mp3", "timestamps" : ("00:00", None ), "destinationTimestamp" : { "title": "Conclusion", "until" : "Blooper" }}, \
], "volume" : 0.03 },\
"episodes" : [],\
"youtube" : {"title" : "Can older Radeon cards play Overwatch 2?", \
"description" : '''In this video, we'll take a closer look on how older GCN 1.0 and 2.0 cards perform in Overwatch 2.''',\
"links" : '''
More games tested with the R9 280:
https://www.youtube.com/playlist?list=PLH6sLgdc_uJ6cLPtH9eylU5IXbHJ3QpQc

TechPowerup entry:
https://www.techpowerup.com/gpu-specs/sapphire-dual-x-r9-280-oc-with-boost.b2845

Phillip's HD 7000 series video:
https://www.youtube.com/watch?v=wsuP_9afO9c
''', \
"tags" : "Overwatch,Overwatch 2,Overwatch2,AMD,ATI,Radeon,GCN,R9 290X,R9 280,HD7950,HD 7950,R7 265,HD7850,HD 7850,R7 260,R7 250X,HD7770,HD 7770,R7 250",\
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
"audio" : {"timestamps" : ("00:00", "00:20.5" ), "volume" : 0.999 },\
"video" : "stock_Overwatch2_gameplay.mp4"\
})

configs["episodes"].append(\
{ "title": "GCN 1.0 - minimum specs for Overwatch 2",\
"audio" : {"timestamps" : ("00:20.5", "00:57.5" ), "volume" : 0.999 },\
"video" : "the_family.mkv"\
})

# this will be split up
configs["episodes"].append(\
{ "title": "Cards tested and test setup",\
"audio" : {"timestamps" : ("00:57.5", "01:21.65" ), "volume" : 0.999 },\
"video" : "gcn_low.mp4"\
})

configs["episodes"].append(\
{ "title": "Cards tested and test setup - med",\
"isChapter" : False,\
"audio" : {"timestamps" : ("01:21.65", "01:43.5" ), "volume" : 0.999 },\
"video" : "gcn_mids.mp4"\
})

configs["episodes"].append(\
{ "title": "Cards tested and test setup - high",\
"isChapter" : False,\
"audio" : {"timestamps" : ("01:43.5", "01:55.5" ), "volume" : 0.999 },\
"video" : "gcn_highs.mp4"\
})

configs["episodes"].append(\
{ "title": "Cards tested and test setup - resolutions",\
"isChapter" : False,\
"audio" : {"timestamps" : ("01:55.5" , "02:13.5" ), "volume" : 0.999 },\
"video" : "the_family.mkv"\
})

configs["episodes"].append(\
{ "title": "1920x1080",\
"audio" : {"file" : "silence_30min.ogg" , "timestamps" : ("00:00", "00:10" ), "volume" : 0.01 },\
"video" : {"file": "stock_Overwatch2_training.mp4", "start" : "00:17"},\
"overlay" : { "text" : ["'1920x1080, low settings, tutorial level'"] },\
})


configs["episodes"].append(\
{ "title": "1920x1080 - training",\
"isChapter" : False,\
"audio" : {"timestamps" : ("02:13.5", "03:02.5" ), "volume" : 0.999 },\
"video" : {"file" : "stock_Overwatch2_training.mp4", "start" : "00:00"},\
"overlay" : { \
    "image" : {"file" : "1080, low settings, tutorial level.png"}\
}, \
})

configs["episodes"].append(\
{ "title": "1920x1080 - in game",\
"isChapter" : False,\
"audio" : {"file" : "silence_30min.ogg" , "timestamps" : ("00:00", "00:10" ), "volume" : 0.01 },\
"video" : {"file": "stock_Overwatch2_gameplay.mp4", "start" : "00:20"},\
"overlay" : { "text" : ["'1920x1080, low settings, bot match'"] },\
})

configs["episodes"].append(\
{ "title": "1920x1080 - bot match",\
"isChapter" : False,\
"audio" : {"timestamps" : ( "03:02.5",  "03:19.5" ), "volume" : 0.999 },\
"video" : "stock_Overwatch2_gameplay.mp4",\
"overlay" : {\
    "image" : {"file" : "1080, low settings, bot match.png"}\
}, \
})

configs["episodes"].append(\
{ "title": "1600x900",\
"audio" : {"file" : "silence_30min.ogg" , "timestamps" : ("00:00", "00:10" ), "volume" : 0.01 },\
"video" : {"file": "stock_Overwatch2_training.mp4", "start" : "01:10"},\
"overlay" : { "text" : ["'1600x900, low settings, tutorial level'"] },\
})

configs["episodes"].append(\
{ "title": "1600x900 - training",\
"isChapter" : False,\
"audio" : {"timestamps" : ( "03:19.5", "04:11" ), "volume" : 0.999 },\
"video" : {"file" : "stock_Overwatch2_training.mp4", "start" : "01:50"}
"overlay" : { \
    "image" : {"file" : "900, low settings, tutorial level.png"}\
}, \
})

configs["episodes"].append(\
{ "title": "1280x720",\
"audio" : {"file" : "silence_30min.ogg" , "timestamps" : ("00:00", "00:10" ), "volume" : 0.01 },\
"video" : {"file": "stock_Overwatch2_training.mp4", "start" : "04:16"},\
"overlay" : { "text" : ["'1280x720, low settings, tutorial level'"] },\
})

configs["episodes"].append(\
{ "title": "1280x720 - training",\
"isChapter" : False,\
"audio" : {"timestamps" : ("04:11", "05:40" ), "volume" : 0.999 },\
"video" : {"file" : "stock_Overwatch2_training.mp4", "start" : "04:30"}
"overlay" : { \
    "image" : {"file" : "720, low settings, tutorial level.png"}\
}, \
})

configs["episodes"].append(\
{ "title": "Conclusion",\
"audio" : {"timestamps" : ("05:40" , "06:10" ), "volume" : 0.999 },\
"video" : "stock_Overwatch2_gameplay.mp4"\
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

