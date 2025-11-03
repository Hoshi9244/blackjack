# Projet Blackjack

## 🎮 Description

Ce projet est une implémentation simple du jeu de **Blackjack** (ou "21") en **Python**, jouable directement dans le terminal.  
Le joueur commence avec une somme d’argent et peut parier à chaque partie.  
Les règles classiques du Blackjack sont respectées : tirer des cartes, rester, et tenter de battre le croupier sans dépasser 21.

Cette version inclut également l’option **Double Down** (doubler la mise et tirer une seule carte supplémentaire).

---

## ⚙️ Fonctionnalités

- Système d’argent et de mises
- Jeu contre un croupier automatisé
- Gestion des valeurs d’As (1 ou 11 selon le contexte)
- Option **Double Down** disponible au premier tour
- Détection des égalités et des dépassements
- Rejouabilité sans relancer le script

---

## 🃏 Règles du jeu

1. Le joueur et le croupier reçoivent chacun **2 cartes**.
2. Le joueur peut choisir :
   - **Tirer (o)** : ajouter une carte à sa main.
   - **Rester (n)** : terminer son tour.
   - **Double Down (d)** : doubler la mise, tirer une seule carte, puis passer la main.
3. Si le joueur dépasse **21**, il perd immédiatement sa mise.
4. Le croupier tire jusqu’à atteindre **au moins 17**.
5. Le gagnant est celui dont la main est la plus proche de 21 sans dépasser.

---

## 💰 Gestion de l’argent

- Le joueur commence avec **100 €**.
- À chaque manche, il choisit le montant de sa **mise**.
- Victoire → gains égaux à la mise.
- Défaite → perte de la mise.
- Égalité → la mise est rendue.
- Double Down → la mise est doublée avant de tirer une carte.

---

## ▶️ Utilisation

### 1. Exécution du jeu

Assurez-vous d’avoir **Python 3** installé, puis exécutez :

```bash
python blackjack.py
```
## 2. Contrôles dans le jeu

o → tirer une carte

n → rester

d → double down (si disponible)

Ctrl + C → quitter le jeu à tout moment
