class Settings:
    IPS = 5 #  will be used as 1/5 one in every 5 sec
    WIDTH = 128
    HEIGHT = 72
    EXT = ".jpeg"
    ROWS = 30
    COLS = 30
    FILENAME_FORMAT = "%04d{ext}"

    @classmethod
    def load(cls, width=None, height=None, ips=None, ext=None, rows=None, cols=None):
        cls.IPS = ips or cls.IPS
        cls.EXT = ext or cls.EXT
        cls.ROWS = rows or cls.ROWS
        cls.COLS = cols or cls.COLS
        cls.WIDTH = width or cls.WIDTH
        cls.HEIGHT = height or cls.HEIGHT

    @classmethod
    def spritefilename(cls, number):
        name = cls.FILENAME_FORMAT % number
        return name.format(ext=cls.EXT)
