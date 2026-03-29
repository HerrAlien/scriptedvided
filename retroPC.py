import scriptedvided

configs = { "defaultAudioFile" : "retro.ogg",\
"mediaFolder" : "F:\\Videos\\Aprils_Fool", \
"stockFolder" : "F:\\Videos\\stock",\
"outputFolder" : "F:\\Videos\\Aprils_Fool\\output", \
"outputFile" : "Aprils_Fool_RetroPC.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "We must test even older GPUs", "until" : "1920x1080 results"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "1920x1080 results", "until" : "Conclusions"}}, \
{"file" : "Inspired - MaikonMusic  Free Background Music  Audio Library Release.mp3", "timestamps" : ("00:00", None ), "destinationTimestamp" : {"title" : "Conclusions", "until" : "EOF"}}, \
], "volume" : 0.045 },\
"episodes" : [],\
"youtube" : {"title" : " ", \
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

Track: Inspired - MaikonMusic [Audio Library Release]
Music provided by Audio Library Plus
Watch: https://www.youtube.com/watch?v=RUkdTkk_52o&t=0s
Free Download / Stream: https://alplus.io/inspired

''', \
"tags" : "ARC,ARC Raiders,AMD,Radeon,GCN,R9 290X,R9 280,R9 370,R7 265,HD 7950,HD 7850,HD7950,HD7850",\
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

# gameplay
configs["episodes"].append(\
{ "title": "Future build looking like the past",\
"audio" : {"timestamps" : ("00:00", "00:08" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "retroPC_overview.MP4"},\
})

configs["episodes"].append(\
{ "title": "RAM pricing from OLX",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : " "},\
})

configs["episodes"].append(\
{ "title": "mistakes have been made",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "retroPC_overview.MP4"},\
"isChapter" : False, \
})

configs["episodes"].append(\
{ "title": "To heck with DDR",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "retroPC_DDRs_v2.MP4" , "start" : "00:00"},\
})

configs["episodes"].append(\
{ "title": "SDRAM used",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : " "},\
})

configs["episodes"].append(\
{ "title": "The CPU",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "need a vid and overlay"},\
})

configs["episodes"].append(\
{ "title": "The Motherboard",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "retroPC_moboOverview.MP4"},\
})

configs["episodes"].append(\
{ "title": "mobo vrm",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "crop of retroPC_moboOverview.MP4"},\
})

configs["episodes"].append(\
{ "title": "mobo dimm slots",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "retroPC_moboDimms.MP4"},\
})

configs["episodes"].append(\
{ "title": "mobo storage",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "retroPC_moboStorage.MP4"},\
})

configs["episodes"].append(\
{ "title": "mobo slots",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "retroPC_moboSlots.MP4"},\
})

configs["episodes"].append(\
{ "title": "mobo rear IO",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "retroPC_moboIO.MP4"},\
})

configs["episodes"].append(\
{ "title": "The GPU",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "retroPC_MX440_2_brighter.mp4"},\
})

configs["episodes"].append(\
{ "title": "Storage",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "retroPC_storage_brighter.mp4"},\
})

configs["episodes"].append(\
{ "title": "The PSU",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "retroPC_PsuLabel_brighter.mp4
"},\
})

configs["episodes"].append(\
{ "title": "usage of the FDD power connector",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "retroPC_PsuFddPower.MP4", "start" : "00:10"},\
})

configs["episodes"].append(\
{ "title": "The Case",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "need video"},\
})

configs["episodes"].append(\
{ "title": "cable management",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "retroPC_overview.MP4"},\
})

configs["episodes"].append(\
{ "title": "OS of Choice",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : " "},\
})

configs["episodes"].append(\
{ "title": "Gaming Results",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "retroPC_games.MP4"},\
})

configs["episodes"].append(\
{ "title": "Quake 3",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "Retro_Q3.MP4"},\
})

configs["episodes"].append(\
{ "title": "Quake 3 results",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "quake3_2026_03_22_15_45_04_286_barred.mp4"},\
"isChapter" : False, \
"overlay" : { \
    "text" : ["'Quake 3'", "'1024x768, high settings - average: 81 FPS'"]\
}, \
})

configs["episodes"].append(\
{ "title": "Medal of Honor: Allied Assault",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "Retro_MOHAA.MP4"},\
})

configs["episodes"].append(\
{ "title": "MOHAA results",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "MOHAA_2026_03_29_17_21_09_595_barred.mp4"},\
"isChapter" : False, \
"overlay" : { \
    "text" : ["'Medal of Honor: Allied Assault'", "'640x480 - average: 41 FPS'"]\
}, \
})

configs["episodes"].append(\
{ "title": "Unreal Tournament",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "Retro_UT2_brighter.mp4"},\
})

configs["episodes"].append(\
{ "title": "UT results",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "UT.mp4"},\
"isChapter" : False, \
"overlay" : { \
    "text" : ["'Unreal Tournament'", "'1024x768, high settings - average: 65 FPS'"]\
}, \
})

configs["episodes"].append(\
{ "title": "Aliens vs. Predator 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "Retro_AvP2_3_brighter.mp4"},\
})

configs["episodes"].append(\
{ "title": "AVP2 results",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "lithtech_2026_03_22_16_00_53_338_barred.mp4", "start" : "00:40"},\
"isChapter" : False, \
"overlay" : { \
    "text" : ["'Aliens vs. Predator 2'", "'800x600, high settings - average: 22 FPS'"]\
}, \
})

configs["episodes"].append(\
{ "title": "Serious Sam: Second Encounter",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "Retro_SSam.MP4"},\
})

configs["episodes"].append(\
{ "title": "Serious Sam results",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "SeriousSam_2026_03_22_16_14_48_214_barred.mp4"},\
"isChapter" : False, \
"overlay" : { \
    "text" : ["'Serious Sam: Second Encounter'", "'640x480, quality preset - average: 51 FPS'"]\
}, \
})

configs["episodes"].append(\
{ "title": "Clive Barker's Undying",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "Undying_2026_03_22_15_35_47_584_barred.mp4", "start" : "00:30"},\
})

configs["episodes"].append(\
{ "title": "Undying results",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "Undying_2026_03_22_15_37_29_923_barred.mp4", "start" : "00:36"},\
"isChapter" : False, \
"overlay" : { \
    "text" : ["'Clive Barker\'s Undying'", "'800x600, medium settings - average: 37 FPS'"]\
}, \
})


# breel with APUs
configs["episodes"].append(\
{ "title": "Conclusions",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "retroPC_MX440.MP4"},\
})

#R9 270 breel
configs["episodes"].append(\
{ "title": "breel 9000 Pro",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : " "},\
})

# gameplay
configs["episodes"].append(\
{ "title": "bye",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "retroPC_overview.MP4"},\
})


#scriptedvided.makeVideoForEpisode(configs["episodes"][1], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][4], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][11], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][12], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][13], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][8], configs)
#print(scriptedvided.makeVideoForEpisode(configs["episodes"][9], configs))
#print(scriptedvided.getSuitableVideoStream(configs["episodes"][9], configs))
#print (configs["youtube"])
#print(scriptedvided.getMusicCreditsString(configs["backgroundTrack"]))
#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "Alien Isolation"][0], configs)
#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "actual 1080 results"][0], configs)
#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "actual 900 results"][0], configs)
#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "actual 720 results"][0], configs)
#print (scriptedvided.getSuitableImage([x for x in configs["episodes"] if x["title"] == "actual 1080 results"][0], configs))

scriptedvided.makeVideo(configs)

# meeds better video, or maybe break it up