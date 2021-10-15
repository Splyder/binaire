'''
Fait par Splyder, le 17/09/2021
'''
def decimal_to_binary(nb:int,method=1)->str:
    
    #la premiere methode utilise la foction bin() qui est native en python, 
    #c'est la façon la plus simple et rapide
    if method==1:
        #je supprime les deux premiers caractères, 
        #python les mets pour signifier que c'est du binaire
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
        
def binary_to_decimal(n:str,method=1)->int:
    
    #la premiere methode utilise la fonction int qui est native en python, 
    #elle est souvent utiliser pour changer le type d'une valeur, 
    #mais avec un deuxieme argument, 
    #elle nous permet entre autre de passer de la bas e 2 a la base 10
    if method==1:
        nombre=int(n,2)
        
    #la deuxieme methode utilise une boucle for pour multiplier chaque element de la liste par une puissance de 2    
    elif method==2:
        nombre=0
        for x in range(len(n)):
            if n[x]=="1":
                nombre=nombre+(2**x) 
    return nombre
