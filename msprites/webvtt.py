import os
import time
from msprites.settings import Settings

class WebVTT:
    HEADER = "WEBVTT\n"
    TIME_FORMAT = "%H:%M:%S.000"
    TIMELINE_FORMAT = "{start} --> {end}\n"
    IMAGE_TITLE_FORMAT = "{filename}#xywh={x},{y},{w},{h}\n\n"
    FILENAME = "master.webvtt"

    def __init__(self, sprites):
        self.sprites = sprites
        self.dir = sprites.dir

    def ips_to_seconds(self):
        return (1/Settings.IPS)

    def seconds_to_timestamp(self, ips):
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

    def get_sprite_content(self):
        contents = [WebVTT.HEADER]
        start, end, filename = 0, self.ips_to_seconds(), ""
        w, h, gridsize = Settings.WIDTH, Settings.HEIGHT ,Settings.ROWS * Settings.COLS
        for i in range(0, self.sprites.thumbs.count()):

            filename = Settings.spritefilename((i+1)//gridsize)
            contents+=[
                WebVTT.TIMELINE_FORMAT.format(
                    start=self.seconds_to_timestamp(start),
                    end=self.seconds_to_timestamp(end),
                ),
                WebVTT.IMAGE_TITLE_FORMAT.format(
                    x=self.getx(i, w, h), y=self.gety(i, w, h),
                    w=w, h=h, filename=filename,
                )
            ]
            start = end
            end += self.ips_to_seconds()
        return contents

    def get_thumbnail_content(self):
        contents = [WebVTT.HEADER]
        start, end, filename = 0, self.ips_to_seconds(), ""
        for i in range(0, self.sprites.thumbs.count()):
            filename = Settings.spritefilename(i+1)
            contents+=[
                WebVTT.TIMELINE_FORMAT.format(
                    start=self.seconds_to_timestamp(start),
                    end=self.seconds_to_timestamp(end),
                ),
                filename
            ]
            start = end
            end += self.ips_to_seconds()
        return contents

    def sprite_dest(self):
        return os.path.join(self.dir.name, self.FILENAME)

    def thumb_dest(self):
        return os.path.join(self.sprites.thumbs.dir.name, self.FILENAME)

    def generate_sprite_master(self):
        filename = self.sprite_dest()
        contents = self.get_sprite_content()
        with open(filename, "w") as f:
                f.writelines(contents)

    def generate_thumbnail_master(self):
        filename = self.thumb_dest()
        contents = self.get_thumbnail_content()
        with open(filename, "w") as f:
                f.writelines(contents)

    def generate(self):
        self.generate_sprite_master()
        self.generate_thumbnail_master()