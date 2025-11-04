Results produced by running `notebooks/pierre/MLT_AE_experiments.ipynb`

Files generated (path relative to repo root `results/`):

- metrics_summary.json
  - JSON summary with OOD accuracy and confusion matrices for `baseline`, `mtl`, and `softshare` models.

- training_curves.png
  - Side-by-side training/validation loss plots for baseline and MTL.

- cm_baseline.png, cm_mtl.png, cm_softshare.png
  - Confusion matrix heatmaps for each model.

- recon_mtl.png, recon_softshare.png
  - Input / reconstruction grids for MTL and SoftShare models (if reconstruction functions available).

- examples_<ClassName>.png
  - Small montages with up to 6 example images per class from the training set.

- class_counts.png
  - Bar chart of class counts in the training set.

How these were produced
- The notebook was run on a local Apple M4 (PyTorch MPS). The notebook cells created a `results/` directory and saved the artifacts above.
- Checkpoints were saved as `cnn_baseline.pt`, `mtl_cnn.pt`, `softshare_mtl.pt` in the notebook working directory (repo root).

Suggested next steps
- If you want a single ZIP with all assets (for slides or sharing), I can create `results.zip` containing the `results/` folder and the three checkpoints.
- I can also prepare a Colab-ready notebook that mounts Drive and writes checkpoints to Drive for longer runs on CUDA GPUs.
- If you want nicer figures for slides (vector PDF, larger DPI), I can re-export with higher resolution or create a single slide-ready PDF.

Tell me which of the suggested next steps you'd like me to do (create ZIP, Colab-ready notebook, or high-res exports).