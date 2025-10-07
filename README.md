# Rubik's Cube Solver 

This project is a fully functional Rubik’s Cube solver written in Python using the beginner’s method. It takes a scrambled cube state as input - either manually or via webcam—and outputs a step-by-step sequence of moves to solve it.

## Features

- Solves any valid cube state using the standard beginner’s method  
- Optional OpenCV integration for scanning real-world cubes via webcam  
- Modular cube state representation with fully implemented move logic  
- Built entirely from scratch - no external solver libraries used  
- Clean, extensible codebase designed for educational or hobbyist expansion

## Getting Started

### Prerequisites
- Python 3.x
- `opencv-python` for webcam scanning (`pip install opencv-python`)
- `numpy`

### Usage

**Manual Input**
```bash
python3 main.py
# Follow the prompts to enter your cube state manually
```

**Webcam Input (optional)**
```bash
python3 scanner.py
# Use keyboard shortcuts to assign face colors
# Once captured, the solver will process the input and return a solution
```

## Folder Structure

- `main.py` — Core solver logic, cube state, and move functions
- `scanner.py` — OpenCV-based face scanner (optional)  

## Future Improvements

- Advanced algorithm integration (e.g., Kociemba)  
- Robot arm or motorized solving output  
- GUI or mobile interface  

**Created by Sean Harbison**  
Feel free to fork, contribute, or reach out!
