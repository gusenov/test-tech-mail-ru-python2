# print range(4000)  # [0, 1, 2, ..., 3997, 3998, 3999]
# print range(4000)[2:]  # [2, 3, 4, ..., 3997, 3998, 3999]
result = []
for x in range(4000)[2:]:
    # print range(int(x**0.5)+1);
    # [0, 1] [0, 1]
    # [0, 1, 2] [0, 1, 2] [0, 1, 2] [0, 1, 2] [0, 1, 2]
    # [0, 1, 2, 3] [0, 1, 2, 3] [0, 1, 2, 3] [0, 1, 2, 3] [0, 1, 2, 3] [0, 1, 2, 3] [0, 1, 2, 3]

    # print range(int(x ** 0.5) + 1)[2:]
    # [] []
    # [2] [2] [2] [2] [2]
    # [2, 3] [2, 3] [2, 3] [2, 3] [2, 3] [2, 3] [2, 3]

    take = True
    for i in range(int(x ** 0.5) + 1)[2:]:
        if (x % i != 0) == False:
            take = False
            break
    if take:
        result.append(x)

# print result  # [2, 3, 5, ..., 3947, 3967, 3989]
# print result[:6]  # [2, 3, 5, 7, 11, 13]
print result[:6][-1]  # 13




N = 6
function = lambda x: all(x % i != 0 for i in range(int(x**0.5)+1)[2:])
a = filter(function, range(4000)[2:])[:N]
print a[-1]  # 13
