# Ghostbusters and Bayes Nets

A project implementing probabilistic inference using Bayes Nets to track invisible ghosts in a Pacman game.

## Project Overview

In this project, Pacman hunts down scared but invisible ghosts. Pacman is equipped with sonar (ears) that provides noisy readings of the Manhattan distance to each ghost. The game ends when Pacman has eaten all the ghosts.

The primary task is to implement inference algorithms to track the ghosts using Bayes Nets, which provide powerful tools for making the most of the information we have.

## Implemented Features

### Question 1: Bayes Net Structure (2 points)
- **File**: `inference.py`
- **Function**: `constructBayesNet(gameState)`
- Constructs the structural components of a Bayes Net for the ghost hunting world
- Creates variables for Pacman, Ghost0, Ghost1, Observation0, and Observation1
- Sets up edges and variable domains according to the project specification

### Question 2: Join Factors (3 points)
- **File**: `factorOperations.py`
- **Function**: `joinFactors(factors)`
- Implements the product rule for joining factors
- Combines multiple factors by multiplying corresponding probability entries
- Handles both conditioned and unconditioned variables correctly

### Question 3: Eliminate Variables (2 points)
- **File**: `factorOperations.py`
- **Function**: `eliminate(factor, eliminationVariable)`
- Implements variable elimination (marginalization)
- Sums over all values of the eliminated variable
- Returns a new factor without the eliminated variable

## Running the Project

### Play the Game
```bash
python busters.py
```

### Run Tests
```bash
# Run all tests for a specific question
python autograder.py -q q1
python autograder.py -q q2
python autograder.py -q q3

# Run a specific test
python autograder.py -t test_cases/q1/1-small-board

# Run without graphics (faster)
python autograder.py -q q1 --no-graphics
```

### Explore Bayes Nets
```bash
python bayesNet.py
```

## Project Structure

- `inference.py` - Main inference algorithms and Bayes Net construction
- `factorOperations.py` - Factor operations (join, eliminate)
- `bayesNet.py` - Bayes Net and Factor class implementations
- `busters.py` - Main game file for Ghostbusters
- `test_cases/` - Test cases for each question
- `layouts/` - Game layout files

## Testing

All implemented questions pass their respective test suites:
- ✅ Question 1: 2/2 points
- ✅ Question 2: 3/3 points
- ✅ Question 3: 2/2 points

## License

Licensing Information: You are free to use or extend these projects for educational purposes provided that (1) you do not distribute or publish solutions, and (2) you retain this notice.
