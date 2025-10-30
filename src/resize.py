import os
from PIL import Image

ROOT = "data/OOD"
TARGET_SIZE = (64, 64)
EXT = (".jpg", ".jpeg", ".png")

def resize_images():
    for cls in ["Forest", "DenseResidential", "MediumResidential"]:
        folder = os.path.join(ROOT, cls)
        if not os.path.exists(folder):
            continue
        for f in os.listdir(folder):
            if f.lower().endswith(EXT):
                path = os.path.join(folder, f)
                try:
                    img = Image.open(path).convert("RGB")
                    if img.size != TARGET_SIZE:
                        img = img.resize(TARGET_SIZE, Image.BILINEAR)
                        img.save(path)
                except Exception as e:
                    print(f"Erreur {f}: {e}")

if __name__ == "__main__":
    resize_images()
    print("Redimensionnement terminé.")
