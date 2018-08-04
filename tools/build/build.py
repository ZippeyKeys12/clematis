#!/usr/bin/env python
import os
import re
import json
import shutil
from distutils.dir_util import copy_tree

from strip import ZStript
from generate import ZGenerate
from preprocess import ZPreprocess

SETTINGS = {
    "ModName": "Clematis",
    "Version": 3.3,
    "IniFiles": [
        "ZCONFIG"
    ]
}


def ZBuild(Settings, Compress):
    # Build Settings
    ModName = Settings["ModName"]
    # Clean build destination
    print("Cleaning Build Destination: ", end="")
    BuildFolder = "dist/"+ModName
    if os.path.exists(BuildFolder):
        shutil.rmtree(BuildFolder)

    # Make build destination and duplicate files
    os.makedirs(BuildFolder)
    copy_tree("src", BuildFolder)
    print("Successful")

    # Move to Build Folder
    os.chdir(BuildFolder+"/")

    # Compact ZScript
    print("Compacting ZScript")
    StartLump = "ZSCRIPT.zsc"
    FullFile = open(StartLump).read()
    FullFile = ZStript(FullFile)
    FullFile = ZPreprocess(FullFile)
    FullFile = ZGenerate(FullFile)
    if Compress:
        FullFile = ZStript(FullFile, True)
    FullFile = "version \"{}\"".format(Settings["Version"])+FullFile
    os.remove("ZSCRIPT.zsc")
    with open(StartLump, "w+") as Output:
        Output.write(FullFile)
    shutil.rmtree("ZSCRIPT")
    print("Compacting ZScript: Successful")
    os.chdir("../")
    if os.path.isfile(ModName+".zip"):
        os.remove(ModName+".zip")
    ArchiveName = ModName+".pk3"
    if os.path.isfile(ArchiveName):
        os.remove(ArchiveName)

    # Compression
    if Compress:
        print("Compressing PK3 Archive: ", end="")
        shutil.make_archive(ModName, "zip")
        os.rename(ModName+".zip", ArchiveName)
        shutil.rmtree(ModName)
        print("Successful")


if __name__ == "__main__":
    from sys import argv
    Compress = False
    for arg in argv[1:]:
        if arg.startswith('-C'):
            Compress = True
    ZBuild(SETTINGS, Compress)
