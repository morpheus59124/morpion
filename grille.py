# definition de la grille
grille= [
    [" "," "," "], 
    [" "," "," "],
    [" "," "," "]
]

# fonctions
def affichage (grille):
    for i in range(3):
        print(grille[i])
affichage(grille)

# coup gagnant
def est_gagnant(grille):
    grille[0]
    for ligne in grille :
        if ligne[0]==ligne[1]==ligne[2] and ligne[0]!=" ":
            return True
    for i in range(3):
        if grille[0][i]==grille[1][i]==grille[2][i] and grille[0][i]!=" ":
            return True



# definitions des tours
def tour(grille, joueur):
    print("C'est le tour du joueur "+str(joueur))
    ligne=input("Entrez le numero de la ligne : ")
    colonne=input("Entrez le numero de la colonne : ")
    print("Vous avez joué la case ("+ligne+","+colonne+")")
    while grille[int(ligne)][int(colonne)]!= " ":
        affichage(grille)
        print("Cette case est deja jouée ! Saisissez une autre case svp !")
        ligne=input("Entrez le numero de la ligne : ")
        colonne=input("Entrez le numero de la colonne : ")
        print("Vous avez joué la case ("+ligne+","+colonne+")")
        return
    if joueur==1 :
        grille[int(ligne)][int(colonne)]="X"
    if joueur==2 :
        grille[int(ligne)][int(colonne)]="O"
    affichage(grille)

# match nul
def est_match_nul(grille):
    for i in range(3):
        if grille[i]==" ":
            return print("t es nul")
    return 

#tour gagnant ou termine
joueur=1
print("Le joueur 1 possède les X. Le joueur 2 possède les O")
gagne=0
while gagne==0:
    tour(grille,joueur)
    if est_gagnant(grille):
        print("Le joueur "+str(joueur)+" remporte la partie")
        gagne=1
    else:
        if est_match_nul(grille):
            print("Plus de place ! Match nul !")
            gagne=1
    if joueur==1:
        joueur=2
    else:
        joueur=1

