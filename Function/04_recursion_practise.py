def sum(n):
    if(n == 1):
        return 1

    return sum(n - 1) + n

S = sum(8)
print(S)