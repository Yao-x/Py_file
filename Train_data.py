import os
import xml.etree.ElementTree as ET
import xml.dom.minidom
import numpy as np
import cv2
filePath="G:\yolo_tensorflow-master\yolo_tensorflow-master1\yolo_tensorflow-master\data\pascal_voc\VOCdevkit\VOC2007\Annotations"
filePath_1="G:\yolo_tensorflow-master\yolo_tensorflow-master1\yolo_tensorflow-master\data\pascal_voc\VOCdevkit\VOC2007\Annotations\\"
Goal_Name=os.listdir(filePath)
Line=len(Goal_Name)


def Gain_name(i):
    Goal_Name[i] = filePath_1 + Goal_Name[i]
    dom = xml.dom.minidom.parse(Goal_Name[i])
    root = dom.documentElement
    itemlist = root.getElementsByTagName('path')
    name = itemlist[0]
    Name = name.firstChild.data
    return Name
def Gain_boxs(i):
    tree = ET.parse(Goal_Name[i])
    objs = tree.findall('object')
    # for obj in objs:
    #     bbox = obj.find('bndbox')
    #     x_min = max(float(bbox.find('xmin').text), 0)
    #     y_min = max(float(bbox.find('ymin').text), 0)
    #     x_max = max(float(bbox.find('xmax').text), 0)
    #     y_max = max(float(bbox.find('ymax').text), 0)
    return objs


for i in range(Line):
    # Goal_Name[i]=filePath_1+Goal_Name[i]
    # dom = xml.dom.minidom.parse(Goal_Name[i])
    # root = dom.documentElement
    # itemlist = root.getElementsByTagName('path')
    # name = itemlist[0]
    # Name = name.firstChild.data
    Name = Gain_name(i)
    # Goal_Name[i] = filePath_1 + Goal_Name[i]
    # tree = ET.parse(Goal_Name[i])
    # objs = tree.findall('object')
    # for obj in objs:
    #     bbox = obj.find('bndbox')
    #     x_min = max(float(bbox.find('xmin').text),0)
    #     y_min = max(float(bbox.find('ymin').text),0)
    #     x_max = max(float(bbox.find('xmax').text), 0)
    #     y_max = max(float(bbox.find('ymax').text),0)
    objs = Gain_boxs(i)
    file = open('Name.txt','a')
    file.write('\n'+Name)
    for obj in objs:
        bbox = obj.find('bndbox')
        x_min = max(float(bbox.find('xmin').text), 0)
        y_min = max(float(bbox.find('ymin').text), 0)
        x_max = max(float(bbox.find('xmax').text), 0)
        y_max = max(float(bbox.find('ymax').text), 0)
        file.write(' ')
        file.write(str(x_min))
        file.write(' ')
        file.write(str(y_min))
        file.write(' ')
        file.write(str(x_max))
        file.write(' ')
        file.write(str(y_max))
        file.write(' ')
        file.write('0')
        # file.write(' ')
    file.close()







# #print(Goal_Name[0])
# for i in range(Line):
#     tree=ET.parse(Goal_Name[i])
#     Path=tree.findall('path')
#     print(Path)

