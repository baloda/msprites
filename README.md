# msprites, media thumbnail sprites, multipule thumbnail spirtes

# Requirements:

    1. FFmpeg
    2. ImageMagick Montage

# Steps:
    1. Extract images using ffmpeg. You can configure size of image and image rate per second(IPS)
    2. Convert Image in spirtesheet of grid ROWSxCOLS
    3. Create a webvtt file of spritesheet images

Recomanded Values for IPS:
    1
    0.50: 1 image every 2 seconds)
    0.25: 1 image in every 4 second
    0.20: 1 image in every 5 second
    0.10: 1 image in every 10 second
    0.05: 1 image in every 20 second

It uses temp folder for storage. for persistence storage move these different folder or location.

Installation
```pip install msprites```

# How to use:
```
import os
from msprites import Settings as SpriteSetting
from msprites import MontageSprites

SpriteSetting.load(ips=0.50)
sprite = MontageSprites.from_media(
    path="..SampleVideo_360x240_20mb.mp4",create_webvtt=True
)

print(sprite.dir.name)
for filename in os.listdir(sprite.dir.name):
    print(filename)
```
