
def solve():
    A, B, C = map(int, input().split())
    count = 0
    coins = 0
    while True:
        if coins >= C:
            break
        count += 1
        coins += A
        if count % 7 == 0:
            coins += B
    print(count)


if __name__ == '__main__':
    solve()
