

## 🚀 Global Space Mission Launch Price Prediction

This project uses **Big Data Analytics with PySpark** to predict the **launch price of global space missions** using a machine learning approach. It leverages a Random Forest Regressor to handle complex, non-linear relationships and provides insights into the most significant cost-driving features.

---

### 📂 Project Structure

- `mission_launch.ipynb`: Main notebook with data processing, modeling, and evaluation.
- `best_random_forest_model/`: Directory where the trained model is saved.
- `README.md`: Project overview and documentation.
- `requirements.txt`: Python libraries used.

---

### 📊 Problem Statement

The objective is to **predict the price** of space launches using various features like:

- Organization behind the launch
- Country of origin
- Rocket status
- Mission status (Success/Failure)

This information can help governments, researchers, and private space organizations **forecast launch costs** and **optimize spending**.

---

### 🛠️ Technologies Used

- **PySpark**
- Google Colab
- Pandas & Matplotlib (for plotting)
- Machine Learning: Random Forest Regression

---

### 📈 Model Performance

| Metric | Value |
|--------|-------|
| RMSE (Root Mean Squared Error) | **3.86** |
| MAE (Mean Absolute Error)      | **0.83** |
| R² (R-Squared Score)           | **0.9972** |

> 📌 The model explains **99.72%** of the variance in the launch prices, indicating **excellent predictive performance**.

---

### 🔍 Feature Importance

The top features that influenced launch pricing:

1. `Organisation`
2. `Country`
3. `Mission_Status` (Success, Failure, Partial Failure)
4. `Rocket_Status`

A horizontal bar chart visualizes these importances in the notebook.

---

### 💾 Saving and Loading the Model

The best model from hyperparameter tuning was saved using:

```python
best_rf_model.save("/content/best_random_forest_model")
```

To load it again:

```python
from pyspark.ml.regression import RandomForestRegressionModel
loaded_model = RandomForestRegressionModel.load("/content/best_random_forest_model")
```

---

### 📌 Key Highlights

- Efficient **feature engineering** using `StringIndexer`, `OneHotEncoder`, and `VectorAssembler`.
- Model tuning using **CrossValidator**.
- Extensive **evaluation metrics** and **visualization** for feature importance.
- Fully scalable for **Big Data** use cases.

---

### 🙋‍♂️ Author

R Manisha Achary
Data Science Intern  
📧 manisha.achary13@gmail.com
🔗 https://www.linkedin.com/in/r-manisha-achary-470798204

