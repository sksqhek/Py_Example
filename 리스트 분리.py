arr = [1, 2, 3, 4, 5]
print(", ".join(str(i) for i in arr)) # Comprehension
print(*arr, sep=', ') # unpacking