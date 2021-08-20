if __name__ == '__main__':
    N = int(input())
    arr = []

    while N != 0:
        A = input().split()

        if len(A) == 3:
            B = int(A[1])
            C = int(A[2])
        elif len(A) == 2:
            B = int(A[1])

        if A[0] == "insert":
            arr.insert(B, C)
        elif A[0] == "print":
            print(arr)
        elif A[0] == "remove":
            arr.remove(B)
        elif A[0] == "append":
            arr.append(B)
        elif A[0] == "sort":
            arr.sort()
        elif A[0] == "pop":
            arr.pop()
        elif A[0] == "reverse":
            arr.reverse()
        N -= 1