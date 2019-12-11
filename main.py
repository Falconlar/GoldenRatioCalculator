import numpy as np
import cv2


face_cascade = cv2.CascadeClassifier(r'/home/omer/work/Face-eye-detection-using-Haar-Cascade-classifier/haarcascade_frontalface_default.xml')

eye_cascade = cv2.CascadeClassifier(r'/home/omer/work/Face-eye-detection-using-Haar-Cascade-classifier/haarcascade_eye.xml')

mouth_cascade = cv2.CascadeClassifier(r'/home/omer/work/Face-eye-detection-using-Haar-Cascade-classifier/haarcascade_mouth.xml')

#gözbebegi_cascade = cv2.CascadeClassifier(r'/home/omer/work/Face-eye-detection-using-Haar-Cascade-classifier/haarcascade_eye_tree_eyeglasses.xml')


for l in range(1, 24):

    print('%d. resim:' %(l))
    img = cv2.imread('%d.jpeg'%(l))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # Yüz hesaplanması ,çizimi ve değerlerin tutulması
    for (x, y, w, h) in faces:
        facesxw = x + w - 100 
        facesyh = y + h + 50

        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]

        eyes = eye_cascade.detectMultiScale(roi_gray)
        mouths = mouth_cascade.detectMultiScale(roi_gray, 3.4, 5)
    #gözbebegi = gözbebegi_cascade.detectMultiScale(roi_gray,1.3,5) 
    
        eyessayac = 0
        mounthssayac = 0
        x1 = 0
        x2 = 0
        xw1 = 0
        xw2 = 0
        x2arası = 0
        x1arası = 0
        mounthxw = 0
        eyesxw = 0
        firstratio = 0
        toplamoran = 0
        toplamaltınoran = 0
    
    # Göz çizimi ve degerlerin tutulması
        for (ex, ey, ew, eh) in eyes:
            if int(eyessayac)<2:
                if int(eyessayac) == 0:
                    x1 = ex 
                    y1 = ey
                    xw1 = ex + ew
                    x1arası = ex + (ew / 2)
                if  int(eyessayac) == 1:
                    x2= ex + ew
                    xw2 = ex + ew
                    w2 = ew 
                    xa2 = ex
                    x2arası =  (w2/ 2) + xa2 + 150
                    
                
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 255), 2)
                eyessayac = eyessayac + 1

        # Agız çizimi ve degerlerinin tutulması
        for (nx, ny, nw, nh) in mouths:
            if int(mounthssayac)<1:
                mounthxw = (nx + nw) - nx
                cv2.rectangle(roi_color, (nx, ny), (nx+nw, ny+nh), (255, 0, 255), 1)
                mounthssayac = mounthssayac +1
                facesandmounty = ny +100
                mounthyh = ny + nh 
                jawandmount = facesyh - ny

        
        # kulanılan hesaplamalar
        eyesxw = x2 - x1
        twoeyesbetween = x2arası - x1arası
        twobrowsebetween = x2 - xw1

        # oran hesaplamaları 
        firstratio = eyesxw / mounthxw
        secondratio = facesyh / facesxw
        thirdratio = facesandmounty / jawandmount
        fourthratio = facesyh / (facesyh - y1)
        fifthratio =  twoeyesbetween / twobrowsebetween 
        
        # oranların birbirine orananı ve ortalaması
        toplamoran = firstratio + secondratio + thirdratio + fourthratio + fifthratio
        toplamaltınoran = toplamoran / 5


        # oranları ekrana basma
        print('1. oran:'+ str(firstratio))#göz genişliği / agiz genişliğiyle 
        print('2. oran:'+ str(secondratio))#yüzün yüksekliği / yüzün genişliği
        print('3. oran:'+ str(thirdratio))#dudakucu alınucu / dudak ucu cane ucu
        print('4. oran:'+ str(fourthratio))#yüz boyu / cene ucundan kaş birleşim yeri arası
        print('5. oran:'+ str(fifthratio))#göz bebekleri arası / kaşlar arası
        print('toplam altın oran:'+ str(toplamaltınoran))#tüm oranların ortalaması
        #for (bx,by,bw,bh) in gözbebegi:
            
            # cv2.circle(roi_color,(bx+bw,by),2,(0,0,0),2)
        

cv2.namedWindow("output", cv2.WINDOW_NORMAL)    # Create window with freedom of dimensions
imS = cv2.resize(img, (1000, 1000))             # Resize image
cv2.imshow("output", imS)
cv2.waitKey(0)

