import scriptedvided
import sv_ffutils

configs = { "defaultAudioFile" : "Asus-Tuf-X570-Gaming+WiFi.ogg",\
"mediaFolder" : "F:\\Videos\\Asus_TufX570_Gaming_WiFi", \
"stockFolder" : "F:\\Videos\\stock",\
"benchmarkFile" : "not needed",\
"outputFolder" : "F:\\Videos\\Asus_TufX570_Gaming_WiFi\\output", \
"outputFile" : "Asus-Tuf-X570-Gaming+WiFi.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "Best board that I sold", "until" : "The VRMs"}}, \
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

####################### intro ###############################

# this is the hook
#configs["episodes"].append(\
#{ "title": "A favorite of miners and gamers alike",\
#"audio" : {"timestamps" : ("09:37.3", "09:46" ), "volume" : 0.999, "padAudio" : 0.05 },\
#"video" : {"file" : ""},\
#})

configs["episodes"].append(\
{ "title": "Best board that I sold",\
"audio" : {"timestamps" : ("00:00", "" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "TufX570Gaming+Wifi_overview.MP4"},\
})

configs["episodes"].append(\
{ "title": "The VRMs",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), ""), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "TufX570Gaming+Wifi_VrmHeatsinks.MP4"},\
})

configs["episodes"].append(\
{ "title": "VRMs - core",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), ""), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "TufX570_VRM_Topology_bright.mp4"},\
"overlay" : { "image" : {"file" : "core_phases.png"} }, \
}) # add overlay

configs["episodes"].append(\
{ "title": "VRMs - soc",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), ""), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "TufX570_VRM_Topology_bright.mp4"},\
"overlay" : { "image" : {"file" : "soc_phases.png"} }, \
}) # add overlay

configs["episodes"].append(\
{ "title": "EPS",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), ""), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "TufX570Gaming+Wifi_VrmHeatsinks.MP4"},\
})

configs["episodes"].append(\
{ "title": "4 DIMM slots, 4 clips",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), ""), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "TufX570Gaming+Wifi_DIMMs.MP4"},\
})


configs["episodes"].append(\
{ "title": "Expansion slots, ports and headers",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), ""), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "TufX570Gaming+Wifi_slots.MP4"},\
})

configs["episodes"].append(\
{ "title": "plenty of room under the main x16",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), ""), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "M.2 slots maybe with arrow overlay",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), ""), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "SATA ports",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), ""), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "TufX570Gaming+Wifi_SataVsPcie_USB3.MP4"},\
}) # TufX570Gaming+Wifi_pins22.MP4


configs["episodes"].append(\
{ "title": "Debug LEDs",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), ""), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "TufX570Gaming+Wifi_pins3_DebugLeds.MP4"},\
})

configs["episodes"].append(\
{ "title": "Pin - audio",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), ""), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "TufX570Gaming+Wifi_pins.MP4"},\
})

configs["episodes"].append(\
{ "title": "Pin - usb2, fans, front panel, clear cmos",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), ""), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "TufX570Gaming+Wifi_pins2.MP4"},\
})

configs["episodes"].append(\
{ "title": "Pin USB3",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), ""), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "TufX570Gaming+Wifi_USB3.MP4"},\
})

configs["episodes"].append(\
{ "title": "Pin RGB",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), ""), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "TufX570Gaming+Wifi_pins4.MP4"},\
}) # TufX570Gaming+Wifi_pins3_DebugLeds.MP4

configs["episodes"].append(\
{ "title": "CPU fan pins",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), ""), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "TufX570Gaming+Wifi_SpiPins.MP4"},\
})

configs["episodes"].append(\
{ "title": "SPI header",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), ""), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "TufX570Gaming+Wifi_SpiPins.MP4"},\
})

# too long of a cut ...
configs["episodes"].append(\
{ "title": "Rear IO",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), ""), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "TufX570Gaming+Wifi_IO.MP4"},\
}) # maybe an overlay with the DVI-D to HDMI adapter?

