from src.preprocess import load_data, preprocess_data
from src.train_model import train_model
from src.evaluate_model import evaluate_model
from src.predict import predict_new

def main():
    print("🚀 Intrusion Detection System Starting...")

    print("\n📦 Loading and Preprocessing Data...")    
    # Load and preprocess training data
    data = load_data('data/KDDTrain+.txt')
    X_train_scaled, y_train, scaler, feature_names = preprocess_data(data)

    print("\n🎯 Training Model...")    
    # Train the model and save it
    train_model(X_train_scaled, y_train, scaler, feature_names)

    print("\n📊 Evaluating Model...")
    evaluate_model()

    print("\n🔍 Running a Sample Prediction...")
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

if __name__ == "__main__":
    main()
