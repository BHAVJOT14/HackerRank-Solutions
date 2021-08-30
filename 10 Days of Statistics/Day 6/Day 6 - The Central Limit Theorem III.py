import math

SAMPLE = 100
M = 500
SD = 80
Z = 1.96
RNG = 0.95

print(round(-1.96 * (SD/math.sqrt(SAMPLE)) + M, 2))
print(round(1.96 * (SD/math.sqrt(SAMPLE)) + M, 2))