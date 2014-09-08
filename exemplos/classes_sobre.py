# A classe String deriva de str
class String(str):
    def __sub__(self, s):
        return self.replace(s, '')

s1 = String('The Lamb Lies Down On Broadway')
s2 = 'Down '

print '"%s" - "%s" = "%s"' % (s1, s2, s1 - s2)
