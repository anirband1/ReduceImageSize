# ReduceImageSize
Dedicated to image size reduction methods without a loss in quality

### There are 3 ways to resize an image in this repo.

- Flat Shading
- Pixelating
- Resizing

------------------------------
In flat shading, the values of the pixel are rounded off to the nearest multiple of a given number, giving it a feeling of 'flatness'.


This works great for preserving detail and reducing size.
It's downside is that it makes gradients a bit chunkier.

In main.py, change FLAT_AMOUNT in the range of 1 (has no effect) to 255 (beyond this, the image becomes 1 color)

------------------------------
For pixelating an image, a grid of pixels are assigned the average color of those pixels.

Pixelating has pretty much the opposite effect from flat shading where it works great on gradients but loses detail in the image.

In main.py, change PIXELATE_AMOUNT in the range of 1 (has no effect) to the image dimensions (after which the image becomes 1 color)

------------------------------
Finally, resizing is much the easiest way of reducing the size of an image.

In main.py, change RESIZE_AMOUNT where values from 0-1 scale the image down and values > 1 scale it up.

For maintaining aspect ratio and reducing the size, set PRESERVE_ASPECT_RATIO to True

##
------------------------------

For images of ~ 6000x6000 and above, the following values produce the best results:

FLAT_AMOUNT : 30 - 40
PIXELATE_AMOUNT : 1 - 2
RESIZE_AMOUNT : 0.6 - 0.4
