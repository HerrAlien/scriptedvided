import scriptedvided
import sv_ffutils

configs = { "defaultAudioFile" : "GTX1060-3G.ogg",\
"mediaFolder" : "F:\\Videos\\GTX1060-3G", \
"stockFolder" : "F:\\Videos\\stock",\
"benchmarkFile" : "F:\\Videos\\GTX1060-3G\\Benchmark_GTX1060_3G.txt",\
"outputFolder" : "F:\\Videos\\GTX1060-3G\\output", \
"outputFile" : "GTX1060-3G.mp4", \
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
#  \"video\" *: *\{ *\"file\" *: *\".*\" *\}
#  scriptedvided.r6sText\('.*' *\, *[0-9]*\, *[0-9]*\)
#   "timestamps" *\: *\( *"[0-9\:\.]*" *\, *"[0-9\:\.]*" *\)
#configs["episodes"].append(\
#{ "title": "A favorite of miners and gamers alike",\
#"audio" : {"timestamps" : (scriptedvided.nextTS(configs),  "" ), "volume" : 0.999, "padAudio" : 0.05 },\
#"video" : {"file" : ""},\
#})

configs["episodes"].append( { "title": "Another NVidia controversy",\
"audio" : {"timestamps" : ("00:00", ""), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})
# fixed in february

# overlay with both GTX-es
configs["episodes"].append( { "title": "Overwatch preview",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
"overlay" : { \
    "text" : [sv_ffutils.ffmpegSafeString("low settings"),\
              scriptedvided.r6sText( '1920x1080' ,  301, 214),\
]}, \
})

# GPUZ side by side, or with an overlay
configs["episodes"].append( { "title": "The GPU",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

# side by side 1060s
configs["episodes"].append( { "title": "Cooling and Thermals",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

#
configs["episodes"].append( { "title": "cooler with single heatpipe",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append( { "title": "no VRM contact",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append( { "title": "zoom in to cuts in heatsink",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append( { "title": "actual temps with GPU breel",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

# side by side GPUzs
configs["episodes"].append( { "title": "Just 3GB",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

# side by side GPUzs
configs["episodes"].append( { "title": "VRAM mattered in this game",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append( { "title": "The test system",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "volume" : 0.999, "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Custom PC'",\
              "'CPU\: Ryzen 5 5600'",\
              "'RAM\: 32GB DDR4, 3600MHz, dual channel'",\
              "'GPU\: GTX 1060 3G'",\
    ]\
}, \
"video" : {"file" : ""}\
})

####################### end of intro ###############################


####################### gaming section ###############################

episodes = configs["episodes"]

scriptedvided.addEpisodeWithTextOverlay(episodes, { "title": "Marvel Rivals",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : [sv_ffutils.ffmpegSafeString("low settings"),\
              scriptedvided.r6sText( ' ' ,  , ),\
              scriptedvided.r6sText( ' ' ,  , ),\
]}, \
})

# needs redone
scriptedvided.addEpisodeWithTextOverlay(episodes, { "title": "Cyberpunk 2077",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : [scriptedvided.r6sText( ' ' ,  , ),\
              scriptedvided.r6sText( ' ' ,  , ),\
              scriptedvided.r6sText( ' ' ,  , ),\
              scriptedvided.r6sText( ' ' ,  , ),\
]}, \
})

scriptedvided.addEpisodeWithTextOverlay(episodes, { "title": "ARC Raiders",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : [sv_ffutils.ffmpegSafeString("low settings"),\
              scriptedvided.r6sText( ' ' ,  , ),\
              scriptedvided.r6sText( ' ' ,  , ),\
              scriptedvided.r6sText( ' ' ,  , ),\
]}, \
"video" : {"file" : ""},\
})

scriptedvided.addEpisodeWithTextOverlay(episodes, { "title": "Fortnite",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : [sv_ffutils.ffmpegSafeString("DX12 mode, medium settings"),\
              scriptedvided.r6sText( ' ' ,  , ),\
              scriptedvided.r6sText( ' ' ,  , ),\
              scriptedvided.r6sText( ' ' ,  , ),\
]}, \
"video" : {"file" : ""},\
})

scriptedvided.addEpisodeWithTextOverlay(episodes, { "title": "Control",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : [sv_ffutils.ffmpegSafeString("1920x1080"),\
              scriptedvided.r6sText( ' ' ,  , ),\
              scriptedvided.r6sText( ' ' ,  , ),\
]},\
"video" : {"file" : ""}\
})

configs["episodes"].append( { "title": "Doom Eternal",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "padAudio" : 0.05 },\
"overlay" : {"benchmark" : {"settings" : "1920x1080, ultra settings", } }, \
})

# single resolution
scriptedvided.addEpisodeWithTextOverlay(episodes, { "title": "Apex Legends",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : [sv_ffutils.ffmpegSafeString("Low settings"),\
              scriptedvided.r6sText( ' ' ,  , ),\
              scriptedvided.r6sText( ' ' ,  , ),\
              scriptedvided.r6sText( ' ' ,  , ),\
]}, \
})

configs["episodes"].append( { "title": "Far Cry 6",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "padAudio" : 0.05 },\
"overlay" : {"benchmark" : {"settings" : "1920x1080, ultra settings", } }, \
})

scriptedvided.addEpisodeWithTextOverlay(episodes, { "title": "Overwatch 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : [sv_ffutils.ffmpegSafeString("Low settings"),\
              scriptedvided.r6sText( ' ' ,  , ),\
              scriptedvided.r6sText( ' ' ,  , ),\
              scriptedvided.r6sText( ' ' ,  , ),\
]}, \
})

configs["episodes"].append(  { "title": "RE4",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "padAudio" : 0.05 },\
"overlay" : {"benchmark" : {"settings" : "1920x1080, balanced preset", } }, \
})

configs["episodes"].append( { "title": "Counter-Strike 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "padAudio" : 0.05 },\
"overlay" : {"benchmark" : {"settings" : "1920x1080, medium settings, no FSR", } }, \
})

configs["episodes"].append(  { "title": "Borderlands 3",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "padAudio" : 0.05 },\
"overlay" : {"benchmark" : {"settings" : "1920x1080, badass settings", } }, \
})

scriptedvided.addEpisodeWithTextOverlay(episodes, { "title": "Robocop",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : [ sv_ffutils.ffmpegSafeString("Low settings"),\
               scriptedvided.r6sText( ' ' ,  , ),\
               scriptedvided.r6sText( ' ' ,  , ),\
]}, \
})

configs["episodes"].append(  { "title": "The Finals",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "padAudio" : 0.05 },\
"overlay" : {"benchmark" : {"settings" : "1920x1080, low settings" } }, \
"video" : {"file" : ""},\
})

#redo and specify a smoother video
configs["episodes"].append( { "title": "Shadow of the Tomb Raider",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "padAudio" : 0.05 },\
"overlay" : {"benchmark" : {"settings" : "1920x1080, highest settings" } }, \
})

#redo and specify a smoother video
configs["episodes"].append(  { "title" : "Terminator", \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "padAudio" : 0.05 },\
"overlay" : {"benchmark" : {"settings" : "1920x1080, epic settings" } },\

})

####################### end of gaming section ###############################


####################### conclusion ###############################
# like Maxwell
configs["episodes"].append(\
{ "title": "But the cooler ...",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "no VRM contact",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "little airflow for VRM",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "fins trap air against the mobo",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "dead mosfet",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "Aliexpress coolers touch the VRM",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "done venting",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "Conclusions",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "Not competing against 6G 1060",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
"overlay" : { "image" : {"file" : "vsOther60Cards.png"} }, \
})

configs["episodes"].append(\
{ "title": "but against Polaris - prices",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "Doom Eternal - 3G stayed at medium",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "Extra 1G might help",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "RX 570 breel",\
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

