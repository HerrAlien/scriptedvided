import scriptedvided
import sv_ffutils

configs = { "defaultAudioFile" : "E5-2680-v2.ogg",\
"mediaFolder" : "F:\\Videos\\e5-2680-v2", \
"stockFolder" : "F:\\Videos\\stock",\
"benchmarkFile" : "F:\\Videos\\e5-2680-v2\\Benchmark_e5-2680-v2.txt",\
"outputFolder" : "F:\\Videos\\e5-2680-v2\\output", \
"outputFile" : "E5-2680-v2.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#00008080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "The Ivy Bridge Server CPU", "until" : "Marvel Rivals"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Marvel Rivals", "until" : "Overwatch 2"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Overwatch 2", "until" : "Checking the IPC"}}, \
{"file" : "Ferco - Inquisitiveness.ogg", "timestamps" : ("01:01", None ), "destinationTimestamp" : {"title" : "Checking the IPC", "until" : "Conclusions"}}, \
{"file" : "Inspired - MaikonMusic  Free Background Music  Audio Library Release.mp3", "timestamps" : ("00:00", None ), "destinationTimestamp" : {"title" : "Conclusions", "until" : "EOF"}}, \
], "volume" : 0.038 },\
"episodes" : [],\
"youtube" : {"title" : "", \
"description" : '''''',\
"links" : '''
Track: Bliss Of Heaven - SOMM [Audio Library Release]
Music provided by Audio Library Plus
Watch: https://www.youtube.com/watch?v=JQ6mKeQLZak&t=0s
Free Download / Stream: https://alplus.io/blisss-heaven

Track: Far Far Away - Ferco [Audio Library Release]
Music provided by Audio Library Plus
Watch: https://www.youtube.com/watch?v=SrkQ3K1umlc&t=0s 
Free Download / Stream: https://alplus.io/far-far-away

Track: Ferco - Inquisitiveness
Creative Commons - Attribution 3.0 Unported (CC BY 3.0)
Free Download: https://hypeddit.com/mlsvxq
Streams: https://share.amuse.io/track/ferco-inquisitiveness
Video: https://www.youtube.com/watch?v=dhJdmwLWtFM&t=0s


Track: Inspired - MaikonMusic [Audio Library Release]
Music provided by Audio Library Plus
Watch: https://www.youtube.com/watch?v=RUkdTkk_52o&t=0s
Free Download / Stream: https://alplus.io/inspired

''', \
"tags" : "",\
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

#"isChapter" : False, \

####################### intro ###############################

# this is the hook 
#  scriptedvided.nextTS\(configs\)\, \"\"
#  \"file\" *\: *\".*\"
#  \"video\" *: *\{\"file\" *: *\".* \"\}
# \"video\" *: *\{ *\"file\" *: *\".*\" *\}
#  scriptedvided.r6sText\('.*' *\, *[0-9]*\, *[0-9]*\)
#   "timestamps" *\: *\( *"[0-9\:\.]*" *\, *"[0-9\:\.]*" *\)
#configs["episodes"].append(\
#{ "title": "A favorite of miners and gamers alike",\
#"audio" : {"timestamps" : (scriptedvided.nextTS(configs),  "" ), "volume" : 0.999, "padAudio" : 0.05 },\
#"video" : {"file" : ""},\
#})

configs["episodes"].append(\
{ "title": "The Ivy Bridge Server CPU",\
"audio" : {"timestamps" : ("00:00", "00:06.8"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "E5-2680-v2_inHand_barred.mp4"},\
})

configs["episodes"].append(\
{ "title": "Helldivers 2 preview",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:17.2" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "HellDivers2.mkv"},\
"isChapter" : False,\
})

# cpu cache
configs["episodes"].append(\
{ "title": "Why it could be good",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:29.7" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "E5-2680-v2_onZ420Board_inHand_barred.mp4"},\
})


configs["episodes"].append(\
{ "title": "Max ram freq",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:40.2" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Z420_inGrass_barred.mp4"},\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "The test system",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:58.3" ), "volume" : 0.999, "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Custom PC'",\
              "'CPU\: Xeon E5 2680 v2'",\
              "'RAM\: 32GB DDR3, 1066 MHz, quad channel'",\
              "'GPU\: Strix GTX 980'",\
    ]\
}, \
"video" : {"file" : "Z420_testSys3_barred.mp4"},\
})

configs["episodes"].append(\
{ "title": "IPC test preview",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:07.5" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Gigasus_ffwd10.mp4", "start" : "00:00"},\
"isChapter" : False,\
})

####################### end of intro ###############################


####################### gaming section ###############################
configs["episodes"].append(\
{ "title": "Marvel Rivals",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:37.6" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, 30% render scale, low settings", \
    }\
}, \
"video" : {"file" : "marvelrivals.mkv", "start" : "04:00"},\
})

# needs redone
configs["episodes"].append(\
{ "title": "Cyberpunk 2077",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:05.2" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : [sv_ffutils.ffmpegSafeString('Cyberpunk 2077'),\
              sv_ffutils.ffmpegSafeString('1280x720, performance FSR, lowest settings'),\
              scriptedvided.r6sText('High crowd density' , 87 , 56  ),\
              scriptedvided.r6sText('Low crowd density' , 100 , 64  ),\
]}, \
"video" : {"file" : "CP2077-crowdsHigh-s-60-e-121.mkv", "start" : "01:00"},\
})

# needs redone
configs["episodes"].append(\
{ "title": "Helldivers 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:28.2" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, performance FSR, lowest settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "ARC Raiders",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:47.5" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
}, \
})

# single resolution
configs["episodes"].append(\
{ "title": "Doom Eternal",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:06.5" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
},\
})

configs["episodes"].append(\
{ "title": "Apex Legends",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:25.5" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
},\
"video" : "ApexLegends.mkv",\
})

configs["episodes"].append(\
{ "title": "Control",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:44" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, lowest settings", \
    }\
},\
"video" : "Control.mkv",\
})

configs["episodes"].append(\
{ "title": "Counter-Strike 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:07.8" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, balanced FSR, low settings", \
    }\
}\
})

configs["episodes"].append(\
{ "title": "Fortnite",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:29.8" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, performance mode", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "The Finals",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:55.6" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, 50% scale, lowest settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Overwatch 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:18.7" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, 50% render scale, low settings", \
    }\
}\
})

configs["episodes"].append(\
{ "title": "Rainbow Six: Siege",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:35.8"), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, 50% scale, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Borderlands 3",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:48.9" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, 50% render scale, very low settings", \
    }\
},\
})

configs["episodes"].append(\
{ "title": "Shadow of the Tomb Raider",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:02.9" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, 50% render scale, lowest settings", \
    }\
},\
})

####################### end of gaming section ###############################


############################ productivity #################################

# this is both time and cycles, for both SMT on and off
configs["episodes"].append(\
{ "title": "Checking the IPC",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:19.1" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Gigasus_ffwd10.mp4", "start" : "00:00"},\
})

configs["episodes"].append(\
{ "title": "time",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:31.1" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Gigasus_ffwd10.mp4", "start" : "00:40"},\
"isChapter" : False,\
"overlay" : { \
    "image" : {"file" : "E5-2680-v2-Time-HL2.png"}\
}, \
})

configs["episodes"].append(\
{ "title": "ipc alone",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:39" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Gigasus_ffwd10.mp4", "start" : "00:30"},\
"isChapter" : False,\
"overlay" : { \
    "image" : {"file" : "ipc alone.png"}\
}, \
})

configs["episodes"].append(\
{ "title": "ipc",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:54.2" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Gigasus_ffwd10.mp4", "start" : "00:15"},\
"isChapter" : False,\
"overlay" : { \
    "image" : {"file" : "E5-2680-v2-IPC-HL2.png"}\
}, \
})

#############################################################################



####################### conclusion ###############################
# happy that it works
configs["episodes"].append(\
{ "title": "Conclusions",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:02.9" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "E5-2680-v2_inHand_barred.mp4"},\
})

configs["episodes"].append(\
{ "title": "best scenario for ddr3",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:13.5" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "E5-2680-v2_onZ420Board_inHand_barred.mp4"},\
})

configs["episodes"].append(\
{ "title": "Ali Express CPU price",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:21.3" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "aliexpress-e5-2680-v2.mkv"},\
})

configs["episodes"].append(\
{ "title": "Compared to Ryzen prices",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:28.5" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "olx-r5-1600.mkv"},\
})

configs["episodes"].append(\
{ "title": "LGA2011 mobo vs AM4",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:37.9" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "aliexpress-x79-mobo.mkv"},\
})

configs["episodes"].append(\
{ "title": "8th gen breel",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:44.4" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_i5-8400_inHand_barred.mp4"},\
})

configs["episodes"].append(\
{ "title": "bye",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:52.4" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "E5-2680-v2_inHand_barred.mp4"},\
})


##configs["episodes"].append(\
##{ "title": "Blooper",\
##"isChapter" : False,\
##"audio" : {"timestamps" : (scriptedvided.nextTS(configs),  "" ) },\
##"video" : {"file" : ""}\
##})

#scriptedvided.makeVideoForEpisode(configs["episodes"][8], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][9], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][13], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][15], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][16], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][17], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][18], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][19], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][21], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][22], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][24], configs)
#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "Borderlands 3"][0], configs)
#scriptedvided.makeVideo(configs)

#for x in range(19,26):
#    scriptedvided.makeVideoForEpisode(configs["episodes"][x], configs)
#
scriptedvided.makeVideo(configs)

