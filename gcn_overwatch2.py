import scriptedvided

configs = { "defaultAudioFile" : "r9_280_2.ogg",\
"mediaFolder" : "C:\\Users\\Admin\\Videos\\overwatch_gcn", \
"stockFolder" : "C:\\Users\\Admin\\Videos\stock",\
"outputFolder" : "C:\\Users\\Admin\\Videos\\overwatch_gcn\\output", \
"outputFile" : "overwatch_gcn.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "H:\\Muzica\\royalty free\\Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3",\
"timestamps" : ("00:30", None ), "destinationTimestamp" : {"title" : "Context of the launch", "until" : "Video capturing leads to CPU bottleneck"}}, \
{"file" : "H:\\Muzica\\royalty free\\bensound-summer.mp3", "timestamps" : ("00:00", None ), "destinationTimestamp" : { "title": "Usefulness of used GPUs", "until" : "Blooper" }}, \
], "volume" : 0.03 },\
"episodes" : [],\
"youtube" : {"title" : "AMD's GCN cards play Overwatch 2", \
"description" : '''In this video, we'll take a closer look to Sapphire's R9 280 Dual-X OC with boost.''',\
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
"audio" : {"timestamps" : ("00:00", "00:12" ), "volume" : 0.999 },\
"video" : "stock_Overwatch2_gameplay.mp4"\
})

configs["episodes"].append(\
{ "title": "GCN 1.0 - minimum specs for Overwatch 2",\
"audio" : {"timestamps" : ("00:12", "00:39.33" ), "volume" : 0.999 },\
"video" : "the_family.mkv"\
})

# this will be split up
configs["episodes"].append(\
{ "title": "Cards tested and test setup",\
"audio" : {"timestamps" : ("00:46", "00:59" ), "volume" : 0.999 },\
"video" : ""\
})


configs["episodes"].append(\
{ "title": "1920x1080",\
"audio" : {"timestamps" : ("00:59", "01:50" ), "volume" : 0.999 },\
"video" : "R9_280_GPU.mkv",\
"overlay" : { \
    "image" : {"file" : "1080, low settings, tutorial level.png"}\
}, \
})

configs["episodes"].append(\
{ "title": "1920x1080 - bot match",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:59", "01:50" ), "volume" : 0.999 },\
"video" : "R9_280_GPU.mkv",\
"overlay" : { \
    "image" : {"file" : "1080, low settings, bot match.png"}\
}, \
})

configs["episodes"].append(\
{ "title": "1600x900",\
"audio" : {"timestamps" : ("00:59", "01:50" ), "volume" : 0.999 },\
"video" : "R9_280_GPU.mkv",\
"overlay" : { \
    "image" : {"file" : "900, low settings, tutorial level.png"}\
}, \
})

configs["episodes"].append(\
{ "title": "1280x720",\
"audio" : {"timestamps" : ("00:59", "01:50" ), "volume" : 0.999 },\
"video" : "R9_280_GPU.mkv",\
"overlay" : { \
    "image" : {"file" : "720, low settings, tutorial level.png"}\
}, \
})


#scriptedvided.makeVideoForEpisode(configs["episodes"][27], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][9], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][8], configs)
#print(scriptedvided.makeVideoForEpisode(configs["episodes"][9], configs))
#print(scriptedvided.getSuitableVideoStream(configs["episodes"][9], configs))
#print (configs["youtube"])
#print(scriptedvided.getMusicCreditsString(configs["backgroundTrack"]))
#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "Usefulness of the HD 6850"][0], configs)
#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "Warframe"][0], configs)
print (scriptedvided.getSuitableImage([x for x in configs["episodes"] if x["title"] == "1920x1080"][0], configs))

#scriptedvided.makeVideo(configs)

