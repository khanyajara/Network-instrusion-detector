import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_data(file_path):
    """
    Loads the KDD Cup 1999 dataset with predefined column names,
    drops the 'difficulty' column (not needed for modeling), and returns the DataFrame.

    Parameters:
        file_path (str): Path to the dataset file.

    Returns:
        pd.DataFrame: Cleaned DataFrame with labeled columns.
    """
    # Define the columns for the dataset
    columns = [
        'duration', 'protocol_type', 'service', 'flag', 'src_bytes', 'dst_bytes',
        'land', 'wrong_fragment', 'urgent', 'hot', 'num_failed_logins', 'logged_in',
        'num_compromised', 'root_shell', 'su_attempted', 'num_root',
        'num_file_creations', 'num_shells', 'num_access_files', 'num_outbound_cmds',
        'is_host_login', 'is_guest_login', 'count', 'srv_count', 'serror_rate',
        'srv_serror_rate', 'rerror_rate', 'srv_rerror_rate', 'same_srv_rate',
        'diff_srv_rate', 'srv_diff_host_rate', 'dst_host_count', 'dst_host_srv_count',
        'dst_host_same_srv_rate', 'dst_host_diff_srv_rate',
        'dst_host_same_src_port_rate', 'dst_host_srv_diff_host_rate',
        'dst_host_serror_rate', 'dst_host_srv_serror_rate', 'dst_host_rerror_rate',
        'dst_host_srv_rerror_rate', 'label', 'difficulty'
    ]

    # Load the dataset
    df = pd.read_csv(file_path, names=columns)
    
    # Drop the 'difficulty' column as it's not required for the model
    df.drop('difficulty', axis=1, inplace=True)
    
    return df

def preprocess_data(df):
    """
    Preprocesses the dataset by encoding categorical variables, converting labels to binary,
    and scaling numerical features.

    Parameters:
        df (pd.DataFrame): Raw input DataFrame.

    Returns:
        X_scaled (np.ndarray): Scaled feature matrix.
        y (pd.Series): Binary target labels (0 = normal, 1 = attack).
        scaler (StandardScaler): Fitted scaler object (used later for transforming test/predict data).
        feature_names (list): List of feature names after encoding and before scaling.
    """
    # Identify categorical columns
    categorical_cols = ['protocol_type', 'service', 'flag']
    
    # Perform one-hot encoding for categorical columns
    df = pd.get_dummies(df, columns=categorical_cols)
    
    # Convert labels to binary (0 for 'normal', 1 for 'attack')
    df['label'] = df['label'].apply(lambda x: 0 if x == 'normal' else 1)

    # Split the data into features (X) and target (y)
    X = df.drop('label', axis=1)
    y = df['label']

    # Capture feature names before scaling
    feature_names = X.columns.tolist()

    # Initialize a scaler and scale the features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    return X_scaled, y, scaler, feature_names

