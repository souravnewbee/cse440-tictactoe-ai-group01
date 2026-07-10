# 🎮 Tic-Tac-Toe AI — CSE 440 Project

**Course:** CSE 440 — Artificial Intelligence  
**Group:** 01 | **Section:** 02  
**Institution:** North South University  
**Semester:** Summer 2026

## 👥 Group Members

| Name | Student ID |
|------|------------|
| Sourav Roy | 2121856042 |
| Sudipta Karmakar | 2132245042 |
| Khatune Jannat | 2131916642 |
| Tabassum Tasnim Mridula | 2211451042 |

---

## 📌 Project Overview

This project implements an intelligent AI agent capable of playing **Tic-Tac-Toe** optimally against a human player. The core focus is on **game tree search algorithms**, specifically:

- **Minimax Algorithm** — for exhaustive game tree exploration
- **Alpha-Beta Pruning** — to optimize Minimax by cutting off unnecessary branches
- **Heuristic Functions** — to evaluate board states and improve AI performance

The goal is to build an AI that never loses, while also exploring how different heuristic strategies affect decision-making efficiency and speed.

---

## 🎯 Objectives

- Implement the classic Minimax algorithm for Tic-Tac-Toe
- Optimize with Alpha-Beta Pruning to reduce computation
- Design and compare different heuristic evaluation functions
- Analyze the performance improvements achieved through pruning and heuristics
- Provide a playable interface (CLI, later GUI) for human vs. AI gameplay

---

## 🛠️ Technologies & Tools

- **Language:** Python 3.x
- **Libraries:** *(to be finalized — Pygame/Tkinter for GUI in later weeks)*
- **Version Control:** Git & GitHub
- **Runtime environment for presentation:** GitHub Codespaces (see [Demo Day Instructions](#-demo-day-instructions-github-only))

---

## 📂 Project Structure

This repository follows the required course structure:

```
cse440-tictactoe-ai-group01/
│
├── main.py                 # Main entry point to run the project
├── README.md               # Project explanation (this file)
├── requirements.txt        # Tools/libraries needed to run the project
│
├── data/                    # Datasets (if any)
│
├── support/                 # Supporting code files
│   ├── game.py              # Core game logic & board representation
│   ├── minimax.py           # Minimax algorithm implementation
│   ├── alpha_beta.py        # Alpha-Beta Pruning implementation
│   └── heuristics.py        # Heuristic evaluation functions
│
└── others/                  # Reports, presentations & demo video
    ├── update_report.pdf        # Mid-project update report
    ├── update_presentation.pptx # Mid-project update presentation
    ├── final_report.pdf         # Final project report
    ├── final_presentation.pptx  # Final project presentation
    └── demo_video.mp4           # Project demo video
```

---

## 📅 Project Timeline & Task Division

### — 1st Half —

| Week | Milestone | Responsible |
|------|-----------|-------------|
| Week 1 | Repository setup, README, project structure | Sourav |
| Week 2 | Game board implementation, CLI, win/draw detection | Sudipta |
| Week 3 | Minimax algorithm implementation | Khatune Jannat |
| Week 4 | Alpha-Beta Pruning optimization | Tabassum |
| Week 5 | Full integration — complete playable Human vs AI (CLI) | Sourav |
| Week 6 *(Before 12th Class)* |finalize update report & update presentation; push everything to GitHub| All (report/slides) |

### 🎤 — 12th Class: Project Update Presentation — 🎤

### — 2nd Half —

| Week | Milestone | Responsible |
|------|-----------|-------------|

| Week 6 | Heuristic functions design & integration| Sudipta |
| Week 7 | Performance analysis — Minimax vs Alpha-Beta vs Heuristics (charts & data) | Tabassum |
| Week 8 | GUI (Pygame/Tkinter) | Sourav |
| Week 9 | Final report, final presentation, demo video | Khatune Jannat |

### 🎤 — Final Presentation — 🎤

---

## 🚀 Getting Started

```bash
# Clone the repository
git clone https://github.com/souravnewbee/cse440-tictactoe-ai-group01.git

# Navigate to the project directory
cd cse440-tictactoe-ai-group01

# Run the game
python main.py
```

---

## 🖥️ Demo Day Instructions (GitHub-only, no laptop/USB)

Presentations run **entirely from GitHub** — no personal laptops or USB drives allowed. Use **GitHub Codespaces** to run the code live from any classroom PC with a browser:

1. Go to the repo page → green **Code** button → **Codespaces** tab → **Create codespace on main**
2. Wait for the environment to load (can take 30–60 seconds — start this *before* your slot begins if possible)
3. In the Codespace terminal, run:
   ```bash
   python main.py
   ```
4. Slides (`others/update_presentation.pptx` or `final_presentation.pptx`) and reports (`others/*.pdf`) can be opened directly via GitHub's built-in file preview — no download needed
5. Demo video (`others/demo_video.mp4`) previews inline on GitHub if small enough; test this in advance

**⏱️ Group 1 presents first, in a strict 5-minute slot with no buffer — be logged into GitHub and ready to launch the Codespace the moment class starts.**

---

## 📖 References

- Russell, S., & Norvig, P. — *Artificial Intelligence: A Modern Approach*
- Minimax Algorithm — [Wikipedia](https://en.wikipedia.org/wiki/Minimax)
- Alpha-Beta Pruning — [Wikipedia](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning)

---

## 📝 License

This project is developed for academic purposes under CSE 440. All rights reserved by the group members.