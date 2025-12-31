import scriptedvided
import sv_ffutils

configs = { "defaultAudioFile" : ". . . .ogg",\
"mediaFolder" : "F:\\Videos\\. . . ", \
"stockFolder" : "F:\\Videos\\stock",\
"benchmarkFile" : "not needed",\
"outputFolder" : "F:\\Videos\\. . . \\output", \
"outputFile" : "Asus_Prime_A320M-K.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "Back to budget boards", "until" : "The VRMs"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "The VRMs", "until" : "Audio from GA-A520M-DS3H"}}, \
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
"audio" : {"timestamps" : ("00:00", "00:14.2" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-A520M-DS3H_overall.MP4"},\
})

configs["episodes"].append(\
{ "title": "The VRMs",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:22"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-A520M-DS3H-V2_VRM.MP4"},\
})

configs["episodes"].append(\
{ "title": "VRMs - core",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:33.1"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-A520M-DS3H-V2_VRM2.MP4"},\
})

configs["episodes"].append(\
{ "title": "VRMs - soc",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:41.7"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-A520M-DS3H-V2_VRM.MP4"},\
})

configs["episodes"].append(\
{ "title": "Two DIMM slots, two clips",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:55.7"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-A520M-DS3H-V2_DIMM.MP4"},\
})

configs["episodes"].append(\
{ "title": "RAM removal",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:41.7"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-A520M-DS3H-V2_VRM.MP4"},\
})


configs["episodes"].append(\
{ "title": "Expansion slots, ports and headers",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:24.2"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-A520M-DS3H-V2_slots.MP4"},\
})

configs["episodes"].append(\
{ "title": "Decorative 1x slot",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:05.3"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-A520M-DS3H-V2_DimmDamaged.MP4"},\
})


configs["episodes"].append(\
{ "title": "M2 slot",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:33.7"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-A520M-DS3H-V2_slots.MP4"},\
})

configs["episodes"].append(\
{ "title": "SATA ports",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:45"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-A520M-DS3H_SATA.MP4"},\
})

configs["episodes"].append(\
{ "title": "Pin headers up to USB",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:06"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-A520M-DS3H-V2_Pins.MP4", "start" : "00:00"},\
})

configs["episodes"].append(\
{ "title": "Pin headers USBs, FP, Clear CMOS",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:25.3"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-A520M-DS3H-V2_Pins.MP4", "start" : "00:30"},\
})

configs["episodes"].append(\
{ "title": "Ambient LED",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:25.3"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-A520M-DS3H-V2_Pins.MP4", "start" : "00:30"},\
})

configs["episodes"].append(\
{ "title": "SPI programing port",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:25.3"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-A520M-DS3H-V2_Pins.MP4", "start" : "00:30"},\
})

# too long of a cut ...
configs["episodes"].append(\
{ "title": "Rear IO",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:01.8"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-A520M-DS3H-V2_IO.MP4"},\
}) # maybe an overlay with the DVI-D to HDMI adapter?


configs["episodes"].append(\
{ "title": "Audio from Prime-A320M-K",\
"isChapter" : False,\
"audio" : {"timestamps" : ("02:49.8", "03:01.8" ), "volume" : 0.001, "padAudio" : 0.05 },\
"video" : {"file" : "GA-A520M-DS3H_audioSample.mkv"},\
})

# EC spi chip first
configs["episodes"].append(\
{ "title": "The BIOS setup utility",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:10.1"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-A520m-DS3Hv2_BIOS_Easy.MP4"},\
}) # list of bios

configs["episodes"].append(\
{ "title": "BIOS advanced, No CPU freq",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:20.4"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-A520m-DS3Hv2_BIOS_NoCpuMultiplier.MP4"},\
})

configs["episodes"].append(\
{ "title": "CPU voltage",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:26.9"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-A520m-DS3Hv2_BIOS_CpuVoltage2.MP4"},\
})

configs["episodes"].append(\
{ "title": "Mem profile - maybe both Easy and advanced",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:38.6"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-A520m-DS3Hv2_BIOS_XMP2.MP4"},\
})

configs["episodes"].append(\
{ "title": "Mem subtimings",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:49.8"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-A520m-DS3Hv2_BIOS_Timings.MP4"},\
})

configs["episodes"].append(\
{ "title": "REBAR and TPM",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:01.4"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-A520m-DS3Hv2_BIOS_Tpm.MP4"},\
})

configs["episodes"].append(\
{ "title": "Fans types and fan curve",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:16.8"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-A520m-DS3Hv2_BIOS_FanType.MP4"},\
})

configs["episodes"].append(\
{ "title": "Save profiles",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:31.6"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-A520m-DS3Hv2_BIOS_FanProfiles.MP4"},\
})

# likes
configs["episodes"].append(\
{ "title": "Conclusions",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:37.7"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-A520M-DS3H_overall.MP4"},\
})

configs["episodes"].append(\
{ "title": "likes",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:43.2"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-A520M-DS3H_DIMMs.MP4"},\
})

configs["episodes"].append(\
{ "title": "good enough to connect parts",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:54.2"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-A520m-DS3Hv2_BIOS_Advanced.MP4"},\
})

configs["episodes"].append(\
{ "title": "Better budget boards",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:15.2"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Asus_Prime_A320m-k_overview.MP4"},\
})

configs["episodes"].append(\
{ "title": "Bye",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:20.6"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-A520M-DS3H-V2_overview.MP4"},\
})

scriptedvided.makeVideo(configs)

