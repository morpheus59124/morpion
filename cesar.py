# On récupère les données.
phrase = input("Ecrivez une phrase:")
decalage = int(input("Valeur du décalage?"))  # Conversion direct en int!
 
# On crée un dictionnaire {lettre_de_départ: lettre_encodée}.
dico = {}
for i in range(26):  # Pour chaque nombre de 0 à 25
    i_caesar = (i + decalage) % 26  # Modulo 26, pour toujours avoir un résultat compris entre 0 et 25 inclus (modulo 26 = reste de la division euclidienne par 26).
    # On ajoute à ces nombre la "valeur" de la lettre a, et on les convertit en lettres!
    c_caesar = chr(i_caesar + ord('a'))
    c = chr(i + ord('a'))
    dico[c] = c_caesar
# On a maintenant un dictionnaire qui à chaque lettre fait correspondre sa valeur codée.
result = ""
for c in phrase:  # Pour chaque caractère de phrase...
    result = result + dico[c]
print(result)


dico2 = {}
for i in range(26):  # Pour chaque nombre de 0 à 25
    i_caesar = (i - decalage) % 26  # Modulo 26, pour toujours avoir un résultat compris entre 0 et 25 inclus (modulo 26 = reste de la division euclidienne par 26).
    # On ajoute à ces nombre la "valeur" de la lettre a, et on les convertit en lettres!
    c_caesar = chr(i_caesar + ord('a'))
    c = chr(i + ord('a'))
    dico2[c] = c_caesar
    result2 = ""
    result2 = result
# On a maintenant un dictionnaire qui à chaque lettre fait correspondre sa valeur codée.

print(result2)