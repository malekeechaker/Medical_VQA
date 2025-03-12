# Medical Visual Question Answering (VQA)

## Description
Ce projet implémente un système de VQA (Visual Question Answering) spécialisé en imagerie médicale. Il permet de répondre automatiquement à des questions posées sur des images médicales en utilisant des modèles d'intelligence artificielle.

## Installation
1. Clonez le dépôt :
   ```bash
   git clone https://github.com/votre-repo/medical-vqa.git
   cd medical-vqa
   ```
2. Créez un environnement virtuel et installez les dépendances :
   ```bash
   python -m venv vqa_env
   source vqa_env/bin/activate  # Sur Windows : vqa_env\Scripts\activate
   pip install -r requirements.txt
   ```

## Utilisation
1. Lancez le script principal :
   ```bash
   python main.py --image path/to/image.jpg --question "Quel est le diagnostic ?"
   ```
2. Exemple de sortie :
   ```bash
   Réponse : Pneumonie détectée.
   ```

## Données Utilisées
Le modèle a été entraîné sur des bases de données d'images médicales contenant des annotations validées par des experts.

## Modèle d'IA
- Utilisation d'un modèle basé sur **Vision Transformer (ViT)** pour l'analyse d'images.
- **BERT** pour le traitement du langage naturel et la compréhension des questions.
- Entraînement réalisé avec **PyTorch** et **Hugging Face Transformers**.

## Résultats
Le modèle atteint une précision de **85%** sur un ensemble de tests médicaux.

## Contributeurs
- **Votre Nom** - Développement et entraînement du modèle
- **Autres contributeurs** (si applicable)

## Licence
Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

