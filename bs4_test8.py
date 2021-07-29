import os
import re

filename = os.listdir("../연습/")

png_image = re.findall("\'(\w+)\.png\'", str(filename))

for i in png_image:
    print(i)