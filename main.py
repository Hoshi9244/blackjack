import random

# Valeurs des cartes
valeurs = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
    '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11
}

def creer_paquet():
    """Crée un paquet mélangé de 52 cartes."""
    cartes = []
    for couleur in ['♠', '♥', '♦', '♣']:
        for valeur in valeurs.keys():
            cartes.append(f"{valeur}{couleur}")
    random.shuffle(cartes)
    return cartes

def valeur_main(main):
    """Calcule la valeur totale d'une main, en gérant les As."""
    total = 0
    as_count = 0
    for carte in main:
        valeur = carte[:-1]
        total += valeurs[valeur]
        if valeur == 'A':
            as_count += 1
    while total > 21 and as_count:
        total -= 10
        as_count -= 1
    return total

def afficher_main(nom, main, cacher_premiere=False):
    """Affiche la main du joueur ou du croupier."""
    if cacher_premiere:
        print(f"{nom} : [??] {' '.join(main[1:])}")
    else:
        print(f"{nom} : {' '.join(main)} (valeur = {valeur_main(main)})")

def blackjack():
    """Jeu principal."""
    argent = 100
    print("=== Bienvenue au Blackjack ===")
    print(f"Vous commencez avec {argent} €")

    while argent > 0:
        print("\n----------------------------")
        print(f"Votre solde actuel : {argent} €")

        # Mise du joueur
        try:
            mise = int(input("Combien voulez-vous miser ? "))
            if mise <= 0 or mise > argent:
                print("Mise invalide.")
                continue
        except ValueError:
            print("Entrez un nombre valide.")
            continue

        paquet = creer_paquet()
        joueur = [paquet.pop(), paquet.pop()]
        croupier = [paquet.pop(), paquet.pop()]

        afficher_main("Croupier", croupier, cacher_premiere=True)
        afficher_main("Joueur", joueur)

        double_possible = True  # Autorisé uniquement au premier tour

        # Tour du joueur
        while valeur_main(joueur) < 21:
            print("\nActions : (o) Tirer | (n) Rester", end="")
            if double_possible and argent >= mise * 2:
                print(" | (d) Double Down", end="")
            print()
            choix = input("Votre choix : ").lower()

            if choix == 'o':
                joueur.append(paquet.pop())
                afficher_main("Joueur", joueur)
                double_possible = False
            elif choix == 'd' and double_possible and argent >= mise * 2:
                mise *= 2
                print(f"Double mise ! Nouvelle mise : {mise} €")
                joueur.append(paquet.pop())
                afficher_main("Joueur", joueur)
                break
            else:
                break

        joueur_valeur = valeur_main(joueur)

        # Résultats joueur
        if joueur_valeur > 21:
            print("Vous avez dépassé 21 ! Vous perdez votre mise.")
            argent -= mise
        else:
            # Tour du croupier
            print("\n--- Tour du croupier ---")
            afficher_main("Croupier", croupier)
            while valeur_main(croupier) < 17:
                croupier.append(paquet.pop())
                afficher_main("Croupier", croupier)

            croupier_valeur = valeur_main(croupier)
            print("\n--- Résultat ---")
            print(f"Joueur : {joueur_valeur} | Croupier : {croupier_valeur}")

            if croupier_valeur > 21 or joueur_valeur > croupier_valeur:
                print("Vous gagnez !")
                argent += mise
            elif joueur_valeur == croupier_valeur:
                print("Égalité ! Votre mise est rendue.")
            else:
                print("Le croupier gagne.")
                argent -= mise

        # Vérifie si le joueur continue
        if argent <= 0:
            print("\nVous êtes ruiné. Fin de la partie.")
            break
        continuer = input("\nVoulez-vous rejouer ? (o/n) : ").lower()
        if continuer != 'o':
            break

    print(f"\nVous repartez avec {argent} €.")
    print("Merci d’avoir joué au Blackjack.")

if __name__ == "__main__":
    blackjack()
