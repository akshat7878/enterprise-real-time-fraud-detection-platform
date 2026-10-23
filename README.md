# Enterprise Real-Time Fraud Detection Platform

A project presentation describing an Azure data-preparation workflow and a proposed fraud-detection application architecture.

## Download

[13-slide PowerPoint](presentations/Enterprise_Fraud_Detection_Platform.pptx)

## Project scope

The project owner reports using Azure Databricks for data preprocessing, Azure cloud storage, and a triggered pipeline on Azure. Exact storage and orchestration services have not been specified.

The original repository checkout contained starter files, not application code. Model training, real-time scoring, alerting, security controls and monitoring in the deck are **proposed designs**, not verified deployed features. No accuracy, latency or business-impact results are claimed. Scheduled/event-triggered preprocessing alone does not establish real-time inference.

## Regenerate the presentation

Requires Python 3.10 or newer:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r presentations/requirements.txt
python presentations/create_presentation.py
python presentations/validate_presentation.py
```

The generator writes the PowerPoint beside its source. Slides are editable and include speaker notes. Presentation dependencies are separate from the future application's dependencies.

## Presentation outline

1. Project introduction
2. Problem and objectives
3. Scope and evidence
4. End-to-end reference architecture
5. Databricks preprocessing
6. Storage and triggered orchestration
7. Fraud signals and features
8. Model development and evaluation
9. Real-time scoring and decisions
10. Security, reliability and monitoring
11. Demonstration and validation plan
12. Implementation roadmap
13. Summary and discussion

## To align the deck with an implementation

Provide sanitized Databricks notebooks, the transaction schema, exact Azure service names, pipeline configuration, model/API source and measured evaluation results. Never commit credentials, customer records or sensitive cloud exports.
