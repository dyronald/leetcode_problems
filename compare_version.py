class VersionWalker:
    def __init__(self, version: str):
        self.version = version
        self.cur = 0

    def next(self):
        if self.cur > len(self.version):
            return None

        dot = self.version.find('.', self.cur)
        if dot == -1:
            dot = len(self.version) 
        rev = int(self.version[self.cur:dot])
        self.cur = dot + 1
        return rev

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ver1 = VersionWalker(version1)
        ver2 = VersionWalker(version2)

        while True:
            rev1 = ver1.next()
            rev2 = ver2.next()
            result = self.cmp(rev1, rev2)

            if result != 0 or (rev1 is None and rev2 is None):
                break
                
        return result

    def cmp(self, val1, val2):
        val1 = 0 if val1 is None else val1
        val2 = 0 if val2 is None else val2

        if val1 < val2:
            return -1
        elif val1 > val2:
            return 1
        else:
            return 0

