# -*- coding: utf-8 -*-
"""Escribe referentiel/*.json y backend/Referentiel.gs desde las listas de abajo."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SECTIONS = [
    (
        "COMP",
        "Comportement et relations avec les autres",
        [
            ("Respecte les règles de la classe", "Respecter les règles de la classe"),
            ("Suit les consignes de l'enseignante", "Suivre les consignes données"),
            ("Attend son tour pour parler", "Attendre son tour pour parler"),
            ("Lève la main avant de prendre la parole", "Lever la main avant de prendre la parole"),
            ("Écoute les autres sans les interrompre", "Écouter les autres sans les interrompre"),
            ("Respecte les autres élèves et leur espace personnel", "Respecter les autres élèves et leur espace personnel"),
            ("Utilise un ton de voix adapté", "Adapter son ton de voix aux situations"),
            ("Se déplace calmement dans la classe", "Se déplacer calmement dans la classe"),
            ("Utilise le matériel de façon appropriée", "Utiliser le matériel de façon appropriée"),
            ("Participe positivement à la vie de classe", "Participer positivement à la vie de classe"),
            ("Accepte les rappels de l'adulte", "Accepter les rappels de l'adulte"),
            ("Respecte les routines et les transitions", "Respecter les routines et les transitions"),
            ("Partage le matériel avec les autres", "Partager le matériel avec les autres"),
            ("Joue et collabore avec les autres élèves", "Participer aux jeux et aux activités avec les autres"),
            ("Gère les désaccords avec calme", "Apprendre à résoudre les désaccords avec calme"),
            ("Demande de l'aide lorsqu'une situation est difficile", "Demander de l'aide lorsqu'une situation est difficile"),
        ],
    ),
    (
        "MOTIV",
        "Motivation, participation et persévérance",
        [
            ("Participe activement aux activités", "Participer davantage aux activités"),
            ("Montre de l'intérêt pour les apprentissages", "Développer son intérêt pour les apprentissages"),
            ("Pose des questions pertinentes", "Poser des questions lorsqu'il ou elle ne comprend pas"),
            ("Partage ses idées avec le groupe", "Partager davantage ses idées avec le groupe"),
            ("Essaie les activités proposées", "Essayer les activités proposées"),
            ("Accepte de relever de nouveaux défis", "Accepter de relever de nouveaux défis"),
            ("Fait preuve de curiosité", "Développer sa curiosité"),
            ("Persévère lorsque la tâche est difficile", "Persévérer lorsque la tâche est difficile"),
            ("Accepte de recommencer après une erreur", "Accepter de recommencer après une erreur"),
            ("Maintient ses efforts pendant une activité", "Maintenir ses efforts pendant une activité"),
            ("Termine les activités commencées", "Terminer les activités commencées"),
            ("S'engage dans les activités moins familières", "Participer aux activités moins familières"),
            ("Prend plaisir à apprendre", "Développer le plaisir d'apprendre"),
        ],
    ),
    (
        "ATTN",
        "Attention et concentration",
        [
            ("Écoute les explications en grand groupe", "Écouter les explications en grand groupe"),
            ("Maintient son attention pendant les explications", "Maintenir son attention pendant les explications"),
            ("Reste concentré pendant le travail individuel", "Rester concentré pendant le travail individuel"),
            ("Écoute les consignes jusqu'à la fin", "Écouter les consignes jusqu'à la fin"),
            ("Commence son travail après les consignes", "Commencer son travail après les consignes"),
            ("Travaille sans se laisser distraire", "Limiter les distractions pendant le travail"),
            ("Revient à son travail après une distraction", "Revenir à son travail après une distraction"),
            ("Maintient son attention jusqu'à la fin d'une tâche", "Maintenir son attention jusqu'à la fin d'une tâche"),
            ("Suit les différentes étapes d'une activité", "Suivre les différentes étapes d'une activité"),
            ("Maintient un rythme de travail adapté", "Maintenir un rythme de travail adapté"),
            ("Termine son travail dans le temps prévu", "Terminer son travail dans le temps prévu"),
            ("Vérifie son travail avant de le remettre", "Prendre le temps de vérifier son travail"),
            ("Réalise les activités avec peu de rappels", "Réaliser les activités avec moins de rappels"),
        ],
    ),
    (
        "AUTO",
        "Autonomie et organisation",
        [
            ("Prépare son matériel pour les activités", "Préparer son matériel pour les activités"),
            ("Retrouve facilement son matériel", "Retrouver son matériel dans son cartable"),
            ("Organise son espace de travail", "Organiser son espace de travail"),
            ("Range son matériel après les activités", "Ranger son matériel après les activités"),
            ("Suit les routines de la classe", "Suivre les routines de la classe"),
            ("Se met au travail de façon autonome", "Se mettre au travail de façon autonome"),
            ("Réalise les tâches sans aide constante", "Réaliser les tâches avec moins d'aide"),
            ("Essaie une stratégie avant de demander de l'aide", "Essayer une stratégie avant de demander de l'aide"),
            ("Utilise les outils disponibles en classe", "Utiliser les outils disponibles en classe"),
            ("Respecte les étapes d'une tâche", "Respecter les étapes d'une tâche"),
            ("Prend soin de son matériel", "Prendre soin de son matériel"),
            ("Se prépare aux changements d'activité", "Se préparer aux changements d'activité"),
            ("Gère son matériel dans son cartable", "Organiser son matériel dans son cartable"),
        ],
    ),
    (
        "LECT",
        "Français – Lecture",
        [
            ("Reconnaît les lettres de l'alphabet", "Reconnaître les lettres de l'alphabet"),
            ("Associe les lettres aux sons correspondants", "Associer les lettres aux sons correspondants"),
            ("Reconnaît les voyelles et les consonnes", "Reconnaître les voyelles et les consonnes"),
            ("Identifie les sons dans les mots", "Identifier les sons dans les mots"),
            ("Lit des syllabes simples", "Lire des syllabes simples"),
            ("Fusionne les syllabes pour lire des mots", "Fusionner les syllabes pour lire des mots"),
            ("Lit des mots simples", "Lire des mots simples sans aide"),
            ("Reconnaît les mots étudiés en classe", "Reconnaître les mots étudiés en classe"),
            ("Lit des phrases courtes", "Lire des phrases courtes"),
            ("Respecte l'ordre des mots lorsqu'il ou elle lit", "Lire les mots dans le bon ordre"),
            ("Décode les mots plutôt que de les deviner", "Décoder les mots plutôt que les deviner"),
            ("Lit avec une certaine fluidité", "Développer la fluidité en lecture"),
            ("Comprend les phrases lues", "Comprendre les phrases lues"),
            ("Répond aux questions sur un texte", "Répondre aux questions sur un texte"),
            ("Repère des informations dans une phrase", "Repérer des informations dans une phrase"),
        ],
    ),
    (
        "ECRI",
        "Français – Écriture",
        [
            ("Forme correctement les lettres", "Améliorer la formation des lettres"),
            ("Respecte le sens de formation des lettres", "Respecter le sens de formation des lettres"),
            ("Écrit les lettres de façon lisible", "Écrire les lettres de façon lisible"),
            ("Respecte l'espace entre les lettres et les mots", "Respecter l'espace entre les lettres et les mots"),
            ("Écrit des syllabes simples", "Écrire des syllabes simples"),
            ("Écrit des mots à partir des sons entendus", "Écrire des mots à partir des sons entendus"),
            ("Écrit les mots étudiés en classe", "Écrire les mots étudiés en classe"),
            ("Utilise les sons pour écrire des mots", "Utiliser les sons pour écrire des mots"),
            ("Écrit des phrases simples", "Construire des phrases simples"),
            ("Respecte l'ordre des mots dans une phrase", "Respecter l'ordre des mots dans une phrase"),
            ("Replace les mots dans le bon ordre", "Replacer les mots dans le bon ordre"),
            ("Utilise une majuscule au début d'une phrase", "Utiliser une majuscule au début d'une phrase"),
            ("Utilise un point à la fin d'une phrase", "Utiliser un point à la fin d'une phrase"),
            ("Sépare correctement les mots", "Séparer correctement les mots"),
            ("Relit et vérifie son travail", "Relire et vérifier son travail"),
            ("Termine les activités d'écriture", "Terminer les activités d'écriture"),
        ],
    ),
    (
        "NUM",
        "Mathématiques – Numération",
        [
            ("Reconnaît les nombres étudiés", "Reconnaître les nombres étudiés"),
            ("Lit les nombres", "Lire les nombres"),
            ("Écrit les nombres correctement", "Écrire les nombres correctement"),
            ("Associe les nombres aux quantités", "Associer les nombres aux quantités"),
            ("Dénombre une collection d'objets", "Dénombrer une collection d'objets"),
            ("Compte sans oublier ni compter deux fois", "Compter sans oublier ni compter deux fois"),
            ("Compte à partir d'un nombre donné", "Compter à partir d'un nombre donné"),
            ("Compte à rebours", "Compter à rebours"),
            ("Trouve le nombre qui vient avant", "Trouver le nombre qui vient avant"),
            ("Trouve le nombre qui vient après", "Trouver le nombre qui vient après"),
            ("Compare deux nombres", "Comparer deux nombres"),
            ("Identifie le plus grand et le plus petit nombre", "Identifier le plus grand et le plus petit nombre"),
            ("Représente un nombre de différentes façons", "Représenter un nombre de différentes façons"),
            ("Comprend les notions de plus que et moins que", "Comprendre les notions de plus que et moins que"),
            ("Comprend la notion d'autant que", "Comprendre la notion d'autant que"),
        ],
    ),
    (
        "CALC",
        "Mathématiques – Calcul et résolution de problèmes",
        [
            ("Résout des additions simples", "Résoudre des additions simples"),
            ("Résout des soustractions simples", "Résoudre des soustractions simples"),
            ("Utilise du matériel pour calculer", "Utiliser du matériel pour calculer"),
            ("Représente une addition avec des objets ou un dessin", "Représenter une addition avec des objets ou un dessin"),
            ("Représente une soustraction avec des objets ou un dessin", "Représenter une soustraction avec des objets ou un dessin"),
            ("Comprend les situations d'ajout", "Comprendre les situations d'ajout"),
            ("Comprend les situations de retrait", "Comprendre les situations de retrait"),
            ("Comprend les situations de partage", "Comprendre les situations de partage"),
            ("Comprend les situations de regroupement", "Comprendre les situations de regroupement"),
            ("Identifie ce que demande un problème", "Identifier ce que demande un problème"),
            ("Choisit une stratégie pour résoudre un problème", "Choisir une stratégie pour résoudre un problème"),
            ("Explique sa démarche", "Expliquer sa démarche"),
            ("Vérifie ses réponses", "Vérifier ses réponses"),
            ("Utilise les stratégies vues en classe", "Utiliser les stratégies vues en classe"),
            ("Résout des problèmes avec autonomie", "Résoudre des problèmes avec plus d'autonomie"),
        ],
    ),
    (
        "MOTR",
        "Motricité fine et réalisation des travaux",
        [
            ("Tient son crayon de façon fonctionnelle", "Améliorer la prise du crayon"),
            ("Contrôle ses mouvements", "Développer le contrôle de ses mouvements"),
            ("Écrit de façon lisible", "Améliorer la lisibilité de son écriture"),
            ("Découpe avec précision", "Découper avec plus de précision"),
            ("Colle les éléments correctement", "Coller les éléments correctement"),
            ("Colorie en respectant les contours", "Colorier en respectant les contours"),
            ("Réalise les travaux avec soin", "Réaliser les travaux avec davantage de soin"),
            ("Utilise le matériel adéquatement", "Utiliser le matériel adéquatement"),
            ("Prend le temps de terminer ses travaux", "Prendre le temps de terminer ses travaux"),
            ("Respecte les étapes de réalisation", "Respecter les étapes de réalisation"),
        ],
    ),
]

BLOCS = [
    (
        "ATT",
        "Attention et concentration",
        [
            (
                "Découper la tâche en petites étapes",
                "Présenter une étape à la fois pour éviter de demander trop d'informations en même temps.",
                "« Fais la première question. Après, on regarde la suivante. »",
            ),
            (
                "Annoncer un objectif clair",
                "Dire simplement ce que l'enfant cherche à faire avant de commencer.",
                "« Aujourd'hui, on repère les mots qui commencent par le son /m/. »",
            ),
            (
                "Faire redire la consigne",
                "Inviter l'enfant à reformuler la consigne. Cela permet de vérifier qu'il a compris ce qui est attendu.",
                "« Qu'est-ce que tu dois faire en premier? »",
            ),
            (
                "Alterner effort et mouvement",
                "Prévoir de courtes pauses actives. Le mouvement peut soutenir le retour à la tâche.",
                "S'étirer, faire quelques pas ou bouger brièvement avant de reprendre.",
            ),
            (
                "Alléger l'espace de travail",
                "Réduire les éléments qui attirent l'attention et garder le matériel utile.",
                "Sur le pupitre : le cahier, le crayon et la gomme.",
            ),
            (
                "S'appuyer sur des repères visuels",
                "Afficher quelques étapes avec des images, des mots ou des cases à cocher.",
                "1. J'écoute 2. Je fais 3. Je vérifie.",
            ),
            (
                "Pratiquer l'attention par le jeu",
                "Proposer des jeux où l'enfant doit repérer une information précise.",
                "Cherche et trouve, jeu des différences ou repérer l'intrus.",
            ),
            (
                "Utiliser un signal de recentrage",
                "Convenir d'un geste ou d'un mot discret pour aider l'enfant à revenir à son activité.",
                "Un petit signe connu de l'enfant, sans interrompre le groupe.",
            ),
        ],
    ),
    (
        "EXE",
        "Fonctions exécutives et autonomie",
        [
            (
                "Prévoir les étapes avant de commencer",
                "Inviter l'enfant à dire ce qu'il fera d'abord, puis ensuite.",
                "« De quoi as-tu besoin? Quelle sera la première étape? »",
            ),
            (
                "Laisser un temps pour chercher",
                "Éviter de donner tout de suite la réponse; offrir un indice au besoin.",
                "« Essaie d'abord. Je peux te donner un indice si tu bloques. »",
            ),
            (
                "Installer des routines visuelles",
                "Rendre les routines prévisibles avec quelques étapes illustrées.",
                "Déposer son sac, sortir son agenda, préparer son matériel.",
            ),
            (
                "Faire de petits jeux de mémoire",
                "Faire retenir puis réaliser deux ou trois consignes simples, selon le niveau de l'enfant.",
                "« Prends ton cahier, ouvre-le et prends ton crayon. »",
            ),
            (
                "Jouer à changer de règle",
                "Proposer des jeux où l'enfant doit adapter sa façon de faire.",
                "Classer des objets par couleur, puis par forme.",
            ),
            (
                "Pratiquer l'attente et le contrôle de soi",
                "Jouer à attendre un signal avant d'agir.",
                "Jacques a dit, 1-2-3 soleil ou jeux de statues.",
            ),
            (
                "Préparer son matériel",
                "Aider l'enfant à prendre l'habitude de réunir seul le matériel nécessaire.",
                "Utiliser une petite liste avant de commencer une activité.",
            ),
            (
                "Installer une routine de vérification",
                "Apprendre à vérifier une ou deux choses à la fin d'une tâche.",
                "« Ai-je répondu? Ai-je écrit mon prénom? »",
            ),
            (
                "Chercher une autre solution",
                "Encourager l'enfant à ajuster sa stratégie quand la première ne fonctionne pas.",
                "« Qu'est-ce que tu pourrais essayer autrement? »",
            ),
        ],
    ),
    (
        "REG",
        "Comportement et autorégulation",
        [
            (
                "Nommer les émotions",
                "Aider l'enfant à mettre des mots sur ce qu'il ressent, sans jugement.",
                "« Tu sembles déçu. Est-ce bien ce que tu ressens? »",
            ),
            (
                "Faire une pause pour se calmer",
                "Enseigner une routine simple : s'arrêter, respirer, puis réfléchir à la suite.",
                "Prendre trois respirations lentes avec l'adulte.",
            ),
            (
                "Pratiquer l'attente",
                "Utiliser des jeux qui demandent d'attendre son tour et de respecter une règle.",
                "Jeux de société simples ou jeux de cartes.",
            ),
            (
                "Souligner un comportement précis",
                "Nommer le comportement observé plutôt que dire seulement « bravo ».",
                "« Tu as attendu que ton camarade ait fini de parler. »",
            ),
            (
                "Préparer les transitions",
                "Rappeler les attentes avant une activité ou un changement de routine.",
                "« Dans deux minutes, on range et on se prépare pour la lecture. »",
            ),
            (
                "Accompagner la frustration",
                "Reconnaître la difficulté et guider l'enfant vers une solution.",
                "« C'est difficile. Veux-tu demander de l'aide ou essayer encore? »",
            ),
            (
                "Parler du point de vue des autres",
                "Inviter l'enfant à réfléchir aux émotions possibles de ses camarades.",
                "« Comment ton ami a-t-il pu se sentir? »",
            ),
            (
                "Réparer après un conflit",
                "Aider l'enfant à poser un geste concret pour réparer la situation.",
                "Aider à reconstruire, ranger ou présenter des excuses sincères.",
            ),
            (
                "Pratiquer avec des mises en situation",
                "Jouer une scène pour apprendre à demander de l'aide, attendre ou exprimer un désaccord.",
                "S'exercer à dire : « Je n'aime pas ça. Arrête, s'il te plaît. »",
            ),
            (
                "Voir l'erreur comme une occasion d'apprendre",
                "Rappeler qu'une erreur donne une information pour essayer autrement.",
                "« Cette façon ne fonctionne pas encore. Que peux-tu changer? »",
            ),
        ],
    ),
    (
        "MOTI",
        "Motivation et engagement dans les apprentissages",
        [
            (
                "Valoriser la stratégie utilisée",
                "Mettre l'accent sur la démarche, l'effort et les progrès, pas seulement sur la bonne réponse.",
                "« Tu as découpé le mot en syllabes pour le lire. »",
            ),
            (
                "Choisir un petit objectif",
                "Fixer une cible claire et réaliste pour que l'enfant puisse voir ses progrès.",
                "Lire quelques mots travaillés en classe en prenant son temps.",
            ),
            (
                "Dire « pas encore »",
                "Aider l'enfant à comprendre qu'une habileté peut se développer avec la pratique.",
                "« Tu ne le maîtrises pas encore; on va pratiquer un peu. »",
            ),
            (
                "Proposer un défi à sa portée",
                "Choisir une tâche un peu nouvelle, mais qui s'appuie sur des acquis.",
                "Lire un mot nouveau avec des sons déjà connus.",
            ),
            (
                "Encourager une nouvelle tentative",
                "Inviter l'enfant à essayer une autre stratégie plutôt que d'abandonner immédiatement.",
                "« Regarde le début du mot. Quel son connais-tu? »",
            ),
            (
                "Faire des liens avec la vie quotidienne",
                "Montrer comment les apprentissages servent dans des situations familières.",
                "Lire une affiche, compter des objets ou écrire une petite liste.",
            ),
            (
                "Offrir un choix limité",
                "Donner deux options qui répondent toutes les deux à l'objectif.",
                "« Préfères-tu lire ce texte ou celui-là? »",
            ),
            (
                "Rendre les progrès visibles",
                "Garder quelques traces des réalisations pour que l'enfant puisse constater son évolution.",
                "Comparer deux textes ou dessins faits à différents moments.",
            ),
            (
                "Faire une courte autoévaluation",
                "Aider l'enfant à identifier une réussite et une chose à pratiquer.",
                "« De quoi es-tu fier? Qu'aimerais-tu améliorer? »",
            ),
            (
                "Apprendre par le jeu",
                "Utiliser des jeux courts pour revoir une notion et maintenir l'engagement.",
                "Bingo de lettres, dominos de nombres ou jeux de sons.",
            ),
        ],
    ),
    (
        "MATH",
        "Mathématique",
        [
            (
                "Faire retrouver une notion de mémoire",
                "Poser une petite question sur un apprentissage déjà vu avant de donner la réponse.",
                "« Quel nombre vient juste avant 8? »",
            ),
            (
                "Représenter une quantité de plusieurs façons",
                "Associer les objets, les doigts, les dessins et les chiffres.",
                "Montrer 6 avec des jetons, les doigts et le chiffre 6.",
            ),
            (
                "Décomposer les nombres",
                "Chercher différentes façons de former une même quantité.",
                "« 8, c'est 5 et combien? Peut-on le faire autrement? »",
            ),
            (
                "Faire expliquer la démarche",
                "Demander à l'enfant de raconter comment il a trouvé sa réponse.",
                "« Qu'as-tu fait avec les jetons ou dans ta tête? »",
            ),
            (
                "Jouer avec la suite des nombres",
                "Trouver le nombre avant, après ou entre deux nombres.",
                "« Quel nombre est entre 5 et 7? »",
            ),
            (
                "Manipuler pour calculer",
                "Utiliser du matériel concret pour représenter les ajouts, les retraits ou les comparaisons.",
                "Cubes, jetons, boutons ou dessins.",
            ),
            (
                "Faire de courts calculs oraux",
                "Proposer de petites situations de calcul en lien avec les notions vues en classe.",
                "« Tu as 4 cubes et j'en ajoute 1. Combien en as-tu? »",
            ),
            (
                "Comparer des collections",
                "Comparer deux groupes et expliquer où il y en a plus, moins ou autant.",
                "Comparer deux collections de crayons ou de blocs.",
            ),
            (
                "Résoudre un problème du quotidien",
                "Présenter une situation familière qui invite à réfléchir à une quantité.",
                "« Il y a 3 pommes. On en ajoute 2. Combien y en a-t-il? »",
            ),
            (
                "Varier les représentations",
                "Relier les doigts, les dés, les boîtes de dix, les objets et les chiffres.",
                "Montrer la même quantité avec des jetons et un dessin.",
            ),
            (
                "Vérifier une réponse",
                "Comparer des réponses et inviter l'enfant à expliquer comment il peut vérifier.",
                "« Comment peux-tu savoir si ta réponse est juste? »",
            ),
            (
                "Revoir les notions à différents moments",
                "Faire de courtes reprises espacées pour aider l'enfant à consolider ce qu'il apprend.",
                "Reprendre quelques nombres ou calculs un autre jour.",
            ),
        ],
    ),
    (
        "FR",
        "Français : lecture et écriture",
        [
            (
                "Jouer avec les sons",
                "Identifier le premier son, le dernier son ou les sons entendus dans un mot.",
                "« Quel son entends-tu au début de moto? »",
            ),
            (
                "Fusionner des syllabes",
                "Assembler oralement des syllabes pour former un mot.",
                "« pa » + « pi » = « papi ».",
            ),
            (
                "Repérer un son dans les mots",
                "Trouver des mots qui commencent ou se terminent par un son ciblé.",
                "Chercher des mots qui commencent par /s/.",
            ),
            (
                "Associer les lettres et les sons",
                "Revoir les correspondances déjà enseignées entre lettres et sons.",
                "Voir la lettre, dire son son et trouver un mot.",
            ),
            (
                "Relire des syllabes et des mots connus",
                "Inviter l'enfant à lire des éléments déjà travaillés en classe, en lui laissant un temps de réflexion.",
                "Relire quelques syllabes ou mots familiers.",
            ),
            (
                "Relire un court texte",
                "Relire un texte bref déjà connu pour gagner en aisance, sans mettre l'accent sur la vitesse.",
                "Faire une relecture attentive d'un texte court.",
            ),
            (
                "Parler de ce qu'on lit",
                "Poser une question pour vérifier la compréhension ou faire une petite déduction.",
                "« Où se passe l'histoire? Pourquoi le personnage fait-il cela? »",
            ),
            (
                "Enrichir le vocabulaire",
                "Expliquer un mot nouveau et inviter l'enfant à le réutiliser.",
                "Trouver une phrase avec le nouveau mot.",
            ),
            (
                "Construire une phrase",
                "Remettre des mots dans l'ordre pour former une phrase qui a du sens.",
                "Utiliser des étiquettes-mots à déplacer.",
            ),
            (
                "Compter les mots d'une phrase",
                "Faire prendre conscience qu'une phrase est composée de mots séparés.",
                "Dire une phrase et placer un jeton par mot.",
            ),
            (
                "Mémoriser un mot",
                "Observer un mot, le cacher, essayer de l'écrire de mémoire, puis vérifier ensemble.",
                "Regarder, cacher, écrire et comparer.",
            ),
            (
                "Écrire une courte phrase",
                "Écrire à partir d'un dessin ou d'une expérience en portant attention aux sons et aux espaces.",
                "Écrire une phrase pour décrire son dessin.",
            ),
            (
                "Relire pour vérifier",
                "Choisir un ou deux éléments à vérifier à la relecture.",
                "Vérifier les espaces et les sons entendus dans les mots.",
            ),
            (
                "Imaginer la suite d'une histoire",
                "Inviter l'enfant à faire une prédiction et à expliquer son idée.",
                "« Que pourrait-il arriver ensuite? Qu'est-ce qui te fait penser cela? »",
            ),
        ],
    ),
    (
        "TRAN",
        "Stratégies transversales",
        [
            (
                "Récupération active : retrouver de mémoire",
                "Inviter l'enfant à se rappeler une information avant de lui redonner la réponse.",
                "« Qu'est-ce que tu te rappelles de ce qu'on a appris? »",
            ),
            (
                "Répétition espacée : revoir à plusieurs moments",
                "Reprendre une notion en courtes périodes réparties sur plusieurs jours.",
                "Revoir quelques mots ou nombres aujourd'hui, puis dans quelques jours.",
            ),
            (
                "Verbalisation : expliquer sa pensée",
                "Encourager l'enfant à dire ce qu'il fait et comment il s'y prend.",
                "« Explique-moi comment tu as trouvé. »",
            ),
            (
                "Apprentissage multisensoriel : voir, dire, faire",
                "Associer la vue, l'écoute, la parole, le geste et la manipulation lorsque c'est utile.",
                "Voir une lettre, dire son son, la tracer et trouver un mot.",
            ),
            (
                "Pause active : bouger pour revenir",
                "Prévoir de courts moments de mouvement entre les activités.",
                "S'étirer ou bouger brièvement, puis reprendre.",
            ),
            (
                "Métacognition : réfléchir à son apprentissage",
                "Aider l'enfant à nommer ce qu'il a appris et ce qui l'a aidé.",
                "« Qu'est-ce qui t'a aidé? Que pourrais-tu essayer la prochaine fois? »",
            ),
        ],
    ),
]

NOMS_PARTIELS = {
    "LECT": [
        "Jouer avec les sons",
        "Fusionner des syllabes",
        "Repérer un son dans les mots",
        "Associer les lettres et les sons",
        "Relire des syllabes et des mots connus",
        "Relire un court texte",
        "Parler de ce qu'on lit",
        "Enrichir le vocabulaire",
        "Imaginer la suite d'une histoire",
    ],
    "ECRI": [
        "Construire une phrase",
        "Compter les mots d'une phrase",
        "Mémoriser un mot",
        "Écrire une courte phrase",
        "Relire pour vérifier",
    ],
    "NUM": [
        "Faire retrouver une notion de mémoire",
        "Représenter une quantité de plusieurs façons",
        "Décomposer les nombres",
        "Jouer avec la suite des nombres",
        "Comparer des collections",
        "Varier les représentations",
        "Revoir les notions à différents moments",
    ],
    "CALC": [
        "Faire expliquer la démarche",
        "Manipuler pour calculer",
        "Faire de courts calculs oraux",
        "Résoudre un problème du quotidien",
        "Vérifier une réponse",
        "Revoir les notions à différents moments",
    ],
    "MOTR": [
        "Préparer son matériel",
        "Installer des routines visuelles",
        "Alléger l'espace de travail",
        "Découper la tâche en petites étapes",
    ],
}

BLOC_COMPLET = {
    "COMP": "Comportement et autorégulation",
    "MOTIV": "Motivation et engagement dans les apprentissages",
    "ATTN": "Attention et concentration",
    "AUTO": "Fonctions exécutives et autonomie",
}


def construire():
    grille = []
    for code, titre, items in SECTIONS:
        grille.append(
            {
                "code": code,
                "titre": titre,
                "items": [
                    {"code": "%s-%02d" % (code, i + 1), "force": force, "defi": defi}
                    for i, (force, defi) in enumerate(items)
                ],
            }
        )

    strategies = []
    for prefixe, bloc, items in BLOCS:
        for i, (nom, utilisation, exemple) in enumerate(items):
            strategies.append(
                {
                    "code": "%s-%02d" % (prefixe, i + 1),
                    "bloc": bloc,
                    "nom": nom,
                    "utilisation": utilisation,
                    "exemple": exemple,
                }
            )

    par_nom = {}
    for strategie in strategies:
        if strategie["nom"] in par_nom:
            raise SystemExit("Nom de stratégie en double : " + strategie["nom"])
        par_nom[strategie["nom"]] = strategie["code"]

    def codes_bloc(bloc):
        return [s["code"] for s in strategies if s["bloc"] == bloc]

    trans = codes_bloc("Stratégies transversales")
    liens = []
    for section in grille:
        code = section["code"]
        if code in BLOC_COMPLET:
            propres = codes_bloc(BLOC_COMPLET[code])
        else:
            propres = [par_nom[nom] for nom in NOMS_PARTIELS[code]]
        for strategie in propres + trans:
            liens.append({"section": code, "strategie": strategie})

    return grille, strategies, liens


def verifier(grille, strategies, liens):
    codes_items = []
    for section in grille:
        for item in section["items"]:
            if not item["code"].startswith(section["code"] + "-"):
                raise SystemExit("Code d'item hors section : " + item["code"])
            if not item["force"] or not item["defi"]:
                raise SystemExit("Force ou défi vide : " + item["code"])
            codes_items.append(item["code"])
    if len(codes_items) != len(set(codes_items)):
        raise SystemExit("Codes d'items en double")

    codes_strat = [s["code"] for s in strategies]
    if len(codes_strat) != len(set(codes_strat)):
        raise SystemExit("Codes de stratégies en double")
    connus = set(codes_strat)
    sections = {s["code"] for s in grille}
    vus = set()
    for lien in liens:
        if lien["section"] not in sections:
            raise SystemExit("Section inconnue : " + lien["section"])
        if lien["strategie"] not in connus:
            raise SystemExit("Stratégie inconnue : " + lien["strategie"])
        cle = (lien["section"], lien["strategie"])
        if cle in vus:
            raise SystemExit("Lien en double : " + str(cle))
        vus.add(cle)
    for code in sections:
        if not any(l["section"] == code for l in liens):
            raise SystemExit("Section sans stratégies : " + code)

    print("items", len(codes_items), "strategies", len(strategies), "liens", len(liens))


def ecrire(grille, strategies, liens):
    dossier = ROOT / "referentiel"
    dossier.mkdir(parents=True, exist_ok=True)
    (dossier / "grille.json").write_text(
        json.dumps({"sections": grille}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    (dossier / "strategies.json").write_text(
        json.dumps({"strategies": strategies}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    (dossier / "correspondance.json").write_text(
        json.dumps({"liens": liens}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    catalogue = {"grille": grille, "strategies": strategies, "correspondance": liens}
    corps = json.dumps(catalogue, ensure_ascii=False, indent=2)
    gs = (
        "/**\n"
        " * Referentiel.gs — Catálogo de la grille y de las stratégies.\n"
        " * Generado por scripts/build-referentiel.py. No editar a mano.\n"
        " * Lo visible para el enseignant está en francés dentro de los textos.\n"
        " */\n"
        "function catalogueReferentiel() {\n"
        "  return "
        + corps
        + ";\n"
        "}\n"
    )
    backend = ROOT / "backend"
    backend.mkdir(parents=True, exist_ok=True)
    (backend / "Referentiel.gs").write_text(gs, encoding="utf-8")
    print("escrito", backend / "Referentiel.gs")


if __name__ == "__main__":
    grille, strategies, liens = construire()
    verifier(grille, strategies, liens)
    ecrire(grille, strategies, liens)
