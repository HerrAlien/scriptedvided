import scriptedvided
import sv_ffutils

configs = { "defaultAudioFile" : "GA-A320M-H.ogg",\
"mediaFolder" : "F:\\Videos\\GA-A320M-H", \
"stockFolder" : "F:\\Videos\\stock",\
"benchmarkFile" : "not needed",\
"outputFolder" : "F:\\Videos\\GA-A320M-H\\output", \
"outputFile" : "GA-A320M-H.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "Budget boards are legion", "until" : "The VRMs"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "The VRMs", "until" : "Rear IO"}}, \
{"file" : "Ferco - Lake Of The Honesty.ogg", "timestamps" : ("00:30", None ), "destinationTimestamp" : {"title" : "Rear IO", "until" : "The BIOS setup utility"}}, \
{"file" : "Ferco - Inquisitiveness.ogg", "timestamps" : ("01:01", None ), "destinationTimestamp" : {"title" : "The BIOS setup utility", "until" : "Conclusions"}}, \
{"file" : "Inspired - MaikonMusic  Free Background Music  Audio Library Release.mp3", "timestamps" : ("00:00", None ), "destinationTimestamp" : {"title" : "Conclusions", "until" : "EOF"}}, \
], "volume" : 0.05 },\
"episodes" : [],\
"youtube" : {"title" : "", \
"description" : ''' Taking a closer look at a budget AM4 motherboard, the Gigabyte GA-A320M-H. ''',\
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
#"video" : {"file" : "rx580_ethereumDust.mp4", "start" : "00:00"},\
#})

configs["episodes"].append(\
{ "title": "Budget boards are legion",\
"audio" : {"timestamps" : ("00:00", "00:15.3" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-A320M-H_Overview.MP4"},\
})

configs["episodes"].append(\
{ "title": "A budget board",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:23.6" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-A320M-H_RamSlots.MP4", "start" : "00:07"},\
})

configs["episodes"].append(\
{ "title": "The VRMs",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:51" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-A320M-H_VRMs.MP4"},\
})

configs["episodes"].append(\
{ "title": "VRMs - caution",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:01.8" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "B450-Pro-M2-V2_MosfetRemoved.mp4"},\
})

configs["episodes"].append(\
{ "title": "DIMMs, only two of them",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:10.2" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-A320M-H_RamSlots.MP4"},\
})

configs["episodes"].append(\
{ "title": "DIMMs - Asrock",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:20.4" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Asrock_A320M-DVS_memorySlots.MP4"},\
})

configs["episodes"].append(\
{ "title": "Expansion slots, ports and headers",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:32.5" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-A320M-H_ExpansionSlots.MP4"},\
})

configs["episodes"].append(\
{ "title": "PCIEx1 vs RX580",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:41.8" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-A320M-H_Pcie1xVs2SlotCard.MP4"},\
})

configs["episodes"].append(\
{ "title": "SATA vs RX580",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:01.9" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Asrock_A320M-DVS_SataVs2SlotCard.MP4"},\
})

configs["episodes"].append(\
{ "title": "M2 slot",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:12.6" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-A320M-H_ExpansionSlots.MP4"},\
})

configs["episodes"].append(\
{ "title": "Pin headers 1",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:20.6" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-A320M-H_PinHeaders1.MP4"},\
})

configs["episodes"].append(\
{ "title": "Pin headers 2",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:25.5" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-A320M-H_PinHeareds2.MP4"},\
})

configs["episodes"].append(\
{ "title": "Rear IO",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:38.3" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-A320M-H_RearIO.MP4"},\
}) # maybe an overlay with the DVI-D to HDMI adapter?

configs["episodes"].append(\
{ "title": "Rear IO - video",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:53.5" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-A320M-H_RearIO.MP4"},\
"overlay" : { \
    "image" : {"file" : "dvi-to-hdmi.png", "chromaColor" : "0x00FF00"}\
}, \
}) # maybe have it condensed with above

configs["episodes"].append(\
{ "title": "Rear IO - audio",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:01.4" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-A320M-H_RearIO.MP4"},\
}) # maybe have it condensed with above

configs["episodes"].append(\
{ "title": "The audio ... oh, the audio.",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:16.3" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-A320M-H-audioTest30dBPreamp.mkv"},\
}) # maybe use a muted video of Audacity

configs["episodes"].append(\
{ "title": "Audio from GA-A320M-H",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:04", "00:22" ), "volume" : 0.001, "padAudio" : 0.05 },\
"video" : {"file" : "GA-A320M-H-audioTestNoPreamp.mkv", "start" : "00:04"},\
})

configs["episodes"].append(\
{ "title": "Mic boost video",\
"isChapter" : False,\
"audio" : {"timestamps" : ("03:16.3", "03:21.3" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "micBoost_start-00-20.mkv", "start" : "00:22"},\
})

configs["episodes"].append(\
{ "title": "Boosted Audio",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:02", "00:18" ), "volume" : 0.001, "padAudio" : 0.05 },\
"video" : {"file" : "GA-A320M-H-audioTest30dBPreamp.mkv", "start" : "00:02"},\
})

configs["episodes"].append(\
{ "title": "Z230",\
"isChapter" : False,\
"audio" : {"timestamps" : ("03:21.3", "03:28.9" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Z230_audio.mkv"},\
})

configs["episodes"].append(\
{ "title": "Z230 Audio",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:02", "00:12" ), "volume" : 0.001, "padAudio" : 0.05 },\
"video" : {"file" : "Z230_audio.mkv", "start" : "00:02"},\
})

configs["episodes"].append(\
{ "title": "video of Z230 audio with settings",\
"isChapter" : False,\
"audio" : {"timestamps" : ("03:28.9", "03:37.2" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Z230_audio.mkv"},\
})

configs["episodes"].append(\
{ "title": "The BIOS setup utility",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:55.1" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-A320M-H_BiosSupport.mkv"},\
}) # list of bios

configs["episodes"].append(\
{ "title": "CPU compatinility",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:02.8" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-A320M-H_CpuCompat.mkv"},\
})

configs["episodes"].append(\
{ "title": "CPU frequency",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:15" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-A320M-H_Bios_CpuFrequency.mp4", "start" : "00:10"},\
})

configs["episodes"].append(\
{ "title": "CPU voltage",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:30.9" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-A320M-H_Bios_CpuVoltage.mp4", "start" : "00:03"},\
})

configs["episodes"].append(\
{ "title": "Mem profile",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:38.8" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-A320M-H_Bios_RAM.mp4", "start" : "00:02"},\
})

configs["episodes"].append(\
{ "title": "Mem subtimings",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:45.3" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-A320M-H_Bios_RAM.mp4", "start" : "00:20"},\
})

configs["episodes"].append(\
{ "title": "REBAR",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:58" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-A320M-H_Bios_REBAR.mp4"},\
})

configs["episodes"].append(\
{ "title": "Fans profiles",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:21.2" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-A320M-H_Bios_Fans.mp4"},\
})

configs["episodes"].append(\
{ "title": "Conclusions",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:45.9" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-A320M-H_Overview.MP4"},\
})

configs["episodes"].append(\
{ "title": "Pricing",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:54.5" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-A320M-H_Olx.mkv"},\
})

configs["episodes"].append(\
{ "title": "Back to breel",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:02.2" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-A320M-H_Overview.MP4"},\
})

configs["episodes"].append(\
{ "title": "Boards with better VRM, or worse RAM slots",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:18" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "A320M_Grenade_overview.MP4"},\
})

configs["episodes"].append(\
{ "title": "Bye",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:24" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-A320M-H_Overview.MP4"},\
})

scriptedvided.makeVideo(configs)

