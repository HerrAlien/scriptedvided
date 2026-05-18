import scriptedvided
import sv_ffutils

configs = { "defaultAudioFile" : "R9_380.ogg",\
"mediaFolder" : "F:\\Videos\\R9_380", \
"stockFolder" : "F:\\Videos\\stock",\
"benchmarkFile" : "F:\\Videos\\R9_380\\Benchmark_R9_380.txt",\
"outputFolder" : "F:\\Videos\\R9_380\\output", \
"outputFile" : "R9_380.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "Peak Rebrandeon", "until" : "Games that will not run"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Games that will not run", "until" : "Counter-Strike 2"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Counter-Strike 2", "until" : "Conclusions"}}, \
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
#  \"video\" : \{\"file\" : \" \"\}
#  scriptedvided.r6sText\('.*' *\, *[0-9]*\, *[0-9]*\)
#   "timestamps" *\: *\( *"[0-9\:\.]*" *\, *"[0-9\:\.]*" *\)
#configs["episodes"].append(\
#{ "title": "A favorite of miners and gamers alike",\
#"audio" : {"timestamps" : (scriptedvided.nextTS(configs),  "" ), "volume" : 0.999, "padAudio" : 0.05 },\
#"video" : {"file" : ""},\
# scriptedvided.nextTS\(configs\)\, \"[0-9,:,\.]*\"
# scriptedvided.r6sText\( *'.*' *\, *[0-9]* *\, *[0-9]* *\)
#})

configs["episodes"].append(\
{ "title": "Peak Rebrandeon",\
"audio" : {"timestamps" : ("00:00", "00:12.7"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_R9_380_onGrass_barred.mp4"},\
})

configs["episodes"].append(\
{ "title": "Remember the 370",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:24.8" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_R7_365_R9_370_barred.mp4"},\
"isChapter" : False,\
})

# GPU-Z
configs["episodes"].append(\
{ "title": "The GPU",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:36.5" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "R9_380_GPUZ.mkv"},\
})

configs["episodes"].append(\
{ "title": "Comparisons, shaders, frequency",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:59.7" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GPUZ_R9_380_280.mp4"},\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Cooling and thermals",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:13" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_r9_380_coolingDetails_barred.mp4"},\
})

configs["episodes"].append(\
{ "title": "Finstack",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:20.4" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_R9_380_onGrass_barred.mp4"},\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "2 fans and temperatures",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:32.1" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "R9_380_weight_barred.mp4", "start" : "00:00"},\
"overlay" : { "text" : ["'Temperatures (Valley)\: 74C (51C delta over ambient)'"] },\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "The test system",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:43.4" ), "volume" : 0.999, "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Custom PC'",\
              "'CPU\: Ryzen 5 5600'",\
              "'RAM\: 32GB DDR4, 3600MHz, dual channel'",\
              "'GPU\: Radeon R9 370 1024'",\
    ]\
}, \
"video" : {"file" : "test_system_RX580.mp4" }\
})


####################### end of intro ###############################


####################### gaming section ###############################
# needs redone

episodes = configs["episodes"]

configs["episodes"].append(\
{ "title": "Games that will not run",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:57.6" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "R9_380_MarvelRivalsError.mkv"},\
})

configs["episodes"].append(\
{ "title": "Cyberpunk 2077",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:19" ), "padAudio" : 0.05 },\
"overlay" : {"benchmark" : {"settings" : "1920x1080, low settings", } }, \
"video" : {"file" : "Cyberpunk2077_2025_04_06_22_49_01_575-converted.mp4", "start" : "00:00"},\
})

configs["episodes"].append(\
{ "title": "Cyberpunk 2077 both",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:26" ), "padAudio" : 0.05 },\
"overlay" : { "image" : {"file" : "Cyberpunk 2077.png"} }, \
"isChapter" : False,\
"video" : {"file" : "Cyberpunk2077_2025_04_06_22_49_01_575-converted.mp4", "start" : "00:30"},\
})

scriptedvided.addEpisodeWithTextOverlay(episodes,\
{ "title": "ARC Raiders",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:45.7" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : [sv_ffutils.ffmpegSafeString("Low Settings"),\
              scriptedvided.r6sText( '1920x1080' , 53, 46),\
              scriptedvided.r6sText( '1600x900' , 61, 50),\
              scriptedvided.r6sText( '1280x720' , 73, 58),\
]}, \
"video" : {"file" : "PioneerGame_DOWNINGsNITCH.mp4" , "start" : "00:54" },\
})

configs["episodes"].append(\
{ "title": "ARC both",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:58" ), "padAudio" : 0.05 },\
"overlay" : { "image" : {"file" : "ARC Raiders.png"} }, \
"video" : {"file" : "PioneerGame_DOWNINGsNITCH.mp4" , "start" : "04:40" },\
"isChapter" : False,\
})

scriptedvided.addEpisodeWithTextOverlay(episodes,\
{ "title": "Fortnite",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:24" ), "padAudio" : 0.05 },\
"video" : {"file" : "FortniteClient-Win64-Shipping_2026_05_17_20_11_42_186.mp4" , "start":"02:50"},\
"overlay" : { \
    "text" : [sv_ffutils.ffmpegSafeString("Legacy Performance Mode, FAR rendering distance"),\
              scriptedvided.r6sText( '1920x1080' , 74 , 24),\
              scriptedvided.r6sText(  '1600x900' , 84 , 63),\
              scriptedvided.r6sText(  '1280x720' , 89 , 67),\
]}, \
})

configs["episodes"].append(\
{ "title": "Fortnite both",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:37.3" ), "padAudio" : 0.05 },\
"overlay" : { "image" : {"file" : "Fortnite.png"} }, \
"video" : {"file" : "FortniteClient-Win64-Shipping_2026_05_17_20_11_42_186.mp4" , "start":"03:10"},\
"isChapter" : False,\
})


# single resolution
scriptedvided.addEpisodeWithTextOverlay(episodes,\
{ "title": "Control",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:55.2" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : [sv_ffutils.ffmpegSafeString("Low Settings"),\
              scriptedvided.r6sText( '1920x1080' ,  54, 36),\
              scriptedvided.r6sText(  '1280x720' , 86 , 49),\
]}, \
"video" : {"file" : "stock_Control_R9_270.mp4", "start" : "02:00"},\
})

configs["episodes"].append(\
{ "title": "Control both",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:01.9" ), "padAudio" : 0.05 },\
"overlay" : { "image" : {"file" : "Control.png"} }, \
"isChapter" : False,\
"video" : {"file" : "rx580_Control_DX11_2024_07_27_22_47_25_351-converted.mp4"},\
})

configs["episodes"].append(\
{ "title": "Doom Eternal, with some issues",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:06.3" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "4_stages_of_strobing.mp4"},\
})

configs["episodes"].append(\
{ "title": "Doom Eternal",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:24.3" ), "volume" : 0.999, "padAudio" : 0.05 },\
"overlay" : {"benchmark" : {"settings" : "1920x1080, high settings", } }, \
"video" : {"file" : "stock_DOOMEternal_2023_12_26.mp4"},\
"isChapter" : False,\
})

scriptedvided.addEpisodeWithTextOverlay(episodes,\
{ "title": "Apex Legends",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:45.8" ), "volume" : 0.999, "padAudio" : 0.05 },\
"overlay" : { \
    "text" : [sv_ffutils.ffmpegSafeString("Low Settings"),\
              scriptedvided.r6sText( '1920x1080' , 95 , 72),\
              scriptedvided.r6sText(  '1600x900'  , 114 , 83),\
              scriptedvided.r6sText(  '1280x720'  , 135 , 94),\
]}, \
})

scriptedvided.addEpisodeWithTextOverlay(episodes,\
{ "title": "FC6",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:04.2" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : [scriptedvided.r6sText( '1920x1080 ultra settings' ,  34, 30),\
              scriptedvided.r6sText( '1920x1080 high settings' ,  42, 37),\
]}, \
"video" : {"file" : "FarCry6Trial_high.mp4"},\
})

configs["episodes"].append(\
{ "title": "FC6 both",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:18.8" ), "padAudio" : 0.05 },\
"overlay" : { "image" : {"file" : "Far Cry 6.png"} }, \
"isChapter" : False,\
"video" : {"file" : "FarCry6Trial_high.mp4"},\
})


# single resolution
configs["episodes"].append(\
{ "title": "RE4",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:32.8" ), "padAudio" : 0.05 },\
"overlay" : {"benchmark" : {"settings" : "1920x1080, prioritize performance, no FSR", } }, \
"video" : {"file" : "stock_re4demo_phoneCall.mp4"},\
})

configs["episodes"].append(\
{ "title": "re4 both",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:43.1" ), "padAudio" : 0.05 },\
"overlay" : { "image" : {"file" : "Resident Evil 4.png"} }, \
"isChapter" : False,\
"video" : {"file" : "rx570_re4demo_balanced.mp4"},\
})

configs["episodes"].append(\
{ "title": "Counter-Strike 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:57" ), "padAudio" : 0.05 },\
"overlay" : {"benchmark" : {"settings" : "1920x1080, medium settings, no FSR", } }, \
})


# bad overlay, this is at 720 ...
configs["episodes"].append(\
{ "title": "CS2 both",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:09.8" ), "padAudio" : 0.05 },\
"overlay" : { "image" : {"file" : "Counter-Strike 2.png"} }, \
"isChapter" : False,\
"video" : {"file" : "stock_CS2_CT_R7_260X.mp4"},\
})

configs["episodes"].append(\
{ "title": "Borderlands 3",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:23.2" ), "padAudio" : 0.05 },\
"overlay" : {"benchmark" : {"settings" : "1920x1080, medium settings", } }, \

})

configs["episodes"].append(\
{ "title": "bl3 both",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:30.5" ), "padAudio" : 0.05 },\
"overlay" : { "image" : {"file" : "Borderlands 3.png"} }, \
"isChapter" : False,\
"video" : {"file" : "Borderlands3_2024_05_03_22_37_22_347.mp4", "start" : "07:00"},\
})


# single resolution
configs["episodes"].append(\
{ "title": "DOTA 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:44.6" ), "padAudio" : 0.05 },\
"video" : "stock_dota2_1080pLow_scale100.mp4",\
"overlay" : {"benchmark" : {"settings" : "1920x1080, low settings", } }, \
})


scriptedvided.addEpisodeWithTextOverlay(episodes,\
{ "title": "The Finals",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:04.5" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : [sv_ffutils.ffmpegSafeString("Low Settings"),\
              scriptedvided.r6sText( '1920x1080' , 55, 42),\
              scriptedvided.r6sText(  '1600x900'  , 67, 52),\
              scriptedvided.r6sText(  '1280x720'  , 81, 60),\
]}, \
})

configs["episodes"].append(\
{ "title": "Finals both",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:13.6" ), "padAudio" : 0.05 },\
"overlay" : { "image" : {"file" : "The Finals.png"} }, \
"isChapter" : False,\
"video" : {"file" : "Discovery_2025_03_15_22_55_07_819.mp4"},\
})


#redo and specify a smoother video
configs["episodes"].append(\
{ "title": "Shadow of the Tomb Raider",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:29.5" ), "padAudio" : 0.05 },\
"overlay" : {"benchmark" : {"settings" : "1920x1080, highest settings", } }, \
})

configs["episodes"].append(\
{ "title": "sottr both",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:43.8" ), "padAudio" : 0.05 },\
"overlay" : { "image" : {"file" : "Shadow of the Tomb Raider.png"} }, \
"isChapter" : False,\
"video" : {"file" : "SOTTR_gaming_highest.mp4", "start" : "04:45"},\
})


configs["episodes"].append(\
{ "title": "Terminator",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:57.8" ), "padAudio" : 0.05 },\
"overlay" : {"benchmark" : {"settings" : "1920x1080, epic settings", } }, \
})

####################### end of gaming section ###############################


####################### conclusion ###############################
# repairs, reuse
configs["episodes"].append(\
{ "title": "Conclusions",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:10.4" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_R9_380_inHand_barred.mp4"},\
})

configs["episodes"].append(\
{ "title": "380 is faster sum all FPS",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:18.3" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_r9_380_r9_280_barred.mp4"},\
})

configs["episodes"].append(\
{ "title": "380 is faster sum all FPS too",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:25.5" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_r9_380_r9_280_barred.mp4"},\
"overlay" : { "image" : {"file" : "SUM of all FPS.png"} }, \
})

configs["episodes"].append(\
{ "title": "300 series vs maxwell",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:38" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_R9_380_inHand_barred.mp4"},\
})

configs["episodes"].append(\
{ "title": "price",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:47.8" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "R9_380_OLX.mkv"},\
})

configs["episodes"].append(\
{ "title": "price too close to Polaris",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:59.1" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "OLX_R9_380_RX_570.mkv"},\
})

configs["episodes"].append(\
{ "title": "gtx 980",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "09:05.3" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_GTX980_barred.mp4"},\
})

configs["episodes"].append(\
{ "title": "bye",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "09:12.4" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_R9_380_inHand_barred.mp4"},\
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

