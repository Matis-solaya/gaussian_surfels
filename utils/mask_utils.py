import tyro
from pathlib import Path
from PIL import Image
import numpy as np
from tqdm import tqdm

def mask_images(path_images:Path, path_masks:Path, output:Path):
    """Apply masks on images"""
    p_images = path_images.glob("*.png")
    for p in tqdm(p_images):
        image = np.asarray(Image.open(p))/255.0
        p_m = path_masks / f"{p.stem}{p.suffix}{p.suffix}"
        mask = np.asarray(Image.open(p_m))/255.0
        masked = Image.fromarray((image * mask *255).astype(np.uint8))
        masked.save(output /f"{p.stem}{p.suffix}")



if __name__=="__main__":
    tyro.cli(mask_images)

