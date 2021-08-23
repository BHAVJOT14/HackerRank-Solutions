
def fact(N):
    if N == 0:
        return 1
    else:
        return N * fact(N - 1)

def combi(N, X):
    result = fact(N) / (fact(N - X) * fact(X))
    return result

def bino(X, N, P):
    Q = 1 - P
    result = combi(N, X) * (P ** X) * (Q ** (N - X))
    return result

if __name__ == '__main__':
    L, R = list(map(float, input().split()))
    Odd = L / R
    TOTAL = list()
    for i in range(3, 7):
        TOTAL.append(bino(i, 6, Odd / (1 + Odd)))
    print(round(sum(TOTAL), 3))