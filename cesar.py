def freq(texte):
        d = {}
        car = []
        for c in texte:
                if c.lower() not in d:
                        if c not in car:
                                d[c.lower()] = 1
                else:
                        d[c.lower()] += 1
                
        return d

def dechiffrer(resultat,index2):
        for lettre in resultat:
                resultat+=chr(ord(lettre)-index2)
        return resultat

while True:
    # On récupère les données.
    demande= int(input("voulez vous Chiffrer(1) ou Dechiffrer(2) ou Decrypter(3): "))
    result=""
    if demande==1:
            phrase = input("Ecrivez une phrase:")
            decalage = int(input("Valeur du décalage?"))  # Conversion direct en int!
            # On crée un dictionnaire {lettre_de_départ: lettre_encodée}.
            dico = {}
            for i in range(255):  # Pour chaque nombre de 0 à 255
                    i_caesar = (i + decalage) % 255  # Modulo 255, pour toujours avoir un résultat compris entre 0 et 25 inclus (modulo 26 = reste de la division euclidienne par 26).
                    # On ajoute à ces nombre la "valeur" de la lettre a, et on les convertit en lettres!
                    c_caesar = chr(i_caesar + 0)
                    c = chr(i + 0)
                    dico[c] = c_caesar
            # On a maintenant un dictionnaire qui à chaque lettre fait correspondre sa valeur codée.
            for c in phrase:  # Pour chaque caractère de phrase...
                resultat = result + dico[c]
                result=resultat
            print(resultat)
    elif demande==2:
            phrase = resultat
            decalage = int(input("Valeur du décalage?"))  # Conversion direct en int!
            # On crée un dictionnaire {lettre_de_départ: lettre_encodée}.
            dico = {}
            for i in range(255):  # Pour chaque nombre de 0 à 255
                    i_caesar = (i - decalage) % 255 # Modulo 255, pour toujours avoir un résultat compris entre 0 et 25 inclus (modulo 26 = reste de la division euclidienne par 26).
                    # On ajoute à ces nombre la "valeur" de la lettre a, et on les convertit en lettres!
                    c_caesar = chr(i_caesar + 0)
                    c = chr(i + 0)
                    dico[c] = c_caesar
            # On a maintenant un dictionnaire qui à chaque lettre fait correspondre sa valeur codée.
            for c in phrase:  # Pour chaque caractère de phrase...
                resultat = result + dico[c]
                result=resultat
            print(resultat)
            print("déchiffrage reussi :)")
            break        
    elif demande==3:
        texte = result
        fichier = open("texte.txt", "w")        #Créer le fichier s'il n'existe pas
        fichier.write(resultat)        #Écrit la valeur de la variable a dans le fichier
        fichier.close()
        with open('texte.txt' , encoding='utf8') as poeme:
                for ligne in poeme:
                        texte += ligne.replace('\n','')
                
        L = sorted(freq(texte).items(), key = lambda colonne: colonne[1] , reverse = True)
        for i in L:
                print('{} : {}'.format(i[0],i[1]))
        print(L[0][0])
        index=ord(L[0][0])     
        index2=index-32
        print(index2)
        decalage = index2

        dechiffrer()
        print(resultat)        
        print("déchiffrage reussi :)")
        break        
                
        continue
        fichier = remove("texte.txt")  



    else:
        print("Choississez 1,2 ou 3")
