import scriptedvided

configs = { "defaultAudioFile" : "repair_xfx_6850_2.ogg",\
"mediaFolder" : "F:\\Videos\\repair_xfx_6850", \
"stockFolder" : "F:\\Videos\\stock",\
"benchmarkFile" : None,\
"outputFolder" : "F:\\Videos\\repair_xfx_6850\\output", \
"outputFile" : "repair_xfx_hd6850.mp4", \
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3",\
"timestamps" : ("00:30", None ), "destinationTimestamp" : {"title" : "The TLDW", "until" : "The CTF circuitry"}}, \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3",\
"timestamps" : ("00:30", None ), "destinationTimestamp" : {"title" : "The CTF circuitry", "until" : "Replace the LDO"}}, \
{"file" : "bensound-summer.mp3", "timestamps" : ("00:00", None ), "destinationTimestamp" : { "title": "Replace the LDO", "until" : "end of video" }}, \
], "volume" : 0.05 },\
"episodes" : [],\
"youtube" : {"title" : "Learning about LDOs while fixing this Radeon HD 6850", \
"description" : '''One valuable lesson from this HD 6850 repair is that there are a lot of chips that are pin compatible with each other - LDOs in this case.''',\
"links" : '''
Repair channels:
https://www.youtube.com/c/LearnElectronicsRepair
https://www.youtube.com/channel/UCKU5nwSWYXa3xfXGBlKyvdw
https://www.youtube.com/c/TechCemetery
https://www.youtube.com/c/TheCod3r
''', \
"tags" : "AMD,ATI,Radeon,TeraScale 2,HD6850,HD 6850,LDO,PEX_VDD",\
"language" : "EN", \
"Caption certification" : "None",\
"recording date" : None,\
"video location" : None, \
"category" : "Science & Technology", \
"subtitles" : None, \
"endscreen" : None, \
"cards" : None, \
}\
}

configs["episodes"].append(\
{ "title": "The TLDW",\
"audio" : {"timestamps" : ("00:00", "00:10.6" ), "volume" : 0.999 },\
"video" : {"file" : "xfx_hd6850_bb_card.mp4", "rotation" : 180}\
})

configs["episodes"].append(\
{ "title": "not quite the ad video",\
"isChapter" : False, \
"audio" : {"timestamps" : ("00:10.6" ,"00:45" ), "volume" : 0.999 },\
"video" : "xfx_hd6850_proba_video.mp4"\
})

configs["episodes"].append(\
{ "title": "Resistance measurements",\
"audio" : {"timestamps" : ("00:45" ,"01:03.5" ), "volume" : 0.999 },\
"video" : "hd6850_resistance_measurements.mkv"\
})

configs["episodes"].append(\
{ "title": "First power up",\
"audio" : {"timestamps" : ("01:03.5" , "01:18.6"), "volume" : 0.999 },\
"video" : "initial_powerup_nope.mp4"\
})

configs["episodes"].append(\
{ "title": "Investigate the phase controller",\
"audio" : {"timestamps" : ("01:18.6", "01:34.6"), "volume" : 0.999 },\
"video" : "apw7088.mkv"\
})

configs["episodes"].append(\
{ "title": "list of voltages to check",\
"isChapter" : False, \
"audio" : {"timestamps" : ("01:34.6" , "01:58.5"), "volume" : 0.999 },\
"video" : "list_voltages_check.mkv"\
})

configs["episodes"].append(\
{ "title": "the soft start pin",\
"isChapter" : False, \
"audio" : {"timestamps" : ("01:58.5","02:11"), "volume" : 0.999 },\
"video" : "datasheet_soft_start.mkv"\
})

configs["episodes"].append(\
{ "title": "what components are connected to the SS",\
"isChapter" : False, \
"audio" : {"timestamps" : ("02:11","02:32"), "volume" : 0.999 },\
"video" : "q1008_q210.mkv"\
})

configs["episodes"].append(\
{ "title": "partial schematics of the circuitry",\
"isChapter" : False, \
"audio" : {"timestamps" : ("02:32","02:48"), "volume" : 0.999 },\
"video" : "power_sensing_spice.mkv"\
})

configs["episodes"].append(\
{ "title": "Q210",\
"isChapter" : False, \
"audio" : {"timestamps" : ("02:48", "03:21"), "volume" : 0.999 },\
"video" : "ctf_spice.mkv"\
})

configs["episodes"].append(\
{ "title": "the base of Q210 being high",\
"isChapter" : False, \
"audio" : {"timestamps" : ("03:21", "03:31.4"), "volume" : 0.999 },\
"video" : "6850_powerSensingOK.mkv"\
})

configs["episodes"].append(\
{ "title": "shorting the pads labeled R241",\
"isChapter" : False, \
"audio" : {"timestamps" : ("03:31.4","03:42.5"), "volume" : 0.999 },\
"video" : "short_r241.mkv"\
})

configs["episodes"].append(\
{ "title": "Yet, we had no picture",\
"isChapter" : False, \
"audio" : {"timestamps" : ("03:42.5","04:09.5"), "volume" : 0.999 },\
"video" : "initial_powerup_nope.mp4"\
})

