import scriptedvided
import sv_ffutils

configs = { "defaultAudioFile" : "GA-B450M-DS3H.ogg",\
"mediaFolder" : "F:\\Videos\\GA-B450M-DS3H_v2", \
"stockFolder" : "F:\\Videos\\stock",\
"benchmarkFile" : "not needed",\
"outputFolder" : "F:\\Videos\\GA-B450M-DS3H_v2\\output", \
"outputFile" : "GA-B450M-DS3H_v2.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "Is this a good budget B450 board", "until" : "The VRMs"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "The VRMs", "until" : "Audio from GA-B450M-DS3H"}}, \
{"file" : "Ferco - Inquisitiveness.ogg", "timestamps" : ("01:01", None ), "destinationTimestamp" : {"title" : "The BIOS setup utility", "until" : "Conclusions"}}, \
{"file" : "Inspired - MaikonMusic  Free Background Music  Audio Library Release.mp3", "timestamps" : ("00:00", None ), "destinationTimestamp" : {"title" : "Conclusions", "until" : "EOF"}}, \
], "volume" : 0.05 },\
"episodes" : [],\
"youtube" : {"title" : "", \
"description" : ''' Is this B450M-DS3H v2 better than another Gigabyte board we reviewed earlier? ''',\
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
{ "title": "Is this a good budget B450 board",\
"audio" : {"timestamps" : ("00:00", "00:08.5" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B450M-DS3H_overview.MP4"},\
})

configs["episodes"].append(\
{ "title": "The VRMs",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:20.7" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B450M-DS3H_VrmHeatsinks.MP4"},\
})

configs["episodes"].append(\
{ "title": "VRMs - no heatsink",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:24.5" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B450M-DS3H_ShowAllPhases.MP4"},\
})

configs["episodes"].append(\
{ "title": "VRMs - core",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:30.8" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B450M-DS3H_CorePhases.MP4"},\
})

configs["episodes"].append(\
{ "title": "VRMs - SOC",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:35.9" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B450M-DS3H_SocPhases.MP4"},\
})

configs["episodes"].append(\
{ "title": "VRMs - conclusion",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:44.2" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B450M-DS3H_VrmHeatsinks.MP4"},\
})

configs["episodes"].append(\
{ "title": "DIMM slots, four of them",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:58.2" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B450M-DS3H_DIMMs.MP4"},\
})

configs["episodes"].append(\
{ "title": "Expansion slots, ports and headers",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:07.7" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B450M-DS3H_slots.MP4"},\
})

configs["episodes"].append(\
{ "title": "PCIEx1 vs RX580",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:15.3" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-A320M-H_Pcie1xVs2SlotCard.MP4"},\
})

configs["episodes"].append(\
{ "title": "PCIEx4",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:27.3" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B450M-DS3H_slots_PcieX4.mp4"},\
})

configs["episodes"].append(\
{ "title": "M2 slot",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:38.4" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B450M-DS3H_slots_M2.mp4"},\
})

configs["episodes"].append(\
{ "title": "SATA ports",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:44.75" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B450M-DS3H_SATA.MP4"},\
})

configs["episodes"].append(\
{ "title": "SATA vs RX580",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:51.7" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-A320M-H_SataVs2SlotCard.MP4"},\
})

configs["episodes"].append(\
{ "title": "Pin headers 1",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:08.1" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B450M-DS3H_pins.MP4"},\
})

configs["episodes"].append(\
{ "title": "Pin headers 2",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:24.7" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B450M-DS3H_pins2.MP4"},\
})

configs["episodes"].append(\
{ "title": "Pin headers RGB",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:34" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B450M-DS3H_PinsCpuLed.MP4"},\
})

# too long of a cut ...
configs["episodes"].append(\
{ "title": "Rear IO",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:52" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B450M-DS3H_IoPs2.mp4"},\
}) # maybe an overlay with the DVI-D to HDMI adapter?

configs["episodes"].append(\
{ "title": "Rear IO 2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:04.9" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B450M-DS3H_IO2.MP4"},\
"isChapter" : False,\
}) # maybe an overlay with the DVI-D to HDMI adapter?

configs["episodes"].append(\
{ "title": "The audio ... oh, the audio.",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:19.7" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B450M-DS3H_audioIntro.mp4"},\
}) # maybe use a muted video of Audacity

configs["episodes"].append(\
{ "title": "Audio from GA-B450M-DS3H",\
"isChapter" : False,\
"audio" : {"timestamps" : ("03:05.7", "03:19.7" ), "volume" : 0.001, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B450M-DS3H_audioSample.mkv"},\
})

configs["episodes"].append(\
{ "title": "The BIOS setup utility",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:26.55" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B450m-DS3Hv2_BIOS_easy.MP4"},\
}) # list of bios

configs["episodes"].append(\
{ "title": "BIOS advanced, CPU freq",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:40.2" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B450m-DS3Hv2_BIOS_CpuMultiplier.MP4"},\
})

configs["episodes"].append(\
{ "title": "CPU voltage",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:51.1" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B450m-DS3Hv2_BIOS_CpuVoltage.MP4"},\
})

configs["episodes"].append(\
{ "title": "Mem profile",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:59.2" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B450m-DS3Hv2_BIOS_Xmp.MP4"},\
})

configs["episodes"].append(\
{ "title": "Mem subtimings",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:08.9" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B450m-DS3Hv2_BIOS_MemTimings.MP4"},\
})

configs["episodes"].append(\
{ "title": "REBAR and TPM",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:25.1" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B450m-DS3Hv2_BIOS_tpm_rebar.mp4"},\
})

configs["episodes"].append(\
{ "title": "Fans types",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:41.1" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B450m-DS3Hv2_BIOS_FanType.MP4"},\
})

configs["episodes"].append(\
{ "title": "Fans curve",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:51.9" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B450m-DS3Hv2_BIOS_FanCurve.MP4"},\
})

configs["episodes"].append(\
{ "title": "RGB fusion",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:07.2" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B450m-DS3Hv2_BIOS_Rgb1.MP4"},\
})

configs["episodes"].append(\
{ "title": "Conclusions",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:15.9" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B450M-DS3H_overview.MP4"},\ 
})

configs["episodes"].append(\
{ "title": "Do not try an R9 in it",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:22.7" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B450M-DS3H_notR9.mkv"},\
})

configs["episodes"].append(\
{ "title": "Good DIMM slots",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:32.4" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B450M-DS3H_overview.MP4"},\
})

configs["episodes"].append(\
{ "title": "Dislikes",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:43.9" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "audio clip video"},\
})

configs["episodes"].append(\
{ "title": "Pricing",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:02.6" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B450M-DS3H_OLX.mkv"},\
})

configs["episodes"].append(\
{ "title": "Better boards, worse boards",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:11.7" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA_AM4_boards_better_worse.mp4"},\
})

configs["episodes"].append(\
{ "title": "Bye",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:19" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GA-B450M-DS3H_overview.MP4"},\
})

scriptedvided.makeVideo(configs)

