# -*- coding: utf-8 -*-

N = 3
a = [[i*N+j for j in range(N)][::1 if i % 2 == 0 else -1] for i in range(N)]
print a[1][2]  # 3

for i in range(N):
    print [i*N+j for j in range(N)], '[::', 1 if i % 2 == 0 else -1, ']', '->', [i * N + j for j in range(N)][::1 if i % 2 == 0 else -1]
