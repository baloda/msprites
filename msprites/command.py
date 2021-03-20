import shlex
from subprocess import Popen
from subprocess import PIPE

class Command:

    @classmethod
    def shell(cls, command):
        sub = Popen(shlex.split(command), stdout=PIPE, stderr=PIPE)
        res, errs = sub.communicate(timeout=60 * 180)

        errs = errs.decode().strip() if errs and isinstance(errs, bytes) else errs
        res = res.decode().strip() if res and isinstance(res, bytes) else res
        return (res, errs)

    @staticmethod
    def execute(cmd):
        return Command.shell(cmd)