# -*- coding: utf-8 -*-
"""
put this file in the same directory of the files to unzip
start with:

python3 MTA-pcapUnziapper.py
"""

import os, zipfile

dir_name = './'
extension = "zip"

os.chdir(dir_name) # change directory from working dir to dir with files
password='infected'
for item in os.listdir(dir_name):
  print(item)
  if item.endswith(extension):
    file_name = os.path.abspath(item)
    print(file_name)
    zip_ref = zipfile.ZipFile(file_name)
    zip_ref.extractall(dir_name, pwd=bytes(password,'utf-8'))
    zip_ref.close() # close file
