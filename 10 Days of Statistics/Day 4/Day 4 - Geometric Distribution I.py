
# Enter your code here. Read input from STDIN. Print output to STDOUT

A, B = map(int, input().split())

C = int(input())

P = float(A / B)

print(round(((1 - P) ** (C - 1) * P), 3))