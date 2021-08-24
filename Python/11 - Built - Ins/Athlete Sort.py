if __name__ == '__main__':
    n, m = input().split()
    dct = []

    for i in range(int(n)):
        elements = input().split()

        if len(elements) == int(m):
            dct.append([int(x) for x in elements])
        else:
            break

    k = int(input())
    
    if k < int(m):
        for x in sorted(dct, key = lambda lst: lst[k]):
            print(" ".join(str(y) for y in x))