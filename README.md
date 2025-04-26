
# 🎬 Video Presentation 2

[▶️ View Demo Video Here](https://drive.google.com/drive/u/0/folders/16V83FB-eZSTD411iCoprn0qRzedV5AAx)

# 🎬 Predicting Streaming Content Success – Milestone 2

This project is part of the **CAP5771 Spring 2025** course at the **University of Florida**. It focuses on engineering features, training models, and preparing data for dashboard visualization to predict the success of streaming content.

---

## 📖 Project Description

The objective is to build a predictive system that determines whether a movie or TV show will succeed on platforms like Netflix, Amazon Prime, Hulu, and Disney+.  
In Milestone 2, we engineered features and trained machine learning models to predict IMDB ratings and content success likelihood.

---

## 🎯 Project Objectives

- Engineer predictive features (profit, sentiment score, budget-to-revenue ratio)
- Apply PCA and correlation analysis for feature selection
- Use Label Encoding for categorical features
- Train ML models for regression and classification
- Evaluate models using RMSE, R², accuracy, F1-score, AUC, and others
- Prepare models and datasets for dashboard use in Milestone 3

---

## 📦 Dataset Overview

Merged datasets from:
- IMDb
- Netflix
- Hulu
- Disney+
- Amazon Prime
- Top Movies Dataset

**Key Features:**
- Title, Genre, Certificate, Language, Platform Availability
- IMDB Ratings, Meta Scores, Budget, Revenue, Profit
- Cast, Crew, Production Companies

---

## 🧰 Tools and Technologies

- **Languages/Platforms:** Python, Jupyter
- **Libraries:** Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn
- **Preprocessing:** LabelEncoder, SimpleImputer, PCA
- **Dashboard (Milestone 3):** Streamlit

---

## 📊 Models Trained

### 🔢 Regression Models (IMDB Rating Prediction)

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- Support Vector Regressor
- MLP Regressor (Neural Network)

### 🎯 Classification Models (Success/Rating Class)

- Random Forest Classifier
- SVM Classifier
- Logistic Regression (optional)

---

## 📊 Classification Model Evaluation

**Classifier:** Random Forest Classifier

| Metric | Score |
|:------:|:-----:|
| Accuracy | 0.91 |
| Precision (weighted) | 0.92 |
| Recall (weighted) | 0.90 |
| F1 Score (weighted) | 0.91 |

### 📄 Classification Report

```text
              precision    recall  f1-score   support

       Low       0.90      0.89      0.89       300
    Medium       0.91      0.92      0.91       400
      High       0.94      0.93      0.93       300

    accuracy                           0.91      1000
   macro avg       0.92      0.91      0.91      1000
weighted avg       0.92      0.91      0.91      1000


Classification Metrics Summary

- Accuracy: 0.91  
- Precision (Weighted): 0.92  
- Recall (Weighted):0.90 
- F1 Score (Weighted):0.91 
- AUC Score:0.94

🔮 Next Steps – Milestone 3

- ✅ Build an interactive dashboard using **Streamlit**  
- 📊 Add KPI filters (platform, genre, year)  
- 📉 Visualize confusion matrix, ROC curve, and feature importance  
- 📦 Deploy model outputs and exportable reports

🧑‍💻 Author

Sai Nilasha Varma Indukuri
CAP5771 – Spring 2025
University of Florida

