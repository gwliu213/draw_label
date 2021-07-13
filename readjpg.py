import json
import cv2
import os
import numpy as np

path = '/Users/gaoliu/Documents/Kronos/sensordog/stadium'
out_path = '/Users/gaoliu/Documents/Kronos/sensordog/stadium/outimg'
if not os.path.exists(out_path):
        os.makedirs(out_path)
for root, dirs, files in os.walk(path):
    for file in files:
        if file.endswith(".jpg"):
            filename, file_extension = os.path.splitext(file)
            labelfile= os.path.join(root +'/outputs/' + filename + '.json')
            img = cv2.imread(os.path.join(root+'/'+file))
            outputfile = os.path.join('/Users/gaoliu/Documents/Kronos/sensordog/outimg/' + filename + '_new.jpg')
            cv2.imshow('Frame', img)
            with open(labelfile, 'r') as file:
                data = json.load(file)
                timelist=[]
                for i in range(len(data['outputs']['object'])):
                    xmin, ymin, xmax, ymax = data['outputs']['object'][i]['bndbox']['xmin'], \
                                             data['outputs']['object'][i]['bndbox']['ymin'], \
                                             data['outputs']['object'][i]['bndbox']['xmax'], \
                                             data['outputs']['object'][i]['bndbox']['ymax']
                    cx = ((data['outputs']['object'][i]['bndbox']['xmin'])+(data['outputs']['object'][i]['bndbox']['xmax']))/2
                    cy = ((data['outputs']['object'][i]['bndbox']['ymin'])+(data['outputs']['object'][i]['bndbox']['ymax']))/2
                    timelist.append(((data['outputs']['object'][i]['bndbox'])))
                    # print(timelist[0]['xmin'])
                    if 'p1' in data['outputs']['object'][i]['name']:
                        color = (255,0,0)
                    elif 'p2' in data['outputs']['object'][i]['name']:
                        color = (0,255,0)
                    elif 'p3' in data['outputs']['object'][i]['name']:
                        color = (0,0,255)
                    elif 'p4' in data['outputs']['object'][i]['name']:
                        color = (255,255,0)
                    else:
                        color = (255,0,255)

                    cv2.rectangle(img,(xmin,ymin),(xmax,ymax),color,3)
                    cv2.circle(img,(int(cx),int(cy)),radius=3, color=(3,186,252),thickness=3)
                    # cv2.circle(image, (x, y), radius=0, color=(0, 0, 255), thickness=-1)
                    cv2.imshow('Frame', img)
                    cv2.waitKey(0)


                cv2.imwrite(outputfile,img)

                # Closes all the frames
                cv2.destroyAllWindows()