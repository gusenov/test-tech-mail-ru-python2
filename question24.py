import itertools

a = [1, 2, 3]
print list(itertools.permutations(a, 3))[3]  # (2, 3, 1)

for p in itertools.permutations(a, 3):
    print p
# (1, 2, 3)
# (1, 3, 2)
# (2, 1, 3)
# (2, 3, 1)
# (3, 1, 2)
# (3, 2, 1)
