# Projet_Annuel_M1IABD

### Documentation
l'API Backend
Le code backend fournit une API pour effectuer des prédictions de sepsis à partir des caractéristiques d'un individu. Il est basé sur le framework Flask et utilise une classe Sepsis pour effectuer les prédictions.

Installation
Pour exécuter l'API, vous devez d'abord installer les dépendances requises. Vous pouvez le faire en exécutant la commande suivante dans votre environnement virtuel ou global :

Copy code
pip install flask pandas joblib
Ensuite, vous pouvez exécuter le fichier index.py pour lancer l'API.

Fonctionnalités de l'API
L'API fournit les fonctionnalités suivantes :

Endpoint /predict - Ce point de terminaison permet de faire des prédictions de sepsis. Il attend une requête POST contenant les caractéristiques d'un individu au format JSON. Les caractéristiques attendues sont les suivantes : "PRG", "PL", "PR", "SK", "TS", "M11", "BD2", "Age", "Insurance". La fonction predict() de la classe Sepsis est utilisée pour effectuer la prédiction. La prédiction renvoyée est un JSON contenant la classe prédite ("Négatif" ou "Positif") et la probabilité associée à la prédiction.

Endpoint /health - Ce point de terminaison permet de vérifier l'état de l'API. Il renvoie simplement un JSON contenant la réponse "Okay".

Authentification
L'API utilise une authentification basée sur les jetons d'accès. Le jeton d'accès doit être inclus dans l'en-tête "Authorization" de chaque requête. Par défaut, le jeton d'accès valide est défini comme "lesecret". Vous pouvez personnaliser la logique de validation du jeton d'accès en implémentant la fonction validate_token() dans le fichier index.py.

Décorateur require_token
Le décorateur require_token est utilisé pour vérifier si le jeton d'accès est valide avant d'exécuter les fonctions des points de terminaison. Si le jeton d'accès est invalide ou manquant, une erreur 401 Unauthorized est renvoyée.

Classes et fonctions
Le code backend est organisé en plusieurs classes et fonctions. Voici une description des principales :

Classe Sepsis : Cette classe gère les prédictions de sepsis. Elle dispose des méthodes suivantes :

__init__(): Initialise l'instance de la classe.
predict(model_name, data): Effectue la prédiction de sepsis en utilisant le modèle spécifié par model_name et les données d'entrée fournies dans data.
health(): Renvoie l'état de santé de l'API.
Fonction validate_token(token): Cette fonction vérifie si un jeton d'accès est valide. Elle peut être personnalisée pour implémenter la logique de validation du jeton d'accès.

Décorateur require_token(func): Ce décorateur est utilisé pour vérifier le jeton d'accès avant d'exécuter une fonction. Il renvoie une erreur 401 Unauthorized si le jeton est invalide ou manquant.

Exécution des tests
Le fichier testSepsis.py contient des tests unitaires pour vérifier le bon fonctionnement des différentes fonctions de la classe Sepsis. Vous pouvez exécuter ces tests en exécutant le fichier avec la commande suivante :

Copy code
python testSepsis.py
Assurez-vous d'avoir les dépendances nécessaires installées avant d'exécuter les tests.

Note importante
La documentation fournie ici est générée automatiquement à partir du code source. Elle peut être incomplète ou nécessiter des ajustements pour correspondre à la logique réelle de votre application. Il est recommandé de la mettre à jour et de l'adapter en fonction des besoins spécifiques de votre projet.
