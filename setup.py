from setuptools import setup, find_packages

setup(
    name="catch_game_rl",
    version="0.1.0",
    description="Q-learning environment for a simple catch game.",
    author="Your Name",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "matplotlib"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
)
