# 📊 Data Engineering Projects

Hands-on projects covering log analysis, big data processing, real-time streaming, data warehousing, and ETL. Each folder contains configuration files, code, and deployment notes for local Docker or cloud-based workflows.

| # | Project | Key Technologies |
|---|---------|------------------|
| 01 | Log Analysis System | Elasticsearch, Logstash, Kibana, Docker |
| 02 | Big Data Processing | Apache Spark, PySpark, Parquet |
| 03 | Data Warehousing | Amazon Redshift, SQL, S3 |
| 04 | Real-time Data Processing | Apache Kafka, Python, Avro |
| 05 | ETL Pipeline for Sales DB | Python, PostgreSQL, Pandas, Airflow |

---

## Quick Start

```bash
cd 01-log-analysis-system/code
docker compose up -d
python3 generate_logs.py
```

## Repository Structure

- 01-log-analysis-system/: ELK-based log ingestion and visualization
- 02-big-data-spark/: PySpark ETL and aggregation example
- 03-redshift-data-warehouse/: Redshift schema setup and loader
- 04-real-time-kafka/: Kafka producer/consumer with Avro schema
- 05-etl-sales-database/: Airflow-based ETL pipeline for sales data
