import scriptedvided
import sv_ffutils

configs = { "defaultAudioFile" : "Hunananzhi-x99-qd4.ogg",\
"mediaFolder" : "F:\\Videos\\Hunananzhi-x99-qd4", \
"stockFolder" : "F:\\Videos\\stock",\
"benchmarkFile" : "not needed",\
"outputFolder" : "F:\\Videos\\Hunananzhi-x99-qd4\\output", \
"outputFile" : "Hunananzhi-x99-qd4.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#00008080"},\
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
{ "title": "X99 ... not!",\
"audio" : {"timestamps" : ("00:00", "00:12.2" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "HuananzhiQD4_overview.MP4"},\
})

configs["episodes"].append(\
{ "title": "actually a q87",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:20.7"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
}) # add the CPUZ as overlay 



configs["episodes"].append(\
{ "title": "The VRMs",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:27.3"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "HuananzhiQD4_VRM.MP4"},\
})

configs["episodes"].append(\
{ "title": "VRMs - core",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:39.3"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Huananzhi_x99_qd4_VrmMosfets2_barred.mp4"},\
"overlay" : {"image" : {"file" : ""} }, \
}) # add overlay

configs["episodes"].append(\
{ "title": "4 DIMM slots, 8 clips",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:55.6"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "HuananzhiQD4_DIMMs.MP4"},\
})

configs["episodes"].append(\
{ "title": "quad channel",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:09.6"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "HuananzhiX99QD4_E5-2670-v3_RAM-good_barred.mp4"},\
"overlay" : {"image" : {"file" : ""} }, \
}) # add overlay qith cpuz again
# HuananzhiX99QD4_E5-2670-v3_RAM-good_barred.mp4 or E5-2670-v3_LargerCPU-Z_mem.mkv, but trimmed down


configs["episodes"].append(\
{ "title": "Expansion slots, ports and headers",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:22.6"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "HuananzhiQD4_slots.MP4"},\
})

configs["episodes"].append(\
{ "title": "M.2 slots maybe with arrow overlay",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:32.4"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "HuananzhiQD4_slots.MP4"},\
"overlay" : {"image" : {"file" : ""} }, \
}) # maybe overlay with the arrows pushing to the CPU?

configs["episodes"].append(\
{ "title": "q87 and SATA channels",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:40.3"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
"overlay" : {"image" : {"file" : ""} }, \
})  # overlay with Intel Ark for Q87 SATA 

configs["episodes"].append(\
{ "title": "Xeon and available PCIE lanes",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:47"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_E5-2670-v3_mobo_inHand_barred.mp4"},\
"overlay" : {"image" : {"file" : ""} }, \
}) # overlay with Intel Ark for Xeon PCIE lanes 


configs["episodes"].append(\
{ "title": "SATA ports",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:59.3"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "HuananzhiQD4_SATA.MP4"},\
}) # ... maybe anoverlay with the q87 and available sata channels?

configs["episodes"].append(\
{ "title": "Pin - audio, COM",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:14.8"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "HuananzhiQD4_pinsUpToUSB3.MP4"},\
})

configs["episodes"].append(\
{ "title": "Pin - USBs",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:19.8"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "HuananzhiQD4_pins2.MP4"},\
})

configs["episodes"].append(\
{ "title": "clear CMOS",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:25.1"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "HuananzhiQD4_pins2.MP4"},\
})

configs["episodes"].append(\
{ "title": "3 pin fan header",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:29.8"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "HuananzhiQD4_pins2.MP4"},\
})

configs["episodes"].append(\
{ "title": "front panel connector",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:34.4"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "HuananzhiQD4_pins2.MP4"},\
})

# too long of a cut ...
configs["episodes"].append(\
{ "title": "Rear IO",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:41.3"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "HuananzhiQD4_IO.MP4"},\
}) # maybe an overlay with the DVI-D to HDMI adapter?

# too long of a cut ...
configs["episodes"].append(\
{ "title": "Maybe overlay with Xeons and no IGPU?",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:47.8"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_E5-2670-v3_mobo_inHand_barred.mp4"},\
"isChapter" : False,\
}) # picture overlay with the Xeon ARC page

configs["episodes"].append(\
{ "title": "Other rear io",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:57.9"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "HuananzhiQD4_IO.MP4"},\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title": "Audio sample",\
"isChapter" : False,\
"audio" : {"timestamps" : ("", "02:57.9" ), "volume" : 0.001, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

# might be removed, if I don't have a good video segment, an have it blended with the BIOS
configs["episodes"].append(\
{ "title": "Audio conclusions",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:02.4" ), "volume" : 0.001, "padAudio" : 0.05 },\
"video" : {"file" : "Huananzhi-X99-QD4-BIOS-OC-bad.MP4"},\
})

# EC spi chip first
configs["episodes"].append(\
{ "title": "The BIOS setup utility",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:10.7"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Huananzhi-X99-QD4-BIOS-CpuFreq.MP4"},\
}) # use the core clock already

configs["episodes"].append(\
{ "title": "CPU voltage",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:19.4"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Huananzhi-X99-QD4-BIOS-VCore.MP4"},\
})

configs["episodes"].append(\
{ "title": "Power limits",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:31.8"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Huananzhi-X99-QD4-BIOS-Power.MP4"},\
})

configs["episodes"].append(\
{ "title": "REBAR-ish",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:37.3"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Huananzhi-X99-QD4-BIOS-Rebar.MP4"},\
})

configs["episodes"].append(\
{ "title": "CSM requirements",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:44.4"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Huananzhi-X99-QD4-BIOS-Rebar.MP4", "start" : "00:00"},\
})

# likes
configs["episodes"].append(\
{ "title": "Conclusions",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:55.5"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "HuananzhiQD4_2023.MP4"},\
})

configs["episodes"].append(\
{ "title": "not the best VRM",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:02.7"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Huananzhi_x99_qd4_VrmMosfets2_barred.mp4"},\
})

configs["episodes"].append(\
{ "title": "one slot per mem channel",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:09"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "HuananzhiX99QD4_E5-2670-v3_RAM-good_barred.mp4"},\
})

configs["episodes"].append(\
{ "title": "RDIMM vs UDIMM",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:19"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "ddr4_Rdimm_vs_Udimm_barred.mp4"},\
})

configs["episodes"].append(\
{ "title": "highlight the buck converters, maybe side by side, zoomed",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:29.7"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "Pricing breel",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:35.2"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "HuananzhiQD4_2023.MP4"},\
})

configs["episodes"].append(\
{ "title": "Pricing screencap",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:42.3"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "more breel",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:47.8"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "B550 prices side by side with x99",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:59.8"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "not really recommended",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:06.2"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "HuananzhiQD4_2023.MP4"},\
})

configs["episodes"].append(\
{ "title": "zoom on CPUs",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:15.9"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "breel_E5-2670-v3_mobo_inHand_barred.mp4"},\
})

configs["episodes"].append(\
{ "title": "Bye",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:22.8"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

scriptedvided.makeVideo(configs)

