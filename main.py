import math

n = 3
mu = [0.3, 0.9, 0.4]
cN = 0.0050794523540588525
e = [0.35, 1, 0.6]
r = [3, 1, 1]
N = 8
p = [[0, 0.35, 0],
     [1, 0.05, 1],
     [0, 0.6, 0]]


def point(i, k):
    temp = (e[i] / mu[i]) ** k
    if k < r[i]:
        return temp / math.factorial(k)
    else:
        return temp / (math.factorial(r[i]) * ((r[i]) ** (k - r[i])))


def pSMO(i, j):
    result = 0
    if i == 0:
        for a in range(N + 1 - j):
            result = result + point(0, j) * point(1, a) * point(2, N - j - a)
    if i == 1:
        for a in range(N + 1 - j):
            result = result + point(0, a) * point(1, j) * point(2, N - j - a)
    if i == 2:
        for a in range(N + 1 - j):
            result = result + point(0, a) * point(1, N - j - a) * point(2, j)
    return result * cN


def c_n_test():
    for j in range(n):
        sum = 0
        for i in range(N + 1):
            sum = sum + pSMO(j, i)
        print("Сума PСМО", j + 1, " = ", sum)


c_n_test()
print("")


def L(i):
    result = 0
    for j in range(r[i] + 1, N + 1):
        result = result + (j - r[i]) * pSMO(i, j)
    return result


L = [L(0), L(1), L(2)]
#print("Середня кількість вимог у черзі:" + L + "")
print(L)


def R(i):
    result = 0
    for j in range(r[i]):
        result = result + (r[i] - j) * pSMO(i, j)
    return r[i] - result


R = [R(0), R(1), R(2)]
print("Середня кількість зайнятих пристроїв:" + R + "")


def M(i):
    return L[i] + R[i]


M = [M(0), M(1), M(2)]
print("Середня кількість вимог:" + M + "")


def Lam(i):
    return R[i] * (1 / mu[i])


Lam = [Lam(0), Lam(1), Lam(2)]
print("Інтенсивність вихідного потоку вимог:" + Lam + "")


def T(i):
    return M[i] / Lam[i]


T = [T(0), T(1), T(2)]
print("Середній час перебування вимоги:" + T + "")


def Q(i):
    return L[i] / Lam[i]


Q = [Q(0), Q(1), Q(2)]
print("Середній час очікування в черзі:" + Q)