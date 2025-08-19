---

## Rock Paper Scissors Lizard Spock Game

**A GP106 Computing Project**
**Department of Computer Engineering, Faculty of Engineering, University of Peradeniya**
**Batch: E/21**

---

## 📌 Project Overview

This project extends the classic **Rock-Paper-Scissors** game by adding two extra gestures: **Lizard** and **Spock**, making the game more interesting and complex.

The game is implemented using an **Arduino UNO** with hardware components such as LEDs, push buttons, and a piezo buzzer.

---

## 🎮 Game Rules

* Rock **crushes** Scissors
* Scissors **cuts** Paper
* Paper **covers** Rock
* Rock **crushes** Lizard
* Lizard **poisons** Spock
* Spock **smashes** Scissors
* Scissors **decapitates** Lizard
* Lizard **eats** Paper
* Paper **disproves** Spock
* Spock **vaporizes** Rock

👉 The game runs for **7 rounds** against the computer. LEDs display the scores, while the buzzer provides sound feedback.

---

## 🛠️ Hardware Components

* Arduino UNO
* 10 LEDs (for scores & computer’s choices)
* Piezo buzzer (sound notifications)
* 6 Push buttons (5 gestures + Start/End)
* Breadboard, resistors, jumper wires

---

## ✨ Project Features

* **Real-Time Player vs Computer**: Play 7 rounds against the computer.
* **LED Score Display**: Scores shown in binary using LEDs.
* **Timed Input**: 3-second window for player input.
* **Buzzer Notifications**: Different tones for round start, win/lose, and game end.
* **Serial Monitor Support**: Displays round details and game summary.
* **Game End Indication**: After 7 rounds, all LEDs blink + buzzer alert.

---

## 📐 Circuit Diagram

The full circuit diagram is available in the folder.

---

## 🕹️ How to Play

1. **Start the Game** → Press the **Start** button.
2. **Choose Your Gesture** → Use the 5 input buttons (Rock, Paper, Scissors, Lizard, Spock).
3. **Computer’s Turn** → The computer randomly picks a gesture.
4. **View Results** → LEDs display the outcome and scores.
5. **End the Game** → Game ends automatically after 7 rounds or manually via the **End** button.


