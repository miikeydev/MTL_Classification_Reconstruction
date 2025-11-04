# Résultats — MTL vs Baseline

## Titre
MTL vs Baseline — Résultats clés (Forest vs Residential)

## Slide (contenu concis pour la diapositive)
- Dataset : Forest vs Residential (images 64×64)
- Mesure OOD (ensemble externe) — accuracy globale :
  - Baseline CNN : 0.733
  - MTL : 0.583
  - SoftShare : 0.508
- Matrices de confusion (extraits) : voir images `results/cm_baseline_highres.png`, `results/cm_mtl_highres.png`, `results/cm_softshare_highres.png`
- Takeaway principal : les modèles multitâches (MTL / SoftShare) n'améliorent pas l'acc OOD pour la classe Forest ; au contraire, ils réduisent la capacité à reconnaître Forest sur l'ensemble OOD.

## Interprétation rapide des matrices de confusion
- Baseline :
  - True Forest (0) → prédictions : 29 correctes, 31 erreurs (prédits Residential)
  - True Residential (1) → prédictions : 1 erreur, 59 correctes
  => Baseline confond beaucoup Forest → Residential en OOD.
- MTL :
  - True Forest : 11 correctes, 49 erreurs
  - True Residential : 1 erreur, 59 correctes
  => MTL aggrave la confusion sur Forest (moins d'exemples correctement reconnus).
- SoftShare :
  - True Forest : 1 correct, 59 erreurs
  - True Residential : 0 erreurs, 60 correctes
  => SoftShare prédit quasiment toujours Residential sur l'OOD (effondrement sur Forest).

## Slide visuel recommandé
- Gauche : `results/training_curves_highres.png` (courbes train/val)
- Centre : `results/cm_baseline_highres.png` (confusion baseline)
- Droite : `results/cm_mtl_highres.png` et/ou `results/cm_softshare_highres.png` (comparaison)
- Bas de diapo : une ligne avec les chiffres d'acc OOD (voir plus haut) et un court takeaway en rouge : "Forest OOD fortement dégradé — déséquilibre / shift probable".

## Notes pour l'orateur (bullet points)
- Rappeler la distinction entre accuracy in-domain (validation) et OOD : ici, les modèles atteignent une bonne val in-domain mais chutent hors distribution.
- Montrer la matrice baseline pour illustrer que Forest est souvent classé Residential → expliquer visuellement ce que cela signifie (ex : exemples visuels s'il y a le temps).
- Souligner que MTL/SoftShare n'apportent pas d'amélioration OOD ici — hypothèses :
  1. déséquilibre de classes et représentation insuffisante de Forest
  2. covariate shift (différence de capture/coverage entre train et OOD)
  3. les losses multitâches favorisent la reconstruction / features partagées qui n'aident pas la séparation Forest vs Residential sur OOD
- Recommandations rapides : échantillonnage équilibré (oversample Forest), augmenter augmentations spécifiques à Forest, fine-tuning sur quelques exemples OOD, ou tester adaptation de domaine (simple style augmentation, color jitter, ou domain adversarial fine-tune).

## Actions techniques rapides (si vous voulez regénérer les images avant la présentation)
1. Ouvrir le notebook `notebooks/pierre/MLT_AE_experiments.ipynb` et exécuter les cellules de la section "Visualisations & diagnostics" (elles sauvegardent dans `results/`).
2. Vérifier que les fichiers suivants existent et sont récents :
   - `results/training_curves_highres.png`
   - `results/cm_baseline_highres.png`, `results/cm_mtl_highres.png`, `results/cm_softshare_highres.png`
   - `results/recon_mtl_highres.png`, `results/recon_softshare_highres.png` (optionnel)
3. Si besoin de zippage : le notebook produit `results_slide.zip` contenant les assets high-res.

## Résumé (1 phrase)
Les modèles multitâches n'améliorent pas la robustesse OOD sur la classe Forest — la diapositive mettra l'accent sur la forte confusion Forest→Residential et propose des pistes d'actions concrètes (échantillonnage, augmentations, fine-tuning OOD).

---
*Fichier généré automatiquement par l'assistant — modifiez librement avant la présentation.*
