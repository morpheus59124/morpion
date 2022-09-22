# definition des joueurs
joueur1 = str(input("entrez le prenom du joueur 1 : "))
joueur2 = str(input("entrez le prenom du joueur 2 : "))

# definition de la grille
grille= [
    [" "," "," "], 
    [" "," "," "],
    [" "," "," "]
]
def affichage ():
    for i in range(3):
        print(grille[i])
affichage()

# definition des touches
touch= {
    1:"A1",
    2:"A2",
    3:"A3",
    4:"B1",
    5:"B2",
    6:"B3",
    7:"C1",
    8:"C2",
    9:"C3"
}
