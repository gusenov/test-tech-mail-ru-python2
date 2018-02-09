l = ['a', 'b', 'c']

# print l.values()  # AttributeError: 'list' object has no attribute 'values'
# print l.contains()  # AttributeError: 'list' object has no attribute 'contains'
# print l.sorted()  # AttributeError: 'list' object has no attribute 'sorted'
# print l.type()  # AttributeError: 'list' object has no attribute 'type'
# print l.items()  # AttributeError: 'list' object has no attribute 'items'
# print l.len()  # AttributeError: 'list' object has no attribute 'len'
# print l.str()  # AttributeError: 'list' object has no attribute 'str'

# print values(l)  # NameError: name 'values' is not defined
# print contains(l)  # NameError: name 'contains' is not defined
# print items(l)  # NameError: name 'items' is not defined

print sorted(l)  # ['a', 'b', 'c']
print type(l)  # <type 'list'>
print len(l)  # 3
print str(l)  # ['a', 'b', 'c']
