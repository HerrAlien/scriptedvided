import scriptedvided

configs = { "defaultAudioFile" : "",\
"mediaFolder" : "F:\\Videos\\4memes4Fortnite", \
"stockFolder" : "F:\\Videos\\stock",\
"benchmarkFile" : "not needed",\
"outputFolder" : "F:\\Videos\\4memes4Fortnite\\output", \
"outputFile" : "4memes4Fortnite.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "", "until" : "Rainbow Six: Siege"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Rainbow Six: Siege", "until" : "Fortnite"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Fortnite", "until" : "Conclusions"}}, \
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
{ "title": "This is not a BUY recommendation",\
"audio" : {"timestamps" : ("00:00", "00:09" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "broll_4meme_cards_porch_hd5770_hd6670_gt730_r7_250.MP4"},\
})

## HD5770
configs["episodes"].append(\
{ "title": "The GPUs",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:21.8" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "broll_4meme_cards_porch_hd5770.MP4"},\
})

configs["episodes"].append(\
{ "title": "HD6670",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:34.1" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "broll_4meme_cards_porch_gt730_hd6670.MP4", "start" : "00:06"},\
})

configs["episodes"].append(\
{ "title": "GT730",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:44.6" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "broll_4meme_cards_porch_gt730_hd6670.MP4", "start" : "00:40"},\
})

configs["episodes"].append(\
{ "title": "R7 250",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:15.1" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "broll_4meme_cards_porch_r7_250.MP4", "start" : "00:16"},\
})

# the game, fortnite 
configs["episodes"].append(\
{ "title": "Test setup",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:23.5" ), "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "Fortnite_C6S1_2025_01_30_p1.mp4", "start" : "01:30"},\
})

configs["episodes"].append(\
{ "title": "The test system",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:39.7" ), "volume" : 0.999, "padAudio" : 0.05 },\
"overlay" : { \
    "text" : ["'Custom build'",\
              "'CPU\: Ryzen 5 3600'",\
              "'RAM\: 32GB DDR4 at 3000 MHz, dual channel'",\
    ]\
}, \
"video" : {"file" : "test_system_noGPU.mp4" }\
})

####################### end of intro ###############################

####################### gaming section ###############################
configs["episodes"].append(\
{ "title": "Fortnite, Chapter 6 Season 1",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:49.6" ), "padAudio" : 0.05 },\
"video" : {"file" : "Fortnite_C6S1_2025_01_30_p1.mp4", "start" : "02:00"} \
})

configs["episodes"].append(\
{ "title": "1080p C6S1",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:14.2" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : "Fortnite (C6S1), 1920x1080, performance mode.png", "chromaColor" : "0x00FF00"}\
}, \
"video" : {"file" : "Fortnite_C6S1_2025_01_30_p1.mp4", "start" : "02:10"} \
})

configs["episodes"].append(\
{ "title": "900p C6S1",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:34.6" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : "Fortnite (C6S1), 1600x900, performance mode.png", "chromaColor" : "0x00FF00"}\
}, \
"video" : {"file" : "Fortnite_C6S1_2025_01_30_p1.mp4", "start" : "02:35"} \
})

configs["episodes"].append(\
{ "title": "720p C6S1",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:07" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : "Fortnite (C6S1), 1280x720, performance mode.png", "chromaColor" : "0x00FF00"}\
}, \
"video" : {"file" : "Fortnite_C6S1_2025_01_30_p1.mp4", "start" : "02:55"} \
})

configs["episodes"].append(\
{ "title": "Fortnite OG, Chapter 1 Season 1",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:22" ), "padAudio" : 0.05 },\
"video" : {"file" : "OG_F_ortnite.mp4", "start" : "00:00"} \
})

configs["episodes"].append(\
{ "title": "1080p OG C1S1",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:50.3" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : "Fortnite OG (C1S1), 1920x1080, performance mode.png", "chromaColor" : "0x00FF00"}\
}, \
"video" : {"file" : "OG_F_ortnite.mp4", "start" : "00:15"} \
})

configs["episodes"].append(\
{ "title": "900p OG C1S1",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:27.7" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : "Fortnite OG (C1S1), 1600x900, performance mode.png", "chromaColor" : "0x00FF00"}\
}, \
"video" : {"file" : "OG_F_ortnite.mp4", "start" : "00:33"} \
})

configs["episodes"].append(\
{ "title": "720p OG C1S1",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:03.7" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : "Fortnite OG (C1S1), 1280x720, performance mode.png", "chromaColor" : "0x00FF00"}\
}, \
"video" : {"file" : "OG_F_ortnite.mp4", "start" : "01:10"} \
})

configs["episodes"].append(\
{ "title": "Fortnite Reload",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:17" ), "padAudio" : 0.05 },\
"video" : {"file" : "F_ortnite_Reload_2024_12_06.mp4", "start" : "00:00"} \
})

configs["episodes"].append(\
{ "title": "1080p Reload",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:45.1" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : "Fortnite Reload, 1920x1080, performance mode.png", "chromaColor" : "0x00FF00"}\
}, \
"video" : {"file" : "F_ortnite_Reload_2024_12_06.mp4", "start" : "00:14"} \
})

configs["episodes"].append(\
{ "title": "900p Reload",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:23.5" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : "Fortnite Reload, 1600x900, performance mode.png", "chromaColor" : "0x00FF00"}\
}, \
"video" : {"file" : "F_ortnite_Reload_2024_12_06.mp4", "start" : "00:42"} \
})

configs["episodes"].append(\
{ "title": "720p Reload",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:02.3" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : "Fortnite Reload, 1280x720, performance mode.png", "chromaColor" : "0x00FF00"}\
}, \
"video" : {"file" : "F_ortnite_Reload_2024_12_06.mp4", "start" : "01:21"} \
})

configs["episodes"].append(\
{ "title": "Fortnite Ballistic",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:25.9" ), "padAudio" : 0.05 },\
"video" : { "file" : "4meme_cards_F_nite_Ballistic_fullRound.mp4" , "start" : "00:00" }\
})

configs["episodes"].append(\
{ "title": "1080p Ballistic",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:02.4" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : "Fortnite Ballistic, 1920x1080, performance mode.png", "chromaColor" : "0x00FF00"}\
}, \
"video" : { "file" : "4meme_cards_F_nite_Ballistic_fullRound.mp4" , "start" : "00:22" }\
})

configs["episodes"].append(\
{ "title": "900p Ballistic",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "08:33.8" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : "Fortnite Ballistic, 1600x900, performance mode.png", "chromaColor" : "0x00FF00"}\
}, \
"video" : { "file" : "4meme_cards_F_nite_Ballistic_4.mp4" , "start" : "00:22" }\
})

configs["episodes"].append(\
{ "title": "720p Ballistic",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "09:17.8" ), "padAudio" : 0.05 },\
"overlay" : { \
    "image" : {"file" : "Fortnite Ballistic, 1280x720, performance mode.png", "chromaColor" : "0x00FF00"}\
}, \
"video" : { "file" : "4meme_cards_F_nite_Ballistic.mp4" , "start" : "00:18" }\
})

####################### end of gaming section ###############################

####################### conclusion ###############################
# really need an upgrade
configs["episodes"].append(\
{ "title": "Time waits for no GPU",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "09:37" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "broll_4meme_cards_porch_hd5770_hd6670_gt730_r7_250.MP4"},\
})

configs["episodes"].append(\
{ "title": "Other games got heavy",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "09:47.4" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : "GImpact_2022_2023.mp4", "start" : "00:00"},\
})

configs["episodes"].append(\
{ "title": "Normal trend HW SW",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "09:55.4" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "Live service games",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "10:03.2" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "HD5770 vs GT 730 - not a display adapter",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "10:25.1" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "HD5770 - The gap",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "10:39.3" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "HD5770 - Maybe retro",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "10:49.3" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "bye",\
"isChapter" : False,\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "11:01" ),  "volume" : 0.999, "padAudio" : 0.05 },\
"video" : {"file" : ""},\
})


##configs["episodes"].append(\
##{ "title": "Blooper",\
##"isChapter" : False,\
##"audio" : {"timestamps" : ( "13:40.5", "14:04.2") },\
##"video" : {"file":"HiRezTrio-P_aladins_R_ealmRoyale_R_ogueCompany.mp4"}\
##})

#scriptedvided.makeVideoForEpisode(configs["episodes"][7], configs)
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
#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "Borderlands 3"][0], configs)
#scriptedvided.makeVideo(configs)

#for x in range(19,26):
#    scriptedvided.makeVideoForEpisode(configs["episodes"][x], configs)
#
scriptedvided.makeVideo(configs)

