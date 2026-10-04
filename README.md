# Head Pose Estimation

This project demonstrates head pose estimation using MediaPipe Face Mesh and OpenCV.

## Requirements

- Python 3.7+
- Webcam

## Installation

1. Create a virtual environment:

   ```
   python -m venv .venv
   ```

2. Activate the virtual environment:
   - On Windows: `.venv\Scripts\activate`
   - On macOS/Linux: `source .venv/bin/activate`

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

Run the head pose estimation script:

```
python head_pose_estimation.py
```

This will open a window showing your webcam feed with head pose visualization. Press ESC to exit.

## How it works

The script uses MediaPipe to detect facial landmarks and OpenCV's solvePnP to estimate the 3D head pose from 2D landmarks. It draws the pose axes on the face.

## Troubleshooting

- If the camera doesn't open, check that your webcam is connected and not used by another application.
- If imports fail, ensure all packages are installed in the virtual environment.
- For better accuracy, calibrate your camera and update the camera_matrix in the script.
