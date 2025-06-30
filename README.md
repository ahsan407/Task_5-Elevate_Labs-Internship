# 🚢 Titanic Dataset - Exploratory Data Analysis (EDA)

## 📊 Overview

This project is a comprehensive Exploratory Data Analysis (EDA) of the Titanic dataset, conducted as part of Task 5 in a Data Analyst internship program. The objective is to uncover meaningful insights into passenger demographics, survival rates, and influential factors using Python data analysis tools.

---

## 🧰 Tools & Technologies Used

- Python 
- Jupyter Notebook
- Pandas
- Matplotlib
- Seaborn

---

## 📁 Dataset Information

- **Source:** Titanic dataset (`train.csv`)
- **Total Rows:** 891
- **Columns:** 12  
  - `PassengerId`, `Survived`, `Pclass`, `Name`, `Sex`, `Age`, `SibSp`, `Parch`, `Ticket`, `Fare`, `Cabin`, `Embarked`

---

## 🧪 EDA Process

### 1. Data Cleaning & Inspection
- Loaded the dataset and checked for missing values
- Analyzed data types and unique counts
- Handled nulls in `Age`, `Cabin`, and `Embarked`

### 2. Univariate Analysis
- Countplots and histograms for categorical and numerical features
- Distribution plots for `Age` and `Fare`

### 3. Bivariate Analysis
- Survival comparison based on `Sex`, `Pclass`, and `Embarked`
- Boxplots for `Age` and `Fare` vs `Survived`

### 4. Multivariate Analysis
- Pairplot for key features (`Age`, `Fare`, `Pclass`, `Survived`)
- Correlation heatmap to understand inter-variable relationships

---

## 📌 Key Findings

- **Survival Rate:** ~38% survived, ~62% did not.
- **Gender:** Females had a significantly higher survival rate than males.
- **Class:** 1st class passengers had higher survival odds; 3rd class had the lowest.
- **Fare:** Higher fare positively correlated with survival.
- **Age:** Children (especially under 10) had better survival chances.
- **Port:** Passengers from Cherbourg showed higher survival rates.

---

## 📄 Deliverables

- `Titanic_ExploratoryDataAnalysis.ipynb` — Jupyter Notebook with full analysis
- `Titanic_EDA_Report.pdf` — Final report with embedded screenshots
- `train.csv` — Titanic dataset
- `code.py` — python code used in jupyter notebook for visualisation
