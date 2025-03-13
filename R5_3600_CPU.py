import scriptedvided

configs = { "defaultAudioFile" : "R5_3600_CPU_v2.ogg",\
"mediaFolder" : "F:\\Videos\\R5_3600", \
"stockFolder" : "F:\\Videos\\stock",\
"benchmarkFile" : "F:\\Videos\\R5_3600\\R5_3600_CPU.txt",\
"outputFolder" : "F:\\Videos\\R5_3600\\output", \
"outputFile" : "R5_3600_CPU.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "New and improved bottlenecks", "until" : "Marvel Rivals"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Marvel Rivals", "until" : "Video rendering test (The GigASUS)"}}, \
{"file" : "Ferco - Inquisitiveness.ogg", "timestamps" : ("01:01", None ), "destinationTimestamp" : {"title" : "Video rendering test (The GigASUS)", "until" : "Conclusions"}}, \
{"file" : "Inspired - MaikonMusic  Free Background Music  Audio Library Release.mp3", "timestamps" : ("00:00", None ), "destinationTimestamp" : {"title" : "Conclusions", "until" : "EOF"}}, \
], "volume" : 0.05 },\
"episodes" : [],\
"youtube" : {"title" : "", \
"description" : '''This video reveals the limits of the Ryzen 5 3600 CPU in some of the more popular online games.''',\
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
{ "title": "New and improved bottlenecks",\
"audio" : {"timestamps" : ("00:00", "00:15.2" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_R5_3600_6c12t.mp4"},\
})

configs["episodes"].append(\
{ "title": "The CPU",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:29.8" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "R5_3600_params_AmdCom.mkv"},\
})

configs["episodes"].append(\
{ "title": "65W TDP, if you squint a bit",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:49" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "R5_3600_TDP.mp4"},\
})

configs["episodes"].append(\
{ "title": "bundled cooler",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:59.8" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_Ryzen5_2600.MP4", "start" : "02:16"},\
})

configs["episodes"].append(\
{ "title": "better cooler",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:15.6" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_WraithPrism.MP4", "start" : "00:00"},\
})

configs["episodes"].append(\
{ "title": "The games and test system",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:33.8" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Marvel-Win64-Shipping_2025_03_09_23_32_45_673.mp4"},\
})

configs["episodes"].append(\
{ "title": "Video compression test",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:47.7" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Gigasus_ffwd10.mp4"},\
})

configs["episodes"].append(\
{ "title": "The test system",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:02.5" ), "volume" : 0.999, "padAudio" : 0.05 },\
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
{ "title": "Marvel Rivals",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:27.5" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, 30% render scale, low settings", \
    }\
}, 
})

configs["episodes"].append(\
{ "title": "Fortnite",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:42.4" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Fortnite'",\
              scriptedvided.r6sText('1280x720, performance mode' ,  227,  133),\
]}, \
"video" : "rx580_high_FortniteClient-Win64.mp4"\
})

configs["episodes"].append(\
{ "title": "Fortnite Reload results",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:55.8" ), "padAudio" : 0.05 },\
"video" : "FortniteClient-bench_reload_2024_07_01.mp4",\
"overlay" : { \
    "text" : ["'Fortnite Reload'",\
              scriptedvided.r6sText('1280x720, performance mode' ,  217,  95),\
]}, \
})

configs["episodes"].append(\
{ "title": "Counter-Strike 2",\
"audio" : {"timestamps" : ("08:43.8", "09:09.1" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
},
})

configs["episodes"].append(\
{ "title": "Delta Force",\
"audio" : {"timestamps" : ( "02:55.8", "03:24.1" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Delta Force'",\
              "'Nice to know you, good bye'",\
]}, \
"video" : "DeltaForce_loadingResources.mp4",\
})

configs["episodes"].append(\
{ "title": "Apex Legends",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:49.2" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
},
"video" : "rx580_r5apex_2024_07_26_22_34_08_382-converted.mp4" \
})

configs["episodes"].append(\
{ "title": "Overwatch 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:07.6" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, 50% render scale, low settings", \
    }\
}
})

configs["episodes"].append(\
{ "title": "The Finals",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:31.5" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
},\
"video" : "rx580_Discovery_2024_07_26_23_03_56_417-converted.mp4" \
})

configs["episodes"].append(\
{ "title": "Rainbow Six: Siege",\
"audio" : {"timestamps" : ("08:16.6", "08:40.4" ), "padAudio" : 0.05 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, 50% render scale, low settings", \
    }\
},
})

####################### end of gaming section ###############################


############################ productivity #################################

configs["episodes"].append(\
{ "title": "Video rendering test (The GigASUS)",\
"audio" : {"timestamps" : ( "04:56.1", "05:08.7" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "blurred_gigasus.mp4"},\
"overlay" : { \
    "image" : {"file" : "overlays_r5_3600_multiCore.png", "chromaColor" : "0x00FF00"}\
}, \
})

configs["episodes"].append(\
{ "title": "Assigning a number to IPC",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:16.2" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_R5_3600_6c12t.mp4"},\
})

configs["episodes"].append(\
{ "title": "Performance onion",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:30.4" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Breel_R5-3600_InMobo9.MP4"},\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Single core",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:42" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "r5_3600_blurred.mp4"},\
"isChapter" : False,\
"overlay" : { \
    "image" : {"file" : "overlays_r5_3600_singleCore.png", "chromaColor" : "0x00FF00"}\
}, \
})

configs["episodes"].append(\
{ "title": "Clock cycles",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:58.5" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "blurred_gigasus.mp4"},\
"isChapter" : False,\
"overlay" : { \
    "image" : {"file" : "overlays_r5_3600_cycles.png", "chromaColor" : "0x00FF00"}\
}, \
})

configs["episodes"].append(\
{ "title": "SMT - what is it good for",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:08.2" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Breel_R5-3600_InMobo9.MP4"},\
})

configs["episodes"].append(\
{ "title": "SMT on compared to SMT off",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:28.2" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "blurred_gigasus.mp4"},\
"isChapter" : False,\
"overlay" : { \
    "image" : {"file" : "overlays_r5_3600_cyclesSmtOff.png", "chromaColor" : "0x00FF00"}\
}, \
})

configs["episodes"].append(\
{ "title": "and power",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:43.4" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "r5_3600_blurred.mp4"},\
"isChapter" : False,\
"overlay" : { \
    "image" : {"file" : "SMT.png", "chromaColor" : "0x00FF00"}\
},\
})

configs["episodes"].append(\
{ "title": "Cache size ... nope",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:57.6" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_Ryzen5_2600.MP4", "start" : "00:16"},\
"isChapter" : False,\
})

#############################################################################



####################### conclusion ###############################
# really need an upgrade
configs["episodes"].append(\
{ "title": "Conclusions",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:12.52" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "r5_3600_concat_breels.mp4"},\
})

configs["episodes"].append(\
{ "title": "motherboard - stretching for the TDP",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:24.5" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-A320M-H_Overview.MP4"},\
})

configs["episodes"].append(\
{ "title": "coolers not really suited for 85W",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:41.9" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_Ryzen5_2600.MP4", "start" : "03:57"},\
})

configs["episodes"].append(\
{ "title": "pricing",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:55.6" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Ryzen5_3600_olx.mkv"},\
})

configs["episodes"].append(\
{ "title": "other CPUs on the way",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:06.3" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "system_AMD_vs_Intel.mp4"},\
})

configs["episodes"].append(\
{ "title": "bye",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:16.4" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_R5_3600_6c12t.mp4"},\
})


##configs["episodes"].append(\
##{ "title": "Blooper",\
##"isChapter" : False,\
##"audio" : {"timestamps" : ( "13:40.5", "14:04.2") },\
##"video" : {"file":"HiRezTrio-P_aladins_R_ealmRoyale_R_ogueCompany.mp4"}\
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

