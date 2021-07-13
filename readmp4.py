import json
import cv2
import numpy as np


with open('/Users/gaoliu/PycharmProjects/vid2img/lost_girl_1124__cam2.json', 'r') as file:
    data = json.load(file)
    timelist=[]
    for i in range(len(data['outputs']['object'])):
        timelist.append(int(float(data['outputs']['object'][i]['keyframes'][0]['time'])))
    print(int(float(data['outputs']['object'][0]['keyframes'][0]['time'])))

    if 33 in timelist:
        idx = timelist.index(33)
        print('idx: ',idx)
        print('yes, 33 is in the list')
# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
    cap = cv2.VideoCapture('/Users/gaoliu/PycharmProjects/vid2img/cam2_out.mp4')
    out = cv2.VideoWriter('cam2_out.mp4', cv2.VideoWriter_fourcc(*'MP4V'), 20,(data['size']['width'],data['size']['height']) )

# Check if camera opened successfully
    if (cap.isOpened() == False):
        print("Error opening video stream or file")

# Read until video is completed
    frame_index = 1
    while (cap.isOpened()):
    # Capture frame-by-frame

        ret, frame = cap.read()
        # start_time = 6
        # stop_time = 10
        if ret == True:
            fps = cap.get(cv2.CAP_PROP_FPS)  # OpenCV2 version 2 used "CV_CAP_PROP_FPS"
            frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            duration = frame_count / fps
            print(frame_index/fps)

            # print('fps = ' + str(fps))
            # print('number of frames = ' + str(frame_count))
            # print('duration (S) = ' + str(duration))
            # minutes = int(duration / 60)
            # seconds = duration % 60
            # print('duration (M:S) = ' + str(minutes) + ':' + str(seconds))
            # Display the resulting frame
            frameWidth = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            frameHeight = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            # if start_time < duration < stop_time:
            #     cv2.putText(img=frame, text='EKO', org=(int(frameWidth / 2 - 20), int(frameHeight / 2)),
            #                 fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=3,
            #                 color=(0, 255, 0))
            #     cv2.imshow('Frame', frame)
            if int(frame_index/fps) in timelist:
                idx = timelist.index(int(frame_index/fps))
                xmin, ymin, xmax, ymax = data['outputs']['object'][idx]['keyframes'][0]['xmin'], \
                                         data['outputs']['object'][idx]['keyframes'][0]['ymin'], \
                                         data['outputs']['object'][idx]['keyframes'][0]['xmax'], \
                                         data['outputs']['object'][idx]['keyframes'][0]['ymax']
                cv2.rectangle(frame,(xmin-5,ymin-10),(xmax+30,ymax+15),(255,0,0),3)
                out.write(frame)
            # Press Q on keyboard to  exit
            cv2.imshow('Frame', frame)

            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
            frame_index += 1
    # Break the loop
        else:
            break



    # When everything done, release the video capture object
    cap.release()
    out.release()

    # Closes all the frames
    cv2.destroyAllWindows()