import numpy as np

from . import img2arr


# region RESIZE

def scale_img2factor(target_img, factor):

    c_height, c_width, _ = target_img.shape
    t_height, t_width = int(c_height*factor), int(c_width*factor)

    new_img_arr = np.zeros(shape=(t_height, t_width, 3))

    for i in range(t_height):
        for j in range(t_width):
            for k in range(3):
                new_img_arr[i , j, k] = target_img.item((min(c_height-1, round(i/factor)), min(c_width-1, round(j/factor)), k))
    
    return new_img_arr

def scale_img2img(target_img, control_img):
    c_height, c_width, _ = control_img.shape
    t_height, t_width, _ = target_img.shape

    h_factor = c_height/t_height
    w_factor = c_width/t_width

    new_img_arr = np.zeros(shape=(c_height, c_width, 3))

    for i in range(c_height):
        for j in range(c_width):
            for k in range(3):
                new_img_arr[i , j, k] = target_img.item((min(t_height-1, round(i/h_factor)), min(t_width-1, round(j/w_factor)), k))
    
    return new_img_arr

# endregion

# region PIXELATE

def pixelate(img, pixelate_amount):

    height, width, _ = img.shape

    pixelate_amount = int(pixelate_amount)
    padding = pixelate_amount//2

    new_img_arr = np.zeros(shape=(height, width, 3))

    # finding average color
    _stop = (padding + 1) if pixelate_amount & 1 else padding # in grid

    for i in range(padding, height + padding, pixelate_amount):
        for j in range(padding, width + padding, pixelate_amount):

            total_pixels = 0
            r_total = 0
            g_total = 0
            b_total = 0

            for _i in range(-padding, _stop):
                for _j in range(-padding, _stop):

                    _x = i + _i
                    _y = j + _j

                    if 0<= _x < height and 0 <= _y < width: # and (_x, _y) != (i, j):
                        r_total += img.item((_x, _y, 0))
                        g_total += img.item((_x, _y, 1))
                        b_total += img.item((_x, _y, 2))
                        total_pixels += 1

            color = np.array((r_total, g_total, b_total)) / total_pixels

            # applying color to all pixels
            for _i in range(-padding, _stop):
                for _j in range(-padding, _stop):

                    _x = i + _i
                    _y = j + _j

                    if 0<= _x < height and 0 <= _y < width: # and (_x, _y) != (i, j):
                        new_img_arr[_x, _y] = color

    return new_img_arr

# endregion

# region FLAT SHADE

def flat(img, CM = 15):

    CM = int(CM)
    height, width, _ = img.shape
    new_img_arr = np.zeros(shape=(height, width, 3))

    __div = CM//2

    def int_round(num):
        rem = num % CM
        return num - rem if rem <= __div else num + CM - rem 


    for i in range(height):
        for j in range(width):
            for k in range(3):
                new_img_arr[i, j, k] = int_round(int(img.item((i, j, k)) * 255)) / 255
    
    return np.clip(new_img_arr, 0, 1)

# endregion

def process(img, flat_amt = 1, resize_amt = 1.0, pixelate_amt = 1, maintain_aspect_ratio = False):
    # sourcery skip: inline-immediately-returned-variable
    
    if 0 in (flat_amt, resize_amt, pixelate_amt):
        return img

    # flat -> pixelate -> resize

    flat_img = flat(img, flat_amt) if flat_amt != 1 else img
    pixelate_img = pixelate(flat_img, pixelate_amt) if pixelate_amt != 1 else flat_img
    resize_img = scale_img2factor(pixelate_img, resize_amt) if resize_amt != 1 else pixelate_img

    if maintain_aspect_ratio:
        resize_img = scale_img2img(resize_img, img)

    return resize_img

