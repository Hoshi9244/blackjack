const readline = require("readline");

// Création d'une interface pour lire les entrées utilisateur
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

// Valeurs des cartes
const valeurs = {
  "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
  "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10, "A": 11
};

// Crée et mélange un paquet de cartes
function creerPaquet() {
  const couleurs = ["♠", "♥", "♦", "♣"];
  let cartes = [];
  for (const c of couleurs) {
    for (const v of Object.keys(valeurs)) {
      cartes.push(`${v}${c}`);
    }
  }
  // Mélange
  for (let i = cartes.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [cartes[i], cartes[j]] = [cartes[j], cartes[i]];
  }
  return cartes;
}

// Calcule la valeur d'une main
function valeurMain(main) {
  let total = 0;
  let nbAs = 0;
  for (const carte of main) {
    const valeur = carte.slice(0, -1);
    total += valeurs[valeur];
    if (valeur === "A") nbAs++;
  }
  while (total > 21 && nbAs > 0) {
    total -= 10;
    nbAs--;
  }
  return total;
}

// Affiche une main
function afficherMain(nom, main, cacher = false) {
  if (cacher) {
    console.log(`${nom} : [??] ${main.slice(1).join(" ")}`);
  } else {
    console.log(`${nom} : ${main.join(" ")} (valeur = ${valeurMain(main)})`);
  }
}

// Fonction principale du jeu
async function blackjack() {
  let argent = 100;
  console.log("=== Bienvenue au Blackjack ===");
  console.log("Vous commencez avec", argent, "€");

  while (argent > 0) {
    console.log(`\nSolde : ${argent} €`);
    const mise = await question("Combien voulez-vous miser ? ");

    const miseInt = parseInt(mise);
    if (isNaN(miseInt) || miseInt <= 0 || miseInt > argent) {
      console.log("Mise invalide.");
      continue;
    }

    let paquet = creerPaquet();
    let joueur = [paquet.pop(), paquet.pop()];
    let croupier = [paquet.pop(), paquet.pop()];

    afficherMain("Croupier", croupier, true);
    afficherMain("Joueur", joueur);

    let doublePossible = true;

    // Tour du joueur
    while (valeurMain(joueur) < 21) {
      let options = "(o) Tirer | (n) Rester";
      if (doublePossible && argent >= 2 * miseInt) options += " | (d) Double Down";
      console.log("\n" + options);

      const choix = (await question("Votre choix : ")).toLowerCase();

      if (choix === "o") {
        joueur.push(paquet.pop());
        afficherMain("Joueur", joueur);
        doublePossible = false;
      } else if (choix === "d" && doublePossible && argent >= 2 * miseInt) {
        miseInt *= 2;
        console.log("Mise doublée :", miseInt, "€");
        joueur.push(paquet.pop());
        afficherMain("Joueur", joueur);
        break;
      } else {
        break;
      }
    }

    const valJoueur = valeurMain(joueur);

    // Si le joueur dépasse 21
    if (valJoueur > 21) {
      console.log("Vous dépassez 21, vous perdez votre mise.");
      argent -= miseInt;
    } else {
      console.log("\nTour du croupier :");
      afficherMain("Croupier", croupier);
      while (valeurMain(croupier) < 17) {
        croupier.push(paquet.pop());
        afficherMain("Croupier", croupier);
      }

      const valCroupier = valeurMain(croupier);
      console.log("\nRésultat final :");
      console.log(`Joueur : ${valJoueur} | Croupier : ${valCroupier}`);

      if (valCroupier > 21 || valJoueur > valCroupier) {
        console.log("Vous gagnez !");
        argent += miseInt;
      } else if (valJoueur === valCroupier) {
        console.log("Égalité, mise rendue.");
      } else {
        console.log("Le croupier gagne.");
        argent -= miseInt;
      }
    }

    if (argent <= 0) {
      console.log("\nVous n'avez plus d'argent. Fin du jeu.");
      break;
    }

    const rejouer = (await question("\nRejouer ? (o/n) : ")).toLowerCase();
    if (rejouer !== "o") break;
  }

  console.log(`\nVous repartez avec ${argent} €.`);
  console.log("Merci d’avoir joué au Blackjack.");
  rl.close();
}

// Fonction utilitaire pour poser une question et attendre la réponse
function question(texte) {
  return new Promise(resolve => rl.question(texte, resolve));
}

// Lancer le jeu
blackjack();
