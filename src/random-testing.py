#!/usr/bin/env python3
# coding: utf-8
"""
    :author: noelcj9
    :brief:  This script is used to perform the task 1 of the assignment 1.
"""

import pandas as pd
import numpy as np
import math

# Global variable to store the DataFrame after operations
df2 = None

# Function to perform rotation on the DataFrame
def rotate_dataframe(df, angle, axis):
    global df2  # Access the global df2 variable
    angle_radians = math.radians(angle)
    rotation_matrix = np.eye(df.shape[1])
    rotation_matrix[axis, axis] = np.cos(angle_radians)
    rotation_matrix[axis, (axis + 1) % df.shape[1]] = -np.sin(angle_radians)
    rotated_features = np.dot(df.values, rotation_matrix.T)
    df2 = pd.DataFrame(rotated_features, columns=df.columns)

# Function to perform translation on the DataFrame
def translate_matrix(matrix, translation_factor, column):
    global df2  # Access the global df2 variable
    translated_matrix = np.copy(matrix)
    translated_matrix[:, column] += translation_factor
    df2 = pd.DataFrame(translated_matrix, columns=df.columns)

def main():
    global df2  # Access the global df2 variable

    while True:
        print("Choose an operation:")
        print("1. Rotate")
        print("2. Translate")
        print("3. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            # Rotation
            angle = float(input("Enter the rotation angle in degrees: "))
            axis = int(input("Enter the axis to rotate (0-7): "))
            rotate_dataframe(df, angle, axis)
            print("DataFrame after Rotation:")
            print(df2)

        elif choice == 2:
            # Translation
            translation_factor = float(input("Enter the translation factor: "))
            column = int(input("Enter the column to translate (0-7): "))
            translate_matrix(df.values, translation_factor, column)
            print("DataFrame after Translation:")
            print(df2)

        elif choice == 3:
            # Exit the program
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")
        
        # Ask the user if they want to perform another action
        next_action = input("Do you want to perform another action? (yes/no): ").lower()
        if next_action != 'yes':
            break  # Exit the loop if the user doesn't want to perform another action

if __name__ == '__main__':
    main()
    if df2 is not None:
        print("df2 after operations:")
        print(df2)

