#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyAesCrypt
from stdiomask import getpass

file_name = input("Input your filename here (same dir with .pyenc): ")
password = getpass(prompt="Password: ", mask="*")


def checkprogress(checkpoint):
    if checkpoint == 0:
        return print("Progress: 0%")
    elif checkpoint == 1:
        return print("Progress: 20%")
    elif checkpoint == 2:
        return print("Progress: 60%")
    elif checkpoint == 3:
        return print("Progress: 100%")


with open(file_name, 'rb') as enc_file:
    checkprogress(0)
    striped_file_name = file_name[:-6]
    checkprogress(1)
    pyAesCrypt.decryptFile(f"./{file_name}", f"./decrypted {striped_file_name}", password)
    checkprogress(2)
    enc_file.close()
    checkprogress(3)