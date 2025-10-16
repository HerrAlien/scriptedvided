''' 
Scripted Video Editor - a bunch of python script to allow rendering of videos 
using FFMPEG.

SV_OPS contains operations on the audio or video streams (truncate, scale, padding
etc.)

Copyright 2022 Herr_Alien <alexandru.garofide@gmail.com>

This program is free software: you can redistribute it and/or modify it under 
the terms of the GNU General Public License as published by the 
Free Software Foundation, either version 3 of the License, or (at your option)
any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY 
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE. See the GNU Affero General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

import subprocess
import os
import sv_utils
import sv_ffutils

# better quality
#defaultOutputParametersNoVideo = ["-c:a", "libvorbis", "-qscale:a", "9"];
#defaultOutputParameters = defaultOutputParametersNoVideo + ["-c:v", "libx264", "-preset", "slow", "-crf", "15"];

# better compression 
defaultOutputParametersNoVideo = ["-c:a", "libvorbis", "-qscale:a", "7"];
defaultOutputParameters = defaultOutputParametersNoVideo + ["-c:v", "libx264", "-preset", "medium", "-crf", "18"];

def toInputParams (inputStream):
    params = [];

    if (type(inputStream) is type({})):        
        length = sv_utils.dictValue(inputStream,"length", 0)
        if (length > 0):
            params.append("-t")
            params.append(str(length))
        
        start = sv_utils.dictValue(inputStream,"start", None)
        if start is not None:
            if (start >= 0):
                params.append("-ss")
                params.append(str(start))
            else:
                params.append("-sseof")
                params.append(str(start - length))
        
        params.append("-i")
        file = sv_utils.dictValue(inputStream,"file")
        params.append(file)
        
    else:
        params.append("-i")
        file = inputStream
        params.append(file)

    return params

    
def getDrawTextCommandFromArray (text, opts):
    textSize = float(sv_utils.dictValue(opts,"fontsize", 48))
    paramText = ""
    borderWidth = 0.5 * textSize
    boxcolor=sv_utils.dictValue(opts,"boxcolor", "#80000080")
    fontcolor=sv_utils.dictValue(opts,"fontcolor", "White")

    '''
        if (t > 4)
            x = borderWidth;
        else
        {
            velocity = (width + borderWidth) / 2
            x = (t-4) * velocity
        }
        
        (Tshow - completeTransition) * velocity = -width.
        (Tshow - (Tshow + transitionAlone)) * velocity = -width.
        
        -transitionAlone * velocity = -width => velocity = width/transitionAlone
        
        
    '''
    
    # use a boxw=H-borderWidth, and a boxh=stepSize
    
    transition=":x=if(gt(t\,4)\, "+ str(borderWidth) + "\,\(t-4\)*\(tw + " + str(borderWidth) + "\)/2)"
    
    if (type(text) is type("")):
        paramText = "drawtext=y=H:box=1:boxborderw=" + str(borderWidth) +":boxcolor="+boxcolor+":font=Arial:fontsize=" + str (textSize) + ":fontcolor=" + fontcolor + ":text="+text
        paramText = paramText + transition
    else:
        lineSpacing = 0.5 * textSize
        stepSize = (textSize + 2 * borderWidth + lineSpacing)
        offsetFromBottom = len(text) * stepSize
        step = 0
        initialOffset = offsetFromBottom
        for line in text:
            iterationStartNode = ";[intermediate"+ str(step) +"]"
            iterationEndNode = "[intermediate"+ str(step + 1) +"]"
            
            if step == 0:
                iterationStartNode = ""
            
            if (step == (len(text) - 1)):
                iterationEndNode = ""

            paramText = paramText  + iterationStartNode + "drawtext=y=(H+"+str(initialOffset)+")/2-"+ str(offsetFromBottom) +":box=1:boxborderw="+ str(borderWidth) + ":boxcolor="+boxcolor+":font=Arial:fontsize="+ str (textSize) +":fontcolor=" + fontcolor + ":text="+line 
            paramText = paramText + transition
            paramText = paramText + iterationEndNode

            offsetFromBottom = offsetFromBottom - stepSize
            step=step+1

    return paramText
        
def getScaleCommand(resolutionPair):
    return "scale="+str(resolutionPair[0])+ "x" +str(resolutionPair[1]) + ":flags=lanczos"
    
# input - the input media to be truncated
# start - the input media to be truncated
def truncate(input, start=None, length=None, output=None, recompress=True):
    params = sv_ffutils.ffmpegParams()
    
    params.append("-i")
    params.append(input)        
    
    if start is not None:
        if (start >= 0):
            params.append("-ss")
            params.append(str(start))
#        else:
#            params.append("-sseof")
#            params.append(str(start - length))
    
    if length is not None and length > 0:
            params.append("-t")
            params.append(str(length))

    if (output == None):
        output = sv_ffutils.defaultOutput (input, "_truncate_" )

    if (not recompress):
        params.append("-c")
        params.append("copy")

    params = params + defaultOutputParameters
    params.append(output)
    subprocess.run(params)
    
    return output
    
def overlayAudio (inputVid, inputAudio, output=None, firstStreamAudioWeight=0.1, recompressVideo=True):
    params = sv_ffutils.ffmpegParams();

    params = params + toInputParams(inputVid)    
    params = params + toInputParams(inputAudio)

    inputVideohasAudio = sv_ffutils.hasAudio(inputVid)
    # detect if input video DOES have audio
    if not inputVideohasAudio:
        params.append("-f")
        params.append("lavfi")
        params.append("-i")
        params.append("anullsrc")
    
    params.append ("-map")
    params.append ("0:a?")
    
    params.append ("-map")
    params.append ("1:a")
    
    if not inputVideohasAudio:
        params.append ("-map")
        params.append ("2:a")
    
    if (output == None):
        audioRoot,ext = os.path.splitext (sv_utils.getFileFromInput(inputAudio))
        output = sv_ffutils.defaultOutput (sv_utils.getFileFromInput(inputVid), "_overlay_"  + os.path.basename(audioRoot) )

    weightsStr = str(firstStreamAudioWeight) + " " + str(1 - firstStreamAudioWeight)
        
    params.append ("-filter_complex")
    if inputVideohasAudio:
        params.append ("[0:a][1:a] amix=weights='" + weightsStr + "'")
    else:
        params.append ("[2:a][1:a] amix=weights='" + weightsStr + "':duration=shortest")
        
    params.append ("-map")
    params.append ("0:v")

    if (not recompressVideo):
        params.append ("-c:v")
        params.append ("copy")
    
    params = params + defaultOutputParameters
    params.append(output)
    subprocess.run(params)
    
    return output

def substituteAudio (inputVid, inputAudio, output=None, recompress=True):
    return sv_ops.overlayAudio(inputVid, inputAudio, output, 0.001, recompress)
    
def appendMultiple (streams, output=None, recompressVideo=True, video=True, audio=True):

    params = sv_ffutils.ffmpegParams();
    for stream in streams:
        sar = sv_ffutils.getSar(stream)
        if sar != (1,1) and sar != (0,0):
            stream = setSarToOne(stream)
        params = params + toInputParams(stream)    

    params.append("-filter_complex")
    
    streamsIds = ""
    for i in range (0, len(streams)):
        iStr = str(i)
        if video:
            streamsIds = streamsIds + "["+iStr+":v]"
        if audio:
            streamsIds = streamsIds + "["+iStr+":a]"
    
    filter = streamsIds + "concat=n=" + str(len(streams)) 
    if video:
        filter = filter + ":v=1"
    else:
        filter = filter + ":v=0"
    if audio:
        filter = filter + ":a=1"
    else:
        filter = filter + ":a=0"
    
    filter = filter + ":unsafe=1"
    
    params.append(filter)
    
    if (not recompressVideo):
        params.append ("-c:v")
        params.append ("copy")

    params.append ("-fpsmax")
    params.append ("30")
    
    if (output == None):
        secondRoot,ext = os.path.splitext (sv_utils.getFileFromInput(streams[0]))
        output = secondRoot + "_append_" + ext

    if video:
        params = params + defaultOutputParameters
    else:
        params = params + defaultOutputParametersNoVideo
        
    params.append(output)
    subprocess.run(params)
    
    return output

def xfadedMultiple (streams, output=None, fadeDuration=1, recompressVideo=True):
    durations = []
    params = sv_ffutils.ffmpegParams();
    for stream in streams:
        if sv_ffutils.getSar(stream) != (1,1):
            stream = setSarToOne(stream)
        params = params + toInputParams(stream)
        durations.append(sv_ffutils.getLengthOfStream(stream))

    params.append("-filter_complex")
    
    currentOffset = 0;
    videograph = ""
    audiograph = ""
    fadeDurationStr = str(fadeDuration)
    for i in range (0, len(streams) - 1):
        currentOffset = durations[i] + currentOffset - fadeDuration
        iStr = str(i)
        nextIStr = str(i+1)
        if i == 0:
            nextIStr = str(i+1)
            videograph = "["+iStr+":v]" + "["+nextIStr+":v]xfade=duration="+ fadeDurationStr +":offset="+ str(currentOffset) +"[intermediateV" + iStr + "];"
            audiograph = "["+iStr+":a]" + "["+nextIStr+":a]acrossfade=d="+ fadeDurationStr +"[intermediateA" + iStr + "];"
        else:
            prevIStr = str(i-1)
            videograph = videograph + "[intermediateV" + prevIStr + "]" + "["+nextIStr+":v]xfade=duration="+ fadeDurationStr +":offset="+ str(currentOffset) +"[intermediateV" + iStr + "];"
            audiograph = audiograph + "[intermediateA" + prevIStr + "]" + "["+nextIStr+":a]acrossfade=d="+ fadeDurationStr +"[intermediateA" + iStr + "];"
            
    filtergraph = videograph + audiograph
    filtergraph = filtergraph[:-1]
    
    params.append(filtergraph)
    params.append("-map")
    params.append("[intermediateV"+ str(len(streams) - 2)+"]")

    params.append("-map")
    params.append("[intermediateA"+ str(len(streams) - 2)+"]")
    
    if (not recompressVideo):
        params.append ("-c:v")
        params.append ("copy")
    
    if (output == None):
        secondRoot,ext = os.path.splitext (sv_utils.getFileFromInput(streams[0]))
        output = "_append_.mp4"

    params = params + defaultOutputParameters
    params.append(output)
    subprocess.run(params)
    
    return output

def concatNoRecompress(streams, output=None):
    if (output == None):
        secondRoot,ext = os.path.splitext (sv_utils.getFileFromInput(streams[0]))
        output = secondRoot + "_append_" + ext

    params = sv_ffutils.ffmpegParams();
    params.append("-safe")
    params.append("0")

    params.append("-f")
    params.append("concat")
    
    f = open ("concat.txt", "w")
    for stream in streams:
        sar = sv_ffutils.getSar(stream)
        if sar != (1,1) and sar != (0,0):
            stream = setSarToOne(stream)
        f.write("file '" + sv_utils.getFileFromInput(stream) + "'\n")
    f.close()

    params.append("-i")
    params.append("concat.txt")
    params.append("-c")
    params.append("copy")
    params = params + defaultOutputParameters
    params.append(output)
    subprocess.run(params)
    return output
    
    
def append (firstStream, secondStream, output=None, recompressVideo=True):
    return appendMultiple([firstStream, secondStream], output, recompressVideo)

    
def padAudioStream (stream, output=None, ammountBegin = 0, amountEnd = 0):
    params = sv_ffutils.ffmpegParams();

    params = params + toInputParams(stream)    
    params.append ("-map")
    params.append ("0:a")

    params.append("-filter_complex")
    params.append("[0:a]adelay=" + str(ammountBegin * 1000) + ":all=1[intermediate];[intermediate]apad=pad_dur=" + str(amountEnd))
    
    if (output == None):
        root,ext = os.path.splitext (sv_utils.getFileFromInput(stream))
        output = sv_ffutils.defaultOutput (root, "_padded_"  + str(ammountBegin) + "_" + str(amountEnd))

    params = params + defaultOutputParameters
    params.append(output)
    subprocess.run(params)
    
    return output

def drawText (stream, text, output=None, opts={"fontcolor" : "White", "boxcolor" : "#80000080", "fontsize" : 48}):
    if (text is None):
        print ("WARNING: no text provided, returning the unmodified input " + "'" + sv_utils.getFileFromInput(stream) + "'")
        return sv_utils.getFileFromInput(stream)
        
    params = sv_ffutils.ffmpegParams();

    params = params + toInputParams(stream)    
    params.append("-filter_complex")

    params.append(getDrawTextCommandFromArray(text, opts))
    
    if (output == None):
        root,ext = os.path.splitext (sv_utils.getFileFromInput(stream))
        output = sv_ffutils.defaultOutput (root, "_withText_"  + ext)

    params = params + defaultOutputParameters
    params.append(output)
    subprocess.run(params)
    
    return output

def scaleVideo(video, resolutionPair, output=None):
    params = sv_ffutils.ffmpegParams();
    params = params + toInputParams(video)    
    params.append("-filter_complex")

    params.append(getScaleCommand(resolutionPair))
    
    if (output == None):
        root,ext = os.path.splitext (sv_utils.getFileFromInput(video))
        output = sv_ffutils.defaultOutput (root, "_scaled_" + str(resolutionPair[0]) + "x" + str(resolutionPair[1])  + ext)

    params = params + defaultOutputParameters
    params.append(output)   
    subprocess.run(params)
    
    return output

    
def rotateVideo(video, angle, output=None):
    params = sv_ffutils.ffmpegParams();
    params = params + toInputParams(video)    
    params.append("-filter_complex")

    angleRadStr = str(angle)  + "*PI/180"
    
    params.append("[0]rotate='" +angleRadStr+":ow=max(iw*abs(cos("+angleRadStr+")),ih*abs(sin("+angleRadStr+"))):oh=max(iw*abs(sin("+angleRadStr+")),ih*abs(cos("+angleRadStr+")))'[R0];[R0]scale='1920x1080:flags=lanczos'[S0];[S0]setsar=1")
    
    if (output == None):
        root,ext = os.path.splitext (sv_utils.getFileFromInput(video))
        output = sv_ffutils.defaultOutput (root, "_rotated_" + str(angle) + "_degrees" + ext)

    params = params + defaultOutputParameters
    params.append(output)   
    subprocess.run(params)
    
    return output

    
def setSarToOne(video, output=None):
    params = sv_ffutils.ffmpegParams();
    params = params + toInputParams(video)    
    params.append("-filter_complex")

    params.append("setsar=1")
    
    if (output == None):
        root,ext = os.path.splitext (sv_utils.getFileFromInput(video))
        output = sv_ffutils.defaultOutput (root, "_setSar1_" + ext)
    
    params = params + defaultOutputParameters
    params.append(output)   
    subprocess.run(params)
    
    return output

def overlayImage (canvas, overlay, colorForChroma="0x00FF00", colorTolerance=0.3, transparencyOfNonChroma=0.2, output=None):
# ffmpeg -i F:\Videos\gta5_vs_ts2\720_2.png -i F:\Videos\stock\6500xt_short_rant.mp4 -filter_complex "[0:v]colorkey=0xFFFFFF:0.3:0.2[ckout];[1:v][ckout]overlay[out];acopy" -map "[out]" f:\videos\1.mp4
# center the image
#ffmpeg -i F:\Videos\gta5_vs_ts2\720_2.png -i F:\Videos\stock\6500xt_short_rant.mp4 -filter_complex "[0:v]colorkey=0xFFFFFF:0.3:0.2[ckout];[1:v][ckout]overlay=x=0.5*(W-w):y=0.5*(H-h)[out];acopy" -map "[out]" f:\videos\1.mp4
    params = sv_ffutils.ffmpegParams();
    params = params + toInputParams(overlay)    
    params = params + toInputParams(canvas)    
    params.append("-filter_complex")

    params.append('[0:v]colorkey='+colorForChroma+':'+ str(colorTolerance) +':'+str(transparencyOfNonChroma)+'[ckout];[1:v][ckout]overlay=x=0.5*(W-w):y=0.5*(H-h)[out];acopy')
    
    params.append("-map")
    params.append("[out]")
    
    if (output == None):
        root,ext = os.path.splitext (sv_utils.getFileFromInput(canvas))
        output = sv_ffutils.defaultOutput (root, "_overlayImage_" + ext)

    params = params + defaultOutputParameters
    params.append(output)   
    subprocess.run(params)
    
    return output

