# 🎯 Real-Time Object Detection and Tracking

This project is designed for **real-time object detection** using **YOLOv8** and **object tracking** with the **ByteTrack** algorithm. Objects detected in video streams or camera input are assigned IDs and tracked consistently.  

## 🚀 Features
- High-accuracy object detection with YOLOv8  
- Stable multi-object tracking with ByteTrack  
- Works with real-time camera or video file input  
- User can select **detect** (detection only) or **track** (detection + tracking) mode  
- Python-based and easily extendable  

## 📂 Project Structure
```
Real-Time-Object-Detection-and-Tracking/
├── src/
│   ├── main.py                  # Main file (mode selection: detect/track)
│   ├── detect.py                # Object detection functions
│   ├── tracking/
│   │   └── bytetrack_tracker.py # ByteTrack algorithm
├── models/
│   └── yolov8s.pt               # YOLOv8 weights file
├── yolov8_env/                  # Virtual environment (recommended)
├── README.md
└── requirements.txt
```

## 🛠 Installation

### 1. Clone the repository
```bash
git clone https://github.com/username/Real-Time-Object-Detection-and-Tracking.git
cd Real-Time-Object-Detection-and-Tracking
```

### 2. Create and activate a virtual environment
```bash
python -m venv yolov8_env
source yolov8_env/bin/activate   # Linux/Mac
yolov8_env\Scripts\activate      # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

## ▶️ Usage

### Detection Mode (detect)
For object detection only:
```bash
python src/main.py
```
Then select `detect` as the mode.  

### Tracking Mode (track)
For YOLOv8 detection + ByteTrack tracking:
```bash
python src/main.py
```
Then select `track` as the mode.  

Source options:
- `0` → Internal camera  
- `1` → External camera  
- `video.mp4` → File path  

## 📊 Example
```bash
Choose mode (detect / track): track
Enter source (0=internal cam, 1=external cam, file path=video.mp4/image.jpg/rtsp://): 0
```

## 📌 Notes
- `yolov8s.pt` must be located in the **models/** directory.  
- Using the virtual environment (`yolov8_env`) is recommended.  
- The project can be easily extended with different trackers or additional features.  

## 👩‍💻 Contribution
Contributions and pull requests are welcome!
