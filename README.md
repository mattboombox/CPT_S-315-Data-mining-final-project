# Credit Card Fraud Detection Using Data Mining Techniques

**Course:** CPT_S 315 – Introduction to Data Mining, Washington State University
**Team:** Matthew Heseltine, Itay Shemesh, Logan Hall, Ethan Olsen

## Overview

This project applies data mining and machine learning techniques to detect fraudulent
credit card transactions in a large, highly imbalanced real-world dataset. Fraudulent
transactions make up less than 1% of the data, so the project focuses on techniques
suited to rare-event detection rather than raw accuracy.

## Dataset

- **Source:** [Kaggle – Credit Card Fraud Detection (ULB Machine Learning Group)](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud/data)
- **Size:** ~284,800 transactions
- **Features:** `Time`, `Amount`, 28 anonymized/PCA-transformed features (`V1`–`V28`), and a binary `Class` label (1 = fraud, 0 = legitimate)
- Because the features are PCA-anonymized, individual variables can't be interpreted directly in real-world terms — a key limitation discussed in the project abstract.

> Note: `creditcard.csv` is not included in this repo due to its size (~150 MB). Download it directly from the Kaggle link above and place it in the project root before running the scripts.

## Methodology

1. **Preprocessing** — Scale the `Amount` column with `StandardScaler` (V1–V28 are already PCA-scaled); split into train/test sets with stratification to preserve the fraud ratio.
2. **Handling class imbalance** — Use class-weighted models (`class_weight="balanced"`) rather than naive resampling, so the model doesn't default to always predicting "legitimate."
3. **Modeling** — Train and evaluate classifiers (starting with logistic regression; decision trees / random forests explored as extensions) to distinguish fraudulent from legitimate transactions.
4. **Evaluation** — Since accuracy is misleading on imbalanced data, evaluate using precision, recall, F1-score, and the confusion matrix.

## Repository Contents

| File | Description |
|---|---|
| `Final_Project_Abstract.pdf` | Project abstract covering motivation, dataset, methodology, challenges, and expected outcomes |
| `logistic_regression_linear.py` | Loads the dataset, scales `Amount`, splits the data, and trains a class-weighted logistic regression model to classify transactions as fraudulent or legitimate |
| `logistic_regression_from_scapy.py` | Utility script for scanning `.pcap` network capture files for plaintext flags/strings in raw TCP payloads (packet-analysis exercise; unrelated to the fraud detection model above) |

## Results

Model performance is reported via a confusion matrix and full classification report
(precision, recall, F1-score) on a held-out 20% test split. See the abstract for the
full discussion of expected outcomes and challenges.

## Requirements

```
pandas
scikit-learn
scapy   # only needed for the packet-analysis script
```

## How to Run

```bash
pip install -r requirements.txt
python logistic_regression_linear.py
```

## Future Work

- Compare logistic regression against decision trees and random forests
- Explore anomaly-detection approaches that treat fraud as outlier behavior
- Experiment with resampling techniques (SMOTE, undersampling) alongside class weighting
