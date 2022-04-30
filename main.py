import math
import os
import numpy as np

from MHA.MHA_code.top_vec import *
from MHA.MHA_code.hor_vec import *
from MHA.MHA_code.util import *
from MHA.MHA_code.Dissimi_mat import *
from MHA.MHA_code.dtw import *
from MHA.MHA_code.cost_func import *


# print('test代码')

# thr = 0.02
# miu = get_miu(top_vec_2(1843.5,352.5,235),hor_vec(),thr)
# # print(miu,len(miu))
#
# rel_dismat = Dissimi_mat(top_vec_2(1843.5,352.5,235),hor_vec(),0.015,miu)
# # print(rel_dismat[100].shape)
#
# t = dtw(top_vec_2(1843.5,352.5,235),hor_vec(),rel_dismat)
#
#
# print("------------")
# print(t[0][0]) #matched
# print(t[1][0]) #k_class
# # print(t[2])  #D
# # print(t[3]) #Dist
# print("------------")
#
#
# print(single_out(rel_dismat[0],t[0][0]))

def rej_idx(a):
    tmp =[]
    for i in range(len(a)):
        if(a[i] != 0):
            tmp.append(a[i])

    a = np.array(tmp)


    return a

# print(single_out(rel_dismat[0],t[0][0])[1])
# idx_hor = rej_idx(single_out(rel_dismat[0],t[0][0])[0])
# idx_top = rej_idx(single_out(rel_dismat[0],t[0][0])[1])
#
# print(idx_hor ,idx_top)




Rho = 15

lambda1 = 0.015

