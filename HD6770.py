import scriptedvided

configs = { "defaultAudioFile" : "HD6770.ogg",\
"mediaFolder" : "F:\\Videos\\HD6770", \
"stockFolder" : "F:\\Videos\\stock",\
"benchmarkFile" : "NA",\
"outputFolder" : "F:\\Videos\\HD6770\\output", \
"outputFile" : "HD6770.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "An odd looking card", "until" : "A bit hot for Heaven"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "A bit hot for Heaven", "until" : "So, what did I do wrong?"}}, \
{"file" : "Inspired - MaikonMusic  Free Background Music  Audio Library Release.mp3", "timestamps" : ("00:00", None ), "destinationTimestamp" : {"title" : "So, what did I do wrong?", "until" : "EOF"}}, \
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
{ "title": "An odd looking card",\
"audio" : {"timestamps" : ("00:00", "00:06.3" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "HD6770_breel.mp4"},\
})

configs["episodes"].append(\
{ "title": "An odd looking card 2",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:23" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Juniper_HD6770_HD5770.mp4"},\
})


configs["episodes"].append(\
{ "title": "Same GPU",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:36.4" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "HD6770_GPUZ.mp4"},\
})

configs["episodes"].append(\
{ "title": "Same PCB even",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:57" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "HD6770_HD5770_samePCB.mp4"},\
})

configs["episodes"].append(\
{ "title": "The test system",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:16" ), "volume" : 0.999, "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Cheap PC for testing GPUs after repairs'",\
              "'CPU\: AMD A4-6400 APU'",\
              "'RAM\: 4GB DDR3 at 1600 MHz, single channel'",\
    ]\
}, \
"video" : {"file" : "HD6770_testSetup.mp4"}\
})

####################### end of intro ###############################




####################### gaming section ###############################
# should start from "And as you can see on screen"
configs["episodes"].append(\
{ "title": "A bit hot for Heaven",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:45.2" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Heaven benchmark'",\
              "'Temperature\: 72C, delta over ambient\: 48C'" \
]}, \
"video" : "HD6770_73C_rising.mp4",\
})

configs["episodes"].append(\
{ "title": "But does it have the fan driver?",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:56" ), "padAudio" : 0.05 },\
"video" : "HD6770_probingForFanPWM.mp4",\
})

configs["episodes"].append(\
{ "title": "This is not Heaven!",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:07" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Heaven benchmark'",\
              "'Temperature\: 92C, delta over ambient\: 68C'" \
]}, \
"video" : "HD6770_90C.mp4" \
})

configs["episodes"].append(\
{ "title": "Too hot for my taste",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:20" ), "padAudio" : 0.05 },\
"video" : "breel_juniper_2_HD6770_HD5770.mp4",\
})

configs["episodes"].append(\
{ "title": "So, what did I do wrong?",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:35" ), "padAudio" : 0.05 },\
"video" : "natural_airflow.mp4",\
})


configs["episodes"].append(\
{ "title": "side by side 90C and the setup",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:47" ), "padAudio" : 0.05 },\
"video" : "not_how_I_run_gpus.mp4",\
})


configs["episodes"].append(\
{ "title": "better designs",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:03.6" ), "padAudio" : 0.05 },\
"video" : "Juniper_HD6770_HD5770.mp4",\
})

configs["episodes"].append(\
{ "title": "preserve it",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:14.9" ), "padAudio" : 0.05 },\
"video" : "breel_juniper_2_HD6770_HD5770.mp4",\
})

configs["episodes"].append(\
{ "title": "bye",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:21.4" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "HD6770_breel.mp4"},\
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

