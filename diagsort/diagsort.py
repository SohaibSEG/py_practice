def sort(a):

    for i in range(len(a)):
        for j in range(len(a)-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a


def get_diags(a):
    n, m = len(a), len(a[1])
    diag_mat = []  # array to hold diagonals

    # get diagonals and sort them
    for i in range(m-1, 0, -1):
        r, c = i, n-1
        tmp = []
        while r < m and c > -1:
            tmp.append(a[c][r])
            r += 1
            c -= 1
        diag_mat.append(sort(tmp))

    for i in range(n-1, -1, -1):
        r, c = i, 0
        tmp = []
        while r > -1 and c < n:
            tmp.append(a[r][c])
            r -= 1
            c += 1
        diag_mat.append(sort(tmp))

    result = []
    # building the array back again size n*m
    for i in range(n):
        tmp = []
        j = len(diag_mat) - 1
        k = m-1
        while k >= 0:
            if len(diag_mat[j]) > 0:
                tmp.append(diag_mat[j].pop())
                k -= 1
                j -= 1
            else:
                j -= 1
        print(tmp)
        result.append(tmp)

    return result


if __name__ == "__main__":
    print(get_diags([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
