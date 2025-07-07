Project Tasks 
Lecture: Artificial Intelligence 
BA, SS 2025, Universities of Europe, Potsdam 
Dr. Harald Stein, Version: 29.5.2025 
 
1. Group Formation 
 
▪  Students will form groups of three 
▪  Each group selects its own members. 
▪  Each student in the group will take on one of the following roles: 
▪  Coding 
▪  Presentation 
▪  Documentation 
 
Project chosen: Logistic Regression: Heart Disease Prediction** 
▪  Use logistic regression to predict the risk of heart disease based on patient data. 
▪  Dataset: https://www.kaggle.com/datasets/iamsouravbanerjee/heart-attack-prediction-dataset 
 
3. Deliverables 
 
Code:  
Well-documented codebase relevant to the chosen topic. 
Presentation:  
A 10 – 15 minute presentation summarizing the project, methodology, and results. 
Documentation:  
A written report (5–10 pages) including: 
▪  Problem statement 
▪  Methodology 
▪  Results and evaluation 
▪  Discussion and conclusion 
 
4. Roles and Responsibilities 
 
Coding:  
Responsible for implementing the main algorithms, ensuring code quality, and preparing code for 
demonstration. 
Presentation:  
Prepares and delivers the group presentation, coordinates visual materials, and answers questions 
during the session. 
Documentation:  
Leads the creation of the written report, compiles contributions from all group members, and ensures 
clarity and completeness.  
5. Presentation Guidelines 
 
▪  Attendance at presentation sessions is not mandatory in person; students may attend and 
present remotely. 
▪  All presentations will be held and evaluated during these sessions. 
▪  Each group must be ready to answer questions about their project. 
 
6. Evaluation Criteria 
 
▪  Technical implementation 
(coding quality, correctness, innovation) 
▪  Clarity and completeness of documentation 
▪  Effectiveness and professionalism of the presentation 
▪  Teamwork and clear distribution of responsibilities 
 
Projects 
 
Project 1 – Heart Attack Prediction with Logistic 
Regression 
 
Objective 
Implement logistic regression to predict heart attack risk and document your machine learning 
process step-by-step. 
Background Dataset 
Use the Heart Attack Prediction Dataset from Kaggle: 
Source: https://www.kaggle.com/datasets/iamsouravbanerjee/heart-attack-prediction-dataset 
•  Features: Age, sex, chest pain type, blood pressure, cholesterol, and other cardiac indicators 
•  Target: Binary classification (heart attack risk: 0/1) 
 
Your Task: Implement Logistic Regression Solution 
1. Data Analysis and Preparation 
Download and explore the heart attack dataset from the provided Kaggle link. 
2. Implementation Requirements 
Core components to include: 
•  Data preprocessing and feature engineering 
•  Train-test split with stratification 
•  Logistic regression model: P(y=1|x) = 1/(1 + e^(-z)) where z = β₀ + β₁x₁ + ... + βₙxₙ 
•  Model training with gradient descent or solver optimization 
•  Prediction generation and probability thresholding 
•  Performance evaluation with multiple metrics 
3. Documentation (Step-by-Step Process) 
Format each step as: 
•  What: Brief description of what you implemented 
•  Why: Reasoning behind your approach 
•  How: Key code snippet or technique used 
 
•  Result: What was achieved/learned 
Required Steps to Document: 
1.  Dataset exploration (feature distributions, correlations, missing values) 
2.  Data preprocessing strategy (handling categorical variables, scaling, feature selection) 
3.  Train-test split implementation (stratification, random state) 
4.  Logistic regression model setup (solver choice, regularization parameters) 
5.  Model training process (fitting procedure, convergence monitoring) 
6.  Prediction generation (probability scores, threshold selection) 
7.  Performance evaluation implementation (accuracy, precision, recall, F1-score) 
8.  Results interpretation (feature importance, model coefficients analysis) 
4. Model Evaluation Requirements 
Calculate and interpret these metrics: 
•  Accuracy: Overall correctness of predictions 
•  Precision: True positives / (True positives + False positives) 
•  Recall (Sensitivity): True positives / (True positives + False negatives) 
•  F1-Score: Harmonic mean of precision and recall 
•  Confusion Matrix: Visual representation of prediction results 
5. Results Section 
•  Feature importance analysis and coefficient interpretation 
•  Confusion matrix visualization 
•  Performance metrics comparison and medical significance 
•  Model limitations and potential improvements 
•  Real-world application considerations 
 
Deliverables 
1.  Python code (well-commented, runnable) 
2.  Presentation 
3.  Documentation (4-6 pages max) following step-by-step format above 

