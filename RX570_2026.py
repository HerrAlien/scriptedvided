import scriptedvided
import sv_ffutils

configs = { "defaultAudioFile" : "rx570_2026.ogg",\
"mediaFolder" : "F:\\Videos\\RX570_2026", \
"stockFolder" : "F:\\Videos\\stock",\
"benchmarkFile" : "F:\\Videos\\RX570_2026\\Benchmark_RX570_2026.txt",\
"outputFolder" : "F:\\Videos\\RX570_2026\\output", \
"outputFile" : "RX570_2026.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "This caused NVidia to panic", "until" : "Marvel Rivals"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Marvel Rivals", "until" : "Apex - both"}}, \
{"file" : "Ferco - Inquisitiveness.ogg", "timestamps" : ("01:01", None ), "destinationTimestamp" : {"title" : "Apex - both", "until" : "The Finals"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "The Finals", "until" : "Conclusions"}}, \
{"file" : "Inspired - MaikonMusic  Free Background Music  Audio Library Release.mp3", "timestamps" : ("00:10", None ), "destinationTimestamp" : {"title" : "Conclusions", "until" : "EOF"}}, \
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
"tags" : "NVidia,GeForce,GTX,Pascal,1060,GTX1060,GTX 1060,1060 3G,GTX1060 3G,GTX 1060 3G,AMD,Radeon,Polaris,GCN4,RX570,RX 570",\
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
#  \"video\" *: *\{ *\"file\" *: *\".*\" *\}
#  scriptedvided.r6sText\('.*' *\, *[0-9]*\, *[0-9]*\)
#   "timestamps" *\: *\( *"[0-9\:\.]*" *\, *"[0-9\:\.]*" *\)
#configs["episodes"].append(\
#{ "title": "A favorite of miners and gamers alike",\
#"audio" : {"timestamps" : (scriptedvided.nextTS(configs),  "" ), "volume" : 0.999, "padAudio" : 0.05 },\
#"video" : {"file":""},\
#})

