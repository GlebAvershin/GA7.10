def R(n):
    n2 = bin(n)[2:]
    if n % 3 == 0:
        n2 += n2[-3:]
    else:
        n2 += bin((n % 3)*3)[2:]
    return int(n2, 2)
for n in range(1, 1000):
    if R(n) > 151:
        print(R(n))
        break