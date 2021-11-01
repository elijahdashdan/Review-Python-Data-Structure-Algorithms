def Solution(A, K):
    N = len(A)
    B = A.copy()

    for i in range(0, N):
        B[(i+K)%N] = A[i]
    return B

print(Solution([1,5,6,7,2],4))