# Trash Detection Model 

This is a proof-of-concept model trained to identify paper and plastic in different shapes, sizes, and environments. This will later be expanded upon, as there are many more types of trash to be classified and detected. 

## Project Overview

- **Problem:** Detect paper and plastic in different orientations and sizes using computer vision.
- **Model Type:** Object Detection (YOLOv8). 
- **Dataset:** Custom YOLO-format dataset with labeled images of paper and plastic, some images in target environment for demonstration. 
- **Goal:** Reliably detect paper and plastic in live camera feed.

## Dataset

- ~350 labeled and annotated images from varied environments
- Classes: 'paper', 'plastic', 'null'
- Data augmentation: Horizontal flip, 90° rotate CW and CCW, Shear ±10° horizontal and vertical, Brightness ±20%

See https://app.roboflow.com/trash-ycdoj/paperplastic-dynp6/3 for dataset details. 

## Training Details

- **Model Type:** Roboflow Object Detection 3.0 (Fast)
- **Training Epochs:** 300
- **Batch Size:** 16
- **Input Size:** 640x640

## Training Graphs

![image](https://github.com/user-attachments/assets/4c240965-25bb-465a-b2ab-374b5daa12e8)

![image](https://github.com/user-attachments/assets/e8a1b6a4-70a1-4788-82a0-37187d459005)





