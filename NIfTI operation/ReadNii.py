mport numpy as np
import os
import nibabel as nib
import imageio  # transfer nii to image
from PIL import Image


def read_nii_image(niifile):
    for root, dirs, files in os.walk(niifile):
        for file in files:
            if '.nii.gz' in file and '.png' not in file:
                savePathAX = os.path.join(root, file.replace('.nii.gz', '_AX'))
                savePathSAG = os.path.join(
                    root, file.replace('.nii.gz', '_SAG'))
                savePathCOR = os.path.join(
                    root, file.replace('.nii.gz', '_COR'))
                fileName = file.replace('.nii.gz', '')
                if not os.path.isdir(savePathAX):
                    os.mkdir(savePathAX)
                if not os.path.isdir(savePathSAG):
                    os.mkdir(savePathSAG)
                if not os.path.isdir(savePathCOR):
                    os.mkdir(savePathCOR)

                # read nii files
                img_path = os.path.join(root, file)
                img = nib.load(img_path)
                img_fdata = img.get_fdata()

                # transfer nii2png
                (x, y, z) = img.shape
                for i in range(z):
                    slice = img_fdata[:, :, i]
                    print(file)
                    imageio.imwrite(os.path.join(
                        savePathAX, '{}.png'.format(i)), slice)

                for i in range(y):
                    slice = img_fdata[:, i, :]
                    print(file)
                    imageio.imwrite(os.path.join(
                        savePathCOR, '{}.png'.format(i)), slice)

                for i in range(x):
                    slice = img_fdata[i, :, :]
                    print(file)
                    imageio.imwrite(os.path.join(
                        savePathSAG, '{}.png'.format(i)), slice)


if __name__ == '__main__':
    read_nii_image(
        r'C:\Users\RTX 3090\Desktop\WangYichong\Data\Masks\Multi-Institutional Paired Expert Segmentations SRI images-atlas-annotations')
    read_nii_image(
        r'C:\Users\RTX 3090\Desktop\WangYichong\Data\Masks\Multi-institutional Paired Expert Segmentations MNI images-atlas-annotations')