import scriptedvided

configs = { "defaultAudioFile" : "recap_r9_290X.ogg",\
"mediaFolder" : "C:\\Users\\Admin\\Videos\\recap_R9_290X", \
"stockFolder" : "C:\\Users\\Admin\\Videos\stock",\
"benchmarkFile" : None,\
"outputFolder" : "C:\\Users\\Admin\\Videos\\recap_R9_290X\\output", \
"outputFile" : "recap_r9_290X.mp4", \
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "H:\\Muzica\\royalty free\\Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3",\
"timestamps" : ("00:00", None ), "destinationTimestamp" : {"title" : "TLDW", "until" : "Does it work?"}}, \
{"file" : "H:\\Muzica\\royalty free\\bensound-summer.mp3", "timestamps" : ("00:00", None ), "destinationTimestamp" : { "title": "Does it work?", "until" : "Blooper" }}, \
], "volume" : 0.05 },\
"episodes" : [],\
"youtube" : {"title" : "Recapping a \'well done\' oven baked R9 290X", \
"description" : '''The previous owner of this card attempted the oven baking method to get rid of some artefacts that he was experiencing. 
The session went a bit south, and the power delivery capacitors bloew up.''',\
"links" : '''
Our review of the R9 290X: https://youtu.be/XrdwJSfOHOs

Repair channels:
https://www.youtube.com/c/LearnElectronicsRepair
https://www.youtube.com/channel/UCKU5nwSWYXa3xfXGBlKyvdw
https://www.youtube.com/c/TechCemetery
https://www.youtube.com/c/TheCod3r

''', \
"tags" : "AMD,Radeon,R9 290X,Sapphire,polymeric,electrolytic,capacitors,ESR,artifacting",\
"language" : "EN", \
"Caption certification" : "None",\
"recording date" : None,\
"video location" : None, \
"category" : "Science & Technology", \
"subtitles" : None, \
"endscreen" : None, \
"cards" : None, \
}\
}

configs["episodes"].append(\
{ "title": "TLDW",\
"audio" : {"timestamps" : ("00:00", "00:12.5" ), "volume" : 0.999 },\
"video" : "R9_290X_bb_S_plitGate.mp4",\
})

configs["episodes"].append(\
{ "title": "The ad",\
"audio" : {"timestamps" : ( "00:12.5", "00:27.8" ), "volume" : 0.999 },\
"video" : "olx_ad.mkv",\
})

configs["episodes"].append(\
{ "title": "Baking session gone bad",\
"audio" : {"timestamps" : ( "00:27.8", "00:45.3" ), "volume" : 0.999 },\
"video" : "R9_290X_blownCaps2-converted.mp4",\
})

configs["episodes"].append(\
{ "title": "Bought for 10 USD, needing 30 USD worth of caps",\
"audio" : {"timestamps" : ("00:45.3", "01:01.8" ), "volume" : 0.999 },\
"video" : "adelaida_caps_r9_290x.mkv",\
})

configs["episodes"].append(\
{ "title": "Alternative source for caps",\
"audio" : {"timestamps" : ( "01:01.8", "01:20" ), "volume" : 0.999 },\
"video" : "mobo_ih61_ad.mkv",\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "A closer look at the damage",\
"audio" : {"timestamps" : ( "01:20", "02:19" ), "volume" : 0.999 },\
"video" : "R9_290X_blownCaps2-converted.mp4",\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Aquiring the spare parts",\
"audio" : {"timestamps" : (  "02:19", "02:36.9" ), "volume" : 0.999 },\
"video" : "mobo-contact-seller.mkv",\
})

configs["episodes"].append(\
{ "title": "One man\'s trash, another man\'s treasure",\
"audio" : {"timestamps" : ( "02:36.9", "02:42" ), "volume" : 0.999 },\
"video" : {"file" : "R9_290X_spareCaps-converted.mp4", "start" : "00:00"},\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Recapping the board",\
"audio" : {"timestamps" : ( "02:42", "03:03.4" ), "volume" : 0.999 },\
"video" : "R9_290X_capsRemoved-converted.mp4",\
})

configs["episodes"].append(\
{ "title": "Video card recapped, but ...",\
"audio" : {"timestamps" : ( "03:03.4", "03:26.7" ), "volume" : 0.999 },\
"video" : "R9_290X_recapped-converted.mp4",\
})

configs["episodes"].append(\
{ "title": "Using different caps for input",\
"audio" : {"timestamps" : ( "03:26.7", "03:53.9" ), "volume" : 0.999 },\
"video" : {"file" : "16v-caps.mp4", "rotation" : 90},\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Does it work?",\
"audio" : {"timestamps" : ( "03:53.9", "04:06" ), "volume" : 0.999 },\
"video" : "R9_290X_card.mp4",\
})

configs["episodes"].append(\
{ "title": "At boot time",\
"audio" : {"timestamps" : ( "04:06", "04:12.4" ), "volume" : 0.999 },\
"video" : "R9_290X_booting-converted.mp4",\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Idle, no fan curve",\
"audio" : {"timestamps" : ( "04:12.4", "04:18.7" ), "volume" : 0.999 },\
"video" : "R9_290X_noFanCurve_idle.mp4",\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Heaven, no fan curve",\
"audio" : {"timestamps" : ("04:18.7", "04:29.4" ), "volume" : 0.999 },\
"video" : "R9_290X_Heaven_noFanCurve.mp4",\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Fan curve",\
"audio" : {"timestamps" : ("04:29.4", "04:33.6" ), "volume" : 0.999 },\
"video" : "custom_fan_curve.mp4",\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Alive and kicking",\
"audio" : {"timestamps" : ( "04:33.6", "05:04" ), "volume" : 0.999 },\
"video" : "r9_290X_bb_W_arzone.mp4",\
})

configs["episodes"].append(\
{ "title": "Blooper",\
"audio" : {"timestamps" : ( "05:04" , "05:10.5" ), "volume" : 0.999 },\
"video" : "R9_290X_Heaven_noFanCurve.mp4",\
})


#scriptedvided.makeVideoForEpisode(configs["episodes"][27], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][9], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][8], configs)
#print(scriptedvided.makeVideoForEpisode(configs["episodes"][9], configs))
#print(scriptedvided.getSuitableVideoStream(configs["episodes"][9], configs))
#print (configs["youtube"])
#print(scriptedvided.getMusicCreditsString(configs["backgroundTrack"]))
#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "Fan controller, glued in"][0], configs)
scriptedvided.makeVideo(configs)


