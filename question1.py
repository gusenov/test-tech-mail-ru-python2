# -*- coding: utf-8 -*-

class Foo:
    def __init__(this):  # def __init__(self):
        this = Foo
        # print type(this)  # <type 'classobj'>
        try:
            this.var += [1]
        except:
            this.var = []


a = Foo()
# print type(a)  # <type 'instance'>
# Сработает исключение и Foo.var присвоится [].

b = Foo()
# print type(a)  # <type 'instance'>
# Исключения не будет потому что Foo.var уже проинициализирован значением [].
# [] + [1] = [1].

print a.var  # [1]
