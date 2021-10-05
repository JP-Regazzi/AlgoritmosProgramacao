aberto =open('numerox.txt', encoding='utf-8')
lista = ['PSOL', 'PT', 'DEM', 'PSD', 'REPUBLICANOS', 'CIDADANIA', 'PL', 'AVANTE', 'PP', 'NOVO', 'PSL', 'PSDB', 'PCO', 'PCdoB', '']
lista_votos = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for linha in aberto:
    l = linha.split()
    print(l)
    for p in l:
        if 'INAPTO' in linha:
            continue
        if p in lista:
            partido = p
            posicao = lista.index(p)
        elif '%' in p or 'º' in p:
            continue
        elif ('1' or '2' or '3' or '4' or '5' or '6' or '7' or '9' or '0') in p:
            lista_votos[posicao] += int(p)
        else:
            continue

print(lista[lista_votos.index(max(lista_votos))])
print(lista[lista_votos.index(min(lista_votos))])
lista_votos.sort(reverse=True)
lista_nova = []
for numero in lista_votos:
    index = lista_votos.index(numero)
    lista_nova += [lista[index]]

for party in lista_nova:
    print(f'{party}', end=' ')

