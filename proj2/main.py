# Author: Group 25 Brett Irvin, Aleksandr Balab, Dane Schoonover
# Date: 1/02/2016
# Description: This program has implementation for divide and conquer, greedy, and 
# dynamic programming soultions to the coin change problem.

import sys, os
from optparse import OptionParser

# Parser: https://docs.python.org/2/library/optparse.html
parser = OptionParser()
parser.add_option("-f", "--file", dest="filename", help="Enter input file name")
(options, args) = parser.parse_args()

# Variables
# The number of sets to run through               
inputArrays = 0   
# Array of coin denominations (aka V)
coinDenom  = []       
# Value to make change
A  = 0        
# Queue for V values        
stackInput = []
# Queue for A values
stackValue = [] 
# Stack Index      
stackTrack = 0  
# Optimal Array for changedp      
optimalArray  = []
# Value of subtracted V[i] in changeDP
tempCoinArray = []    


##### READ FILE
def readFile(filename):
  global stackInput, stackValue, inputArrays
  
  with open(filename) as f:
    # all lines in the file
    lines = f.readlines()
  
  # Step thru every other line
  for i in range(0, len(lines), 2):
    # Every other line starting from the first line
    inputArrays += 1
    tempV = lines[i].strip('\n')[1:-1]
    tempV = map(int, tempV.split(','))
    tempA = int(lines[i+1].strip('\n'))
    stackInput.append(tempV)
    stackValue.append(tempA)

##### SUM COINS OF SOLUTION
def sumCoins(solution):
  
  # Local
  sum = 0
  
  for coin in solution:
    sum += coin
  return sum

# Access coin sets and input value in sequence
def getNextSetFromQueue():
  global stackInput, stackValue, stackTrack
  curr = (stackInput[stackTrack], stackValue[stackTrack])
  return curr

# SAVE OUTPUT
def saveFile(filename, solution, m):
  f = open(filename[:-4] + "change.txt",'a')
  f.write(str(solution))
  f.write('\n')
  f.write(str(m))
  f.write('\n')
  f.close()

# SUM COINS FROM LOCAL SOLUTIONS
def localSumCoins(localSolution1, localSolution2):
  
  # Local
  coinCount = 0
  
  for coin in localSolution1: coinCount += coin
  for coin in localSolution2: coinCount += coin
  return coinCount

def sumBothSolutions(localSolution1, localSolution2):
  newSolution = [0] * len(localSolution1)
  for i in xrange(0, len(localSolution1)):
    newSolution[i] = localSolution1[i] + localSolution2[i]
  return newSolution

##### CHANGE SLOW 
def changeSlow():
  global coinDenom, A
  
  # Local
  optimal = []
  optimal = changeSlowAlgo(coinDenom, A)
  
  return (optimal, sumCoins(optimal))


def changeSlowAlgo(coinDenom, k):
  
  # Local
  numberOfUniqueCoins = len(coinDenom)
  localSolution = []

  for i in range(0, numberOfUniqueCoins):
    if coinDenom[i] == k:
      localSolution = [0] * numberOfUniqueCoins
      localSolution[i] = 1
      return localSolution
  
  localSolution = [0] * numberOfUniqueCoins
  minimumNumberOfCoins = sys.maxint
  for i in range(1, k/2+1):
    localSolution1 = changeSlowAlgo(coinDenom, i)
    localSolution2 = changeSlowAlgo(coinDenom, k-i)
    latestCoinCount = localSumCoins(localSolution1, localSolution2)
    
    # If the solutions have provided a new minimum coin count
    if latestCoinCount < minimumNumberOfCoins:
      minimumNumberOfCoins = latestCoinCount
      localSolution = sumBothSolutions(localSolution1, localSolution2)
  return localSolution


##### CHANGE GREEDY
def changeGreedy ():
  global V, A
  
  # Local
  optimal  = []
  optimal  = changeGreedyAlgo (coinDenom, A)
  
  return (optimal , sumCoins(optimal ))

def changeGreedyAlgo (coinDenom, k):
  localSolution = [0] * len(coinDenom)
  newSolution = [0] * len(localSolution)

  for i in range(len(coinDenom)-1, -1, -1):
    if coinDenom[i] <= k:
      localSolution[i] = 1
      k -= coinDenom[i]
      break

  # Determine if we have found optimum
  if k == 0:
    return localSolution
  else:
    remainingSolution = changeGreedyAlgo (coinDenom, k)
    for i in range(0, len(localSolution)):
      newSolution[i] = localSolution[i] + remainingSolution[i]
    return newSolution


##### CHANGE DP
def changeDpAlgo (coinDenom, k):
  global tempCoinArray
  
  # Local
  coins = []
  tempArray = []
  
  if k == 0:
    return 0
  for i in range(0, len(coinDenom)):
    if coinDenom[i] <= k:
      if optimalArray[k - coinDenom[i]] < sys.maxint:
        coins.append(optimalArray[k - coinDenom[i]])
        tempArray.append(coinDenom[i])
      
  minCoin = min(coins)
  for i in range(0, len(coins)):
    if coins[i] == minCoin:
      minCoinIdx = i
      break
  tempCoinArray[k] += tempArray[minCoinIdx]
  return 1 + minCoin

def changeDp ():
  global coinDenom, A, optimalArray, tempCoinArray

  # Local
  optimal  = [0] * len(coinDenom)
  optimalArray = [sys.maxint] * (A+1)
  tempCoinArray = [0] * (A+1)
  
  for i in range(0, A+1):
    optimalArray[i] = changeDpAlgo (coinDenom, i)
  j = A
  while j > 0:
    for w in range(0, len(coinDenom)):
      if tempCoinArray[j] == coinDenom[w]:
        optimal [w] += 1
        j -= coinDenom[w]
  return (optimal , optimalArray[A])

##### MAIN
def main():
  global inputArrays, coinDenom, A, stackTrack

  # Local
  optimal  = []
  m = 0

  # Create stackInput and stackValue queue
  readFile(options.filename)
  
  # Delete the file if it exists (for re-runs)
  if os.path.isfile(options.filename[:-4] + "change.txt"):
    os.system("rm " + options.filename[:-4] + "change.txt")

  for i in range(0, inputArrays):
    
    # print getNextSetFromQueue()
    (coinDenom, A) = getNextSetFromQueue()
    stackTrack += 1
    
    # Run changeSlow and save solution/minCoins
    (optimal , m) = changeSlow()
    saveFile(options.filename, optimal , m)
    
    # Run changeGreedy and save solution/minCoins
    (optimal , m) = changeGreedy ()
    saveFile(options.filename, optimal , m)
    
    # Run changeDp and save solution/minCoins
    (optimal , m) = changeDp ()
    saveFile(options.filename, optimal , m)

if __name__ == "__main__":
  main()