import random

# Valeurs des cartes
valeurs = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
    '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11
}

# Crée et mélange un paquet de cartes
def creer_paquet():
    couleurs = ['♠', '♥', '♦', '♣']
    cartes = []
    for c in couleurs:
        for v in valeurs.keys():
            cartes.append(f"{v}{c}")
    random.shuffle(cartes)
    return cartes

# Calcule la valeur d'une main
def valeur_main(main):
    total = 0
    nb_as = 0
    for carte in main:
        valeur = carte[:-1]
        total += valeurs[valeur]
        if valeur == 'A':
            nb_as += 1
    # Si on dépasse 21 et qu'on a des As, on les compte comme 1
    while total > 21 and nb_as > 0:
        total -= 10
        nb_as -= 1
    return total

# Affiche une main
def afficher_main(nom, main, cacher=False):
    if cacher:
        print(f"{nom} : [??] {' '.join(main[1:])}")
    else:
        print(f"{nom} : {' '.join(main)} (valeur = {valeur_main(main)})")

def blackjack():
    argent = 100
    print("=== Bienvenue au Blackjack ===")
    print("Vous commencez avec", argent, "€")

    while argent > 0:
        print("\nSolde :", argent, "€")
        try:
            mise = int(input("Combien voulez-vous miser ? "))
            if mise <= 0 or mise > argent:
                print("Mise invalide.")
                continue
        except ValueError:
            print("Veuillez entrer un nombre.")
            continue

        paquet = creer_paquet()
        joueur = [paquet.pop(), paquet.pop()]
        croupier = [paquet.pop(), paquet.pop()]

        afficher_main("Croupier", croupier, cacher=True)
        afficher_main("Joueur", joueur)

        double_possible = True

        # Tour du joueur
        while valeur_main(joueur) < 21:
            print("\n(o) Tirer | (n) Rester", end="")
            if double_possible and argent >= 2 * mise:
                print(" | (d) Double Down", end="")
            print()
            choix = input("Votre choix : ").lower()

            if choix == 'o':
                joueur.append(paquet.pop())
                afficher_main("Joueur", joueur)
                double_possible = False
            elif choix == 'd' and double_possible and argent >= 2 * mise:
                mise *= 2
                print("Mise doublée :", mise, "€")
                joueur.append(paquet.pop())
                afficher_main("Joueur", joueur)
                break
            else:
                break

        val_joueur = valeur_main(joueur)

        # Si le joueur dépasse 21
        if val_joueur > 21:
            print("Vous dépassez 21, vous perdez votre mise.")
            argent -= mise
        else:
            # Tour du croupier
            print("\nTour du croupier :")
            afficher_main("Croupier", croupier)
            while valeur_main(croupier) < 17:
                croupier.append(paquet.pop())
                afficher_main("Croupier", croupier)

            val_croupier = valeur_main(croupier)
            print("\nRésultat final :")
            print("Joueur :", val_joueur, "| Croupier :", val_croupier)

            if val_croupier > 21 or val_joueur > val_croupier:
                print("Vous gagnez !")
                argent += mise
            elif val_joueur == val_croupier:
                print("Égalité, mise rendue.")
            else:
                print("Le croupier gagne.")
                argent -= mise

        if argent <= 0:
            print("\nVous n'avez plus d'argent. Fin du jeu.")
            break
        rejouer = input("\nRejouer ? (o/n) : ").lower()
        if rejouer != 'o':
            break

    print("\nVous repartez avec", argent, "€.")
    print("Merci d’avoir joué au Blackjack.")

if __name__ == "__main__":
    blackjack()
