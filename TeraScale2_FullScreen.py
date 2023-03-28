import scriptedvided

configs = { "defaultAudioFile" : "5770_FS.ogg",\
"mediaFolder" : "F:\\Videos\\hd5770_ref_FS", \
"stockFolder" : "F:\\Videos\\stock",\
"benchmarkFile" : "F:\\Videos\\hd5770_ref_FS\\Benchmark_hd5770_FS.txt",\
"outputFolder" : "F:\\Videos\\hd5770_ref_FS\\output", \
"outputFile" : "hd5770_ref_FS.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3",\
"timestamps" : ("00:30", None ), "destinationTimestamp" : {"title" : "I was wrong", "until" : "Back to full screen"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3",\
"timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Back to full screen", "until" : "TeraScale 2 can be used by Average Joe"}}, \
{"file" : "bensound-summer.mp3", "timestamps" : ("00:00", None ), "destinationTimestamp" : { "title": "TeraScale 2 can be used by Average Joe", "until" : "end-of-video" }}, \
], "volume" : 0.035 },\
"episodes" : [],\
"youtube" : {"title" : "Old Radeon HD5000/6000 games just fine in 2023 ", \
"description" : '''I was wrong when I concluded that the TeraScale 2 GPUs are no longer suitable for the regular PC user, because of the troubles related to running in full screen mode. However, I’m quite happy to  have to eat my own words.''',\
"links" : '''
Our 2023 review of the HD 5770 : 
Our review of the HD 5870: https://youtu.be/RGXJdRJkStE
''', \
"tags" : "AMD,ATI,Radeon,HD5770,HD 5770,TeraScale 2,HD6850,HD 6850",\
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

configs["episodes"].append(\
{ "title": "I was wrong",\
"audio" : {"timestamps" : ("00:00", "00:10.6" ), "volume" : 0.999, "padding" : 0.25 },\
"video" : {"file" : "conclusion-hd5770-2023.mp4", "start" : "00:55"}\
})

configs["episodes"].append(\
{ "title": "Radeon HD 5000 and 6000, end of 2022 to early 2023",\
"audio" : {"timestamps" : ("00:10.6" ,"00:31.75" ), "volume" : 0.999, "padding" : 0.25 },\
"video" : "5870_r__6__s_bad__Alien__Isolation_bad_CTD.mkv"\
})

configs["episodes"].append(\
{ "title": "5770 begining of 2023",\
"isChapter" : False,\
"audio" : {"timestamps" : ("00:31.75", "00:47.5" ), "volume" : 0.999, "padding" : 0.25 },\
"video" : "stock_RocketLeague_1080pLower.mp4"\
})

configs["episodes"].append(\
{ "title": "Back to full screen",\
"audio" : {"timestamps" : ( "00:47.5", "01:06.8" ), "volume" : 0.999, "padding" : 1 },\
"video" : {"file" : "A_lienIsolation_fs_hd6850_2023.mp4", "start" : "00:00"}\
})

configs["episodes"].append(\
{ "title": "GTA V___BF V",\
"isChapter" : False,\
"audio" : {"timestamps" : ("01:06.8", "01:14.9" ), "volume" : 0.999 },\
"video" : "gtav_bfv.mp4"\
})

configs["episodes"].append(\
{ "title": "Valorant___Fortnite",\
"isChapter" : False,\
"audio" : {"timestamps" : ( "01:14.9", "01:19" ), "volume" : 0.999 },\
"video" : "valorant_fortnite.mp4"\
})

configs["episodes"].append(\
{ "title": "Rocket____league",\
"isChapter" : False,\
"audio" : {"timestamps" : ( "01:19", "01:25.3" ), "volume" : 0.999 },\
"video" : {"file": "stock_RocketLeague_1080pLower.mp4", "start" : "00:05"}\
})

configs["episodes"].append(\
{ "title": "Will the HD 5770 work in full screen?",\
"audio" : {"timestamps" : ( "01:25.3", "01:36.8" ), "volume" : 0.999 },\
"video" : "hd5770-breels-sidebyside.mkv"\
})

configs["episodes"].append(\
{ "title": "Yes - it works",\
"isChapter" : False,\
"audio" : {"timestamps" : (  "01:36.8", "01:47.5" ), "volume" : 0.999 },\
"video" : "valorant_apex_ai.mp4"\
})

configs["episodes"].append(\
{ "title": "FS stats",\
"isChapter" : False,\
"audio" : {"timestamps" : (  "01:47.5", "01:58.2"), "volume" : 0.999 },\
"video" : {"file" : "A_lienIsolation_fs_hd6850_2023.mp4", "start" : "00:00"}\
})

configs["episodes"].append(\
{ "title": "Grand Theft Auto V",\
"audio" : {"timestamps" : ("01:58.2", "02:10.4"), "volume" : 0.999 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Rainbow Six: Siege",\
"audio" : {"timestamps" : ("02:10.4", "02:27.4"), "volume" : 0.999 },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings, 50% render scale", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Alien: Isolation",\
"audio" : {"timestamps" : ("02:27.4", "02:46") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, ultra settings", \
    }\
}, \
"video" : "stock_Alien_Isolation_1080p.mp4",\
})

configs["episodes"].append(\
{ "title": "TeraScale 2 can be used by Average Joe",\
"audio" : {"timestamps" : ( "02:46", "02:58.7" ), "volume" : 0.999 },\
"video" : "hd5770_refDesign_breel.mp4"\
})

configs["episodes"].append(\
{ "title": "Recommendation for 2023 review",\
"isChapter" : False,\
"audio" : {"timestamps" : (  "02:58.7", "03:20" ), "volume" : 0.999 },\
"video" : "hd5770-breels-sidebyside.mkv"\
})


##configs["episodes"].append(\
##{ "title": "Blooper",\
##"isChapter" : False,\
##"audio" : {"timestamps" : ( "13:40.5", "14:04.2") },\
##"video" : {"file":"HiRezTrio-P_aladins_R_ealmRoyale_R_ogueCompany.mp4"}\
##})

scriptedvided.makeVideo(configs)

