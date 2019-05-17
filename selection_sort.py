import cv2
import numpy as np
from matplotlib import cm
import math
import tqdm
'''
Selection sort visualizer by Kaelan Moffett-Steinke.
Generates 'selection_sort.avi' using openCV's VideoWriter.
Inspired by these gifs
https://imgur.com/gallery/voutF
'''

# width and height are for the matrix of pixels that gets sorted and by extension the video resolution
width = 200
height = 200
writer = cv2.VideoWriter("output.avi", cv2.VideoWriter_fourcc(*"MJPG"), 60, (width, height))
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

for i in range(mat.shape[1]):
    # Write frame
    if (i % 1 == 0):
        writer.write(mat_hsv.copy().astype('uint8'))

    # Do a pass
    # loop through rows
    for j in range(i, mat.shape[0]):
        #writer.write(mat_hsv.copy().astype('uint8'))
        base = mat[j, i]
        base_hsv = mat_hsv[j, i].copy()
        minim = base
        minim_hsv = mat_hsv[j, i].copy()
        min_j = j
        min_k = i
        for k in range(i, mat.shape[1]):
            if mat[j, k] < minim:
                minim = mat[j, k].copy()
                minim_hsv = mat_hsv[j, k].copy()
                min_j = j
                min_k = k
        mat[j, i] = minim
        mat_hsv[j, i] = minim_hsv
        mat[min_j, min_k] = base
        mat_hsv[min_j, min_k] = base_hsv
t.update()
t.close()
writer.release()
