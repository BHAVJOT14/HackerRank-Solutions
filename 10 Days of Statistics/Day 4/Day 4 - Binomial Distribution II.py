
import math

P = 0.12
firstAnwser = 0

for i in range(0, 3):
    firstAnwser += math.factorial(10) / math.factorial(i) / math.factorial(10 - i) * P ** i * (1 - P) ** (10 - i)
    if i == 1:
        secondAnswer = 1 - firstAnwser

print(round(firstAnwser, 3))
print(round(secondAnswer, 3))