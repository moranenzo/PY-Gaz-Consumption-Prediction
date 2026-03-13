# Gas Consumption Forecasting with CatBoost

> **Accurate daily residential gas consumption forecasting using gradient boosting, oversampling, and automated hyperparameter search.**

---

## About the Project

This project was developed as part of the **STATAPP** course at **ENSAE Paris**, in close collaboration with **Irina Kouvabina** from **ENGIE**.

The project was reviewed by **Alexandre Tsybakov**, Head of the Statistics Department at **CREST-ENSAE Paris**.

The goal was to design a machine learning pipeline capable of delivering highly accurate **daily forecasts of residential gas consumption**, for both ordinary and atypical days (such as public holidays and weekends). The models aim to deliver operationnal-level forecasting on normal days while **significantly reducing errors on days with unusual consumption patterns** (e.g., public holidays). A strong emphasis was placed on model **interpretability** and **efficiency**, ensuring the model remains practical for real-world wholesale trading operations.

---

## Key Findings

| Model | Global Error (MAPE) | Holiday Error (MAPE) |
|---|---|---|
| Tuned CatBoost (baseline) | 4.34% | 6.36% |
| CatBoost + 4× Holiday Oversampling | 4.38% | **5.60%** |
| AutoML CatBoost (Optuna, enriched dataset) | **3.52%** | **5.01%** |
| Ensemble (10 CatBoost + 2 LightGBM + 2 XGBoost) | 3.60% | **4.53%** |

```markdown
By leveraging holiday oversampling, automated hyperparameter optimization (Optuna), and model ensembling, we successfully reduced both global and holiday-specific forecasting errors.
```

---

## Project Structure

```
Gas-Consumption-Forecasting/
│
├── data/
│   └── conso_data.csv              # Main dataset (not included, request from ENGIE)
│
├── models/                         # Saved CatBoost model files (.cbm)
│   ├── cb_base_model.cbm
│   ├── cb_golden_model.cbm
│   ├── RS_model_no_target.cbm
│   ├── focused_optuna_model_no_target.cbm
│   └── ...
│
├── params/                         # Best hyperparameter configs (JSON)
│
├── automl_results/                 # Outputs from AutoML/Optuna runs
│
├── metrics/                        # Evaluation metrics and results
│
├── utils.py                        # Shared utilities (SHAP plots, feature importance, etc.)
│
├── main.ipynb                      # 🔑 Main training and evaluation notebook
├── cb_base.ipynb                   # Baseline CatBoost model
├── cb_golden.ipynb                 # "Golden features" CatBoost model
├── cb_golden_tuned.ipynb           # Tuned golden CatBoost model
├── cb_time.ipynb                   # Time-aware CatBoost model
├── oversampling.ipynb              # Holiday oversampling experiments
├── automl.ipynb                    # AutoML / Optuna hyperparameter search
├── training_model(1).ipynb         # Additional training experiments
├── data_exploration_jules(1).ipynb # Exploratory Data Analysis (EDA)
├── descriptive_statistics.ipynb    # Descriptive statistics
│
├── final_metrics.json              # Consolidated final model metrics
├── requirements.txt                # Python dependencies
└── README.md
```

---

## Methodology

### 1. Feature Engineering
- **Temporal features**: day of week, week of year, month, season, year
- **Weather-related proxies**: lagged consumption, rolling averages
- **Calendar features**: French public holidays flag, weekend indicators, bridge days
- **"Golden features"**: a curated set of high-signal engineered features selected through feature importance analysis

### 2. Models
- **CatBoost (Baseline)**: gradient boosting on decision trees, natively handles categorical features
- **CatBoost (Golden)**: trained on the curated feature subset for maximum interpretability
- **Hyperparameter Tuning**:
  - Random Search
  - [Optuna](https://optuna.org/) with pruning for efficient Bayesian search
- **Holiday Oversampling**: 4× oversampling of holiday samples using `imbalanced-learn` to address class imbalance
- **AutoML (Optuna)**: automated full hyperparameter search on enriched + oversampled data
- **Ensemble**: performance-weighted ensemble combining CatBoost, LightGBM, and XGBoost

### 3. Evaluation
- **MAPE** (Mean Absolute Percentage Error) — primary metric
- **RMSE** (Root Mean Square Error)
- **R²** 
- Separate evaluation on **global** vs. **holiday** subsets

### 4. Interpretability
- **SHAP values** (TreeExplainer) for global and per-instance explanations
- **CatBoost native feature importance**
- **SHAP dependence plots** and **waterfall plots**

---

## Getting Started

### Prerequisites

- Python ≥ 3.9
- Jupyter Notebook or JupyterLab

> **Note on Data**: The dataset `conso_data.csv` is proprietary to ENGIE and is not included in this repository. To reproduce the results, please request the data directly from ENGIE and place the file in the `data/` directory.

### Installation

```bash
git clone https://github.com/<your-username>/Gas-Consumption-Forecasting.git
cd Gas-Consumption-Forecasting
pip install -r requirements.txt
```

### Running the Project

Open the notebooks in the following order for a full walkthrough:

1. **`descriptive_statistics.ipynb`** — Descriptive statistics
2. **`main.ipynb`** — Main training pipeline and results
3. **`oversampling.ipynb`** — Holiday oversampling experiments
4. **`automl.ipynb`** — Optuna AutoML search

---

## Dependencies

| Package | Purpose |
|---|---|
| `catboost` | Main gradient boosting framework |
| `scikit-learn` | Preprocessing, metrics, pipelines |
| `optuna` | Automated hyperparameter optimization |
| `optuna-integration[catboost]` | Optuna–CatBoost integration with pruning |
| `imbalanced-learn` | Holiday oversampling (SMOTE-like) |
| `shap` | Model interpretability / SHAP values |
| `matplotlib` / `seaborn` | Static visualizations |
| `plotly` | Interactive visualizations |
| `ipywidgets` | Notebook UI widgets |

---

## License

This project is for academic purposes. All rights reserved © ENGIE.
