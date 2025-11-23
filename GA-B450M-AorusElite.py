import scriptedvided
import sv_ffutils

configs = { "defaultAudioFile" : "GA-B450M-Aorus-Elite-V2.ogg",\
"mediaFolder" : "F:\\Videos\\GA-B450M-Aorus-Elite-V2", \
"stockFolder" : "F:\\Videos\\stock",\
"benchmarkFile" : "not needed",\
"outputFolder" : "F:\\Videos\\GA-B450M-Aorus-Elite-V2\\output", \
"outputFile" : "GA-B450M-AorusElite.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "This has to be good", "until" : "The VRMs"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "The VRMs", "until" : "Audio from GA-B450M-AorusElite"}}, \
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
#"video" : {"file" : ""},\
#})

configs["episodes"].append(\
{ "title": "This has to be good",\
"audio" : {"timestamps" : ("00:00", "00:12.9" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Aorus-B450-Elite_Overall.MP4"},\
})

configs["episodes"].append(\
{ "title": "The VRMs",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:22.5" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Aorus-B450-Elite_VRM.MP4"},\
})

configs["episodes"].append(\
{ "title": "VRMs - boardview, core",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:36" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B450M-AorusElite_BViewVrmVcore.mkv"},\
})

configs["episodes"].append(\
{ "title": "VRMs - boardview, soc",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:42" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B450M-AorusElite_BViewVrmSoc.mkv"},\
})

configs["episodes"].append(\
{ "title": "VRMs - boardview, advertising",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:50.2" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B450M-AorusEliteV2_8+8Phases.mkv"},\
})

configs["episodes"].append(\
{ "title": "VRMs - overview",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:07.8" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Aorus-B450-Elite_VRM.MP4"},\
})

configs["episodes"].append(\
{ "title": "VRMs - ESP, boarview and mobo",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:16.1" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B450M-AorusEliteV2-12VEps.mp4"},\
})


configs["episodes"].append(\
{ "title": "Four good DIMM slots",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:32.5" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Aorus-B450-Elite_DIMMs.MP4"},\
})

configs["episodes"].append(\
{ "title": "Expansion slots, ports and headers",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:52.8" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Aorus-B450-Elite_Slots.MP4"},\
})

configs["episodes"].append(\
{ "title": "M2 slots",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:07" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Aorus-B450-Elite_Slots.MP4"},\
})

configs["episodes"].append(\
{ "title": "SATA ports",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:23.4" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Aorus-B450-Elite_SATA.MP4"},\
})

configs["episodes"].append(\
{ "title": "Pin headers 1, up to com",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:50.9" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Aorus-B450-Elite_Pins1.MP4"},\
})

configs["episodes"].append(\
{ "title": "Pin headers 2, com USBs",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:09.6" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Aorus-B450-Elite_Pins2.MP4"},\
})

configs["episodes"].append(\
{ "title": "Pin headers 3, FP, cmos",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:26.3" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Aorus-B450-Elite_Pins2.MP4"},\
})

configs["episodes"].append(\
{ "title": "Pin headers RGB, top",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:36" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Aorus-B450-Elite_RgbLed1.MP4"},\
})

configs["episodes"].append(\
{ "title": "Pin headers RGB, next to CPU",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:46.4" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Aorus-B450-Elite_RgbLED2.MP4"},\
})

configs["episodes"].append(\
{ "title": "Debug LEDs",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:07" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Aorus-B450-Elite_DebugLEDs.MP4"},\
})

# too long of a cut ...
configs["episodes"].append(\
{ "title": "Rear IO",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:27.7" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Aorus-B450-Elite_IO.MP4"},\
}) # maybe an overlay with the DVI-D to HDMI adapter?

# breel with rear IO and side by side the audio in Audacity
configs["episodes"].append(\
{ "title": "The Gigabyte microphone input",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:37.6" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B450M-AorusEliteV2_AudioIoAndClip.mp4"},\
}) # maybe use a muted video of Audacity

configs["episodes"].append(\
{ "title": "Audio from GA-B450M-AorusElite",\
"isChapter" : False,\
"audio" : {"timestamps" : ("04:27.6", "04:37.6" ), "volume" : 0.001, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B450M-AorusEliteV2_AudioSample.mp4", "start" : "00:03"},\
})

# EC spi chip first
configs["episodes"].append(\
{ "title": "The BIOS setup utility",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:00.2" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B450M-AorusEliteV2_EcChip.mp4"},\
}) # list of bios

configs["episodes"].append(\
{ "title": "BIOS - EZ mode",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:14.4" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B450-AorusEliteV2_BIOS_Easy.MP4"},\
})

configs["episodes"].append(\
{ "title": "BIOS advanced, CPU freq",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:25.4" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B450-AorusEliteV2_BIOS_CpuMultiplier.MP4"},\
})

configs["episodes"].append(\
{ "title": "CPU voltage",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:43.3" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B450-AorusEliteV2_BIOS_CpuVoltage.MP4"},\
})

configs["episodes"].append(\
{ "title": "Mem profile",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:52" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B450-AorusEliteV2_BIOS_XMP.MP4"},\
})

configs["episodes"].append(\
{ "title": "Mem subtimings",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:07.4" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B450-AorusEliteV2_BIOS_MemFreqTimings.MP4"},\
})

configs["episodes"].append(\
{ "title": "REBAR and TPM",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:25" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B450-AorusEliteV2_BIOS_TpmAbove4G.MP4", "start" : "00:00"},\
})

configs["episodes"].append(\
{ "title": "Fans types",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:31.8" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B450-AorusEliteV2_BIOS_FanType.MP4"},\
})

configs["episodes"].append(\
{ "title": "Fans curve",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:40.2" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B450-AorusEliteV2_BIOS_FanCurve.MP4"},\
})

configs["episodes"].append(\
{ "title": "RGB fusion",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:54.2" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B450-AorusEliteV2_BIOS_Rgb1.MP4", "start" : "00:00"},\
})

configs["episodes"].append(\
{ "title": "RGB fusion - color selection",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:00.2" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B450-AorusEliteV2_BIOS_Rgb1.MP4", "start" : "00:14"},\
})

# likes
configs["episodes"].append(\
{ "title": "Conclusions",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:15" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Aorus-B450-Elite_Overall.MP4"},\
})

configs["episodes"].append(\
{ "title": "dislikes",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:27.6" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B450M-AorusEliteV2-12VEps.mp4"},\
})

configs["episodes"].append(\
{ "title": "dislikes - heatsinks and pins",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:45.4" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Aorus-B450-Elite_heatsinkSecured.MP4"},\
})

configs["episodes"].append(\
{ "title": "Harrowing bios update",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:05.7" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B450M-AorusEliteV2_BiosUpdateProcess.mkv"},\
})

configs["episodes"].append(\
{ "title": "People might like it",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:14.3" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Aorus-B450-Elite_Overall.MP4"},\
})

configs["episodes"].append(\
{ "title": "Bye",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:31.7" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Aorus-B450-Elite_Overall.MP4"},\
})

scriptedvided.makeVideo(configs)

