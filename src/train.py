import os
import joblib
import argparse
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from .preprocessing import preprocess_data
from .feature_engineering import feature_engineering
from .evaluation import evaluate

from utils.paths import DATASET_PATH

def main(max_depth):
    print(f"Reading & Preprocessing data...")
    file_path = DATASET_PATH
    df = preprocess_data(file_path)

    X, y = feature_engineering(df)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = DecisionTreeRegressor(max_depth=max_depth)
    print("Training model...")
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    print("Evaluating model...")
    evaluate(y_pred, y_test)

    os.makedirs('models', exist_ok=True)
    model_path = 'models/decision_tree_model.pkl'
    joblib.dump(model, model_path)
    print(f"\nTraining finished. Model saved to '{model_path}'")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train a decision tree model.")
    parser.add_argument('--max_depth', type=int, default=3, help="The maximum depth of the decision tree.")
    args = parser.parse_args()
    main(args.max_depth)