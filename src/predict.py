import pandas as pd
import joblib

def predict_new(sample):
    model = joblib.load("models/intrusion_model.pkl")
    scaler = joblib.load("models/scaler.pkl")
    feature_names = joblib.load("models/feature_names.pkl")

    df = pd.DataFrame([sample])

    # One-hot encode categorical columns
    df = pd.get_dummies(df)

    # Add missing columns that existed during training
    for col in feature_names:
        if col not in df.columns:
            df[col] = 0

    # Ensure correct column order
    df = df[feature_names]

    # Scale and predict
    scaled = scaler.transform(df)
    prediction = model.predict(scaled)

    print("🔍 Sample Prediction:", "Attack" if prediction[0] == 1 else "Normal")


if __name__ == "__main__":
    sample = {
        'duration': 0,
        'protocol_type': 'tcp',
        'service': 'http',
        'flag': 'SF',
        'src_bytes': 181,
        'dst_bytes': 5450,
        'land': 0,
        'wrong_fragment': 0,
        'urgent': 0,
        'hot': 0,
        'num_failed_logins': 0,
        'logged_in': 1,
        'num_compromised': 0,
        'root_shell': 0,
        'su_attempted': 0,
        'num_root': 0,
        'num_file_creations': 0,
        'num_shells': 0,
        'num_access_files': 0,
        'num_outbound_cmds': 0,
        'is_host_login': 0,
        'is_guest_login': 0,
        'count': 9,
        'srv_count': 9,
        'serror_rate': 0.00,
        'srv_serror_rate': 0.00,
        'rerror_rate': 0.00,
        'srv_rerror_rate': 0.00,
        'same_srv_rate': 1.00,
        'diff_srv_rate': 0.00,
        'srv_diff_host_rate': 0.00,
        'dst_host_count': 9,
        'dst_host_srv_count': 9,
        'dst_host_same_srv_rate': 1.00,
        'dst_host_diff_srv_rate': 0.00,
        'dst_host_same_src_port_rate': 1.00,
        'dst_host_srv_diff_host_rate': 0.00,
        'dst_host_serror_rate': 0.00,
        'dst_host_srv_serror_rate': 0.00,
        'dst_host_rerror_rate': 0.00,
        'dst_host_srv_rerror_rate': 0.00
    }
    predict_new(sample)
