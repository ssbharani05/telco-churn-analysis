```
import pandas as pd
import numpy as pd

```


```
import matplotlib.pyplot as plt
import seaborn as sns

```


```
Matplotlib is building the font cache; this may take a moment.

```


```
# Machine Learning
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score

# Settings
import warnings
warnings.filterwarnings('ignore')
plt.style.use('seaborn-v0_8')

print("✅ All libraries loaded successfully!")

```


```
✅ All libraries loaded successfully!import os
print(os.path.expanduser("~"))
/Users/bharanidhars
print(os.listdir('/Users/bharanidhars/Documents'))
['.DS_Store', '.localized', 'telecomiq_business_queries.sql', 'Zoom', 'TelecomIQ', 'Bharanidhar_BA_Resume.pdf', 'Bharanidhar_S_Resume.pages']
print(os.listdir('/Users/bharanidhars/Documents/TelecomIQ'))
['telco_churn.csv']
df = pd.read_csv('/Users/bharanidhars/Documents/TelecomIQ/telco_churn.csv')

print("Shape:", df.shape)
print("\nFirst 5 rows:")
df.head()
Shape: (7043, 21)

First 5 rows: Basic information about the dataset
print("Dataset Info:")
print("="*50)
print(f"Total Customers: {df.shape[0]}")
print(f"Total Features: {df.shape[1]}")
print("\nColumn Names:")
print(df.columns.tolist())
print("\nData Types:")
print(df.dtypes)
print("\nMissing Values:")
print(df.isnull().sum())# Fix TotalCharges - convert to numeric
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

# Check how many became NaN after conversion
print("Missing values in TotalCharges after fix:", df['TotalCharges'].isnull().sum())

# Fill those missing values with median
df['TotalCharges'].fillna(df['TotalCharges'].median(), inplace=True)

# Convert Churn to binary (Yes=1, No=0)
df['Churn_Binary'] = df['Churn'].map({'Yes': 1, 'No': 0})

print("\n✅ Data cleaning complete!")
print("TotalCharges dtype now:", df['TotalCharges'].dtype)# Churn Distribution
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Count plot
df['Churn'].value_counts().plot(kind='bar', ax=axes[0], 
                                 color=['#2ecc71', '#e74c3c'], 
                                 edgecolor='black')
axes[0].set_title('Customer Churn Count', fontsize=14, fontweight='bold')
axes[0].set_xlabel('Churn')
axes[0].set_ylabel('Number of Customers')
axes[0].tick_params(rotation=0)

# Pie chart
df['Churn'].value_counts().plot(kind='pie', ax=axes[1],
                                 colors=['#2ecc71', '#e74c3c'],
                                 autopct='%1.1f%%',
                                 startangle=90)
axes[1].set_title('Churn Percentage', fontsize=14, fontweight='bold')
axes[1].set_ylabel('')

plt.suptitle('TelecomIQ - Overall Churn Analysis', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig('/Users/bharanidhars/Documents/TelecomIQ/churn_distribution.png', dpi=150)
plt.show()
print("✅ Chart saved!")# Churn by Contract Type
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Count plot
sns.countplot(data=df, x='Contract', hue='Churn', 
              palette=['#2ecc71', '#e74c3c'], ax=axes[0])
axes[0].set_title('Churn by Contract Type', fontsize=14, fontweight='bold')
axes[0].set_xlabel('Contract Type')
axes[0].set_ylabel('Number of Customers')

# Churn rate plot
contract_churn = df.groupby('Contract')['Churn_Binary'].mean() * 100
contract_churn.plot(kind='bar', ax=axes[1], 
                    color=['#e74c3c', '#f39c12', '#2ecc71'],
                    edgecolor='black')
axes[1].set_title('Churn Rate by Contract Type', fontsize=14, fontweight='bold')
axes[1].set_xlabel('Contract Type')
axes[1].set_ylabel('Churn Rate (%)')
axes[1].tick_params(rotation=15)

# Add value labels on bars
for i, v in enumerate(contract_churn):
    axes[1].text(i, v + 0.5, f'{v:.1f}%', ha='center', fontweight='bold')

plt.suptitle('TelecomIQ - Contract Type Analysis', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig('/Users/bharanidhars/Documents/TelecomIQ/churn_by_contract.png', dpi=150)
plt.show()
print("✅ Chart saved!")# Churn by Tenure Groups
df['Tenure_Group'] = pd.cut(df['tenure'], 
                             bins=[0, 12, 24, 48, 72],
                             labels=['0-12 months', '13-24 months', 
                                     '25-48 months', '49+ months'])

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Count plot
sns.countplot(data=df, x='Tenure_Group', hue='Churn',
              palette=['#2ecc71', '#e74c3c'], ax=axes[0])
axes[0].set_title('Churn by Tenure Group', fontsize=14, fontweight='bold')
axes[0].set_xlabel('Tenure Group')
axes[0].set_ylabel('Number of Customers')
axes[0].tick_params(rotation=15)

# Churn rate plot
tenure_churn = df.groupby('Tenure_Group', observed=True)['Churn_Binary'].mean() * 100
tenure_churn.plot(kind='bar', ax=axes[1],
                  color=['#e74c3c', '#f39c12', '#f1c40f', '#2ecc71'],
                  edgecolor='black')
axes[1].set_title('Churn Rate by Tenure Group', fontsize=14, fontweight='bold')
axes[1].set_xlabel('Tenure Group')
axes[1].set_ylabel('Churn Rate (%)')
axes[1].tick_params(rotation=15)

for i, v in enumerate(tenure_churn):
    axes[1].text(i, v + 0.5, f'{v:.1f}%', ha='center', fontweight='bold')

plt.suptitle('TelecomIQ - Tenure Analysis', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig('/Users/bharanidhars/Documents/TelecomIQ/churn_by_tenure.png', dpi=150)
plt.show()
print("✅ Chart saved!")# Churn by Internet Service and Payment Method
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Internet Service churn rate
internet_churn = df.groupby('InternetService')['Churn_Binary'].mean() * 100
internet_churn.plot(kind='bar', ax=axes[0],
                    color=['#e74c3c', '#f39c12', '#2ecc71'],
                    edgecolor='black')
axes[0].set_title('Churn Rate by Internet Service', fontsize=14, fontweight='bold')
axes[0].set_xlabel('Internet Service')
axes[0].set_ylabel('Churn Rate (%)')
axes[0].tick_params(rotation=15)

for i, v in enumerate(internet_churn):
    axes[0].text(i, v + 0.5, f'{v:.1f}%', ha='center', fontweight='bold')

# Payment Method churn rate
payment_churn = df.groupby('PaymentMethod')['Churn_Binary'].mean() * 100
payment_churn.plot(kind='bar', ax=axes[1],
                   color=['#e74c3c', '#f39c12', '#3498db', '#2ecc71'],
                   edgecolor='black')
axes[1].set_title('Churn Rate by Payment Method', fontsize=14, fontweight='bold')
axes[1].set_xlabel('Payment Method')
axes[1].set_ylabel('Churn Rate (%)')
axes[1].tick_params(rotation=15)

for i, v in enumerate(payment_churn):
    axes[1].text(i, v + 0.5, f'{v:.1f}%', ha='center', fontweight='bold')

plt.suptitle('TelecomIQ - Service & Payment Analysis', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig('/Users/bharanidhars/Documents/TelecomIQ/churn_by_service_payment.png', dpi=150)
plt.show()
print("✅ Chart saved!")# Correlation Heatmap
# First encode categorical columns
df_encoded = df.copy()
le = LabelEncoder()

cat_columns = ['gender', 'Partner', 'Dependents', 'PhoneService', 
               'MultipleLines', 'InternetService', 'OnlineSecurity',
               'OnlineBackup', 'DeviceProtection', 'TechSupport',
               'StreamingTV', 'StreamingMovies', 'Contract',
               'PaperlessBilling', 'PaymentMethod']

for col in cat_columns:
    df_encoded[col] = le.fit_transform(df_encoded[col])

# Select numeric columns only
numeric_cols = ['gender', 'SeniorCitizen', 'Partner', 'Dependents',
                'tenure', 'MonthlyCharges', 'TotalCharges',
                'Contract', 'PaymentMethod', 'Churn_Binary']

corr_matrix = df_encoded[numeric_cols].corr()

plt.figure(figsize=(12, 8))
sns.heatmap(corr_matrix, annot=True, fmt='.2f', 
            cmap='RdYlGn', center=0,
            linewidths=0.5, square=True)
plt.title('TelecomIQ - Feature Correlation Heatmap', 
          fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig('/Users/bharanidhars/Documents/TelecomIQ/correlation_heatmap.png', dpi=150)
plt.show()
print("✅ Chart saved!")# ===== ML MODEL - Data Preparation =====
# Drop columns we don't need
df_model = df_encoded.drop(['customerID', 'Churn', 'Tenure_Group'], axis=1)

# Define features and target
X = df_model.drop('Churn_Binary', axis=1)
y = df_model['Churn_Binary']

# Split data - 80% train, 20% test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

print("✅ Data split complete!")
print(f"Training samples: {X_train.shape[0]}")
print(f"Testing samples: {X_test.shape[0]}")# ===== TRAIN MODELS =====

# Model 1 - Logistic Regression
lr_model = LogisticRegression(max_iter=1000, random_state=42)
lr_model.fit(X_train, y_train)
lr_pred = lr_model.predict(X_test)
lr_prob = lr_model.predict_proba(X_test)[:, 1]

# Model 2 - Random Forest
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
rf_pred = rf_model.predict(X_test)
rf_prob = rf_model.predict_proba(X_test)[:, 1]

# Compare both models
print("="*50)
print("MODEL COMPARISON")
print("="*50)
print(f"\n📊 Logistic Regression:")
print(f"   AUC Score: {roc_auc_score(y_test, lr_prob):.4f}")
print(f"\n🌲 Random Forest:")
print(f"   AUC Score: {roc_auc_score(y_test, rf_prob):.4f}")
print("\n✅ Models trained successfully!")# ===== MODEL PERFORMANCE VISUALIZATION =====
from sklearn.metrics import roc_curve

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Confusion Matrix - Random Forest
cm = confusion_matrix(y_test, lr_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=axes[0],
            xticklabels=['Not Churned', 'Churned'],
            yticklabels=['Not Churned', 'Churned'])
axes[0].set_title('Confusion Matrix\nLogistic Regression', 
                   fontsize=14, fontweight='bold')
axes[0].set_ylabel('Actual')
axes[0].set_xlabel('Predicted')

# ROC Curve
lr_fpr, lr_tpr, _ = roc_curve(y_test, lr_prob)
rf_fpr, rf_tpr, _ = roc_curve(y_test, rf_prob)

axes[1].plot(lr_fpr, lr_tpr, color='#e74c3c', linewidth=2,
             label=f'Logistic Regression (AUC = 0.84)')
axes[1].plot(rf_fpr, rf_tpr, color='#3498db', linewidth=2,
             label=f'Random Forest (AUC = 0.82)')
axes[1].plot([0, 1], [0, 1], 'k--', linewidth=1)
axes[1].set_title('ROC Curve Comparison', fontsize=14, fontweight='bold')
axes[1].set_xlabel('False Positive Rate')
axes[1].set_ylabel('True Positive Rate')
axes[1].legend()

plt.suptitle('TelecomIQ - Model Performance', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig('/Users/bharanidhars/Documents/TelecomIQ/model_performance.png', dpi=150)
plt.show()
print("✅ Chart saved!")# ===== FEATURE IMPORTANCE =====
feature_importance = pd.DataFrame({
    'Feature': X.columns,
    'Importance': rf_model.feature_importances_
}).sort_values('Importance', ascending=False).head(10)

plt.figure(figsize=(10, 6))
sns.barplot(data=feature_importance, x='Importance', y='Feature',
            palette='RdYlGn_r')
plt.title('TelecomIQ - Top 10 Factors Driving Churn', 
          fontsize=16, fontweight='bold')
plt.xlabel('Importance Score')
plt.ylabel('Feature')

for i, v in enumerate(feature_importance['Importance']):
    plt.text(v + 0.001, i, f'{v:.3f}', va='center', fontweight='bold')

plt.tight_layout()
plt.savefig('/Users/bharanidhars/Documents/TelecomIQ/feature_importance.png', dpi=150)
plt.show()
print("\n🔑 Top 10 Churn Drivers:")
print(feature_importance.to_string(index=False))# ===== CHURN PROBABILITY SCORES =====
# Add churn probability to original dataframe
df['Churn_Probability'] = lr_model.predict_proba(
    df_encoded[X.columns])[:, 1]

# Categorize risk levels
df['Risk_Level'] = pd.cut(df['Churn_Probability'],
                           bins=[0, 0.3, 0.6, 1.0],
                           labels=['Low Risk', 'Medium Risk', 'High Risk'])

# Summary
risk_summary = df['Risk_Level'].value_counts()
print("="*50)
print("CUSTOMER RISK SEGMENTATION")
print("="*50)
print(risk_summary)
print(f"\n💰 High Risk Customers: {risk_summary['High Risk']}")
print(f"⚠️  Medium Risk Customers: {risk_summary['Medium Risk']}")
print(f"✅ Low Risk Customers: {risk_summary['Low Risk']}")

# Save scored dataset
df.to_csv('/Users/bharanidhars/Documents/TelecomIQ/telco_churn_scored.csv', 
          index=False)
print("\n✅ Scored dataset saved!")# ===== FINAL SUMMARY =====
print("="*50)
print("TELECOMIQ - PYTHON PHASE COMPLETE")
print("="*50)
print(f"\n📊 Total Customers Analysed: 7,043")
print(f"🔴 Overall Churn Rate: 26.54%")
print(f"🤖 Model AUC Score: 0.84 (84% accurate)")
print(f"🚨 High Risk Customers Found: 1,034")
print(f"⚠️  Medium Risk Customers: 1,651")
print(f"✅ Low Risk Customers: 4,358")
print(f"\n📁 Files Saved:")
print(f"   ✅ churn_distribution.png")
print(f"   ✅ churn_by_contract.png")
print(f"   ✅ churn_by_tenure.png")
print(f"   ✅ churn_by_service_payment.png")
print(f"   ✅ correlation_heatmap.png")
print(f"   ✅ model_performance.png")
print(f"   ✅ feature_importance.png")
print(f"   ✅ telco_churn_scored.csv")
print("\n🚀 Ready for Power BI Dashboard!")
```
