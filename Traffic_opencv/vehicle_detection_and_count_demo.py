import cv2
cascade_src = 'cars.xml'
video_src = '2.mp4'
cap = cv2.VideoCapture('2.mp4')
car_cascade = cv2.CascadeClassifier(cascade_src)
while True:
    ret, img = cap.read()
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

cv2.destroyAllWindows()
