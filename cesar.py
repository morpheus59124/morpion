while True:
    # On récupère les données.
    demande= int(input("voulez vous crypter(1) ou decrypter(2) : "))
    result=""
    if demande==1:
            phrase = input("Ecrivez une phrase:")
            decalage = int(input("Valeur du décalage?"))  # Conversion direct en int!
            # On crée un dictionnaire {lettre_de_départ: lettre_encodée}.
            dico = {}
            for i in range(255):  # Pour chaque nombre de 0 à 25
                    i_caesar = (i + decalage) % 255  # Modulo 26, pour toujours avoir un résultat compris entre 0 et 25 inclus (modulo 26 = reste de la division euclidienne par 26).
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
            for i in range(255):  # Pour chaque nombre de 0 à 25
                    i_caesar = (i - decalage) % 255 # Modulo 26, pour toujours avoir un résultat compris entre 0 et 25 inclus (modulo 26 = reste de la division euclidienne par 26).
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
    else:
        pass

