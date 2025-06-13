# Catch Game based on reinforcement learning

A simple reinforcement learning environment for a 1D "Catch the Falling Object" game using Q-learning.

## 🧠 Purpose

Catch Game RL is a reinforcement learning project that simulates a 1D game where an agent learns to catch a falling object using the Q-learning algorithm. The purpose of this library is to demonstrate fundamental reinforcement learning concepts in a simple, interpretable environment.

It is ideal for:
	•	Beginners learning reinforcement learning
	•	Educators demonstrating Q-learning
	•	Developers experimenting with RL strategies in a minimal setup


## ⚙️ Functionality

The project provides:
	•	A grid-based game environment (CatchEnvironment) where an object falls and a basket moves to catch it.
	•	A Q-learning agent (QLearningAgent) that learns to optimize its actions via reward feedback.
	•	Visualization of agent performance using matplotlib.
	•	Console-based simulation of trained policies for quick feedback.

Key Features
	•	Temporal state representation
	•	Epsilon-greedy exploration with decay
	•	Training and testing modes
	•	Graphical plotting of results
	•	Easily extendable design


## 💻 System Requirements

To run this project, you’ll need:
	•	Python ≥ 3.7
	•	Visual Studio Code (VS Code)
	•	The following Python packages:
	•	numpy
	•	matplotlib


## 🛠️ Installation Guide for Visual Studio Code (VS Code)

Step 1: Install Visual Studio Code

Download and install VS Code from: https://code.visualstudio.com

Step 2: Install Python and Git
	•	Download Python from: https://www.python.org/downloads/
	•	Install Git from: https://git-scm.com

Ensure both are added to your system PATH.

Step 3: Clone or Download the Project

If you downloaded the ZIP:
	1.	Unzip the file
	2.	Open the folder in VS Code:

File → Open Folder → Select "catch_game_rl"

Or use Git:

git clone https://github.com/your-username/catch_game_rl.git
cd catch_game_rl
code .

Step 4: Set Up the Python Environment

In VS Code:
	1.	Open the terminal (Ctrl + `` )
	2.	Create a virtual environment:

python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\\Scripts\\activate


	3.	Install the package in editable mode:

pip install -e .



Step 5: Install VS Code Python Extension

If prompted, install the Python extension for VS Code from Microsoft. It provides:
	•	IntelliSense
	•	Code navigation
	•	Virtual environment detection
	•	Debugging tools


## 🚀 Run the Example

Run the example training script:

python examples/run_training.py

You’ll see training output in the console and performance plots at the end.


## Analogy
Think of the agent as a child learning to catch a ball:

At first, the child randomly moves their hands and misses the ball.
Each time they catch the ball, they remember what worked (positive reward).
Over time, they learn to position their hands correctly to catch the ball more often.
Why This is Cool
Reinforcement learning is a way for computers to learn from experience, just like humans do. This simple game demonstrates how an agent can learn to make decisions without being explicitly told what to do.
