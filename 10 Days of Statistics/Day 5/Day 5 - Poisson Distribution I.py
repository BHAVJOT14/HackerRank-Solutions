
from math import factorial, exp

meanVar = float(input())
N = int(input())

Result = ((meanVar ** N) * exp(-meanVar)) / factorial(N)

print("%.3f" % Result)