import scriptedvided
import sv_ffutils

configs = { "defaultAudioFile" : "Asus Prime A320M-K.ogg",\
"mediaFolder" : "F:\\Videos\\ASUS_Prime_A320M-K", \
"stockFolder" : "F:\\Videos\\stock",\
"benchmarkFile" : "not needed",\
"outputFolder" : "F:\\Videos\\ASUS_Prime_A320M-K\\output", \
"outputFile" : "Asus_Prime_A320M-K.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "Hungry for more", "until" : "The VRMs"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "The VRMs", "until" : "Audio from Prime-A320M-K"}}, \
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
{ "title": "Hungry for more",\
"audio" : {"timestamps" : ("00:00", "00:14.5" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Asus_Prime_A320m-k_bowing.MP4", "start" : "00:00"},\
})

configs["episodes"].append(\
{ "title": "The VRMs",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:17.6"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Asus_Prime_A320m-k_VRM.MP4"},\
})

configs["episodes"].append(\
{ "title": "VRMs - core",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:24.1"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Asus_Prime_A320m-k_VrmCore.MP4"},\
})

configs["episodes"].append(\
{ "title": "VRMs - soc",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:29"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Asus_Prime_A320m-k_VrmSoc.MP4"},\
})

configs["episodes"].append(\
{ "title": "VRMs - coils",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:37.5"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Asus_Prime_A320m-k_VRM.MP4"},\
})

configs["episodes"].append(\
{ "title": "Two DIMM slots, two clips",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:45.7"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Asus_Prime_A320m-k_DIMMs.MP4"},\
})

configs["episodes"].append(\
{ "title": "RAM removal",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:51.7"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Asrock_A320M-DVS_RamInsertionRemoval.MP4", "start" : "00:23"},\
})


configs["episodes"].append(\
{ "title": "Expansion slots, ports and headers",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:59.7"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Asus_Prime_A320m-k_Slots.MP4"},\
})

configs["episodes"].append(\
{ "title": "Decorative 1x slot",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:13.2"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-A320M-H_Pcie1xVs2SlotCard.MP4", "start" : "00:15"},\
})


configs["episodes"].append(\
{ "title": "M2 slot",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:27.2"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Asus_Prime_A320m-k_Slots.MP4"},\
})

configs["episodes"].append(\
{ "title": "SATA ports",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:36.9"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Asus_Prime_A320m-k_SATA.MP4"},\
})

configs["episodes"].append(\
{ "title": "Pin - audio",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:48.9"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Asus_Prime_A320m-k_pins.MP4"},\
})

configs["episodes"].append(\
{ "title": "Pin - tpm",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:58.3"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Asus_Prime_A320m-k_pins.MP4"},\
})

configs["episodes"].append(\
{ "title": "Pin - weird",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:05.1"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Asus_Prime_A320m-k_pins.MP4"},\
})

configs["episodes"].append(\
{ "title": "Pin headers USBs, FP, Clear CMOS",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:17"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Asus_Prime_A320m-k_pins2.MP4"},\
})

configs["episodes"].append(\
{ "title": "Ambient LED",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:28.2"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Asus_Prime_A320m-k_overview.MP4"},\
})

configs["episodes"].append(\
{ "title": "SPI programing port",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:44.9"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Asus_Prime_A320m-k_pinsSPI.MP4"},\
})

# too long of a cut ...
configs["episodes"].append(\
{ "title": "Rear IO",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:13.2"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Asus_Prime_A320m-k_IO.MP4"},\
}) # maybe an overlay with the DVI-D to HDMI adapter?


configs["episodes"].append(\
{ "title": "Audio from Prime-A320M-K",\
"isChapter" : False,\
"audio" : {"timestamps" : ("03:00.2", "03:13.2" ), "volume" : 0.001, "padAudio" : 0.05 },\
"video" : {"file" : "Prime_A320M-K_Audio.mkv"},\
})

# EC spi chip first
configs["episodes"].append(\
{ "title": "The BIOS setup utility",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:22"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Asus_Prime_A320m-k_BIOS_EZ.MP4"},\
}) # list of bios

# maybe side by 
configs["episodes"].append(\
{ "title": "BIOS advanced, No CPU freq, unlike GA-A320M-H",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:40"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Asus_Prime_A320m-k_BIOS_NoOverclock.MP4"},\
})

configs["episodes"].append(\
{ "title": "CPU voltage",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:53.3"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Asus_Prime_A320m-k_BIOS_VCORE.MP4"},\
})

configs["episodes"].append(\
{ "title": "Mem profile - maybe both Easy and advanced",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:01.5"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Asus_Prime_A320m-k_BIOS_XMP.MP4"},\
})

configs["episodes"].append(\
{ "title": "Mem subtimings",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:15.2"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Asus_Prime_A320m-k_BIOS_RamTimings.MP4"},\
})

configs["episodes"].append(\
{ "title": "REBAR and TPM",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:23.3"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Asus_Prime_A320m-k_BIOS_REBAR.MP4"},\
})

configs["episodes"].append(\
{ "title": "Fans types and fan curve",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:39"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Asus_Prime_A320m-k_FanType.MP4"},\
})

configs["episodes"].append(\
{ "title": "Save profiles",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:54.2"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Asus_Prime_A320m-k_BIOS_OverclockProfile.MP4"},\
})

# likes
configs["episodes"].append(\
{ "title": "Conclusions",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:09.2"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Asus_Prime_A320m-k_VRM.MP4"},\
})

configs["episodes"].append(\
{ "title": "likes",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:17"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Asus_Prime_A320m-k_Slots.MP4"},\
})

configs["episodes"].append(\
{ "title": "good enough to connect parts",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:28.7"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Asus_Prime_A320m-k_overview.MP4"},\
})

configs["episodes"].append(\
{ "title": "Better budget boards",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:35"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "A320M_Grenade_overview.MP4", "start" : "00:48"},\
})

configs["episodes"].append(\
{ "title": "Bye",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:40.8"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Asus_Prime_A320m-k_overview.MP4"},\
})

scriptedvided.makeVideo(configs)

