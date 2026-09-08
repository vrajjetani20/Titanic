# ---- Titanic Survival Analysis and Data Visualization ------

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import seaborn as sns

df = None
last_plot = None


def load_dataset():
    global df
    print("\n== Load Dataset ==")
    file_path = input(
        "Enter the path of the dataset (CSV file): "
    )  
    try:
        df = pd.read_csv(file_path)
        print("Dataset loaded successfully!")
    except:
        print("Error: File not found or invalid path!")


def explore_data():
    if df is None:
        print("\nPlease load the dataset first!")
        return

    while True:
        print("\n== Explore Data ==")
        print("1. Display the first 5 rows")
        print("2. Display the last 5 rows")
        print("3. Display column names")
        print("4. Display data types")
        print("5. Display basic info")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                print("\n", df.head())
            case "2":
                print("\n", df.tail())
            case "3":
                print("\nColumns in dataset:")
                for col in df.columns:
                    print("-", col)
            case "4":
                print("\nData Types:\n", df.dtypes)
            case "5":
                print("\nBasic Dataset Info:")
                df.info()
            case "6":
                break
            case _:
                print("Invalid choice, try again!")


def dataframe_operations():
    global df
    if df is None:
        print("\nPlease load the dataset first!")
        return

    while True:
        print("\n== Perform DataFrame Operations ==")
        print("1. Select specific columns")
        print("2. Filter rows by condition")
        print("3. Sort values by column")
        print("4. Group by a column and aggregate")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                cols = input("Enter column names (comma separated): ")
                col_list = [c.strip() for c in cols.split(",")]
                try:
                    print(df[col_list].head())
                except:
                    print("Error: Invalid column name entered!")

            case "2":
                col = input("Enter column name to filter (e.g. Sex, Pclass): ")
                val = input("Enter value to match: ")
                try:
                    result = df[df[col].astype(str) == str(val)]
                    print("Total matches:", len(result))
                    print(result.head())
                except:
                    print("Error filtering data!")

            case "3":
                col = input("Enter column name to sort: ")
                order = input("Sort ascending? (yes/no): ")
                try:
                    is_asc = True if order.lower() == "yes" else False
                    print(df.sort_values(by=col, ascending=is_asc).head())
                except:
                    print("Error sorting column!")

            case "4":
                col = input(
                    "Enter category column to group by (e.g. Sex, Pclass): "
                )
                try:
                    print(df.groupby(col)["Survived"].mean())
                except:
                    print("Error performing groupby!")

            case "5":
                break
            case _:
                print("Invalid choice!")


def handle_missing_data():
    global df
    if df is None:
        print("\nPlease load the dataset first!")
        return

    while True:
        print("\n== Handle Missing Data ==")
        print("1. Display rows with missing values")
        print("2. Fill missing values with mean")
        print("3. Drop rows with missing values")
        print("4. Replace missing values with a specific value")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                null_data = df[df.isnull().any(axis=1)]
                if len(null_data) == 0:
                    print("\nNo missing values found in the dataset!")
                else:
                    print(
                        f"\nTotal rows with missing values: {len(null_data)}"
                    )
                    print(null_data.head())

            case "2":
                col = input("Enter numeric column name (e.g., Age): ")
                try:
                    df[col] = df[col].fillna(df[col].mean())
                    print(f"Missing values in {col} filled with mean value.")
                except:
                    print("Error: Please provide a valid numeric column!")

            case "3":
                before_len = len(df)
                df = df.dropna()
                print(f"Dropped {before_len - len(df)} rows. Total left: {len(df)}")

            case "4":
                col = input("Enter column name (e.g., Embarked): ")
                val = input("Enter replacement value: ")
                try:
                    df[col] = df[col].fillna(val)
                    print(f"Replaced null values in {col} with {val}.")
                except:
                    print("Error replacing values!")

            case "5":
                break
            case _:
                print("Invalid choice!")


def generate_statistics():
    if df is None:
        print("\nPlease load the dataset first!")
        return
    print("\n== Descriptive Statistics ==")
    print(df.describe())


