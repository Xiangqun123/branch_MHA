import math

import cv2


from MHA.MHA_code.hor_vec import *
from MHA.MHA_code.top_vec import *
from MHA.MHA_code.read_dataset import *

frame = 362

anno_top = read_x_anno('top')
anno_hor = read_x_anno('hor')
anno_hor = anno_hor[frame-1]
anno_top = anno_top[frame-1]

print(anno_hor)
print(anno_top)

idxhor_ls = [1, 2, 3, 4]
idxtop_ls = [1, 2, 4, 8]

true_cam_x,true_cam_y  = 2056.0 ,186.5

best_angle = 235

img_id = str(frame).zfill(4)
print(img_id)

get_x = 1 #1 top 2 hor


img_path1 = "E:/matlab_learn/CVMOT-AAAI2020/dataset/Images/V0-S_canteen_0-G_1/frame_sel/hor/%s.jpg"%img_id
img_path2 = "E:/matlab_learn/CVMOT-AAAI2020/dataset/Images/V0-S_canteen_0-G_1/frame_sel/top/%s.jpg"%img_id

img1 = cv2.imread(img_path1)
img2 = cv2.imread(img_path2)
# cv2.imwrite(save_path, img)

if get_x == 1:

    for i in range(len(idxtop_ls)):
        x1 = anno_hor[idxhor_ls[i]-1][0]
        y1 = anno_hor[idxhor_ls[i]-1][1]
        x2 = anno_hor[idxhor_ls[i]-1][2]
        y2 = anno_hor[idxhor_ls[i]-1][3]
        ground_truth = anno_hor[idxhor_ls[i]-1][4]
        ground_truth_top = anno_top[idxtop_ls[i]-1][4]


        cv2.rectangle(img1, (int(x1), int(y1)), (int(x2), int(y2)), (255, 0, 0), thickness=3)
        cv2.putText(img1, str(int(ground_truth)), (int(x2), int(y2)), fontScale=5,fontFace=cv2.FONT_ITALIC,color=(0, 255, 0),thickness=3)
        cv2.putText(img1, str(int(ground_truth_top)), (int(x2), int(y1)), fontScale=5, fontFace=cv2.FONT_ITALIC, color=(0, 255, 255),thickness=3)#黄色
        cv2.putText(img1, str(i+1)+'matched', (int(x2-100), int(y2+50)), fontScale=1.5, fontFace=cv2.FONT_ITALIC,color=(0, 5, 5), thickness=3)
    cv2.namedWindow('test1', cv2.WINDOW_NORMAL)
    # cv2.resizeWindow('test1',500*500)
    cv2.imshow("test1", img1)
    cv2.imwrite('hor_match.jpg', img1)

if get_x == 2:
    for i in range(len(idxtop_ls)):
        x1 = anno_top[idxtop_ls[i]-1][0]
        y1 = anno_top[idxtop_ls[i]-1][1]
        x2 = anno_top[idxtop_ls[i]-1][2]
        y2 = anno_top[idxtop_ls[i]-1][3]
        ground_truth = anno_top[idxtop_ls[i]-1][4]
        ground_truth_hor = anno_hor[idxhor_ls[i]-1][4]

        print(ground_truth, ground_truth_hor)

        cv2.rectangle(img2, (int(x1), int(y1)), (int(x2), int(y2)), (255, 0, 0), thickness=3)
        cv2.putText(img2, str(int(ground_truth)), (int(x2), int(y2)), fontScale=5,fontFace=cv2.FONT_ITALIC,color=(0, 255, 0),thickness=3)
        cv2.putText(img2, str(int(ground_truth_hor)), (int(x2), int(y1)), fontScale=5, fontFace=cv2.FONT_ITALIC, color=(0, 255, 255),thickness=3)

        cv2.putText(img2, str(i+1)+'matched', (int(x2+50), int(y1+50)), fontScale=2, fontFace=cv2.FONT_ITALIC,color=(5, 5, 5), thickness=3)


    point_size = 1
    point_color = (0, 255, 255) # BGR
    thickness = 4 # 可以为 0 、4、8

    xxx = int(true_cam_x)
    yyy = int(true_cam_y)
    anglexxx = best_angle
    anglexxx_re = anglexxx*math.pi/180
    cv2.circle(img2, (xxx, yyy), point_size, point_color, thickness)


    ptStart = (xxx,yyy)
    ptEnd = (int(xxx+200*math.cos(anglexxx_re)), int(yyy+200*math.sin(anglexxx_re)))
    ptEnd1 = (int(xxx+300*math.cos(anglexxx_re+math.pi/4+math.pi)), int(yyy+300*math.sin(anglexxx_re+math.pi/4+math.pi)))
    ptEnd2 = (int(xxx+300*math.cos(anglexxx_re+math.pi*3/4+math.pi)), int(yyy+300*math.sin(anglexxx_re+math.pi*3/4+math.pi)))


    point_color = (166, 255, 55) # BGR
    point_color1 = (255,0,0)
    thickness = 2
    lineType = 4
    cv2.arrowedLine(img2, ptStart, ptEnd, point_color, thickness, lineType)
    cv2.arrowedLine(img2, ptStart, ptEnd1, point_color1, thickness, lineType)
    cv2.arrowedLine(img2, ptStart, ptEnd2, point_color1, thickness, lineType)

    cv2.namedWindow('test2', cv2.WINDOW_NORMAL)
    cv2.imshow("test2", img2)
    cv2.imwrite('top_match.jpg', img2)


# print(img1.shape)

"""
img.shape	# (rows, columns, channels)
img.size	# (total number of pixels)
img.dtype	# (datatype of image)
# img2 = cv2.resize(img, (w,h), interpolation)	# interpolation=cv2.INTER_CUBIC

"""

# x1 = 1986
# y1 = 144
# x2 = 2082
# y2 = 229
#
# # color:(*,*,*)
# # thickness:粗细(thickness=-1表示填充效果)
# cv2.rectangle(img1, (x1,y1), (x2,y2), (255,0,0), thickness=3)







cv2.waitKey(0)