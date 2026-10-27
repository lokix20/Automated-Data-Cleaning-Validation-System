# Automated Data Cleaning & Validation System

An automated data quality and validation pipeline that inspects datasets, infers semantic data types, detects personally identifiable information (PII), and generates structured schema definitions with expectation rules.

---

## 🚀 Features

- **Semantic Type Inference**: Automatically categorizes columns into semantic types (`ID`, `EMAIL`, `PHONE`, `DATE`, `NUMERIC`, `TEXT`).
- **PII Detection**: Detects sensitive personal data such as names, email addresses, and phone numbers.
- **Schema & Expectation Generation**: Builds a machine-readable `schema.json` containing:
  - Dataset metadata (row count, column count).
  - Field-level semantic types and PII flags.
  - Expected formats (valid email, phone number, valid dates).
  - Expected value ranges (e.g., minimum values, score bounds).

---

## 📁 Project Structure

```text
├── data/
│   └── hr_dataset.csv       # Sample HR employee dataset
├── type_inference.py        # Semantic data type inference
├── pii_detector.py          # PII identification logic
├── schema_generator.py      # Column schema & expectation builder
├── main.py                  # Main execution pipeline
├── schema.json              # Generated schema output
├── explore.py               # Exploratory data script
└── .gitignore               # Git ignore rules
```

---

## 🛠️ Getting Started

### Prerequisites

- Python 3.8+
- [pandas](https://pandas.pydata.org/)

Install dependencies:
```bash
pip install pandas
```

### Running the Pipeline

Execute `main.py` to analyze the dataset and generate the schema:
```bash
python main.py
```

This will produce or update `schema.json`.
