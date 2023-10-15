''' 
Scripted Video Editor - a bunch of python script to allow rendering of videos 
using FFMPEG.

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
import shutil
import sv_utils
import sv_ffutils
import sv_ops
import random


def getDefaultGraphInputArgs():
    return ["ffmpeg", "-f", "lavfi", "-i", "color=c=#00ff00:size=1280x720"]

def getDrawRectangleFilterCommand(x,y,w,h,color):
    return "drawbox=x="+str(x)+":y="+str(y)+":w="+str(w)+":h="+str(h)+":t=fill:c="+color

def getDrawTextCommand(x,y,fontSize,color,text):
    return "drawtext=box=0:x="+str(x)+"-tw/2:y="+str(y)+":fontfile=FreeSans.ttf:fontsize=" + str (fontSize) + ":fontcolor=" + color + ":text='"+text+"'"

    
'''
Single series meta data is a dictionary that must have the following structure:
{ 
  bottomX : [int] represents the X coord of the bottom left corner, 
  bottomY : [int] represents the X coord of the bottom left corner,
  spacing : [int] represents the space between the right edge of previous entry and left edge of the current
  width   : [int] represents the width of the bar
  maxHeight : [int] height in pixels for the normalized value of 1.0
  color : [string] "#rrggbb" color of the bar 
  name  : [string] unique name for this series
}
'''

def getNormalizedValues(values):
    normalizedValues = []
    maxValue = -999999
    for value in values:
        if value > maxValue:
            maxValue = value

    for value in values:
        normalizedValues.append( float(value) / maxValue)

    return normalizedValues

def getDrawSingleSeriesBars (seriesMetaData, values):
    drawBoxes = []
    x = seriesMetaData["bottomX"]
    y = seriesMetaData["bottomY"]
    w = seriesMetaData["width"]
    spacing = seriesMetaData["spacing"]
    maxHeight = seriesMetaData["maxHeight"]
    color = seriesMetaData["color"]
    labelColor = seriesMetaData["labelColor"]
    name = seriesMetaData["name"]
    scale = seriesMetaData["scale"]
    
    normalizedValues = getNormalizedValues (values)
    labelIndex = 0
    drawLabels = []

    labelName = "label" + name
    
    for value in normalizedValues:
        height = int (maxHeight * value * scale + 0.5)
        label = str (values[labelIndex])
        drawBoxes.append (getDrawRectangleFilterCommand (x, y - height, w, height, color))
        drawLabels.append (getDrawTextCommand (int(x + 0.5*w), y - height + 10, int(0.6*w), labelColor, label))
        labelIndex = labelIndex + 1
        x = x + w + spacing

    cmd = ""
    for i in range(len(drawBoxes)):
        if (i == 0):
            cmd = cmd + drawBoxes[i] + "["+name+str(i)+"]"
        elif (i == len(drawBoxes)-1):
            cmd = cmd + "["+name+str(i - 1)+"]" + drawBoxes[i]
        else:
            cmd = cmd + ";["+name+str(i - 1)+"]" + drawBoxes[i] + "["+name+str(i)+"];"
    
    cmd = cmd + "["+labelName+"];["+labelName+"]"
    for i in range(len(drawLabels)):
        if (i == 0):
            cmd = cmd + drawLabels[i] + "["+labelName+str(i)+"]"
        elif (i == len(drawLabels)-1):
            cmd = cmd + "["+labelName+str(i - 1)+"]" + drawLabels[i]
        else:
            cmd = cmd + ";["+labelName+str(i - 1)+"]" + drawLabels[i] + "["+labelName+str(i)+"];"
            
    return cmd

if __name__ == "__main__":
    meta = {"bottomX" : 30, "bottomY" : 640, "width" : 50, "spacing" : 80, "maxHeight" : 500, "color" : "#ff0000", "labelColor" : "#ffffff", "name" : "Average" , "scale" : 1 }
    meta2 = {"bottomX" : 90, "bottomY" : 640, "width" : 50, "spacing" : 80, "maxHeight" : 500, "color" : "#0000ff", "labelColor" : "#ffffff", "name" : "Average" , "scale" : 42.0/58  }
    params = getDefaultGraphInputArgs()
    params.append ("-filter_complex")
    params.append (getDrawSingleSeriesBars ( meta , [37,43,58]) + "[AVG];[AVG]" + getDrawSingleSeriesBars ( meta2 , [13,20,42]))
    params = params + ["-frames:v", "1"]
    params.append ("out.png")
    subprocess.run(params)
    print (params)