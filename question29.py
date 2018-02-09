users = {'bob'}

# print bob in users  # NameError: name 'bob' is not defined
print 'bob' in users  # True
# print users.has_key('bob')  # AttributeError: 'set' object has no attribute 'has_key'
# print users.has_key(bob)  # AttributeError: 'set' object has no attribute 'has_key'
# print users.has_keys('bob')  # AttributeError: 'set' object has no attribute 'has_key'