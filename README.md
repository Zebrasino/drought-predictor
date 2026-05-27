# 🌾 Drought Predictor

![Python](https://img.shields.io/badge/Python-3.14-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?logo=scikit-learn&logoColor=white)

An end-to-end machine learning pipeline that predicts drought severity levels (0–5) from meteorological data using a Random Forest classifier.

---

## Overview

Drought Predictor ingests meteorological features—precipitation, temperature, wind speed, and more—to classify drought severity across six levels. The project packages the full ML lifecycle: data loading, model training, serialization, and real-time inference via a REST API.

| Metric | Value |
|--------|-------|
| Algorithm | Random Forest Classifier |
| Features | 19 meteorological variables |
| Target Classes | 6 (None, D0–D4) |
| Accuracy | **~76%** |
| Random Baseline | 16.7% |

## Dataset

**US Drought Meteorological Data** sourced from [Kaggle](https://www.kaggle.com/).

The model uses the following 19 meteorological features:

| Feature | Description |
|---------|-------------|
| `PRECTOT` | Total precipitation |
| `PS` | Surface pressure |
| `QV2M` | Specific humidity at 2m |
| `T2M` | Temperature at 2m |
| `T2MDEW` | Dew point temperature at 2m |
| `T2MWET` | Wet bulb temperature at 2m |
| `T2M_MAX` | Maximum temperature at 2m |
| `T2M_MIN` | Minimum temperature at 2m |
| `T2M_RANGE` | Temperature range at 2m |
| `TS` | Earth skin temperature |
| `WS10M` | Wind speed at 10m |
| `WS10M_MAX` | Maximum wind speed at 10m |
| `WS10M_MIN` | Minimum wind speed at 10m |
| `WS10M_RANGE` | Wind speed range at 10m |
| `WS50M` | Wind speed at 50m |
| `WS50M_MAX` | Maximum wind speed at 50m |
| `WS50M_MIN` | Minimum wind speed at 50m |
| `WS50M_RANGE` | Wind speed range at 50m |

**Target variable — Drought severity level:**

| Level | Label | Description |
|-------|-------|-------------|
| 0 | None | No drought |
| 1 | D0 | Abnormally dry |
| 2 | D1 | Moderate drought |
| 3 | D2 | Severe drought |
| 4 | D3 | Extreme drought |
| 5 | D4 | Exceptional drought |

## Project Structure

```
drought-predictor/
├── src/
│   ├── api/
│   │   └── main.py          # FastAPI application & endpoints
│   ├── core/
│   │   └── config.py        # Configuration & settings
│   ├── data/
│   │   └── loader.py        # Data loading & preprocessing
│   └── model/
│       └── train.py         # Model training pipeline
├── models/                   # Serialized model artifacts
├── data/
│   └── raw/                  # Raw dataset files
├── Dockerfile
├── pyproject.toml
├── poetry.lock
├── .gitignore
└── README.md
```

## Tech Stack

- **Language:** Python 3.14
- **ML Framework:** scikit-learn (RandomForestClassifier)
- **API Framework:** FastAPI + Uvicorn
- **Validation:** Pydantic
- **Serialization:** Joblib
- **Dependency Management:** Poetry
- **Containerization:** Docker

## Getting Started

### Prerequisites

- Python 3.14+
- [Poetry](https://python-poetry.org/docs/#installation)
- Docker (optional)

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/<your-username>/drought-predictor.git
   cd drought-predictor
   ```

2. **Install dependencies**

   ```bash
   poetry install
   ```

3. **Download the dataset**

   Download the US Drought Meteorological Data from Kaggle and place it at:

   ```
   data/raw/drought.csv
   ```

4. **Train the model**

   ```bash
   poetry run python -m src.model.train
   ```

5. **Run the API**

   ```bash
   poetry run uvicorn src.api.main:app --reload
   ```

   The API will be available at `http://localhost:8000`.

## Docker Usage

> **Note:** The trained model is not included in the Docker image. Train the model locally first, then mount the `models/` directory as a volume.

**Build the image:**

```bash
docker build -t drought-predictor .
```

**Run the container:**

```bash
docker run -d -p 8000:8000 -v ./models:/app/models drought-predictor
```

## API Reference

### `GET /health`

Health check endpoint.

**Response:**

```json
{ "status": "healthy" }
```

### `POST /predict`

Accepts 19 meteorological features and returns the predicted drought severity level with a confidence score.

**Request body:**

```json
{
  "PRECTOT": 0.5,
  "PS": 95.2,
  "QV2M": 0.012,
  "T2M": 22.5,
  "T2MDEW": 15.3,
  "T2MWET": 18.1,
  "T2M_MAX": 28.0,
  "T2M_MIN": 17.0,
  "T2M_RANGE": 11.0,
  "TS": 23.1,
  "WS10M": 3.2,
  "WS10M_MAX": 6.5,
  "WS10M_MIN": 1.1,
  "WS10M_RANGE": 5.4,
  "WS50M": 5.8,
  "WS50M_MAX": 9.2,
  "WS50M_MIN": 2.3,
  "WS50M_RANGE": 6.9
}
```

**Response:**

```json
{
  "drought_level": 2,
  "confidence": 0.83
}
```

### Interactive Documentation

Swagger UI is available at [`/docs`](http://localhost:8000/docs) when the server is running.