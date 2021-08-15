#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyAesCrypt
from stdiomask import getpass


def checkprogress(checkpoint):
    if checkpoint == 0:
        return print("Progress: 0%")
    elif checkpoint == 1:
        return print("Progress: 60%")
    elif checkpoint == 2:
        return print("Progress: 80%")
    elif checkpoint == 3:
        return print("Progress: 100%")


file_name = input("Input your filename here (same dir with extension): ")

password = getpass(prompt="Password: ", mask="*")
checkprogress(0)
checkprogress(1)
checkprogress(2)

pyAesCrypt.encryptFile(f"./{file_name}", f"./{file_name}.pyenc", password)
checkprogress(3)



