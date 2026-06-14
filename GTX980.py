import scriptedvided
import sv_ffutils

configs = { "defaultAudioFile" : "R5_2400G.ogg",\
"mediaFolder" : "F:\\Videos\\R5_2400G", \
"stockFolder" : "F:\\Videos\\stock",\
"benchmarkFile" : "F:\\Videos\\R5_2400G\\Benchmark_R5_2400G_cpu.txt",\
"outputFolder" : "F:\\Videos\\R5_2400G\\output", \
"outputFile" : "R5_2400G.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "One of the first AM4 APUs", "until" : "Marvel Rivals"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Marvel Rivals", "until" : "Doom Eternal all"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Doom Eternal all", "until" : "DOTA 2"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "DOTA 2", "until" : "Video rendering test (The GigASUS)"}}, \
{"file" : "Ferco - Inquisitiveness.ogg", "timestamps" : ("01:01", None ), "destinationTimestamp" : {"title" : "Video rendering test (The GigASUS)", "until" : "Conclusions"}}, \
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
"audio" : {"timestamps" : ("00:00", ""), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

#Maybe have an overlay?
configs["episodes"].append( { "title": "Arc Raiders preview",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

# focus on PCIE lanes
configs["episodes"].append( { "title": "The GPU",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

# focus on PCIE lanes
configs["episodes"].append( { "title": "TDP and Overwatch",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

# focus on PCIE lanes
configs["episodes"].append( { "title": "Cooling and Thermals",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

# focus on PCIE lanes
configs["episodes"].append( { "title": "No RAM cooling",\
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
              "'GPU\: GTX 980'",\
    ]\
}, \
"video" : {"file" : ""},\
})

####################### end of intro ###############################


####################### gaming section ###############################

episodes = configs["episodes"]

scriptedvided.addEpisodeWithTextOverlay(episodes, { "title": "Marvel Rivals",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : [scriptedvided.r6sText("1920x1080, low settings", , ),\
              scriptedvided.r6sText("1280x720, low settings" , , ),\
]}, \
})

# needs redone
scriptedvided.addEpisodeWithTextOverlay(episodes, { "title": "Cyberpunk 2077",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : [sv_ffutils.ffmpegSafeString("1024x768, lowest settings, FSR performance"),\
              scriptedvided.r6sText("", , ),\
              scriptedvided.r6sText("", , ),\
]}, \
})

scriptedvided.addEpisodeWithTextOverlay(episodes, { "title": "ARC Raiders",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : [sv_ffutils.ffmpegSafeString("1280x720, low settings, 0.5 render scale"),\
              scriptedvided.r6sText("", , ),\
              scriptedvided.r6sText("", , ),\
]}, \
"video" : {"file" : ""},\
})

scriptedvided.addEpisodeWithTextOverlay(episodes, { "title": "Fortnite",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : [sv_ffutils.ffmpegSafeString("1280x720, performance mode, 0.5 render scale"),\
              scriptedvided.r6sText("", , ),\
              scriptedvided.r6sText("", , ),\
]}, \
"video" : {"file" : ""},\
})


scriptedvided.addEpisodeWithTextOverlay(episodes, { "title": "Control",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : [sv_ffutils.ffmpegSafeString("960x540, lowest settings"),\
              scriptedvided.r6sText("", , ),\
              scriptedvided.r6sText("", , ),\
]}, \
})

scriptedvided.addEpisodeWithTextOverlay(episodes, { "title": "Rainbow Six: Siege",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), ""), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : [sv_ffutils.ffmpegSafeString("1280x720, low settings, 0.5 render scale"),\
              scriptedvided.r6sText("", , ),\
              scriptedvided.r6sText("", , ),\
]}, \
})

# single resolution
scriptedvided.addEpisodeWithTextOverlay(episodes, { "title": "Apex Legends",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : [sv_ffutils.ffmpegSafeString("800x600, low settings"),\
              scriptedvided.r6sText("", , ),\
              scriptedvided.r6sText("", , ),\
]}, \
})

