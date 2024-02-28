import csv
import math
from star import *


def createStarsArray(fileName):
    filename = fileName
    array = []
    noNameStar = 1

    # Open the CSV file for reading
    with open(filename, 'r') as file:
        # Use the CSV module to read the file
        reader = csv.reader(file)
        # Skip the header row
        next(reader)
        # Loop through the rows of the file
        for row in reader:
            ID = int(row[0])
            name = row[6]
            distance = float(row[9])
            x = float(row[17])
            y = float(row[18])
            z = float(row[19])

            if name == "":
                name = "No Named Star "
                name = name + str(noNameStar)
                noNameStar = noNameStar + 1

            newStar = Star(ID, name, distance, x, y, z)
            array.append(newStar)
    file.close()
    array[0].setFound(True)
    return array


def calDistance(star1, star2):
    star1X, star1Y, star1Z = star1.getXYZ()
    star2X, star2Y, star2Z = star2.getXYZ()
    distance = math.sqrt((star2X - star1X)**2 + (star2Y - star1Y)**2 + (star2Z - star1Z)**2)
    return distance


def starTraversal(array, radius):
    comparisons = 0
    assignments = 0
    starsFound = 1
    nextStarID = -1
    withInArray = []
    totalDist = 0
    for stars in array:
        if stars.distance <= radius:
            withInArray.append(stars)
    currentStarID = array[0]
    while starsFound != len(withInArray):
        minDist = 10000000000000000000000000000000000000000000
        for stars in withInArray:
            assignments += 1
            if not stars.getFound():
                dist = calDistance(currentStarID, stars)
                if dist < minDist:
                    comparisons += 1
                    minDist = dist
                    minDist = round(minDist, 3)
                    nextStarID = stars
        totalDist = totalDist + minDist
        totalDist = round(totalDist, 3)
        print(currentStarID.getName(), "-->", nextStarID.getName(), "Distance = ", minDist, "Total Distance = ",
              totalDist)
        nextStarID.setFound(True)
        currentStarID = nextStarID
        starsFound = starsFound + 1
    print("Number of Stars = ", starsFound, " Final Total Distance = ", totalDist, "\n")

    return comparisons, assignments


def main():
    starsArray = createStarsArray("hygxyz.csv")
    print(starTraversal(starsArray, 10))
    print('\n')


main()
