import sys
from wand.image import Image

if len(sys.argv) < 3:
    print('{0} <Image 1> <Image 2>'.format(sys.argv[0]))
    sys.exit()

image1_path = sys.argv[1]
image2_path = sys.argv[2]

with Image(filename=image1_path) as image1:
    with Image(filename=image2_path) as image2:
        with image1.clone() as clone:
            clone.watermark(image2, 0.7, 100, 100)
            clone.save(filename= image1_path + "_" + image2_path)