N, A, B, idx, S = int(input()), [], [], [], 0
A, B = list(map(int, input().split())), list(map(int, input().split()))
C, D = A.copy(), B.copy()
C.sort(), D.sort(reverse=True)
for i in range(N):
    for j in range(N):
        if D[i] == B[j]:
            if j not in idx:
                A[j] = C[i]
                idx.append(j)
                break
for k in range(N):
    S += A[k] * B[k]
print(S)