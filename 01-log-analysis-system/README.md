# Log Analysis System with ELK Stack

## Overview
Real-time log monitoring using Elasticsearch, Logstash, and Kibana inside Docker. The sample generator writes application logs to disk, Logstash ingests them, and Kibana can visualize the results.

## How to Run
1. Change into the code folder.
2. Start the stack with docker compose up -d.
3. Run python3 generate_logs.py to emit sample logs.
