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
                imagePath = os.path.join(root, file.replace('.nii.gz', ''))
                maskPath = os.path.join(root, file.replace('.nii.gz', '_masks'))
                # read nii files
                img_path = os.path.join(root, file)
                img = nib.load(img_path)
                img_fdata = img.get_fdata()

                # transfer nii2png
                (x, y, z) = img.shape
                for i in range(x):
                    slice = img_fdata[i, :, :]
                    if 'masks' in file:
                        imageio.imwrite(os.path.join(maskPath, '{}_{}.png'.format(file.split('.',1)[0].replace('_masks',''),i)),slice)
                    else:
                        imageio.imwrite(os.path.join(imagePath, '{}_{}.png'.format(file.split('.',1)[0],i)),slice)

if __name__ == '__main__':
    pass