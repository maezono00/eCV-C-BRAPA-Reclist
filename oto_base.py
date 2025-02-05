#programa que gera a oto base da reclist BRAPA e-CV

consoantes = ['b', 'ch', 'd', 'dj', 'f', 'g', 'h', 'j', 'k', 'l', 'lh', 'nh', 'p', 'r', 'sh', 't', 'v']
consoantes_final = ['ch', 'm', 'n', 's', 'w', 'y', 'z']
regional = ['x']
vogais = ['a', 'e', 'i', 'o', 'u', 'eh', 'oh', 'an', 'en', 'in', 'on', 'un', 'ax']

with open('teste_oto.txt', 'w') as arquivo:
    for valor_vog in vogais:
        arquivo.write("_" + str(valor_vog) + "_-_" + str(valor_vog) + ".wav=" + "- " + str(valor_vog) + ",,,,," + '\n')
    
    for valor_vog in vogais:
        arquivo.write("_" + str(valor_vog) + "_-_" + str(valor_vog) + ".wav=" + str(valor_vog) + ",,,,," + '\n')

    for valor_vog in vogais:
        arquivo.write("_" + str(valor_vog) + "_-_" + str(valor_vog) + ".wav=" + str(valor_vog) + " -,,,,," + '\n')

    for valor_cons in consoantes:
        if valor_cons != 'r':
            for valor_vog in vogais:
                arquivo.write("_" + str(valor_cons) + "_" + str(valor_vog) + "_" + "e" + "_" + str(valor_cons) + "_" +str(valor_vog) + ".wav" + "=" + "-" + (str(valor_cons)) + " " + str(valor_vog) + ",,,,," + '\n')
        
            for valor_vog in vogais:
                arquivo.write("_" + str(valor_cons) + "_" + str(valor_vog) + "_" + "e" + "_" + str(valor_cons) + "_" +str(valor_vog) + ".wav" + "=" + (str(valor_cons)) + " " + str(valor_vog) + ",,,,," + '\n')
        else:
            for valor_vog in vogais:
                arquivo.write("_" + str(valor_cons) + "_" + str(valor_vog) + "_" + "e" + "_" + str(valor_cons) + "_" +str(valor_vog) + "_" + "x" + ".wav" + "=" + "-" + (str(valor_cons)) + " " + str(valor_vog) + ",,,,," + '\n')
        
            for valor_vog in vogais:
                arquivo.write("_" + str(valor_cons) + "_" + str(valor_vog) + "_" + "e" + "_" + str(valor_cons) + "_" +str(valor_vog) + "_" + "x" + ".wav" + "=" + (str(valor_cons)) + " " + str(valor_vog) + ",,,,," + '\n')

            for valor_vog in vogais:
                arquivo.write("_" + str(valor_cons) + "_" + str(valor_vog) + "_" + "e" + "_" + str(valor_cons) + "_" +str(valor_vog) + "_" + "x" + ".wav" + "=" + str(valor_vog) + " " + "x" + ",,,,," + '\n')

    for valor_cons in consoantes_final:
        for valor_vog in vogais:
            arquivo.write("_" + str(valor_cons) + "_" + str(valor_vog) + "_" + "e" + "_" + str(valor_cons) + "_" +str(valor_vog) + "_" + str(valor_cons) + ".wav" + "=" + "-" + (str(valor_cons)) + " " + str(valor_vog) + ",,,,," + '\n')
        
        for valor_vog in vogais:
            arquivo.write("_" + str(valor_cons) + "_" + str(valor_vog) + "_" + "e" + "_" + str(valor_cons) + "_" +str(valor_vog) + "_" + str(valor_cons) + ".wav" + "=" + (str(valor_cons)) + " " + str(valor_vog) + ",,,,," + '\n')
        
        for valor_vog in vogais:
            arquivo.write("_" + str(valor_cons) + "_" + str(valor_vog) + "_" + "e" + "_" + str(valor_cons) + "_" +str(valor_vog) + "_" + str(valor_cons) + ".wav" + "=" + str(valor_vog) + " " + (str(valor_cons)) + ",,,,," + '\n')