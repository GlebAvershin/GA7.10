import sys
sys.setrecursionlimit(10000)
def F(n):
    if n == 1:
        return n
    if n >= 3:
        return F(n) + n
print(F(3))

def G(n):
    if n == 1:
        return n
    if n >= 3:
        return G(n + 1) - n
print(G(3))

def H(n):
    if n == 1:
        return n
    if n >= 3:
        return H(n + 1) - n
print(H(3))

k = 0
for i in range(1, 1000):
    if i % 4 == 0:
        k += 1
print(k)