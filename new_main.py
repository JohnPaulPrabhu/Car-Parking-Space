import cv2

video_path = './data/parking_1920_1080_loop.mp4'
mask_path = './data/mask_1920_1080.png'


mask = cv2.imread(mask_path, 0)
'''
0 means, we are explicitly mentioning that we reading the grayscale image
1 means, loading an color image
-1 means, load the image as it is, it can contain the alpha channel
'''

cap = cv2.VideoCapture(video_path)

ret = True
while ret:
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
    

cap.release()
cv2.destroyAllWindows()