import scriptedvided

configs = { "defaultAudioFile" : "",\
"mediaFolder" : "F:\\Videos\\....", \
"stockFolder" : "F:\\Videos\\stock",\
"benchmarkFile" : "F:\\Videos\\....\\....",\
"outputFolder" : "F:\\Videos\\....\\output", \
"outputFile" : ".....mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "", "until" : "Rainbow Six: Siege"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Rainbow Six: Siege", "until" : "Fortnite"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Fortnite", "until" : "Conclusions"}}, \
{"file" : "Inspired - MaikonMusic  Free Background Music  Audio Library Release.mp3", "timestamps" : ("00:00", None ), "destinationTimestamp" : {"title" : "Conclusions", "until" : "EOF"}}, \
], "volume" : 0.05 },\
"episodes" : [],\
"youtube" : {"title" : "", \
"description" : ''' GPU Hook 
We're using the same Z230 workstation with an i7 4770 equivalent CPU and 32 GB of DDR3 running in dual channel at 1600MHz.''',\
"links" : '''
Track: Bliss Of Heaven - SOMM [Audio Library Release]
Music provided by Audio Library Plus
Watch: https://www.youtube.com/watch?v=JQ6mKeQLZak&t=0s
Free Download / Stream: https://alplus.io/blisss-heaven

Track: Far Far Away - Ferco [Audio Library Release]
Music provided by Audio Library Plus
Watch: https://www.youtube.com/watch?v=SrkQ3K1umlc&t=0s 
Free Download / Stream: https://alplus.io/far-far-away

Track: Inspired - MaikonMusic [Audio Library Release]
Music provided by Audio Library Plus
Watch: https://www.youtube.com/watch?v=RUkdTkk_52o&t=0s
Free Download / Stream: https://alplus.io/inspired

Our 2023 review of the HD 7770: 
Our 2022 review of the HD 7770: https://youtu.be/4rEcNy2YC0I

TechPowerup entries: https://www.techpowerup.com/gpu-specs/radeon-r7-260.c2511
TechPowerup entries: https://www.techpowerup.com/gpu-specs/asus-r7-260-1-gb.b2732
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
#configs["episodes"].append(\
#{ "title": "A favorite of miners and gamers alike",\
#"audio" : {"timestamps" : ("09:37.3", "09:46" ), "volume" : 0.999, "padAudio" : 0.05 },\
#"video" : {"file" : "rx580_ethereumDust.mp4", "start" : "00:00"},\
#})

configs["episodes"].append(\
{ "title": "",\
"audio" : {"timestamps" : ("00:00", "" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

## HD5770
configs["episodes"].append(\
{ "title": "The GPUs",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "HD6670",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "GT730",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "R7 250",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

# the game, fortnite 
configs["episodes"].append(\
{ "title": "Test setup",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "The test system",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "volume" : 0.999, "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Custom build'",\
              "'CPU\: Ryzen 5 3600'",\
              "'RAM\: 32GB DDR4 at 3000 MHz, dual channel'",\
    ]\
}, \
"video" : {"file" : "test_system_noGPU.mp4" }\
})

####################### end of intro ###############################

####################### gaming section ###############################
configs["episodes"].append(\
{ "title": "Fortnite, Chapter 6 Season 1",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "padAudio" : 0.05 },\
"video" : "" \
})

configs["episodes"].append(\
{ "title": "1080p C6S1",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : "", "chromaColor" : "0x00FF00"}\
}, \
"video" : "" \
})

configs["episodes"].append(\
{ "title": "900p C6S1",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : "", "chromaColor" : "0x00FF00"}\
}, \
"video" : "" \
})

configs["episodes"].append(\
{ "title": "720p C6S1",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : "", "chromaColor" : "0x00FF00"}\
}, \
"video" : "" \
})

configs["episodes"].append(\
{ "title": "Fortnite OG, Chapter 1 Season 1",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "padAudio" : 0.05 },\
"video" : "" \
})

configs["episodes"].append(\
{ "title": "1080p OG C1S1",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : "", "chromaColor" : "0x00FF00"}\
}, \
"video" : "" \
})

configs["episodes"].append(\
{ "title": "900p OG C1S1",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : "", "chromaColor" : "0x00FF00"}\
}, \
"video" : "" \
})

configs["episodes"].append(\
{ "title": "720p OG C1S1",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : "", "chromaColor" : "0x00FF00"}\
}, \
"video" : "" \
})

configs["episodes"].append(\
{ "title": "Fortnite Reload",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "padAudio" : 0.05 },\
"video" : "" \
})

configs["episodes"].append(\
{ "title": "1080p Reload",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : "", "chromaColor" : "0x00FF00"}\
}, \
"video" : "" \
})

configs["episodes"].append(\
{ "title": "900p Reload",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : "", "chromaColor" : "0x00FF00"}\
}, \
"video" : "" \
})

configs["episodes"].append(\
{ "title": "720p Reload",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : "", "chromaColor" : "0x00FF00"}\
}, \
"video" : "" \
})

configs["episodes"].append(\
{ "title": "Fortnite Ballistic",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "padAudio" : 0.05 },\
"video" : "" \
})

configs["episodes"].append(\
{ "title": "1080p Ballistic",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : "", "chromaColor" : "0x00FF00"}\
}, \
"video" : "" \
})

configs["episodes"].append(\
{ "title": "900p Ballistic",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : "", "chromaColor" : "0x00FF00"}\
}, \
"video" : "" \
})

configs["episodes"].append(\
{ "title": "720p Ballistic",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : "", "chromaColor" : "0x00FF00"}\
}, \
"video" : "" \
})

####################### end of gaming section ###############################

####################### conclusion ###############################
# really need an upgrade
configs["episodes"].append(\
{ "title": "Time waits for no GPU",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "Normal trend",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "HD5770 vs GT 730 - not a display adapter",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "HD5770 - The gap",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "HD5770 - Maybe retro",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "bye",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})


##configs["episodes"].append(\
##{ "title": "Blooper",\
##"isChapter" : False,\
##"audio" : {"timestamps" : ( "13:40.5", "14:04.2") },\
##"video" : {"file":"HiRezTrio-P_aladins_R_ealmRoyale_R_ogueCompany.mp4"}\
##})

#scriptedvided.makeVideoForEpisode(configs["episodes"][7], configs)
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