configs["episodes"].append(\
{ "title": "The CTF circuitry",\
"audio" : {"timestamps" : ("04:09.5","04:26.5"), "volume" : 0.999 },\
"video" : "prioritized_ctf.mkv"\
})

configs["episodes"].append(\
{ "title": "what MSI uses for some of their Polaris cards",\
"isChapter" : False, \
"audio" : {"timestamps" : ("04:26.5","05:03"), "volume" : 0.999 },\
"video" : "ctf_polaris.mkv"\
})

configs["episodes"].append(\
{ "title": "13K resistor on my favourite donor board",\
"isChapter" : False, \
"audio" : {"timestamps" : ("05:03","05:23.8"), "volume" : 0.999 },\
"video" : "search_of_13k.mkv"\
})

configs["episodes"].append(\
{ "title": "searched for a 10K resistor",\
"isChapter" : False, \
"audio" : {"timestamps" : ("05:23.8","05:38.5"), "volume" : 0.999 },\
"video" : "search_for_10k.mkv"\
})

configs["episodes"].append(\
{ "title": "CTF fixed",\
"isChapter" : False, \
"audio" : {"timestamps" : ("05:38.5", "05:57"), "volume" : 0.999 },\
"video" : "10k_placed.mp4"\
})

configs["episodes"].append(\
{ "title": "Ooh 300 (U300)",\
"audio" : {"timestamps" : ("05:57", "06:19"), "volume" : 0.999 },\
"video" : "U300_is_bad.mkv"\
})

configs["episodes"].append(\
{ "title": "a replacement for the APL5920",\
"isChapter" : False, \
"audio" : {"timestamps" : ("06:19", "06:52.6"), "volume" : 0.999 },\
"video" : "anpec_uP7701.mkv"\
})

configs["episodes"].append(\
{ "title": "7103",\
"isChapter" : False, \
"audio" : {"timestamps" : ("06:52.6", "07:05.6"), "volume" : 0.999 },\
"video" : "anpec_gs7103.mkv"\
})

configs["episodes"].append(\
{ "title": "NCT3730S",\
"isChapter" : False, \
"audio" : {"timestamps" : ("07:05.6", "07:25.2"), "volume" : 0.999 },\
"video" : "anpec_nuvoton.mkv"\
})

configs["episodes"].append(\
{ "title": "Replace the LDO",\
"audio" : {"timestamps" : ("07:25.2", "07:28.1"), "volume" : 0.999 },\
"video" : "black_screen.mkv"\
})

configs["episodes"].append(\
{ "title": "desoldered the bad 2 amps Anpec",\
"isChapter" : False, \
"audio" : {"timestamps" : ("07:28.1","07:33"), "volume" : 0.999, "padding" : 0.25 },\
"video" : {"file" : "LDO_old_removed.mp4", "rotation" : -90}\
})

configs["episodes"].append(\
{ "title": "desoldered one of the nuvoTon chips",\
"isChapter" : False, \
"audio" : {"timestamps" : ("07:33" , "07:38.6"), "volume" : 0.999, "padding" : 0.25 },\
"video" : "LDO_donor.mp4"\
})

configs["episodes"].append(\
{ "title": "soldered in place the 3 amps LDO",\
"isChapter" : False, \
"audio" : {"timestamps" : ("07:38.6","07:51.3"), "volume" : 0.999, "padding" : 0.25 },\
"video" : {"file" : "LDO_placed.mp4", "rotation" : -90}\
})

configs["episodes"].append(\
{ "title": "Finally working",\
"audio" : {"timestamps" : ("07:51.3","07:59.5"), "volume" : 0.999, "padding" : 0.25 },\
"video" : "working_powerup.mp4"\
})

configs["episodes"].append(\
{ "title": "Heaven ran fine",\
"isChapter" : False, \
"audio" : {"timestamps" : ("07:59.5","08:12.5"), "volume" : 0.999, "padding" : 1 },\
"video" : "xfx_hd6850_heaven-gpuz-repair.mp4"\
})


#configs["episodes"].append(\
#{ "title": "The GTX 770",\
#"isChapter" : False, \
#"audio" : {"timestamps" : ("00:39.7", "00:48.6"), "volume" : 0.999 },\
#"video" : {"file" : "gtx770_bb_V_alorant.mp4", "start" : "00:00" }\
#})


#scriptedvided.makeVideoForEpisode(configs["episodes"][0], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][9], configs)
#scriptedvided.makeVideoForEpisode(configs["episodes"][8], configs)
#print(scriptedvided.makeVideoForEpisode(configs["episodes"][9], configs))
#print(scriptedvided.getSuitableVideoStream(configs["episodes"][9], configs))
#print (configs["youtube"])
#print(scriptedvided.getMusicCreditsString(configs["backgroundTrack"]))
#scriptedvided.makeVideoForEpisode([x for x in configs["episodes"] if x["title"] == "Lane 6 fixed"][0], configs)
scriptedvided.makeVideo(configs)


