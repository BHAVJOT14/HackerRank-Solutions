
X = int(input())

arr = list(map(int, input().split()))
weight = list(map(int, input().split()))

Y = 0

for i in range(X):
    Y = Y + arr[i] * weight[i]

print("{:.1f}".format(Y / sum(weight)))