import os
import time
from msprites.settings import Settings

class WebVTT:
    HEADER = "WEBVTT\n"
    TIME_FORMAT = "%H:%M:%S"
    TIMELINE_FORMAT = "{start} --> {end}\n"
    IMAGE_TITLE_FORMAT = "{filename}#xywh={x},{y},{w},{h}\n\n"
    FILENAME = "sprite.webvtt"

    def __init__(self, sprites):
        self.sprites = sprites
        self.dir = sprites.dir

    def ips_seconds_to_timestamp(self, ips):
        return time.strftime(WebVTT.TIME_FORMAT, time.gmtime(ips))

    def getx(self, imnumber, w, h):
        # coridinate in sprite image for a given image
        gridsize = Settings.ROWS * Settings.COLS
        imnumber = imnumber-((imnumber//gridsize)*gridsize)
        hindex = imnumber//Settings.ROWS
        windex = imnumber % Settings.COLS
        return windex*w

    def gety(self, imnumber, w, h):
        # coridinate in sprite image for a given image
        gridsize = Settings.ROWS * Settings.COLS
        imnumber = imnumber-((imnumber//gridsize)*gridsize)
        hindex = imnumber//Settings.ROWS
        windex = imnumber % Settings.COLS
        return hindex*h


    def content(self):
        contents = [WebVTT.HEADER]
        start, end, filename = 0, Settings.IPS, ""
        w, h, gridsize = Settings.WIDTH, Settings.HEIGHT ,Settings.ROWS * Settings.COLS
        for i in range(0, self.sprites.thumbs.count()):

            filename = Settings.spritefilename((i+1)//gridsize)
            contents+=[
                WebVTT.TIMELINE_FORMAT.format(
                    start=self.ips_seconds_to_timestamp(start),
                    end=self.ips_seconds_to_timestamp(end),
                ),
                WebVTT.IMAGE_TITLE_FORMAT.format(
                    x=self.getx(i, w, h), y=self.gety(i, w, h),
                    w=w, h=h, filename=filename,
                )
            ]
            start = end
            end += Settings.IPS
        return contents

    def dest(self):
        return os.path.join(self.dir.name, self.FILENAME)

    def generate(self):
        with open(self.dest(), "w") as f:
            f.writelines(self.content())