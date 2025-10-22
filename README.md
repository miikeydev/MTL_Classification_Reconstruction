# MTL — Classification & Reconstruction

**Objective:**
Train a single CNN to perform **two tasks simultaneously** — **land-use classification** (Forest vs Residential) and **image reconstruction** — to study how **Multi-Task Learning (MTL)** improves generalization and reduces overfitting.

---

## Dataset

Dataset: [**EuroSAT RGB**](https://www.kaggle.com/datasets/waseemalastal/eurosat-rgb-dataset)
Only **Forest** and **Residential** classes are included.
Download manually and place in:

```
data/
├─ Forest/
└─ Residential/
```

---

## Experiments

Each member has their own notebook folder for experiments:

```
notebooks/
├─ alexi/
├─ houssem/
├─ mahouna/
└─ pierre/
```

Use these as playgrounds to test preprocessing, models, or training ideas.
If needed later, results can be centralized into a main training script.