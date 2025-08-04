# Data Cleaning & Preprocessing Project

## 📌 Overview
This project cleans and preprocesses the **Customer Personality Analysis** dataset from Kaggle.  
It follows **clean coding standards** and includes logging, modular functions, and unit tests.

---

## ✅ Features
- Handle missing values (numeric → median, text → "Unknown")
- Remove duplicate rows
- Standardize text fields
- Convert date columns to `datetime`
- Rename columns for consistency
- Add derived `age` column
- Generate summary report
- Logging for every step
- Unit tests included

---

## 🛠️ Tech Stack
- Python 3.x
- Pandas
- Pytest (for tests)

---

## ▶️ How to Run
1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/data-cleaning-project.git
   cd data-cleaning-project
Create Virtual Environment

bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
Install Dependencies

bash
Copy
Edit
pip install -r requirements.txt
Run the Script

bash
Copy
Edit
python src/data_cleaning.py
Check Output

Cleaned file: data/cleaned_customer_personality.csv

Log file: logs/cleaning.log

Summary report: reports/cleaning_summary.md