configs["episodes"].append( { "title": "This caused NVidia to panic",\
"audio" : {"timestamps" : ("00:00", "00:09.8"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file":""},\
})
# fixed in february

# overlay with both GTX-es
configs["episodes"].append( { "title": "some game preview",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:17.7" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file":"stock-ApexLegends-1080p-low.mkv"},\
"overlay" : { "image" : {"file" : "Apex Legends.png"} }, \
})

# GPUZ side by side, or with an overlay
configs["episodes"].append( { "title": "The GPU",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:31.4" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file":""},\
})

# side by side 1060s
configs["episodes"].append( { "title": "Cooling and Thermals",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:44.1" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file":""},\
})

configs["episodes"].append( { "title": "The test system",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:55.2" ), "volume" : 0.999, "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Custom PC'",\
              "'CPU\: Ryzen 5 5600'",\
              "'RAM\: 32GB DDR4, 3600MHz, dual channel'",\
              "'GPU\: Sapphire RX 570'",\
    ]\
}, \
"video" : {"file":""}\
})

####################### end of intro ###############################


####################### gaming section ###############################

episodes = configs["episodes"]

scriptedvided.addEpisodeWithTextOverlay(episodes, { "title": "Marvel Rivals",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:16.4" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : [sv_ffutils.ffmpegSafeString("low settings"),\
              scriptedvided.r6sText(' ' , -1 , -1  ),\
              scriptedvided.r6sText(' ' , -1 , -1  ),\
]}, \
})

configs["episodes"].append( { "title": "Marvel - both",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:27.1" ), "padAudio" : 0.05 },\
"isChapter" : False,\
"overlay" : { "image" : {"file" : "Marvel Rivals.png"} }, \
"video" : {"file":""}\
})

scriptedvided.addEpisodeWithTextOverlay(episodes, { "title": "Cyberpunk 2077",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:57.5" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : [scriptedvided.r6sText(' ' , -1 , -1  ),\
              scriptedvided.r6sText(' ' , -1 , -1  ),\
              scriptedvided.r6sText(' ' , -1 , -1  ),\
              scriptedvided.r6sText(' ' , -1 , -1  ),\
]}, \
})

configs["episodes"].append( { "title": "CP2077 - both",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:08.5" ), "padAudio" : 0.05 },\
"isChapter" : False,\
"overlay" : { "image" : {"file" : "Cyber Punk 2077.png"} }, \
"video" : {"file":""}\
})

scriptedvided.addEpisodeWithTextOverlay(episodes, { "title": "Helldivers 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:34.8" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : [scriptedvided.r6sText(' ' , -1 , -1  ),\
              scriptedvided.r6sText(' ' , -1 , -1  ),\
              scriptedvided.r6sText(' ' , -1 , -1  ),\
              scriptedvided.r6sText(' ' , -1 , -1  ),\
]}, \
})


scriptedvided.addEpisodeWithTextOverlay(episodes, { "title": "ARC Raiders",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:56.7" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : [sv_ffutils.ffmpegSafeString("low settings"),\
              scriptedvided.r6sText(' ' , -1 , -1  ),\
              scriptedvided.r6sText(' ' , -1 , -1  ),\
              scriptedvided.r6sText(' ' , -1 , -1  ),\
]}, \
})

configs["episodes"].append( { "title": "ARC - both",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:06.9" ), "padAudio" : 0.05 },\
"isChapter" : False,\
"overlay" : { "image" : {"file" : "ARC Raiders.png"} }, \
"video" : {"file":""}\
})

scriptedvided.addEpisodeWithTextOverlay(episodes, { "title": "Fortnite",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:26" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : [sv_ffutils.ffmpegSafeString("DX12 mode, medium settings"),\
              scriptedvided.r6sText(' ' , -1 , -1  ),\
              scriptedvided.r6sText(' ' , -1 , -1  ),\
              scriptedvided.r6sText(' ' , -1 , -1  ),\
]}, \
"video" : {"file":""},\
})

configs["episodes"].append( { "title": "Fortnite - both",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:37.7" ), "padAudio" : 0.05 },\
"isChapter" : False,\
"overlay" : { "image" : {"file" : "Fortnite.png"} }, \
"video" : {"file":""},\
})

configs["episodes"].append(  { "title": "Control",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:50.2" ), "padAudio" : 0.05 },\
"video" : "",\
"overlay" : {"benchmark" : {"settings" : "1920x1080, high settings" } },\
})

configs["episodes"].append( { "title": "Control - both",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:58.4" ), "padAudio" : 0.05 },\
"isChapter" : False,\
"overlay" : { "image" : {"file" : "Control.png"} }, \
"video" : {"file":""}\
})

configs["episodes"].append( { "title": "Doom Eternal ",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:11.5" ), "padAudio" : 0.05 },\
"overlay" : {"benchmark" : {"settings" : "1920x1080, low settings", } }, \
})

configs["episodes"].append( { "title": "Doom - both",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:30.1" ), "padAudio" : 0.05 },\
"isChapter" : False,\
"overlay" : { "image" : {"file" : "Doom Eternal.png"} }, \
"video" : {"file":""}\
})

# single resolution
scriptedvided.addEpisodeWithTextOverlay(episodes, { "title": "Apex Legends",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:49.5" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : [sv_ffutils.ffmpegSafeString("Low settings"),\
              scriptedvided.r6sText(' ' , -1 , -1  ),\
              scriptedvided.r6sText(' ' , -1 , -1  ),\
              scriptedvided.r6sText(' ' , -1 , -1  ),\
]}, \
})

configs["episodes"].append( { "title": "Apex - both",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:00.9" ), "padAudio" : 0.05 },\
"isChapter" : False,\
"overlay" : { "image" : {"file" : "Apex Legends.png"} }, \
"video" : {"file":""},\
})

configs["episodes"].append( { "title": "Far Cry 6",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:14.8" ), "padAudio" : 0.05 },\
"overlay" : {"benchmark" : {"settings" : "1920x1080, ultra settings", } }, \
})

configs["episodes"].append( { "title": "FC6 - both",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:22.2" ), "padAudio" : 0.05 },\
"isChapter" : False,\
"overlay" : { "image" : {"file" : "Far Cry 6.png"} }, \
"video" : {"file":""},\
})

configs["episodes"].append({ "title": "Overwatch 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:40.7" ), "padAudio" : 0.05 },\
"video" : {"file":""},\
"overlay" : { "image" : {"file" : "Overwatch 2.png"} }, \
})

configs["episodes"].append(  { "title": "RE4",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:57.7" ), "padAudio" : 0.05 },\
"video" : "stock_re4demo_phoneCall.mp4",\
"overlay" : {"benchmark" : {"settings" : "1920x1080, balanced preset", } }, \
})

configs["episodes"].append( { "title": "re4 - both",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:08.6" ), "padAudio" : 0.05 },\
"isChapter" : False,\
"overlay" : { "image" : {"file" : "Resident Evil 4.png"} }, \
"video" : {"video" : "rx570_re4demo_balanced.mp4" , "start" : "00:00" },\
})

configs["episodes"].append( { "title": "Counter-Strike 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:26.2" ), "padAudio" : 0.05 },\
"overlay" : {"benchmark" : {"settings" : "1920x1080, medium settings, no FSR", } }, \
})

configs["episodes"].append( { "title": "CS2 - both",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:36.2" ), "padAudio" : 0.05 },\
"isChapter" : False,\
"video" : "stock_CS2_T_R7_265.mp4",\
"overlay" : { "image" : {"file" : "Counter Strike 2.png"} }, \
})

scriptedvided.addEpisodeWithTextOverlay(episodes, { "title": "Borderlands 3",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:50.5" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : [ scriptedvided.r6sText(' ' , -1 , -1  ),\
               scriptedvided.r6sText(' ' , -1 , -1  ),\
]}, \
})

configs["episodes"].append( { "title": "BL3 - both",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:02.1" ), "padAudio" : 0.05 },\
"isChapter" : False,\
"video" : "Borderlands3_2024_05_03_22_58_15_076.mp4",\
"overlay" : { "image" : {"file" : "Borderlands 3.png"} }, \
})

scriptedvided.addEpisodeWithTextOverlay(episodes, { "title": "Robocop",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:23.9" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : [ sv_ffutils.ffmpegSafeString("Low settings"),\
               scriptedvided.r6sText(' ' , -1 , -1  ),\
               scriptedvided.r6sText(' ' , -1 , -1  ),\
]}, \
})

configs["episodes"].append( { "title": "Robocop - both",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:38.2" ), "padAudio" : 0.05 },\
"isChapter" : False,\
"overlay" : { "image" : {"file" : "Robocop_ Rogue City.png"} }, \
"video" : {"file":""},\
})

scriptedvided.addEpisodeWithTextOverlay(episodes, { "title": "The Finals",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:01.3" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : [sv_ffutils.ffmpegSafeString("low settings"),\
              scriptedvided.r6sText(' ' , -1 , -1  ),\
              scriptedvided.r6sText(' ' , -1 , -1  ),\
              scriptedvided.r6sText(' ' , -1 , -1  ),\
]}, \
"video" : {"file":""},\
})

configs["episodes"].append( { "title": "Finals - both",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:15.2" ), "padAudio" : 0.05 },\
"isChapter" : False,\
"overlay" : { "image" : {"file" : "The Finals.png"} }, \
"video" : {"file":""},\
})

#redo and specify a smoother video
configs["episodes"].append( { "title": "Shadow of the Tomb Raider",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:33" ), "padAudio" : 0.05 },\
"video" : "SOTTR_gaming_highest.mp4",\
"overlay" : {"benchmark" : {"settings" : "1920x1080, very high settings" } }, \
})

configs["episodes"].append( { "title": "sottr - both",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:43.2" ), "padAudio" : 0.05 },\
"isChapter" : False,\
"video" : "SOTTR_gaming_highest.mp4",\
"overlay" : { "image" : {"file" : "Shadow of the Tomb Raider.png"} }, \
})


####################### end of gaming section ###############################


####################### conclusion ###############################
# more ram more better
configs["episodes"].append(\
{ "title": "Conclusions",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:55.5" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file":""},\
})

# mybe breel with 570 and the bar gaph?
configs["episodes"].append(\
{ "title": "More RAM - Apex",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "09:17.5" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file":""},\
})

# mybe breel with 1060 3G and the bar gaph?
configs["episodes"].append(\
{ "title": "No need for RAM - CS2",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "09:39.3" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file":""},\
})

# breel with both, and each with an overlay for what games they play best
configs["episodes"].append(\
{ "title": "Chose based on games",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "09:50.8" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file":""},\
})

configs["episodes"].append(\
{ "title": "OLX pricing single card breel",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "10:06.6" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file":""},\
})

configs["episodes"].append(\
{ "title": "One extra GB worth the price",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "10:18" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file":"olx-rx570-gtx1060_3G.mkv"},\
})

configs["episodes"].append(\
{ "title": "Risky Polaris",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "10:31.5" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file":"mining-rigs.mkv"},\
})

configs["episodes"].append(\
{ "title": "Second recommendation",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "10:44.2" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file":""},\
})

configs["episodes"].append(\
{ "title": "bye",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "10:52" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file":""},\
})


##configs["episodes"].append(\
##{ "title": "Blooper",\
##"isChapter" : False,\
##"audio" : {"timestamps" : (scriptedvided.nextTS(configs),  "" ) },\
##"video" : {"file":""},\
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
scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "Counter-Strike 2"][0], configs)
#scriptedvided.makeVideo(configs)

#for x in range(19,26):
#    scriptedvided.makeVideoForEpisode(configs["episodes"][x], configs)
#
# scriptedvided.makeVideo(configs)

