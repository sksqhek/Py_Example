import sys
from wand.image import Image

if len(sys.argv) < 5:
    print('{0} <ORIGINAL PATH> <BRIGHTNESS> <SATURATION> <HUE>'
          .format(sys.argv[0]))
    sys.exit()

original_path = sys.argv[1]
brightness = float(sys.argv[2])
saturation = float(sys.argv[3])
hue = (float(sys.argv[4]) * 100 / 180 ) + 100 

with Image(filename=original_path) as image:
    with image.clone() as clone:
        clone.modulate(brightness, saturation, hue) 
        clone.save(filename= 'modulated_' + original_path)