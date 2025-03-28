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

### **Clone the Repository**
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

---

## 🎮 How It Works

1️⃣ **Click "Start"** to begin a new session  
2️⃣ **Perform squats** (go below **90°** to count)  
3️⃣ **Live messages** appear based on squat depth  
4️⃣ **Squat count updates automatically**  
5️⃣ **Click "Stop"** to end the session and **reset**  

---

## 🔥 Future Enhancements

- 📊 **Session Analysis** – Show best depth, average squat speed  
- 📅 **Database Integration** – Track user progress over time  
- 🏆 **Leaderboard System** – Compare squat counts with others  
