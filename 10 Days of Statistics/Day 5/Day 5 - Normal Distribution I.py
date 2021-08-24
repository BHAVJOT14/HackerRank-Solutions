
import math

MU = 20
SD = 2

def normal_cdf(X, MU, SD):
    return 1 / 2 * (1 + math.erf((X - MU) / (SD * math.sqrt(2))))

RESULT_1 = normal_cdf(19.5, MU, SD)
RESULT_2 = normal_cdf(22, MU, SD) - normal_cdf(20, MU, SD)

print(round(RESULT_1, 3))
print(round(RESULT_2, 3))
