
def solve():
    N = int(input())
    S = input()
    stomp = 0
    for i in range(1, len(S)):
        pass
    i = 0
    while True:
        if i >= len(S) - 1:
            break
        if S[i] != S[i + 1]:
            stomp += 1
            i += 1
        i += 1
    print(stomp)


if __name__ == '__main__':
    solve()
