#!/usr/bin/env python3
import platform

def check_os():
    pf = platform.system()
    print(pf)
    if "Linux" not in str(pf):
        # Not GNU/Linux
        return False
    else:
        return True
    return True