
st_num, sb_num = map(int, input().split())

scores = []

for _ in range(sb_num):
    scores.append(map(float, input().split()))
        
for el in zip(*scores):
    print(sum(el) / sb_num)