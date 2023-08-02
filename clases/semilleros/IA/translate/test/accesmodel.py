import tensorflow as tf

# Define the path where the model was saved
saved_model_path = "ye"

# Load the model from the SavedModel format
loaded_model = tf.saved_model.load(saved_model_path)

# Now, you can use the loaded_model to make predictions on new data

# Example: Predict using new data
import numpy as np

# Create a sample input data for prediction
sample_input = np.random.random((1, 784))  # Replace this with your actual input data

# Make predictions using the loaded model
predictions = loaded_model(sample_input)

# `predictions` will contain the output of the model based on the input data

print("Predictions:", predictions)

