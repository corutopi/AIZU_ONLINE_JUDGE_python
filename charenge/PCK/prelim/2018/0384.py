
def solve():
    a, n, m = map(int, input().split())

    max_y = len(str(m)) * 9
    count = 0
    for y in range(1, max_y + 1):
        x = (y + a) ** n
        if x <= m and y == sum([int(i) for i in str(x)]):
            # print(x, y, a)
            count += 1
    print(count)


if __name__ == '__main__':
    solve()
