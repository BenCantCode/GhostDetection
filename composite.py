import numpy as np
import cv2
import random
from PIL import Image
import numpy as np
from skimage.util import random_noise

for i in range(0,500):
    ghost = Image.open('./images/{}.png'.format(i))

    # https://www.kaggle.com/c/deepfake-detection-challenge/discussion/124099   
    cap = cv2.VideoCapture("video.avi") #video_name is the video being called
    cap.set(1, random.randrange(0,(21*60+51)*20)); # Where frame_no is the frame you want
    ret, frame = cap.read() # Read the frame
    bg = Image.fromarray(frame)

    # overlay ghost on image
    bg.paste(ghost, (0, 0), ghost)
    
    bg.save('./composited/{}.png'.format(i))



    