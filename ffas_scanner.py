#!/usr/bin/env python3
import os

def scanfromscanner(uri, filename, mode="Color", resolution="300"):
    scancmd = "scanimage --format png -d '{}' --resolution {} -p -o {} --mode {}".format(uri, str(resolution), filename, mode)
    print("+ {}".format(scancmd))
    os.system(scancmd)
    return True