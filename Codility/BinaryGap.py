def Solution(N):
    N = bin(N)[2:]
    print(N)
    b = 0
    bmax = 0

    for i in N:
        if int(i) == 0:
            b +=1
        elif int(i) == 1:
            bmax = max(b, bmax)
            b = 0
    return bmax

print(Solution(123))