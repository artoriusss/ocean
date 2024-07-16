from sklearn.metrics import mean_absolute_error, median_absolute_error, r2_score, mean_squared_error

def evaluate(y_pred, y_test):
    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    medae = median_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    print("\nResulted metrics:")
    print("-----------------------------------")
    print(f'Mean Squared Error (MSE): {mse}')
    print(f'Mean Absolute Error (MAE): {mae}')
    print(f'R-squared (R²): {r2}')
    print(f'Median Absolute Error: {medae}')
    print("-----------------------------------")
    return mse, mae, medae, r2