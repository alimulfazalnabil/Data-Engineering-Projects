from datetime import datetime

import pandas as pd
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from sqlalchemy import create_engine

DB_URL = "postgresql://user:pass@localhost/sales"
CSV_PATH = "/data/raw_sales.csv"


def extract():
    return pd.read_csv(CSV_PATH)


def transform(**context):
    df = context['task_instance'].xcom_pull(task_ids='extract')
    df['date'] = pd.to_datetime(df['date'])
    df['revenue'] = df['quantity'] * df['price']
    df = df.dropna()
    return df


def load(**context):
    df = context['task_instance'].xcom_pull(task_ids='transform')
    engine = create_engine(DB_URL)
    df.to_sql('sales', engine, if_exists='replace', index=False)


default_args = {'owner': 'airflow', 'start_date': datetime(2023, 1, 1)}
dag = DAG('etl_sales_pipeline', default_args=default_args, schedule_interval='@daily')

t1 = PythonOperator(task_id='extract', python_callable=extract, dag=dag)
t2 = PythonOperator(task_id='transform', python_callable=transform, provide_context=True, dag=dag)
t3 = PythonOperator(task_id='load', python_callable=load, provide_context=True, dag=dag)

t1 >> t2 >> t3
