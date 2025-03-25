# 🏋️ Squat Counter Project

A real-time **Squat Counter** using **Django, OpenCV, and Mediapipe**, which detects squats based on knee angles and provides live feedback.

## 🎯 Features
✅ **Real-Time Squat Detection** – Uses a webcam to track knee angle  
✅ **Automatic Squat Counting** – Counts only when depth ≤ 90°  
✅ **Live Feedback Messages** – Displays **"Go Deeper"**, **"Nice"**, **"Perfect"**  
✅ **Session-Based Tracking** – Each session resets on start  
✅ **Audio Feedback** – Plays a sound when a squat is completed  
✅ **Live Timer** – Tracks duration of workout  
✅ **Responsive UI** – Built using Django & Bootstrap  

---

## ⚙️ Tech Stack
- **Backend:** Django, Python  
- **Computer Vision:** OpenCV, Mediapipe  
- **Frontend:** HTML, CSS, JavaScript, Bootstrap  
- **Real-Time Updates:** Django Streaming (SSE)  

---

## 🚀 Installation Guide

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/YOUR_USERNAME/SquatAnalyzer.git
cd SquatAnalyzer

python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate      # Windows

pip install -r requirements.txt

python manage.py runserver
```

Go to http://127.0.0.1:8000/ and start squatting! 🏋️‍♂️🔥