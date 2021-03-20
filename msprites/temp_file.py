class TempFile:
    def __init__(self, name):
        self.name = name
    def cleanup(self):
        os.unlink(self.name)