# too long of a cut ...
configs["episodes"].append(\
{ "title": "with router antenna",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), ""), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "TufX570Gaming+Wifi_IO.MP4"},\
"isChapter" : False,\
}) # maybe an overlay with the DVI-D to HDMI adapter?

configs["episodes"].append(\
{ "title": "Audio introduction",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "Audio sample",\
"isChapter" : False,\
"audio" : {"timestamps" : ("03:07.7", "03:21.7" ), "volume" : 0.001, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

# EC spi chip first
configs["episodes"].append(\
{ "title": "The BIOS setup utility",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), ""), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "TufX570Gaming+WiFi_BiosEZ.MP4"},\
}) # list of bios

# maybe side by 
configs["episodes"].append(\
{ "title": "BIOS advanced, CPU freq",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), ""), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "TufX570Gaming+WiFi_BiosCpuFreq.MP4"},\
})

configs["episodes"].append(\
{ "title": "CPU voltage",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), ""), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "TufX570Gaming+WiFi_BiosCpuVoltage.MP4"},\
})

configs["episodes"].append(\
{ "title": "Mem profile - maybe both Easy and advanced",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), ""), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "TufX570Gaming+WiFi_Bios_DOCP.MP4"},\
})

configs["episodes"].append(\
{ "title": "Mem subtimings",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), ""), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "TufX570Gaming+WiFi_Bios_RamManual.MP4"},\
})

configs["episodes"].append(\
{ "title": "REBAR and TPM",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), ""), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "TufX570Gaming+WiFi_tpm-rebar.mp4", "start" : "00:08"},\
})

configs["episodes"].append(\
{ "title": "Fans types",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), ""), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "TufX570Gaming+WiFi_BiosFanTypes.MP4"},\
})

configs["episodes"].append(\
{ "title": "fan curve",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), ""), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "TufX570Gaming+WiFi_BiosFanProfilesAndCurve.MP4"},\
})

configs["episodes"].append(\
{ "title": "Tools - ezflash",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), ""), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "TufX570Gaming+WiFi_BiosUtilities.MP4"},\
})

configs["episodes"].append(\
{ "title": "Tools - oc profiles",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), ""), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "TufX570Gaming+WiFi_BiosUtilities.MP4"},\
})

configs["episodes"].append(\
{ "title": "Tools - AURA",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), ""), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "TufX570Gaming+WiFi_Bios_Aura.MP4"},\
})

# likes
configs["episodes"].append(\
{ "title": "Conclusions",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), ""), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "TufX570Gaming+Wifi_overview.MP4"},\
})

configs["episodes"].append(\
{ "title": "has wifi",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), ""), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "TufX570Gaming+Wifi_IO.MP4"},\
})

configs["episodes"].append(\
{ "title": "likes - vrm for 200W plus",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), ""), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "TufX570_VRM_Topology_bright.mp4"},\
})

configs["episodes"].append(\
{ "title": "but I do not use more than 100W",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), ""), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "r5_5600_3600.mp4"},\
})

configs["episodes"].append(\
{ "title": "HP Z230",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), ""), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Z230_front_barred.mp4"},\
})

configs["episodes"].append(\
{ "title": "I test old GPUs, B550 at most for me",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), ""), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_RX570_R9_270_GTX1050Ti_GT1030.MP4"},\
})

configs["episodes"].append(\
{ "title": "x570 is wasted on me",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), ""), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "TufX570Gaming+Wifi_overview.MP4"},\
})

configs["episodes"].append(\
{ "title": "other boards",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), ""), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B550m-DS3H-Overview.MP4"},\
})

configs["episodes"].append(\
{ "title": "Bye",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), ""), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "TufX570Gaming+Wifi_overview.MP4"},\
})

scriptedvided.makeVideo(configs)

