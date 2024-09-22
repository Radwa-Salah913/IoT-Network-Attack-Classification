## IoT Network Attack Classification
This project focuses on classifying network attack types in IoT environments using the RT-IoT2022 dataset. The dataset includes network traffic data from various IoT devices under normal and attack scenarios, with 12 attack classes and 85 features. We use an SVM model for multi-class classification, achieving an accuracy of 97%, precision 98% and recall 97%. The project also includes a Streamlit-based deployment and To analyze data with PowerBI, open the PowerBI Dashboard file and explore the insights based on your dataset.

[Dataset](https://www.kaggle.com/datasets/joebeachcapital/real-time-internet-of-things-rt-iot2022)

## Dataset Preprocessing
Preprocessing steps include:

Checking for missing values.

Removing duplicates.

Removing highly correlated features.

Dropping columns with more than 90% of the same value.

checking for each features whether it follows a normal distribution or not to decide whether to standardize or min-max scale using QQ plot and shapiro wilk test.

Classify your categorical features into (ordinal and nominal) to decide which features will be label encoded and which features should be OHE.

Outliers are not handled due to the imbalance in attack types, where certain classes have very few samples.

## Model and Results
The model uses Support Vector Machine (SVM) for multi-class classification. It classifies network traffic into 12 different attack types and achieves an accuracy of 97%, precision 98% and recall 97%.

## Deployment 
Using streamlit library

## Dashboard
Using PowerBI for data analysis and extracting useful insights
[Dashboard](https://fcibuedu-my.sharepoint.com/:u:/g/personal/radwa403485_fci_bu_edu_eg/ETPro0nBh4hNhOJB6lTPcdEBdI9iA8DFAr1QFb29c0JUHg?e=fJaaiC)
