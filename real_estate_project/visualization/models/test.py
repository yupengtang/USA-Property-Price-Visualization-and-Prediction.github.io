import joblib
import numpy as np
import pandas as pd

# Step 1: Load the model
model_path = 'neural_net_regressor.joblib'
try:
    mlp_model = joblib.load(model_path)
    print("Model loaded successfully!")
except FileNotFoundError:
    print(f"Error: The file {model_path} was not found.")
except Exception as e:
    print(f"An error occurred while loading the model: {e}")

# Step 2: Prepare input data
# Example with NumPy
input_data = pd.DataFrame({
    'acre_lot': [5.1, 4.9],
    'bath': [3.5, 3.0],
    'bed': [1.4, 1.4],
    'city': [0.2, 0.2],
    'house_size': [1, 1.0],  # Example of missing data
    'state': [7.0, 6.4],
    'status': [3.2, 3.2],
    'zip_code': [1.2, 1.2]
})

# Alternatively, using Pandas DataFrame
# input_df = pd.DataFrame({
#     'feature1': [5.1, 4.9],
#     'feature2': [3.5, 3.0],
#     'feature3': [1.4, 1.4]
# })
# Define the correct order of features
correct_order = ['zip_code', 'status', 'bed', 'bath', 'acre_lot', 'city', 'state', 'house_size']
input_data = input_data[correct_order]
# Step 3: Make predictions
try:
    predictions = mlp_model.predict(input_data)
    print("Predictions:", predictions)

    # If you need probabilities
    if hasattr(mlp_model, "predict_proba"):
        probabilities = mlp_model.predict_proba(input_data)
        print("Probability Estimates:", probabilities)

except Exception as e:
    print(f"An error occurred during prediction: {e}")