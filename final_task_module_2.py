
def delitel1(n):
    delitel = []
    if n:
        for k in range(2, n + 1):
            result = n % k
            if result == 0 and k != 2:
               delitel.append(k)
    return delitel

def password1():
    password = []
    for a in range(0, len(delitel1(n))):
        p = delitel1(n)[a]
        for j in range(1, (p // 2) + 1):
            if j == (p - j):
                continue
            elif j < round(p // 2) + 1:
                password.append(j)
                password.append(p - j)
    print('password: ', *password, sep='')
    return password

n = int(input())
if 2 < n < 21:
    password1()
else:
    print('Введите число от 3 до 20')