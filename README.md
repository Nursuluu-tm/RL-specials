# Catch Game RL

A simple reinforcement learning environment for a 1D "Catch the Falling Object" game using Q-learning.

This script implements a simple reinforcement learning agent using the Q-learning algorithm
to solve a 1D grid-based "Catch the Falling Object" game.

The environment is a vertical grid where a single object falls from the top to the bottom
over a series of time steps. At the bottom row, a basket can move left, right, or stay in
place to catch the falling object. The agent is trained to learn optimal movements of the 
basket to maximize successful catches.

Key Features:
-------------
- Q-learning algorithm with temporal state representation.
- Epsilon-greedy exploration strategy with decay.
- Modular design with CatchEnvironment and QLearningAgent classes.
- Console-based animation for testing the learned policy.
- Performance tracking and visualization using matplotlib.

Dependencies:
-------------
- numpy
- matplotlib
- Python 3.x standard libraries (random, time, os, collections)

Usage:
------
Simply run the script to train the agent, view animated test episodes,
and plot the learning progress.
See the example in `run_training.py`.

## Installation

```bash
pip install -e .
```


MIT
