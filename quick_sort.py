def partition(S, low, high):
    pivotitiem = S[low]
    j = high
    i = low + 1
    while j >= i:
        while (S[i] > pivotitiem):
            i += 1
        while (S[j] < pivotitiem):
            j -= 1
        if (j > i):
            S[i], S[j] = S[j], S[i]
    pivotpoint = j

    S[low], S[pivotpoint] = S[pivotpoint], S[low]
    return pivotpoint


def quicksort(S, low, high):
    if (high > low):
        pivotpoint = partition(S, low, high)
        quicksort(S, low, pivotpoint - 1)
        quicksort(S, pivotpoint + 1, high)


a = [26, 5, 37, 1, 61, 11, 59, 15, 48, 19]
print("Before : {}".format(a[0:]))
print("\n")
quicksort(a, 0, len(a) - 1)
print("After :{}".format(a[0:])) 