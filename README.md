# Enterprise Real-Time Financial Transaction Anomaly Detection Platform

## Overview

This project is an end-to-end Data Engineering and Machine Learning solution that detects potentially fraudulent financial transactions using Azure cloud services, Apache Spark, Kafka, and Machine Learning.

The platform processes historical transaction data through a Medallion Architecture (Bronze, Silver, Gold), trains a fraud detection model, and simulates real-time transaction processing using Apache Kafka and Spark Structured Streaming.

The objective is to demonstrate how modern financial institutions can build scalable fraud detection pipelines using cloud-native technologies.

---

## Project Objectives

* Build an enterprise-style data engineering pipeline on Microsoft Azure.
* Process transaction data using Azure Databricks and Delta Lake.
* Train a machine learning model for fraud detection.
* Simulate real-time transaction streams using Apache Kafka.
* Perform real-time fraud prediction using Spark Structured Streaming.
* Store prediction results in Azure SQL Database.
* Visualize fraud analytics using Power BI.

---

## Architecture

```
Historical Transaction Dataset
            │
            ▼
Azure Data Factory
            │
            ▼
Azure Data Lake Storage Gen2
            │
            ▼
Azure Databricks
            │
Bronze → Silver → Gold
            │
            ▼
Feature Engineering
            │
            ▼
Machine Learning Model
            │
            ▼
MLflow Model Registry
            │
────────────────────────────────────
            │
Kafka Producer
(Stream Test Dataset)
            │
            ▼
Kafka Topic
            │
            ▼
Spark Structured Streaming
            │
            ▼
Real-Time Fraud Prediction
            │
            ▼
Azure SQL Database
            │
            ▼
Power BI Dashboard
```

---

## Technology Stack

* Microsoft Azure
* Azure Data Factory
* Azure Data Lake Storage Gen2
* Azure Databricks
* Delta Lake
* Apache Spark
* Spark SQL
* Apache Kafka
* Spark Structured Streaming
* Scikit-learn
* MLflow
* Azure SQL Database
* Power BI
* Python

---

## Project Status

🚧 Currently under development.

The project is being built incrementally following enterprise software engineering practices.

Current Progress:

* [x] Project initialization
* [ ] Azure infrastructure
* [ ] Data ingestion
* [ ] Bronze layer
* [ ] Silver layer
* [ ] Gold layer
* [ ] Feature engineering
* [ ] Machine learning
* [ ] Kafka streaming
* [ ] Real-time prediction
* [ ] Power BI dashboard

---

## Future Enhancements

* Real banking transaction simulation
* Customer behavioral feature engineering
* Advanced fraud detection models
* CI/CD deployment
* Real-time monitoring and alerting

---

## Author
Akshat Kumawat