
import math

TICKETS = 250
STUDENTS = 100
MEAN = 2.4
SD = 2

MU = STUDENTS * MEAN
S = math.sqrt(100)*SD

def normal_distribution(x, mu, sd):
    
    return 1/2*(1+math.erf((x-mu)/(sd*math.sqrt(2))))

print(round(normal_distribution(x=TICKETS, mu=MU, sd=S), 4))