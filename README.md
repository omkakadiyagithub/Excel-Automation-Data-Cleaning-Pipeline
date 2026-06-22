# Excel Automation & Data Cleaning Pipeline

## Overview

A Python-based automation pipeline designed to clean, process, validate, and transform large Excel datasets into business-ready reports.

This project automates repetitive spreadsheet operations such as duplicate removal, missing value handling, data quality assessment, KPI generation, and Excel report creation. The pipeline reduces manual effort and provides structured insights for business decision-making.

---

## Business Problem

Organizations often receive large Excel datasets containing:

- Duplicate records
- Missing customer information
- Cancelled transactions
- Invalid quantities and prices
- Inconsistent reporting formats

Manually cleaning and analyzing such datasets is time-consuming and error-prone.

This project automates the entire workflow and generates clean datasets along with KPI summaries and Excel reports.

---

## Features

### Data Cleaning & Transformation

- Removes duplicate records
- Handles missing Customer IDs
- Removes cancelled invoices
- Removes negative quantities
- Removes negative unit prices
- Creates Sales Amount calculations
- Generates cleaned datasets automatically

### Data Quality Reporting

- Original row count
- Cleaned row count
- Rows removed
- Duplicate records identified
- Missing Customer IDs detected
- Negative quantities identified
- Negative prices identified

### KPI Generation

The pipeline automatically generates:

- Total Revenue
- Total Orders
- Total Customers
- Average Order Value
- Top Revenue Country

### Excel Report Automation

Creates a multi-sheet Excel report containing:

#### Clean Data Sheet
Processed and cleaned transaction dataset.

#### KPI Summary Sheet
Business performance metrics.

#### Data Quality Report Sheet
Detailed data quality assessment and cleaning statistics.

---

## Technologies Used

- Python
- Pandas
- NumPy
- OpenPyXL

---

## Dataset

**Online Retail Dataset**

Contains transactional retail sales data including:

- Invoice Number
- Product Information
- Quantity
- Invoice Date
- Unit Price
- Customer ID
- Country

---

## Project Structure

```text
Excel_Automation_Data_Cleaning_Pipeline/

│
├── data/
│   ├── Online Retail.xlsx
│   └── clean_retail_data.csv
│
├── reports/
│   ├── kpi_summary.csv
│   ├── data_quality_report.csv
│   └── Final_Report.xlsx
│
├── screenshots/
│   ├── pipeline_execution.png
│   ├── Clean Data sheet.png
│   ├── KPI Summary sheet.png
│   └── Data Quality Report sheet.png
│
├── scripts/
│   ├── inspect_data.py
│   ├── clean_data.py
│   ├── generate_kpis.py
│   ├── data_quality_report.py
│   └── excel_report_generator.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

## Workflow

### Step 1: Data Inspection

Reads and analyzes the raw Excel dataset.

### Step 2: Data Cleaning

- Remove duplicates
- Handle missing values
- Remove cancelled invoices
- Remove invalid transactions

### Step 3: Data Quality Assessment

Generate data quality statistics and cleaning summary.

### Step 4: KPI Generation

Calculate business performance metrics.

### Step 5: Excel Report Generation

Create a professional Excel report with multiple sheets.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/omkakadiyagithub/Excel-Automation-Data-Cleaning-Pipeline.git
```

Navigate to the project:

```bash
cd Excel-Automation-Data-Cleaning-Pipeline
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the complete pipeline:

```bash
python main.py
```

---

## Sample Output

### KPI Summary

| Metric | Value |
|----------|----------|
| Total Revenue | 8,911,407.90 |
| Total Orders | 18,532 |
| Total Customers | 4,338 |
| Average Order Value | 480.87 |
| Top Revenue Country | United Kingdom |

---

## Screenshots

### Pipeline Execution

Add screenshot:

```
screenshots/pipeline_execution.png
```

### Clean Data Sheet

```
screenshots/Clean Data sheet.png
```

### KPI Summary Sheet

```
screenshots/KPI Summary sheet.png
```

### Data Quality Report Sheet

```
screenshots/Data Quality Report sheet.png
```

---

## Project Highlights

- Automated Excel data cleaning workflow
- Business KPI generation
- Data quality monitoring
- Multi-sheet Excel reporting
- Reusable and modular Python scripts
- End-to-end automation pipeline

---

## Future Enhancements

- Interactive Dashboard using Streamlit
- Automated Email Report Distribution
- Excel Charts & Visualizations
- Scheduled Pipeline Execution
- Advanced Data Validation Rules

---

## Author

**Om Kakadiya**

GitHub: https://github.com/omkakadiyagithub