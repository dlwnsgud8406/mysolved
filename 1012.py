T = input()
T = int(T)
pair_list = []
for i in range(0, T):
    M, N, K = input().split()
    M = int(M)
    N = int(N) 
    K = int(K)
    for j in range(0, K):
        X, Y = input().split()
        pair_list.append((int(X), int(Y)))
    print(pair_list)