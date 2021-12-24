import numpy as np
import os
import nibabel as nib
import imageio  # transfer nii to image
from PIL import Image
import torch


def read_nii_image(niifile):
    for root, dirs, files in os.walk(niifile):
        for file in files:
            if '.nii.gz' in file:
                savePath = os.path.join(root, file.replace('.nii.gz', ''))
                os.mkdir(savePath)
                # read nii files
                img_path = os.path.join(root, file)
                img = nib.load(img_path)
                img_fdata = img.get_fdata()

                # transfer nii2png
                (x, y, z) = img.shape
                for i in range(x):
                    slice = img_fdata[i, :, :]
                    imageio.imwrite(os.path.join(savePath, '{}_{}.png'.format(file, i)),slice)

if __name__ == '__main__':
    read_nii_image(r'example')