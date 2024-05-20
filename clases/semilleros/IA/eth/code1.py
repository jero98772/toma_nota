import numpy as np
import pandas as pd
from os import listdir
from os.path import isfile, join
from sklearn.preprocessing import StandardScaler, LabelEncoder, PCA
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score

class Recording:
    def _init_(self, file_path):
        self.data = pd.read_pickle(file_path)
        self.labels = self.data.get('labels', {})

def get_energy(signal):
    fft_signal = np.fft.fft(signal)
    energy = np.sum(np.abs(fft_signal)**2)
    return energy / len(signal)

def extract_features(signal, fs, window_size_seconds=5):
    window_size = int(fs * window_size_seconds)
    step_size = window_size // 2
    windows = [signal[i:i+window_size] for i in range(0, len(signal) - window_size, step_size)]
    return {
        'energy': [get_energy(w) for w in windows],
        'std': [np.std(w) for w in windows],
        'mean': [np.mean(w) for w in windows]
    }

def process_data(directory):
    features_list = []
    for filename in [f for f in listdir(directory) if isfile(join(directory, f))]:
        recording = Recording(join(directory, filename))
        if 'ax' in recording.data:
            fs = recording.data['ax'].samplerate  # Assume same fs for all sensors
            features = {}
            for axis in ['ax', 'ay', 'az', 'gx', 'gy', 'gz']:
                if axis in recording.data:
                    data = recording.data[axis].values
                    axis_features = extract_features(data, fs)
                    for key, value in axis_features.items():
                        features[f'{axis}_{key}'] = value
            features['location'] = recording.labels.get('watch_location', 'Unknown')
            features_df = pd.DataFrame(features)
            features_list.append(features_df)
    return pd.concat(features_list, ignore_index=True)

def train_and_evaluate(data):
    features = [col for col in data.columns if col != 'location']
    X = data[features]
    y = data['location']
    
    label_encoder = LabelEncoder()
    y_encoded = label_encoder.fit_transform(y)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)
    
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    pca = PCA(n_components=5)
    X_train_pca = pca.fit_transform(X_train_scaled)
    X_test_pca = pca.transform(X_test_pca)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train_pca, y_train)
    predictions = model.predict(X_test_pca)
    
    print("Classification Report:")
    print(classification_report(y_test, predictions, target_names=label_encoder.classes_))

# Example usage
folder_path = '/path/to/data'
data = process_data(folder_path)
train_and_evaluate(data)