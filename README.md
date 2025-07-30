# 🧱 Concrete Strength Prediction

This project is a machine learning application that predicts the compressive strength of concrete based on its ingredients. It features an interactive user interface built using Streamlit, allowing users to input values for various components of concrete and receive a real-time prediction.

## 🚀 Features

- Predicts concrete compressive strength using a trained ML model.
- Interactive web app built with Streamlit.
- User-friendly input interface for all concrete ingredients.
- Preprocessing done using `FunctionTransformer` and Scikit-learn pipeline.

## 📊 Input Features

The model takes the following input parameters:

- Cement (kg in m³)
- Blast Furnace Slag
- Fly Ash
- Water
- Superplasticizer
- Coarse Aggregate
- Fine Aggregate
- Age (in days)

## 🛠️ Tech Stack

- Python
- Pandas, NumPy
- Scikit-learn (FunctionTransformer, regression model)
- Streamlit

## 🧠 Model Details

- Regression model trained on the Concrete Compressive Strength dataset.
- Custom preprocessing with `FunctionTransformer`.
- Standardized input data before prediction.

## 🖥️ How to Run

### 1. Clone the repository
```bash
git clone https://github.com/your-username/concrete-strength-predictor.git
cd concrete-strength-predictor
