# fixCreateStamp.py
#
# Pull EXIF DateTimeOriginal and adjust the file Create Date to match
# Prints the suggested commands rather than executing them, so you can eyeball for correctness
# Works with JPEG only! Known to NOT work on MOV and HEIC
# Compatibility: macOS
#
################################################################################
# Copyright 2022 Kyle Botteon
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
################################################################################
#!/usr/bin/env python3

import sys
import os
import subprocess
# https://pillow.readthedocs.io/en/stable/reference/Image.html
from PIL import Image

EXIF_DATE_TIME_ORIGINAL = 36867

def main(fileList):

    for file in fileList:

        # Extract EXIF DateTimeOriginal
        imageHandle = Image.open(file)
        exif = imageHandle._getexif() # .getexif() doesn't work?
        dateTimeOriginal = exif.get(EXIF_DATE_TIME_ORIGINAL)

        # If there is no EXIF data, can't do much here; try the next file
        if dateTimeOriginal == None:
            print(f"No EXIF data found in {file}")
            continue

        # Extract date-time to reformat into a shell command
        exifYear = dateTimeOriginal[0:4]
        exifMonth = dateTimeOriginal[5:7]
        exifDay = dateTimeOriginal[8:10]
        exifHour = dateTimeOriginal[11:13]
        exifMin = dateTimeOriginal[14:16]
        exifSec = dateTimeOriginal[17:19]

        # Form and print the suggested commands
        command = "SetFile"
        args = "-d \"{}/{}/{} {}:{}:{}\" {}".format( \
            exifMonth, exifDay, exifYear, exifHour, exifMin, exifSec, file)
        print(f"{command} {args}")

if __name__ == "__main__":

    args = []
    for arg in sys.argv[1:]:
        # Skip directories
        if not os.path.isdir(arg):
            args.append(arg)

    main(args)
