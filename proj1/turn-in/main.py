# Author: Group 25 Brett Irvin, Aleksandr Balab, Dane Schoonover
# Date: 23/01/2016
# Description: This program contains four algorithms which use
# various approaches to find the max sub array from a larger array.

# IMPORTS
import os
import sys
import re
from algos import algorithm1, algorithm2, algorithm3, algorithm4

# GLOBAL
PROBLEM_FILE = "MSS_Problems.txt"
RESULTS_FILE = "MSS_Results.txt"
mainArray = []
maxSubArrayArray = []
infile = open(PROBLEM_FILE, 'r')  #File containing all arrays to be tested
outfile = open(RESULTS_FILE, 'w')  #Outfile used as a temp file for arrays

###########################################################
# Utility function
# This function was derived from https://github.com/PeterRissberger/CS325/blob/master/enum1.py
# We did not know how to read/write/clean up files in python and time constraints dictated
# that we find a working solution to implement.

def scanInput():
  #Cleanup junk brackets and commas from file 
  string = infile.read()
  string = string.translate(None, '[],')  #Clean up junk commas and brackets from input
  outfile.write(string)
  outfile.seek(0)
    
  #Make array of arrays contained in infile
  with open('MSS_Results.txt') as f: 
    outerArray = []
    for line in f: 
      line = line.split() 
      if line: 
        line = [int(i) for i in line]
        outerArray.append(line)

  #Clean up outfile used as temp work file
  outfile.truncate(0)

  return outerArray
###########################################################

# MAIN PROGRAM
def main():
  global mainArray

  print "Correctness Test"
  # Read the test cases from the test file and save to global 2D array
  mainArray = scanInput()
  totalTests = len(mainArray)
  count = 0.0

  for j in xrange(len(mainArray)):
    maxSum = 0
    array = mainArray[j]
    maxSubArray = []
    string = 'array #%d' % (j+1,)
    (maxSum, maxSubArray, runTime) = algorithm1(array)
    outfile.write("-----------------------------------\n")
    outfile.write("Algorithm 1 Results for " + string + "\n")
    outfile.write("-----------------------------------\n")
    outfile.write("Original Array: " + str(array) + "\n")
    outfile.write("Maximum subarray: " + str(maxSubArray) + "\n")
    outfile.write("Maximum sum: " + str(maxSum) + "\n\n") 
    print "-----------------------------------"
    print "Algorithm 1 Results for " + string
    print "-----------------------------------"
    print "Original Array: " + str(array)
    print "Max SubArray: " + str(maxSubArray)
    print "Maximum Sum: " + str(maxSum)
    print "Runtime: " + str(runTime)  + "\n"
  
  for j in xrange(len(mainArray)):
    maxSum = 0
    array = mainArray[j]
    maxSubArray = []
    string = 'array #%d' % (j+1,)
    (maxSum, maxSubArray, runTime) = algorithm2(array)
    outfile.write("-----------------------------------\n")
    outfile.write("Algorithm 2 Results for " + string + "\n")
    outfile.write("-----------------------------------\n")
    outfile.write("Original Array: " + str(array) + "\n")
    outfile.write("Maximum subarray: " + str(maxSubArray) + "\n")
    outfile.write("Maximum sum: " + str(maxSum) + "\n\n") 
    print "-----------------------------------"
    print "Algorithm 2 Results for " + string
    print "-----------------------------------"
    print "Original Array: " + str(array)
    print "Max SubArray: " + str(maxSubArray)
    print "Maximum Sum: " + str(maxSum)
    print "Runtime: " + str(runTime)  + "\n"
  
  for j in xrange(len(mainArray)):
    maxSum = 0
    array = mainArray[j]
    maxSubArray = []
    string = 'array #%d' % (j+1,)
    (maxSum, maxSubArray, runTime) = algorithm3(array)
    outfile.write("-----------------------------------\n")
    outfile.write("Algorithm 3 Results for " + string + "\n")
    outfile.write("-----------------------------------\n")
    outfile.write("Original Array: " + str(array) + "\n")
    outfile.write("Maximum subarray: " + str(maxSubArray) + "\n")
    outfile.write("Maximum sum: " + str(maxSum) + "\n\n") 
    print "-----------------------------------"
    print "Algorithm 3 Results for " + string
    print "-----------------------------------"
    print "Original Array: " + str(array)
    print "Max SubArray: " + str(maxSubArray)
    print "Maximum Sum: " + str(maxSum)
    print "Runtime: " + str(runTime)  + "\n"

  for j in xrange(len(mainArray)):
    maxSum = 0
    array = mainArray[j]
    maxSubArray = []
    string = 'array #%d' % (j+1,)
    (maxSum, maxSubArray, runTime) = algorithm4(array)
    outfile.write("-----------------------------------\n")
    outfile.write("Algorithm 2 Results for " + string + "\n")
    outfile.write("-----------------------------------\n")
    outfile.write("Original Array: " + str(array) + "\n")
    outfile.write("Maximum subarray: " + str(maxSubArray) + "\n")
    outfile.write("Maximum sum: " + str(maxSum) + "\n\n") 
    print "-----------------------------------"
    print "Algorithm 2 Results for " + string
    print "-----------------------------------"
    print "Original Array: " + str(array)
    print "Max SubArray: " + str(maxSubArray)
    print "Maximum Sum: " + str(maxSum)
    print "Runtime: " + str(runTime)  + "\n"
    
if __name__ == "__main__":
  main()
