# rename.py
#
# Methodically renames files, like that large cache of images you forgot about
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

import os

OLD_EXT = "bin"
NEW_EXT = "txt"

for thisFile in os.listdir(os.getcwd()):

    print("found    {}".format(thisFile))

    nameArr = os.path.splitext(thisFile)

    if(nameArr[-1] == ".{}".format(OLD_EXT)):
        newName = "{}.{}".format(nameArr[0], NEW_EXT)
        print("renaming {} -> {}".format(thisFile, newName))
        os.rename(thisFile, newName)
