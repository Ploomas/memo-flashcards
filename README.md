# Mémo — cartes de révision personnelles

[Ouvrir l’application](https://memo-cartes-ipad-nov26.ribbedcinch2.chatgpt.site) · [Télécharger les sources prêtes à modifier](dist/memo-sources.zip)

Dans ce dépôt, les fichiers de l’application se trouvent dans `dist/`. Pour lancer un serveur depuis la racine du dépôt : `python3 -m http.server 8000 --directory dist`. Pour télécharger tout le dépôt sur GitHub : **Code → Download ZIP**. Aucune donnée personnelle de révision n’est incluse.

Application web indépendante, en français, sans dépendance et sans serveur de données. Ce n'est pas une copie complète d'Anki ni une version officielle. Le dépôt https://github.com/ankitects/anki a été consulté : son application de bureau utilise notamment Rust, Python et Qt et n'est pas installable telle quelle sur iPad. Aucun code Anki n'est incorporé à cette version de Mémo.

## Sur iPad

1. Ouvrez le lien du site dans Safari, puis Partager → Sur l'écran d'accueil.
2. Créez un paquet et ajoutez vos cartes. Les six cartes de départ sont des exemples, supprimables.
3. Révisez le recto, affichez le verso, choisissez À revoir / Difficile / Bien / Facile.
4. Exportez régulièrement une sauvegarde JSON dans Fichiers. Le stockage est local au navigateur et à l'adresse du site : pas de synchronisation automatique. Safari peut effacer des données locales, notamment en navigation privée.

## Modifier l'application sur iPad

Décompressez memo-sources.zip dans Fichiers. Utilisez un éditeur de code pour iPad capable d'ouvrir un dossier et de prévisualiser du HTML (par exemple un éditeur avec serveur local). Modifiez `style.css` pour l'apparence et `app.js` pour les fonctions. `index.html` définit la page. Le fichier `memo-autonome.html` contient tout dans un fichier pour les éditeurs avec aperçu HTML. Un aperçu dans Fichiers n'est pas un navigateur complet : il ne permet pas forcément d'exécuter l'application ou de conserver ses données.

Pour l'usage quotidien, hébergez le dossier contenant index.html en HTTPS. Aucun npm, build, compte Anki ou serveur de base de données n'est nécessaire. Après modification, incrémentez la version CACHE dans sw.js. Le service worker propose un cache hors ligne, mais le comportement sur iPad et derrière l'authentification de l'hébergement n'a pas été testé. Ne comptez pas sur le cache comme sauvegarde.

## Sur ordinateur

Depuis le dossier des fichiers : `python3 -m http.server 8000`, puis ouvrez http://localhost:8000. Les cartes et préférences sont stockées sous la clé localStorage `memo.collection.v1`.

## Import / export

- JSON : collection Mémo version 1, cartes, progression, préférences et historique. Importer remplace la collection après confirmation.
- TSV UTF-8 : une carte par ligne, colonnes recto, verso, nom du paquet, mots-clés. Les colonnes sont séparées par une tabulation. Les lignes commençant par # sont ignorées. L'import ajoute des cartes ; il ne déduplique pas.
- Export TSV vers Anki : lors de l'import dans Anki, associez les colonnes 1 et 2 au recto et au verso et sélectionnez le paquet voulu. Les colonnes 3 et 4 sont des métadonnées ; l'export ne conserve pas la planification Anki et aplatit les sauts de ligne.
- Pas de prise en charge .apkg/.colpkg, images, audio, HTML enrichi, cartes à trous, extensions ou AnkiWeb.

## Planification

Ordonnanceur simplifié propre à Mémo, différent de FSRS et d'Anki. À revoir : disponible à nouveau dans une minute, dans une nouvelle session. Une nouvelle carte évaluée Bien revient dans un jour, Facile dans quatre jours. Les intervalles suivants dépendent de la facilité et de l'intervalle précédent. Une session ne contient que les cartes dues au moment de son démarrage. Annuler restaure la dernière réponse et son état précédent.

## Validation

Syntaxe JavaScript vérifiée avec Node. Tests de planification, validation d'import, affichage des vues et sauvegarde exécutés avec un DOM simulé. Pas de validation Safari/iPad ou de test visuel navigateur dans cet environnement.

## Licence

Code original Mémo : licence MIT incluse. Anki reste la propriété de ses contributeurs et son code est distribué selon sa propre licence AGPL-3.0-or-later et les exceptions décrites dans son dépôt. Le présent téléchargement ne contient pas les sources d'Anki.

## Publier avec GitHub Pages

Le dossier `docs/` contient une copie prête à publier de l’application.

1. Ouvrez **Settings → Pages** dans ce dépôt.
2. Dans **Build and deployment**, choisissez **Deploy from a branch**.
3. Sélectionnez la branche **main**, le dossier **/docs**, puis **Save**.
4. Attendez la fin du déploiement GitHub Pages. L’adresse attendue est https://ploomas.github.io/memo-flashcards/ (elle ne fonctionne qu’après activation et déploiement).

GitHub Pages pour un dépôt privé nécessite une offre GitHub compatible. Si votre offre ne le permet pas, GitHub proposera de changer d’offre ou de rendre le dépôt public ; choisissez explicitement ce qui vous convient. La visibilité du dépôt n’a pas été modifiée par cette configuration.

Après modification de `dist/`, exécutez `python3 scripts/prepare-pages.py`, puis committez et poussez `dist/` et `docs/`. Sur iPad sans Python, recopiez les fichiers modifiés de `dist/` vers `docs/`.

Les cartes sont liées à l’adresse du site : pour passer de l’ancien hébergement à GitHub Pages, exportez la collection JSON sur l’ancien site, puis importez-la sur le nouveau.
