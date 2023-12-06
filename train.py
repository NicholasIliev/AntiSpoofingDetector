from ultralytics import YOLO

# initialize
model = YOLO('yolov8n.pt')  

def main():
    # dataset.yaml path
    model.train(data='Dataset/SplitData/dataOffline.yaml', epochs=30) 

if __name__ == "__main__":
    main()