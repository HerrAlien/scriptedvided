import scriptedvided
import sv_ffutils

configs = { "defaultAudioFile" : "gtx1060.ogg",\
"mediaFolder" : "F:\\Videos\\GTX1060", \
"stockFolder" : "F:\\Videos\\stock",\
"benchmarkFile" : "F:\\Videos\\GTX1060\\Benchmark_GTX_1060.txt",\
"outputFolder" : "F:\\Videos\\GTX1060\\output", \
"outputFile" : "GTX1060.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#00800080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "Steam Hardware Survey Champion", "until" : "Marvel Rivals"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Marvel Rivals", "until" : "Overwatch 2"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Overwatch 2", "until" : "Conclusions"}}, \
{"file" : "Inspired - MaikonMusic  Free Background Music  Audio Library Release.mp3", "timestamps" : ("00:00", None ), "destinationTimestamp" : {"title" : "Conclusions", "until" : "OLX"}}, \
{"file" : "Inspired - MaikonMusic  Free Background Music  Audio Library Release.mp3", "timestamps" : ("00:10", None ), "destinationTimestamp" : {"title" : "OLX", "until" : "EOF"}}, \
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
"tags" : "NVidia,GeForce,GTX,Pascal,1060,GTX1060,GTX 1060,1060 6G,GTX1060 6G,GTX 1060 6G",\
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

configs["episodes"].append( { "title": "Steam Hardware Survey Champion",\
"audio" : {"timestamps" : ("00:00", "00:16.1"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_GTX1060_inGrass.MP4"},\
})
# fixed in february

#Maybe have an overlay?
configs["episodes"].append( { "title": "Arc Raiders preview",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:28.1" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "PioneerGame_gotBackSafe2.mp4", "start" : "10:22"},\
"overlay" : { \
    "text" : [sv_ffutils.ffmpegSafeString("low settings"),\
              scriptedvided.r6sText('1920x1080' , 68, 46),\
              scriptedvided.r6sText('1600x900'  , 84, 54),\
              scriptedvided.r6sText('1280x720'  , 102, 65),\
]}, \
})

# focus on PCIE lanes
configs["episodes"].append( { "title": "The GPU",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:47.4" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GTX1060_GPUZ.mkv"},\
})


# side by side with the 290?
configs["episodes"].append( { "title": "Cooling and Thermals",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:57.4" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GTX1060_R9_290.MP4"},\
"overlay" : { "image" : {"file" : "vs290.png"} }, \
})

#side by side, the cooler on its back, and the fans on the other side
configs["episodes"].append( { "title": "Chunky cooler",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:06.25" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GTX1060_cooling.mp4", "start" : "00:26"},\
})

# internal plate for VRAM 
configs["episodes"].append( { "title": "VRAM and VRM cooling",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:12.8" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GTX1060_cooling.mp4", "start" : "00:00"},\
})

# internal plate for VRAM 
configs["episodes"].append( { "title": "empty PCB",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:26.6" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GTX1060_Pcb.mp4"},\
})

# internal plate for VRAM 
configs["episodes"].append( { "title": "on scale and temps",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:42.7" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GTX1060_weight_barred.mp4"},\
"overlay" : { \
    "text" : ["'Temperatures (Valley)\: 66C (43C delta over ambient)'"]}, \
})


configs["episodes"].append( { "title": "The test system",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:01.6" ), "volume" : 0.999, "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Custom PC'",\
              "'CPU\: Ryzen 5 5600'",\
              "'RAM\: 32GB DDR4, 3600MHz, dual channel'",\
              "'GPU\: GTX 1060'",\
    ]\
}, \
"video" : {"file" : "test_system_RX580.mp4" }\
})

####################### end of intro ###############################


####################### gaming section ###############################

episodes = configs["episodes"]

scriptedvided.addEpisodeWithTextOverlay(episodes, { "title": "Marvel Rivals",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:23.5" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : [sv_ffutils.ffmpegSafeString("low settings"),\
              scriptedvided.r6sText('1920x1080' , 65, 52),\
              scriptedvided.r6sText('1280x720'  , 115, 92),\
]}, \
})

# needs redone
scriptedvided.addEpisodeWithTextOverlay(episodes, { "title": "Cyberpunk 2077",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:05.5" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : [scriptedvided.r6sText('1920x1080, low settings' ,    67, 50),\
              scriptedvided.r6sText('1920x1080, medium settings' , 40, 31),\
              scriptedvided.r6sText('1600x900, high settings' ,    43, 33),\
              scriptedvided.r6sText('1280x720, ultra settings' ,   51, 38),\
]}, \
})

scriptedvided.addEpisodeWithTextOverlay(episodes, { "title": "ARC Raiders",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:29.1" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : [sv_ffutils.ffmpegSafeString("low settings"),\
              scriptedvided.r6sText('1920x1080' , 68, 46),\
              scriptedvided.r6sText('1600x900'  , 84, 54),\
              scriptedvided.r6sText('1280x720'  , 102, 65),\
]}, \
"video" : {"file" : "PioneerGame_gotBackSafe2.mp4", "start" : "09:30"},\
})

configs["episodes"].append( { "title": "Counter-Strike 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:49.9" ), "padAudio" : 0.05 },\
"overlay" : {"benchmark" : {"settings" : "1920x1080, medium settings, no FSR", } }, \
})


scriptedvided.addEpisodeWithTextOverlay(episodes, { "title": "Control",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:14.4" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : [sv_ffutils.ffmpegSafeString("1920x1080"),\
              scriptedvided.r6sText('High settings'   , 39, 31),\
              scriptedvided.r6sText('Medium settings' , 51, 43),\
]},\
"video" : { "file" : "rx580_Control_DX11_2024_07_27_22_47_25_351-converted.mp4", "start" : "01:29" }\
})

scriptedvided.addEpisodeWithTextOverlay(episodes, { "title": "Fortnite",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:39.7" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : [sv_ffutils.ffmpegSafeString("DX12 mode, medium settings"),\
              scriptedvided.r6sText('1920x1080' , 103, 71),\
              scriptedvided.r6sText('1600x900'  , 125, 89),\
              scriptedvided.r6sText('1280x720'  , 156, 109),\
]}, \
"video" : {"file" : "FortniteClient-Win64-Shipping_2026_06_01_18_13_44_994.mkv", "start" : "01:54"},\
})

configs["episodes"].append( { "title": "Doom Eternal",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:58.1" ), "padAudio" : 0.05 },\
"overlay" : {"benchmark" : {"settings" : "1920x1080, ultra settings", } }, \
})

# single resolution
scriptedvided.addEpisodeWithTextOverlay(episodes, { "title": "Apex Legends",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:35" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : [sv_ffutils.ffmpegSafeString("Low settings"),\
              scriptedvided.r6sText('1920x1080' , 184, 129),\
              scriptedvided.r6sText('1600x900'  , 228, 155),\
              scriptedvided.r6sText('1280x720'  , 280, 187),\
]}, \
})

configs["episodes"].append( { "title": "Far Cry 6",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:53.1" ), "padAudio" : 0.05 },\
"overlay" : {"benchmark" : {"settings" : "1920x1080, ultra settings", } }, \
})

scriptedvided.addEpisodeWithTextOverlay(episodes, { "title": "Overwatch 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:20.7" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : [sv_ffutils.ffmpegSafeString("Low settings"),\
              scriptedvided.r6sText('1920x1080' , 335, 242),\
              scriptedvided.r6sText('1600x900'  , 449, 333),\
              scriptedvided.r6sText('1280x720'  , 593, 462),\
]}, \
})

configs["episodes"].append(  { "title": "RE4",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:40.4" ), "padAudio" : 0.05 },\
"overlay" : {"benchmark" : {"settings" : "1920x1080, balanced preset", } }, \
})


scriptedvided.addEpisodeWithTextOverlay(episodes, { "title": "Rainbow Six: Siege",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:07.7"), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : [sv_ffutils.ffmpegSafeString("Low settings"),\
              scriptedvided.r6sText('1920x1080, 100% scale' , 104, 80),\
              scriptedvided.r6sText('1920x1080, 50% scale'  , 159, 121),\
]}, \
})

configs["episodes"].append(  { "title": "Borderlands 3",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:23.7" ), "padAudio" : 0.05 },\
"overlay" : {"benchmark" : {"settings" : "1920x1080, badass settings", } }, \
})


scriptedvided.addEpisodeWithTextOverlay(episodes, { "title": "Robocop",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:49.1" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : [ sv_ffutils.ffmpegSafeString("Low settings"),\
               scriptedvided.r6sText('1920x1080, native'      , 43, 35),\
               scriptedvided.r6sText('1920x1080, FSR Quality' , 54, 44),\
]}, \
})

configs["episodes"].append(  { "title": "The Finals",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:06.9" ), "padAudio" : 0.05 },\
"overlay" : {"benchmark" : {"settings" : "1920x1080, low settings" } }, \
"video" : {"file" : "Discovery_2025_03_15_22_55_07_819.mp4", "start" : "03:30"},\
})

#redo and specify a smoother video
configs["episodes"].append( { "title": "Shadow of the Tomb Raider",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:24.2" ), "padAudio" : 0.05 },\
"overlay" : {"benchmark" : {"settings" : "1920x1080, highest settings" } }, \
})

#redo and specify a smoother video
configs["episodes"].append(  { "title" : "Terminator", \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:39.8" ), "padAudio" : 0.05 },\
"overlay" : {"benchmark" : {"settings" : "1920x1080, epic settings" } },\

})

####################### end of gaming section ###############################


####################### conclusion ###############################
# like Maxwell
configs["episodes"].append(\
{ "title": "Conclusions",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:48.6" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_GTX1060_inHand_barred.mp4"},\
})

configs["episodes"].append(\
{ "title": "side by side with the GTX 960 maybe",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "09:00.1" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_GTX1060_family_barred.mp4"},\
})


configs["episodes"].append(\
{ "title": "1060 and R7 370 both MSI",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "09:03.9" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GTX_1060_R9_370_weighted.mp4", "start" : "00:00"},\
})

configs["episodes"].append(\
{ "title": "R7 370 cooler weight",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "09:13.8" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GTX_1060_R9_370_weighted.mp4", "start" : "00:18"},\
})


configs["episodes"].append(\
{ "title": "1060 cooler weight",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "09:23.2" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GTX_1060_R9_370_weighted.mp4", "start" : "00:05"},\
})

configs["episodes"].append(\
{ "title": "solder bals",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "09:34.4" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_RX580_rippedMem_barred.mp4"},\
})

configs["episodes"].append(\
{ "title": "Zero RPM",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "09:42.8" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_GTX1060_inGrass.MP4"},\
})

configs["episodes"].append(\
{ "title": "3 fans 50 class",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "09:55" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "RTX_3050_3fans.mkv"},\
})

configs["episodes"].append(\
{ "title": "OLX",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "10:3.8" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GTX_1060_breel_andOLX.mp4"},\
})

configs["episodes"].append(\
{ "title": "price of RX 580",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "10:11.2" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "RX_580_olx.mkv"},\
})


configs["episodes"].append(\
{ "title": "settings vs VRAM breel w both RX 580 and GTX 1060",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "10:17.7" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_GTX1060_inHand_barred.mp4"},\
})

configs["episodes"].append(\
{ "title": "bye",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "10:26.8" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_GTX1060_inGrass.MP4"},\
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

