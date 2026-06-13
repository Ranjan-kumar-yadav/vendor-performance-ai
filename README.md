# Vendor Performance AI

## Overview

Vendor Performance AI is a Machine Learning-based classification system that predicts vendor performance levels using operational and customer-related metrics.

The model classifies vendors into the following categories:

* Excellent
* Good
* Average
* Poor

This project is designed for delivery, e-commerce, and multi-vendor platforms where vendor quality monitoring is important.

---

## Features

* Vendor performance prediction
* FastAPI REST API integration
* Random Forest Classifier
* Machine Learning model deployment
* Real-time prediction endpoint
* Ready for integration with vendor dashboards

---

## Input Features

The model uses the following features:

| Feature           | Description                   |
| ----------------- | ----------------------------- |
| total_orders      | Total orders received         |
| accepted_orders   | Orders accepted by vendor     |
| avg_rating        | Average customer rating       |
| cancellation_rate | Order cancellation rate       |
| complaints_count  | Number of customer complaints |

---

## Tech Stack

* Python
* Scikit-learn
* FastAPI
* NumPy
* Pandas
* Joblib

---

## Project Structure

```text
vendor-performance-ai/
│
├── main.py
├── vendor_model.pkl
├── label_encoder.pkl
├── vendor_performance.csv
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Ranjan-kumar-yadav/vendor-performance-ai.git

cd vendor-performance-ai
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run FastAPI Server

```bash
python -m uvicorn main:app --reload
```

Server:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## API Example

### Request

```json
{
  "total_orders": 1200,
  "accepted_orders": 1180,
  "avg_rating": 4.8,
  "cancellation_rate": 0.01,
  "complaints_count": 3
}
```

### Response

```json
{
  "performance": "Excellent"
}
```

---

## Future Improvements

* Vendor performance score (0–100)
* Vendor ranking system
* Recommendation engine
* Supabase integration
* Real-time analytics dashboard
* Automated retraining pipeline

---

## Author

Ranjan Kumar

Machine Learning & AI Developer
