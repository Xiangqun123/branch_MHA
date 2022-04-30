import math
import numpy as np

lambda1 = 0.015
rou = 25




def Dissimi_mat(vtop,vhor, lamd, miu):
    dij = []
    for i in range(len(vtop)):
        dij1 = []
        for j in range(vtop[i].shape[0]):
            for k in range(vhor[i].shape[0]):
                dij1.append(lambda1*math.fabs(vtop[i][j][0]-vhor[i][k][0])+math.fabs(miu[i]*vtop[i][j][0]-vhor[i][k][0]))


        rel_temp = np.array(dij1).reshape(vtop[i].shape[0],-1)
        dij.append(rel_temp)

    rel_dij = np.array(dij,dtype=object)
    return rel_dij