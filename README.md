# 🚢 Titanic Data Analysis & Visualization

A beginner-friendly **Python Data Analysis and Visualization** project built with **Pandas, NumPy, Matplotlib, and Seaborn**.

This project provides an interactive menu-driven program for loading a Titanic CSV dataset, exploring data, performing DataFrame operations, handling missing values, generating descriptive statistics, creating visualizations, and saving plots.

## ✨ Features

- 📂 **Load Dataset** from a CSV file
- 🔎 **Explore Data**
  - Display first 5 rows
  - Display last 5 rows
  - Display column names
  - Display data types
  - Display basic dataset information
- 🧮 **DataFrame Operations**
  - Select specific columns
  - Filter rows by condition
  - Sort values by a column
  - Group data and calculate aggregates
- 🧹 **Handle Missing Data**
  - Display rows containing missing values
  - Fill numeric missing values with the mean
  - Drop rows with missing values
  - Replace missing values with a specific value
- 📊 **Descriptive Statistics** using `DataFrame.describe()`
- 📈 **Data Visualization**
  - Bar Plot
  - Line Plot
  - Scatter Plot
  - Pie Chart
  - Histogram
  - Stack Plot
- 💾 **Save Visualization** as a PNG image
- 🔁 Interactive menu that continues until the user selects Exit

## 🛠️ Technologies Used

- 🐍 Python
- 🐼 Pandas
- 🔢 NumPy
- 📉 Matplotlib
- 📊 Seaborn


## ⚙️ Installation

Make sure Python is installed on your computer.

Install the required libraries:

```bash
pip install pandas numpy matplotlib seaborn
```

## ▶️ How to Run

1. Download or clone this project.
2. Open the project folder in **VS Code** or another Python editor.
3. Open a terminal in the project folder.
4. Run:

```bash
python titanic.py
```

5. Select an option from the main menu.

Example:

```text
========== Data Analysis & Visualization Program ==========
Please select an option:
1. Load Dataset
2. Explore Data
3. Perform DataFrame Operations
4. Handle Missing Data
5. Generate Descriptive Statistics
6. Data Visualization
7. Save Visualization
8. Exit
===========================================================
```

## 📌 Dataset

The program is demonstrated with the `titanic.csv` dataset.

The analysis uses columns such as:

- `PassengerId`
- `Pclass`
- `Name`
- `Sex`
- `Age`
- `SibSp`
- `Parch`
- `Ticket`
- `Fare`
- `Cabin`

The DataFrame grouping operation also uses the `Survived` column when calculating the mean survival value.

## 🖥️ Screenshots

### 1️ Load Dataset


<img width="746" height="402" alt="1" src="https://github.com/user-attachments/assets/83464dec-5115-47e3-9987-f3d2b8ee69a9" />


### 2️ Explore Data

<img width="801" height="542" alt="2" src="https://github.com/user-attachments/assets/0ab8869b-83a1-41c8-b120-dc84ef19648a" />


### 3️ DataFrame Operations

<img width="862" height="567" alt="3" src="https://github.com/user-attachments/assets/f0efe24b-e6b1-4b82-b0c2-361d21743098" />


### 4 Handle Missing Data

<img width="752" height="437" alt="4" src="https://github.com/user-attachments/assets/b3f0fb27-807f-4ad2-bbc4-4906f228bfe6" />


### 5 Descriptive Statistics

<img width="1002" height="526" alt="5" src="https://github.com/user-attachments/assets/c97627b5-2704-4320-bc30-bec139626357" />


### 6  Data Visualization

<img width="1280" height="607" alt="6" src="https://github.com/user-attachments/assets/bdd83a12-faaa-4cb4-bdd3-79356db7c487" />

### 7  Save Visualization

<img width="1206" height="375" alt="7" src="https://github.com/user-attachments/assets/ebffeca6-4174-4d36-9e42-649b513f9aae" />


The program supports six types of charts:

| Chart | Purpose |
|---|---|
| 📊 Bar Plot | Compare category counts |
| 📈 Line Plot | Show values across an x-axis |
| 🔵 Scatter Plot | Show relationships between two numeric columns |
| 🥧 Pie Chart | Show category proportions |
| 📉 Histogram | Show the distribution of numeric data |
| 📚 Stack Plot | Compare cumulative values |

## 🧠 Concepts Practiced

This project demonstrates practical use of:

- Functions
- Global variables
- `while` loops
- `match-case`
- User input
- Pandas DataFrames
- Data filtering and sorting
- GroupBy and aggregation
- Missing-value handling
- Descriptive statistics
- Data visualization
- File saving
- Exception handling

## 👨‍💻 Author

**Vraj Jetani**

---

⭐ If you find this project useful, consider giving it a star on GitHub!
