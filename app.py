import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def generate_data(a, b, noise, num_points):
    """
    Generates synthetic data for a simple linear regression problem.

    Args:
        a (float): The slope of the line.
        b (float): The intercept of the line.
        noise (float): The amount of random noise to add to the data.
        num_points (int): The number of data points to generate.

    Returns:
        pd.DataFrame: A DataFrame with 'x' and 'y' columns.
    """
    x = np.linspace(0, 10, num_points)
    y = a * x + b + np.random.normal(0, noise, num_points)
    return pd.DataFrame({'x': x, 'y': y})

def train_model(data):
    """
    Trains a linear regression model.

    Args:
        data (pd.DataFrame): The training data.

    Returns:
        LinearRegression: The trained model.
    """
    model = LinearRegression()
    model.fit(data[['x']], data['y'])
    return model

def evaluate_model(model, data):
    """
    Evaluates the trained model.

    Args:
        model (LinearRegression): The trained model.
        data (pd.DataFrame): The data used for evaluation.

    Returns:
        tuple: A tuple containing the Mean Squared Error and the R-squared score.
    """
    y_pred = model.predict(data[['x']])
    mse = np.mean((data['y'] - y_pred) ** 2)
    r2 = model.score(data[['x']], data['y'])
    return mse, r2

st.title("Interactive Linear Regression Explorer")

st.sidebar.header("Model Parameters")
a = st.sidebar.slider("Slope (a)", -10.0, 10.0, 2.5, 0.1)
noise = st.sidebar.slider("Noise", 0.0, 50.0, 10.0, 1.0)
num_points = st.sidebar.slider("Number of Points", 10, 500, 100, 10)
b = 5 # Constant intercept for simplicity

data = generate_data(a, b, noise, num_points)
model = train_model(data)
mse, r2 = evaluate_model(model, data)

# Calculate residuals and identify outliers
y_pred = model.predict(data[['x']])
data['predicted_y'] = y_pred
data['residual'] = data['y'] - data['predicted_y']
data['abs_residual'] = np.abs(data['residual'])
outliers = data.nlargest(5, 'abs_residual')


st.header("Regression Analysis")
st.write(f"Original Formula: `y = {a}x + {b}`")
st.write(f"Predicted Formula: `y = {model.coef_[0]:.2f}x + {model.intercept_:.2f}`")

col1, col2 = st.columns(2)
col1.metric("Mean Squared Error", f"{mse:.2f}")
col2.metric("R-squared", f"{r2:.2f}")

# Plotting
fig, ax = plt.subplots()
# Plot all data points
ax.scatter(data['x'], data['y'], label='Original Data', alpha=0.7)
# Plot the regression line
ax.plot(data['x'], y_pred, color='red', label='Fitted Line')
# Highlight the outliers
ax.scatter(outliers['x'], outliers['y'], color='orange', s=50, label='Top 5 Outliers', zorder=5)

# Add labels for the outliers
for i, row in outliers.iterrows():
    ax.text(row['x'], row['y'], f' {i}', fontsize=9)
    
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()
st.pyplot(fig)

# Display outliers table at the bottom
st.header("Top 5 Outliers")
st.dataframe(outliers[['x', 'y', 'predicted_y', 'residual']].round(2))
