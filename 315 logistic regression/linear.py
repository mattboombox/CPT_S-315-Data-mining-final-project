import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

# Load dataset
df = pd.read_csv("creditcard.csv")

# Features and labels
X = df.drop("Class", axis=1)
y = df["Class"]

# Scale ONLY Amount (V1–V28 are already scaled via PCA)
scaler = StandardScaler()
X["Amount"] = scaler.fit_transform(X[["Amount"]])

# Split data (IMPORTANT: stratify keeps fraud ratio consistent)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Logistic Regression with class weighting (handles imbalance)
model = LogisticRegression(
    class_weight="balanced",
    solver="liblinear",
    max_iter=5000
)

# Train
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluation
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))