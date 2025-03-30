import scriptedvided
import sv_ffutils

configs = { "defaultAudioFile" : "....ogg",\
"mediaFolder" : "F:\\Videos\\...", \
"stockFolder" : "F:\\Videos\\stock",\
"benchmarkFile" : "not needed",\
"outputFolder" : "F:\\Videos\\...\\output", \
"outputFile" : "MSI-A320M-Grenade.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "A good looking board", "until" : "The VRMs"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "The VRMs", "until" : "The audio - a bit meh"}}, \
{"file" : "Ferco - Inquisitiveness.ogg", "timestamps" : ("01:01", None ), "destinationTimestamp" : {"title" : "Audio wrapup", "until" : "Conclusions"}}, \
{"file" : "Inspired - MaikonMusic  Free Background Music  Audio Library Release.mp3", "timestamps" : ("00:00", None ), "destinationTimestamp" : {"title" : "Conclusions", "until" : "EOF"}}, \
], "volume" : 0.05 },\
"episodes" : [],\
"youtube" : {"title" : "", \
"description" : ''' A320M does not mean a chea board, and the MSI A320M Grenade is here to prove it. ''',\
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
{ "title": "A good looking board",\
"audio" : {"timestamps" : ("00:00", "00:10.1" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "A320M_Grenade_overview.MP4"},\
})

configs["episodes"].append(\
{ "title": "BIOS not that great",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:17.8" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Grenade_and_A320M-H.mp4"},\
})

configs["episodes"].append(\
{ "title": "The VRMs",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:36.3" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "A320M_Grenade_PowerDelivery.mp4"},\
})

configs["episodes"].append(\
{ "title": "VRM has a heatsink",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:46.7" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "A320_Grenade-LEDs.MP4"},\
})

# this might need a better shot, when filming the 2 slots GPU
configs["episodes"].append(\
{ "title": "DIMMs, also just two of them",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:55.5" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "A320M_Grenade_overview.MP4"},\
})

configs["episodes"].append(\
{ "title": "Expansion slots, ports and headers",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:16" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "A320M_Grenade_expansionSlots.MP4"},\
})

# needs video
configs["episodes"].append(\
{ "title": "PCIEx1 vs GTX970",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:21.6" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "M2 slot",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:30" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "A320M_Grenade_expansionSlots.MP4"},\
})

configs["episodes"].append(\
{ "title": "SATA",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:38.2" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "A320M_Grenade_SATA.MP4"},\
})

#needs video
configs["episodes"].append(\
{ "title": "SATA vs GTX970",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:48.8" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "Pin headers 1",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:06.8" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "A320M_Grenade_pinHeader1.mp4"},\
})

configs["episodes"].append(\
{ "title": "Pin headers 2",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:27" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "A320M_Grenade_pinHeader2.mp4"},\
})

configs["episodes"].append(\
{ "title": "Rear IO",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:51.4" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "A320M_Grenade_IO.mp4"},\
}) # maybe an overlay with the DVI-D to HDMI adapter?

configs["episodes"].append(\
{ "title": "Rear IO - audio",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:56.8" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
}) # audacity

configs["episodes"].append(\
{ "title": "The audio - a bit meh",\
"audio" : {"timestamps" : ("00:00", "" ), "volume" : 0.001, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
}) # audacity

configs["episodes"].append(\
{ "title": "Audio wrapup",\
"isChapter" : False,\
"audio" : {"timestamps" : ("02:56.8", "03:03.5" ), "volume" : 0.001, "padAudio" : 0.05 },\
"video" : {"file" : "A320M_Grenade_IO.mp4"},\
}) # rear IO, maybe?

configs["episodes"].append(\
{ "title": "The BIOS setup utility",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:09.9" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "A320M-Grenade_BIOS_CpuNoOC_cropped.mp4"},\
}) # list of bios? or side by side BIOS and list of BIOS-es?

configs["episodes"].append(\
{ "title": "Mem profile",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:16.8" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "A320M-Grenade_BIOS_RAM_cropped.mp4"},\
})

configs["episodes"].append(\
{ "title": "CPU voltage",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:40.8" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "A320M-Grenade_BIOS_CpuVoltage_cropped.mp4"},\
})

# maybe a side by side here with GA-A320M-H
configs["episodes"].append(\
{ "title": "CPU frequency - nope",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:56.3" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "A320M-Grenade_BIOS_CpuNoOC_cropped.mp4"},\
})

configs["episodes"].append(\
{ "title": "OC profiles",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:09.8" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "A320M-Grenade_BIOS_OcProfilesToUSB_cropped.mp4"},\
})

configs["episodes"].append(\
{ "title": "Fans profiles",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:19.6" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "A320M-Grenade_BIOS_Fans_cropped.mp4"},\
})

configs["episodes"].append(\
{ "title": "Fans profiles - GA better",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:24" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Grenade_and_A320M-H_fans.mp4"},\
})


configs["episodes"].append(\
{ "title": "REBAR and TPM",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:34.4" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Grenade_RebarAndTpm.mp4"},\
})


configs["episodes"].append(\
{ "title": "Conclusions",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:47.6" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "A320_Grenade-LEDs.MP4"},\
})

configs["episodes"].append(\
{ "title": "bad BIOS circuitry",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:03.5" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "bad BIOS circuitry 2",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:13.9" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

# maybe side by side programmer and programming ?
configs["episodes"].append(\
{ "title": "reprogramming",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:28.7" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "Back to breel",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:53.6" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "A320M_Grenade_overview.MP4"},\
})

configs["episodes"].append(\
{ "title": "Asrock A320M-DVS",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:00" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Asrock_A320M-DVS-overview.MP4"},\
})

configs["episodes"].append(\
{ "title": "Bye",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:06" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "A320M_Grenade_overview.MP4"},\
})

scriptedvided.makeVideo(configs)

