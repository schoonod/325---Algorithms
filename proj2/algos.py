from main import *

####### CHANGESLOW #######
def executeChangeSlow():
  global coinDenom, A
  solution = []
  solution = changeSlow(coinDenom, A)
  print "The solution is: " + str(solution)
  print "Total number of coins: " + str(solutionCoinSum(solution))
  return (solution, solutionCoinSum(solution))

# The actual changeSlow algorithm is here
def changeSlow(coinDenom, k):
  # coinDenom = The list containing coin values
  # A = The value we are trying to make using various coins
  numberOfUniqueCoins = len(coinDenom)
  localSolution = []
  
  # Base Case:
  for i in xrange(0, numberOfUniqueCoins):
    if coinDenom[i] == k:
      # Create a list of size "numberOfUniqueCoins"
      localSolution = [0] * numberOfUniqueCoins
      localSolution[i] = 1
      return localSolution
  
  # Otherwise:
  localSolution = [0] * numberOfUniqueCoins
  # Replace sys.maxint with sys.maxsize in Python v3.0
  minimumNumberOfCoins = sys.maxint
  for i in xrange(1, k/2+1):
    localSolution1 = changeSlow(coinDenom, i)
    localSolution2 = changeSlow(coinDenom, k-i)
    latestCoinCount = calculateCoinCount(localSolution1, localSolution2)
    if latestCoinCount < minimumNumberOfCoins:
      minimumNumberOfCoins = latestCoinCount
      localSolution = sumBothSolutions(localSolution1, localSolution2)
  return localSolution

####### CHANGEGREEDY #######
def executeChangeGreedy():
  solution = []
  solution = changeGreedy(coinDenom, A)
  print "The solution is: " + str(solution)
  print "Total number of coins: " + str(solutionCoinSum(solution))
  return (solution, solutionCoinSum(solution))

# The greed algorithm. I believe it has an asymptotic runtime of O(coinDenom*k)
def changeGreedy(coinDenom, k):
  localSolution = [0] * len(coinDenom)
  for i in xrange(len(coinDenom)-1, -1, -1):
    if coinDenom[i] <= k:
      localSolution[i] = 1
      k -= coinDenom[i]
      break
  # Check for Base Case
  if k == 0:
    return localSolution
  # Otherwise, recurse further
  else:
    remainingSolution = changeGreedy(coinDenom, k)
    return sumBothSolutions(localSolution, remainingSolution)




####### CHANGEDP #######
# Kicks off the changedp algoithm (Dynamic Programming Method)
def executeChangedp():
  global coinDenom, A, C, Cv
  solution = [0] * len(coinDenom)
  C = [sys.maxint] * (A+1)
  Cv = [0] * (A+1)
  # Calculate every value in C[] from the bottom-up.
  # This allows you to use previous values to find future values.
  for i in xrange(0, A+1):
    C[i] = changedp(coinDenom, i)
    #print "%d = %d" % (i, C[i])
  j = A
  while j > 0:
    for w in xrange(0, len(coinDenom)):
      if Cv[j] == coinDenom[w]:
        solution[w] += 1
        j -= coinDenom[w]
  print "The solution is: " + str(solution)
  print "Total number of coins: " + str(C[A])
  return (solution, C[A])

def changedp(coinDenom, k):
  global Cv
  coins = []
  tempCv = []
  if k == 0:
    return 0
  for i in xrange(0, len(coinDenom)):
    if coinDenom[i] <= k:
      if C[k - coinDenom[i]] < sys.maxint:
        coins.append(C[k - coinDenom[i]])
        tempCv.append(coinDenom[i])
      
  minCoin = min(coins)
  for i in xrange(0, len(coins)):
    if coins[i] == minCoin:
      minCoinIdx = i
      break
  Cv[k] += tempCv[minCoinIdx]

  return 1 + minCoin