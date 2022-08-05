import json

with open('dados.json') as json_file:
    dados = json.load(json_file)
    menorVal = 99999
    maiorVal = 0
    media = 0
    numDias = 0
    print(dados)
    for x in range (len(dados)):
        valor_da_vez = dados[x]['valor']
        if (valor_da_vez < menorVal):
            menorVal = valor_da_vez
        if (valor_da_vez > maiorVal):
            maiorVal = valor_da_vez
        
        media += valor_da_vez

    media /= len(dados)
    for x in range(len(dados)):
        valor_da_vez = dados[x]['valor']

        if (valor_da_vez > 0 and valor_da_vez > media):
            numDias +=1 
    

    print('Menor valor:' + str(menorVal))
    print('Maior valor:' + str(maiorVal))
    print('Num de dias superior a media:' + str(numDias))
