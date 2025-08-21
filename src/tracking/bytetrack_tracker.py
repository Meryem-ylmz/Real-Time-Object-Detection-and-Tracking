import cv2 as cv
from ultralytics import YOLO

model = YOLO("models/yolov8s.pt")

MIN_AREA = 16 * 16
PER_CLASS_CONF = {
    0: 0.50,
    2: 0.55,
    3: 0.50,
    5: 0.60,
    7: 0.60
}

def track(frame, classes=None, conf=0.5, imgsz=480):
    results = model.track(
        frame,
        classes=classes,
        conf=conf,
        imgsz=imgsz,
        persist=True
    )

    if len(results) == 0 or results[0].boxes is None or results[0].boxes.shape[0] == 0:
        return frame, results

    names = results[0].names

    for box in results[0].boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        conf_score = float(box.conf[0])
        cls = int(box.cls[0])
        track_id = int(box.id[0]) if box.id is not None else -1

        w, h = max(0, x2 - x1), max(0, y2 - y1)
        if w * h < MIN_AREA:
            continue

        if cls in PER_CLASS_CONF and conf_score < PER_CLASS_CONF[cls]:
            continue

        label = names[cls] if 0 <= cls < len(names) else str(cls)

        cv.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        text = f"ID:{track_id} {label} {conf_score:.2f}"
        cv.putText(frame, text, (x1, max(0, y1 - 10)),
                   cv.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    return frame, results