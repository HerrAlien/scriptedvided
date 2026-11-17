import scriptedvided
import sv_ffutils

configs = { "defaultAudioFile" : "Prime-B350M-A.ogg",\
"mediaFolder" : "F:\\Videos\\AsusPrime-B350M-A", \
"stockFolder" : "F:\\Videos\\stock",\
"benchmarkFile" : "not needed",\
"outputFolder" : "F:\\Videos\\AsusPrime-B350M-A\\output", \
"outputFile" : "AsusPrime-B350M-A.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "Middle ground ... tease?", "until" : "The VRMs"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "The VRMs", "until" : "Audio sample"}}, \
{"file" : "Ferco - Inquisitiveness.ogg", "timestamps" : ("01:01", None ), "destinationTimestamp" : {"title" : "The BIOS setup utility", "until" : "Conclusions"}}, \
{"file" : "Inspired - MaikonMusic  Free Background Music  Audio Library Release.mp3", "timestamps" : ("00:00", None ), "destinationTimestamp" : {"title" : "Conclusions", "until" : "EOF"}}, \
], "volume" : 0.035 },\
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
{ "title": "Middle ground ... tease?",\
"audio" : {"timestamps" : ("00:00", "00:11.6" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "PrimeB350m-overview_firstFrame.mp4", "start" : "00:00"},\
})

configs["episodes"].append(\
{ "title": "The VRMs",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:18.2"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "PrimeB350m-VRMs.MP4"},\
})

# add overlay # add overlay # add overlay # add overlay
configs["episodes"].append(\
{ "title": "VRM topo",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:27.4"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "PrimeB350m-VRMs.MP4"},\
"overlay" : { "image" : {"file" : "vrm.png" } }, \
}) # add overlay # add overlay # add overlay

configs["episodes"].append(\
{ "title": "PCB holes",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:35.4"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "PrimeB350m-addedHeatsink.MP4", "start" : "00:04"},\
}) # add overlay

configs["episodes"].append(\
{ "title": "Z97 heatsink",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:42.3"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "PrimeB350m-addedHeatsink.MP4", "start" : "00:24"},\
})

configs["episodes"].append(\
{ "title": "keep the heatsink",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:54.5"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "PC-David-Mobo.MP4", "start" : "00:10"},\
})

configs["episodes"].append(\
{ "title": "4 DIMM slots",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:08.5"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "PrimeB350m-DIMMs.MP4"},\
})

# # # full board overview
configs["episodes"].append(\
{ "title": "Expansion slots, ports and headers",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:17.1"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "PrimeB350m-overview.MP4"},\
})

##Needs overlays:s:
configs["episodes"].append(\
{ "title": "GPU slot",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:22"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "PrimeB350m-slots.MP4"},\
"overlay" : { "image" : {"file" : "pciex16.png" } }, \
})

##Needs overlays:s:
configs["episodes"].append(\
{ "title": "x1 slots",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:29.9"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "PrimeB350m-slots.MP4"},\
"overlay" : { "image" : {"file" : "pciex1.png" } }, \
})

# -----------------------------------------------------------------------------------------------------
##NEEDS RECORDING
configs["episodes"].append(\
{ "title": "Great success",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:00.2", "00:01.5"), "volume" : 0.999, "padAudio" : 0.05, "file" : "extraPrimeB350M-A.ogg" },\
"video" : {"file" : "GA-A320M-H_Pcie1xVs2SlotCard.MP4", "start" : "00:25"},\
})

##NEEDS RECORDING
configs["episodes"].append(\
{ "title": "NVME slot",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:01.5", "00:16"), "volume" : 0.999, "padAudio" : 0.05, "file" : "extraPrimeB350M-A.ogg" },\
"video" : {"file" : "PrimeB350m-slots.MP4"},\
})
# -----------------------------------------------------------------------------------------------------

## again, overview - ish
configs["episodes"].append(\
{ "title": "SATA",\
"isChapter" : False,\
"audio" : {"timestamps" : ("01:29.9", "01:36.1"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "PrimeB350m-overview.MP4"},\
})

##Needs overlays:s:
configs["episodes"].append(\
{ "title": "regular ssd",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:41.4"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_digUpOldSSD_barred.mp4"},\
})

configs["episodes"].append(\
{ "title": "SATA ports",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:55.3"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "PrimeB350m-SATA2_slightlybrighter.mp4"},\
}) 

# overlays, overlays ... 
configs["episodes"].append(\
{ "title": "Pins intro",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:09.7"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "PrimeB350m-pins_brighter.mp4"},\
"overlay" : { "image" : {"file" : "audio-com.png" } }, \
})

configs["episodes"].append(\
{ "title": "tpm",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:16", "00:23"), "volume" : 0.999, "padAudio" : 0.05, "file" : "extraPrimeB350M-A.ogg" },\
"video" : {"file" : "PrimeB350m-pins_brighter.mp4"},\
"overlay" : { "image" : {"file" : "tpm.png" } }, \
})

configs["episodes"].append(\
{ "title": "USB",\
"isChapter" : False,\
"audio" : {"timestamps" : ("02:20", "02:25.6"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "PrimeB350m-pins_brighter.mp4"},\
"overlay" : { "image" : {"file" : "usb2.png" } }, \
})

## REDO REDO
configs["episodes"].append(\
{ "title": "front panel",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:23", "00:30.7"), "volume" : 0.999, "padAudio" : 0.05, "file" : "extraPrimeB350M-A.ogg" },\
"video" : {"file" : "PrimeB350m-pins2_brighter.mp4"},\
"overlay" : { "image" : {"file" : "front-panel.png" } }, \
})

## REDO REDO
configs["episodes"].append(\
{ "title": "RGB",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:30.7", "00:36.5"), "volume" : 0.999, "padAudio" : 0.05,  "file" : "extraPrimeB350M-A.ogg" },\
"video" : {"file" : "PrimeB350m-SysFanSpi_brighter.mp4"},\
"overlay" : { "image" : {"file" : "rgb.png" } }, \
})

##Needs overlays::##Needs overlays::##Needs overlays::##Needs overlays::
configs["episodes"].append(\
{ "title": "SPI header",\
"isChapter" : False,\
"audio" : {"timestamps" : ("02:40.9", "02:53"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "PrimeB350m-SysFanSpi_brighter.mp4"},\
"overlay" : { "image" : {"file" : "spi.png" } }, \
})

##Needs overlays::##Needs overlays::##Needs overlays::##Needs overlays::
configs["episodes"].append(\
{ "title": "clear RTC",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:59.4"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "PrimeB350m-pins2_brighter.mp4"},\
"overlay" : { "image" : {"file" : "clear-rtc.png" } }, \
})

configs["episodes"].append(\
{ "title": "CPu fans, phd 6k",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:07.4"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "PrimeB350m-CpuFanPhd6000_brighter.mp4"},\
})

configs["episodes"].append(\
{ "title": "sys fan",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:13.6"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "PrimeB350m-SysFanSpi_brighter.mp4"},\
"overlay" : { "image" : {"file" : "sysFan.png" } }, \
})

#just the rear io reel
configs["episodes"].append(\
{ "title": "Rear IO",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:42.3"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "PrimeB350m-IO.MP4"},\
"isChapter" : False,\
}) # maybe an overlay with the DVI-D to HDMI adapter?


configs["episodes"].append(\
{ "title": "Audio sample",\
"isChapter" : False,\
"audio" : {"timestamps" : ("03:28.3", "03:42.3" ), "volume" : 0.001, "padAudio" : 0.05 },\
"video" : {"file" : "PrimeB350M-A-audioSample.mkv"},\
})

# EC spi chip first
configs["episodes"].append(\
{ "title": "The BIOS setup utility",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:54.2"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "ASUS-PrimeB350m-A_BIOS_Ez_noTilt.mp4"},\
}) # list of bios

configs["episodes"].append(\
{ "title": "BIOS advanced, CPU freq",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:04.3"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "ASUS-PrimeB350m-A_BIOS_CpuFreq_noTilt.mp4"},\
})

configs["episodes"].append(\
{ "title": "CPU voltage",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:13"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "ASUS-PrimeB350m-A_BIOS_CpuVoltage_noTilt.mp4"},\
})

configs["episodes"].append(\
{ "title": "Mem subtimings",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:24.8"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "ASUS-PrimeB350m-A_BIOS_XMP_noTilt.mp4", "start" : "00:11"},\
})

configs["episodes"].append(\
{ "title": "rebar",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:29.5"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "ASUS-PrimeB350m-A_BIOS_Rebar_noTilt.mp4"},\
})

configs["episodes"].append(\
{ "title": "TPM",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:38.4"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "ASUS-PrimeB350m-A_BIOS_Tpm_noTilt.mp4"},\
})


configs["episodes"].append(\
{ "title": "Fans types",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:36.6", "00:45.15"), "volume" : 0.999, "padAudio" : 0.05 ,  "file" : "extraPrimeB350M-A.ogg"},\
"video" : {"file" : "ASUS-PrimeB350m-A_BIOS_FanCurve2_noTilt.mp4"},\
})

configs["episodes"].append(\
{ "title": "ICE-400",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:45.15", "00:54.1"), "volume" : 0.999, "padAudio" : 0.05 ,  "file" : "extraPrimeB350M-A.ogg"},\
"video" : {"file" : "AigoICE400SE.mp4"},\
})

configs["episodes"].append(\
{ "title": "fan curves",\
"isChapter" : False,\
"audio" : {"timestamps" : ("04:47.9", "04:56.2"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "ASUS-PrimeB350m-A_BIOS_FanCurve_noTilt.mp4"},\
})

# with VRMs. Side by side with the B550
configs["episodes"].append(\
{ "title": "Conclusions",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:01.1"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "PrimeB350m-overview.MP4"},\
})


configs["episodes"].append(\
{ "title": "concl-pcie",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:08.4"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "PrimeB350m-slots.MP4"},\
})

configs["episodes"].append(\
{ "title": "concl-sata",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:17.1"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "PrimeB350m-SATA2_slightlybrighter.mp4"},\
})

configs["episodes"].append(\
{ "title": "holes are a tease",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:25.8"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "PrimeB350m-VRMs.MP4"},\
})

configs["episodes"].append(\
{ "title": "Wraith prism",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:30.1"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_WraithPrism.MP4"},\
})

configs["episodes"].append(\
{ "title": "used in a build",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:43.9"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "PC-David-overview_slightlybrighter.mp4"},\
})

configs["episodes"].append(\
{ "title": "wraiths",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:55.8"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "WraithPrism_Asus_Prime_B550M-K.MP4", "start" : "00:16"},\
})

configs["episodes"].append(\
{ "title": "motherboards to subscribe",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:05.5"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "MSI-B350mProVD-Plus-Overview.MP4"},\
})

configs["episodes"].append(\
{ "title": "Bye",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:15.7"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "PrimeB350m-overview.MP4"},\
})


# scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "USB"][0], configs)



scriptedvided.makeVideo(configs)

