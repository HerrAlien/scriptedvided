import scriptedvided
import sv_ffutils

configs = { "defaultAudioFile" : "GA-A520M-DS3H.ogg",\
"mediaFolder" : "F:\\Videos\\GA-A520M-DS3H", \
"stockFolder" : "F:\\Videos\\stock",\
"benchmarkFile" : "not needed",\
"outputFolder" : "F:\\Videos\\GA-A520M-DS3H\\output", \
"outputFile" : "GA-A520M-DS3H.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "Back to budget boards", "until" : "The VRMs"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "The VRMs", "until" : "Debug LEDs"}}, \
{"file" : "Ferco - Inquisitiveness.ogg", "timestamps" : ("01:01", None ), "destinationTimestamp" : {"title" : "Debug LEDs", "until" : "Audio from GA-B450M-AorusElite"}}, \
{"file" : "Ferco - Inquisitiveness.ogg", "timestamps" : ("01:01", None ), "destinationTimestamp" : {"title" : "The BIOS setup utility", "until" : "Conclusions"}}, \
{"file" : "Inspired - MaikonMusic  Free Background Music  Audio Library Release.mp3", "timestamps" : ("00:00", None ), "destinationTimestamp" : {"title" : "Conclusions", "until" : "EOF"}}, \
], "volume" : 0.05 },\
"episodes" : [],\
"youtube" : {"title" : "", \
"description" : '''   ''',\
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
#"video" : {"file" : " "},\
#})

configs["episodes"].append(\
{ "title": "Back to budget boards",\
"audio" : {"timestamps" : ("00:00", "00:14.2" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : " "},\
})

configs["episodes"].append(\
{ "title": "The VRMs",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:22") : 0.05 },\
"video" : {"file" : " "},\
})

configs["episodes"].append(\
{ "title": "VRMs - core",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:33.1") : 0.05 },\
"video" : {"file" : " "},\
})

configs["episodes"].append(\
{ "title": "VRMs - soc",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:41.7") : 0.05 },\
"video" : {"file" : " "},\
})

configs["episodes"].append(\
{ "title": "Three good DIMM slots",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:55.7") : 0.05 },\
"video" : {"file" : " "},\
})

configs["episodes"].append(\
{ "title": "Damaged dimm",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:05.3") : 0.05 },\
"video" : {"file" : " "},\
})

configs["episodes"].append(\
{ "title": "Expansion slots, ports and headers",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:24.2") : 0.05 },\
"video" : {"file" : " "},\
})

configs["episodes"].append(\
{ "title": "M2 slot",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:33.7") : 0.05 },\
"video" : {"file" : " "},\
})

configs["episodes"].append(\
{ "title": "SATA ports",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:45") : 0.05 },\
"video" : {"file" : " "},\
})

configs["episodes"].append(\
{ "title": "Pin headers up to TPM",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:06") : 0.05 },\
"video" : {"file" : " "},\
})

configs["episodes"].append(\
{ "title": "Pin headers USBs, FP, Clear CMOS",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:25.3") : 0.05 },\
"video" : {"file" : " "},\
})

# too long of a cut ...
configs["episodes"].append(\
{ "title": "Rear IO",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:01.8") : 0.05 },\
"video" : {"file" : " "},\
}) # maybe an overlay with the DVI-D to HDMI adapter?


# breel with rear IO and side by side the audio in Audacity
configs["episodes"].append(\
{ "title": "The Gigabyte microphone input",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:01.8") : 0.05 },\
"video" : {"file" : " "},\
}) # maybe use a muted video of Audacity

configs["episodes"].append(\
{ "title": "Audio from GA-A520M-DS3H",\
"isChapter" : False,\
"audio" : {"timestamps" : ("02:49.8", "03:01.8" ), "volume" : 0.001, "padAudio" : 0.05 },\
"video" : {"file" : "GA-A520M-DS3H_audioSample.mkv"},\
})

# EC spi chip first
configs["episodes"].append(\
{ "title": "The BIOS setup utility",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:10.1") : 0.05 },\
"video" : {"file" : " "},\
}) # list of bios

configs["episodes"].append(\
{ "title": "BIOS advanced, No CPU freq",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "") : 0.05 },\
"video" : {"file" : " "},\
})

configs["episodes"].append(\
{ "title": "CPU voltage",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "") : 0.05 },\
"video" : {"file" : " "},\
})

configs["episodes"].append(\
{ "title": "Mem profile",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "") : 0.05 },\
"video" : {"file" : " "},\
})

configs["episodes"].append(\
{ "title": "Mem subtimings",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "") : 0.05 },\
"video" : {"file" : " "},\
})

configs["episodes"].append(\
{ "title": "REBAR and TPM",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "") : 0.05 },\
"video" : {"file" : " "},\
})

configs["episodes"].append(\
{ "title": "Fans types",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "") : 0.05 },\
"video" : {"file" : " "},\
})

configs["episodes"].append(\
{ "title": "Fans curve",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "") : 0.05 },\
"video" : {"file" : " "},\
})

configs["episodes"].append(\
{ "title": "Save profiles",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "") : 0.05 },\
"video" : {"file" : " "},\
})

# likes
configs["episodes"].append(\
{ "title": "Conclusions",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "") : 0.05 },\
"video" : {"file" : " "},\
})

configs["episodes"].append(\
{ "title": "likes 4 RAMs",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "") : 0.05 },\
"video" : {"file" : " "},\
})

configs["episodes"].append(\
{ "title": "dislikes - BIOS issues",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "") : 0.05 },\
"video" : {"file" : " "},\
})

configs["episodes"].append(\
{ "title": "Not much different than the A320",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "") : 0.05 },\
"video" : {"file" : " "},\
})

configs["episodes"].append(\
{ "title": "Better budget boards",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "") : 0.05 },\
"video" : {"file" : " "},\
})

configs["episodes"].append(\
{ "title": "Bye",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "") : 0.05 },\
"video" : {"file" : " "},\
})

scriptedvided.makeVideo(configs)

