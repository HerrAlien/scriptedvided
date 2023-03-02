import scriptedvided

configs = { "defaultAudioFile" : "hd5770-2023.ogg",\
"mediaFolder" : "F:\\Videos\\hd5770_reference", \
"stockFolder" : "F:\\Videos\\stock",\
"benchmarkFile" : "F:\\Videos\\hd5770_reference\\Benchmark_hd5770_ref.txt",\
"outputFolder" : "F:\\Videos\\stock\\no longer relevant", \
"outputFile" : "dgpu_over_igpu.mp4", \
"textOpts" : {"fontcolor" : "White", "boxcolor" : "#80000080"},\
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


scriptedvided.makeVideo(configs)

