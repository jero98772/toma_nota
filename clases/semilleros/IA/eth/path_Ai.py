import pandas as pd

# Define the data
data = {
    'start': ['Central', 'Central', 'Walchenbrücke', 'Main building', 'Main building'],
    'end': ['Main building', 'Main building', 'Main building', 'Walchenbrücke', 'Junction Bahnhofquai'],
    'route': ['Weinbergstrasse - Leonhardstrasse - Rämistrasse', 'Weinbergstrasse - Leonhardstrasse - Clausiusstrasse - Rämistrasse',
              'Walchebrücke - Walchetor - Stampfenbachstrasse - Leonhardstrasse - Rämistrasse',
              'Rämistrasse - Leonhardstrasse - stairs down to Stampfenbachstrasse - Walchetor - Walchebrücke',
              'Rämistrasse - Karl-Schmid-Strasse - Schienhutgasse - Hirschengraben - Central - Bahnhofbrücke'],
    'distance': [830, 840, 830, 830, 780],
    'elevation_gain': [44, 44, 47, -47, -45]
}

# Convert the data into a DataFrame
df = pd.DataFrame(data)

# Add a target column indicating the class (path)
df['path'] = [0, 1, 2, 3, 4]  # Assigning a class number to each path

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Splitting the data into features and target
X = df[['distance', 'elevation_gain']]
y = df['path']

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initializing and training the random forest classifier
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
rf_classifier.fit(X_train, y_train)

# Predicting on the test set
y_pred = rf_classifier.predict(X_test)

# Calculating the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
