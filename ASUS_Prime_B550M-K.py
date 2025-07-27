import scriptedvided
import sv_ffutils

configs = { "defaultAudioFile" : "MSI-B350-Tomahawk.ogg",\
"mediaFolder" : "F:\\Videos\\B350 Tomahawk", \
"stockFolder" : "F:\\Videos\\stock",\
"benchmarkFile" : "not needed",\
"outputFolder" : "F:\\Videos\\B350 Tomahawk\\output", \
"outputFile" : "MSI-B350-Tomahawk.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "Best budget board ... maybe", "until" : "The VRMs"}}, \
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
{ "title" : "Best budget board ... maybe",\
"audio" : {"timestamps" : ("00:00", "00:18.7" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "ASUS-B550M-K-breel1.MP4"},\
})

# this is for the heatsinks segment
configs["episodes"].append(\
{ "title" : "The VRMs",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:30.7" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "ASUS-B550M-K-breel2.MP4"},\
})

configs["episodes"].append(\
{ "title" : "VCORE",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:37.5" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "ASUS-B550M-K-VRM.MP4"},\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title" : "SOC topology",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:43.2" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "ASUS-B550M-K-VRM.MP4"},\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title" : "Asus and Asrock side by side",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:50.2" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
"isChapter" : False,\
})

configs["episodes"].append(\
{ "title" : "again no heatsinks",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:57" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "ASUS-B550M-K-breel2.MP4"},\
"isChapter" : False,\
})

# this might need a better shot, when filming the 2 slots GPU
configs["episodes"].append(\
{ "title" : "The DIMM slots",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:12.4" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "ASUS-B550M-K-MemSlots.MP4", "start" : "00:23"},\
})

configs["episodes"].append(\
{ "title" : "The expansion slots",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:29.6" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "ASUS-B550M-K-slots.MP4"},\
})

# needs video
configs["episodes"].append(\
{ "title" : "first M.2 slot",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:43.8" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "ASUS-B550M-K-slots.MP4"},\
})

configs["episodes"].append(\
{ "title" : "second M.2 slot",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:59.6" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "ASUS-B550M-K-slots.MP4"},\
})

configs["episodes"].append(\
{ "title" : "SATA ports",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:15.2" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
}) # maybe an overlay with the DVI-D to HDMI adapter?

configs["episodes"].append(\
{ "title" : "The pin headers",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:26.7" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
}) # audacity

configs["episodes"].append(\
{ "title" : "usb2 usb3 FP1 FP2",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:37.5" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
}) # rear IO, maybe?


# needs an arrow overlayed, pointing to the debug LEDs
configs["episodes"].append(\
{ "title" : "speaker port",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:42.9" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
}) # rear IO, maybe?

# needs an arrow overlayed, pointing to the debug LEDs
configs["episodes"].append(\
{ "title" : "front usb3",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:50.4" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
}) # rear IO, maybe?


# must provide some overlays ...
configs["episodes"].append(\
{ "title" : "Rear IO",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:01.6" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

# maybe a side by side here with GA-A320M-H
configs["episodes"].append(\
{ "title" : "The video out",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:13" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

# maybe a side by side here with GA-A320M-H
configs["episodes"].append(\
{ "title" : "Audio codec",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:21.2" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title" : "ALC887 was tested before breel with boards",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:28.2"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title" : "ALC887 tested before breel with audios",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:39.8"), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title" : "actual audio",\
"isChapter" : False,\
"audio" : {"timestamps" : ( "03:23.8" , scriptedvided.nextTS(configs)), "volume" : 0.001, "padAudio" : 0.05 },\
"video" : {"file" : "Prime-B550M-K_audio.mkv", "start" : "00:04"},\
})

configs["episodes"].append(\
{ "title" : "The BIOS",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:44.7" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title" : "others did more with less",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:56.5" ), "volume" : 0.999, "padAudio" : 0.05 },\
"isChapter" : False,\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title" : "CPU compat list",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:06.1" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title" : "bioses side by side",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:13.7" ), "volume" : 0.999, "padAudio" : 0.05 },\
"isChapter" : False,\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title" : "DOCP and rebar side by side",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:26.6" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title" : "fan profiles and fan curve",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:35.6" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title" : "fan types",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:44.5" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title" : "CPU multiplier",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:51" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title" : "VCORE setup",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:00.9" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})


# conflicted
configs["episodes"].append(\
{ "title" : "Conclusions",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:14" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title" : "does have some features but",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:21.2" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title" : "best used with downdrafts",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:32.6" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title" : "do not use a ryzen 7",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:43.1" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title" : "blown mosfets",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:46.3" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title" : "CPU compat is an issue",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:53" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title" : "Tourist trap",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:01.5" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})


configs["episodes"].append(\
{ "title" : "Bye",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:12.3" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

scriptedvided.makeVideo(configs)

