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


## How the Code Works
Environment Setup:

The CatchEnvironment class creates the grid and handles the falling object and basket movements.
It also calculates rewards based on whether the basket catches the object.
Agent's Brain:

The QLearningAgent class is the agent's "brain."
It uses a table (called a Q-table) to store information about the best moves for different situations.
The agent updates this table as it plays the game and learns.
Training the Agent:

The agent plays the game thousands of times (EPISODES = 2000).
During each game, it tries different moves, observes the rewards, and updates its Q-table to improve.
Testing the Agent:

After training, the agent plays a few test games to show how well it has learned.
You can watch the basket move and see whether it catches the object.
Visualizing Progress:

The code plots a graph showing how the agent's success rate improves over time.

## Analogy
Think of the agent as a child learning to catch a ball:

At first, the child randomly moves their hands and misses the ball.
Each time they catch the ball, they remember what worked (positive reward).
Over time, they learn to position their hands correctly to catch the ball more often.
Why This is Cool
Reinforcement learning is a way for computers to learn from experience, just like humans do. This simple game demonstrates how an agent can learn to make decisions without being explicitly told what to do.
