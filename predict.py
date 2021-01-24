

from yolo import YOLO
from PIL import Image
from tqdm import tqdm
import cv2
import numpy as np
import time


#    one picture
test_select = 'one'


#    videos
# test_select = 'many'



#---------------------------------------------------------------
if test_select == 'one':
    yolo = YOLO()
    img = 'img/street.jpg'
    # img = 'img/1.jpg'
    # img = 'img/00003.jpg'
    #img = 'VOCdevkit/UA_test/MVI_39031/img00001.jpg'
    image = Image.open(img)
    r_image = yolo.detect_image(image)
    r_image.show()
    # r_image.save('logs/save_result/1.jpg')



#----------------------------------------------------------------
# ## UA
# if test_select == 'many':
#
#     yolo = YOLO()
#     name_id = str()
#     name_all = 1470
#     for id in range(name_all):
#         id+=1
#         id = str(id)
#         zer = len(id)
#         zer_num = 5 - zer
#         zer0 = '0'
#         zer_new = str()
#         for i in range(zer_num):
#             zer_new = zer0 + zer_new
#
#         name_id = 'img' + zer_new + id
#         image = Image.open('./VOCdevkit/UA_test/MVI_39031/'+name_id+".jpg")
#         r_image = yolo.detect_image(image)
#         # r_image.show()
#         r_image.save('./VOCdevkit/UA_test/result/' + name_id + ".jpg")


#-------------------------------------------------------------------------------
## voc
if test_select == 'many':
    yolo = YOLO()
    image_ids = open('VOCdevkit/VOC2012/ImageSets/Main/test.txt').read().strip().split()
    for image_id in tqdm(image_ids):
        image_path = "./VOCdevkit/VOC2012/JPEGImages/"+image_id+".jpg"
        image = Image.open(image_path)
        r_image = yolo.detect_image(image)
        # r_image.show()
        r_image.save('./VOCdevkit/VOC_test_result/' + image_id + ".jpg")

#----------------------------------------------------------------------------------
    image_ids = open('VOCdevkit/VOC2012/ImageSets/Main/test.txt').read().strip().split()
    for image_id in tqdm(image_ids):
        img = Image.open('./VOCdevkit/VOC_test_result/' + image_id + ".jpg")
        img = np.array(img)
        cv2.imshow('img',img)
        cv2.waitKey(1)
        time.sleep(1)



