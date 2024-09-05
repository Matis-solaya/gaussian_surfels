import cv2
import numpy as np
from pathlib import Path
import tyro

def show_image_and_normal(img_path:Path):

    img = cv2.imread(str(img_path))
    normal_path = img_path.parent.parent / "normal" / f"{img_path.stem}_normal.npy"
    normal = np.load(normal_path)

    concat = np.concatenate(
        [
            img / 255.0,
            np.abs(normal[0].transpose(1,2,0)[...,::-1])
        ],
        axis=1,
    )
    vis = cv2.resize(concat, (concat.shape[1]//6, concat.shape[0]//6))
    cv2.imshow(f"{img_path}", vis)
    cv2.waitKey(0)
    cv2.imwrite(f"{img_path.stem}.png", concat*255)


if __name__ == "__main__":
    tyro.cli(show_image_and_normal)
