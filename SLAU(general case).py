def rang_find(matrix):
    rang = 0
    count_1 = 0
    count_0 = 0
    basis_vars = []
    for j in range(n):
        for i in range(m):
            if matrix[i][j] == 1:
                count_1 += 1
            if matrix[i][j] == 0:
                count_0 += 1
        if count_0 == m - 1 and count_1 == 1:
            rang += 1
            basis_vars.append(j)
        count_1 = 0
        count_0 = 0
    return rang, basis_vars


def zeros_algo(mas, div):
    unnes = 0
    for i in range(m):
        if (i < div[0]) | (i > div[0]):
            tmp_el = mas[i][div[1]]
            for j in range(n + 1):
                mas[i][j] = mas[i][j] - mas[div[0]][j] * tmp_el
                if A[i][j] == int(A[i][j]):
                    unnes += 1
                else:
                    A[i][j] = round(A[i][j], 5)
    return mas


def gauss_le_classique(A):
    tmp = []
    flag = 0
    unnes = 0
    for i in range(m):
        for j in range(n + 1):
            if A[i][j] != 0 and flag == 0 and j != n:
                tmp.append(i)
                tmp.append(j)
                el = A[i][j]
                flag = 1
            if flag == 1 :
                A[i][j] = A[i][j] / el
                if A[i][j] == int(A[i][j]):
                    unnes += 1
                else:
                    A[i][j] = round(A[i][j], 5)
        if flag == 1:
            A = zeros_algo(A, tmp)
        flag = 0
        tmp = []
    return A


if __name__ == "__main__":
    print("give the size of the SLAU\n")
    print("Enter the number of the lines\n>>")

    m = int(input())

    print("Enter the number of the columns\n>>" )

    n = int(input())
    A = [[int(i) for i in input().split()] for j in range(m)]

    print("Given system: ")

    for line in range(m):
        print(*A[line])

    print("Enter the column of free coefficients\n>>")

    b = [int(el) for el in input().split()]

    for i in range(m):
        A[i].append(b[i])

    A = gauss_le_classique(A)

    for line in range(m):
        print(*A[line])

    rank, basis = rang_find(A)
    F = [[0 for j in range(n - rank)] for i in range(n)]
    for i in range(m):
        for j in range(n):
            if j in basis:
                continue
            if A[i][j] != 0:
                F[i][j - rank] = -A[i][j]
            else:
                F[i][j - rank] = A[i][j]

    for u in range(n - 1):
        if not 0 in F[u]:
            continue
        else:
            F[u], F[u + 1] = F[u + 1], F[u]

    E = [[0 for j in range(n - rank)] for i in range(n - rank)]
    for i in range(n - rank):
        for j in range(n - rank):
            if i == j:
                E[i][j] = 1
            else:
                continue

    while len(F) != rank:
        F.pop()
    for i in range(n - rank):
        F.append(E[i])
    ez_solve = [0 for i in range(n)]
    for i in range(n):
        if i in basis:
            if A[i][-1] == 0:
                continue
            else:
                ez_solve[i] = A[i][-1]

    print('===============================ez=============================')
    print("FUNDAMENTAL SHIT","|", "UNIQUE SOLVE")
    for i in range(n):
        print('(',*F[i],')','|', '(',ez_solve[i],')')
