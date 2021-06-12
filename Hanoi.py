# Tower Of Hanoi with Recursion

N = int(input("Enter no. Disk : "))

M = [[0 for i in range(3)] for j in range(N)]
for i in range(N):
    M[i][0] = i+1

Z = 0


def Pegs(M, S, D):  # Repersentation
    global Z
    Z += 1
    S = ord(S)-65
    D = ord(D)-65
    t = 0
    while t < N and M[t][S] == 0:
        t += 1
    if t == N:
        t = N-1
    T = M[t][S]
    M[t][S] = 0
    t = 0
    while t+1 < N and M[t+1][D] == 0:
        t += 1
    M[t][D] = T

    for i in M:
        for j in i:
            if j == 0:
                print("-", end=" ")
            else:
                print(j, end=" ")
        print("")
    print("A B C")


def towerofhanoi(M, n, source, aux, dest):  # Main Function
    if n <= 0:
        return
    towerofhanoi(M, n-1, source, dest, aux)
    print("")
    print("Step : ", source, " -> ", dest)
    Pegs(M, source, dest)
    towerofhanoi(M, n-1, aux, source, dest)


towerofhanoi(M, N, 'A', 'B', 'C')
print("\nTotal No of Steps = ", Z)
print("Min no of Steps 2^n-1 = ", 2**N-1)
