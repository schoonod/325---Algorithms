# Author: Group 25 Brett Irvin, Aleksandr Balab, Dane Schoonover
# Date: 23/01/2016
# Description: This program contains four algorithms which use
# various approaches to find the max sub array from a larger array.

from time import time
import os
import sys
import re

# GLOBAL
maxSubArrayArray = []

###############
# Largest sum between left and right subarray
def maxLeftRight(left, right):
  if  left > right: return left
  else: return right


###############
# Largest sum between leftRight and middle
def maxLeftRightMiddle(left, right, middle): return maxLeftRight(maxLeftRight(left, right), middle)

###############
# Largest sum of two arrays
def maxMiddleSum(array, low, mid, high):

  # Left array
  sum = 0
  leftSum = 0
  for i in xrange(mid, low-1, -1):
    sum += array[i]
    if sum > leftSum:
      leftSum = sum

  # Right array
  sum = 0
  right = 0
  for i in xrange(mid+1, high+1, 1):
    sum += array[i]
    if sum > right:
      right = sum

  return (leftSum + right)

###############
def maxSubArray(array, low, high):
  # BASE CASE
  if low == high:
    return array[low] 
  
  mid = (low + high) / 2

  # Return the maximum of left sum, right sum, and combined(middle) sum
  return maxLeftRightMiddle(maxSubArray(array, low, mid), maxSubArray(array, mid+1, high),(maxMiddleSum(array, low, mid, high)))

# Enumeration
def algorithm1(array):
  global maxSubArrayArray
  
  actualMaxArray = []
  currentMaxArray = []
  maxSum = 0
  curSum = 0
  t0 = time()
 
  for i in xrange(0, len(array)):
    for k in xrange(0, len(array)):
      for m in xrange(i, k+1):
        curSum += array[m]
        currentMaxArray.append(array[m])
      if curSum > maxSum:
        maxSum = curSum
        actualMaxArray = currentMaxArray
        currentMaxArray = []
      else:
        currentMaxArray = []
      curSum = 0
  
  t1 = time()
  runTime = t1 - t0
  
  return (maxSum, actualMaxArray, runTime)
  
# Better Enumeration
def algorithm2(array):
  maxSumIndexes = [0,0]
  maxSumArrayArray = []
  maxSum = 0
  curSum = 0
  t0 = time()
    
  for i in xrange(0, len(array)):
    curSum = 0
    for k in xrange(i, len(array)):
      curSum += array[k]
      if curSum > maxSum:
        maxSum = curSum
        maxSumIndexes = [i,k]
  
  t1 = time()
  runTime = t1 - t0
 
  for x in xrange(maxSumIndexes[0], maxSumIndexes[1]+1):
    maxSumArrayArray.append(array[x])
  
  return (maxSum, maxSumArrayArray, runTime)

# Divide and Conquer
def algorithm3(array):
  maxSum = 0
  maxSumArrayArray = []
  t0 = time()  
  
  maxSum = maxSubArray(array, 0, len(array)-1)
  t1 = time()
  runTime = t1 - t0
  
  maxSumArrayArray = algorithm4(array)[1]
  return (maxSum, maxSumArrayArray, runTime)

# Linear time
def algorithm4(array):
  firstIndex = 0
  maxFirstIndex = 0
  maxLastIndex = 0
  maxSum = 0
  curSum = 0
  maxSubArray = []
  t0 = time()

  for i in xrange(0, len(array)):
    if curSum + array[i] < 0:
      firstIndex = i+1
      curSum = 0
    else:
      curSum = curSum + array[i]

    if maxSum < curSum:
      maxFirstIndex = firstIndex
      maxLastIndex = i
      maxSum = curSum

  t1 = time()
  runTime = t1 - t0
  
  for i in xrange(maxFirstIndex, maxLastIndex + 1):
    maxSubArray.append(array[i])
  
  return (maxSum, maxSubArray, runTime)




