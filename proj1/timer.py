# Author: Group 25 Brett Irvin, Aleksandr Balab, Dane Schoonover
# Date: 23/01/2016
# Description: This program contains four algorithms which use
# various approaches to find the max sub array from a larger array.


from algos import algorithm1, algorithm2, algorithm3, algorithm4
import os
import sys
import re
import algos
import random
from time import time

# GLOBAL
MIN = 1
MAX = 1000

def randArray(n):
  t0 = time()
  arr1 = []
  for i in xrange(10):
    arr2 = []
    for j in xrange(n):
      arr2.append(random.randint(MIN, MAX))
    arr1.append(arr2)
  t1 = time()
  return arr1

def main():
  global mainArray

  print "Enumeration:" 
  for k in [100, 150, 200, 250, 300, 350, 400, 450, 500, 550]:
    mainArray = randArray(k)
    time = 0
    tests = len(mainArray)
    for j in xrange(len(mainArray)):
      maxSum = 0
      maxSubArray = []
      array = mainArray[j]
      (maxSum, maxSubArray, runTime) = algorithm1(array)
      time += runTime/10
    print time/10

  print "Better Enumeration:" 
  for k in [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]:
    mainArray = randArray(k)
    time = 0
    tests = len(mainArray)
    for j in xrange(len(mainArray)):
      maxSum = 0
      maxSubArray = []
      array = mainArray[j]
      (maxSum, maxSubArray, runTime) = algorithm2(array)
      time += runTime
    print time/10
  
  print "Divide and Conquer:" 
  for k in [20000, 40000, 60000, 80000, 100000, 120000, 140000, 160000, 180000, 200000]:
    mainArray = randArray(k)
    time = 0
    tests = len(mainArray)
    for j in xrange(len(mainArray)):
      maxSum = 0
      maxSubArray = []
      array = mainArray[j]
      (maxSum, maxSubArray, runTime) = algorithm3(array)
      time += runTime
    print time/10
  
  print "Linear Time:" 
  for k in [200000, 400000, 600000, 800000, 1000000, 1200000, 1400000, 1600000, 1800000, 2000000]:
    mainArray = randArray(k)
    time = 0
    tests = len(mainArray)
    for j in xrange(len(mainArray)):
      maxSum = 0
      maxSubArray = []
      array = mainArray[j]
      (maxSum, maxSubArray, runTime) = algorithm4(array)
      time += runTime
    print time/10

if __name__ == "__main__":
  main()
