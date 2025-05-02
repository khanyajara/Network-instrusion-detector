import os
import pandas as pd
import joblib
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from src.preprocess import load_data

def evaluate_model():
    print("📊 Evaluating Model...")
    data_path = os.path.join('data', 'KDDTest+.txt')
    df = load_data(data_path)

    # Load saved artifacts
    scaler = joblib.load(os.path.join('models', 'scaler.pkl'))
    model = joblib.load(os.path.join('models', 'logistic_model.pkl'))
    train_columns = joblib.load(os.path.join('models', 'train_columns.pkl'))

    # Preprocess test data
    df = pd.get_dummies(df, columns=['protocol_type', 'service', 'flag'])
    df['label'] = df['label'].apply(lambda x: 0 if x == 'normal' else 1)

    # Align test set columns with training
    for col in train_columns:
        if col not in df.columns:
            df[col] = 0
    df = df[train_columns]

    X_test = df.drop('label', axis=1)
    y_test = df['label']
    X_test_scaled = scaler.transform(X_test)

    y_pred = model.predict(X_test_scaled)

    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
    print("Classification Report:\n", classification_report(y_test, y_pred))

if __name__ == "__main__":
    evaluate_model()