scriptedvided.addEpisodeWithTextOverlay(episodes, { "title": "Far Cry 6",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : [sv_ffutils.ffmpegSafeString("1280x720, low settings, 0.5 render scale"),\
              scriptedvided.r6sText("", , ),\
              scriptedvided.r6sText("", , ),\
]}, \
})

scriptedvided.addEpisodeWithTextOverlay(episodes, { "title": "Overwatch 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : [sv_ffutils.ffmpegSafeString("1280x720, low settings, 0.5 render scale"),\
              scriptedvided.r6sText("", , ),\
              scriptedvided.r6sText("", , ),\
]}, \
})

scriptedvided.addEpisodeWithTextOverlay(episodes, { "title": "RE4",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : [sv_ffutils.ffmpegSafeString("640x480, prioritize performance"),\
              scriptedvided.r6sText("", , ),\
              scriptedvided.r6sText("", , ),\
]}, \
})

scriptedvided.addEpisodeWithTextOverlay(episodes, { "title": "Counter-Strike 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : [sv_ffutils.ffmpegSafeString("1280x720, low settings, FSR balanced"),\
              scriptedvided.r6sText("", , ),\
              scriptedvided.r6sText("", , ),\
]}, \
})

scriptedvided.addEpisodeWithTextOverlay(episodes, { "title": "Borderlands 3",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : [sv_ffutils.ffmpegSafeString("1280x720, very low settings, 0.5 render scale"),\
              scriptedvided.r6sText("", , ),\
              scriptedvided.r6sText("", , ),\
]}, \
})

scriptedvided.addEpisodeWithTextOverlay(episodes, { "title": "DOTA 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : [sv_ffutils.ffmpegSafeString("1920x1080, low settings"),\
              scriptedvided.r6sText("", , ),\
              scriptedvided.r6sText("", , ),\
]}, \
"video" : "stock_dota2_1080pLow_scale100.mp4"\
})

scriptedvided.addEpisodeWithTextOverlay(episodes, { "title": "Robocop",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : [sv_ffutils.ffmpegSafeString("1920x1080, low settings"),\
              scriptedvided.r6sText("", , ),\
              scriptedvided.r6sText("", , ),\
]}, \
"video" : "stock_dota2_1080pLow_scale100.mp4"\
})

scriptedvided.addEpisodeWithTextOverlay(episodes, { "title": "The Finals",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : [sv_ffutils.ffmpegSafeString("1280x720, low settings, 0.5 render scale"),\
              scriptedvided.r6sText("", , ),\
              scriptedvided.r6sText("", , ),\
]}, \
})

#redo and specify a smoother video
scriptedvided.addEpisodeWithTextOverlay(episodes, { "title": "Shadow of the Tomb Raider",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : [sv_ffutils.ffmpegSafeString("800x600, very low settings"),\
              scriptedvided.r6sText("", , ),\
              scriptedvided.r6sText("", , ),\
]}, \
"video" : {"file" : ""},\
})

#redo and specify a smoother video
scriptedvided.addEpisodeWithTextOverlay(episodes, { "title": "Terminator",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "padAudio" : 0.05 },\
"overlay" : { \
    "text" : [sv_ffutils.ffmpegSafeString("1024x768, low settings, 0.5 render scale"),\
              scriptedvided.r6sText("", , ),\
              scriptedvided.r6sText("", , ),\
]}, \
})

####################### end of gaming section ###############################


####################### conclusion ###############################
# like Maxwell
configs["episodes"].append(\
{ "title": "Conclusions",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "side by side with the RX 580",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "ASUS cooler weight",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "Gigabyte cooler weight",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "Ripped off mem chip",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "Gigabyte touches RAM compared to ASUS",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "ASUS does not care about lifespan",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "Maxwell vs Pascal",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "1060 preview",\
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
#scriptedvided.makeVideoForEpisode(configs["episodes"][21], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][22], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][24], configs)
#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "Marvel Rivals"][0], configs)
#scriptedvided.makeVideo(configs)

#for x in range(19,26):
#    scriptedvided.makeVideoForEpisode(configs["episodes"][x], configs)
#
scriptedvided.makeVideo(configs)

