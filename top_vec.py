from MHA.MHA_code.read_dataset import *
import math
from MHA.MHA_code.util import angle

# O_loc = [1986,144,2082,229]
test_v = [1900, 0]
O_loc = [2034, 186.5]
a = math.pi/4 # a value


def top_vec(O_loc ,v_loc):


    OV_vec = O_loc + v_loc
    anno_ls = read_x_anno('top')
    W = 2688 # width
    H = 1512



    for i in range(len(anno_ls)):
        anno_ls[i][:, 0] = (anno_ls[i][:, 0] + anno_ls[i][:, 2]) / 2
        anno_ls[i][:, 1] = (anno_ls[i][:, 3] + anno_ls[i][:, 1]) / 2
        for j in range(anno_ls[i].shape[0]):
            OP_vec = O_loc+ [anno_ls[i][j,0], anno_ls[i][j,1]]


            # print(OP_vec)
            # print(math.cos(angle(OV_vec,OP_vec)),math.sin(angle(OV_vec,OP_vec)))
            # if(math.cos(angle(OV_vec,OP_vec))==1 and math.sin(angle(OV_vec,OP_vec)) == 0):
            #     print(i,j)


            anno_ls[i][j,0] = (math.cos(angle(OV_vec,OP_vec))/math.sin(angle(OV_vec,OP_vec)))/(math.cos(a)/math.sin(a))
            # print(np.linalg.norm(OP_vec, ord=2))
            anno_ls[i][j, 1] = np.linalg.norm(OP_vec,ord=2)*math.sin(angle(OV_vec,OP_vec))




        anno_ls[i] = np.delete(anno_ls[i], [2,3], axis=1)



    return anno_ls
#
# for frame_anno in top_vec(O_loc,test_v):
#     print(frame_anno)

def top_vec_1():
    return top_vec_2(O_loc[0],O_loc[1],0)


def top_vec_2(cam_locx, cam_locy, angle1):
    # angle1 =180
    angle1_re = angle1+0.00000001
    OV_vec = [cam_locx,cam_locy,cam_locx+100*math.cos(angle1_re*math.pi/180),cam_locy+100*math.sin(angle1_re*math.pi/180)]


    anno_ls = read_x_anno('top')
    W = 2688  # width
    H = 1512

    O_loc = [cam_locx,cam_locy]

    for i in range(len(anno_ls)):
        anno_ls[i][:, 0] = (anno_ls[i][:, 0] + anno_ls[i][:, 2]) / 2
        anno_ls[i][:, 1] = (anno_ls[i][:, 3] + anno_ls[i][:, 1]) / 2
        for j in range(anno_ls[i].shape[0]):
            OP_vec = O_loc+ [anno_ls[i][j,0], anno_ls[i][j,1]]
            # print("这是第%s帧第%s个构造向量"%(str(i+1),str(j+1)))
            # print(angle1)
            # # print(i+1)
            # print(OV_vec)
            # print(OP_vec)

            # print(OV_vec)
            # print(OP_vec)

            # print(OP_vec)
            # print(math.cos(angle(OV_vec,OP_vec)),math.sin(angle(OV_vec,OP_vec)))
            # if(math.cos(angle(OV_vec,OP_vec))==1 and math.sin(angle(OV_vec,OP_vec)) == 0):
            #     print(i,j)

            # print(angle(OV_vec,OP_vec))
            anno_ls[i][j,0] = (math.cos(angle(OV_vec,OP_vec))/math.sin(angle(OV_vec,OP_vec)))/(math.cos(a)/math.sin(a))
            # print(np.linalg.norm(OP_vec, ord=2))
            anno_ls[i][j, 1] = np.linalg.norm(OP_vec,ord=2)*math.sin(angle(OV_vec,OP_vec))




        anno_ls[i] = np.delete(anno_ls[i], [2,3], axis=1)



    return anno_ls
