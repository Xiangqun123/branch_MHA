import math
import numpy as np

a = float("inf")


def rej_idx(c):
    tmp =[]
    for i in range(len(c)):
        if(c[i] != 0):
            tmp.append(c[i])

    c = np.array(tmp)


    return c

def single_out(dismat,match_idx_P,thresh=100):
    n = match_idx_P.shape[0]
    m = match_idx_P.shape[1]

    w = dismat*match_idx_P
    # print(w,w.shape)
    match_idx_top = np.arange(1,n+1)
    match_idx_hor = np.arange(1,m+1)
    # print(match_idx_hor)

    w_temp = w
    w_temp = np.where(w_temp==0,a,w_temp)

    hor_num = np.count_nonzero(match_idx_P != 0, axis=1)

    top_num = np.count_nonzero(match_idx_P != 0, axis=0)
    idx_temp_top = np.zeros(int(m),dtype=int)
    idx_temp_hor = np.zeros(int(n),dtype=int)
    # print(idx_temp_hor)

    # print(hor_num,top_num)

    for i in range(0,n):
        if(hor_num[i] >= 2):
            loc = np.argmin(w_temp[i,:])
            # print(loc,"opio")
            idx_temp_top[loc] = 1
            w[i,:] = w[i,:]*idx_temp_top
            # print(1,w[:, i])

    for i in range(0,m):
        if(top_num[i] >= 2):
            loc = np.argmin(w_temp[:,i])
            # print(loc,"loccc")
            idx_temp_hor[loc] = 1
            # print(w[:,i].shape)
            w[:,i] = w[:,i]*(idx_temp_hor.T)



    w = np.where(w>thresh,0,w)


    w_temp1 = np.where(w==0,1,0)
    mask_hor = 1 - np.all(w_temp1,axis=0)
    # print(mask_hor)
    match_idx_hor = match_idx_hor*mask_hor


    mask_top = 1 - np.all(w_temp1, axis=1)
    # print(mask_top)
    match_idx_top = match_idx_top * mask_top.T

    score = np.sum(w)

    match_idx_hor = rej_idx(match_idx_hor)
    match_idx_top = rej_idx(match_idx_top)


    #!!!!!改
    if(len(match_idx_hor)!= len(match_idx_top)):
        print('异常啦，这个地方')
        print(match_idx_hor,match_idx_top)
        print('长度不一')
        # print(dismat*match_idx_P)
        # print(hor_num)


        # if(len(match_idx_hor) > len(match_idx_top)):
        #     match_idx_hor = match_idx_hor[0:-1]
        # elif(len(match_idx_hor) <len(match_idx_top)):
        #     match_idx_top = match_idx_top[0:-1]










    return match_idx_hor,match_idx_top,score


def cost_func(dismat,match_idx_P,thresh=100):
    pass