def data_visualization():
    global last_plot
    if df is None:
        print("\nPlease load the dataset first!")
        return

    while True:
        print("\n== Data Visualization ==")
        print("1. Bar Plot")
        print("2. Line Plot")
        print("3. Scatter Plot")
        print("4. Pie Chart")
        print("5. Histogram")
        print("6. Stack Plot")
        print("7. Back to Main Menu")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                col = input(
                    "Enter column for Bar Plot (e.g., Pclass, Sex, Survived): "
                )
                if col in df.columns:
                    last_plot = plt.figure()
                    df[col].value_counts().plot(kind="bar", color="skyblue")
                    plt.title(f"Bar Plot of {col}")
                    plt.xlabel(col)
                    plt.ylabel("Count")
                    print("Generating bar plot...")
                    plt.show()
                    print("Bar plot displayed successfully!")
                else:
                    print("Invalid column name!")

            case "2":
                x_col = input("Enter x-axis column: ")
                y_col = input("Enter y-axis column: ")
                if x_col in df.columns and y_col in df.columns:
                    last_plot = plt.figure()
                    plt.plot(df[x_col], df[y_col], marker="o", color="green")
                    plt.title(f"{y_col} vs {x_col}")
                    plt.xlabel(x_col)
                    plt.ylabel(y_col)
                    print("Generating line plot...")
                    plt.show()
                    print("Line plot displayed successfully!")
                else:
                    print("Invalid columns!")

            case "3":
                x_col = input("Enter x-axis column (e.g., Age): ")
                y_col = input("Enter y-axis column (e.g., Fare): ")
                if x_col in df.columns and y_col in df.columns:
                    last_plot = plt.figure()
                    plt.scatter(df[x_col], df[y_col], color="red", alpha=0.5)
                    plt.title(f"Scatter Plot: {y_col} vs {x_col}")
                    plt.xlabel(x_col)
                    plt.ylabel(y_col)
                    print("Generating scatter plot...")
                    plt.show()
                    print("Scatter plot displayed successfully!")
                else:
                    print("Invalid columns!")

            case "4":
                col = input("Enter column for Pie Chart (e.g., Sex, Survived): ")
                if col in df.columns:
                    last_plot = plt.figure()
                    df[col].value_counts().plot(
                        kind="pie", autopct="%1.1f%%", startangle=90
                    )
                    plt.title(f"Distribution of {col}")
                    plt.ylabel("")
                    print("Generating pie chart...")
                    plt.show()
                    print("Pie chart displayed successfully!")
                else:
                    print("Invalid column!")

            case "5":
                col = input("Enter numeric column for Histogram (e.g., Age, Fare): ")
                if col in df.columns:
                    last_plot = plt.figure()
                    plt.hist(df[col].dropna(), bins=10, color="orange", edgecolor="black")
                    plt.title(f"Histogram of {col}")
                    plt.xlabel(col)
                    plt.ylabel("Frequency")
                    print("Generating histogram...")
                    plt.show()
                    print("Histogram displayed successfully!")
                else:
                    print("Invalid column!")

            case "6":
                col1 = input("Enter first numeric column: ")
                col2 = input("Enter second numeric column: ")
                if col1 in df.columns and col2 in df.columns:
                    clean_data = df[[col1, col2]].dropna()
                    last_plot = plt.figure()
                    plt.stackplot(
                        range(len(clean_data)),
                        clean_data[col1],
                        clean_data[col2],
                        labels=[col1, col2],
                    )
                    plt.legend(loc="upper left")
                    plt.title("Stack Plot")
                    print("Generating stack plot...")
                    plt.show()
                    print("Stack plot displayed successfully!")
                else:
                    print("Invalid columns!")

            case "7":
                break
            case _:
                print("Invalid choice!")


def save_visualization():
    global last_plot
    if last_plot is None:
        print("\nNo visualization has been generated yet to save!")
        return

    print("\n== Save Visualization ==")
    file_name = input("Enter file name to save the plot (e.g., plot.png): ")
    if not file_name.endswith(".png"):
        file_name = file_name + ".png"

    try:
        last_plot.savefig(file_name)
        print(f"Visualization saved as {file_name} successfully!")
    except:
        print("Error saving image!")


def main():
    while True:
        print("\n========== Data Analysis & Visualization Program ==========")
        print("Please select an option:")
        print("1. Load Dataset")
        print("2. Explore Data")
        print("3. Perform DataFrame Operations")
        print("4. Handle Missing Data")
        print("5. Generate Descriptive Statistics")
        print("6. Data Visualization")
        print("7. Save Visualization")
        print("8. Exit")
        print("===========================================================")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                load_dataset()
            case "2":
                explore_data()
            case "3":
                dataframe_operations()
            case "4":
                handle_missing_data()
            case "5":
                generate_statistics()
            case "6":
                data_visualization()
            case "7":
                save_visualization()
            case "8":
                print("\nExiting the program. Goodbye!")
                break
            case _:
                print("Invalid selection, please choose between 1 and 8.")


main()