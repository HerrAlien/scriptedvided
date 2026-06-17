import scriptedvided
import sv_ffutils

configs = { "defaultAudioFile" : "GTX980.ogg",\
"mediaFolder" : "F:\\Videos\\GTX980", \
"stockFolder" : "F:\\Videos\\stock",\
"benchmarkFile" : "F:\\Videos\\GTX980\\Benchmark_GTX_980.txt",\
"outputFolder" : "F:\\Videos\\GTX980\\output", \
"outputFile" : "GTX980.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#00800080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "Back to Maxwell", "until" : "Marvel Rivals"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Marvel Rivals", "until" : "RE4"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "RE4", "until" : "Conclusions"}}, \
{"file" : "Inspired - MaikonMusic  Free Background Music  Audio Library Release.mp3", "timestamps" : ("00:00", None ), "destinationTimestamp" : {"title" : "Conclusions", "until" : "EOF"}}, \
], "volume" : 0.046 },\
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
"tags" : "NVidia,GeForce,GTX,Maxwell,980,GTX980,GTX 980",\
"language" : "EN", \
"Caption certification" : "None",\
"recording date" : None,\
"video location" : None, \
"category" : "Gaming", \
"subtitles" : None, \
"endscreen" : None, \
"cards" : None, \
},\
}

#"isChapter" : False, \

####################### intro ###############################

# this is the hook 
#  scriptedvided.nextTS\(configs\)\, *\"[0-9][0-9]\:[0-9][0-9]\.?[0-9]?[0-9]?\"
#  \"file\" *\: *\".*\"
#  \"video\" *: *\{\"file\" *: *\".* \"\}
#  scriptedvided.r6sText\('.*' *\, *[0-9]*\, *[0-9]*\)
#   "timestamps" *\: *\( *"[0-9\:\.]*" *\, *"[0-9\:\.]*" *\)
#configs["episodes"].append(\
#{ "title": "A favorite of miners and gamers alike",\
#"audio" : {"timestamps" : (scriptedvided.nextTS(configs),  "" ), "volume" : 0.999, "padAudio" : 0.05 },\
#"video" : {"file" : ""},\
#})

