import subprocess

class DefaultLogger():
    def __init__(self, externals=[]):
        self.externals = externals
    def log(self, mes):
        subprocess.call('echo "{}"'.format(mes), shell=True)
        self._external_log(mes)
    def error(self, mes):
        subprocess.call('echo "[ERROR]{}"'.format(mes), shell=True)
        self._external_log(mes)
    def _external_log(self, mes):
        for ex in self.externals:
            ex.log(mes)
    def _external_error(self, mes):
        for ex in self.externals:
            ex.error(mes)
