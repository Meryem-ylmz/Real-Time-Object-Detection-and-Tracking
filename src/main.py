import cv2 as cv
import os
import time
from detect import detect
from tracking.bytetrack_tracker import track

CLASSES = [0, 2, 3, 5, 7]
CONF_TH = 0.5
IMG_SZ = 480

class VideoStream:
    def __init__(self, width=1280, height=720):
        source = input("Enter source (0=internal cam, 1=external cam, file path=video.mp4/image.jpg/rtsp://): ").strip()

        self.is_image = False
        if not source.isdigit():
            ext = os.path.splitext(source)[1].lower()
            if ext in ['.jpg', '.jpeg', '.png']:
                self.is_image = True
                self.image_path = source
                return
        else:
            source = int(source)

        self.cap = cv.VideoCapture(source)
        if self.cap.isOpened():
            self.cap.set(cv.CAP_PROP_FRAME_WIDTH, width)
            self.cap.set(cv.CAP_PROP_FRAME_HEIGHT, height)
            self.cap.set(cv.CAP_PROP_BUFFERSIZE, 1)

    def read(self):
        if self.is_image:
            frame = cv.imread(self.image_path)
            return True, frame, frame.copy()
        if not self.cap or not self.cap.isOpened():
            return False, None, None
        ret, frame = self.cap.read()
        if not ret:
            return False, None, None
        return True, frame, frame.copy()

    def release(self):
        if not self.is_image and self.cap:
            self.cap.release()

def main():
    mode = input("Choose mode (detect / track): ").strip().lower()
    if mode not in ("detect", "track"):
        print("Invalid mode! Defaulting to 'track'.")
        mode = "track"

    stream = VideoStream()
    window_title = f"Week 7 - {mode.capitalize()}"

    prev_time = time.time()

    while True:
        ret, frame, copy_frame = stream.read()
        if not ret:
            break

        if mode == "detect":
            frame, _ = detect(frame, classes=CLASSES, conf=CONF_TH, imgsz=IMG_SZ)
        else:
            frame, _ = track(frame, classes=CLASSES, conf=CONF_TH, imgsz=IMG_SZ)

        now = time.time()
        fps = 1.0 / (now - prev_time) if now > prev_time else 0.0
        prev_time = now
        cv.putText(frame, f"FPS: {fps:.1f}", (10, 30),
                   cv.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 255), 2)

        cv.imshow(window_title, frame)

        if stream.is_image:
            key = cv.waitKey(0) & 0xFF
            if key in (27, ord('q')):
                break
        else:
            key = cv.waitKey(1) & 0xFF
            if key in (27, ord('q')):
                break

    stream.release()
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()