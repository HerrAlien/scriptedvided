import scriptedvided
import sv_ffutils

configs = { "defaultAudioFile" : "GA-B550M-DS3H_2.ogg",\
"mediaFolder" : "F:\\Videos\\GA-B550M-DS3H", \
"stockFolder" : "F:\\Videos\\stock",\
"benchmarkFile" : "not needed",\
"outputFolder" : "F:\\Videos\\GA-B550M-DS3H\\output", \
"outputFile" : "GA-B550M-DS3H.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "DS3H boards are growing on me", "until" : "The VRMs"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "The VRMs", "until" : "Audio sample"}}, \
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
# \"video\" *: *\{ *\"file\" *: *\".*\" *\}

####################### intro ###############################

# this is the hook
#configs["episodes"].append(\
#{ "title": "A favorite of miners and gamers alike",\
#"audio" : {"timestamps" : ("09:37.3", "09:46" ), "volume" : 0.999, "padAudio" : 0.05 },\
#"video" : {"file" : ""},\
#})

configs["episodes"].append(\
{ "title": "DS3H boards are growing on me",\
"audio" : {"timestamps" : ("00:00", "00:14.9" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B550m-DS3H-Overview.MP4"},\
})

configs["episodes"].append(\
{ "title": "The VRMs",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:25.3"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B550m-DS3H-VRM.MP4"},\
})

configs["episodes"].append(\
{ "title": "VRMs - soc",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:37.5"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B550M-VRM-SOC.mkv"},\
}) # add overlay

configs["episodes"].append(\
{ "title": "VRMs - core",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:52.3"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B550M-VRM-VCORE.mkv"},\
}) # add overlay

configs["episodes"].append(\
{ "title": "8 clips for 4 DIMM slots",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:59.9"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B550m-DS3H-DIMMS.MP4"},\
})


configs["episodes"].append(\
{ "title": "Expansion slots, ports and headers",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:13.4"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B550m-DS3H-Slots.MP4"},\
})

configs["episodes"].append(\
{ "title": "useless X1",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:21.6"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B550M-DS3H_BottomM.2VsGpu.MP4", "start" : "00:04"},\
})

configs["episodes"].append(\
{ "title": "SATA ports",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:34"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B550m-DS3H-SATA2.MP4"},\
}) # TufX570Gaming+Wifi_pins22.MP4

configs["episodes"].append(\
{ "title": "M.2 slots",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:38.5"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B550m-DS3H-Slots.MP4"},\
})

configs["episodes"].append(\
{ "title": "1st M.2",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:48.4"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B550M-DS3H_TopM.2VsGpu.MP4", "start" : "00:04"},\
})

configs["episodes"].append(\
{ "title": "2nd M.2 versus GPU",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:56.8"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B550M-DS3H_BottomM.2VsGpu.MP4", "start" : "00:04"},\
})

configs["episodes"].append(\
{ "title": "2nd M.2 to chipset",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:05.6"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B550m-DS3H-Slots.MP4"},\
})


configs["episodes"].append(\
{ "title": "Pins intro",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:10.3"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B550m-DS3H-Overview.MP4"},\
})

configs["episodes"].append(\
{ "title": "Pin - audio, rgb",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:19.1"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B550m-DS3H-Pins.MP4"},\
})

configs["episodes"].append(\
{ "title": "Pin - tpm, com, usb",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:26.2"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B550m-DS3H-Pins2.MP4"},\
})

configs["episodes"].append(\
{ "title": "Pin FP",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:38.9"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B550m-DS3H-Pins2.MP4"},\
})

configs["episodes"].append(\
{ "title": "Pin SYS FAN 2",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:42.4"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B550m-DS3H-Pins2.MP4"},\
})

configs["episodes"].append(\
{ "title": "Pin SYS FAN 1, prism RGB",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:50.3"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B550m-DS3H-CpuLED.MP4"},\
})

configs["episodes"].append(\
{ "title": "Pin CPU FAN, more RGB",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:58.9"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B550m-DS3H-TopLEDs.MP4"},\
})

