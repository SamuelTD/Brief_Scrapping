# BricoScrapping

BricoScrapping est un projet de scrapping conçu pour extraire des informations sur les catégories et les produits du site [Bricodepot](https://www.bricodepot.fr). Ce projet utilise le framework Scrapy et comprend deux spiders : 

1. **bricospider_categories** : collecte les catégories et sous-catégories du site.
2. **bricospider_product** : extrait les détails des produits à partir des catégories.

---

## Fonctionnalités

### bricospider_categories
- Récupère toutes les catégories et sous-catégories disponibles sur le site.
- Identifie si une page contient une liste de produits.
- Enregistre les informations sous forme d'objets `CategoryItem` (nom, URL, et si la page contient une liste de produits).

### bricospider_product
- Explore les pages des catégories pour extraire les informations des produits.
- Gère les paginations pour couvrir toutes les pages d'une catégorie.
- Extrait les détails comme le nom, le prix, la référence produit, le code produit, et la marque.

---

## Installation

1. Clonez ce dépôt sur votre machine locale :
   ```bash
   git clone https://github.com/votre-utilisateur/bricoscrapping.git
   cd bricoscrapping

2. Installez les dépendances nécessaires dans un environnement virtuel Python :
    ```bash
    python -m venv venv
    source venv/bin/activate  # Sur Windows : venv\Scripts\activate
    pip install -r requirements.txt

3. Configurez vos paramètres Scrapy si nécessaire dans le fichier settings.py.

## Structure du Projet
    bricoscrapping/
    │
    ├── bricoscrapping/
    │   ├── __init__.py
    │   ├── items.py           # Définitions des items Scrapy
    │   ├── middlewares.py     # Middlewares Scrapy
    │   ├── pipelines.py       # Pipelines pour le traitement des données extraites
    │   ├── settings.py        # Configuration Scrapy
    │   ├── spiders/
    │   │   ├── __init__.py
    │   │   ├── bricospider_categories.py  # Spider pour les catégories
    │   │   ├── bricospider_product.py     # Spider pour les produits
    │
    ├── requirements.txt       # Liste des dépendances
    └── README.md              # Documentation du projet```

---

## Structure du Projet
**Lancer les Spiders**

1. Pour les catégories 
Exécutez la commande suivante pour lancer le spider ```bricospider_categories``` et collecter les catégories :
    ```bash 
    scrapy crawl bricospider_categories -o categories.json
Cela sauvegardera les données dans un fichier JSON nommé ```categories.json```.
2. Pour les produits :
Exécutez la commande suivante pour lancer le spider ```bricospider_product``` :
    ```bash 
    scrapy crawl bricospider_categories -o products.json

Cela sauvegardera les détails des produits dans un fichier JSON nommé ```products.json```.

---

## Licence
Ce projet est sous licence MIT. 

---

## Auteur
Samuel Thorez-Debrucq
GitHub : https://github.com/SamuelTD