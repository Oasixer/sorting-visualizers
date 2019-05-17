import cv2
import numpy as np
from matplotlib import cm
import math
import tqdm

width = 200
height = 200
writer = cv2.VideoWriter("output.avi", cv2.VideoWriter_fourcc(*"MJPG"), 60, (width, height))
# might need to be
mat = np.zeros((height, width))
# (rows, cols, channels)
one_row = np.linspace(0, 255, num=width)

for row in range(height):
    np.random.shuffle(one_row)
    mat[row] = one_row.copy()

#mat = np.array(np.random.shuffle(_row.copy().)

# below might need to be height, width
mat_hsv = np.random.randint(0, 1, (height, width, 3))

for work in range(mat.shape[0]):
    for fuck in range(mat.shape[1]):
        not_rgb = cm.viridis(int(mat[work, fuck]))
        mat_hsv[work, fuck, 0] = int(math.ceil(not_rgb[0] * 255))
        mat_hsv[work, fuck, 1] = int(math.ceil(not_rgb[1] * 255))
        mat_hsv[work, fuck, 2] = int(math.ceil(not_rgb[2] * 255))

# numpything.shape()[0] == rows
num_samples = mat.shape[1]
t = tqdm.tqdm(
    total=num_samples,
    dynamic_ncols=True,
    leave=False,
    bar_format=
    '{l_bar}{bar}|[Elapsed: {elapsed}][Remaining: {remaining}][Samples: {n_fmt}/{total_fmt}][{rate_fmt}{postfix}]'
)
for retarded in range(mat.shape[1]):
    for i in range(mat.shape[1] - 1 - retarded):
        # Write frame
        if (i % 1 == 0):
            writer.write(mat_hsv.copy().astype('uint8'))
        # Do a pass
        # loop through rows
        for j in range(mat.shape[0]):
            base = mat[j, i]
            base_hsv = mat_hsv[j, i].copy()
            #minim = base
            #minim_hsv = mat_hsv[j, i].copy()
            #min_j = j
            #min_k = i
            #for k in range(i, mat.shape[1]):
            k = i + 1
            if mat[j, k] > base:
                mat[j, i] = mat[j, k]
                mat[j, k] = base
                mat_hsv[j, i] = mat_hsv[j, k].copy()
                mat_hsv[j, k] = base_hsv

                #minim = mat[j, k].copy()
                #minim_hsv = mat_hsv[j, k].copy()
                #min_j = j
                #min_k = k
            # for loop ends here
            #mat[j, i] = minim
            #print(minim_hsv)
            #mat_hsv[j, i] = minim_hsv
            #mat[min_j, min_k] = base
    t.update()
t.close()
writer.release()
