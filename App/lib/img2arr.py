import numpy as np
import matplotlib.image as mimg

# Image initialization
def __rgba2rgb(img):
    height, width, _ = img.shape
    rgb_img_arr = np.zeros(shape=(height, width, 3))

    for i in range(height):
        for j in range(width):
            for k in range(3):
                rgb_img_arr[i, j, k] = img.item((i, j, k))

    return rgb_img_arr


# 0.299R + 0.587G + 0.114B.
def __rgb2gray(img):
    height, width, _ = img.shape
    gray_img_arr = np.zeros(shape=(height, width))

    for i in range(height):
        for j in range(width):
            r_gray = img.item((i, j, 0)) * 0.299
            g_gray = img.item((i, j, 1)) * 0.587
            b_gray = img.item((i, j, 2)) * 0.114

            gray_img_arr[i, j] = r_gray + g_gray + b_gray

    return gray_img_arr


def get_image(path, ignore_alpha = True):
    img = mimg.imread(path)

    if path.endswith('.jpg') or path.endswith('.tif') or path.endswith('.jpeg'):
        return img / 255 
        
    elif path.endswith('.png') and ignore_alpha:
        return __rgba2rgb(img)

    return img