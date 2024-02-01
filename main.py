#!/usr/bin/env python3
import ffas_paperarchive as paperarchive
import ffas_jobcontrol as jobcontrol
import ffas_syscheck as syscheck
import sys

# MAIN PROGRAM ENTRANCE
# TODO: MOST FUNCTIONS ARE NOT IMPLEMENTED YET

print("+", "-"*20, "+", sep="")
print("Yet Another Full-Fledged Archive System")

# Check system platform.
# Currently only GNU/Linux is supported.
if syscheck.check_os:
    # Linux, pass.
    pass
else:
    # Not Linux
    print("Only GNU/Linux operating systems are supported currently.")
    print("Exiting normally.")
    sys.exit(0)

# Check first start.
try:
    open("camera_config.json")
    open("scanner_config.json")
except FileNotFoundError:
    # First time start
    print("First time use detected, starting setup wizard.")
    print("Camera setting up...")
    paperarchive.get_camera()
    print("Scanner setting up...")
    paperarchive.get_scanner()
    print("Setup completed.")

status = 1
while status:
    print("OPTIONS")
    print("1. Start a new scan")
    print("99. Quit")

    option = input(">> ")
    # Process the options
    option = int(option)
    if option == 1:
        jobcontrol.newjob()
    elif option == 99:
        print("Exiting cleanly.")
        status = 0
    else:
        print("Unknown command.")
        print("+", "-"*20, "+")
    
sys.exit(0)