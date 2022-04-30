import math
import numpy as np

def dtw(vtop,vhor,dismat):
    match_idx_P_ls = []
    k_class_ls = []
    D_ls = []
    Dist_ls = []


    for i in range(len(vtop)):

        N = vtop[i].shape[0]
        M = vhor[i].shape[0]

        D = np.zeros([N, M])

        D[0][0] = dismat[i][0][0]

        for n in range(1,N):
            D[n][0] = dismat[i][n][0] + D[n-1][0]

        for m in range(1,M):
            D[0][m] = dismat[i][0][m] + D[0][m-1]

        for n in range(1,N):
            for m in range(1, M):
                D[n][m] = dismat[i][n][m] + min(D[n-1][m],D[n-1][m-1],D[n][m-1])


        Dist = D[N-1][M-1]
        n = N
        m = M
        k_class = 1


        match_idx = []
        match_idx_P = np.zeros([N,M])
        match_idx = match_idx+[N,M]
        match_idx_P[N-1][M-1] = 1



        while((n+m)!=0):
            i = 0
            if(n==0):
                m = m-1
            elif(m==0):
                n = n-1
            else:
                # print(min(D[n-2][m-1],D[n-1][m-2],D[n-2][m-2]))
                list1 = np.array([D[n-2][m-1],D[n-1][m-2],D[n-2][m-2]])
                number = np.argmin(list1)
                # print("isdfoisfh",number)
                # print("n",n,"m",m)
                # i+=1
                # print(i)
                if(number == 0):
                    n = n-1
                elif(number == 1):
                    m = m-1
                elif(number == 2):
                    n = n-1
                    m = m-1
                    k_class += 1

            match_idx = np.vstack((match_idx,[n,m]))
            match_idx_P[n-1,m-1] = 1

        match_idx_P_ls.append(match_idx_P)
        k_class_ls.append(k_class)
        D_ls.append(D)
        Dist_ls.append(Dist)




    return match_idx_P_ls, k_class_ls,D_ls,Dist_ls