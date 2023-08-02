import tensorflow as tf

# Assume you have a trained or loaded model (for demonstration purposes, we'll use a simple Sequential model)
model = tf.keras.Sequential([
    tf.keras.layers.Dense(128, activation='relu', input_shape=(784,)),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

# Compile the model (you should compile your model with an appropriate optimizer and loss function)
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model (you can also load your pre-trained model here)
# model.fit(...)

# Choose a directory to save the model
save_path = "ye"

# Save the model in SavedModel format
tf.saved_model.save(model, save_path)

print("Model saved successfully.")
