# msprites, media thumbnail sprites, multipule thumnails spirtes

# Requirements:

    1. FFmpeg
    2. ImageMagick Montage

# Steps:
    1. Extract images using ffmpeg. You can configure size of image and image rate per second(ips)
    2. Convert Image in spirtesheet of grid ROWSxCOLS
    3. Create a webvtt file of spritesheet images

It uses temp folder for storage. for persistence storage move these different folder or location.

Installation
```pip install msprites```

# How to use:
```
import os
from msprites import Settings as SpriteSetting
from msprites import MontageSprite

SpriteSetting.load(ips=0.50)
sprite = MontageSprites.from_media(
    path="..SampleVideo_360x240_20mb.mp4",create_webvtt=True
)

print(sprite.dir.name)
for filename in os.listdir(sprite.dir.name):
    print(filename)
```