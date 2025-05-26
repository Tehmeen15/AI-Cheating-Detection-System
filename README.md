# Advanced Cheating Detection System

A sophisticated real-time cheating detection system that uses computer vision and facial landmark analysis to monitor students during exams. The system employs advanced eye tracking and gaze direction analysis to detect when students look away from their papers.

## Features

- Real-time face detection using dlib
- Advanced eye tracking using 68 facial landmarks
- Eye Aspect Ratio (EAR) calculation for precise eye state detection
- Gaze direction analysis to detect looking away behavior
- Multiple student monitoring support
- Live webcam feed with detailed status overlay
- Visual feedback with eye contours and measurements
- Real-time display of gaze angles and EAR values

## Technical Details

The system uses several advanced techniques:
- Eye Aspect Ratio (EAR) calculation to determine if eyes are open/closed
- Gaze direction analysis using facial landmark positions
- Contour-based eye tracking for better accuracy
- Real-time status updates with numerical measurements

## Prerequisites

- Python 3.8 or higher
- Webcam with good resolution
- Required Python packages (listed in requirements.txt)
- Good lighting conditions for optimal face detection

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd cheating-detection
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Download the required model files:
- The system uses the `shape_predictor_68_face_landmarks.dat` file for facial landmark detection
- Make sure this file is in the same directory as the main script

## Usage

1. Run the main script:
```bash
python "cheating detection.py"
```

2. The system will:
- Open your webcam feed
- Detect faces in real-time
- Track eye movements and gaze direction
- Calculate Eye Aspect Ratio (EAR)
- Display detailed status for each detected student including:
  - Gaze angle in degrees
  - EAR value
  - Current status (Focused/Looking away/Eyes closed)

3. Status Indicators:
- Green: Student is focused
- Red: Student is looking away or eyes are closed

4. To exit the program:
- Press 'q' on your keyboard

## Detection Parameters

The system uses the following thresholds:
- EAR (Eye Aspect Ratio) < 0.2: Indicates eyes might be closed
- Gaze angle > 30 degrees: Indicates looking away from the paper
- These values can be adjusted in the code based on specific requirements

## Notes

- The system requires good lighting conditions for optimal face detection
- Make sure your webcam is properly connected and accessible
- The facial landmark predictor file (`shape_predictor_68_face_landmarks.dat`) must be present in the project directory
- For best results, ensure students are facing the camera directly
- The system works best when students maintain a consistent distance from the camera

## License

This project is licensed under the MIT License - see the LICENSE file for details. 