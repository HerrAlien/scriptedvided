import scriptedvided
import sv_ffutils

configs = { "defaultAudioFile" : "Asrock-A320M-DVS.ogg",\
"mediaFolder" : "F:\\Videos\\Asrock-A320M-DVS", \
"stockFolder" : "F:\\Videos\\stock",\
"benchmarkFile" : "not needed",\
"outputFolder" : "F:\\Videos\\Asrock-A320M-DVS\\output", \
"outputFile" : "Asrock-A320M-DVS.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "Fine distilled garboleum", "until" : "The VRMs"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "The VRMs", "until" : "actual audio"}}, \
{"file" : "Ferco - Inquisitiveness.ogg", "timestamps" : ("01:01", None ), "destinationTimestamp" : {"title" : "The BIOS", "until" : "Conclusions"}}, \
{"file" : "Inspired - MaikonMusic  Free Background Music  Audio Library Release.mp3", "timestamps" : ("00:00", None ), "destinationTimestamp" : {"title" : "Conclusions", "until" : "pricing - bought as deffective"}}, \
{"file" : "Inspired - MaikonMusic  Free Background Music  Audio Library Release.mp3", "timestamps" : ("00:00", None ), "destinationTimestamp" : {"title" : "pricing - bought as deffective", "until" : "EOF"}}, \
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
{ "title" : "Fine distilled garboleum",\
"audio" : {"timestamps" : ("00:00", "00:12.7" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Asrock_A320M-DVS-overview.MP4"},\
})

#some side by side breels?
configs["episodes"].append(\
{ "title" : "Costs me most",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:26.9" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "A320m-dvs_olx_deffective.mkv"},\
})

configs["episodes"].append(\
{ "title" : "The VRMs",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:38.3" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Asrock_A320M-DVS-overview.MP4"},\
})

# maybe overlay on mosfets
configs["episodes"].append(\
{ "title" : "zoom on core and soc",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:52.3" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Asrock_A320M-DVS_VRMs.MP4"},\
})

# maybe overlay with counts
configs["episodes"].append(\
{ "title" : "cheap out on mosfet count",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:58.6" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Asrock_A320M-DVS_VRMs.MP4"},\
})

# maybe overlay on coils
configs["episodes"].append(\
{ "title" : "VRM coils",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:09.1" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Asrock_A320M-DVS_VRMs.MP4"},\
})

# this might need a better shot, when filming the 2 slots GPU
configs["episodes"].append(\
{ "title" : "The DIMM slots",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:18.2" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Asrock_A320M-DVS_memorySlots.MP4"},\
})

configs["episodes"].append(\
{ "title" : "insert RAM",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:22.4" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Asrock_A320M-DVS_RamInsertionRemoval.MP4", "start" : "00:04"},\
})

configs["episodes"].append(\
{ "title" : "remove RAM",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:26.9" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Asrock_A320M-DVS_RamInsertionRemoval.MP4", "start" : "00:26"},\
})


configs["episodes"].append(\
{ "title" : "The expansion slots",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:34.7" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Asrock_A320M-DVS_slots.MP4"},\
})

# needs video
configs["episodes"].append(\
{ "title" : "insert GPU",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:40.5" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Asrock_A320M-DVS_SataVs2SlotCard.MP4", "start" : "00:25"},\
})

configs["episodes"].append(\
{ "title" : "back to slots breel",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:49.7" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Asrock_A320M-DVS_slots.MP4"},\
})

configs["episodes"].append(\
{ "title" : "SATA ports",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:13.7" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Asrock_A320M-DVS_SATA.MP4"},\
}) # maybe an overlay with the DVI-D to HDMI adapter?

configs["episodes"].append(\
{ "title" : "No M.2 for you",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:25.9" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Asrock_A320M-DVS_slots.MP4"},\
}) # audacity

configs["episodes"].append(\
{ "title" : "The pin headers",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:38.3" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Asrock_A320M-DVS_headers.MP4", "start" : "00:00"},\
}) # audacity

configs["episodes"].append(\
{ "title" : "chassis intrusion, front panel",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:47.2" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Asrock_A320M-DVS_headers.MP4", "start" : "00:50"},\
}) # rear IO, maybe?

configs["episodes"].append(\
{ "title" : "USB pin headers",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:56.5" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Asrock_A320M-DVS_DIMMSlots.MP4", "start" : "00:00"},\
}) # rear IO, maybe?

configs["episodes"].append(\
{ "title" : "SPI header",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:12.7" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Asrock_A320M-DVS_headers.MP4", "start" : "01:18"},\
}) # list of bios? or side by side BIOS and list of BIOS-es?

# vide outputs
configs["episodes"].append(\
{ "title" : "Rear IO",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:30.1" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Asrock_A320M-DVS_IO.MP4", "start" : "00:00"},\
})

configs["episodes"].append(\
{ "title" : "rear io, others",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:47.1" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Asrock_A320M-DVS_IO.MP4", "start" : "00:20"},\
})

# maybe a side by side here with GA-A320M-H
configs["episodes"].append(\
{ "title" : "The audio",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:58.1" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Asrock-A320m-DVS_audio.mkv"},\
})

configs["episodes"].append(\
{ "title" : "actual audio",\
"isChapter" : False,\
"audio" : {"timestamps" : ("03:38.1", "03:58.1" ), "volume" : 0.001, "padAudio" : 0.05 },\
"video" : {"file" : "Asrock-A320m-DVS_audio.mkv", "start" : "00:04"},\
})

configs["episodes"].append(\
{ "title" : "The BIOS",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:02.9" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Asrock-A320M-DVS_Tpm2.MP4"},\
})

configs["episodes"].append(\
{ "title" : "DOCP - yes",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:14.1" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Asrock-A320M-DVS_RAM.MP4"},\
})

configs["episodes"].append(\
{ "title" : "Save OC profile",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:20.3" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Asrock-A320M-DVS_SaveOcProfile.MP4"},\
})

# maybe side by side programmer and programming ?
configs["episodes"].append(\
{ "title" : "TPM and REBAR",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:30.4" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "A320m-dvs-tpm-rebar.mp4"},\
})

configs["episodes"].append(\
{ "title" : "Fan control",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:47" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Asrock-A320M-DVS_Fans.MP4"},\
})

configs["episodes"].append(\
{ "title" : "No CPU voltage, no multiplier",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:00.5" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Asrock-A320M-DVS_RAM.MP4"},\
})

# conflicted
configs["episodes"].append(\
{ "title" : "Conclusions",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:26.2" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Asrock_A320M-DVS-overview.MP4"},\
})

configs["episodes"].append(\
{ "title" : "but then the DIMMs",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:31.8" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Asrock_A320M-DVS_memorySlots.MP4"},\
})

configs["episodes"].append(\
{ "title" : "then the BIOS",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:44" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Asrock-A320M-DVS_RAM.MP4"},\
})

configs["episodes"].append(\
{ "title" : "pricing - bought as deffective",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:02.5" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "A320m-dvs_olx_deffective.mkv"},\
})

configs["episodes"].append(\
{ "title" : "pricing - HD and HDV are better",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:17.9" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Asrock_AM4_emag.mkv"},\
})

configs["episodes"].append(\
{ "title" : "Bye",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:26.3" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Asrock_A320M-DVS-overview.MP4"},\
})

scriptedvided.makeVideo(configs)

