# factorOperations.py
# -------------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).

from typing import List
from bayesNet import Factor
import functools
from util import raiseNotDefined

def joinFactorsByVariableWithCallTracking(callTrackingList=None):


    def joinFactorsByVariable(factors: List[Factor], joinVariable: str):
        """
        Input factors is a list of factors.
        Input joinVariable is the variable to join on.

        This function performs a check that the variable that is being joined on
        appears as an unconditioned variable in only one of the input factors.

        Then, it calls your joinFactors on all of the factors in factors that
        contain that variable.

        Returns a tuple of
        (factors not joined, resulting factor from joinFactors)
        """

        if not (callTrackingList is None):
            callTrackingList.append(('join', joinVariable))

        currentFactorsToJoin =    [factor for factor in factors if joinVariable in factor.variablesSet()]
        currentFactorsNotToJoin = [factor for factor in factors if joinVariable not in factor.variablesSet()]

        # typecheck portion
        numVariableOnLeft = len([factor for factor in currentFactorsToJoin if joinVariable in factor.unconditionedVariables()])
        if numVariableOnLeft > 1:
            print("Factor failed joinFactorsByVariable typecheck: ", factor)
            raise ValueError("The joinBy variable can only appear in one factor as an \nunconditioned variable. \n" +
                               "joinVariable: " + str(joinVariable) + "\n" +
                               ", ".join(map(str, [factor.unconditionedVariables() for factor in currentFactorsToJoin])))

        joinedFactor = joinFactors(currentFactorsToJoin)
        return currentFactorsNotToJoin, joinedFactor

    return joinFactorsByVariable

joinFactorsByVariable = joinFactorsByVariableWithCallTracking()

########### ########### ###########
########### QUESTION 2  ###########
########### ########### ###########

def joinFactors(factors: List[Factor]):
    """
    Input factors is a list of factors.

    You should calculate the set of unconditioned variables and conditioned
    variables for the join of those factors.

    Return a new factor that has those variables and whose probability entries
    are product of the corresponding rows of the input factors.

    You may assume that the variableDomainsDict for all the input
    factors are the same, since they come from the same BayesNet.

    joinFactors will only allow unconditionedVariables to appear in
    one input factor (so their join is well defined).

    Hint: Factor methods that take an assignmentDict as input
    (such as getProbability and setProbability) can handle
    assignmentDicts that assign more variables than are in that factor.

    Useful functions:
    Factor.getAllPossibleAssignmentDicts
    Factor.getProbability
    Factor.setProbability
    Factor.unconditionedVariables
    Factor.conditionedVariables
    Factor.variableDomainsDict
    """

    # typecheck portion
    setsOfUnconditioned = [set(factor.unconditionedVariables()) for factor in factors]
    if len(factors) > 1:
        intersect = functools.reduce(lambda x, y: x & y, setsOfUnconditioned)
        if len(intersect) > 0:
            print("Factor failed joinFactors typecheck: ", factor)
            raise ValueError("unconditionedVariables can only appear in one factor. \n"
                    + "unconditionedVariables: " + str(intersect) +
                    "\nappear in more than one input factor.\n" +
                    "Input factors: \n" +
                    "\n".join(map(str, factors)))


    "*** YOUR CODE HERE ***"
    # Step 1: Convert input to a list (handles different input types like dict_values)
    factors = list(factors)

    # Step 2: Check that we have at least one factor to join
    if len(factors) == 0:
        raise ValueError("joinFactors requires at least one factor")

    # Step 3: Get the variable domains dictionary
    # All factors come from the same Bayes Net, so they share the same domains
    variableDomainsDict = factors[0].variableDomainsDict()

    # Step 4: Determine which variables will be unconditioned in the result
    # Rule: A variable is unconditioned if it's unconditioned in ANY input factor
    # Example: joinFactors(P(X|Y), P(Y)) -> X and Y are both unconditioned in result
    unconditionedVars = set()
    for factor in factors:
        unconditionedVars.update(factor.unconditionedVariables())

    # Step 5: Determine which variables will be conditioned in the result
    # Rule: A variable is conditioned if it's conditioned in ANY input factor,
    #       BUT NOT if it's unconditioned in the result (from step 4)
    # Example: joinFactors(P(X|Y,Z), P(Y)) -> X and Y are unconditioned, Z is conditioned
    conditionedVars = set()
    for factor in factors:
        conditionedVars.update(factor.conditionedVariables())

    # Remove variables that became unconditioned (they can't be both)
    conditionedVars = conditionedVars - unconditionedVars

    # Step 6: Create a new factor with the calculated variables
    resultFactor = Factor(list(unconditionedVars), list(conditionedVars), variableDomainsDict)

    # Step 7: Fill in the probability table using the product rule
    # For each row in the result factor, multiply the probabilities from all input factors
    # This implements: P(A, B, C) = P(A|B) * P(B) when joining those factors
    for assignmentDict in resultFactor.getAllPossibleAssignmentDicts():
        product = 1.0
        for factor in factors:
            # getProbability can handle assignmentDicts with extra variables
            # (it just ignores variables not in that factor)
            product *= factor.getProbability(assignmentDict)
        resultFactor.setProbability(assignmentDict, product)

    return resultFactor
    "*** END YOUR CODE HERE ***"

