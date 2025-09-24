def creer_plateau():
    plateau = [[" " for _ in range(8)] for _ in range(8)]
    for i in range(3):  # Pions joueur 1
        for j in range(8):
            if (i + j) % 2 == 1:
                plateau[i][j] = "x"
    for i in range(5, 8):  # Pions joueur 2
        for j in range(8):
            if (i + j) % 2 == 1:
                plateau[i][j] = "o"
    return plateau

def afficher_plateau(plateau):
    print("  " + " ".join(str(i) for i in range(8)))
    for i in range(8):
        print(i, " ".join(plateau[i]))

def deplacement_valide(plateau, x1, y1, x2, y2, joueur):
    if not (0 <= x2 < 8 and 0 <= y2 < 8):
        return False
    piece = plateau[x1][y1]
    if piece != joueur:
        return False
    if plateau[x2][y2] != " ":
        return False
