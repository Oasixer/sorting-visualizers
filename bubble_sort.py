import cv2
import numpy as np
from matplotlib import cm
import math
import tqdm
'''
Bubble sort visualizer by Kaelan Moffett-Steinke.
Generates 'bubble_sort.avi' using openCV's VideoWriter.
Inspired by these gifs
https://imgur.com/gallery/voutF
'''

# width and height are for the matrix of pixels that gets sorted and by extension the video resolution
width = 200
height = 200
writer = cv2.VideoWriter("bubble_sort.avi", cv2.VideoWriter_fourcc(*"MJPG"), 60, (width, height))
mat = np.zeros((height, width))
one_row = np.linspace(0, 255, num=width)

for row in range(height):
    np.random.shuffle(one_row)
    mat[row] = one_row.copy()

mat_hsv = np.random.randint(0, 1, (height, width, 3))

# Note:
# mat.shape()[0] == nRows, mat.shape()[1] == nCols
for row in range(mat.shape[0]):
    for col in range(mat.shape[1]):
        not_rgb = cm.viridis(int(mat[row, col]))
        mat_hsv[row, col, 0] = int(math.ceil(not_rgb[0] * 255))
        mat_hsv[row, col, 1] = int(math.ceil(not_rgb[1] * 255))
        mat_hsv[row, col, 2] = int(math.ceil(not_rgb[2] * 255))

# Note:
# mat.shape()[0] == nRows, mat.shape()[1] == nCols
num_samples = mat.shape[1]  # Num samples for ETA
t = tqdm.tqdm(
    total=num_samples,
    dynamic_ncols=True,
    leave=False,
    bar_format=
    '{l_bar}{bar}|[Elapsed: {elapsed}][Remaining: {remaining}][Samples: {n_fmt}/{total_fmt}][{rate_fmt}{postfix}]'
)
for col in range(mat.shape[1]):
    for col_offset in range(mat.shape[1] - 1 - col):
        # Write frame
        if (col_offset % 1 == 0):
            writer.write(mat_hsv.copy().astype('uint8'))
        for row in range(mat.shape[0]):
            base = mat[row, col_offset]
            base_hsv = mat_hsv[row, col_offset].copy()
            k = col_offset + 1
            if mat[row, k] > base:
                mat[row, col_offset] = mat[row, k]
                mat[row, k] = base
                mat_hsv[row, col_offset] = mat_hsv[row, k].copy()
                mat_hsv[row, k] = base_hsv
    t.update()
t.close()
writer.release()
