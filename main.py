'''
Fait par Splyder, le 17/09/2021
'''
def decimal_to_binary(nb,method=1):

    #la première methode utilise la foction bin() qui est native en python
    if method==1:
        #je supprime les deux premiers caractères, python les mets pour signifier que c'est du binaire
        return bin(nb)[2:]

    #la deuxieme methode utilise l'algorithme d'euclide pour passer de la base 10 à la base 2
    elif method==2:
        liste_de_bits=[]
        while nb!=0:
            #on integre le reste de la division euclidienne a une liste
            liste_de_bits.append(nb%2)
            #quotient de la division euclidienne
            nb=nb//2
        #on inverse l'ordre des elements de la liste
        liste_de_bits=liste_de_bits[::-1]
        #on transforme le contenue de la liste en une seule variable
        bits=" ".join(map(str,liste_de_bits))
        return bits
