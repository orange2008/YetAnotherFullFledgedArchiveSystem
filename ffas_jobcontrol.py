#!/usr/bin/env python3

import ffas_paperarchive as paperarchive
import os

def newjob():
    """This is an interactive function."""
    # TODO, DPI and scan mode settings
    dpi = 300
    mode = "Color"
    try:
        print("Scanning for barcode.")
        print("To manually enter, press Control+C (SIGINT)")
        barcode = paperarchive.scanbarcode()
        barcode = str(barcode)
    except KeyboardInterrupt:
        barcode = input("Barcode: ")
        barcode = str(barcode)
    print("Barcode: {}".format(str(barcode)))
    counter = 0
    print("Scan Job created.")
    pausing = input("Press 'Enter/Return' to continue.")
    print("Start to scan")
    os.mkdir(str(barcode))
    while True:
        counter += 1
        current_filename = paperarchive.scanfromscanner(barcode, counter, "./" + str(barcode))
        opt = input("Press 'y' for preview, 'q' to end the job, otherwise we'll start a new scan: ")
        if str(opt) == 'y':
            os.system("xdg-open " + "./" + str(barcode) + "/" + str(current_filename))
            pausing = input("Press any key to continue.")
        elif str(opt) == 'q':
            break
    print("-"*20)
    print("Job Summary")
    print("Barcode: ", barcode)
    print("Total Pages: ", counter)
    print("DPI: ", dpi)
    print("Scan Mode: ", mode)
    print("-"*20)
    return True