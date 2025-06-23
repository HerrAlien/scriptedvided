import scriptedvided
import sv_ffutils

configs = { "defaultAudioFile" : "MSI-B350-Tomahawk.ogg",\
"mediaFolder" : "F:\\Videos\\B350 Tomahawk", \
"stockFolder" : "F:\\Videos\\stock",\
"benchmarkFile" : "not needed",\
"outputFolder" : "F:\\Videos\\B350 Tomahawk\\output", \
"outputFile" : "MSI-B350-Tomahawk.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "A sight for sore eyes", "until" : "The VRMs"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "The VRMs", "until" : "actual audio"}}, \
{"file" : "Ferco - Inquisitiveness.ogg", "timestamps" : ("01:01", None ), "destinationTimestamp" : {"title" : "The BIOS", "until" : "Conclusions"}}, \
{"file" : "Inspired - MaikonMusic  Free Background Music  Audio Library Release.mp3", "timestamps" : ("00:00", None ), "destinationTimestamp" : {"title" : "Conclusions", "until" : "EOF"}}, \
], "volume" : 0.05 },\
"episodes" : [],\
"youtube" : {"title" : "", \
"description" : '''I think I overpaid for this Asrock A320M-DVS.''',\
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
{ "title" : "A sight for sore eyes",\
"audio" : {"timestamps" : ("00:00", "00:11.5" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "B350_Tomahawk-LEDs.MP4", "start" : "00:25"},\
})

# this is for the heatsinks segment
configs["episodes"].append(\
{ "title" : "The VRMs",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:23.6" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "B350_VRM.MP4", "start" : "01:46"},\
})

configs["episodes"].append(\
{ "title" : "NB topology",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:37.5" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "MSI-B350-Tomahawk_VRMs.MP4", "file" : "01:00"},\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title" : "VCORE and SOC topology",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:51.4" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "MSI-B350-Tomahawk_VRMs.MP4", "file" : "01:50"},\
"isChapter" : False,\
})

# this might need a better shot, when filming the 2 slots GPU
configs["episodes"].append(\
{ "title" : "The DIMM slots",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:00" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "B350_unboxing_overview.MP4", "start" : "01:05"},\
})

# needs another BREEL?
configs["episodes"].append(\
{ "title" : "remove RAM comparisons",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:07.4" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})


configs["episodes"].append(\
{ "title" : "The expansion slots",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:22.1" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "B350_extensionSlots.MP4", "start" : "00:07"},\
})

# needs video
configs["episodes"].append(\
{ "title" : "M.2 slot",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:34" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "B350_extensionSlots.MP4", "start" : "00:00"},\
})


## maybe s[lit it at 01:40.9 ?
configs["episodes"].append(\
{ "title" : "PCI slots",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:53.3" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "B350_extensionSlots.MP4", "start" : "00:55"},\
})

configs["episodes"].append(\
{ "title" : "SATA ports",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:06.9" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "B350_secondUSB3.MP4", "start" : "00:12"},\
}) # maybe an overlay with the DVI-D to HDMI adapter?

configs["episodes"].append(\
{ "title" : "The pin headers",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:30.5" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "B350_pinHeaders.MP4", "start" : "00:41"},\
}) # audacity

configs["episodes"].append(\
{ "title" : "usb2 usb3 FP1 FP2",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:42.1" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "B350_pinHeaders.MP4", "start" : "01:15"},\
}) # rear IO, maybe?


# needs an arrow overlayed, pointing to the debug LEDs
configs["episodes"].append(\
{ "title" : "Debug LEDs",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:50" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "B350_unboxing_overview.MP4", "start" : "01:15"},\
}) # rear IO, maybe?

configs["episodes"].append(\
{ "title" : "clear cmos",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:56" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "B350_pinHeaders.MP4", "start" : "01:35"},\
}) # list of bios? or side by side BIOS and list of BIOS-es?

configs["episodes"].append(\
{ "title" : "ci tpm SPI header",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:04" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "B350_pinHeaders.MP4", "start" : "01:45"},\
}) # list of bios? or side by side BIOS and list of BIOS-es?

configs["episodes"].append(\
{ "title" : "CH341A",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:15.2" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "MSI-B450M-Pro-M2-V2_ReprogramBios.mp4"},\
}) # list of bios? or side by side BIOS and list of BIOS-es?

# must provide some overlays ...
configs["episodes"].append(\
{ "title" : "Rear IO",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:33.6" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "B350_IO.MP4"},\
})

# must provide some overlays ...
configs["episodes"].append(\
{ "title" : "LAN, USB3, USB-C",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:42.5" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "B350_IO.MP4"},\
})

# maybe a side by side here with GA-A320M-H
configs["episodes"].append(\
{ "title" : "The audio",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:53.4" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "B350_Tomahawk-LEDs.MP4"},\
})

configs["episodes"].append(\
{ "title" : "actual audio",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:00.6"), "volume" : 0.001, "padAudio" : 0.05 },\
"video" : {"file" : "B350_unboxing_overview.MP4"},\
})

configs["episodes"].append(\
{ "title" : "The BIOS",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:11.8" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "B350_Tomahawk_MFlash_rotated.mp4"},\
})

configs["episodes"].append(\
{ "title" : "CPU multiplier",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:23.8" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "B350_Tomahawk_CpuMultiplier_rotated.mp4"},\
})

configs["episodes"].append(\
{ "title" : "CPU voltage",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:39.5" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "B350_Tomahawk_CpuVoltage_rotated.mp4"},\
})

configs["episodes"].append(\
{ "title" : "DOCP",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:46.7" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "B350_Tomahawk_RamProfiles_rotated.mp4"},\
})

configs["episodes"].append(\
{ "title" : "ram timings",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:52" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "B350_Tomahawk_RamSubtimings_rotated.mp4"},\
})

# needs overlay
configs["episodes"].append(\
{ "title" : "overlay or better video fclock and gear ratio",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:00.2" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "B350_Tomahawk_FClock_GearRatio.mp4"},\
})

configs["episodes"].append(\
{ "title" : "Fan control",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:14.1" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "B350_Tomahawk_Fans2_rotated.mp4"},\
})

configs["episodes"].append(\
{ "title" : "Fan type could be better",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:26.7" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "B350_Tomahawk_FanTypes.mp4"},\
})

# maybe side by side programmer and programming ?
configs["episodes"].append(\
{ "title" : "TPM and REBAR",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:37.1" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "B350_Tomahawk_TpmRebar.mp4"},\
})

# conflicted
configs["episodes"].append(\
{ "title" : "Conclusions",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:52.9" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "B350_unboxing_overview.MP4", "start" : "00:47"},\
})

configs["episodes"].append(\
{ "title" : "conclusions vcore and heatsink",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:08" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "B350_VRM.MP4", "start" : "00:35"},\
})


configs["episodes"].append(\
{ "title" : "I like it",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:22.3" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "B350_Tomahawk-LEDs.MP4", "start" : "00:08"},\
})

configs["episodes"].append(\
{ "title" : "Bye",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:30" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "B350_unboxing_overview.MP4", "start" : "01:05"},\
})

scriptedvided.makeVideo(configs)