configs["episodes"].append(\
{ "title": "No debug LED",\
"isChapter" : False,\
"audio" : {"timestamps" : ("03:06.5", "03:13.5"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B550m-DS3H-Overview.MP4"},\
})

configs["episodes"].append(\
{ "title": "No SPI header",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:20.6"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B550m-DS3H-CpuLED.MP4"},\
}) # TufX570Gaming+Wifi_pins3_DebugLeds.MP4


configs["episodes"].append(\
{ "title": "SOP clip",\
"isChapter" : False,\
"audio" : {"timestamps" : ("06:31.7", "06:38"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "B350_PcMate_BiosReprogram.mp4", "start" : "00:00"},\
})


###
###  need to rescript and re-record, this one has a SOP-8 chip
###

###configs["episodes"].append(\
###{ "title": "DFN vs SOP",\
###"isChapter" : False,\
###"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:27"), "volume" : 0.999, "padAudio" : 0.05 },\
###"video" : {"file" : ""},\
###})
###
###configs["episodes"].append(\
###{ "title": "MSI reprogram",\
###"isChapter" : False,\
###"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:32.5"), "volume" : 0.999, "padAudio" : 0.05 },\
###"video" : {"file" : ""},\
###})
###
###configs["episodes"].append(\
###{ "title": "Desoldered DFN",\
###"isChapter" : False,\
###"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:39.7"), "volume" : 0.999, "padAudio" : 0.05 },\
###"video" : {"file" : ""},\
###})
###
# too long of a cut ...
configs["episodes"].append(\
{ "title": "Rear IO",\
"audio" : {"timestamps" : ("03:39.7", "03:53.2"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B550m-DS3H-IO.MP4"},\
}) # maybe an overlay with the DVI-D to HDMI adapter?

# too long of a cut ...
configs["episodes"].append(\
{ "title": "Audio hint",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:57.2"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B550M-micIn.mkv"},\
"isChapter" : False,\
}) # maybe an overlay with the DVI-D to HDMI adapter?


configs["episodes"].append(\
{ "title": "Audio sample",\
"isChapter" : False,\
"audio" : {"timestamps" : ("03:44.2", "03:57.2" ), "volume" : 0.001, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B550M-micIn.mkv"},\
})

# EC spi chip first
configs["episodes"].append(\
{ "title": "The BIOS setup utility",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:06.3"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B550M-DS3H-BIOS-EZ.MP4"},\
}) # list of bios

# maybe side by 
configs["episodes"].append(\
{ "title": "BIOS advanced, BCLK",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:14.1"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B550M-DS3H-BIOS-BaseClk.MP4"},\
})

configs["episodes"].append(\
{ "title": "BIOS advanced, CPU freq",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:25.3"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B550M-DS3H-BIOS-CoreFreq.MP4"},\
})

configs["episodes"].append(\
{ "title": "CPU voltage",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:43.7"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B550M-DS3H-BIOS-VCore.MP4"},\
})

configs["episodes"].append(\
{ "title": "Mem profile",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:49.3"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B550M-DS3H-BIOS-DOCP.MP4"},\
})

configs["episodes"].append(\
{ "title": "Mem subtimings",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:57.2"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B550M-DS3H-BIOS-RamTimings.MP4", "start" : "00:04"},\
})

configs["episodes"].append(\
{ "title": "Fans types",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:07.5"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B550M-DS3H-BIOS-FanType.MP4"},\
})

configs["episodes"].append(\
{ "title": "fan curve",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:13.5"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B550M-DS3H-BIOS-FanCurve.MP4"},\
})

configs["episodes"].append(\
{ "title": "save fan curve",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:21"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B550M-DS3H-BIOS-SaveFanCurve.MP4"},\
})

configs["episodes"].append(\
{ "title": "TPM",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:28.9"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B550M-DS3H-BIOS-TPM.MP4"},\
})

configs["episodes"].append(\
{ "title": "rebarrish",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:40.6"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B550M-DS3H-BIOS-Rebarish.MP4"},\
})

configs["episodes"].append(\
{ "title": "qflash",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:45.7"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B550M-DS3H-BIOS-QFlash.MP4"},\
})


# TO BE REPLACED
configs["episodes"].append(\
{ "title": "Conclusions",\
"audio" : {"timestamps" : ("06:39.6", "06:46.4"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B550m-DS3H-Overview.MP4"},\
})


configs["episodes"].append(\
{ "title": "heatsinks",\
"isChapter" : False,\
"audio" : {"timestamps" : ("06:10", "06:16.2"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B550m-DS3H-VRM.MP4"},\
})

configs["episodes"].append(\
{ "title": "supports cheap coolers",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:21.7"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_3_vs_4pin_cooler_barred.mp4"},\
})


configs["episodes"].append(\
{ "title": "Bye",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:30"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B550m-DS3H-Overview.MP4"},\
})

scriptedvided.makeVideo(configs)

