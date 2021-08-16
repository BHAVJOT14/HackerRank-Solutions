n = int(input())
numb = list(map(int, input().split()))

    #==============================
    #          For Mean
    #============================== 


sum = 0

for i in numb:
    sum = sum + i
print(float(sum / n))

    #==============================
    #          For Median
    #============================== 

numb = sorted(numb)

if n % 2 == 0:
    A = numb[n//2]
    B = numb[n//2 - 1]
    print((A+B)/2)
else:
    print(numb[n//2])

    #==============================
    #          For Mode
    #============================== 

MAX_1 = 0
numb = sorted(numb)

for i in numb:
    COUNTER = 0
    INDEX = numb.index(i)

    for j in range(INDEX, len(numb)):
        if i == numb[j]:
            COUNTER = COUNTER + 1
        if COUNTER > MAX_1:
            MAX_1 = COUNTER
            if MAX_1 == 1:
                MODE = numb[0]
            else:
                MODE = i

print(MODE)