configs["episodes"].append( { "title": "Back to Maxwell",\
"audio" : {"timestamps" : ("00:00", "00:12.5"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_GTX980_barred.mp4"},\
})

#Maybe have an overlay?
configs["episodes"].append( { "title": "Arc Raiders preview",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:27.7" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "PioneerGame_2026_02_21_BurriedCity.mp4", "start" : "02:47"},\
"overlay" : { \
    "text" : [scriptedvided.r6sText("1920x1080, low settings", 72, 49),\
              scriptedvided.r6sText("1600x900, low settings", 87, 57),\
              scriptedvided.r6sText("1280x720, low settings", 97, 58),\
]}, \
})

# focus on PCIE lanes
configs["episodes"].append( { "title": "The GPU",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:43" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GTX980_GPUZ.mkv"},\
})

# focus on PCIE lanes
configs["episodes"].append( { "title": "TDP and Overwatch",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:52" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "stock_Overwatch2_training.mp4"},\
})

# focus on PCIE lanes
configs["episodes"].append( { "title": "Cooling and Thermals",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:58.4" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GTX980_cooling2_barred.mp4", "start" : "00:00"},\
})

configs["episodes"].append( { "title": "Chunky cooler",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:04.7" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_GTX980_RX580_coolerWeights_barred.mp4", "start" : "00:11"},\
})

# need to redo this one, had bad values
configs["episodes"].append( { "title": "No RAM cooling",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:18" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GTX980_cooling1_barred.mp4", "start" : "00:00"},\
"overlay" : { \
    "text" : ["'Temperatures (Valley)\: 75C (52C delta over ambient)'"]}, \
})

configs["episodes"].append( { "title": "The test system",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:26.9" ), "volume" : 0.999, "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Custom PC'",\
              "'CPU\: Ryzen 5 5600'",\
              "'RAM\: 32GB DDR4, 3600MHz, dual channel'",\
              "'GPU\: GTX 980'",\
    ]\
}, \
"video" : {"file" : "test_system_RX580.mp4" }\
})

####################### end of intro ###############################


####################### gaming section ###############################

episodes = configs["episodes"]

scriptedvided.addEpisodeWithTextOverlay(episodes, { "title": "Marvel Rivals",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:49.5" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : [scriptedvided.r6sText("1920x1080, low settings", 61, 51),\
              scriptedvided.r6sText("1280x720, low settings" , 104, 86),\
]}, \
})

# needs redone
scriptedvided.addEpisodeWithTextOverlay(episodes, { "title": "Cyberpunk 2077",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:13.5" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : [scriptedvided.r6sText("1920x1080, low settings, no FSR", 47 , 33 ),\
              scriptedvided.r6sText("1600x900, medium settings, no FSR", 48, 35),\
              scriptedvided.r6sText("1280x720, high settings, no FSR", 48, 35),\
]}, \
})

scriptedvided.addEpisodeWithTextOverlay(episodes, { "title": "ARC Raiders",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:37" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : [scriptedvided.r6sText("1920x1080, low settings", 72, 49),\
              scriptedvided.r6sText("1600x900, low settings", 87, 57),\
              scriptedvided.r6sText("1280x720, low settings", 97, 58),\
]}, \
"video" : {"file" : "PioneerGame_2026_02_21_BurriedCity.mp4", "start" : "02:47"},\
})

scriptedvided.addEpisodeWithTextOverlay(episodes, { "title": "Fortnite",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:59.8" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : [sv_ffutils.ffmpegSafeString("DX12 mode, medium settings"),\
              scriptedvided.r6sText("1920x1080", 108, 81),\
              scriptedvided.r6sText("1600x900" , 132, 95),\
              scriptedvided.r6sText("1280x720" , 163, 117),\
]}, \
"video" : {"file" : "FortniteClient-Win64-Shipping_2026_06_01_18_13_44_994.mkv"},\
})

configs["episodes"].append( { "title": "Fortnite perf vs high",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:09" ), "padAudio" : 0.05 },\
"isChapter" : False,\
"video" : {"file" : "FNiteDX12VsPerformance.mp4", "start" : "00:05"},\
})

scriptedvided.addEpisodeWithTextOverlay(episodes, { "title": "Control",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:30.8" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : [scriptedvided.r6sText("1920x1080, high settings"  , 44, 37),\
              scriptedvided.r6sText("1920x1080, medium settings", 59, 50),\
]}, \
})

scriptedvided.addEpisodeWithTextOverlay(episodes, { "title": "Rainbow Six: Siege",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:56"), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : [scriptedvided.r6sText("1920x1080, high settings", 114, 78),\
              scriptedvided.r6sText("1920x1080, low settings", 114, 78),\
              scriptedvided.r6sText("1920x1080, low settings, 50% render scale", 156, 117),\
]}, \
})

# single resolution
scriptedvided.addEpisodeWithTextOverlay(episodes, { "title": "Apex Legends",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:25.5" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : [sv_ffutils.ffmpegSafeString("Low settings"),\
              scriptedvided.r6sText("1920x1080", 179, 131),\
              scriptedvided.r6sText("1600x900" , 218, 150),\
              scriptedvided.r6sText("1280x720", 255, 176),\
]}, \
})

scriptedvided.addEpisodeWithTextOverlay(episodes, { "title": "Far Cry 6",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:41" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : [scriptedvided.r6sText("1920x1080, high settings", 58, 47),\
              scriptedvided.r6sText("1920x1080, ultra settings", 48, 40 ),\
]}, \
})

scriptedvided.addEpisodeWithTextOverlay(episodes, { "title": "Overwatch 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:14.6" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : [sv_ffutils.ffmpegSafeString("Low settings"),\
              scriptedvided.r6sText("1920x1080", 333, 242),\
              scriptedvided.r6sText("1600x900" , 437, 307),\
              scriptedvided.r6sText("1280x720" , 589, 460),\
]}, \
})

scriptedvided.addEpisodeWithTextOverlay(episodes, { "title": "RE4",\
"audio" : {"timestamps" : ("05:19.6", "05:45.9" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : [scriptedvided.r6sText("1920x1080, performance preset, no FSR", 66, 51),\
              scriptedvided.r6sText("1920x1080, balanced preset, no FSR"   , 51, 33),\
]}, \
})

configs["episodes"].append( { "title": "Counter-Strike 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:09" ), "padAudio" : 0.05 },\
"overlay" : {"benchmark" : {"settings" : "1920x1080, medium settings, no FSR", } }, \
})

scriptedvided.addEpisodeWithTextOverlay(episodes, { "title": "Borderlands 3",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:31" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : [scriptedvided.r6sText("1920x1080, high settings"  , 55, 44),\
              scriptedvided.r6sText("1920x1080, badass settings", 43, 35),\
]}, \
})

configs["episodes"].append(  { "title": "DOTA 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:46.9" ), "padAudio" : 0.05 },\
"overlay" : {"benchmark" : {"settings" : "1920x1080, highest settings" } }, \
"video" : "stock_dota2_1080pLow_scale100.mp4"\
})

scriptedvided.addEpisodeWithTextOverlay(episodes, { "title": "Robocop",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:11.2" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : [scriptedvided.r6sText("1920x1080, medium settings", 32, 25),\
              scriptedvided.r6sText("1920x1080, low settings"   , 35, 29),\
]}, \
})

configs["episodes"].append(  { "title": "The Finals",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:26.3" ), "padAudio" : 0.05 },\
"overlay" : {"benchmark" : {"settings" : "1920x1080, low settings" } }, \
"video" : {"file" : "Discovery_2025_03_15_22_55_07_819.mp4"},\
})

#redo and specify a smoother video
configs["episodes"].append( { "title": "Shadow of the Tomb Raider",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:41.1" ), "padAudio" : 0.05 },\
"overlay" : {"benchmark" : {"settings" : "1920x1080, highest settings" } }, \
})

#redo and specify a smoother video
configs["episodes"].append(  { "title" : "Terminator", \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:59" ), "padAudio" : 0.05 },\
"overlay" : {"benchmark" : {"settings" : "1920x1080, epic settings" } },\
"video" : {"file" : "Terminator-Win64-Shipping_2024_07_20_23_51_41_842-converted.mp4", "start" : "35:02"}} )

####################### end of gaming section ###############################


####################### conclusion ###############################
# like Maxwell
configs["episodes"].append(\
{ "title": "Conclusions",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:05.7" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_GTX980_inHands2_barred.mp4"},\
})

configs["episodes"].append(\
{ "title": "side by side with the RX 580",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:26.5" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_gtx980_rx580_barred.mp4"},\
})

configs["episodes"].append(\
{ "title": "ASUS cooler weight",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:32.3" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_GTX980_RX580_coolerWeights_barred.mp4", "start" : "00:07"},\
})

configs["episodes"].append(\
{ "title": "Gigabyte cooler weight",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:38.7" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_GTX980_RX580_coolerWeights_barred.mp4", "start" : "00:37"},\
})

configs["episodes"].append(\
{ "title": "Ripped off mem chip",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:49.6" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_RX580_rippedMem_barred.mp4"},\
})

configs["episodes"].append(\
{ "title": "Gigabyte touches RAM compared to ASUS",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:59.8" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "coolers_VRAM_gtx980_rx580.mp4"},\
"overlay" : { "image" : {"file" : "overlay_coolers.png"} }, \
})

configs["episodes"].append(\
{ "title": "ASUS does not care about lifespan",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "09:08.4" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_GTX980_barred.mp4"},\
})

configs["episodes"].append(\
{ "title": "OLX",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "09:27.2" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "gtx980_olx.mkv"},\
})

configs["episodes"].append(\
{ "title": "Maxwell vs Pascal",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "09:33.8" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_GTX980_inHands2_barred.mp4"},\
})

configs["episodes"].append(\
{ "title": "1060 preview",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "09:43.1" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_GTX1060_inHand_barred.mp4"},\
})

configs["episodes"].append(\
{ "title": "bye",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "09:49.7" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_GTX980_barred.mp4"},\
})


##configs["episodes"].append(\
##{ "title": "Blooper",\
##"isChapter" : False,\
##"audio" : {"timestamps" : (scriptedvided.nextTS(configs),  "" ) },\
##"video" : {"file" : ""},\
##})

#scriptedvided.makeVideoForEpisode(configs["episodes"][8], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][9], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][13], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][15], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][16], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][17], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][18], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][19], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][20], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][22], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][24], configs)
#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "Marvel Rivals"][0], configs)
#scriptedvided.makeVideo(configs)

#for x in range(19,26):
#    scriptedvided.makeVideoForEpisode(configs["episodes"][x], configs)
#
scriptedvided.makeVideo(configs)

