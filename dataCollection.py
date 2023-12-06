import cv2
import cvzone
from cvzone.FaceDetectionModule import FaceDetector

########### Initialize ##############
confidence = 0.8
offsetPercentageH = 0.1
offsetPercentageW = 0.2
camWidth, camHeight = 640, 480
floatingPoint = 6
#####################################

cap = cv2.VideoCapture(0)
cap.set(3, camWidth)
cap.set(4, camHeight)
detector = FaceDetector()
while True:
    success, img = cap.read()
    img, bboxs = detector.findFaces(img, draw=False)

    if bboxs:
        ## bboxInfo = "id", "bbox", "score", "center"
        for bbox in bboxs:
            x, y, w, h = bbox["bbox"]
            score = bbox["score"][0]
            print(score)
            print(x, y, w, h)
            
            # ------ Check the score ------
            if score > confidence:
                
                # ------ Adding an offset to the face detected ------
                offsetW = offsetPercentageW * w
                x = int(x - offsetW)
                w = int(w + 2 * offsetW)
                
                offsetH = offsetPercentageH * h
                y = int(y - offsetH * 5)
                h = int(h + offsetH * 5.5)
                
                # ------ To avoid values below 0 ------
                if x < 0: x = 0
                if y < 0: y = 0
                if w < 0: w = 0
                if h < 0: h = 0
                
                # ------ Find bluriness ------
                imgFace = img[y:y+h, x:x+w]
                cv2.imshow("Face", imgFace)
                blurValue = int(cv2.Laplacian(imgFace, cv2.CV_64F).var())
                
                # ------ Normalise value ------
                ih, iw, _ = img.shape
                xc, yc = x + w/2, y + h/2
                
                xcn, ycn = round(xc / iw, floatingPoint), round(yc / ih, floatingPoint)
                wn, hn = w / iw, h / ih
                print(xcn, ycn, wn, hn)
                
                # ------ To avoid values above 1 ------
                if xcn > 1: xcn = 1
                if ycn > 1: ycn = 1
                if wn > 1: wn = 1
                if hn > 1: hn = 1
                
                # ------ Drawing ------
                cv2.rectangle(img, (x, y, w, h), (255, 0, 0), 3)
                cvzone.putTextRect(img, f'Score: {int(score*100)}% Blur: {blurValue}', (x, y-20), scale=2, thickness=2)


    cv2.imshow("Image", img)
    cv2.waitKey(1)