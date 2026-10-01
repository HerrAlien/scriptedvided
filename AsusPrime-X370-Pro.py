import scriptedvided
import sv_ffutils

configs = { "defaultAudioFile" : "Prime-X370-Pro.ogg",\
"mediaFolder" : "F:\\Videos\\AsusPrime-X370-Pro", \
"stockFolder" : "F:\\Videos\\stock",\
"benchmarkFile" : "not needed",\
"outputFolder" : "F:\\Videos\\AsusPrime-X370-Pro\\output", \
"outputFile" : "AsusPrime-X370-Pro.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "Good bang for the buck", "until" : "The VRMs"}}, \
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
{ "title": "Good bang for the buck",\
"audio" : {"timestamps" : ("00:00", "00:17.2" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "ASUS-PrimeX370Pro-Overview_bright.MP4"},\
})

configs["episodes"].append(\
{ "title": "The VRMs",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:27.1"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "ASUS-PrimeX370Pro-VRM_bright.MP4"},\
})

configs["episodes"].append(\
{ "title": "VRM Topo",\
"isChapter" : False,\
"audio" : {"file" : "Prime-X370-Pro-VrmTopo.ogg", \
"timestamps" : ("00:00", "00:13.1"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "X370-Pro-VRM-Topo.mkv", "start" : "00:15"},\
}) # add overlay

configs["episodes"].append(\
{ "title": "VRMs overview again",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:35.5", "00:45.2"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "ASUS-PrimeX370Pro-VRM_bright.MP4"},\
}) # add overlay

configs["episodes"].append(\
{ "title": "4 DIMM slots",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:51"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "ASUS-PrimeX370Pro-DIMMs_bright.MP4"},\
})

configs["episodes"].append(\
{ "title": "RAM removal with overlay",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:02.6"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Asrock_A320M-DVS_RamInsertionRemoval.MP4", "start" : "00:23"},\
}) # add overlay


configs["episodes"].append(\
{ "title": "Expansion slots, ports and headers",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:07.4"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "ASUS-PrimeX370Pro-Slots2_bright.MP4"},\
})

##Needs overlays:s:
configs["episodes"].append(\
{ "title": "GPU slot",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:11.6"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "ASUS-PrimeX370Pro-Slots2_bright.MP4"},\
"overlay" : { "image" : {"file" : "slots-overlays-GPU.png"} }, \
})

##Needs overlays:s:
configs["episodes"].append(\
{ "title": "x1 slots",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:20.3"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "ASUS-PrimeX370Pro-Slots2_bright.MP4"},\
"overlay" : { "image" : {"file" : "slots-overlays-x1s.png"} }, \
})

##Needs overlays:s:
configs["episodes"].append(\
{ "title": "x8",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:31.8"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "ASUS-PrimeX370Pro-Slots2_bright.MP4"},\
"overlay" : { "image" : {"file" : "slots-overlays-x8.png"} }, \
})

##Needs overlays:s:
configs["episodes"].append(\
{ "title": "x4 and x1",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:37"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "ASUS-PrimeX370Pro-Slots2_bright.MP4"},\
"overlay" : { "image" : {"file" : "slots-overlays-x1x4.png"} }, \
})

configs["episodes"].append(\
{ "title": "m.2",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:45.5"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "ASUS-PrimeX370Pro-M2_bright.MP4"},\
})

configs["episodes"].append(\
{ "title": "SATA ports",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:57.2"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "ASUS-PrimeX370Pro-SATA_bright.MP4"},\
}) 

configs["episodes"].append(\
{ "title": "Pins intro",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:01.7"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "ASUS-PrimeX370Pro-Overview_bright.MP4"},\
})

configs["episodes"].append(\
{ "title": "Audio, com, tpm, PHD 6000",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:12.5"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "ASUS-PrimeX370Pro-Pins_bright.MP4"},\
})

configs["episodes"].append(\
{ "title": "Pin - USB2, USB3, clear RTC, CI",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:31.9"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "ASUS-PrimeX370Pro-Pins2_bright.MP4"},\
})

configs["episodes"].append(\
{ "title": "Pin fan headers, FP",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:38.9"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "ASUS-PrimeX370Pro-Pins2_bright.MP4"},\
})

configs["episodes"].append(\
{ "title": "weird USB3",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:44.6"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "ASUS-PrimeX370Pro-USBC31_bright.MP4"},\
})

##Needs overlays::
configs["episodes"].append(\
{ "title": "CPU fans",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:47.9"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "ASUS-PrimeX370Pro-VRM_bright.MP4"},\
})

configs["episodes"].append(\
{ "title": "sys fans",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:52"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "ASUS-PrimeX370Pro-SPI_RGB_bright.MP4"},\
})

configs["episodes"].append(\
{ "title": "SPI header",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:58.8"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "ASUS-PrimeX370Pro-SPI_RGB_bright.MP4"},\
})


#Needs overlays::
configs["episodes"].append(\
{ "title": "Rear IO",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:11"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "ASUS-PrimeX370Pro-IO_bright.MP4"},\
})

#Needs overlays::
configs["episodes"].append(\
{ "title": "video outs",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:14.7"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "ASUS-PrimeX370Pro-IO_bright.MP4"},\
"isChapter" : False,\
}) # maybe an overlay with the DVI-D to HDMI adapter?

#Needs overlays::
configs["episodes"].append(\
{ "title": "USBs, ethernet, audio",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "3:21.4"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "ASUS-PrimeX370Pro-IO_bright.MP4"},\
"isChapter" : False,\
}) # maybe an overlay with the DVI-D to HDMI adapter?


# too long of a cut ...
configs["episodes"].append(\
{ "title": "Audio hint",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:26.9"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Prime-X370-Pro-audioSample.mkv"},\
"isChapter" : False,\
}) # maybe an overlay with the DVI-D to HDMI adapter?


configs["episodes"].append(\
{ "title": "Audio sample",\
"isChapter" : False,\
"audio" : {"timestamps" : ("03:16", "03:26.9" ), "volume" : 0.001, "padAudio" : 0.05 },\
"video" : {"file" : "Prime-X370-Pro-audioSample.mkv"},\
})

# EC spi chip first
configs["episodes"].append(\
{ "title": "The BIOS setup utility",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:37.9"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "PrimeX370-Pro_BIOS_EzXmp.MP4"},\
}) # list of bios

configs["episodes"].append(\
{ "title": "BIOS advanced, CPU freq",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:49.3"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "PrimeX370-Pro_BIOS_CoreFreq2.MP4"},\
})

configs["episodes"].append(\
{ "title": "CPU voltage",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:04.5"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "PrimeX370-Pro_BIOS_CoreVoltage2.MP4"},\
})

configs["episodes"].append(\
{ "title": "Mem profile",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:11.1"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "PrimeX370-Pro_BIOS_Xmp2.MP4"},\
})

configs["episodes"].append(\
{ "title": "Mem subtimings",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:21.9"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "PrimeX370-Pro_BIOS_RamTimings2.MP4"},\
})

configs["episodes"].append(\
{ "title": "Fans types",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:26.4"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "PrimeX370-Pro_BIOS_FanTypes.MP4", "start" : "00:00"},\
})

configs["episodes"].append(\
{ "title": "Aigo",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:31.9"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "system_cpuCooler_coldplate.mp4"},\
})

configs["episodes"].append(\
{ "title": "Fans types again",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:36"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "PrimeX370-Pro_BIOS_FanTypes.MP4", "start" : "08:00"},\
})

configs["episodes"].append(\
{ "title": "fan curve text mode",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:47.1"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "PrimeX370-Pro_BIOS_FanCurveText.MP4"},\
})

configs["episodes"].append(\
{ "title": "fan curve with UI",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:54.3"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "PrimeX370-Pro_BIOS_FanProfilesCurveEditor.MP4"},\
})


# with VRMs. Side by side with the B550
configs["episodes"].append(\
{ "title": "Conclusions",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:10.8"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "ASUS-PrimeX370Pro-Overview_bright.MP4"},\
})


configs["episodes"].append(\
{ "title": "decent VRM",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:21.8"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "ASUS-PrimeX370Pro-VRM_bright.MP4"},\
})

configs["episodes"].append(\
{ "title": "ok solution, but single M.2",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:29.8"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "ASUS-PrimeX370Pro-M2_bright.MP4"},\
})

configs["episodes"].append(\
{ "title": "SSD prices",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:34.8"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "SSD-prices.mkv"},\
})

configs["episodes"].append(\
{ "title": "motherboards to subscribe",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:41.4"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "MSI-B350mProVD-Plus-Overview.MP4"},\
})

configs["episodes"].append(\
{ "title": "Bye",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:48.2"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "ASUS-PrimeX370Pro-Overview_bright.MP4"},\
})


# scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "GPU slot"][0], configs)



scriptedvided.makeVideo(configs)

