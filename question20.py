l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print list(l)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print max(l)  # 9
print min(l)  # 0
# index(l)  # NameError: name 'index' is not defined
# count(l)  # NameError: name 'count' is not defined
print len(l)  # 10
print sorted(l) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# remove(l)  # NameError: name 'remove' is not defined
# append(l)  # NameError: name 'append' is not defined

print l.index(5)  # 5
print l.count(6)  # 1
print l.remove(5)  # None
print l.append(5)  # None