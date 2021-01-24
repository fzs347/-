## YOLOV3：Object detection based on YOLO v3
---

### Contents 

2. [Environment](#所需环境)
3. [Download](#文件下载)
4. [How2predict](#预测步骤)
5. [How2train](#训练步骤)
6. [Reference](#Reference)

### Environment
torch == 1.7.1 \
Ubuntu == 16.04.4 \
Python == 3.8 \
opencv == 3.4.9

### Download
1、re-train weights：yolo_weights.pth (coco)  \
2、model.pth \
2、Voc2012（datasets, labels, txt）



### Predict
#### 
1、Use model.pth：run predict.py to predict images \
2、Use prediict_video.py to predict video
```python
_defaults = {
    "model_path": 'model.pth',
    "classes_path": 'voc_classes.txt,
    "score" : 0.5,
    "iou" : 0.4,
    "model_image_size" : (416, 416)
}

```


### Train
1、Download pre-train weights：yolo_weights.pth (coco) \
2、Use VOC format for training \
3、Prepare datasets and label files （the VOCdevkit folder）
```python
classes = ["aeroplane", "bicycle", "bird", "boat", "bottle", "bus", "car", "cat", "chair", "cow", "diningtable", "dog", "horse", "motorbike", "person", "pottedplant", "sheep", "sofa", "train", "tvmonitor"]
```

### Reference 

[1]	Redmon, Joseph, et al. "You only look once: Unified, real-time object detection." Proceedings of the IEEE conference on computer vision and pattern recognition. 2016 \
[2]	Redmon, Joseph, and Ali Farhadi. "YOLO9000: better, faster, stronger." Proceedings of the IEEE conference on computer vision and pattern recognition. 2017 \
[3]	Redmon, Joseph, and Ali Farhadi. "Yolov3: An incremental improvement." arXiv preprint arXiv:1804.02767 (2018).
