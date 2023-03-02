import scriptedvided

configs = { "defaultAudioFile" : "hd5770-2023.ogg",\
"mediaFolder" : "F:\\Videos\\hd5770_reference", \
"stockFolder" : "F:\\Videos\\stock",\
"benchmarkFile" : "F:\\Videos\\hd5770_reference\\Benchmark_hd5770_ref.txt",\
"outputFolder" : "F:\\Videos\\hd5770_reference\\output", \
"outputFile" : "hd5770_reference.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3",\
"timestamps" : ("00:30", None ), "destinationTimestamp" : {"title" : "Why retesting the HD 5770", "until" : "Alien: Isolation"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3",\
"timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Alien: Isolation", "until" : "Battlefield V"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3",\
"timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Battlefield V", "until" : "Rocket League"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3",\
"timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "Rocket League", "until" : "Usefulness of an old (D)GPU"}}, \
{"file" : "bensound-summer.mp3", "timestamps" : ("00:00", None ), "destinationTimestamp" : { "title": "Usefulness of an old (D)GPU", "until" : "Blooper" }}, \
], "volume" : 0.04 },\
"episodes" : [],\
"youtube" : {"title" : "Can an old Radeon still play games in 2023 (HD 5770)?", \
"description" : '''We decied to re-test the old AMD Radeon HD 5770 in 2023; with various game and windows updates, how well does the HD 5770 run today, compared to a year ago?''',\
"links" : '''
Our review of the HD 5770 from a year ago (2022): https://www.youtube.com/watch?v=-1eIjIxfx0k
Our review of the HD 5870: https://youtu.be/RGXJdRJkStE

Iceberg Tech's review of UHD 730: https://www.youtube.com/watch?v=5xvRPxVMQ1k

TechPowerup entry: https://www.techpowerup.com/gpu-specs/radeon-hd-5770.c250

Intel 11th gen processors, to illustrate the costs of an IGPU:
The core i5 11400 (has an IGPU): https://ark.intel.com/content/www/us/en/ark/products/212270/intel-core-i511400-processor-12m-cache-up-to-4-40-ghz.html
The core i5 11400F (no IGPU): https://ark.intel.com/content/www/us/en/ark/products/212271/intel-core-i511400f-processor-12m-cache-up-to-4-40-ghz.html
''', \
"tags" : "AMD,ATI,Radeon,HD5770,HD 5770,TeraScale 2",\
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
{ "title": "Why retesting the HD 5770",\
"audio" : {"timestamps" : ("00:00", "00:09.6" ), "volume" : 0.999, "padding" : 0.25 },\
"video" : "review_r5770-pmd1g.mkv"\
})

configs["episodes"].append(\
{ "title": "5870_r6s_bad__AI_bad_CTD",\
"isChapter" : False,\
"audio" : {"timestamps" : ( "00:09.6", "00:25.1" ), "volume" : 0.999, "padding" : 0.25 },\
"video" : "5870_r__6__s_bad__Alien__Isolation_bad_CTD.mkv"\
})

configs["episodes"].append(\
{ "title": "the question becomes",\
"isChapter" : False,\
"audio" : {"timestamps" : ( "00:25.1", "00:39" ), "volume" : 0.999, "padding" : 0.25 },\
"video" : "hd5770_refDesign_breel.mp4"\
})

configs["episodes"].append(\
{ "title": "Specs for the test system",\
"audio" : {"timestamps" : ( "00:39", "00:53.5" ), "volume" : 0.999, "padding" : 0.25 },\
"video" : {"file":"Z230_closed.mp4", "rotation":180}\
})

configs["episodes"].append(\
{ "title": "GPU (and video card differences)",\
"audio" : {"timestamps" : ( "00:53.5" , "01:20" ), "volume" : 0.999, "padding" : 0.25 },\
"video" : {"file":"hd5770_refDesign_gpuz_specs_heaven.mp4", "start" : "01:10"}\
})

