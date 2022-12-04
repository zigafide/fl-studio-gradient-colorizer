#!/usr/bin/python

import os
import sys

from colour import Color
import configparser
#rootdir = 'D:/FL STUDIO!/!SAMPLES/!SWAIN -PARANOID'

config_folder = ''
config_folder_color1 = ''
config_folder_color2 = ''
config_file_color1 = ''
config_file_color2 = ''
config_ignore_subs = ''

def main():
    loadsettings('settings.txt')
    os.system('color 4')
    print("Make sure the settings below are correct before continuing.")
    print("Folder: "+config_folder)
    print("Ignore subfolders: " + config_ignore_subs)
    input("Press enter if these settings are correct.")
    os.system('color a')
    # remove nfo files first
    if config_ignore_subs == 'false':
        for subdir, dirs, files in os.walk(config_folder):
            for file in files:
                # print(os.path.splitext(file)[1])
                if os.path.splitext(file)[1] == ".nfo":
                    os.remove(subdir + os.sep + file)
    if config_ignore_subs == 'true':
        for file in os.listdir(config_folder):
            if os.path.splitext(file)[1] == ".nfo":
                os.remove(config_folder + os.sep + file)

    # dict1 is wavs

    dirlist = []
    dict1 = {}

    #if ignore sub folders is true, we will not use os.walk

    if config_ignore_subs == 'false':
        for subdir, dirs, files in os.walk(config_folder):
            if subdir not in dirlist:
                dirlist.append(subdir)
            for file in files:
                count = dict1.get(subdir, 0)
                count = count + 1
                dict1[subdir] = count
                if subdir not in dirlist:
                    dirlist.append(subdir)

    if config_ignore_subs == 'true':
        for file in os.listdir(config_folder):
            subdir = config_folder+os.sep+file
            if subdir not in dirlist:
                dirlist.append(subdir)
                
    #make root folder colored
    
    originalpath = os.getcwd()
    os.chdir(config_folder)
    os.chdir('../')
    with open(os.path.basename(config_folder) + ".nfo", 'w') as f:
            color1 = Color(config_folder_color1)

            sys.stdout.write("\rcurrent file: "+os.path.basename(config_folder)+"...................................")
            finalcolor = str(color1.hex_l)[1:]
            finalcolorfinal = finalcolor[4]+finalcolor[5]+finalcolor[2]+finalcolor[3]+finalcolor[0]+finalcolor[1]
            f.write('Color=$' + finalcolorfinal + '\n')
            f.write('IconIndex=21\n')
            f.write('HeightOfs=0\n')
            f.write('SortGroup=1\n')
            f.write('---------\n')
            f.write("colorized by zigafide's colorizer\n")
            f.write('follow @zigafidethegod on Instagram')
    os.chdir(originalpath)

   
    #dirlist.append(config_folder)
    folderindex = {}
    foldersize = {}
    #add all folders to dict
    for folder in dirlist:
    	folderindex[os.path.dirname(folder)] = 0
    	foldersize[os.path.dirname(folder)] = 0
    	
    for folder in dirlist:
        foldersize[os.path.dirname(folder)] = foldersize[os.path.dirname(folder)] + 1 
     
    
    for folder in dirlist:
        foldername = os.path.basename(folder)
        # print(dict1[key])
        if os.path.isfile(folder):
            foldername = os.path.splitext(foldername)[0]
        with open(os.path.dirname(folder) + os.sep + foldername + ".nfo", 'w') as f:
            color1 = Color(config_folder_color1)
            color2 = Color(config_folder_color2)
            colors = list(color1.range_to(color2, foldersize[os.path.dirname(folder)]))

            sys.stdout.write("\rcurrent file: "+foldername+"...................................")
            finalcolor = str(colors[folderindex[os.path.dirname(folder)]].hex_l)[1:]
            finalcolorfinal = finalcolor[4]+finalcolor[5]+finalcolor[2]+finalcolor[3]+finalcolor[0]+finalcolor[1]
            f.write('Color=$' + finalcolorfinal + '\n')
            f.write('IconIndex=21\n')
            f.write('HeightOfs=0\n')
            f.write('SortGroup=1\n')
            f.write('---------\n')
            f.write("colorized by zigafide's colorizer\n")
            f.write('follow @zigafidethegod on Instagram')
            folderindex[os.path.dirname(folder)] = folderindex[os.path.dirname(folder)] + 1

    for key in dict1.keys():
        for subdir, dirs, files in os.walk(key):
            index = 0
            howmanyfiles = dict1[key]
            for file in files:
                # print(file)
                # print(dict1[key])
                if not os.path.splitext(file)[1] == '.nfo':
                    if os.path.isfile(key + os.sep + file):
                        with open(key + os.sep + os.path.splitext(file)[0] + ".nfo", 'w') as f:
                            # convert hex to decimal
                            color1 = Color(config_file_color1)
                            color2 = Color(config_file_color2)
                            colors = list(color1.range_to(color2, howmanyfiles))

                            extension = os.path.splitext(file)[1]
                            iconindex = iconfromext(extension)

                            sys.stdout.write("\rcurrent file: " + file+"...................................")
                            finalcolor = str(colors[index].hex_l)[1:]
                            finalcolorfinal = finalcolor[4]+finalcolor[5]+finalcolor[2]+finalcolor[3]+finalcolor[0]+finalcolor[1]
                            f.write('Color=$' + finalcolorfinal + '\n')
                            f.write('IconIndex=' + str(iconindex) + '\n')
                            f.write('HeightOfs=0\n')
                            f.write('SortGroup=1\n')
                            f.write('---------\n')
                            f.write("colorized by zigafide's colorizer\n")
                            f.write('follow @zigafidethegod on Instagram')
                        index = index + 1


#function for deciding which icon to use
def iconfromext(ext):
    match ext:
        case '.wav':
            return 33
        case '.mid':
            return 9
        case _:
            return 33


def loadsettings(filename):
    config = configparser.ConfigParser()
    config.read("settings.txt")
    global config_folder
    global config_folder_color1
    global config_folder_color2
    global config_file_color1
    global config_file_color2
    global config_ignore_subs
    config_folder = config.get("config", "drumkit_folder")
    config_folder_color1 = config.get("config", "folders_color1")
    config_folder_color2 = config.get("config", "folders_color2")
    config_file_color1 = config.get("config", "files_color1")
    config_file_color2 = config.get("config", "files_color2")
    config_ignore_subs = config.get("config", "ignore_sub_folders")

main()

print("\nDone!")
print("Script by zigafide")
input(".")