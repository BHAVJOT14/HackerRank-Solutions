def mean(X):
    
    return sum(X)/len(X)

def lsr(X, Y):
    
    B = sum([(X[i] - mean(X)) * (Y[i] - mean(Y))
             for i in range(len(X))]) / sum([(j - mean(X)) ** 2 for j in X])
    A = mean(Y) - (B * mean(X))
    return A + (B * 80)

X = []
Y = []

for i in range(5):
    A, B = list(map(int, input().split()))
    X.append(A)
    Y.append(B)

print(round(lsr(X, Y), 3))