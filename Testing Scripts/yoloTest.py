from ultralytics import YOLO
import cv2
import cvzone
import math

# Initialize video capture and set resolution
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

# Load YOLO model
model = YOLO('../models/yolov8n.pt')

# List of class names
classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
               "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
               "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack",
               "umbrella", "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball",
               "kite", "baseball bat", "baseball glove", "skateboard", "surfboard", "tennis racket",
               "bottle", "wine glass", "cup", "fork", "knife", "spoon", "bowl", "banana", "apple",
               "sandwich", "orange", "broccoli", "carrot", "hot dog", "pizza", "donut", "cake", "chair",
               "sofa", "pottedplant", "bed", "diningtable", "toilet", "tvmonitor", "laptop", "mouse",
               "remote", "keyboard", "cell phone", "microwave", "oven", "toaster", "sink", "refrigerator",
               "book", "clock", "vase", "scissors", "teddy bear", "hair drier", "toothbrush"]

while True:
    # Read frame from video capture
    success, img = cap.read()

    # Perform object detection using YOLO
    results = model(img, stream=True, verbose=False)

    for r in results:
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            w, h = x2 - x1, y2 - y1

            # Draw rectangle around the object
            cvzone.cornerRect(img, (x1, y1, w, h))

            # Extract confidence score and class index
            conf = math.ceil((box.conf[0] * 100)) / 100
            cls = box.cls[0]

            # Get class name based on class index
            name = classNames[int(cls)]

            # Display class name and confidence score
            cvzone.putTextRect(img, f'{name} {conf}', (max(0, x1), max(35, y1)), scale=0.5, thickness=1)

    # Display the frame
    cv2.imshow("Image", img)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    fps = cap.get(cv2.CAP_PROP_FPS)
    print(fps)

# Release the video capture object
cap.release()
cv2.destroyAllWindows()
