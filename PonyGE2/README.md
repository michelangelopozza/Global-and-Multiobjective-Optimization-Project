# Grammatical Evolution of Differential Equations

---

- **Author:** Michelangelo Pozza
- **Student ID:** IN2300012 
- **Course:** Global and Multiobjective Optimization

---

## Project Overview

This project investigates the effectiveness of _Grammatical Evolution (GE)_ applied to the problem of _Symbolic Regression_ for differential equations. The primary objective is to discover analytical expressions that can accurately approximate or reconstruct the physical laws governing specific dynamical systems, starting solely from observational data.

The project focuses on two physical systems:

- _Damped Single Pendulum_

- _Damped Double Pendulum (Chaotic system)_

#### Core Tasks

- **Modeling**: Define the physical systems governed by ordinary differential equations (ODEs).

- **Data Generation**: Simulate the systems using numerical integration (scipy.integrate.odeint) to generate "Ground Truth" datasets.

- **Evolution**: Use Grammatical Evolution to evolve algebraic and differential equations that match the generated data, defining specific grammars (.bnf) and fitness functions.

## Setup and Requirements

The project is implemented in _Python 3.10.12_ and utilizes the _PonyGE2_ evolutionary computation framework.

#### Prerequisites
- Python 3.10+

- NumPy, Pandas, SciPy, Matplotlib

#### Project Structure
The repository is organized as follows:

- **PonyGE2/**: The core library used for the evolutionary process.

- **PonyGE2/grammars/**: Contains the Backus-Naur Form (BNF) grammar files used to constrain the search space for the single and double pendulum.

- **PonyGE2/parameters/**: Configuration files defining the hyperparameters for the evolutionary runs.

- **PonyGE2/datasets/**: CSV files containing the simulated training data (Time, Angle, Angular Velocity).

- **PonyGE2/src/fitness/**: Custom fitness functions used to evaluate the quality of the evolved equations (typically MSE against the numerical simulation).

- **PonyGE2/src/**: Jupyter Notebooks for data generation and result visualization.

- **PonyGE2/results/**: This directory contains the output of all generations, including fitness evolution metrics. Due to the high computational cost of the experiments, some pre-computed results are provided.

#### References
- **PonyGE2 Documentation**: Available in PonyGE2.wiki or as PonyGE2.pdf.

- **Fenton et al. (2017)**: "PonyGE2: Grammatical Evolution in Python" (1703.08535v2.pdf).

## How to Execute
#### Data Generation & Visualization

To generate the training datasets and visualize the physics of the pendulums, open and run the following Jupyter Notebooks:

- _PonyGE2/src/single_pendulum_main.ipynb_

- _PonyGE2/src/double_pendulum_main.ipynb_

These notebooks perform numerical integration of the ODEs to generate the training datasets. Subsequently, they run the Grammatical Evolution algorithm and benchmark the evolved equations against the ground truth.

## PonyGE2 Configuration

For all experiments, the following evolutionary settings were standardized to ensure consistency.

#### Evolutionary Strategy
- **Initialization**: RHH (Ramped Half-and-Half)

- **Selection**: Tournament Selection

- **Crossover**: Subtree Crossover

- **Mutation**: Subtree Mutation

- **Replacement**: Generational

#### Hyperparameters
The parameter selection was driven by a literature review and the necessary trade-offs to ensure convergence towards the optimal solution while maintaining population diversity.

- **Crossover Probability**: Set between 0.75 and 0.9. High crossover ensures the recombination of good building blocks found in the population.

- **Mutation Probability**: Set between 0.1 and 0.2. This range allows for sufficient exploration of the search space without disrupting the evolutionary progress too aggressively.

- **Random Seed**: No fixed seeds were used; experiments are stochastic.

## Problem Description

#### Methodology

1. **Simulation**: We simulate $N$ data points over a time period $T$ based on the known Lagrangian mechanics of the systems.
2. **Grammar Definition**: We define a grammar that includes the necessary mathematical operators ($+, -, *, /, \sin, \cos$) and state variables ($x, \dot{x}$).
    - Note for Double Pendulum: To aid convergence, the grammar was designed to include specific physical insights (e.g., angular differences).
3. **Symbolic Regression**: The GE algorithm evolves a population of equation trees. The fitness of each individual is calculated by integrating the candidate equation and comparing the resulting trajectory with the training data.

---

_This document was partially created with the help of Gemini Pro (translation and structure)_