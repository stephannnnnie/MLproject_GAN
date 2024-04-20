import cv2
import os
from PIL import Image



if __name__ == '__main__':
    # extract frame from the video
    videoCapture = cv2.VideoCapture("../test2_1.mp4")
    fps = videoCapture.get(cv2.CAP_PROP_FPS)
    size = (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
            int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    videoWriter = cv2.VideoWriter('output.mp4', cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), (fps / 10), size)
    images = os.listdir("./results/school/")

    # read the frame
    
    for image in images:
        #success, frame = videoCapture.read()
        #cv2.imshow('a',frame)
        frame = Image.open(image)
        videoWriter.isOpened()
        videoWriter.write(frame)
        

    print("success")
    videoCapture.release()
    videoWriter.release()
    cv2.destroyAllWindows()
    # write frames into video file

