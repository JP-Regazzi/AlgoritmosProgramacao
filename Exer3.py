vetor1 = eval(input('Digite em formato de lista o valor do vetor 1, este no maximo sendo R4'))
vetor2 = eval(input('Digite em formato de lista o valor do vetor 2, este no maximo sendo R4'))
rn = len(vetor1)
rn2 = len(vetor2)
produto = 0
if rn > 4 or rn2 > 4:
    quit()
for i in range(0, rn):
    produto += vetor1[i]*vetor2[i]
print(produto)
