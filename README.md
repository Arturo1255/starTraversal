# Star Traversal Program README

## Overview

Star Traversal is a Python program designed to work with the "hygxyz.csv" database, which contains detailed information on stars. This program is capable of reading the database, creating an array of Star objects, and performing a traversal operation to calculate distances between stars within a specified radius.

## Requirements

- Python 3.x
- CSV file named "hygxyz.csv" containing star data. The "hygxyz.csv" file can be downloaded from [Astronexus](https://www.astronexus.com/hyg). All credit for this database goes to the creater of this database.
- CSV file named "hygxys-small.csv" is a smaller version of the "hygxyz.csv" file.
- `star.py` module containing the `Star` class definition

## Features

- **Create Stars Array**: Reads the "hygxyz.csv" file to create an array of Star objects. Each star's ID, name, distance, and coordinates (x, y, z) are extracted from the CSV.
- **Calculate Distance**: Calculates the Euclidean distance between two stars using their 3D coordinates.
- **Star Traversal**: Performs a traversal to find stars within a given radius from the starting star, calculating the total travel distance between them.

## Setup

Ensure that you have Python 3.x installed on your system. Place the "hygxyz.csv" file in the same directory as the program. The `star.py` module should also be in the same directory or in your Python path.

## Usage

1. **Prepare the Data**: Ensure "hygxyz.csv" and `star.py` are correctly placed.
2. **Run the Program**: Execute the program using Python:

    ```
    python star_traversal.py
    ```

3. **Input**: The program uses "hygxyz.csv" as its data source and does not require any input from the user. However, you can modify the `main()` function to change the radius used for star traversal.

## How It Works

1. **Reading the CSV**: The program reads "hygxyz.csv", skipping the header and creating Star objects for each row in the CSV. Stars without a name are assigned a generic name.
2. **Calculating Distances**: It calculates distances between stars using the Euclidean formula.
3. **Traversal**: The program finds all stars within the specified radius from the starting star(The Sun). It will then move to the next closest star that has not been found. It will continue this method until every star in the specified radius has been found. It will also calculate the total distance traveled in parsecs. 

## Modifying the Program

- **Change Radius**: Modify the `radius` parameter in the `starTraversal` function call within `main()` to change the search radius.
- **Custom Star Data**: You can replace "hygxyz.csv" with another CSV file containing star data. Ensure the format matches (ID, name, distance, x, y, z fields).

