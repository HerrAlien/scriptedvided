import scriptedvided

configs = { "defaultAudioFile" : "R5_3600_build_2.ogg",\
"mediaFolder" : "F:\\Videos\\R5_3600_build", \
"stockFolder" : "F:\\Videos\\stock",\
"benchmarkFile" : "F:\\Videos\\R5_3600_build\\Benchmark_GTX_1050Ti_2024.txt",\
"outputFolder" : "F:\\Videos\\R5_3600_build\\output", \
"outputFile" : "R5_3600_build.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "Something new, something old, something defective", "until" : "The case"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "The case", "until" : "The RAM"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "The RAM", "until" : "Conclusions"}}, \
{"file" : "Inspired - MaikonMusic  Free Background Music  Audio Library Release.mp3", "timestamps" : ("00:00", None ), "destinationTimestamp" : {"title" : "Conclusions", "until" : "EOF"}}, \
], "volume" : 0.05 },\
"episodes" : [],\
"youtube" : {"title" : "", \
"description" : ''' GPU Hook 
We're using the same Z230 workstation with an i7 4770 equivalent CPU and 32 GB of DDR3 running in dual channel at 1600MHz.''',\
"links" : '''
Track: Bliss Of Heaven - SOMM [Audio Library Release]
Music provided by Audio Library Plus
Watch: https://www.youtube.com/watch?v=JQ6mKeQLZak&t=0s
Free Download / Stream: https://alplus.io/blisss-heaven

Track: Far Far Away - Ferco [Audio Library Release]
Music provided by Audio Library Plus
Watch: https://www.youtube.com/watch?v=SrkQ3K1umlc&t=0s 
Free Download / Stream: https://alplus.io/far-far-away

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
{ "title": "Something new, something old, something defective",\
"audio" : {"timestamps" : ("00:00", "00:13.9" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "test_system_noGPU.mp4"},\
})


configs["episodes"].append(\
{ "title": "The Z230 is getting old",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:30" ), "volume" : 0.999, "padAudio" : 0.05 },\
"isChapter" : False,\
"video" : {"file" : "system_z230.mp4"},\
})

configs["episodes"].append(\
{ "title": "A new test system",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:43.3" ), "volume" : 0.999, "padAudio" : 0.05 },\
"isChapter" : False,\
"video" : {"file" : "test_system_noGPU.mp4"},\
})

configs["episodes"].append(\
{ "title": "The case",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:58" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "system_b351_temperedMetal.mp4"},\
})

configs["episodes"].append(\
{ "title": "looks like the Z230",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:06.8" ), "volume" : 0.999, "padAudio" : 0.05 },\
"isChapter" : False,\
"video" : {"file" : "system_b351_z230.mp4", "start" : "00:15"},\
})

configs["episodes"].append(\
{ "title": "has enough room",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:22.6" ), "volume" : 0.999, "padAudio" : 0.05 },\
"isChapter" : False,\
"video" : {"file" : "system_b351_airflow.mp4"},\
})

configs["episodes"].append(\
{ "title": "tempered metal",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:32.8" ), "volume" : 0.999, "padAudio" : 0.05 },\
"isChapter" : False,\
"video" : {"file" : "system_b351_temperedMetal.mp4", "start" : "00:00"},\
})

configs["episodes"].append(\
{ "title": "The CPU",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:03.1" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "broll_R5_3600.mp4"},\
})

configs["episodes"].append(\
{ "title": "The motherboard",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:14.2" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "BReel_B450M_ProM2V2_3.mp4"},\
})

configs["episodes"].append(\
{ "title": "control CPU voltage",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:27" ), "volume" : 0.999, "padAudio" : 0.05 },\
"isChapter" : False,\
"video" : {"file" : "B450M_bios1.mp4", "start" : "02:32", "rotation" : -2.5},\
})

configs["episodes"].append(\
{ "title": "plain mobo",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:38.5" ), "volume" : 0.999, "padAudio" : 0.05 },\
"isChapter" : False,\
"video" : {"file" : "broll_MSI_B450M_and_issues.mp4"},\
})

configs["episodes"].append(\
{ "title": "with no RGB",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:49.5" ), "volume" : 0.999, "padAudio" : 0.05 },\
"isChapter" : False,\
"video" : {"file" : "broll_MSI_B450M_features.mp4", "start" : "00:50"},\
})

configs["episodes"].append(\
{ "title": "but with EZ-debug",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:57.1" ), "volume" : 0.999, "padAudio" : 0.05 },\
"isChapter" : False,\
"video" : {"file" : "broll_MSI_B450M_features.mp4", "start" : "02:55"},\
})

configs["episodes"].append(\
{ "title": "no m2 standoff and no backplate",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:03.1" ), "volume" : 0.999, "padAudio" : 0.05 },\
"isChapter" : False,\
"video" : {"file" : "broll_MSI_B450M_and_issues.mp4", "start" : "01:23"},\
})

configs["episodes"].append(\
{ "title": "backplate from Aliexpress",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:14.6" ), "volume" : 0.999, "padAudio" : 0.05 },\
"isChapter" : False,\
"video" : {"file" : "system_b450M_metalBackplate.mp4", "start" : "00:15"},\
})

configs["episodes"].append(\
{ "title": "vs makeshist backplate",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:21.6" ), "volume" : 0.999, "padAudio" : 0.05 },\
"isChapter" : False,\
"video" : {"file" : "broll_MSI_B450M_withBackplate_M2Post.mp4", "start" : "00:43"},\
})

configs["episodes"].append(\
{ "title": "nylon retainer for M2",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:38.4" ), "volume" : 0.999, "padAudio" : 0.05 },\
"isChapter" : False,\
"video" : {"file" : "broll_MSI_B450M_withBackplate_M2Post.mp4", "start" : "01:43"},\
})

configs["episodes"].append(\
{ "title": "replaced with a regular nylon post",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:48" ), "volume" : 0.999, "padAudio" : 0.05 },\
"isChapter" : False,\
"video" : {"file" : "nvme_nylon_post.MP4", "start" : "00:50"},\
})

# needs better audio
configs["episodes"].append(\
{ "title": "The CPU cooler",\
"audio" : {"timestamps" : ("07:04.7", "07:17.2" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "system_cpuCooler_directTouched.mp4"},\
})

configs["episodes"].append(\
{ "title": "BUCKLE",\
"audio" : {"timestamps" : ("04:02.7", "04:11.3" ), "volume" : 0.999, "padAudio" : 0.05 },\
"isChapter" : False,\
"video" : {"file" : "cooler_installation.mp4", "start" : "00:26"},\
})

configs["episodes"].append(\
{ "title": "same company as the case",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:20.7" ), "volume" : 0.999, "padAudio" : 0.05 },\
"isChapter" : False,\
"video" : {"file" : "system_aigo_sameManufacturer.mp4", "start" : "00:11"},\
})

configs["episodes"].append(\
{ "title": "The RAM",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:34.9" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "broll_DDR4_2x16GB.mp4", "start" : "01:40"},\
})

configs["episodes"].append(\
{ "title": "started single channel",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:52.4" ), "volume" : 0.999, "padAudio" : 0.05 },\
"isChapter" : False,\
"video" : {"file" : "building_loadingMoboNoCooler.mp4", "start" : "02:15"},\
})

configs["episodes"].append(\
{ "title": "paired with a corsair",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:03.2" ), "volume" : 0.999, "padAudio" : 0.05 },\
"isChapter" : False,\
"video" : {"file" : "B450M_bios2-converted.mp4", "start" : "01:10", "rotation" : -2.5},\
})

configs["episodes"].append(\
{ "title": "The boot drive",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:21.1" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "nvme_drive.MP4"},\
})

configs["episodes"].append(\
{ "title": "just a plain nvme drive",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:34.1" ), "volume" : 0.999, "padAudio" : 0.05 },\
"isChapter" : False,\
"video" : {"file" : "building_loadingMoboNoCooler.mp4", "start" : "03:27"},\
})

configs["episodes"].append(\
{ "title": "Single exhaust fan",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:48.8" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "system_exhaustFan.mp4"},\
})

configs["episodes"].append(\
{ "title": "but can get intake fans as well",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:53" ), "volume" : 0.999, "padAudio" : 0.05 },\
"isChapter" : False,\
"video" : {"file" : "system_intakeFans.mp4"},\
})

configs["episodes"].append(\
{ "title": "The PSU - not a defective one",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:06.9" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "PSU_FSP_hydro.mkv"},\
})

configs["episodes"].append(\
{ "title": "it is the old one",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:17.4" ), "volume" : 0.999, "padAudio" : 0.05 },\
"isChapter" : False,\
"video" : {"file" : "mounting_ioShieldAndPSU.mp4", "start" : "01:01"},\
})

configs["episodes"].append(\
{ "title": "A GPU ... any GPU.",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:32.25" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "test_system_RX580-converted.mp4"},\
})

configs["episodes"].append(\
{ "title": "needs 8 pin",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:42.4" ), "volume" : 0.999, "padAudio" : 0.05 },\
"isChapter" : False,\
"video" : {"file" : "XFX_RX580_breel.mp4"},\
})

configs["episodes"].append(\
{ "title": "Conclusions",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:47.35" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "test_system_noGPU.mp4"},\
})

configs["episodes"].append(\
{ "title": "not current gen",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:54.5" ), "volume" : 0.999, "padAudio" : 0.05 },\
"isChapter" : False,\
"video" : {"file" : "test_system_RX580-converted.mp4"},\
})

configs["episodes"].append(\
{ "title": "bye",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:02" ), "volume" : 0.999, "padAudio" : 0.05 },\
"isChapter" : False,\
"video" : {"file" : "test_system_noGPU.mp4"},\
})


##configs["episodes"].append(\
##{ "title": "Blooper",\
##"isChapter" : False,\
##"audio" : {"timestamps" : ( "13:40.5", "14:04.2") },\
##"video" : {"file":"HiRezTrio-P_aladins_R_ealmRoyale_R_ogueCompany.mp4"}\
##})

#scriptedvided.makeVideoForEpisode(configs["episodes"][2], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][9], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][13], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][15], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][16], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][17], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][18], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][19], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][21], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][22], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][24], configs)
#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "control CPU voltage"][0], configs)
#scriptedvided.makeVideo(configs)

#for x in range(19,26):
#    scriptedvided.makeVideoForEpisode(configs["episodes"][x], configs)
#
scriptedvided.makeVideo(configs)
