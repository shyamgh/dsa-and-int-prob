
def print_max_move(arr_len, t):
    count = 0
    for i in range(0, arr_len, 3):
        count += 1
        print(i)
    print('Case #{}: {}'.format(t, count))


t = 0

try:
    t = int(input())
    for i in range(t):
        n = int(input())
        print_max_move(n, i+1)
except Exception as e:
    pass
