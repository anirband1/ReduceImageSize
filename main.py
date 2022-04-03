import os
import matplotlib.pyplot as plt
from App.lib.core_func import process
from App.lib.img2arr import get_image

FLAT_AMOUNT = 37                # Integer (Avoid with gradients)            drastic above ~ 32
RESIZE_AMOUNT = 0.5             # Float (Avoid with VERY FINE detail)       drastic below ~ 0.6
PIXELATE_AMOUNT = 1             # Integer (Avoid with images in the range of 900x900 or below)

PRESERVE_ASPECT_RATIO = False   # Set to true to preserver the original image's aspect ratio

for img_name in os.listdir('Input Images'):

    if img_name.endswith('png' or 'jpg' or 'jpeg' or 'tiff'):
        path_to_img = os.path.join('Input Images', img_name)

        img = get_image(path_to_img)
        plt.imsave(f'Output Images/{img_name.split(".")[0]} Edited.png', process(img,
                                                                flat_amt=FLAT_AMOUNT,
                                                                resize_amt=RESIZE_AMOUNT,
                                                                pixelate_amt=PIXELATE_AMOUNT,
                                                                maintain_aspect_ratio=PRESERVE_ASPECT_RATIO))


