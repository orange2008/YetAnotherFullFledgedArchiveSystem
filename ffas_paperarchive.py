#!/usr/bin/env python3
import ffas_barcode as barcode
import json

def get_camera():
    try:
        with open("camera_config.json") as f:
            obj = json.load(f)
    except:
        obj = {} # just make errors lol, who cares
    try:
        camindex = obj['camera_index']
    except KeyError:
        # No Camera config available
        camindex = barcode.list_cameras()
        # Should let UI take care of this, but screw it, who cares.
        if not camindex:
            # No Cameras
            print("No Camera found.")
            return False # Not going to exit the program directly.
        else:
            print("Available Camera IDs: ", end=" ")
            for i in camindex:
                print(i, sep=", ", end=" ")
            loopstatus = 1
            while loopstatus:
                print("")
                option = input("Which to use?(usually 0 is the default one): ")
                option = int(option)
                if option not in camindex:
                    print("Not valid camera option.")
                else:
                    loopstatus = 0
            camconfig = {"camera_index": int(option)}
        with open("camera_config.json", 'w') as f:
            json.dump(camconfig, f)
    return camindex

def scan():
    camindex = get_camera()
    scanned = barcode.main(camindex)
    print(scanned)

scan()