def cost_func():

    cam_loc_vec = get_cam_loc()

    Cam_loc_x_list = []
    Cam_loc_y_list = []
    angle_rel_list = []
    idx_top_rel_list = []
    idx_hor_rel_list = []

    # cwd = os.getcwd()
    # file = open(cwd+'/fra_good.txt', 'w')
    for i in range(230,231):
        print("now address %dth frame"%(i+1))
        vhor = hor_vec()
        Cost_rel = math.inf
        Cam_loc_x = 0
        Cam_loc_y = 0
        angle_rel = 0
        top_N = top_vec_1()[i].shape[0]

        idx_top_rel = []
        idx_hor_rel = []

        true_cam_ls = get_true_camloc()


        for anglex in range(0,360,5):

            # for j in range(top_N):
            #
            #     #this
            #     thr = 0.025
            #     vtop = top_vec_2(cam_loc_vec[i][j][0],cam_loc_vec[i][j][1],anglex)
            #
            #
            #     miu = get_miu(vtop, vhor, thr)
            #
            #     rel_dismat = Dissimi_mat(vtop, vhor, 0.015, miu)
            #     # print(rel_dismat[0].shape)
            #
            #     dtw_rel = dtw(vtop, vhor, rel_dismat)
            #     # print(len(dtw_rel[0]))
            #     print(rel_dismat[i].shape)
            #     print(dtw_rel[0])
            #
            #     match_mat = single_out(rel_dismat[i], dtw_rel[0][i])
            #
            #
            #     # print(match_mat)
            #     idx_hor = rej_idx(match_mat[0])
            #     idx_top = rej_idx(match_mat[1])
            #
            #     len1 = max(vtop[i].shape[0],vhor[i].shape[0])
            #     lamda1 = len(idx_top)
            #     # print(lamda1,"kkk")
            #     # print(idx_hor)
            #
            #     if(lamda1 == 0):#???
            #         continue
            #     penalty_vec = math.pow(Rho,(len1/lamda1))
            #
            #     vtopcutvhor_rej_x = []
            #     vtopcutvhor_rej_y = []
            #     for z in range(len(idx_top)):
            #         # print(idx_hor[z])
            #         # print(vtop[i][idx_top[z]-1,:]-vhor[i][idx_hor[z]-1,:])
            #         vtopcutvhor_rej_x.append(vtop[i][idx_top[z]-1][0]-vhor[i][idx_hor[z]-1][0])
            #         vtopcutvhor_rej_y.append(miu[i]*vtop[i][idx_top[z]-1][1] - vhor[i][idx_hor[z]-1][1])
            #
            #     # print(vtopcutvhor_rej_x,vtopcutvhor_rej_y)
            #
            #     score = (lambda1*np.linalg.norm(vtopcutvhor_rej_x, ord=1)+ np.linalg.norm(vtopcutvhor_rej_y, ord=1))
            #
            #     Cost_now = penalty_vec*score
            #
            #     if(Cost_now<Cost_rel):
            #         Cost_rel = Cost_now
            #         Cam_loc_x = cam_loc_vec[i][j][0]
            #         Cam_loc_y = cam_loc_vec[i][j][1]
            #         angle_rel = anglex
            #         idx_top_rel = idx_top
            #         idx_hor_rel = idx_hor
            #         # print('dsdsffsdfs')

            # this
            thr = 0.02
            vtop = top_vec_2(true_cam_ls[i][0], true_cam_ls[i][1], anglex)

            miu = get_miu(vtop, vhor, thr)

            rel_dismat = Dissimi_mat(vtop, vhor, 0.015, miu)
            # print(rel_dismat[0].shape)

            dtw_rel = dtw(vtop, vhor, rel_dismat)
            # print(len(dtw_rel[0]))
            # print(rel_dismat[i].shape)
            # print(dtw_rel[0][i].shape)

            match_mat = single_out(rel_dismat[i], dtw_rel[0][i])

            # print(match_mat)
            idx_hor = rej_idx(match_mat[0])
            idx_top = rej_idx(match_mat[1])

            len1 = max(vtop[i].shape[0], vhor[i].shape[0])
            lamda1 = len(idx_top)
            # print(lamda1,"kkk")
            # print(idx_hor)

            if (lamda1 == 0):  # ???
                continue
            penalty_vec = math.pow(Rho, (len1 / lamda1))

            vtopcutvhor_rej_x = []
            vtopcutvhor_rej_y = []
            for z in range(len(idx_top)):
                # print(idx_hor[z])
                # print(vtop[i][idx_top[z]-1,:]-vhor[i][idx_hor[z]-1,:])
                vtopcutvhor_rej_x.append(vtop[i][idx_top[z] - 1][0] - vhor[i][idx_hor[z] - 1][0])
                vtopcutvhor_rej_y.append(miu[i] * vtop[i][idx_top[z] - 1][1] - vhor[i][idx_hor[z] - 1][1])

            # print(vtopcutvhor_rej_x,vtopcutvhor_rej_y)

            score = (lambda1 * np.linalg.norm(vtopcutvhor_rej_x, ord=1) + np.linalg.norm(vtopcutvhor_rej_y,
                                                                                         ord=1))

            Cost_now = penalty_vec * score

            if (Cost_now < Cost_rel):
                Cost_rel = Cost_now
                Cam_loc_x = true_cam_ls[i][0]
                Cam_loc_y = true_cam_ls[i][1]
                angle_rel = anglex
                idx_top_rel = idx_top
                idx_hor_rel = idx_hor
                # print('dsdsffsdfs')


            print('now best',Cost_rel,Cam_loc_x,Cam_loc_y,angle_rel)
            print('best matching ',idx_hor_rel,"hor ==>",idx_top_rel,'top')
            print("now angle is %d"%anglex)

        anno_top = read_x_anno('top')
        anno_hor = read_x_anno('hor')
        anno_top = anno_top[i]
        anno_hor = anno_hor[i]
        count = 0
        for i in range(len(idx_hor_rel)):
            # print(anno_hor)
            # print(anno_top)
            print(anno_hor[idx_hor_rel[i] - 1][4], 'hor==>top', anno_top[idx_top_rel[i] - 1][4])
            if (anno_hor[idx_hor_rel[i] - 1][4] == anno_top[idx_top_rel[i] - 1][4]):
                count += 1

        print('accu', count / len(idx_hor_rel))
        # if (count / len(idx_hor_rel) >= 0.6):
        #     file.write('%d\n'%i)

        Cam_loc_x_list.append(Cam_loc_x)
        Cam_loc_y_list.append(Cam_loc_y)
        angle_rel_list.append(angle_rel)
        idx_hor_rel_list.append(idx_hor_rel)
        idx_top_rel_list.append(idx_top_rel)

    # file.close()

    return Cam_loc_x_list,Cam_loc_y_list,angle_rel_list,idx_hor_rel_list,idx_top_rel_list

x = cost_func()
print(x)














