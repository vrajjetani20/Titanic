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

## 📁 Project Structure

```text
Titanic_Data_Analysis_Project/
│
├── titanic.py
├── titanic.csv
├── README.md
└── screenshots/
    ├── output_1.png
    ├── output_2.png
    ├── output_3.png
    ├── output_4.png
    └── output_5.png
```

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

### 1️⃣ Load Dataset

The program loads the Titanic CSV dataset successfully.

![Load Dataset](screenshots/output_1.png)

### 2️⃣ Explore Data

The Explore Data menu can display rows, column names, data types, and basic information.

![Explore Data](screenshots/output_2.png)

### 3️⃣ DataFrame Operations

Specific columns can be selected from the dataset.

![DataFrame Operations](screenshots/output_3.png)

### 4️⃣ Handle Missing Data

Missing rows can be removed. In the demonstrated run, **331 rows were dropped and 87 rows remained**.

![Handle Missing Data](screenshots/output_4.png)

### 5️⃣ Descriptive Statistics

The program generates descriptive statistics including count, mean, standard deviation, minimum, quartiles, and maximum.

![Descriptive Statistics](screenshots/output_5.png)

## 📊 Visualization Options

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
