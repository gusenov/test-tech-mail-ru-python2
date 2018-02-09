# -*- coding: utf-8 -*-


class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def fromstring(cls, s):
        day, month, year = map(int, s.split('-'))
        return Date(day, month, year)
    
    # @classmethod
    # @staticmethod
    # def fromstring(s):
    #     day, month, year = map(int, s.split('-'))
    #     return Date(day, month, year)

    def __str__(self):
        return '%02d-%02d-%02d' % (self.day, self.month, self.year)


# with @classmethod and cls
d = Date.fromstring('01-02-2012')
print d  # 01-02-2012

# with @classmethod only
# d = Date.fromstring('01-02-2012')
# print d  # TypeError: fromstring() takes exactly 1 argument (2 given)

# with @staticmethod
# d = Date.fromstring('01-02-2012')
# print d  # 01-02-2012
