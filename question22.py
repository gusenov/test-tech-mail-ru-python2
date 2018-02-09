class Rational(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q

    def __lt__(self, other):
        return self.p * other.q < other.p * self.q

    def __repr__(self):
        return "%d/%d" % (self.p, self.q)


a = [Rational(1, 2), Rational(3, 4), Rational(3, 5)]
a.sort()
print a  # [1/2, 3/5, 3/4]
