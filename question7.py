# -*- coding: utf-8 -*-

s1 = b'Hello, world'  # байтовая строка
# Байтовые строки поддерживают практически все строковые методы.

s2 = u'Hello, world'  # строка Unicode

s3 = r'Hello, world'  # "сырая" строка (механизм экранирования отключается)

s4 = ur'Hello, world'  # "сырая" строка Unicode

s5 = 'Hello, world'  # не нужно экранировать кавычки и нужно экранировать апострофы внутри, вот так \'

# Многострочный блок текста.
# Внутри такой строки возможно присутствие кавычек и апострофов, главное, чтобы не было трех кавычек подряд.
s6 = '''Hello, world'''

# s7 = ''Hello, world''  # SyntaxError: invalid syntax
# s8 = ""Hello, world""  # SyntaxError: invalid syntax

s9 = "Hello, world"  # не нужно экранировать апострофы и нужно экранировать кавычки внутри, вот так \"
