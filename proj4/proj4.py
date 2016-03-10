"""Awesome Codez"""

import os
import sys
import math

def get_file_contents(file):

    #2d array
    cityList = []

    # Get all of the lines from the file
    with open(file) as f:
        lines = f.readlines()

    # Get city data and create 2d array of cities and city data
    for line in lines:
        city = line.split()
        cityList.append(city)

    # Return array of city arrays
    return cityList

def calculate_distance(city1, city2):
    aSquared = (int(city1[1]) - int(city2[1]))**2
    bSquared = (int(city1[2]) - int(city2[2]))**2
    cSquared = math.sqrt(aSquared + bSquared)
    return int(round(cSquared))


def get_approx_path(cityArray):
    visitingCityOrder = [cityArray[0]]
    totalDistance = 0
    index = 1

    while (index < len(cityArray)):
            shortestDistance = 0
            closestCity = 0
            for city in cityArray:
                if city in visitingCityOrder:
                    continue

                # Calculate distance between last city in visiting city order and current city
                distance = calculate_distance(visitingCityOrder[-1], city)

                # If the current city has the shortest distance
                if distance < shortestDistance or shortestDistance == 0:
                    shortestDistance = distance
                    closestCity = city

            visitingCityOrder.append(closestCity)
            totalDistance += shortestDistance
            index += 1
    return totalDistance, visitingCityOrder

    # for index, mainCity in enumerate(cityArray):
    #     # Checks for the end of the Array
    #     if mainCity[0] in visitingCityOrder:
    #             continue
    #     if index >= len(cityArray) - 2:
    #         continue
    #
    #     closestCity = cityArray[index+1][0]
    #     shortestCityDistance = calculate_distance(mainCity, cityArray[index+1])
    #     print "SHORTEST CITY DISTANCE IS "
    #     print shortestCityDistance
    #
    #     for city in cityArray[index+1:]:
    #         if city[0] in visitingCityOrder:
    #             continue
    #         distance = calculate_distance(mainCity, city)
    #         print "DISTANCE IS "
    #         print distance
    #         if distance < shortestCityDistance:
    #             shortestCityDistance = distance
    #             closestCity = int(city[0])
    #             print "CLOSEST CITY IS "
    #             print closestCity
    #
    #     visitingCityOrder.append(closestCity)
    #     shortestPath += shortestCityDistance




if __name__ == '__main__':
    # Get input file; return 2d array of cities
    cities = get_file_contents(sys.argv[1])

    # Run algorithm based on city and coordinates
    shortestPath, cityOrder = get_approx_path(cities)

    print "Shortest Path is "
    print (shortestPath)
    for city in cityOrder:
        print "City is " + str(city[0])
    # Output results to file

