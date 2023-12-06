import cv2
import cvzone
from cvzone.FaceDetectionModule import FaceDetector

########### Initialize ##############
confidence = 0.8  # Minimum confidence level for face detection
offsetPercentageH = 0.1  # Offset percentage for adjusting face height
offsetPercentageW = 0.2  # Offset percentage for adjusting face width
camWidth, camHeight = 640, 480  # Camera width and height
floatingPoint = 6  # Number of floating-point digits for normalization
#####################################

# Open the camera
cap = cv2.VideoCapture(0)
cap.set(3, camWidth)
cap.set(4, camHeight)

# Initialize FaceDetector from cvzone
detector = FaceDetector()

while True:
    # Read a frame from the camera
    success, img = cap.read()

    # Detect faces in the frame without drawing rectangles (draw=False)
    img, bboxs = detector.findFaces(img, draw=False)

    if bboxs:
        # Iterate through the detected faces
        for bbox in bboxs:
            x, y, w, h = bbox["bbox"]
            score = bbox["score"][0]
            print(score)
            print(x, y, w, h)

            # ------ Check the confidence score ------
            if score > confidence:

                # ------ Adjust the face rectangle using offset percentages ------
                offsetW = offsetPercentageW * w
                x = int(x - offsetW)
                w = int(w + 2 * offsetW)

                offsetH = offsetPercentageH * h
                y = int(y - offsetH * 5)
                h = int(h + offsetH * 5.5)

                # ------ Ensure values are non-negative ------
                x = max(0, x)
                y = max(0, y)
                w = max(0, w)
                h = max(0, h)

                # ------ Extract the face region for blur analysis ------
                imgFace = img[y:y+h, x:x+w]
                cv2.imshow("Face", imgFace)

                # ------ Calculate bluriness using Laplacian variance ------
                blurValue = int(cv2.Laplacian(imgFace, cv2.CV_64F).var())

                # ------ Normalize the position and size values ------
                ih, iw, _ = img.shape
                xc, yc = x + w / 2, y + h / 2

                xcn, ycn = round(xc / iw, floatingPoint), round(yc / ih, floatingPoint)
                wn, hn = w / iw, h / ih

                # ------ Ensure normalized values are within the valid range [0, 1] ------
                xcn = min(1, xcn)
                ycn = min(1, ycn)
                wn = min(1, wn)
                hn = min(1, hn)

                # ------ Draw the adjusted face rectangle and display text information ------
                cv2.rectangle(img, (x, y, w, h), (255, 0, 0), 3)
                cvzone.putTextRect(img, f'Score: {int(score * 100)}% Blur: {blurValue}', (x, y - 20),
                                    scale=2, thickness=2)

    # Display the processed frame
    cv2.imshow("Image", img)

    # Wait for a key event or update the display every 1 millisecond
    cv2.waitKey(1)
