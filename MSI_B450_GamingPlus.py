import scriptedvided
import sv_ffutils

configs = { "defaultAudioFile" : "MSI-B450m-GamingPlus.ogg",\
"mediaFolder" : "F:\\Videos\\B450 Gaming Plus", \
"stockFolder" : "F:\\Videos\\stock",\
"benchmarkFile" : "not needed",\
"outputFolder" : "F:\\Videos\\B450 Gaming Plus\\output", \
"outputFile" : "MSI-B450-GamingPlus.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "Only 20 bucks", "until" : "The VRMs"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "The VRMs", "until" : "actual audio"}}, \
{"file" : "Ferco - Inquisitiveness.ogg", "timestamps" : ("01:01", None ), "destinationTimestamp" : {"title" : "The BIOS", "until" : "Conclusions"}}, \
{"file" : "Inspired - MaikonMusic  Free Background Music  Audio Library Release.mp3", "timestamps" : ("00:00", None ), "destinationTimestamp" : {"title" : "Conclusions", "until" : "EOF"}}, \
], "volume" : 0.05 },\
"episodes" : [],\
"youtube" : {"title" : "", \
"description" : '''Not great, not terrible | ASUS Prime B550M-K''',\
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
#"isChapter" : False, \

####################### intro ###############################

# this is the hook 
#  scriptedvided.nextTS\(configs\)\, *\"[0-9][0-9]\:[0-9][0-9]\.?[0-9]?[0-9]?\"
#  \"file\" *\: *\".*\"
#  scriptedvided.r6sText\('.*' *\, *[0-9]*\, *[0-9]*\)
#   "timestamps" *\: *\( *"[0-9\:\.]*" *\, *"[0-9\:\.]*" *\)
#configs["episodes"].append(\
#{ "title": "A favorite of miners and gamers alike",\
#"audio" : {"timestamps" : (scriptedvided.nextTS(configs),  "" ), "volume" : 0.999, "padAudio" : 0.05 },\
#"video" : {"file" : ""},\
# \"video\" *: *\{\"file\" *: *\".*\"\}
#})

####################### intro ###############################

# this is the hook
#configs["episodes"].append(\
#{ "title": "A favorite of miners and gamers alike",\
#"audio" : {"timestamps" : ("09:37.3", "09:46" ), "volume" : 0.999, "padAudio" : 0.05 },\
#"video" : {"file" : ""},\
#})

configs["episodes"].append(\
{ "title" : "Only 20 bucks",\
"audio" : {"timestamps" : ("00:00", "00:11.8" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "MsiB450GamingPlus_overview.MP4"},\
})

# this is for the heatsinks segment
configs["episodes"].append(\
{ "title" : "The VRMs",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:23.3" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "MsiB450GamingPlus_VRM-ish.MP4"},\
})

configs["episodes"].append(\
{ "title" : "The VRMs overview",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:29.8" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "B450_GamingPlus_VRMs_wBars.mp4"},\
})

configs["episodes"].append(\
{ "title" : "SOC topology",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:37" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "B450_GamingPlus_VRMs_soc.mp4"},\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title" : "VCORE topology",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:47.05" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "B450_GamingPlus_VRMs_core.mp4"},\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title" : "VRM overview no heatsinks",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:59.1" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "B450_GamingPlus_VRMs_wBars.mp4"},\
"isChapter" : False,\
})

#configs["episodes"].append(\
#{ "title" : "Asus and Grenade side by side",\
#"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "" ), "volume" : 0.999, "padAudio" : 0.05 },\
#"video" : {"file" : ""},\
#"isChapter" : False,\
#})

# this might need a better shot, when filming the 2 slots GPU
configs["episodes"].append(\
{ "title" : "The DIMM slots",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:10.6" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "MsiB450GamingPlus_Dimms.MP4"},\
})

configs["episodes"].append(\
{ "title" : "The expansion slots",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:30.5" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "MsiB450GamingPlus_slots.MP4"},\
})

# needs video
configs["episodes"].append(\
{ "title" : "first M.2 slot",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:49.4" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "MsiB450GamingPlus_slots.MP4"},\
})

configs["episodes"].append(\
{ "title" : "pcie 2 x 4",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:58.5" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "MsiB450GamingPlus_slots.MP4"},\
})

configs["episodes"].append(\
{ "title" : "SATA ports",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:13.1" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "MsiB450GamingPlus_SATA.MP4"},\
}) # maybe an overlay with the DVI-D to HDMI adapter?

configs["episodes"].append(\
{ "title" : "The pin headers",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:31.5" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "MsiB450GamingPlus_pins1.MP4"},\
}) # audacity

configs["episodes"].append(\
{ "title" : "last bottom pins",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:48.5" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "MsiB450GamingPlus_pins2.MP4"},\
}) # rear IO, maybe?


configs["episodes"].append(\
{ "title" : "EZ debug LEDs",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:57.4" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "MsiB450GamingPlus_Debug.MP4"},\
}) # rear IO, maybe?

configs["episodes"].append(\
{ "title" : "JBAT header",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:03.8" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "MsiB450GamingPlus_pins3.MP4"},\
})

configs["episodes"].append(\
{ "title" : "JRGB1 header",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:11.55" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "MsiB450GamingPlus_RgbPins2.MP4"},\
})

configs["episodes"].append(\
{ "title" : "SPI header",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:20.2" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "MsiB450GamingPlus_SpiPins.MP4"},\
})

# must provide some overlays ...
configs["episodes"].append(\
{ "title" : "Rear IO",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:44.3" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "MsiB450GamingPlus_IO2.MP4"},\
})

# maybe a side by side here with GA-A320M-H
configs["episodes"].append(\
{ "title" : "The video out",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:50.8" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "MsiB450GamingPlus_IO.MP4"},\
})

# maybe a side by side here with GA-A320M-H
configs["episodes"].append(\
{ "title" : "Audio codec",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:02.5" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "MsiB450GamingPlus_IO2.MP4"},\
})

configs["episodes"].append(\
{ "title" : "actual audio",\
"isChapter" : False,\
"audio" : {"timestamps" : ( "03:47" , "04:02.5" ), "volume" : 0.001, "padAudio" : 0.05 },\
"video" : {"file" : "B450_GamingPlus_audio.mkv"},\
})

configs["episodes"].append(\
{ "title" : "The BIOS",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:09.3" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "MsiB450GamingPlus_BiosMflash_noTilt.mp4"},\
})

configs["episodes"].append(\
{ "title" : "CPU multiplier",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:19.6" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "MsiB450GamingPlus_BiosCpuMultiplier_noTilt.mp4"},\
})

configs["episodes"].append(\
{ "title" : "VCORE setup",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:38" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "MsiB450GamingPlus_BiosCpuVoltage_noTilt.mp4"},\
})

configs["episodes"].append(\
{ "title" : "DOCP",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:47.6" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "MsiB450GamingPlus_BiosRAM_noTilt.mp4"},\
})

configs["episodes"].append(\
{ "title" : "OC profiles",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:00" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "MsiB450GamingPlus_BiosOcProfiles_noTilt.mp4"},\
})

configs["episodes"].append(\
{ "title" : "TPM an REBAR",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:10.2" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "MsiB450GamingPlus_BiosRebarTpm.mp4"},\
})

configs["episodes"].append(\
{ "title" : "fan profiles and fan curve",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:25.5" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "MsiB450GamingPlus_BiosFans_noTilt.mp4"},\
})


# conflicted
configs["episodes"].append(\
{ "title" : "Conclusions",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:34.7" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "MsiB450GamingPlus_overview.MP4"},\
})

configs["episodes"].append(\
{ "title" : "Replacement for the Tomahawk",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:48.4" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "MsiB450GamingPlus_VRM-ish.MP4"},\
})

configs["episodes"].append(\
{ "title" : "Pricing",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:03" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "B450_GamingPlus_olx.mkv"},\
})

configs["episodes"].append(\
{ "title" : "Bye",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:17" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "MsiB450GamingPlus_overview.MP4"},\
})

scriptedvided.makeVideo(configs)

