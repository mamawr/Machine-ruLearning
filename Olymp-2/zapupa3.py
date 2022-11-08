n, m, k = map(int, input().split())
state = [int(_) for _ in range(1, n + 1)]
flager = {}
for _ in range(m):
    pos1, pos2 = map(int, input().split())
    flager.pop(pos1, None)
    flager.pop(pos2, None)
    state[pos1 - 1], state[pos2 - 1] = state[pos2 - 1], state[pos1 - 1]
    
    if abs(state[pos1 - 1] - pos1) > k:
        flager[pos1] = 1

    if abs(state[pos2 - 1] - pos2) > k:
        flager[pos2] = 1
    
    print (1 if len(flager) > 0 else 0)