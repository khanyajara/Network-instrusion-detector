import os
import joblib
import pandas as pd
from sklearn.linear_model import LogisticRegression

def train_model(X_train, y_train, scaler, feature_names):
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    os.makedirs('models', exist_ok=True)
    joblib.dump(model, os.path.join('models', 'logistic_model.pkl'))
    joblib.dump(model, os.path.join('models', 'intrusion_model.pkl'))  # Added for compatibility
    joblib.dump(scaler, os.path.join('models', 'scaler.pkl'))
    joblib.dump(feature_names, os.path.join('models', 'feature_names.pkl'))

    # Save the feature names including 'label' at the end
    train_columns = feature_names + ['label']
    joblib.dump(train_columns, os.path.join('models', 'train_columns.pkl'))

    print("✅ Model, Scaler, and Training Columns Saved.")
