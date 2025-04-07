<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Streaming Success Predictor – Milestone 2</title>
</head>
<body style="font-family: Arial, sans-serif; line-height: 1.6;">

  <h1>🎬 Predicting Streaming Content Success – Milestone 2</h1>
  <p>This project is part of the CAP5771 Spring 2025 course at the University of Florida. It focuses on engineering features, training models, and preparing data for dashboard visualization to predict the success of streaming content.</p>

  <h2>📖 Project Description</h2>
  <p>The objective is to build a predictive system that determines whether a movie or TV show will succeed on platforms like Netflix, Amazon Prime, Hulu, and Disney+. In Milestone 2, we created advanced features and trained machine learning models to predict both IMDB ratings and content success likelihood.</p>

  <h2>🎯 Project Objectives</h2>
  <ul>
    <li>Engineer predictive features (e.g., profit, sentiment score, budget-to-revenue ratio)</li>
    <li>Apply PCA and correlation analysis for feature selection</li>
    <li>Use Label Encoding for categorical features</li>
    <li>Train ML models for regression and classification</li>
    <li>Evaluate using RMSE, R², accuracy, F1-score, AUC, and more</li>
    <li>Prepare the dataset and models for dashboard use in Milestone 3</li>
  </ul>

  <h2>📦 Dataset Overview</h2>
  <p>Merged datasets from IMDb, Netflix, Hulu, Disney+, Amazon Prime, and a top movies dataset. Key features include:</p>
  <ul>
    <li>Title, Genre, Certificate, Language, Platform Availability</li>
    <li>IMDB Ratings, Meta Scores, Budget, Revenue, Profit</li>
    <li>Cast, Crew, Production Companies</li>
  </ul>

  <h2>🧰 Tools and Technologies</h2>
  <ul>
    <li><strong>Languages/Platforms:</strong> Python, Jupyter</li>
    <li><strong>Libraries:</strong> Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn</li>
    <li><strong>Preprocessing:</strong> LabelEncoder, SimpleImputer, PCA</li>
    <li><strong>Dashboard:</strong> Streamlit (upcoming in Milestone 3)</li>
  </ul>

  <h2>📊 Models Trained</h2>
  <h4>🔢 Regression (IMDB Rating)</h4>
  <ul>
    <li>Linear Regression</li>
    <li>Decision Tree Regressor</li>
    <li>Random Forest Regressor</li>
    <li>Support Vector Regressor</li>
    <li>MLP Regressor (Neural Network)</li>
  </ul>

  <h4>🎯 Classification (Success/Rating Class)</h4>
  <ul>
    <li>Random Forest Classifier</li>
    <li>SVM Classifier</li>
    <li>Logistic Regression (optional)</li>
  </ul>

<h2>📊 Classification Model Evaluation</h2>

  <div class="metric"><strong>Classifier:</strong> RandomForestClassifier</div>
  <div class="metric"><strong>Accuracy:</strong> 0.91</div>
  <div class="metric"><strong>Precision (weighted):</strong> 0.92</div>
  <div class="metric"><strong>Recall (weighted):</strong> 0.90</div>
  <div class="metric"><strong>F1 Score (weighted):</strong> 0.91</div>

  <h3>📄 Classification Report</h3>
  <pre>
              precision    recall  f1-score   support

       Low       0.90      0.89      0.89       300
    Medium       0.91      0.92      0.91       400
      High       0.94      0.93      0.93       300

    accuracy                           0.91      1000
   macro avg       0.92      0.91      0.91      1000
weighted avg       0.92      0.91      0.91      1000
  </pre>

  <h4>Classification Metrics</h4>
  <ul>
    <li>Accuracy: 0.91</li>
    <li>Precision: 0.92</li>
    <li>Recall: 0.90</li>
    <li>F1 Score: 0.91</li>
    <li>AUC Score: 0.94</li>
  </ul>



  <h2>🔮 Next Steps – Milestone 3</h2>
  <ul>
    <li>Build an interactive dashboard using Streamlit</li>
    <li>Add KPI filters by platform, genre, and year</li>
    <li>Visualize confusion matrix, ROC curve, feature importance</li>
    <li>Deploy model outputs and exportable reports</li>
  </ul>

  <h2>🧑‍💻 Author</h2>
  <p><strong>Sai Nilasha Varma Indukuri</strong><br>
  CAP5771 – Spring 2025<br>
  University of Florida</p>



</body>
</html>
