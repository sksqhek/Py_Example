import copy


def matrix_print(arr,  size):
    for r in range(size):
        for c in range(size):
            print("%003d" % arr[r][c], " ", end="")
        print()

def rotate(arr, size):
    arr2 = copy.deepcopy(arr)

    for r in range(size):
        for c in range(size):
            arr2[c][size - 1 - r] = arr[r][c]
    return arr2


N = int(input())

arr = []
for i in range(N):
    arr.append([])
    for j in range(N):
        arr[i].append(0)

i = 0
j = -1
cnt = 1
u = N
o = 1

while True:
    for k in range(u):
        j += o
        arr[i][j] = cnt
        cnt += 1

    if u < 0:
        break

    u -= 1

    for k in range(u):
        i += o
        arr[i][j] = cnt
        cnt += 1
    o *= -1

print("#0")
matrix_print(arr, N)

print("#90")
arr = rotate(arr,N)
matrix_print(arr, N)

print("#180")
arr = rotate(arr,N)
matrix_print(arr, N)

print("#270")
arr = rotate(arr,N)
matrix_print(arr, N)

print("#360")
arr = rotate(arr,N)
matrix_print(arr, N)