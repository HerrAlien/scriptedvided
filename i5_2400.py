import scriptedvided

configs = { "defaultAudioFile" : "i5_2400.ogg",\
"mediaFolder" : "F:\\Videos\\i5_2400", \
"stockFolder" : "F:\\Videos\\stock",\
"outputFolder" : "F:\\Videos\\i5_2400\\output", \
"outputFile" : "i5_2400.mp4", \
"benchmarkFile" : "F:\\Videos\\i5_2400\\Benchmark_i5_2400.txt",\
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#00008080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "Going full potato", "until" : "Alien Isolation"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Alien Isolation", "until" : "Counter-Strike 2"}}, \
{"file" : "Inspired - MaikonMusic  Free Background Music  Audio Library Release.mp3", "timestamps" : ("00:00", None ), "destinationTimestamp" : {"title" : "Counter-Strike 2", "until" : "Splitgate"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Splitgate", "until" : "After disabling SPECTRE and MELTDOWN patches"}}, \
{"file" : "Wait For Me  Jeff The Second (No Copyright Music).mp3", "timestamps" : ("00:35", None ), "destinationTimestamp" : {"title" : "After disabling SPECTRE and MELTDOWN patches", "until" : "Is it worth buying?"}}, \
{"file" : "Guide You Home - Ferco and Andie - Free Background Music - Audio Library Release.ogg", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "Is it worth buying?", "until" : "Blooper"}}, \
], "volume" : 0.06 },\
"episodes" : [],\
"youtube" : {"title" : "Single digit USD priced CPU in 2024 (i5 2400)", \
"description" : '''We'll be exploring how the 2nd gen Intel core i5 2400 run today.''',\
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

Wait For Me - Jeff The Second  https://www.youtube.com/watch?v=YuBBSQI2XDQ&t=0s
Creative Commons Attribution
Free Download / Stream: https://bit.ly/3LLKFj0
Music promoted by Audio Library   
https://www.youtube.com/watch?v=YuBBSQI2XDQ&t=0s

Track: Guide You Home - Ferco & Andie [Audio Library Release]
Music provided by Audio Library Plus
Watch: https://www.youtube.com/watch?v=16eNerPDIsU&t=0s
Free Download / Stream: https://alplus.io/guide-you-home

''', \
"tags" : "Sandy Bridge,Intel,i5 2400,Spectre,Meltdown,Inspectre",\
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
{ "title": "Going full potato",\
"audio" : {"timestamps" : (lastTS, "00:12.3" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "X79-andys-tech.mp4", "start" : "00:01" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "The test platform",\
"audio" : {"timestamps" : (lastTS, "00:35" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "breel_SandyBridge_outside.mp4" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]


## this might need breaking up ...
configs["episodes"].append(\
{ "title": "The i5 2400",\
"isChapter" : False, \
"overlay" : { \
    "text" : ["'Cores\: 4'",\
              "'Threads\: 4'",\
              "'Base Frequency\: 3.1 GHz'",\
              "'Max Turbo Frequency\: 3.4 GHz'",\
    ]\
}, \
"audio" : {"timestamps" : (lastTS, "01:07" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "ark_i5_2400.mp4" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]
#####

## record inspectre on the 2400
configs["episodes"].append(\
{ "title": "Downloading extra performance with Inspectre",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "01:23.4" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "inspectre_off.mp4" , "start" : "00:00" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "System RAM",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "01:41.6" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "breel_RAM_4x4GB.mp4", "start" : "00:08" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "GPU",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "01:58.7" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "broll_GTX1050Ti_outside.mp4" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "shot with the case",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "02:16.3" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "breel_i5_2400_case_3.mp4" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Drake meme with the PSUs",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "02:29.2" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "PSUs_drakeMeme_input.mp4" , "start" : "00:05"},\
"overlay" : { "image" : {"file" : "drake_meme.png", "chromaColor" : "0x00FF00"}\
}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Game settings",\
"overlay" : { \
    "text" : ["'1280x720 resolution'",\
              "'50\\\% or less 3D scale, when available'",\
              "'lowest settings'",\
    ]\
}, \
"audio" : {"timestamps" : (lastTS, "02:57.1" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "lowRes_4nite.mp4" , "start" : "00:10"},\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]


configs["episodes"].append(\
{ "title": "Alien Isolation",\
"audio" : {"timestamps" : (lastTS, "03:13" ), "padAudio" : 0.1 },\
"overlay" : {  "benchmark" : { \
        "settings" : "1280x720, low settings", \
}}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Grand Theft Auto V",\
"audio" : {"timestamps" : (lastTS, "03:28.2" ), "padAudio" : 0.1 },\
"overlay" : {  "benchmark" : { \
        "settings" : "1280x720, low settings", \
}}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Control",\
"audio" : {"timestamps" : (lastTS, "03:43.7" ), "padAudio" : 0.1 },\
"overlay" : {  "benchmark" : { \
        "settings" : "1280x720, low settings", \
}}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Resident Evil 4 (Remake)",\
"audio" : {"timestamps" : (lastTS, "04:02.6" ), "padAudio" : 0.1 },\
"overlay" : {  "benchmark" : { \
        "settings" : "1280x720, 50% render scale, low settings", \
}}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Warframe",\
"audio" : {"timestamps" : (lastTS, "04:20" ), "padAudio" : 0.1 },\
"overlay" : {  "benchmark" : { \
        "settings" : "1280x720, low settings", \
}}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Battlefield V",\
"audio" : {"timestamps" : (lastTS, "04:36" ), "padAudio" : 0.1 },\
"overlay" : {  "benchmark" : { \
        "settings" : "1280x720, 50% render scale, low settings", \
}}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Apex Legends",\
"audio" : {"timestamps" : (lastTS, "05:01" ), "padAudio" : 0.1 },\
"overlay" : { "image" : {"file" : "Apex Legends.png", "chromaColor" : "0x00FF00"}\
}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Fortnite",\
"audio" : {"timestamps" : (lastTS, "05:29.6" ), "padAudio" : 0.1 },\
"overlay" : {  "benchmark" : { \
        "settings" : "1280x720, 30% 3D scale, FAR render distance, performance mode", \
}}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Rocket League",\
"audio" : {"timestamps" : (lastTS, "05:44.4" ), "padAudio" : 0.1 },\
"overlay" : {  "benchmark" : { \
        "settings" : "1280x720, low settings", \
}}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "The Finals",\
"audio" : {"timestamps" : (lastTS, "06:24.5" ), "padAudio" : 0.1 },\
"overlay" : { "image" : {"file" : "The Finals.png", "chromaColor" : "0x00FF00"}\
}})

lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Rainbow Six: Siege",\
"audio" : {"timestamps" : (lastTS, "06:51.4" ), "padAudio" : 0.1 },\
"overlay" : { "image" : {"file" : "Rainbow Six Siege.png", "chromaColor" : "0x00FF00"}\
}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Counter-Strike 2",\
"audio" : {"timestamps" : (lastTS, "07:22.6" ), "padAudio" : 0.1 },\
"overlay" : { "image" : {"file" : "Counter Strike 2.png", "chromaColor" : "0x00FF00"}\
}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Valorant",\
"audio" : {"timestamps" : (lastTS, "07:49.8" ), "padAudio" : 0.1 },\
"overlay" : { "image" : {"file" : "Valorant.png", "chromaColor" : "0x00FF00"}\
}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "DOTA2",\
"audio" : {"timestamps" : (lastTS, "08:02.8" ), "padAudio" : 0.1 },\
"overlay" : {  "benchmark" : { \
        "settings" : "1280x720, low settings", \
}}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Overwatch 2",\
"audio" : {"timestamps" : (lastTS, "08:21.8" ), "padAudio" : 0.1 },\
"overlay" : {  "benchmark" : { \
        "settings" : "1280x720, 50% 3D scale, low settings", \
}}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Paladins, Realm Royale and Rogue Company",\
"video" : {"file":"HiRezTrio-P_aladins_R_ealmRoyale_R_ogueCompany.mp4"},\
"audio" : {"timestamps" : (lastTS, "08:26.3" ), "padAudio" : 0.1 },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Paladins",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "08:31.85" ), "padAudio" : 0.1 },\
"overlay" : {  "benchmark" : { \
        "settings" : "1280x720, low settings", \
}}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Realm Royale",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "08:38.45" ), "padAudio" : 0.1 },\
"overlay" : {  "benchmark" : { \
        "settings" : "1280x720, low settings", \
}}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Rogue Company",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "08:48.6" ), "padAudio" : 0.1 },\
"overlay" : {  "benchmark" : { \
        "settings" : "1280x720, low settings", \
}}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Splitgate",\
"audio" : {"timestamps" : (lastTS, "09:08.7" ), "padAudio" : 0.1 },\
"overlay" : { \
    "text" : ["'Splitgate'",\
              scriptedvided.r6sText('1280x720, low settings, 100% render scale', 220,  42),\
              scriptedvided.r6sText('1280x720, low settings, 50% render scale', 229,  51),\
    ]\
}, \
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "World of Tanks Blitz",\
"audio" : {"timestamps" : (lastTS, "09:21" ), "padAudio" : 0.1 },\
"overlay" : {  "benchmark" : { \
        "settings" : "1280x720, low settings", \
}}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]


configs["episodes"].append(\
{ "title": "After disabling SPECTRE and MELTDOWN patches",\
"audio" : {"timestamps" : (lastTS, "09:34.5" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "inspectre_on.mp4" , "start" : "00:00"},\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

### manually specify videos here!

configs["episodes"].append(\
{ "title": "Fortnite (retested)",\
"isChapter" : False, \
"video" : {"file" : "stock_FortniteClient-Win_2023_12_24.mp4" , "start" : "08:40"},\
"audio" : {"timestamps" : (lastTS, "09:48.6" ), "padAudio" : 0.1 },\
"overlay" : { "image" : {"file" : "Fortnite_inspectre.png", "chromaColor" : "0x00FF00"}\
}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]


configs["episodes"].append(\
{ "title": "Rainbow Six: Siege (retested)",\
"isChapter" : False, \
"video" : {"file" : "stock_RainbowSixSiege_benchmark2.mp4"},\
"audio" : {"timestamps" : (lastTS, "10:01.6" ), "padAudio" : 0.1 },\
"overlay" : { "image" : {"file" : "Rainbow Six Siege_inspectre.png", "chromaColor" : "0x00FF00"}\
}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Apex Legends (retested)",\
"video" : {"file" : "stock_ApexLegends_long.mp4" , "start" : "01:20"},\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "10:16.7" ), "padAudio" : 0.1 },\
"overlay" : { "image" : {"file" : "Apex Legends_inspectre.png", "chromaColor" : "0x00FF00"}\
}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Valorant (retested)",\
"isChapter" : False, \
"video" : {"file" : "stock_VALORANT_r7_265_2023.mp4" , "start" : "00:10"},\
"audio" : {"timestamps" : (lastTS, "10:31.85" ), "padAudio" : 0.1 },\
"overlay" : { "image" : {"file" : "Valorant_inspectre.png", "chromaColor" : "0x00FF00"}\
}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Counter-Strike 2 (retested)",\
"isChapter" : False, \
"video" : {"file" : "stock_cs2_CT_gt1030lp.mp4" , "start" : "01:30"},\
"audio" : {"timestamps" : (lastTS, "10:43.4" ), "padAudio" : 0.1 },\
"overlay" : { "image" : {"file" : "Counter Strike 2_inspectre.png", "chromaColor" : "0x00FF00"}\
}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "Is it worth buying?",\
"audio" : {"timestamps" : (lastTS, "11:02.2" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "breel_SandyBridge_outside.mp4" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "very cheap - price",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "11:17" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "i5_2400_olx.mkv" },\
})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

## might need a longer video file
configs["episodes"].append(\
{ "title": "Comparison to Haswell",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "11:44.8" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "blurred_Finals.mp4" },\
"overlay" : { "image" : {"file" : "MORE_THAN_FREQUENCIES3.png", "chromaColor" : "0x00FF00"}\
}})
lastTS = configs["episodes"][-1]["audio"]["timestamps"][1]

configs["episodes"].append(\
{ "title": "bye",\
"isChapter" : False, \
"audio" : {"timestamps" : (lastTS, "12:04" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "breel_SandyBridge_outside.mp4" },\
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
#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "Alien Isolation"][0], configs)
#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "actual 1080 results"][0], configs)
#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "actual 900 results"][0], configs)
#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "actual 720 results"][0], configs)
#print (scriptedvided.getSuitableImage([x for x in configs["episodes"] if x["title"] == "actual 1080 results"][0], configs))

scriptedvided.makeVideo(configs)

# meeds better video, or maybe break it up