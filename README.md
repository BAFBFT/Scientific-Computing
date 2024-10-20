# Wave Propagation Simulation
![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
![NumPy](https://img.shields.io/badge/Numpy-777BB4?style=for-the-badge&logo=numpy&logoColor=white)


This project simulates the propagation of a wave over a 2D grid using the finite-difference method to solve the wave equation. The result is visualized as a heatmap animation, showing the displacement of the wave over time.

## Features

- 2D wave equation solver
- Heatmap visualization of the wave propagation
- Animation of the wave propagation

## Output Plot
Below is a gif showing the output from the simualtion.  
![Output Plot](https://github.com/BAFBFT/Wave-equation-simulation/blob/main/wave_simulation.gif)

## Stability Condition

The Courant-Friedrichs-Lewy (CFL) condition is enforced in this project to ensure the stability of the finite-difference method used. The CFL condition is checked in the code, and an assertion is made to prevent violation. [CFL condition](https://en.wikipedia.org/wiki/Courant%E2%80%93Friedrichs%E2%80%93Lewy_condition)

## Requirements

- Python 3.x
- Numpy
- Matplotlib

You can install the required packages using:

```bash
pip install matplotlib
pip install numpy 
