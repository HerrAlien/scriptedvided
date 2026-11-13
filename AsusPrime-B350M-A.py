import scriptedvided
import sv_ffutils

configs = { "defaultAudioFile" : "Prime-X370-Pro.ogg",\
"mediaFolder" : "F:\\Videos\\AsusPrime-X370-Pro", \
"stockFolder" : "F:\\Videos\\stock",\
"benchmarkFile" : "not needed",\
"outputFolder" : "F:\\Videos\\AsusPrime-X370-Pro\\output", \
"outputFile" : "AsusPrime-X370-Pro.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "Good bang for the buck", "until" : "The VRMs"}}, \
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
# \"video\" *: *\{ *\"file\" *: *\".*\" *\}

####################### intro ###############################

# this is the hook
#configs["episodes"].append(\
#{ "title": "A favorite of miners and gamers alike",\
#"audio" : {"timestamps" : ("09:37.3", "09:46" ), "volume" : 0.999, "padAudio" : 0.05 },\
#"video" : {"file" : ""},\
#})

configs["episodes"].append(\
{ "title": "Middle ground ... tease?",\
"audio" : {"timestamps" : ("00:00", "" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "The VRMs",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), ""), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "VRM topo",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), ""), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
}) # add overlay

configs["episodes"].append(\
{ "title": "PCB holes",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), ""), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
}) # add overlay

configs["episodes"].append(\
{ "title": "Z97 heatsink",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), ""), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
}) # add overlay

configs["episodes"].append(\
{ "title": "keep the heatsink",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), ""), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
}) # add overlay

configs["episodes"].append(\
{ "title": "4 DIMM slots",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:51"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

# # # full board overview
configs["episodes"].append(\
{ "title": "Expansion slots, ports and headers",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), ""), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

##Needs overlays:s:
configs["episodes"].append(\
{ "title": "GPU slot",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), ""), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

##Needs overlays:s:
configs["episodes"].append(\
{ "title": "x1 slots",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), ""), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

# -----------------------------------------------------------------------------------------------------
##NEEDS RECORDING
configs["episodes"].append(\
{ "title": "Great success",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), ""), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

##NEEDS RECORDING
configs["episodes"].append(\
{ "title": "NVME slot",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), ""), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})
# -----------------------------------------------------------------------------------------------------

## again, overview - ish
configs["episodes"].append(\
{ "title": "SATA",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), ""), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

##Needs overlays:s:
configs["episodes"].append(\
{ "title": "regular ssd",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), ""), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "SATA ports",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), ""), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
}) 

# including audio, COM
configs["episodes"].append(\
{ "title": "Pins intro",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), ""), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

# include 
configs["episodes"].append(\
{ "title": "missing tpm, USB",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), ""), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "front panel",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), ""), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "RGB",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), ""), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "SPI header",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), ""), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

##Needs overlays::
configs["episodes"].append(\
{ "title": "clear RTC",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), ""), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "CPu fans, phd 6k",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), ""), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "sys fan",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), ""), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})


#Needs overlays::
configs["episodes"].append(\
{ "title": "Rear IO",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), ""), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

#Needs overlays::
configs["episodes"].append(\
{ "title": "PS2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), ""), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
"isChapter" : False,\
})

#Needs overlays::
configs["episodes"].append(\
{ "title": "VGA",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), ""), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
"isChapter" : False,\
})

#Needs overlays::
configs["episodes"].append(\
{ "title": "digital video",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), ""), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
"isChapter" : False,\
})

#Needs overlays::
configs["episodes"].append(\
{ "title": "USBs, ethernet, audio",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "3:21.4"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
"isChapter" : False,\
}) # maybe an overlay with the DVI-D to HDMI adapter?


configs["episodes"].append(\
{ "title": "Audio sample",\
"isChapter" : False,\
"audio" : {"timestamps" : ("03:16", "03:26.9" ), "volume" : 0.001, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

# EC spi chip first
configs["episodes"].append(\
{ "title": "The BIOS setup utility",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), ""), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
}) # list of bios

configs["episodes"].append(\
{ "title": "BIOS advanced, CPU freq",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), ""), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "CPU voltage",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), ""), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "Mem subtimings",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), ""), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "TPM and rebar",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), ""), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})


configs["episodes"].append(\
{ "title": "Fans types",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), ""), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})


configs["episodes"].append(\
{ "title": "fan curves",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), ""), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})


# with VRMs. Side by side with the B550
configs["episodes"].append(\
{ "title": "Conclusions",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), ""), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})


configs["episodes"].append(\
{ "title": "concl-pcie",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), ""), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "concl-sata",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), ""), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "holes are a tease",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), ""), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "Wraith prism",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), ""), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "used in a build",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), ""), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "wraiths",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), ""), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "motherboards to subscribe",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), ""), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "Bye",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), ""), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})


# scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "GPU slot"][0], configs)



scriptedvided.makeVideo(configs)

