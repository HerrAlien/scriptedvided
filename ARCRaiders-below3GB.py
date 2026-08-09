import scriptedvided

configs = { "defaultAudioFile" : "",\
"mediaFolder" : "F:\\Videos\\ARCRaiders-below3G", \
"stockFolder" : "F:\\Videos\\stock",\
"outputFolder" : "F:\\Videos\\ARCRaiders-below3G\\output", \
"outputFile" : "ARCRaiders-below3G.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
"backgroundTrack" : { "audioTracks" : [ \
{"file" : "Bliss Of Heaven - SOMM [Audio Library Release]-Free Copyright-safe Music.mp3", "timestamps" : ("00:20", None ), "destinationTimestamp" : {"title" : "3GB GPUs run ARC Raiders just fine", "until" : "image quality not that bad"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "image quality not that bad", "until" : "How about 1GB GPUs"}}, \
{"file" : "Far Far Away - Ferco _ Free Background Music _ Audio Library Release.mp3", "timestamps" : ("00:33", None ), "destinationTimestamp" : {"title" : "How about 1GB GPUs", "until" : "Conclusions"}}, \
{"file" : "Inspired - MaikonMusic  Free Background Music  Audio Library Release.mp3", "timestamps" : ("00:00", None ), "destinationTimestamp" : {"title" : "Conclusions", "until" : "EOF"}}, \
], "volume" : 0.045 },\
"episodes" : [],\
"youtube" : {"title" : " ", \
"description" : ''' ''',\
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
"tags" : "ARC,ARC Raiders,AMD,NVidia,Radeon,GeForce,GCN,R9 270,R9 380,R7 260X,RX 460,GTX 1050,GTX 960,GTX 760,GTX 750 Ti,GTX 650 Ti,Kepler,Maxwell,Pascal",\
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

# gameplay
configs["episodes"].append(\
{ "title": "3GB GPUs run ARC Raiders just fine",\
"audio" : {"timestamps" : ("00:00", "00:11.6" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "Exhibit no 1 the R9 280",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:22.5" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "F:\\Videos\\ARCRaiders-GCNs\\output\\ARCRaiders-GCNs.mp4", "start" : "04:20"},\
})

configs["episodes"].append(\
{ "title": "But can it run with even less VRAM",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:29.4" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "cards_gtx1050_960_760_rx460_r7_260X_R9_270_barred.mp4", "start" : "00:06"},\
})

configs["episodes"].append(\
{ "title": "Even 1GB can do it",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:36" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "HD7790_PioneerGame_2026_08_03_22_33_36_325_zoomedOnAfterburner.mp4", "start" : "00:00"},\
})

configs["episodes"].append(\
{ "title": "Kepler does not work ok on DX11",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:42.6" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "Kepler_InGame_Dx11VsDx12.mp4", "start" : "00:10"},\
})

configs["episodes"].append(\
{ "title": "GCN craps out in DX12",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:49.13" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "ARCRaiders_crash.mkv"},\
})

configs["episodes"].append(\
{ "title": "1060 3G hook",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "00:56.5" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "breel_GTX1060_3G_inGrass_barred.mp4"},\
})

# this is the initial 6
configs["episodes"].append(\
{ "title": "The GPUs to be tested",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:13" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "cards_gtx1050_960_760_rx460_r7_260X_R9_270_barred.mp4", "start" : "00:06"},\
"overlay" : { "image" : {"file" : "6GPUsIDed.png"} }, \
})

configs["episodes"].append(\
{ "title": "snowballing to the 750 ti and 1GB cards",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:23.9" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "cards_GTX750Ti_650Ti_HD7790_barred.mp4"},\
"overlay" : { "image" : {"file" : "overlay_3MoreCards.png"} }, \
})

# overlay with resolution, quality. Maybe add CPU specs
# use January potato video. Or maybe just the PC and ingame settings
configs["episodes"].append(\
{ "title": "Test system and settings",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:36.2" ), "volume" : 0.999, "padAudio" : 0.1 },\
"overlay" : { \
    "text" : ["'Custom PC'",\
              "'CPU\: Ryzen 5 5600'",\
              "'RAM\: 32GB DDR4, 3600MHz, dual channel'",\
              "'GPUs\: GTX 1050, GTX 960, GTX 760, GTX 750 Ti, GTX 650 Ti'",\
              "'           RX 460, R9 270, R7 260X, HD 7790'",\
    ]\
}, \
"video" : {"file" : "test_system_RX580.mp4" }\
})

# Footage from 1050
configs["episodes"].append(\
{ "title": "image quality not that bad",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:43.5" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "GTX1050_PioneerGame_2026_08_02_17_16_08_861.mp4", "start" : "00:30"},\
})

configs["episodes"].append(\
{ "title": "side by side 1050 image and old potato",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "01:51.3" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "JanPotatoVsAugPotato.mp4", "start" : "00:14"},\
"overlay" : { "image" : {"file" : "JanPotato_vs_AugPotato.png"} }, \
})

# 3 slices zoomed on the MSI afterburner overlay.
# Add image overlay, pointing out which card is what.
configs["episodes"].append(\
{ "title": "Results for 2GB NVidia GPUs, DX12",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:00.9" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "DX12_GTXes_sideBySide.mp4", "start" : "00:00" },\
"overlay" : { "image" : {"file" : "3_GTX_Overlays.png"} }, \
})

#maybe blurr the video here?
configs["episodes"].append(\
{ "title": "Actual NVidia DX 12 graph",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:30" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "GTX1050_PioneerGame_2026_08_02_17_16_08_861.mp4", "start" : "01:00"},\
"overlay" : { "image" : {"file" : "NVidia ARC Raiders, DX12, 720p, low settings.png"} }, \
})

# the crash, without GPUZ overlay
configs["episodes"].append(\
{ "title": "2GB AMD Radeon vs. DX12",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:36.9" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "ARCRaiders_crash.mkv"},\
})

configs["episodes"].append(\
{ "title": "all 4 debug cards with red X overlay",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:48.3" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "4DebugCards.MP4"},\
"overlay" : { "image" : {"file" : "4DebugGPUsIDed.png"} }, \
})

configs["episodes"].append(\
{ "title": "Hallock, on YT",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:52.8" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : ""},\
"overlay" : { "image" : {"file" : ""} }, \
})

configs["episodes"].append(\
{ "title": "Hallock, full screen",\
"isChapter" : False, \
"audio" : {"timestamps" : ("minusWhateverSeconds", "02:52.8" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : ""},\
"overlay" : { "image" : {"file" : ""} }, \
})

# video of all 4 debug GPUs, overlays showing which card is which
configs["episodes"].append(\
{ "title": "DX11 saves the Radeon cards",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "02:58.4" ), "volume" : 0.001, "padAudio" : 0.1 },\
"video" : {"file" : "4DebugCards.MP4"},\
"overlay" : { "image" : {"file" : "4DebugGPUsIDed.png"} }, \
})

# green checkmark overlay for the 380
configs["episodes"].append(\
{ "title": "only the 380 works in dx12",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:03.7" ), "volume" : 0.001, "padAudio" : 0.1 },\
"video" : {"file" : "4DebugCards.MP4"},\
"overlay" : { "image" : {"file" : "4DebugGPUs380Works.png"} }, \
})

configs["episodes"].append(\
{ "title": "the cmdline opt",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:14.6" ), "volume" : 0.001, "padAudio" : 0.1 },\
"video" : {"file" : ""},\
})

# this is the actual graph
configs["episodes"].append(\
{ "title": "Results for 2GB AMD GPUs, DX11",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:41" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : ""},\
"overlay" : { "image" : {"file" : "AMD ARC Raiders, DX11, 720p, low settings.png"} }, \
})

# maybe the overlay can als point out what APIs can be used on each GPU for this game
configs["episodes"].append(\
{ "title": "cannot compare dx11 to dx12 breel with all 6 cards",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:50.4" ), "volume" : 0.001, "padAudio" : 0.1 },\
"video" : {"file" : "cards_gtx1050_960_760_rx460_r7_260X_R9_270_barred.mp4", "start" : "00:06"},\
"overlay" : { "image" : {"file" : "6GPUsDxApis.png"} }, \
})

# 3 slices zoomed on the MSI afterburner overlay.
# Add image overlay, pointing out which card is what.
configs["episodes"].append(\
{ "title": "Results for 2GB NVidia GPUs, DX11",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "03:56.75" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : ""},\
"overlay" : { "image" : {"file" : ""} }, \
})

configs["episodes"].append(\
{ "title": "Actual NVidia DX 11 graph",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:13.7" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : ""},\
"overlay" : { "image" : {"file" : "NVidia ARC Raiders, DX11, 720p, low settings.png"} }, \
})

configs["episodes"].append(\
{ "title": "NVidia DX 11 vs DX12 graph",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:29.2" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : ""},\
"overlay" : { "image" : {"file" : "NVidia ARC Raiders, DX11 vs DX12.png"} }, \
})

# maybe use an unblurred gameplay video here?
# vs. blurred GPUs?
configs["episodes"].append(\
{ "title": "Comparing all 2GB GPUs",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "04:56.2" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : ""},\
"overlay" : { "image" : {"file" : "Both ARC Raiders, DX11, 720p, low settings.png"} }, \
})

# side by side breels with the 650 Ti and HD 7790
# add overlay, explaining which is which
configs["episodes"].append(\
{ "title": "How about 1GB GPUs",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:09.4" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : ""},\
"overlay" : { "image" : {"file" : ""} }, \
})

configs["episodes"].append(\
{ "title": "ask for comments - 6 GPUs",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:18.6" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : "cards_gtx1050_960_760_rx460_r7_260X_R9_270_barred.mp4", "start" : "00:06"},\
})

# maybe side by side in game cap, zoomed on the Afterburner overlay
# maybe even add an overlay pointing out the two different APIs
configs["episodes"].append(\
{ "title": "Cannot really compare them - different DX APIs",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:31.7" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : ""},\
"overlay" : { "image" : {"file" : ""} }, \
})

# use a text overlay here, not an image
configs["episodes"].append(\
{ "title": "650 Ti results",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:40.2" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : ""},\
"overlay" : { "image" : {"file" : ""} }, \
})

# use a text overlay here, not an image
configs["episodes"].append(\
{ "title": "7790 results",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "05:54" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : ""},\
"overlay" : { "image" : {"file" : ""} }, \
})

# side by side, GCN crash and -dx11 fix.
# maibe add an overlay.
configs["episodes"].append(\
{ "title": "Conclusions",\
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:04.8" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : ""},\
})

# in game cap, zoomed on the DX12 API. Maybe side by side with the 760 breel.
configs["episodes"].append(\
{ "title": "Kepler runs good in DX12",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:16.8" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : ""},\
})

# impro might merge with the above.
configs["episodes"].append(\
{ "title": "Kepler runs good in DX12",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:27.4" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "2GB can run the game - 6 cards breel",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:32.5" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "2TFlops - maybe 750 Ti and GPUZ",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:41.8" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "Video quality - not that bad",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "06:49.7" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : ""},\
})

# gameplay crawling to the elevator
# might cover also the last mention of -dx11 
configs["episodes"].append(\
{ "title": "fate of legacy cards",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:00.2" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "again-dx11",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:08.4" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "Apex Legends dropped DX11",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:14.9" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "Fortnite dropped DX11",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:20.3" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "Kepler still works for now",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:26.2" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : ""},\
})

configs["episodes"].append(\
{ "title": "bye",\
"isChapter" : False, \
"audio" : {"timestamps" : (scriptedvided.nextTS(configs), "07:35.3" ), "volume" : 0.999, "padAudio" : 0.1 },\
"video" : {"file" : ""},\
})



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