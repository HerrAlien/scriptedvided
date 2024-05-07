''' 
Scripted Video Editor - a bunch of python script to allow rendering of videos 
using FFMPEG.

SV_UTILS contains various utilities (converting string timestaps to numbers etc.)

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

def filePathSafeString(someText):
    return someText.replace(":", " ").replace("?", " ")

def dictValue(dict, key, default=None):
    try:
        return dict[key]
    except:
        return default

def getSeconds (timeAsString):
    if timeAsString is None:
        return None
        
    if type(timeAsString) is not type (""):
        return float(timeAsString)

    times = timeAsString.split(":")
    arrayLen = len(times)
    
    if arrayLen == 2 and times[1] is None:
        return float(timeAsString)
    
    factor = 1.0
    value = 0.0
    
    try:
        for index in range(0, arrayLen):
            value = value + float(times[arrayLen - 1 - index]) * factor
            factor = factor * 60
    except:
        print("ERR: Could not convert input string to seconds: " + timeAsString)
        
    return value

def twoDigitString(number):
    if (number < 10):
        return "0" + str(number)
    return str(number)
    
def secondsToTime(seconds):
    hours = int(seconds/3600)
    minutes = int((seconds - 3600 * hours) / 60)
    seconds = int((seconds - 3600 * hours - 60 * minutes) + 0.5)

    if seconds == 60:
        seconds = 0
        minutes = minutes + 1
    
    hoursStr = twoDigitString(hours)
    minutesStr = twoDigitString(minutes)
    secondsStr = twoDigitString(seconds)

    return hoursStr + ":" + minutesStr + ":" + secondsStr

def getFileFromInput (inputStream):
    if (type(inputStream) is type({})):        
        return dictValue(inputStream,"file")
    else:
        return inputStream

# move to UTILS
def getFpsValueFromLine(line):
    valueOfInterest = line.split(":")[1]
    valueOfInterest = valueOfInterest.replace(" ", "")
    valueOfInterest = valueOfInterest.replace("FPS\n", "")
    return int(float(valueOfInterest) + 0.5)
    
# move to UTILS
def parseBenchmarkFile (benchmarkFile):
    returnedDict = {}
    currentKey = ""
    currentValue = [0,0,0]
    benchmarkCompletedMark = " benchmark completed,"
    framesRenderedInMark = "frames rendered in"
    
    fileHandler = open(benchmarkFile, "r")
    fileLines = fileHandler.readlines()
    lineIndexFollowingKey = -1
    for line in fileLines:
        if benchmarkCompletedMark in line:
            currentKey = line[21:]
            gameNameEndsAt = currentKey.index(benchmarkCompletedMark)
            currentKey = currentKey[0:gameNameEndsAt]
            currentKey = currentKey.upper()
            lineIndexFollowingKey = 0
            
            tagsStartAt = line.index(framesRenderedInMark) + len(framesRenderedInMark)
            tagsStr = line[tagsStartAt:]
            tagsStartAt = tagsStr.index(" s") + 2
            tagsStr = tagsStr[tagsStartAt:]
            tagsStr = tagsStr.replace("(", "").replace(")", ",").replace("\r","").replace("\n","")
            tagsArr = tagsStr.split(",")
            finalTags = []
            for tag in tagsArr:
                tag = tag.strip()
                if len(tag) > 0:
                    finalTags.append(tag)
            finalTags.sort() 
            finalTags.append(currentKey)
            currentValue = [0,0,0, finalTags]
        else:
            if lineIndexFollowingKey == 0: # average
                currentValue[0] = getFpsValueFromLine(line)
            elif lineIndexFollowingKey == 3: # 1%
                currentValue[1] = getFpsValueFromLine(line)
            elif lineIndexFollowingKey == 4: # 0.1%
                currentValue[2] = getFpsValueFromLine(line)
                returnedDict[currentKey] = currentValue
                lineIndexFollowingKey = -1
            
            if lineIndexFollowingKey >= 0:
                lineIndexFollowingKey = lineIndexFollowingKey + 1

    return returnedDict

def parseBenchmarkFileAsArray (benchmarkFile):
    returned = []
    currentKey = ""
    currentValue = [0,0,0]
    benchmarkCompletedMark = " benchmark completed,"
    framesRenderedInMark = "frames rendered in"
    
    fileHandler = open(benchmarkFile, "r")
    fileLines = fileHandler.readlines()
    lineIndexFollowingKey = -1
    for line in fileLines:
        if benchmarkCompletedMark in line:
            currentKey = line[21:]
            gameNameEndsAt = currentKey.index(benchmarkCompletedMark)
            currentKey = currentKey[0:gameNameEndsAt]
            currentKey = currentKey.upper()
            lineIndexFollowingKey = 0
            
            tagsStartAt = line.index(framesRenderedInMark) + len(framesRenderedInMark)
            tagsStr = line[tagsStartAt:]
            tagsStartAt = tagsStr.index(" s") + 2
            tagsStr = tagsStr[tagsStartAt:]
            tagsStr = tagsStr.replace("(", "").replace(")", ",").replace("\r","").replace("\n","")
            tagsArr = tagsStr.split(",")
            finalTags = []
            for tag in tagsArr:
                tag = tag.strip()
                if len(tag) > 0:
                    finalTags.append(tag)
            finalTags.sort() 
            finalTags.append(currentKey)
            currentValue = [0,0,0, finalTags]
        else:
            if lineIndexFollowingKey == 0: # average
                currentValue[0] = getFpsValueFromLine(line)
            elif lineIndexFollowingKey == 3: # 1%
                currentValue[1] = getFpsValueFromLine(line)
            elif lineIndexFollowingKey == 4: # 0.1%
                currentValue[2] = getFpsValueFromLine(line)
                returned.append(currentValue)
                lineIndexFollowingKey = -1
            
            if lineIndexFollowingKey >= 0:
                lineIndexFollowingKey = lineIndexFollowingKey + 1

    return returned



# filtering predicate needs more work - avoid casing, have some sort of list of
# synonims etc etc
def filterBenchmarkArray (inputArray, whitelistOfTags):
    filtered = []
    for entry in inputArray:
        addEntry = True
        for allowedTag in whitelistOfTags:
            if not (allowedTag in entry[-1]):
                addEntry = False

        if addEntry:
            filtered.append(entry)
            
    return filtered
    
# move to UTILS
def aliases(inputName):
    gameAliases = [\
        ["Apex", "Apex Legends", "ApexLegends", "Apex_Legends", "r5apex.exe", "R5Apex"],\
        ["Alien Isolation", "Alien: Isolation", "Alien:Isolation", "AlienIsolation", "Alien_Isolation", "AI.exe"],\
        ["Call of Duty: Warzone","Call_of_Duty_Warzone", "CallOfDutyWarzone", "COD Warzone", "COD_Warzone", "Warzone", "ModernWarfare.exe", "ModernWarfare"],\
        ["Battlefield V","Battlefield 5", "Battlefield_V", "Battlefield_5", "bfv", "bf5", "bfv.exe"],\
        ["Rainbow Six Siege","Rainbow 6 Siege", "Rainbow Six: Siege","Rainbow 6: Siege", "Rainbow_Six_Siege","Rainbow_6_Siege", \
        "r6s", "RainbowSixSiege","Rainbow6Siege", "RainbowSix", "RainbowSixSiege", "RainbowSix.exe", "RainbowSix"],\
        ["Counter-Strike: Global Offensive","Counter Strike: Global Offensive", "ConunterStrike: Global Offensive",\
        "ConunterStrike", "cs:go","csgo", "cs-go", "csgo.exe"],\
        ["Rocket League","Rocket_League", "RocketLeague", "RocketLeague.exe"],\
        ["Genshin Impact", "GenshinImpact", "Genshin_Impact", "GenshinImpact.exe"], \
        ["Realm Royale", "Realm_Royale", "RealmRoyale", "Realm.exe", "Realm"], \
        ["Rogue Company", "Rogue_Company", "RogueCompany", "RogueCompany.exe"], \
        ["World of Tanks Blitz", "World_of_Tanks_Blitz", "World of Tanks: Blitz", "WorldOfTanksBlitz", "WoT Blitz", "WoT: Blitz",\
        "WoT_Blitz", "wotblitz", "wotblitz.exe"], \
        ["Hyperscape", "Hyperscape.exe"],\
        ["Warframe", "Warframe.x64.exe"],\
        ["Control", "Control_DX11.exe"],\
        ["DOTA2", "dota2.exe"],\
        ["Grand Theft Auto V", "gtav", "gta5", "GTA5.exe", "GTA V", "GTA_V", "gta_5"],\
        ["Splitgate", "PortalWars-Win64-Shipping.exe", "PortalWars"],\
        ["Fortnite", "FortniteClient-Win64-Shipping.exe"],\
        ["Valorant", "VALORANT-Win64-Shipping.exe"],\
        ["Paladins", "Paladins.exe"],\
        ["Overwatch 2", "Overwatch", "Overwatch.exe", "Overwatch2", "Overwatch_2"],\
        ["Dying Light", "DyingLightGame", "DyingLightGame.exe", "DyingLight"],\
        ["Resident Evil 4 (Remake)", "re4demo.exe", "re4demo"],\
        ["PUBG", "TslGame.exe", "TslGame"],\
        ["CS2", "Counter-Strike 2" , "cs2.exe"],\
        ["The Finals", "Finals" , "Discovery.exe"],\
        ["Doom Eternal", "DoomEternal" , "DOOMEternalx64vk.exe" ],\
    ]

    if inputName is None:
        for namesArr in gameAliases:
            print(namesArr[0])
        return []
    
    arrToReturn = []
    
    for namesArr in gameAliases:
        for potentialName in namesArr:
            if potentialName.upper() == inputName.upper():
                arrToReturn = namesArr

    for namesArr in gameAliases:
        for potentialName in namesArr:
            potentialNameUpper = potentialName.upper()
            inputNameUpper = inputName.upper()
            if potentialNameUpper.find(inputNameUpper) >= 0 or inputNameUpper.find(potentialNameUpper) >= 0:
                arrToReturn = namesArr

    if len(arrToReturn) == 0:
        print ("WARNING: '" + inputName + "' has no known aliases.")
    else:
        uppedArr = []
        for name in arrToReturn:
            uppedArr.append(name.upper())
        
        arrToReturn = uppedArr
        
    return arrToReturn # no lnown
