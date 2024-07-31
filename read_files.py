import os
from cocoapi.PythonAPI.pycocotools.coco import COCO
from PIL import Image
import numpy as np

base_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'pentax_train_set')
annotations_path = '/Users/dylan/Desktop/pentax_train_set/annotations'
annotation_files = [f for f in os.listdir(annotations_path) if f.endswith('.json')]

training = annotation_files[0:int(len(set(annotation_files))*0.8)]
validation = annotation_files[int(len(set(annotation_files))*0.8):]

for files in training:
        
    coco = COCO(os.path.join(annotations_path, files))
    
    img_ids = coco.getImgIds()
    for img_id in img_ids:
        img_info = coco.loadImgs(img_id)[0]
        file_path = img_info['file_name']
        file_name = file_path.split("general/")[1]
        ann_ids = coco.getAnnIds(imgIds=img_id)
        anns = coco.loadAnns(ann_ids)

        mask = np.zeros((img_info['height'], img_info['width']))


        for ann in anns:
            ann_mask = coco.annToMask(ann)
            mask = np.maximum(mask,ann_mask)
            mask_image = Image.fromarray(mask.astype(np.uint8) * 255)
            mask_image.save(os.path.join(base_path, 'label', 'training', f"{file_name}"))
            

    without_json = files[:-5]
    images = os.path.join(base_path, 'images', without_json, 'polyp1', 'general')
    image_files = [f for f in os.listdir(images) if f.endswith('.png')]
    
    for img in image_files:

        image_path = os.path.join(images, img)
        image_data = Image.open(image_path)
        image_data.save(os.path.join(base_path, 'img', 'training', f"{img}"))

for files in validation:
        
    coco = COCO(os.path.join(annotations_path, files))
    
    img_ids = coco.getImgIds()
    for img_id in img_ids:
        img_info = coco.loadImgs(img_id)[0]
        file_path = img_info['file_name']
        file_name = file_path.split("general/")[1]
        ann_ids = coco.getAnnIds(imgIds=img_id)
        anns = coco.loadAnns(ann_ids)

        mask = np.zeros((img_info['height'], img_info['width']))

        for ann in anns:
            ann_mask = coco.annToMask(ann)
            mask = np.maximum(mask,ann_mask)
            mask_image = Image.fromarray(mask.astype(np.uint8) * 255)
            mask_image.save(os.path.join(base_path, 'label', 'validation', f"{file_name}"))
            
    without_json = files[:-5]
    images = os.path.join(base_path, 'images', without_json, 'polyp1', 'general')
    image_files = [f for f in os.listdir(images) if f.endswith('.png')]
    
    for img in image_files:
        image_path = os.path.join(images, img)
        image_data = Image.open(image_path)
        image_data.save(os.path.join(base_path, 'img', 'validation', f"{img}"))
        
            




    
        
        
        
        
        
        
    
    
    
    
    
    
    
    
    
    
    