# Projet application web médicale pour detecter la septicémie

**Objectif** :
Mise en place d'une application web destinée au domaine médical pour prédire la septicémie basée sur un modèle de machine learning, optimisé à plusieurs reprises.

**Composants du Projet** :
- **Front-end** : Conception de l'interface utilisateur.
- **API Backend** :
  - Fondé sur le framework Flask.
  - Offre une prédiction de septicémie en utilisant des données spécifiques d'un individu.
  - Les données nécessaires sont : "PRG", "PL", "PR", "SK", "TS", "M11", "BD2", "Age", "Insurance".
  - Les réponses incluent la prédiction ("Négatif" ou "Positif") et la probabilité associée.
  - L'API utilise une authentification basée sur des jetons.

**Installation** :
1. Installez les dépendances avec la commande :
pip install flask pandas joblib
2. Lancez l'API en exécutant :
python index.py

**Fonctionnalités de l'API** :
- **/predict** : Reçoit une requête POST au format JSON pour prédire la septicémie.
- **/health** : Vérifie l'état de l'API.

**Authentification** :
- Utilisation de jetons d'accès.
- Le jeton par défaut est "lesecret", mais peut être personnalisé.

**Structure du Code Backend** :
Classe Sepsis : Gère les prédictions. Comprend :
- `predict(model_name, data)` : Pour faire des prédictions.
- `health()` : Pour obtenir l'état de l'API.

Fonction `validate_token(token)` : Vérifie la validité d'un jeton d'accès.

Décorateur `require_token` : Assure que le jeton d'accès est valide avant l'exécution.

**Tests** :
Des tests unitaires sont disponibles dans testSepsis.py. Exécutez avec :
python testSepsis.py
