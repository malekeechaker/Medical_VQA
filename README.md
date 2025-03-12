# Medical Visual Question Answering (VQA)

## Description
Ce projet implémente un système de VQA (Visual Question Answering) spécialisé en imagerie médicale. Il permet de répondre automatiquement à des questions posées sur des images médicales en utilisant des modèles d'intelligence artificielle.

## Installation
1. Clonez le dépôt :
   ```bash
   git clone https://github.com/malekeechaker/Medical-VQA.git
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
The BLIP model was proposed in BLIP: Bootstrapping Language-Image Pre-training for Unified Vision-Language Understanding and Generation by Junnan Li, Dongxu Li, Caiming Xiong, Steven Hoi.

BLIP is a model that is able to perform various multi-modal tasks including: 

- Visual Question Answering
- Image-Text retrieval (Image-text matching)
- Image Captioning
- The abstract from the paper is the following:

Vision-Language Pre-training (VLP) has advanced the performance for many vision-language tasks. However, most existing pre-trained models only excel in either understanding-based tasks or generation-based tasks. Furthermore, performance improvement has been largely achieved by scaling up the dataset with noisy image-text pairs collected from the web, which is a suboptimal source of supervision. In this paper, we propose BLIP, a new VLP framework which transfers flexibly to both vision-language understanding and generation tasks. BLIP effectively utilizes the noisy web data by bootstrapping the captions, where a captioner generates synthetic captions and a filter removes the noisy ones. We achieve state-of-the-art results on a wide range of vision-language tasks, such as image-text retrieval (+2.7% in average recall@1), image captioning (+2.8% in CIDEr), and VQA (+1.6% in VQA score). BLIP also demonstrates strong generalization ability when directly transferred to videolanguage tasks in a zero-shot manner. Code, models, and datasets are released.
