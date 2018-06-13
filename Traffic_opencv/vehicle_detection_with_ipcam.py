import cv2

cascade_src = 'cars.xml'
video_src = '2.mp4'
cap = cv2.VideoCapture(video_src)
#cap = cv2.VideoCapture(0)
car_cascade = cv2.CascadeClassifier(cascade_src)
ip_cam=["192.168.101.11:8080","192.168.101.11:8080","192.168.101.11:8080","192.168.101.11:8080"]
try:
    while True:
        #for ip in ip_cam:
        #    url="http://"+ip+"/shot.jpg"
        #    imgPath=urllib.urlopen(url)
        #    imgNp=np.array(bytearray(imgPath.read()),dtype=np.uint8)
        #    img=cv2.imdecode(imgNp,-1)
        __,img=cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cars = car_cascade.detectMultiScale(gray, 1.1, 1)
        for (x,y,w,h) in cars:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        cv2.imshow('video', img)
        print "Found "+str(len(cars))+" car(s)"
        b=str(len(cars))
        a= float(b)
        if a>=5:
            print ("more traffic")
        else:
            print ("no traffic")
        if cv2.waitKey(33) == 27:
            break
except KeyboardInterrupt:            
    cv2.destroyAllWindows()

