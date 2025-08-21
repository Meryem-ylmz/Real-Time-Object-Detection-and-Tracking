import cv2 as cv
from ultralytics import YOLO

model = YOLO("models/yolov8s.pt", task="detect")

def detect(frame, classes=None, conf=0.5, imgsz=480):
    results = model(frame, classes=classes, conf=conf, imgsz=imgsz)

    for box in results[0].boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        conf_score = float(box.conf[0])
        cls = int(box.cls[0])
        label = results[0].names[cls]

        cv.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
        text = f"{label} {conf_score:.2f}"
        cv.putText(frame, text, (x1, max(0, y1 - 10)),
                   cv.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

    return frame, results