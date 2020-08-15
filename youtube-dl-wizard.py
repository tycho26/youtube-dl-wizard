#TODO: Create config for youtube-dl.exe location.

import os

url = ""
videoFormat = "mp4"
audioOnly = False
audioFormat = "mp3"
playlist = ""
downloadPlaylist = False
keepThumbnail = True
command = "youtube-dl"

videoFormats = ["mp4","webm"]

def GetUrl():
    global url
    url = input("What URL would you like to download? ")
    #Implement regex
    if(url != ""):
        if("list" in url):
            choice = input("It appears the video you chosen is part of a playlist, do you want to download the whole playlist? y/n ")
            if(choice == "y" or choice == "Y"):
                global downloadPlaylist
                downloadPlaylist = True
            elif(choice == "n" or choice == "N"):
                downloadPlaylist
                downloadPlaylist = False
            else:
                print("Invalid option, try again.")
                GetUrl()
        return
    else:
        print("URL cannot be empty")
        GetUrl()

def GetAudioFormat():
    choice = input("Do you want audio only? y/n ")
    if(choice == "y" or choice == "Y"):
        global audioOnly
        audioOnly = True
        #Select audio format
    elif(choice == "n" or choice == "N"):
        audioOnly
        audioOnly = False
        return
    else:
        print("Invalid option, try again.")
        GetAudioFormat()

def GetVideoFormat():
    print("What video format do you want? ")
    for num, format in enumerate(videoFormats, start=1):
        print(num,": "+format)
    choice = input()
    choice = int(choice)
    global videoFormat
    videoFormat = videoFormats[choice-1]

def GetThumbnail():
    choice = input("Do you want to embed the original thumbnail into the download? y/n ")
    if(choice == "y" or choice == "Y"):
        global keepThumbnail
        keepThumbnail = True
    elif(choice == "n" or choice == "N"):
        keepThumbnail
        keepThumbnail = False
    else:
        print("Invalid option, try again.")
        GetThumbnail()

def BuildCommand():
    global command
    
    if(keepThumbnail == True):
        command = command+" --write-thumbnail"

    if(downloadPlaylist == True):
        command = command+" --yes-playlist"
    else:
        command = command+" --no-playlist"

    if(audioOnly == True):
        command = command+" -x --audio-format "+audioFormat
    else:
        command = command+" -f "+videoFormat

    command = command+" \""+url+"\""
    
    print(command)

def Wizard():
    GetUrl()
    GetAudioFormat()
    if(audioOnly == False):
        GetVideoFormat()
    GetThumbnail()
    BuildCommand()

Wizard()


os.system(command)
