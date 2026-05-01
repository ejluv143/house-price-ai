import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error

df = pd.read_csv("house_data_ph.csv")

X = df[[
    "size_sqm",
    "bedrooms",
    "location_score",
    "finish_level",
    "cost_per_sqm"
]]

y = df["estimated_price"]

categorical_features = ["finish_level"]
numeric_features = [
    "size_sqm",
    "bedrooms",
    "location_score",
    "cost_per_sqm"
]

preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),
        ("num", "passthrough", numeric_features),
    ]
)

model = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("model", LinearRegression())
    ]
)

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

r2 = r2_score(y_test, predictions)
mae = mean_absolute_error(y_test, predictions)

print("Model trained successfully!")
print("R2 Score:", round(r2, 4))
print("Mean Absolute Error:", round(mae, 2))

joblib.dump(model, "house_price_model.pkl")

print("Model saved as house_price_model.pkl")