#programa que gera a reclist BRAPA e-CV

consoantes = ['b', 'ch', 'd', 'dj', 'f', 'g', 'h', 'j', 'k', 'l', 'lh', 'nh', 'p', 'r', 'sh', 't', 'v']
consoantes_final = ['ch', 'm', 'n', 's', 'w', 'y', 'z']
regional = ['x']
vogais = ['a', 'e', 'i', 'o', 'u', 'eh', 'oh', 'an', 'en', 'in', 'on', 'un', 'ax']

with open('reclist_python.txt', 'w') as arquivo:
    for valor_vog in vogais:
        arquivo.write("_" + str(valor_vog) + "_-_" + str(valor_vog) + '\n')
    arquivo.write('\n')

    for valor_cons in consoantes:
        if valor_cons != 'r':
            for valor_vog in vogais:
                arquivo.write("_" + str(valor_cons) + "_" + str(valor_vog) + "_" + "e" + "_" + str(valor_cons) + "_" +str(valor_vog) + '\n')
            arquivo.write('\n')
    
        else:
            for valor_vog in vogais:
                arquivo.write("_" + str(valor_cons) + "_" + str(valor_vog) + "_" + "e" + "_" + str(valor_cons) + "_" +str(valor_vog) + "_x" + '\n')
            arquivo.write('\n')

    for valor_cons in consoantes_final:
        for valor_vog in vogais:
            arquivo.write("_" + str(valor_cons) + "_" + str(valor_vog) + "_" + "e" + "_" + str(valor_cons) + "_" +str(valor_vog) + "_" + str(valor_cons) + '\n')
        arquivo.write('\n')