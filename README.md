# 🖐️ Hand Mouse – Gesture Controlled Computer Interaction 🖱️

**Author:** Sayani Das (Sia)  
**Date:** 2025  

---

## ✨ Overview
Hand Mouse is a **real-time gesture-controlled mouse** using your webcam. It allows you to:  

- 🖱️ Move your cursor  
- 👆 Left click  
- 🤏 Right click  
- 📜 Scroll  

Built with **Python, OpenCV, MediaPipe, and PyAutoGUI**, it transforms your hand into a fully functional mouse. Perfect for **touchless interactions**, accessibility solutions, or just flexing your hand-magic skills 💖.

---

## 🚀 Features
- 👆 **Cursor Movement:** Move your mouse by moving your index finger.  
- 🤏 **Left Click:** Pinch thumb + index finger → triggers left click.  
- ✌️ **Right Click:** Pinch thumb + middle finger → triggers right click.  
- 📜 **Scroll:** Move hand up/down with index + middle finger → scroll page.  
- ⏱️ **Cooldown Logic:** Prevents click spamming for smooth experience.  
- 👀 **Visual Feedback:** Circles appear on detected fingertips.  

---

## 🛠️ Tech Stack / Libraries
- Python 3.12+  
- OpenCV → Webcam feed & drawing landmarks  
- MediaPipe → Hand landmark detection  
- PyAutoGUI → Cursor movement, click, scroll  
- NumPy → Coordinate mapping  
- Math → Distance calculations  

---

## 🧠 How It Works
1. 🎥 Webcam captures your hand.  
2. 🤖 MediaPipe detects hand landmarks.  
3. 🖐️ Index + thumb/middle fingertips are tracked.  
4. 📏 Distance between fingertips is calculated:  
   - 👆 Thumb + index < threshold → left click  
   - ✌️ Thumb + middle < threshold → right click  
5. 🖱️ Cursor follows index fingertip (coordinate interpolation).  
6. 📜 Vertical movement of index + middle finger → scroll up/down.  
7. ⏱️ Cooldown prevents click spamming.  

---


## ▶️ How to Run


- Show your hand in front of the webcam  
- Perform gestures to control the mouse  
- Press **q** to quit the application  


---


## ⚠️ Limitations

- Requires good lighting conditions  
- Accuracy may reduce with complex backgrounds  
- Supports single-hand detection  

---

## 🌱 Future Enhancements

- Keyboard control using gestures  
- Multi-hand detection  
- Gesture customization panel  
- Improved accuracy using ML models  

---

## ❤️ Acknowledgements

- Google **MediaPipe**
- OpenCV Community
- Python Open Source Contributors

---

Built with 💖 by Sia

