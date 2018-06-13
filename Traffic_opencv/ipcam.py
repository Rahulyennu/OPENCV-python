import urllib
import cv2
import numpy as np
url="http://192.168.101.11:8080/shot.jpg"
while True:    
    imgPath=urllib.urlopen(url)
    imgNp=np.array(bytearray(imgPath.read()),dtype=np.uint8)
    img=cv2.imdecode(imgNp,-1)
    cv2.imshow("rahi",img)
    if ord('q') ==  cv2.waitKey(10):
        exit(0)
