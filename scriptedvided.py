import subprocess
import os

def ffmpegParams():
    return ["ffmpeg", "-y"]

def defaultOutput (input, suffix):
    root, ext = os.path.splitext (input)
    return root + suffix + ext

# input - the input media to be truncated
# start - the input media to be truncated
def truncate(input, output=None, start=0, length=0, recompress=False):
    params = ffmpegParams();

    if (length > 0):
        params.append("-t")
        params.append(str(length))
    
    if (start >= 0):
        params.append("-ss")
        params.append(str(start))
    else:
        params.append("-sseof")
        params.append(str(start - length))
    
    params.append("-i")
    params.append(input)
    
    if (length > 0):
        params.append("-t")
        params.append(str(length))

    if (output == None):
        output = defaultOutput (input, "_truncate_" + str(start) + "_" + str(length))

    if (not recompress):
        params.append("-c")
        params.append("copy")

    params.append(output)
    
    subprocess.run(params)
    
    return output
    
def substituteAudio (inputVid, inputAudio, output=None, recompress=False):
    params = ffmpegParams();

    params.append ("-i")
    params.append (inputAudio)
    
    params.append("-an")
    params.append ("-i")
    params.append(inputVid)
    
    if (output == None):
        audioRoot,ext = os.path.splitext (inputAudio)
        output = defaultOutput (inputVid, "_substituteAudio_"  + os.path.basename(audioRoot) )

    if (not recompress):
        params.append("-c")
        params.append("copy")

    params.append(output)
    subprocess.run(params)
    
    return output
    
def overlayAudio (inputVid, inputAudio, output=None, firstStreamAudioWeight=0.1, recompressVideo=True):
    params = ffmpegParams();

    params.append ("-i")
    params.append(inputVid)    

    params.append ("-i")
    params.append (inputAudio)

    
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

def append (firstStream, secondStream, output=None, recompressVideo=True):
    params = ffmpegParams();

    params.append ("-i")
    params.append(firstStream)    

    params.append ("-i")
    params.append (secondStream)

        
    params.append("-filter_complex")
    params.append("concat")
    
    if (not recompressVideo):
        params.append ("-c:v")
        params.append ("copy")
    
    if (output == None):
        secondRoot,ext = os.path.splitext (secondStream)
        output = defaultOutput (firstStream, "_append_"  + os.path.basename(secondRoot))

    params.append(output)
    subprocess.run(params)
    
    return output
    
if __name__ == "__main__":
   truncatedvid = truncate ("C:\\Users\\Admin\\Videos\\hd7770\\hd7770_RainbowSix_720p_100renderScale.mp4", None, -10, 30)
   truncatedaudio = truncate ("C:\\Users\\Admin\\Videos\\Generic old GPU advice.ogg", None, -10, 30)
#   truncatedaudio2 = truncate ("C:\\Users\\Admin\\Videos\\Generic old GPU advice.ogg", None, -2, 30)
   overlayAudio (truncatedvid, truncatedaudio , "merged_audio.mp4", 0.15)
   truncatedvid1 = truncate ("C:\\Users\\Admin\\Videos\\hd7770\\hd7770_RainbowSix_720p_100renderScale.mp4", None, -40, 10)
   truncatedvid2 = truncate ("C:\\Users\\Admin\\Videos\\hd7770\\hd7770_RainbowSix_720p_100renderScale.mp4", None, -10, 10)
   append(truncatedvid1, truncatedvid2)
