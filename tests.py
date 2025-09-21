# tests.py
import exercice1

# Exemple de matrice 9x9
matrice = [[i*9 + j + 1 for j in range(9)] for i in range(9)]

print("Affichage par ligne :")
exercice1.afficher_par_ligne(matrice)

print("\nAffichage par colonne :")
exercice1.afficher_par_colonne(matrice)

print("\nAffichage par bloc :")
exercice1.afficher_par_bloc(matrice)
