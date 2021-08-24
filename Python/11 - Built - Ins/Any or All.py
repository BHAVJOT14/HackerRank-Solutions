

num_cnt = int(input().strip())
arr = list(input().strip().split())
print(all([all([int(x) > 0 for x in arr]), any([x == x[::-1] for x in arr])]))