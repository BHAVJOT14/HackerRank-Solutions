import math

A = int(input())
B = int(input())
C = int(input())
Flag = math.sqrt(B) * int(input())

print(round(0.5 * (1 + math.erf((A - (B * C)) / (Flag * math.sqrt(2)))), 4))