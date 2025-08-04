# Titanic Dataset - Task 1: Data Cleaning & Preprocessing 🚢

This repository contains my solution for **Task 1** of the internship project — **data cleaning and preprocessing on the Titanic dataset**.

---

##  Task Objective

> Prepare the Titanic dataset for machine learning by cleaning, transforming, and exporting it in a usable format.

---

##  What I Did:

###  Step-by-Step:

1. **Loaded the dataset**
   - Used `pandas` to load `Titanic-Dataset.csv`.

2. **Explored the data**
   - Used `.head()`, `.info()`, and `.isnull().sum()` to check structure and missing values.

3. **Handled missing values**
   - Dropped `Cabin` (too many nulls).
   - Filled `Age` with **median**.
   - Filled `Embarked` with **mode** (`S`).

4. **Dropped unnecessary columns**
   - Removed `Name` and `Ticket` (not useful for ML).
   - Saved `PassengerId`, `Name`, `Ticket` separately for reports if needed.

5. **Encoded categorical features**
   - Used `pd.get_dummies()` to one-hot encode `Sex` and `Embarked`.
   - Used `drop_first=True` to avoid multicollinearity.

6. **Scaled numerical features**
   - Standardized `Age`, `Fare`, `SibSp`, `Parch` using `StandardScaler()`.

7. **(Optional) Removed outliers**
   - Removed rows with `Fare` > 99th percentile for cleaner training.

8. **Exported the cleaned dataset**
   - Saved as `cleaned_titanic.csv`.

---

##  Final Files

| File | Description |
|------|-------------|
| `CLEANING.py` or `.ipynb` | Full Python code |
| `cleaned_titanic.csv` | Final preprocessed dataset |
| `README.md` | This file 😊 |

---

##  What I Learned

- How to handle missing data
- One-hot encoding vs label encoding
- Why feature scaling matters
- Good practices for preparing data for ML
- How to separate model-useful and display-useful columns

---

##  Tools Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib / Seaborn (optional for outlier boxplots)
- VS Code

---

##  Submission

Submitted via the official form: [Google Form Link](https://forms.gle/8Gm83s53KbyXs3Ne9)  
GitHub Repo: _Paste your repo link here after upload_

---

##  Preview (Optional)

Add screenshots of:
- Code
- Output CSV
- VS Code view
- Final Excel file

---

## 🏁 Tags

`titanic` `data-cleaning` `machine-learning` `pandas` `python` `internship-project`

---

>  Task completed successfully! Let me know if you'd like me to improve anything.
