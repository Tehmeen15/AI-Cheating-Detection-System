# 🎓 Advanced Cheating Detection System

A powerful real-time exam monitoring system that leverages computer vision and facial landmark detection to identify suspicious behavior during online assessments. This tool uses advanced eye tracking and gaze direction analysis to detect when students look away from their screens or close their eyes.

## 🚀 Key Features

- 🔍 Real-time face detection using `dlib`
- 👁️ 68-point facial landmark tracking for precision
- 📐 Eye Aspect Ratio (EAR) calculation to detect eye closure
- 👀 Gaze direction analysis to flag off-screen glances
- 👨‍🏫 Multi-student tracking and status reporting
- 📸 Live webcam feed with visual feedback and overlays
- 🧮 Real-time display of EAR and gaze angles
- 🎨 Colored status indicators (Focused / Looking Away / Eyes Closed)

## 🧠 How It Works

The system detects faces and landmarks in real time, then:
- Calculates the **Eye Aspect Ratio (EAR)** to determine if the eyes are closed
- Analyzes the **gaze direction** based on eye landmarks
- Flags students looking away or closing eyes during the session
- Displays each student's status and related measurements on screen

## 🛠️ Technical Highlights

- EAR threshold (default < `0.2`) for eye closure detection
- Gaze angle threshold (default > `30°`) for distraction detection
- Color-coded feedback:
  - 🟢 Focused
  - 🔴 Eyes closed or looking away

## 📦 Requirements

- Python 3.8+
- Webcam (HD preferred)
- Good ambient lighting
- Required libraries listed in `requirements.txt`
- `shape_predictor_68_face_landmarks.dat` model file from [dlib's official site](http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2)

## 🔧 Installation

1. **Clone the repository:**
```bash
git clone <repository-url>
cd cheating-detection
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Download the shape predictor model:**
- Download from: [http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2](http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2)
- Extract and place the `.dat` file in your project directory

## ▶️ Usage

1. **Run the script:**
```bash
python "cheating detection.py"
```

2. **Live feed actions:**
- Detects faces and eyes
- Tracks multiple students
- Displays status:
  - Gaze angle (in degrees)
  - EAR value
  - Focus status

3. **Controls:**
- Press `q` to exit the program

## ⚙️ Detection Parameters

You can tweak these thresholds in the script for better accuracy:
- `EAR < 0.2` → Eyes might be closed
- `Gaze angle > 30°` → Student is likely looking away

## 📌 Tips for Best Performance

- Ensure students are **facing the webcam directly**
- Maintain **good lighting** conditions
- Use a **stable webcam feed**
- Avoid low-resolution or grainy video

## 📄 License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

---

**Built with ❤️ by Tehmeen – AI & ML Developer**

🔗 [LinkedIn](www.linkedin.com/in/tehmeen-sajjad-a13866254) | 💼 [Fiverr](https://www.fiverr.com/official_codes)  
#AI #CheatingDetection #Python #ComputerVision #OpenCV #dlib #ExamProctoring

## ✅ Benefits

- Automates exam monitoring, reducing the need for manual invigilation
- Provides instant alerts for suspicious behaviors
- Enhances academic integrity in remote settings
- Easily adaptable to various environments and exam formats
- Can be extended to work with recorded videos and streaming platforms

## 💡 Use Cases

- Online exams and quizzes
- Remote proctoring platforms
- E-learning environments
- Virtual classrooms
- AI-based surveillance research

## 📞 Contact

For collaboration, customization, or freelance projects, feel free to reach out:

📧 Email: [tehmeen315@yahoo.com]  
🌐 Portfolio: [https://github.com/Tehmeen15]  
📱 LinkedIn: [https://www.linkedin.com/in/tehmeen-sajjad-a13866254]  
💼 Fiverr: [https://www.fiverr.com/official_codes]

---

🛡️ This project ensures fair assessment in a virtual education world, powered by AI.
