
def geometric(P, X):
    G = (1 - P) ** (X - 1) * P
    return G

A, B = map(float, input().split())

X = int(input())

P = A / B

G = 0

for i in range(1, 6): 
    G = G + geometric(P, i)

print("%.3f" %G)