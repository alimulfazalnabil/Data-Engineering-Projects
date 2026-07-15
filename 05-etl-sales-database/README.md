# ETL Pipeline for a Sales Database

## Overview
Extract data from CSV files, transform it by cleaning and aggregating, and load it into PostgreSQL. The workflow is orchestrated with Airflow.

## How to Run
1. Install requirements with pip install -r requirements.txt.
2. Update the database URL and CSV path in etl_dag.py.
3. Start Airflow and trigger the DAG.
