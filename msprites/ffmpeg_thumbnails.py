import os
import tempfile
from msprites.command import Command
from msprites.settings import Settings
from msprites.constants import FFMPEG_THUMBNAIL_IMAGES
from msprites.temp_file import TempFile


class FFmpegThumbnails(Settings):

    def __init__(self, filename):
        self.filename = filename
        self.dir = tempfile.TemporaryDirectory()

    def dest(self):
        return os.path.join(self.dir.name, self.FILENAME_FORMAT.format(ext=self.EXT))

    def generate(self):
        cmd = FFMPEG_THUMBNAIL_IMAGES.format(
            input=self.filename, ips=self.IPS, width=self.WIDTH,
            height=self.HEIGHT, output=self.dest()
        )
        result = Command.execute(cmd=cmd)

    def cleanup(self):
        self.dir.cleanup()

    def count(self):
        imlist = os.listdir(self.dir.name)
        return len(imlist)

    @classmethod
    def from_media(cls, path):
        thumbs = FFmpegThumbnails(filename=path)
        thumbs.generate()
        return thumbs