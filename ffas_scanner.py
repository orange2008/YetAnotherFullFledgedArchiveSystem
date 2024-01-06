#!/usr/bin/env python3
import os

def scanfromscanner(uri, mode="Color", resolution="300", filename="1.png"):
    scancmd = "scanimage --format png -d '{}' --resolution {} -p -o {} --mode {}".format(uri, str(resolution), filename, mode)
    print("+ {}".format(scancmd))
    os.system(scancmd)
    # Try to get a barcode from it
    
    return True