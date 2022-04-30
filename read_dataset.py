# coding:utf-8

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
import sys
import numpy as np

# anno_path = 'E:/matlab_learn/CVMHAT-main/CVMHAT_dataset-anno/GT_xml/GT_xml/V0-S_canteen_0-G_1/hor/0001.xml'



def read_anno(annopath):
    tree = ET.parse(annopath)
    root = tree.getroot()

    lis = []

    for obj in root.findall('object'):
        obj_id = obj.find('name').text
        rec = obj.find('rectangle')
        xmin = rec.find('xmin').text
        ymin = rec.find('ymin').text
        xmax = rec.find('xmax').text
        ymax = rec.find('ymax').text
        ls_temp = [float(xmin), float(ymin), float(xmax), float(ymax), float(obj_id)]
        lis.extend(ls_temp)

    anno = np.array(lis).reshape(len(root.findall('object')), -1)

    return anno


def read_x_anno(view):
    ls = []
    for i in range(1,601):
        str1 = str(i).zfill(4)
        ls.append(read_anno('E:/matlab_learn/CVMHAT-main/CVMHAT_dataset-anno/GT_xml/GT_xml/V0-S_canteen_0-G_1/%s/%s.xml'%(view,str1)))
    anno_mat = np.array(ls, dtype=object)
    return anno_mat




# print(read_x_anno('top').shape)

# x = [[[1,2],[3,4]],[[5,6],[7,8]]]
# y = np.array(x)
# print(y.shape)

# anno = read_anno(anno_path)
# print(anno)
