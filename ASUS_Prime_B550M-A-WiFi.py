import scriptedvided
import sv_ffutils

configs = { "defaultAudioFile" : "Asus-Prime-B550M-A-Wifi.ogg",\
"mediaFolder" : "F:\\Videos\\ASUS_Prime_B550M-A-WiFi", \
"stockFolder" : "F:\\Videos\\stock",\
"benchmarkFile" : "not needed",\
"outputFolder" : "F:\\Videos\\ASUS_Prime_B550M-A-WiFi\\output", \
"outputFile" : "ASUS_Prime_B550M-A-WiFi.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "Hungry for more", "until" : "The VRMs"}}, \
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
#"video" : {"file" : " "},\
#})

configs["episodes"].append(\
{ "title": "Better than most",\
"audio" : {"timestamps" : ("00:00", "00:23.9" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "PrimeB550-A_WiFi_Overview_bright.mp4"},\
})

configs["episodes"].append(\
{ "title": "The VRMs",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:37.6"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "PrimeB550-A_WiFi_VRM_Heatsink_bright.mp4"},\
})

configs["episodes"].append(\
{ "title": "VRMs - core",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:44.7"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "PrimeB550-A_WiFi_VRM_Core_bright.mp4"},\
})

configs["episodes"].append(\
{ "title": "VRMs - soc",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:00"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "PrimeB550-A_WiFi_VRM_SOC_bright.mp4"},\
})

configs["episodes"].append(\
{ "title": "4 DIMM slots, 4 clips",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:09.7"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "PrimeB550-A_WiFi_DIMMs_bright.mp4"},\
})


configs["episodes"].append(\
{ "title": "Expansion slots, ports and headers",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:28.8"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "PrimeB550-A_WiFi_Slots_bright.mp4"},\
})

configs["episodes"].append(\
{ "title": "Useful 1x slot",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:37"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "PrimeB550-A_WiFi_Slots_bright.mp4"},\
})


configs["episodes"].append(\
{ "title": "Decorative PCIEx1 slot",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:46.7"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "PrimeB550-A_WiFi_Slots_bright.mp4"},\
})

configs["episodes"].append(\
{ "title": "SATA ports",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:57.7"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "PrimeB550-A_WiFi_Pins_USB2_FP_SATA_bright.mp4"},\
})

configs["episodes"].append(\
{ "title": "Pin - audio",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:08.2"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "PrimeB550-A_WiFi_Pins_bright.mp4"},\
})

configs["episodes"].append(\
{ "title": "Pin - argb",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:15.5"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "PrimeB550-A_WiFi_RGB_USB2_bright.mp4"},\
})

configs["episodes"].append(\
{ "title": "Pin - clear cmos",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:23.7"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "PrimeB550-A_WiFi_PinsClearRTC_bright.mp4"},\
})

configs["episodes"].append(\
{ "title": "Pin USB3",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:35.2"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "PrimeB550-A_WiFi_PinsUsb3_bright.mp4"},\
})

configs["episodes"].append(\
{ "title": "Pin RGB",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:44.7"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "PrimeB550-A_WiFi_Pins_Rgb_bright.mp4"},\
})

configs["episodes"].append(\
{ "title": "Pin TPM SPI",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:55.7"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "PrimeB550-A_WiFi_Pins_Tpm_bright.mp4"},\
})

# too long of a cut ...
configs["episodes"].append(\
{ "title": "Rear IO",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:18.3"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "PrimeB550-A_WiFi_IO_bright.mp4"},\
}) # maybe an overlay with the DVI-D to HDMI adapter?

configs["episodes"].append(\
{ "title": "Audio introduction",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:21.7" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Prime_B550m-a-WiFi_audio.mkv"},\
})

configs["episodes"].append(\
{ "title": "Audio sample",\
"isChapter" : False,\
"audio" : {"timestamps" : ("03:07.7", "03:21.7" ), "volume" : 0.001, "padAudio" : 0.05 },\
"video" : {"file" : "Prime_B550m-a-WiFi_audio.mkv"},\
})

# EC spi chip first
configs["episodes"].append(\
{ "title": "The BIOS setup utility",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:31.6"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "PrimeB550M-A_WiFi_BiosEz.MP4"},\
}) # list of bios

# maybe side by 
configs["episodes"].append(\
{ "title": "BIOS advanced, CPU freq",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:43.5"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "PrimeB550M-A_WiFi_BIOS_CpuFreq.MP4"},\
})

configs["episodes"].append(\
{ "title": "CPU voltage",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:02.9"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "PrimeB550M-A_WiFi_BIOS_CpuCoreVoltage.MP4"},\
})

configs["episodes"].append(\
{ "title": "Mem profile - maybe both Easy and advanced",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:09.6"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "PrimeB550M-A_WiFi_BIOS_DOCP.MP4"},\
})

configs["episodes"].append(\
{ "title": "Mem subtimings",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:20.1"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "PrimeB550M-A_WiFi_BIOS_RamManual.MP4"},\
})

configs["episodes"].append(\
{ "title": "REBAR and TPM",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:28.2"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Prime_B550m-a-wifi-tpm-rebar.mp4"},\
})

configs["episodes"].append(\
{ "title": "Fans types",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:45.2"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "PrimeB550M-A_WiFi_BIOS_FanTypeAndCurve.MP4" , "start" : "00:11"},\
})

configs["episodes"].append(\
{ "title": "fan curve",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:51.6"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "PrimeB550M-A_WiFi_BIOS_FanCurveEditor.MP4"},\
})

configs["episodes"].append(\
{ "title": "Tools",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:00.7"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "PrimeB550M-A_WiFi_BIOS_Tools.MP4"},\
})

# likes
configs["episodes"].append(\
{ "title": "Conclusions",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:09.8"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "PrimeB550-A_WiFi_Overview_bright.mp4"},\
})

configs["episodes"].append(\
{ "title": "likes - heatsink",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:14.8"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "PrimeB550-A_WiFi_VRM_Heatsink_bright.mp4"},\
})

configs["episodes"].append(\
{ "title": "likes - audio",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:16.8"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Prime_B550m-a-WiFi_audio.mkv"},\
})

configs["episodes"].append(\
{ "title": "likes - SATA and M2",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:20.9"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "PrimeB550-A_WiFi_Slots_bright.mp4"},\
})

configs["episodes"].append(\
{ "title": "dislikes",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:29.8"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "PrimeB550M-A_WiFi_BIOS_FanTypeAndCurve.MP4"},\
})

configs["episodes"].append(\
{ "title": "pretty good though",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:47.3"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "PrimeB550-A_WiFi_Overview_bright.mp4"},\
})

configs["episodes"].append(\
{ "title": "other boards",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:55"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "TufX570Gaming+Wifi_overview.MP4"},\
})

configs["episodes"].append(\
{ "title": "Bye",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:03.9"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "PrimeB550-A_WiFi_Overview_bright.mp4"},\
})

scriptedvided.makeVideo(configs)