########### ########### ###########
########### QUESTION 3  ###########
########### ########### ###########

def eliminateWithCallTracking(callTrackingList=None):

    def eliminate(factor: Factor, eliminationVariable: str):
        """
        Input factor is a single factor.
        Input eliminationVariable is the variable to eliminate from factor.
        eliminationVariable must be an unconditioned variable in factor.

        You should calculate the set of unconditioned variables and conditioned
        variables for the factor obtained by eliminating the variable
        eliminationVariable.

        Return a new factor where all of the rows mentioning
        eliminationVariable are summed with rows that match
        assignments on the other variables.

        Useful functions:
        Factor.getAllPossibleAssignmentDicts
        Factor.getProbability
        Factor.setProbability
        Factor.unconditionedVariables
        Factor.conditionedVariables
        Factor.variableDomainsDict
        """
        # autograder tracking -- don't remove
        if not (callTrackingList is None):
            callTrackingList.append(('eliminate', eliminationVariable))

        # typecheck portion
        if eliminationVariable not in factor.unconditionedVariables():
            print("Factor failed eliminate typecheck: ", factor)
            raise ValueError("Elimination variable is not an unconditioned variable " \
                            + "in this factor\n" +
                            "eliminationVariable: " + str(eliminationVariable) + \
                            "\nunconditionedVariables:" + str(factor.unconditionedVariables()))

        if len(factor.unconditionedVariables()) == 1:
            print("Factor failed eliminate typecheck: ", factor)
            raise ValueError("Factor has only one unconditioned variable, so you " \
                    + "can't eliminate \nthat variable.\n" + \
                    "eliminationVariable:" + str(eliminationVariable) + "\n" +\
                    "unconditionedVariables: " + str(factor.unconditionedVariables()))

        "*** YOUR CODE HERE ***"
        # Step 1: Get the variable domains dictionary (stays the same)
        # This tells us what values each variable can take
        variableDomainsDict = factor.variableDomainsDict()

        # Step 2: Determine the variables in the result factor
        # After eliminating a variable, it's removed from unconditioned variables
        # Example: eliminate(P(X, Y | Z), Y) -> result has X unconditioned, Z conditioned
        unconditionedVars = set(factor.unconditionedVariables())
        unconditionedVars.remove(eliminationVariable)

        # Conditioned variables stay the same (we only eliminate unconditioned variables)
        conditionedVars = set(factor.conditionedVariables())

        # Step 3: Create a new factor without the variable we're eliminating
        resultFactor = Factor(list(unconditionedVars), list(conditionedVars), variableDomainsDict)

        # Step 4: Fill in probabilities using marginalization (summing out the variable)
        # For each row in the result, we sum over all possible values of the eliminated variable
        # Example: If eliminating Y from P(X, Y), we compute P(X) = sum over all Y values of P(X, Y)
        for assignmentDict in resultFactor.getAllPossibleAssignmentDicts():
            sum_prob = 0.0
            # Sum over all possible values that the eliminated variable can take
            for eliminationValue in variableDomainsDict[eliminationVariable]:
                # Create a full assignment that includes the eliminated variable
                # This lets us look up the probability in the original factor
                fullAssignmentDict = assignmentDict.copy()
                fullAssignmentDict[eliminationVariable] = eliminationValue
                # Add this probability to our sum
                sum_prob += factor.getProbability(fullAssignmentDict)
            # Set the summed probability in the result factor
            resultFactor.setProbability(assignmentDict, sum_prob)

        return resultFactor
        "*** END YOUR CODE HERE ***"

    return eliminate

eliminate = eliminateWithCallTracking()
