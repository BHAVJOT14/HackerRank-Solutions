
avg__X, avg__Y = [float(num) for num in input().split(" ")]

# Cost
cost__X = 160 + 40*(avg__X + avg__X**2)
cost__Y = 128 + 40*(avg__Y + avg__Y**2)

print(round(cost__X, 3))
print(round(cost__Y, 3))