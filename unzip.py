#!/bin/python3
import os
import zipfile

files = os.listdir()

for f in files:
    if f[-3:] == "zip":
        try:
            os.system(f"unzip {f} -d {f[:-4]}")
        except:
            print("fail")
    else:
        print("no zip files")
