import scriptedvided

configs = { "defaultAudioFile" : "Update_Xeon_E3-1241_V3.ogg",\
"mediaFolder" : "C:\\Users\\Admin\\Videos\\E3_1241_v3", \
"stockFolder" : "C:\\Users\\Admin\\Videos\stock",\
"outputFolder" : "C:\\Users\\Admin\\Videos\\E3_1241_v3\\output", \
"outputFile" : "Update_Haswell_E3_1241_v3.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#00408080"},\
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#00408080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "H:\\Muzica\\royalty free\\Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3",\
"timestamps" : ("00:30", None ), "destinationTimestamp" : {"title" : "TLDW", "until" : "Conclusion"}}, \
{"file" : "H:\\Muzica\\royalty free\\bensound-summer.mp3", "timestamps" : ("00:00", None ), "destinationTimestamp" : { "title": "Conclusion", "until" : "Blooper" }}, \
], "volume" : 0.03 },\
"episodes" : [],\
"youtube" : {"title" : "Abruptly updating the review of the 4 core Haswell processors", \
"description" : '''A unexpected buy, the R9 290X, had me re-visiting the 4 cores Haswell CPUs, with the hope of finding the FPS limits for this group of chips.''',\
"links" : '''
The previous videos on the topic:
https://www.youtube.com/watch?v=xfnZ5kaaKJs
https://www.youtube.com/watch?v=ClxqfeoFZgw

Specs for the Xeon E3 1241 v3 CPU:
https://www.intel.com/content/www/us/en/products/sku/80909/intel-xeon-processor-e31241-v3-8m-cache-3-50-ghz/specifications.html

Specs for the Core i7 4770 CPU:
https://www.intel.com/content/www/us/en/products/sku/75122/intel-core-i74770-processor-8m-cache-up-to-3-90-ghz/specifications.html

Specs for the Core i7 4670 CPU:
https://www.intel.com/content/www/us/en/products/sku/75047/intel-core-i54670-processor-6m-cache-up-to-3-80-ghz/specifications.html

Other videos used:
Hyper Threading video: https://www.youtube.com/watch?v=VcoVYfDVEww
HUB review of the 12600k: https://www.youtube.com/watch?v=LzhwVLUVork

''', \
"tags" : "Intel,4th Gen,Haswell,core i7, core i5, i5,i7,Xeon,4770,i7 4770, 4670, i5 4670",\
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
"audio" : {"timestamps" : ("00:00", "00:17.6" ), "volume" : 0.999 },\
"video" : "warzone-apex-side-by-side.mp4"\
})

configs["episodes"].append(\
{ "title": "Reasons for re-testing the Haswell based Xeon",\
"audio" : {"timestamps" : ("00:17.6", "00:35" ), "volume" : 0.999 },\
"video" : {"file" : "hub_r5_i5.mkv", "start":"00:00"}\
})

# consider inside of the case though, or capture done with HT off
configs["episodes"].append(\
{ "title": "Avoiding GPU bottlenecks",\
"audio" : {"timestamps" : ("00:35", "01:14" ), "volume" : 0.999 },\
"video" : {"file": "i5_4690_W_arzone.mp4", "rotation" : 180},\
})

configs["episodes"].append(\
{ "title": "R9 290X",\
"audio" : {"timestamps" : ("01:14", "01:30" ), "volume" : 0.999 },\
"isChapter" : False,\
"video" : {"file": "R9_290X_bb_A_pex.mp4", "start" : "00:00"},\
})


configs["episodes"].append(\
{ "title": "\'Warzone\' and \'Apex Legends\' got re-tested",\
"audio" : {"timestamps" : ("01:30", "02:00" ), "volume" : 0.999 },\
"video" : "warzone-apex-side-by-side.mp4",\
})


configs["episodes"].append(\
{ "title": " CoD Warzone",\
"audio" : {"timestamps" : ("02:00", "03:02" ) , "volume" : 0.97 },\
"video" : {"file": "i5_4690_W_arzone.mp4", "rotation" : 180},\
"overlay" : { \
    "text" : ["'Call of Duty\: Warzone - 800x600, low settings, hyperthreading OFF (i5 4670-like)'",\
    "'Average\: 134fps, 1\\\% lows\: 85fps'"],\
    },\
})

configs["episodes"].append(\
{ "title": " CoD Warzone (hyperthreading ON, i7 like)",\
"isChapter" : False,\
"audio" : {"timestamps" : ("03:02", "03:45" ) , "volume" : 0.97 },\
"video" : "stock_warzone_paciffic_720p.mp4",\
"overlay" : { \
    "text" : ["'Call of Duty\: Warzone - 800x600, low settings, hyperthreading ON (i7 4770-like)'",\
    "'Average\: 150fps, 1\\\% lows\: 90fps'"],\
    },\
})

configs["episodes"].append(\
{ "title": "Apex Legends",\
"audio" : {"timestamps" : ("03:45", "04:34" ), "volume" : 0.97  },\
"video" : {"file": "i5_4690_A_pexLegends.mp4", "rotation" : 180},\
"overlay" : { \
    "text" : ["'Apex Legends - 1024x768, low settings, hyperthreading OFF (i5 4670-like)'",\
    "'Average\: 144fps, 1\\\% lows\: 107fps'"],\
    },\
})

configs["episodes"].append(\
{ "title": "Apex Legends (hyperthreading ON, equiv. i7)",\
"isChapter" : False,\
"audio" : {"timestamps" : ("04:34", "05:00" ), "volume" : 0.97  },\
"video" : "stock_ApexLegends_1080p.mp4",\
"overlay" : { \
    "text" : ["'Apex Legends - 1024x768, low settings, hyperthreading ON (i7 4770-like)'",\
    "'Average\: 144fps, 1\\\% lows\: 112fps'"],\
    },\
})

configs["episodes"].append(\
{ "title": "Conclusion",\
"audio" : {"timestamps" : ("05:00", "05:40"), "volume" : 0.999 },\
"video" : {"file" : "HyperThreading.mkv", "start" : "00:30"}\
})


configs["episodes"].append(\
{ "title": "Blooper",\
"isChapter" : False,\
"audio" : {"timestamps" : ( "05:44", "05:52"), "volume" : 0.999},\
"video" : "HyperThreading.mkv",\
})


#scriptedvided.makeVideoForEpisode(configs["episodes"][27], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][9], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][8], configs)
#print(scriptedvided.makeVideoForEpisode(configs["episodes"][9], configs))
#print(scriptedvided.getSuitableVideoStream(configs["episodes"][9], configs))
#print (configs["youtube"])
#print(scriptedvided.getMusicCreditsString(configs["backgroundTrack"]))
#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "Apex Legends"][0], configs)
#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "Counter Strike: Global Offensive"][0], configs)
scriptedvided.makeVideo(configs)

