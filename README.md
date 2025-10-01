# Interactive Linear Regression Explorer

**Live Demo:** [https://helloabcd666.streamlit.app/](https://helloabcd666.streamlit.app/)

This web application provides an interactive environment to understand the fundamentals of simple linear regression. It's designed as an educational tool to visualize how different parameters influence a model's fit and performance.

## Features

The application is built with Streamlit and allows you to:

*   **Adjust Data Parameters in Real-Time:** Use the sidebar sliders to control the underlying data generation:
    *   **Slope (a):** Change the slope of the true linear relationship.
    *   **Noise:** Introduce random variance to the data points to simulate real-world scenarios.
    *   **Number of Points:** Increase or decrease the size of the dataset.

*   **Visualize the Regression Model:** The main chart displays:
    *   The raw, generated data points (blue).
    *   The linear regression model's fitted line (red).

*   **Analyze Model Performance:** Key metrics and formulas are provided to help evaluate the model:
    *   **Original vs. Predicted Formula:** Compare the true formula used for data generation against the formula learned by the model.
    *   **Mean Squared Error (MSE):** A measure of the average squared difference between the estimated values and the actual value.
    *   **R-squared:** A statistical measure of how close the data are to the fitted regression line.

*   **Identify and Inspect Outliers:**
    *   The **Top 5 Outliers** (points with the largest residual error) are highlighted in orange on the plot and annotated with their data ID.
    *   A table at the bottom lists these outliers, showing their actual values, predicted values, and the calculated residual.

## How to Run Locally

To run this application on your own machine, follow these steps:

1.  **Prerequisites:**
    *   Ensure you have Python 3.7+ installed.
    *   It's recommended to use a virtual environment.

2.  **Clone the Repository:**
    ```bash
    git clone https://github.com/Joxanne/AIoT.git
    cd AIoT
    ```

3.  **Install Dependencies:**
    Install all the required Python packages using the `requirements.txt` file.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Streamlit App:**
    Launch the application from your terminal.
    ```bash
    streamlit run app.py
    ```
    The application should automatically open in your web browser.
