from ultralytics import YOLO
import cv2
import cvzone
import math

confidence = 0.8

# Initialize video capture and set resolution
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

# Load YOLO model
model = YOLO('models/n_version_1_30.pt')

# List of class names
classNames = ["fake", "real"]

# Get screen resolution
screen_width = 3840  # Change this to your screen resolution
screen_height = 2160  # Change this to your screen resolution

# Create a resizable window
cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Image", screen_width, screen_height)

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

            # Extract confidence score and class index
            conf = math.ceil((box.conf[0] * 100)) / 100
            cls = box.cls[0]

            # Get class name based on class index
            name = classNames[int(cls)].upper()
            
            if conf > confidence:
                if name == "REAL":
                    # Draw green rectangle if real
                    color = (0, 255, 0)
                else:  
                    # Draw red rectangle if fake
                    color = (0, 0, 255)
                # Draw rectangle around the object
                cvzone.cornerRect(img, (x1, y1, w, h), colorC=color, colorR=color)
                # Display class name and confidence score
                cvzone.putTextRect(img, f'{name} {int(conf*100)}%', (max(0, x1), max(35, y1)), scale=2, thickness=2, colorR=color, colorB=color)

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
