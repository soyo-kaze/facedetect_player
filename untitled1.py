import cv2 as o
import vlc as v

pr = v.MediaPlayer('sss.mkv')

face_ft = o.CascadeClassifier('Cascades/frontface.xml')

cam = o.VideoCapture(0)
font = o.FONT_HERSHEY_SIMPLEX
p=True
while True:
    boo, img = cam.read()
    grayimg = o.cvtColor(img, o.COLOR_BGR2GRAY)
    
    face_list = face_ft.detectMultiScale(grayimg, scaleFactor=2,)
    
    for (x,y,w,h) in face_list:
        o.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        o.putText(img, "face", (x+2, y),font, 1, (0,255,0), 2, o.LINE_AA)
        
    if(len(face_list)>0 and p==True):
        print("played")
        pr.play()
        p=False
    elif(len(face_list)==0 and p==False):
        print("paused")
        pr.pause()
        p=True
    
    o.imshow('Detection',img)
    
    k = o.waitKey(25)
    if k == 27:
        break

print("stopped")
pr.stop()
cam.release()
o.destroyAllWindows()