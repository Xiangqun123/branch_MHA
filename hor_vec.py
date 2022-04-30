import numpy as nm
import numpy as np

from MHA.MHA_code.read_dataset import *

def hor_vec():
    anno_ls = read_x_anno('hor')
    W = 2688 # width
    # for frame_anno in anno_ls:
    #     frame_anno[:, 0] = (frame_anno[:, 0] + frame_anno[:, 2]-W)/W
    #     frame_anno[:, 1] = 1/(frame_anno[:, 3] - frame_anno[:, 1])
    #     frame_anno = np.delete(frame_anno, [2,3], axis=1)

    for i in range(len(anno_ls)):
        anno_ls[i][:, 0] = (anno_ls[i][:, 0] + anno_ls[i][:, 2] - W) / W
        anno_ls[i][:, 1] = 1 / (anno_ls[i][:, 3] - anno_ls[i][:, 1])
        anno_ls[i] = np.delete(anno_ls[i], [2,3], axis=1)

    return anno_ls

# for frame_anno in hor_vec():
#     print(frame_anno)