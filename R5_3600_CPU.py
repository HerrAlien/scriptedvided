import scriptedvided
import sv_ffutils

configs = { "defaultAudioFile" : ".ogg",\
"mediaFolder" : "F:\\Videos\\", \
"stockFolder" : "F:\\Videos\\stock",\
"benchmarkFile" : "",\
"outputFolder" : "F:\\Videos\\\\output", \
"outputFile" : "R5_3600_CPU.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "", "until" : ""}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "", "until" : ""}}, \
{"file" : "Ferco - Lake Of The Honesty.ogg", "timestamps" : ("00:30", None ), "destinationTimestamp" : {"title" : "", "until" : ""}}, \
{"file" : "Ferco - Inquisitiveness.ogg", "timestamps" : ("01:01", None ), "destinationTimestamp" : {"title" : "", "until" : ""}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "", "until" : ""}}, \
{"file" : "Inspired - MaikonMusic  Free Background Music  Audio Library Release.mp3", "timestamps" : ("00:00", None ), "destinationTimestamp" : {"title" : "", "until" : "EOF"}}, \
], "volume" : 0.05 },\
"episodes" : [],\
"youtube" : {"title" : "", \
"description" : ''' ''',\
"links" : '''
Track: Bliss Of Heaven - SOMM [Audio Library Release]
Music provided by Audio Library Plus
Watch: https://www.youtube.com/watch?v=JQ6mKeQLZak&t=0s
Free Download / Stream: https://alplus.io/blisss-heaven

Track: Far Far Away - Ferco [Audio Library Release]
Music provided by Audio Library Plus
Watch: https://www.youtube.com/watch?v=SrkQ3K1umlc&t=0s 
Free Download / Stream: https://alplus.io/far-far-away

Ferco - Lake Of The Honesty
Creative Commons - Attribution 3.0 Unported (CC BY 3.0)
Free Download: hypeddit.com/lo55nr
Video: https://www.youtube.com/watch?v=LMQEm8PVnpc&t=0s

Ferco - Inquisitiveness
Creative Commons - Attribution 3.0 Unported (CC BY 3.0)
Free Download: https://hypeddit.com/mlsvxq
Streams: https://share.amuse.io/track/ferco-inquisitiveness
Video: https://www.youtube.com/watch?v=dhJdmwLWtFM&t=0s

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
#"isChapter" : False,\
#})

configs["episodes"].append(\
{ "title": "A much needed upgrade",\
"audio" : {"timestamps" : ("00:00", "00:15.2" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "The CPU",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:29.8" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "The TDP",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:49.1" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
"isChapter" : False,\
})

# this might be split
configs["episodes"].append(\
{ "title": "The bundled cooler",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:15.6" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "The test setup",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:33.9" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "Multimedia test",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:47.7" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Test system",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:02.5" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
"overlay" : { \
    "text" : ["'Custom build'",\
              "'RAM\: 32GB DDR4 at 3000 MHz, dual channel'",\
              "'GPUs\: XFX Radeon RX 580, Sapphire Radeon R9 290X'",\
    ]\
}, \
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Marvel Rivals",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:27.5" ), "volume" : 0.999, "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings, 30% render scale", \
    }\
}, \
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "Fortnite",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:42.4" ), "volume" : 0.999, "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
}, \
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "Fortnite Reload",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:55.9" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
}, \
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Delta Force is out",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:24" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "Apex Legends",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:49.3" ), "volume" : 0.999, "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
}, \
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "Overwatch 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:07.6" ), "volume" : 0.999, "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings, 50% render scale", \
    }\
}, \
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "The Finals",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:31.6" ), "volume" : 0.999, "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
}, \
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "Rainbow Six: Siege",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:56.2" ), "volume" : 0.999, "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings, 50% render scale", \
    }\
}, \
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "The video compression test",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:08.7" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "real world performance",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:16.2" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Performance onion",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:30.4" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "single core",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:42" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "clock cycles",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:58.5" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "can gauge IPC",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:08.2" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "SMT off",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:28.2" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "SMT - good performance gain",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:43.4" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "teasing cache",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:57.6" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Conclusion",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:24.5" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "Not cool",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:41.9" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Pricing",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:55.6" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "More CPUs",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:06.2" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Bye",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:13" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
"isChapter" : False,\
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
