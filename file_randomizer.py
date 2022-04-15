#!/usr/bin/env python
from PIL import Image
import hashlib

import datetime
import time
import random
import sys
import subprocess
import re

def randomFilename():
    # year, month, day, hour=0, minute=0, second=0, microsecond=0
    my_date = datetime.datetime(2022, 4, 1, 5, 3, 3)
    my_date2 = datetime.datetime(2022, 4, 15, 0, 0, 0)
    unix_time = random.randint(time.mktime(my_date.timetuple()), time.mktime(my_date2.timetuple()))
    final_string = str(int(unix_time)) + '{}'.format(random.randint(0, 999))

    return final_string

# will match first '.', so this won't work with filenames with two dots in them
def getExtension(file):
    extension = re.sub(r'.*\.', '', file)
    if extension == 'jpg_large' or extension == 'jpg_orig':
        extension = 'jpg'
    return '.' + extension

folder = sys.argv[1]

# Folder passed in should have a forward slash at the end
if folder[-1:] != "/":
    folder += "/"

files = subprocess.check_output(['find', folder, '-maxdepth', '1', '-type', 'f', '-printf', "%f\n"])
files = files.split('\n')

for file in files:
    if file != '':
        extension = getExtension(file)
        print(extension)
        subprocess.check_output(['mv', '{}{}'.format(folder, file), '{}{}{}'.format(folder, randomFilename(), extension)])