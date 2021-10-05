# -*- coding: utf-8 -*-
N = float((input()))


def numero_minimo_moedas(N):
    n100 = 0
    for x in range(int(N//100)):
        n100 += 1
    N -= (100*n100)
    n50 = 0
    for x in range(int(N//50)):
        n50 += 1
    N -= (50*n50)
    n20 = 0
    for x in range(int(N//20)):
        n20 += 1
    N -= (20*n20)
    n10 = 0
    for x in range(int(N//10)):
        n10 += 1
    N -= (10*n10)
    n5 = 0
    for x in range(int(N//5)):
        n5 += 1
    N -= (5*n5)
    n2 = 0
    for x in range(int(N//2)):
        n2 += 1
    N -= (2*n2)
    m1 = 0
    for x in range(int(N//1)):
        m1 += 1
    N -= m1
    m0_5 = 0
    for x in range(int(N*100//50)):
        m0_5 += 1
    N -= (0.5*m0_5)
    m0_25 = 0
    for x in range(int(N*100//25)):
        m0_25 += 1
    N -= (0.25*m0_25)
    m0_1 = 0
    for x in range(int(N*100//10)):
        m0_1 += 1
    N -= (0.1*m0_1)
    m0_05 = 0
    for x in range(int(N*100//5)):
        m0_05 += 1
    N -= (0.05*m0_05)
    m0_01 = 0
    for x in range(int(N*100//1)):
        m0_01 += 1
    N -= (0.01*m0_01)
    return f'''NOTAS:
{n100} nota(s) de R$ 100.00
{n50} nota(s) de R$ 50.00
{n20} nota(s) de R$ 20.00
{n10} nota(s) de R$ 10.00
{n5} nota(s) de R$ 5.00
{n2} nota(s) de R$ 2.00
MOEDAS:
{m1} moeda(s) de R$ 1.00
{m0_5} moeda(s) de R$ 0.50
{m0_25} moeda(s) de R$ 0.25
{m0_1} moeda(s) de R$ 0.10
{m0_05} moeda(s) de R$ 0.05
{m0_01} moeda(s) de R$ 0.01
'''


print(numero_minimo_moedas(N))

