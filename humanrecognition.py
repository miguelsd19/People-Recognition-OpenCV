#Python code using OpenCV for human recognition using as example a tiktok video

import cv2

cap = cv2.VideoCapture(0)#cv2.VideoCapture(0)
human_cascade = cv2.CascadeClassifier('frontalFace.xml')#haarcascade_fullbody.xml

#print(cap.read())
cont=0
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    print(ret)
    if frame is None:
        print("Se terminó el vídeo")
        break

    # Our operations on the frame come here
    try:
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        print(gray)
        humans = human_cascade.detectMultiScale(gray, 1.9, 1)
    
        # Display the resulting frame
        for (x,y,w,h) in humans:
            cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0,0),2)
        
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        """
        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Display the resulting frame
        cv2.imshow('frame', gray)
        if cv2.waitKey(1) == ord('q'):
            break
        """
    except:
        cont+=1
        print("error")
        if cont>5:
            break   
    # When everything done, release the capture
cap.release()
cv2.destroyAllWindows()