configs["episodes"].append(\
{ "title": "Cooling and thermals",\
"audio" : {"timestamps" : ("01:20", "01:35.3" ), "volume" : 0.999, "padding" : 0.25 },\
"video" : {"file":"hd5770_refDesign_cooling.mp4"}\
})

configs["episodes"].append(\
{ "title": "hd5770_heaven_gpuz_sensors",\
"isChapter" : False,\
"audio" : {"timestamps" : ( "01:35.3", "01:54" ), "volume" : 0.999, "padding" : 0.25 },\
"video" : {"file":"hd5770_heaven_gpuz_sensors.mp4"}\
})



configs["episodes"].append(\
{ "title": "Alien: Isolation",\
"audio" : {"timestamps" : ("01:54","02:35") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, ultra settings", \
    }\
}, \
"video" : "hd5870_A_lienIsolation.mkv"
})


configs["episodes"].append(\
{ "title": "Apex Legends",\
"audio" : {"timestamps" : ("02:35", "03:00" )  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "CoD Warzone",\
"audio" : {"timestamps" : ("03:00", "03:08" )  },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Battlefield V",\
"audio" : {"timestamps" : ("03:08", "03:35.3" ) },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Control",\
"audio" : {"timestamps" : ("03:35.3", "03:52.2") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Rainbow Six: Siege",\
"audio" : {"timestamps" : ("03:52.2", "04:28.8") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings, 50% render scale", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Grand Theft Auto V",\
"audio" : {"timestamps" : ("04:28.8",  "05:09") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1280x720, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Counter Strike: Global Offensive",\
"audio" : {"timestamps" : ( "05:09" , "05:29.4" ) },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "DOTA2",\
"audio" : {"timestamps" : ("05:29.4", "05:58.5") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings, 100% render scale", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Fortnite",\
"audio" : {"timestamps" : ("05:58.5", "06:29.5") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, performance mode, view distance FAR, 100% render scale", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Overwatch 2",\
"audio" : {"timestamps" : ( "06:29.5", "07:16.7") },\
"overlay" : { \
    "text" : ["'Overwatch 2'",\
              scriptedvided.r6sText('1920x1080, low settings, 100% render scale',55, 42),\
              scriptedvided.r6sText('1280x720, low settings, 100% render scale',104, 76),\
    ]\
}, \
"video" : "stock_Overwatch2_gameplay_5770" \
})

configs["episodes"].append(\
{ "title": "Rocket League",\
"audio" : {"timestamps" : ("07:16.7", "07:48.3") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings, 100% render scale", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Splitgate",\
"audio" : {"timestamps" : ("07:48.3", "08:22") },\
"overlay" : { \
    "text" : ["'Splitgate'",\
              scriptedvided.r6sText('1920x1080, low settings, 100% render scale',45, 27),\
              scriptedvided.r6sText('1920x1080, low settings, 70% render scale',74, 51),\
    ]\
}, \
})

configs["episodes"].append(\
{ "title": "Valorant",\
"audio" : {"timestamps" : ("08:22", "08:51.2") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Genshin Impact",\
"audio" : {"timestamps" : ("08:51.2", "09:21") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings, 1.0 render scale", \
    }\
}, \
})


configs["episodes"].append(\
{ "title": "HiRez Studios trio (Paladins, Realm Royale, Rogue Company)",\
"audio" : {"timestamps" : ("09:21", "09:36.4" ), "volume" : 0.999, "padding" : 0.25 },\
"video" : {"file":"HiRezTrio-P_aladins_R_ealmRoyale_R_ogueCompany.mp4"}\
})



configs["episodes"].append(\
{ "title": "Paladins",\
"isChapter" : False,\
"audio" : {"timestamps" : ("09:36.4", "09:42.3") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, high settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Realm Royale",\
"isChapter" : False,\
"audio" : {"timestamps" : ("09:42.3", "09:48.2") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, high settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Rogue Company",\
"isChapter" : False,\
"audio" : {"timestamps" : ("09:48.2", "09:55") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "World of Tanks Blitz",\
"audio" : {"timestamps" : ("09:55", "10:13.5") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, high settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Warframe",\
"audio" : {"timestamps" : ("10:13.5", "10:44.3") },\
"overlay" : { \
    "benchmark" : { \
        "settings" : "1920x1080, low settings", \
    }\
}, \
})

configs["episodes"].append(\
{ "title": "Usefulness of an old (D)GPU",\
"audio" : {"timestamps" : ("10:44.3", "11:07.8") },\
"video" : "icebergtech_uhd730.mkv"
})

configs["episodes"].append(\
{ "title": "R5_apu_igpu_price",\
"isChapter" : False,\
"audio" : {"timestamps" : ("11:07.8", "11:21.5") },\
"video" : "R5_apu_igpu_price.mp4"
})

configs["episodes"].append(\
{ "title": "10400-vs-10400f",\
"isChapter" : False,\
"audio" : {"timestamps" : ("11:21.5", "11:40.8") },\
"video" : "10400-vs-10400f.mkv"
})

configs["episodes"].append(\
{ "title": "pricing_hd5770",\
"isChapter" : False,\
"audio" : {"timestamps" : ( "11:40.8", "11:56") },\
"video" : {"file" : "pricing_hd5770.mkv", "start" : "00:00"}
})

configs["episodes"].append(\
{ "title": "Usefulness of the HD 5770",\
"audio" : {"timestamps" : ( "11:56", "12:16.7") },\
"video" : {"file" : "pricing_hd5770.mkv", "start" : "00:20"}
})

configs["episodes"].append(\
{ "title": "olx-hd5770-gt730",\
"isChapter" : False,\
"audio" : {"timestamps" : ( "12:16.7", "12:33.4") },\
"video" : {"file" : "olx-hd5770-gt730.mkv"}
})

configs["episodes"].append(\
{ "title": "TeraScale2-games-needing-windowed",\
"isChapter" : False,\
"audio" : {"timestamps" : ( "12:33.4", "12:43") },\
"video" : {"file" : "TeraScale2-games-needing-windowed.mkv"}
})

configs["episodes"].append(\
{ "title": "hd5870_AlienIsolation",\
"isChapter" : False,\
"audio" : {"timestamps" : ("12:43", "12:56") },\
"video" : {"file" : "hd5870_AlienIsolation.mkv"}
})

configs["episodes"].append(\
{ "title": "F_ortnite_lobby_f11",\
"isChapter" : False,\
"audio" : {"timestamps" : ( "12:56", "13:02") },\
"video" : {"file" : "F_ortnite_lobby_f11.mp4"}
})

configs["episodes"].append(\
{ "title": "google-gtaV-config-files",\
"isChapter" : False,\
"audio" : {"timestamps" : ("13:02", "13:08.5") },\
"video" : {"file" : "google-gtaV-config-files.mkv"}
})

configs["episodes"].append(\
{ "title": "game_config_files",\
"isChapter" : False,\
"audio" : {"timestamps" : ("13:08.5", "13:25") },\
"video" : {"file" : "game_config_files.mkv"}
})

configs["episodes"].append(\
{ "title": "hd5770-breels-sidebyside",\
"isChapter" : False,\
"audio" : {"timestamps" : ("13:25", "13:34.5") },\
"video" : {"file" : "hd5770-breels-sidebyside.mkv", "start" : "00:10"}
})

configs["episodes"].append(\
{ "title": "hd5770_refDesign_breel-thisIsIt",\
"isChapter" : False,\
"audio" : {"timestamps" : ("13:34.5", "13:40.5") },\
"video" : {"file" : "hd5770_refDesign_breel.mp4"}
})

configs["episodes"].append(\
{ "title": "Blooper",\
"isChapter" : False,\
"audio" : {"timestamps" : ( "13:40.5", "14:04.2") },\
"video" : {"file" : "HiRezTrio-Paladins_RealmRoyale_RogueCompany.mp4"}
})

scriptedvided.makeVideo(configs)

