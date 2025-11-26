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

### Question 4: Variable Elimination (2 points)
- **File**: `inference.py`
- **Function**: `inferenceByVariableElimination(bayesNet, queryVariables, evidenceDict, eliminationOrder)`
- Implements probabilistic inference using variable elimination algorithm
- Interleaves join and eliminate operations for efficiency
- More efficient than enumeration for large Bayes Nets

### Question 5a: DiscreteDistribution Class (0 points, required for later questions)
- **File**: `inference.py`
- **Methods**: `normalize()` and `sample()`
- `normalize()`: Normalizes distribution so values sum to 1, preserving proportions
- `sample()`: Performs weighted random sampling from the distribution

### Question 5b: Observation Probability (1 point)
- **File**: `inference.py`
- **Function**: `getObservationProb(noisyDistance, pacmanPosition, ghostPosition, jailPosition)`
- Calculates P(noisyDistance | pacmanPosition, ghostPosition)
- Handles special case when ghost is in jail (deterministic None observation)

### Question 6: Exact Inference Observation (2 points)
- **File**: `inference.py`
- **Function**: `observeUpdate(observation, gameState)` in `ExactInference` class
- Implements Bayesian belief update using the forward algorithm
- Updates beliefs based on noisy distance observations
- Uses the rule: P(GhostPosition | Observation) ∝ P(Observation | GhostPosition) × P(GhostPosition)

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
python autograder.py -q q4
python autograder.py -q q5
python autograder.py -q q6

# Run a specific test
python autograder.py -t test_cases/q1/1-small-board

# Run without graphics (faster)
python autograder.py -q q1 --no-graphics

# Run all implemented questions
python autograder.py -q q1 -q q2 -q q3 -q q4 -q q5 -q q6 --no-graphics
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
- ✅ Question 1: 2/2 points - Bayes Net Structure
- ✅ Question 2: 3/3 points - Join Factors
- ✅ Question 3: 2/2 points - Eliminate Variables
- ✅ Question 4: 2/2 points - Variable Elimination
- ✅ Question 5: 1/1 points - DiscreteDistribution and Observation Probability
- ✅ Question 6: 2/2 points - Exact Inference Observation

**Total: 12/12 points implemented**

## License

Licensing Information: You are free to use or extend these projects for educational purposes provided that (1) you do not distribute or publish solutions, and (2) you retain this notice.
