import subprocess
import sys

print("=" * 50)
print("EXCEL AUTOMATION & DATA CLEANING PIPELINE")
print("=" * 50)

print("\nStep 1: Cleaning Data...")
subprocess.run([sys.executable, "scripts/clean_data.py"])

print("\nStep 2: Generating KPIs...")
subprocess.run([sys.executable, "scripts/generate_kpis.py"])

print("\nStep 3: Creating Excel Report...")
subprocess.run([sys.executable, "scripts/excel_report_generator.py"])

print("\nPipeline Completed Successfully!")