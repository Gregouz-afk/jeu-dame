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

    dx = x2 - x1
    dy = abs(y2 - y1)

    if joueur == "x" and dx == 1 and dy == 1:
        return True
    if joueur == "o" and dx == -1 and dy == 1:
        return True

    if abs(dx) == 2 and dy == 2:
        milieu_x = (x1 + x2) // 2
        milieu_y = (y1 + y2) // 2
        ennemi = "o" if joueur == "x" else "x"
        if plateau[milieu_x][milieu_y] == ennemi:
            return True
    return False

def jouer_coup(plateau, x1, y1, x2, y2):
    joueur = plateau[x1][y1]
    plateau[x1][y1] = " "
    plateau[x2][y2] = joueur
    if abs(x2 - x1) == 2:  # Si c’était une prise
        milieu_x = (x1 + x2) // 2
        milieu_y = (y1 + y2) // 2
        plateau[milieu_x][milieu_y] = " "
