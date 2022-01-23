import subprocess
import os

def ffmpegParams():
    return ["ffmpeg", "-y"]

def defaultOutput (input, suffix):
    root, ext = os.path.splitext (input)
    return root + suffix + ext
    
def dictValue(dict, key, default=-1):
    try:
        return dict[key]
    except:
        return default
    
def toInputParams (inputStream):
    params = [];

    if (type(inputStream) is type({})):        
        length = dictValue(inputStream,"length")
        if (length > 0):
            params.append("-t")
            params.append(str(length))
        
        start = dictValue(inputStream,"start")
        if (start >= 0):
            params.append("-ss")
            params.append(str(start))
        else:
            params.append("-sseof")
            params.append(str(start - length))
        
        params.append("-i")
        params.append(dictValue(inputStream,"file"))
    else:
        params.append("-i")
        params.append(inputStream)

    return params


# input - the input media to be truncated
# start - the input media to be truncated
def truncate(input, start=-1, length=-1, output=None, recompress=False):
    params = ffmpegParams() + toInputParams( {"file" : input, "start" : start, "length" : length} );

    if (output == None):
        output = defaultOutput (input, "_truncate_" )

    if (not recompress):
        params.append("-c")
        params.append("copy")

    params.append(output)
    
    subprocess.run(params)
    
    return output
    
def substituteAudio (inputVid, inputAudio, output, recompress=False):
    params = ffmpegParams();

    params.append ("-vn")
    params = params + toInputParams (inputAudio)
    
    params.append("-an")
    params = params + toInputParams (inputVid)
    
    if (output == None):
        audioRoot,ext = os.path.splitext (inputAudio)
        output = defaultOutput (inputVid, "_substituteAudio_"  + os.path.basename(audioRoot) )

    if (not recompress):
        params.append("-c")
        params.append("copy")

    params.append(output)
    subprocess.run(params)
    
    return output
    
def overlayAudio (inputVid, inputAudio, output, firstStreamAudioWeight=0.1, recompressVideo=True):
    params = ffmpegParams();

    params = params + toInputParams(inputVid)    
    params = params + toInputParams(inputAudio)

    params.append ("-map")
    params.append ("0:a")
    
    params.append ("-map")
    params.append ("1:a")
    
    if (output == None):
        audioRoot,ext = os.path.splitext (inputAudio)
        output = defaultOutput (inputVid, "_overlay_"  + os.path.basename(audioRoot) )

    weightsStr = str(firstStreamAudioWeight) + " " + str(1 - firstStreamAudioWeight)
        
    params.append ("-filter_complex")
    params.append ("[0:a][1:a] amix=weights='" + weightsStr + "'")

    params.append ("-map")
    params.append ("0:v?")

    params.append ("-map")
    params.append ("1:v?")
    
    if (not recompressVideo):
        params.append ("-c:v")
        params.append ("copy")
    
    params.append(output)
    subprocess.run(params)
    
    return output

def append (firstStream, secondStream, output, recompressVideo=True):
    params = ffmpegParams();

    params = params + toInputParams(firstStream)    

    params = params + toInputParams(secondStream)    

        
    params.append("-filter_complex")
    params.append("concat")
    
    if (not recompressVideo):
        params.append ("-c:v")
        params.append ("copy")
    
    if (output == None):
        secondRoot,ext = os.path.splitext (secondStream)
        output = defaultOutput ("", "_append_"  + os.path.basename(secondRoot))

    params.append(output)
    subprocess.run(params)
    
    return output

def getLengthOfStream (filepath):
    finishedProc = subprocess.run (["ffprobe", filepath], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out = str(finishedProc.stderr) + str(finishedProc.stdout)
    durationIndex = out.index("Duration")
    out = out[durationIndex:];
    commaIndex = out.index(",")
    out = out[0:commaIndex]
    spaceIndex  = out.index(" ")
    out = out[spaceIndex+1:]
    print(out)
    

    
if __name__ == "__main__":
#   truncatedvid = truncate ( "C:\\Users\\Admin\\Videos\\hd7770\\hd7770_RainbowSix_720p_100renderScale.mp4", -10, 30, "vid.mp4" )
#   truncatedaudio = truncate ( "C:\\Users\\Admin\\Videos\\Generic old GPU advice.ogg", -10, 30, "audio.ogg" )
#   truncatedaudio2 = truncate ("C:\\Users\\Admin\\Videos\\Generic old GPU advice.ogg", None, -2, 30)
#   overlayAudio ({"file":"C:\\Users\\Admin\\Videos\\hd7770\\hd7770_RainbowSix_720p_100renderScale.mp4", "start" : -10, "length" : 30}, \
#   {"file":"C:\\Users\\Admin\\Videos\\Generic old GPU advice.ogg", "start":-10, "length" : 30} , "merged_audio.mp4", 0.15)
#   truncatedvid1 = truncate ("C:\\Users\\Admin\\Videos\\hd7770\\hd7770_RainbowSix_720p_100renderScale.mp4", "t1.mp4", -40, 10)
#   truncatedvid2 = truncate ("C:\\Users\\Admin\\Videos\\hd7770\\hd7770_RainbowSix_720p_100renderScale.mp4", "t2.mp4", -10, 10)
#   append({"file":"C:\\Users\\Admin\\Videos\\hd7770\\hd7770_RainbowSix_720p_100renderScale.mp4", "start" : -10, "length" : 10}, \
#   {"file":"C:\\Users\\Admin\\Videos\\hd7770\\hd7770_RainbowSix_720p_100renderScale.mp4", "start" : -40, "length" : 10}, "appended.mp4")
    getLengthOfStream ("audio.ogg")
