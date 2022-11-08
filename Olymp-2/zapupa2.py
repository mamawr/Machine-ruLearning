n, m, k = map(int, input().split())
amount = [int(_) for _ in range(1, n + 1)]
pos_1, pos_2 = 0, 0
flag = True
pos_1, pos_2 = 0, 0
for _ in range(m):
    flag = True
    pos_1, pos_2 = map(int, input().split())
    amount[pos_1 - 1], amount[pos_2 - 1] = amount[pos_2 - 1], amount[pos_1 - 1]
    for i in range(1, n + 1):
        if abs((amount.index(i) + 1) - i) > k:
            print(1)
            flag = False
            break
    if flag:
        print(0)
