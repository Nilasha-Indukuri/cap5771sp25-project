import streamlit as st
import joblib
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Page Configuration
st.set_page_config(page_title="Movie Sentiment Insights", layout="wide", page_icon="🎞️")

# Top-wide Banner
st.markdown("""
    <div style='background-color:#0E1117;padding:20px;border-radius:10px'>
        <h1 style='color:white;text-align:center'>🎬 Movie Sentiment Intelligence Platform</h1>
        <p style='color:#AAAAAA;text-align:center;font-size:18px;'>Real-time sentiment analysis from movie plot descriptions</p>
    </div>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.markdown("<h3 style='font-size:24px; color:#1e4d2b;'>🐊 </h3>", unsafe_allow_html=True)
st.sidebar.image("https://upload.wikimedia.org/wikipedia/en/thumb/7/7e/Florida_Gators_logo.svg/1200px-Florida_Gators_logo.svg.png", width=140)
st.sidebar.markdown("### 🐊 University of Florida")

page = st.sidebar.radio("Navigate", ["Project Summary", "Model Dashboard", "About Project"])

st.sidebar.markdown("---")
st.sidebar.markdown("**Status:** 🟢 Running")
st.sidebar.markdown("**Model Type:** Random Forest")
st.sidebar.markdown("**Version:** `v1.0`")

# Load model helper
@st.cache_resource
def load_assets():
    model = joblib.load("C:/Users/nilas/cap5771sp25-project/script/models/logistic_regression.pkl")
    return model

try:
    model = load_assets()
except Exception as e:
    st.sidebar.error("❌ Model load failed")
    model = None

# Project Summary
st.markdown("### 📝 Project Summary")

st.markdown("""
This project focuses on predicting movie ratings using machine learning techniques based on key numerical features derived from movie metadata.

It was developed as part of the **CAP5771 Spring 2025** coursework at the **University of Florida**, following the **CRISP-DM lifecycle**:

- **📊 EDA:** Analysis of genres, vote averages, and financial metrics (budget vs. revenue)
- **🛠️ Feature Engineering:** Creation of derived features like `profit`, `star_power_score`, and `budget_popularity_interaction`
- **🧠 Modeling:** Multiple classifiers and regressors including Logistic Regression, Random Forest, Decision Tree, and XGBoost
- **📈 Evaluation:** Accuracy, F1-score, confusion matrix, and ROC-AUC were used to interpret model performance
- **💻 Deployment:** A user-friendly dashboard built with **Streamlit** allows real-time prediction and visualization of insights

The end goal is to empower film analysts and producers with predictive tools to understand what makes a movie successful based on quantifiable traits.
""")



# Model Dashboard
if page == "Model Dashboard":
    st.markdown("## 📊 Model Dashboard — Insights from Milestones 1, 2 & 3")

    st.subheader("📌 Milestone 1: Exploratory Data Analysis (EDA)")
    with st.expander("🎬 Genre Distribution"):
        st.image("C:/Users/nilas/cap5771sp25-project/pic1.png", caption="Genre Distribution")
    with st.expander("⭐ Vote Average Distribution"):
        st.image("C:/Users/nilas/cap5771sp25-project/pic2.png", caption="Vote Average Distribution")
    with st.expander("📊 Correlation matrix"):
        st.image("C:/Users/nilas/cap5771sp25-project/pic3.png", caption="Correlation matrix")

    st.subheader("⚙️ Milestone 2: Feature Engineering & Model Performance")
    with st.expander("📈 Feature Importance (Random Forest)"):
        st.image("C:/Users/nilas/cap5771sp25-project/pic5.png", caption="Top Features - Random Forest")
    with st.expander("📉 Confusion Matrix - Logistic Regression"):
        st.image("C:/Users/nilas/cap5771sp25-project/pic6.png", caption="Logistic Regression Confusion Matrix")
    with st.expander("🧪 Model Comparison"):
        st.image("C:/Users/nilas/cap5771sp25-project/pic 7.png", caption="Accuracy & F1 Score Across Models")

    st.subheader("📈 Milestone 3: Final Evaluation & Dashboard Output")
    with st.expander("🚦 ROC Curves for Classifiers"):
        st.image("C:/Users/nilas/cap5771sp25-project/pic8.png", caption="ROC Curves for 4 Classifiers")
    with st.expander("🧠 Streamlit Tool Snapshot"):
        st.image("C:/Users/nilas/cap5771sp25-project/pic9.png", caption="Final Deployed Dashboard")


   



# About Section
elif page == "About Project":
    st.title("📌 About the Project")
    st.markdown("""
### 🎬 Overview

This project explores the use of machine learning to analyze and predict movie success based on various features extracted from metadata and user engagement data. Built as part of the **CAP5771 – Applied Data Science** course at the **University of Florida**, this tool is an end-to-end demonstration of real-world data science application, from raw data to live deployment.

---

### 🧠 Objective

The main goal is to build a robust machine learning pipeline that can:
- Predict a movie’s **sentiment score** or **rating** based on numerical features (regression).
- Classify whether a movie is **highly rated (≥ 7)** (classification).
- Visualize insights and allow real-time predictions via an interactive **Streamlit dashboard**.

---

### 🧱 Methodology

The project follows the **CRISP-DM** (Cross Industry Standard Process for Data Mining) lifecycle:

1. **Business Understanding**  
   Understanding key drivers of movie ratings and user sentiment.

2. **Data Collection & Preparation**  
   - Combined data from IMDb, Netflix, Hulu, Amazon Prime, Disney+, and a top movies dataset.
   - Performed cleaning, normalization, missing value handling, and scaling.
   - Created features such as `profit`, `star_power_score`, and `budget_popularity_interaction`.

3. **Exploratory Data Analysis (EDA)**  
   - Visualized genre popularity, revenue trends, vote distributions, and feature correlations.
   - Identified patterns that influence high vs. low-rated movies.

4. **Feature Engineering & Selection**  
   - Created meaningful derived features to boost model performance.
   - Conducted correlation analysis and selected the top 13 features.

5. **Model Training & Evaluation**  
   - Trained multiple models including:
     - Logistic Regression
     - Random Forest
     - Decision Tree
     - XGBoost
     - RandomForestRegressor (for sentiment score)
   - Evaluated using Accuracy, F1-score, Confusion Matrix, ROC-AUC, MAE, RMSE, and R².

6. **Tool Development**  
   - Built a dynamic multi-page Streamlit app with:
     - Executive Summary
     - Model Dashboard (all plots and insights from Milestones 1–3)
     - Real-time Prediction (for both regression and classification)
     - Project Documentation

---

### 📊 Dataset Sources

- **IMDb & TMDB:** Ratings, reviews, metadata
- **Netflix / Amazon / Hulu / Disney+:** Platform-specific availability and attributes
- **Top Movies Dataset:** Financial data like budget and revenue

---

### 🚀 Deployment

The tool is deployed locally using Streamlit and is designed to be modular and extensible:
- Easy to swap models using `.pkl` files
- Interactive sliders and inputs to simulate new movie launches
- Embedded visualization of model performance

---

### 🎯 Outcome

This project demonstrates the integration of:
- Machine learning models
- Feature engineering
- Model interpretability
- Data visualization
- Full-stack data science development

It’s a blueprint for future deployments where **AI can support creative and strategic decisions** in the entertainment industry.

""")

