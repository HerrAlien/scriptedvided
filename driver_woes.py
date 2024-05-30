import scriptedvided

configs = { "defaultAudioFile" : "legacy_drivers.ogg",\
"mediaFolder" : "F:\\Videos\\driver_woes", \
"stockFolder" : "F:\\Videos\\stock",\
"outputFolder" : "F:\\Videos\\driver_woes\\output", \
"outputFile" : "driver_woes.mp4", \
"benchmarkFile" : "",\
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#00008080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "Legacy video cards FTW ... right?", "until" : "1 - Dude, where's your full screen mode? | Radeon HD 5000-6000 series"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "1 - Dude, where's your full screen mode? | Radeon HD 5000-6000 series", "until" : "2 - Error 182 | Radeon HD 7000, R7-R9 200-300 series"}}, \
{"file" : "Inspired - MaikonMusic  Free Background Music  Audio Library Release.mp3", "timestamps" : ("00:00", None ), "destinationTimestamp" : {"title" : "2 - Error 182 | Radeon HD 7000, R7-R9 200-300 series", "until" : "3 - The GT 730 ... but which one? | Fermi (GF108) GT 730"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "3 - The GT 730 ... but which one? | Fermi (GF108) GT 730", "until" : "Closing words"}}, \
{"file" : "Inspired - MaikonMusic  Free Background Music  Audio Library Release.mp3", "timestamps" : ("00:00", None ), "destinationTimestamp" : {"title" : "Closing words", "until" : "[eof]"}}, \
], "volume" : 0.045 },\
"episodes" : [],\
"youtube" : {"title" : "How to fix (some of) the issues of legacy GPU drivers", \
"description" : '''We're exploring some of the issues encountered while running GPUs with legacy drivers. Think Fermi GT 730, Radeon R9 290 and Radeon HD 5770''',\
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
''', \
"tags" : "NVidia,GeForce,Fermi,GT730,GT 730,Fermi GT730,Fermi GT 730,AMD,Radeon,TeraScale2,HD5770,HD 5770,HD6850,HD 6850,HD5870,HD 5870,HD6870,HD 6870,HD5000,HD6000,GCN,GCN 1.0,GCN 2.0,GCN 3.0,R9 270,R7,R9,200,300,HD7000",\
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

lastTS = "00:00"
configs["episodes"].append(\
{ "title": "Legacy video cards FTW ... right?",\
"audio" : {"timestamps" : (lastTS, "00:16.9" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "broll_legacy_gpus.mp4" },\
}) # needs a video with TS2, R9 270 and GT 730
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "all issues in one screen",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "00:40.5" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "4_issues_merged.mp4" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

#let's start with AMD - zoom out on the where's your full screen
configs["episodes"].append(\
{ "title": "1 - Dude, where's your full screen mode? | Radeon HD 5000-6000 series",\
"audio" : {"timestamps" : (lastTS, "00:43.5" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "HD5770_F_allout4_windowed.mp4" },\
"overlay" : { \
    "image" : {"file" : "dude_where_is_fs.png", "chromaColor" : "0x00FF00"}\
}, \
}) # overlay with batman
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "DX11 is popular",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "00:52.2" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "w_arzone-a_pex-side-by-side.mp4" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "TS2 cards - first for DX11",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "01:00.2" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "broll_ts2_family_outside_takingTurns.mp4" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "HD5770 and Fortnite",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "01:11.5" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "hd5770_f_ortnite_B-Reel.mp4" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Fallout 4 in windowed",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "01:25.6" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "HD5770_F_allout4_windowed.mp4" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Game crashing at launch",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "01:40" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "HD5770_O_verwatch2.mkv" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "No driver would help. But!",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "01:59.4" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "F_ortnite_lobby_f11.mp4", "start" : "00:25" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "CCC",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "02:23.5" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "TS2_fix_FS.mkv" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "R9 270",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "02:36.8" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "breel_r9_270_outside.mp4" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

# GCN is now legacy
configs["episodes"].append(\
{ "title": "2 - Error 182 | Radeon HD 7000, R7-R9 200-300 series",\
"audio" : {"timestamps" : (lastTS, "02:49.8" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "R9_family_poor.mkv" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "GCN search for drivers",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "03:02.8" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "AMD_recommends_22.6.1.mp4" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Blink 182",\
"isChapter" : False, \
"audio" : {"timestamps" : ("00:00", "00:03" ), "volume" : 0.001, "padAudio" : 0.1 },\
"video" : {"file" : "blink_182.mkv" },\
})
# lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Actual error 182",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "03:11.05" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "error_182.mp4" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

# GCN is now legacy
configs["episodes"].append(\
{ "title": "Trust Microsoft",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "03:24.3" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "win_update.mp4" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Win update means old drivers",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "03:33.6" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "gcn_win_update_old_drivers.mp4" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "a - punch card name",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "03:41.1" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "gcn_21.5.1_downloading.mkv" , "start" : "00:07"},\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "b - ignore 22.6.1",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "03:44.4" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "gcn_21.5.1_downloading.mkv" , "start" : "00:20"},\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "c - previous drivers",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "03:50.6" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "gcn_21.5.1_downloading.mkv" , "start" : "00:25"},\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "d - choose 21.5.1",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "04:01.4" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "gcn_21.5.1_downloading.mkv" , "start" : "00:35"},\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "e - this one installs",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "04:04.4" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "gcn_21.5.1_downloading.mkv" , "start" : "02:41"},\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "NVidia does it too",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "04:13.7" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "GF108_download_kepler_driver.mkv" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]


configs["episodes"].append(\
{ "title": "3 - The GT 730 ... but which one? | Fermi (GF108) GT 730",\
"audio" : {"timestamps" : (lastTS, "04:23.6" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "730_family_2.mkv" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Download drivers 730",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "04:33.5" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "GF108_download_kepler_driver.mkv" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "drivers 730 fail to install",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "04:48.3" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "GF108_install_kepler_driver.mkv" , "start" : "00:46"},\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "use the 430 ones",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "05:07.9" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "GF108_download_fermi_driver.mkv", "start" : "00:18" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Closing words",\
"audio" : {"timestamps" : (lastTS, "05:30.2" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "broll_ts2_family_outside_takingTurns.mp4" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "better testing means more effort",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "05:57" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "no open source",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "06:33.5" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "hd5770_f_ortnite_B-Reel.mp4" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Brees with cards, end",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "06:44.3" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "broll_legacy_gpus.mp4" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]


configs["episodes"].append(\
{ "title": "Bye",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "06:52.2" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "broll_legacy_gpus.mp4" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]





#scriptedvided.makeVideoForEpisode(configs["episodes"][1], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][4], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][11], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][12], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][13], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][8], configs)
#print(scriptedvided.makeVideoForEpisode(configs["episodes"][9], configs))
#print(scriptedvided.getSuitableVideoStream(configs["episodes"][9], configs))
#print (configs["youtube"])
#print(scriptedvided.getMusicCreditsString(configs["backgroundTrack"]))
#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "DOTA2"][0], configs)
#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "actual 1080 results"][0], configs)
#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "actual 900 results"][0], configs)
#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "actual 720 results"][0], configs)
#print (scriptedvided.getSuitableImage([x for x in configs["episodes"] if x["title"] == "actual 1080 results"][0], configs))

scriptedvided.makeVideo(configs)

# meeds better video, or maybe break it up