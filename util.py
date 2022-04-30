import math
from MHA.MHA_code.read_dataset import *

AB = [2034, 186.5, 2034, 186.5]
CD = [2034, 186.5, 1800, 0]
EF = [2, 5, -2, 6]
PQ = [-3, -4, 1, -6]


def angle(v1, v2):
    dx1 = v1[2] - v1[0]
    dy1 = v1[3] - v1[1]
    dx2 = v2[2] - v2[0]
    dy2 = v2[3] - v2[1]
    angle1 = math.atan2(dy1, dx1)
    angle1 = angle1 * 180 / math.pi
    # print(angle1)
    angle2 = math.atan2(dy2, dx2)
    angle2 = angle2 * 180 / math.pi
    # print(angle2)
    if angle1 * angle2 >= 0:
        included_angle = abs(angle1 - angle2)
    else:
        included_angle = abs(angle1) + abs(angle2)
        if included_angle > 180:
            included_angle = 360 - included_angle


    return included_angle*math.pi/180


def get_miu(vtop,vhor,thr):
    count = 0
    miu = 0
    rel_miu = []
    for i in range(len(vtop)):
        p = 0
        for j in range(vhor[i].shape[0]):
            for k in range(vtop[i].shape[0]):
                if(math.fabs(vtop[i][k][0]-vhor[i][j][0]) <= thr):
                    miu += vhor[i][j][1]/vtop[i][k][1]
                    p += 1.0
        if (p == 0):
            count+=1
            # print('no one match miu',count)
            p = 1
        miu = miu / p
        rel_miu.append(miu)

        miu = 0
        p = 0

    return rel_miu

def get_cam_loc():
    anno_ls = read_x_anno('top')

    for i in range(len(anno_ls)):
        anno_ls[i][:, 0] = (anno_ls[i][:, 0] + anno_ls[i][:, 2] ) / 2
        anno_ls[i][:, 1] = (anno_ls[i][:, 3] + anno_ls[i][:, 1]) / 2
        anno_ls[i] = np.delete(anno_ls[i], [2,3], axis=1)



    return anno_ls

def get_true_camloc():

    anno_ls = get_cam_loc()
    true_loc_ls = []
    for i in range(len(anno_ls)):
        true_loc_x = 0
        true_loc_y = 0
        for j in range(anno_ls[i].shape[0]):
            if(int(anno_ls[i][j][2]) == 0):
                true_loc_x = anno_ls[i][j][0]
                true_loc_y = anno_ls[i][j][1]
        true_loc_ls.append([true_loc_x,true_loc_y])

    return true_loc_ls

# ang1 = angle(AB, CD)
# print("AB和CD的夹角")
# print(ang1)
# a = math.pi/4
# print((math.cos(ang1)/math.sin(ang1))/(math.cos(a)/math.sin(a)))



# ang2 = angle(AB, EF)
# print("AB和EF的夹角")
# print(ang2)
# ang3 = angle(AB, PQ)
# print("AB和PQ的夹角")
# print(ang3)
# ang4 = angle(CD, EF)
# print("CD和EF的夹角")
# print(ang4)
# ang5 = angle(CD, PQ)
# print("CD和PQ的夹角")
# print(ang5)
# ang6 = angle(EF, PQ)
# print("EF和PQ的夹角")
# print(ang6)