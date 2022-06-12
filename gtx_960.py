import scriptedvided

configs = { "defaultAudioFile" : "gtx_960.ogg",\
"mediaFolder" : "C:\\Users\\Admin\\Videos\\gtx_960", \
"stockFolder" : "C:\\Users\\Admin\\Videos\stock",\
"benchmarkFile" : "C:\\Users\\Admin\\Videos\\gtx_960\\Benchmark_gtx960.txt",\
"outputFolder" : "C:\\Users\\Admin\\Videos\\gtx_960\\output", \
"outputFile" : "gtx_960.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#00800080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "H:\\Muzica\\royalty free\\Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3",\
"timestamps" : ("00:30", None ), "destinationTimestamp" : {"title" : "Context of the launch", "until" : "Apex Legends"}}, \
{"file" : "H:\\Muzica\\royalty free\\bensound-summer.mp3", "timestamps" : ("00:00", None ), "destinationTimestamp" : { "title": "Usefulness of used GPUs", "until" : "end-of-video" }}, \
], "volume" : 0.03 },\
"episodes" : [],\
"youtube" : {"title" : "The half review for the fully dead GTX 960", \
"description" : '''This GTX 960 was sold as defective; and while it could be resurrected for a short while, this was not to last.''',\
"links" : '''
More games tested with the GT 1030:
https://www.youtube.com/watch?v=6GplcZaKbW8
https://www.youtube.com/watch?v=LZMuVTUvT7I

TechPowerup entries:
https://www.techpowerup.com/gpu-specs/kfa2-gt-1030.b4633
https://www.techpowerup.com/gpu-specs/geforce-gt-1030.c2954

Intel 11th gen processors:
The core i5 11400 (has an IGPU): https://ark.intel.com/content/www/us/en/ark/products/212270/intel-core-i511400-processor-12m-cache-up-to-4-40-ghz.html
The core i5 11400F (no IGPU): https://ark.intel.com/content/www/us/en/ark/products/212271/intel-core-i511400f-processor-12m-cache-up-to-4-40-ghz.html

NVidia Special Event (Pascal): https://www.youtube.com/watch?v=0xnzwjPyx8A
Office PC and GT 1030: https://www.youtube.com/watch?v=yP4z2Vdmf1o
R7 250 review: https://youtu.be/L4oFUVoxIzs
''', \
"tags" : "NVidia,GeForce,Maxwell,GTX960,GTX 960",\
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
{ "title": "Shorter video this time around",\
"audio" : {"timestamps" : ("00:00", "00:22" ), "volume" : 0.999 },\
"video" : "gtx_960_rotating.mp4"\
})

configs["episodes"].append(\
{ "title": "The GPU",\
"audio" : {"timestamps" : ("00:31", "01:04" ), "volume" : 0.999 },\
"video" : "gtx_960_techpowerup.mkv",\
})


configs["episodes"].append(\
{ "title": "Cooling and thermals",\
"audio" : {"timestamps" : ( "02:08", "02:24" ), "volume" : 0.999 },\
"video" : {"file" : "gtx_960_cooling.mp4"},\
})

configs["episodes"].append(\
{ "title": "Cooling and thermals - thermals only",\
"audio" : {"timestamps" : ( "02:24", "02:53" ), "volume" : 0.999 },\
"video" : "gtx_960_heaven.mp4",\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "This is a full size card",\
"audio" : {"timestamps" : ( "01:25", "02:08" ), "volume" : 0.999 },\
"isChapter" : False,\
"video" : "gtx_960_techpowerup.mkv",\
})


##configs["episodes"].append(\
##{ "title": "Cooling solution - axial",\
##"audio" : {"timestamps" : ("01:46", "02:07" ), "volume" : 0.9 },\
##"video" : "r7_260_1.mov",\
##"overlay" : { \
##    "text" : ["'Example of a cooler using axial fans'",\
##              "'(ASUS Radeon R7 260)'"]\
##}, \
##"isChapter" : False,\
##})


configs["episodes"].append(\
{ "title": "CoD Warzone",\
"audio" : {"timestamps" : ("03:21.3", "03:49" ) , "volume" : 0.97 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "720p, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Battlefield V",\
"audio" : {"timestamps" : ("03:49", "04:20.6" ) , "volume" : 0.97 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "720p, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Control",\
"audio" : {"timestamps" : ("04:20.6", "04:44.13") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "720p, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Rainbow Six: Siege",\
"audio" : {"timestamps" : ("04:44.13", "05:18.5") },\
"overlay" : { \
    "text" : ["'Rainbow Six\: Siege'",\
              "'1080p, low setings, 100\\\% render scale - Average\: 101fps, 1\\\% lows\: 78ps'",\
              "'720p, low setings, 100\\\% render scale - Average\: 179fps, 1\\\% lows\: 114fps'",\
              "'1080p, low setings, 50\\\% render scale - Average\: 143fps, 1\\\% lows\: 103fps'",\
              "'720p, low setings, 50\\\% render scale - Average\: 207fps, 1\\\% lows\: 139fps'"]\
}, \
})


configs["episodes"].append(\
{ "title": "Rocket League",\
"audio" : {"timestamps" : ("07:29.5", "07:53.4") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1080p, low settings, 100% render scale", \
    }\
}, \
})


configs["episodes"].append(\
{ "title": "Genshin Impact",\
"audio" : {"timestamps" : ("08:53", "09:16") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1080p, low settings, 1.0 render scale", \
    }\
}, \
})


configs["episodes"].append(\
{ "title": "Rogue Company",\
"audio" : {"timestamps" : ("09:55", "10:19.4") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1080p, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Warframe",\
"audio" : {"timestamps" : ("10:35", "10:58.7") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1080p, low settings", \
    }\
}, \
})


configs["episodes"].append(\
{ "title": "Alien: Isolation",\
"audio" : {"timestamps" : ("05:18.5","05:36.1") },\
"video" : "stock_Alien_Isolation_1080p.mp4",\
"overlay" : { \
    "text" : ["'Alien\: Isolation'",\
              "'Did not complete benchmark'"]\
}, \
})

configs["episodes"].append(\
{ "title": "Usefulness of the GTX 960",\
"audio" : {"timestamps" : ("10:58.7", "11:30.45"), "volume" : 0.999 },\
"video" : "gtx_960_control.mp4"\
})

#configs["episodes"].append(\
#{ "title": "Usefulness of the R7 250",\
#"audio" : {"timestamps" : ("12:11.06", "12:53.27") },\
#"video" : {"file" : "", "start":""}\
#})


#scriptedvided.makeVideoForEpisode(configs["episodes"][27], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][9], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][8], configs)
#print(scriptedvided.makeVideoForEpisode(configs["episodes"][9], configs))
#print(scriptedvided.getSuitableVideoStream(configs["episodes"][9], configs))
#print (configs["youtube"])
#print(scriptedvided.getMusicCreditsString(configs["backgroundTrack"]))
#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "Usefulness of the HD 6850"][0], configs)
#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "Warframe"][0], configs)
scriptedvided.makeVideo(configs)

