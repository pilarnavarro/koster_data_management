# Author: J. Germishuys
# Creation date: 28/01/2022

import os
import math
from tqdm import tqdm
import argparse
import numpy as np
import cv2 as cv
from pathlib import Path
from itertools import product
from patchify import patchify, unpatchify


def run_patchify(folder_path, patch_size: list = [540, 720]):
    """
    Given an image, it will create a folder named after the image with all the patches of the image.

    :param folder_path: the path to the folder containing the images
    :param patch_size: list = [540, 720]
    :type patch_size: list
    """
    for img in tqdm(os.listdir(folder_path)):
        print("Processing", img)
        try:
            image = cv.imread(str(Path(folder_path, img)))[:, :, ::-1]
            image = cv.resize(
                image,
                (
                    math.floor(image.shape[0] / 100) * 100,
                    math.floor(image.shape[1] / 100) * 100,
                ),
            )

            # Optional: Remove blur and equalise histogram across image
            # sharpen_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
            # image = cv.filter2D(image, -1, sharpen_kernel)
            # image = run_histogram_equalization(image)

            patches = patchify(
                image, (patch_size[0], patch_size[1], 3), step=patch_size[1]
            )  # patch shape [540,720,3]
            print(f"You are creating {patches.shape[0]*patches.shape[1]} patches")

            patch_path = (
                f"{Path(os.path.dirname(folder_path), os.path.basename(folder_path))}"
                + "_patches"
            )
            if not os.path.exists(patch_path):
                os.mkdir(patch_path)

            combinations = product(
                list(np.arange(patches.shape[0])), list(np.arange(patches.shape[1]))
            )
            for row, col in combinations:
                patch = patches[row][col][0]
                img_fn, ext = os.path.splitext(img)
                cv.imwrite(f"{patch_path}/{img_fn}_patch_{row}_{col}.jpg", patch)

        except:
            print(f"Failed patching of  {str(Path(folder_path, img))}")

        # Optional: reconstruction of patches
        # assert patches.shape == (3647, 5471, 1, 2, 2, 3)
        # reconstructed_image = unpatchify(patches, image.shape)
        # print(reconstructed_image.shape) # (512, 512, 3)
        # assert (reconstructed_image == image).all()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Patches large image into smaller images for upload to Citizen Science platform."
    )
    parser.add_argument(
        "-f",
        "--folder_path",
        help="Folder path containing images to be converted to patches",
        required=True,
    )
    parser.add_argument("-ps", "--patch_size", nargs="+", type=int, default=[540, 720])
    args = vars(parser.parse_args())
    run_patchify(args["folder_path"], args["patch_size"])
    print(
        f"Output saved to {Path(os.path.dirname(args['folder_path']), os.path.basename(args['folder_path']))}"
        + "_patches"
    )
