n, m = map(int, input().split())
counter = 1
for i in range(1, m + 1):
    a, b = map(int, input().split())
    if i == 1 or i == n:
        print(m)
    else:
        while i != b:
            counter += 1
            i += 1
        print(counter)
