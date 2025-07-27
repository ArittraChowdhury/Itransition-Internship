# Task 3

# 🎲 Non-Transitive Dice Game – Task #3

This is my implementation of Task #3 from the programming assignment. The game simulates a generalised **non-transitive dice game** using secure, **HMAC-based fair random generation**, and allows for arbitrary dice configurations via **command line arguments**.

---

## 📌 Features

- 🎲 Accepts 3 or more dice as CLI arguments, each with custom face values
- 🔐 Implements a **provably fair random number protocol** using HMAC and SHA3-256
- 🧠 Uses modular classes with clear responsibilities (parser, game logic, crypto, etc.)
- 📊 Includes a help table displaying **win probabilities** for each dice pair
- ✅ Handles invalid inputs gracefully with helpful messages
- 👨‍💻 Fully console-based CLI menu with interactive user input

---

## 🏁 How to Run

### 🔧 Requirements
- Python 3.8 or above
- `tabulate` library for ASCII table display

Install required dependency:
```bash
pip install tabulate
Run program-> python main.py
📖 Game Flow
A fair coin flip (0 or 1) decides who picks a die first — proven with HMAC.
First player selects a die.
The second player picks a different die.
Both players roll — each roll uses a fair random generation protocol:
HMAC commitment → user input → key reveal → result = (comp + user) % N
The winner is determined by comparing dice roll results.
User enter? for a probability help table or X to exit at any time.

