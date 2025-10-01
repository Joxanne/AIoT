### Project: Interactive Simple Linear Regression Web App

**Objective:** Develop a Python web application that demonstrates a simple linear regression model. The application will follow the CRISP-DM framework, allow user interaction for parameter tuning, and be deployed using a web framework like Streamlit.

---

### Phase 1: Project Setup & Foundation (CRISP-DM: Business Understanding)

1.  **Business Understanding:**
    *   **Goal:** Create an educational tool to visualize how parameters like slope (`a`), noise, and data quantity affect a simple linear regression model (`y = ax + b`).
    *   **Success Criteria:** A functional web app where users can adjust parameters and see the updated regression plot and model performance instantly.

2.  **Initial Setup:**
    *   Create a project directory.
    *   Create a Python script, e.g., `app.py`.
    *   Create a `requirements.txt` file to list necessary libraries:
        ```
        streamlit
        pandas
        numpy
        scikit-learn
        matplotlib
        ```
    *   Install dependencies: `pip install -r requirements.txt`.

### Phase 2: Data Generation & Preparation (CRISP-DM: Data Understanding & Preparation)

1.  **Data Understanding:**
    *   The data will be synthetically generated. It is not from an external source.
    *   The underlying model is linear: `y = ax + b`.
    *   We will introduce random noise to simulate real-world data.

2.  **Data Preparation:**
    *   **Function `generate_data(a, b, noise, num_points)`:**
        *   Input: slope `a`, intercept `b`, noise level, and number of data points.
        *   Process:
            *   Generate `x` values (e.g., a sequence of numbers).
            *   Generate `y` values using `y = a * x + b`.
            *   Add random noise to the `y` values.
        *   Output: A pandas DataFrame with `x` and `y` columns.

### Phase 3: Modeling & Evaluation (CRISP-DM: Modeling & Evaluation)

1.  **Modeling:**
    *   **Function `train_model(data)`:**
        *   Input: The generated data (DataFrame).
        *   Process:
            *   Use `scikit-learn`'s `LinearRegression` model.
            *   Fit the model to the `x` and `y` data.
        *   Output: The trained model object.

2.  **Evaluation:**
    *   **Function `evaluate_model(model, data)`:**
        *   Input: The trained model and the original data.
        *   Process:
            *   Calculate metrics like **Mean Squared Error (MSE)** and **R-squared score**.
        *   Output: A dictionary or tuple containing the evaluation metrics.
    *   **Visualization:**
        *   Create a scatter plot of the original data points.
        *   Overlay the fitted regression line from the trained model.
        *   Display the original formula (`y = ax + b`) and the model's predicted formula.

### Phase 4: Deployment (CRISP-DM: Deployment)

1.  **Web Framework Selection:**
    *   **Streamlit** is chosen for its simplicity and speed in creating data-centric apps.

2.  **UI Implementation (`app.py`):**
    *   **Title:** Add a clear title, e.g., "Interactive Linear Regression Explorer".
    *   **Sidebar for Controls:**
        *   Use `st.sidebar.slider()` for the user to modify:
            *   Slope `a` (e.g., from -10 to 10).
            *   Noise level (e.g., from 0 to 50).
            *   Number of points (e.g., from 10 to 500).
        *   Keep the intercept `b` constant for simplicity, or add a slider for it as well.
    *   **Main Panel for Display:**
        *   **Header:** Briefly explain the purpose of the app.
        *   **Data Generation:** Call `generate_data()` with the user's chosen parameters.
        *   **Model Training:** Call `train_model()` on the generated data.
        *   **Display Plot:** Use `st.pyplot()` to show the `matplotlib` visualization (scatter plot + regression line).
        *   **Display Evaluation:**
            *   Show the original parameters vs. the model's learned parameters (slope and intercept).
            *   Display the MSE and R-squared score using `st.metric()` or `st.write()`.

### Phase 5: Finalization

1.  **Code Refinement:**
    *   Add comments and docstrings to all functions to explain the process.
    *   Ensure the code is clean and readable.
2.  **Documentation:**
    *   Create a `README.md` file explaining:
        *   The project's purpose.
        *   How to set up the environment and run the app (`streamlit run app.py`).
3.  **Deployment (Optional, for sharing):**
    *   Deploy the app to Streamlit Community Cloud by connecting it to a GitHub repository.