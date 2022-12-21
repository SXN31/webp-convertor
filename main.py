#!/usr/bin/python

import sys
from pathlib import Path
from PIL import Image

args = sys.argv[1:]
lengthArgs = len(args)
count = 1
countWritten = 0

#let's use is_dir() from pathlib later to check if something is a directory or not
#let's use with_suffix('.png') to change the suffix
print(f"Reading {lengthArgs} arguments.")
print(f"-------------------------------------------")
for arg in args:
    print(f"Processing {count} of {lengthArgs} images")    
    image_webp = arg
    #image_png = str(arg) + ".png"
    extension = Path(image_webp).suffix
    if not extension == ".png":      
        pngPath = Path(image_webp).with_suffix('.png')
        if not pngPath.is_file():
            print(f"Processing: {image_webp}")
            loadedImage = Image.open(image_webp)
            loadedImage.save(pngPath, format="png", lossless=True)
            print(f"Wrote file {pngPath}")
            countWritten += 1
        else:
            print(f"Skipping existing file: {pngPath}")
    else:
        print(f"File is a png, skipping: {image_webp}")
    percent = round((count / lengthArgs)*100,2)
    count+=1
    print(f"Progress: {percent}% complete. \n")
print(f"-------------------------------------------")
print(f"Job complete. {countWritten} pngs created.")














