import os
import joblib
import pandas as pd

# Direktori model
MODEL_DIR = "model"

# Load model dan scaler dari direktori model/
def load_model():
    model = joblib.load(os.path.join(MODEL_DIR, "attrition_model.pkl"))
    scaler = joblib.load(os.path.join(MODEL_DIR, "scaler.pkl"))
    print("\n✅ Model dan scaler berhasil dimuat kembali")
    return model, scaler

# Prediksi dengan model yang telah disimpan
def predict_attrition(model, scaler, income, overtime, satisfaction):
    new_data = pd.DataFrame({
        'MonthlyIncome': [income],
        'OverTime': [overtime],
        'JobSatisfaction': [satisfaction]
    })
    
    new_data[['MonthlyIncome', 'JobSatisfaction']] = scaler.transform(
        new_data[['MonthlyIncome', 'JobSatisfaction']]
    )
    
    prediction = model.predict(new_data)[0]
    probability = model.predict_proba(new_data)[0]
    
    return prediction, probability

if __name__ == "__main__":
    # Load model
    model, scaler = load_model()

    # Contoh prediksi
    income = 5000
    overtime = 1  # Yes
    satisfaction = 3
    
    prediction, probability = predict_attrition(model, scaler, income, overtime, satisfaction)
    
    print(f"\nPrediction for new employee:")
    print(f"Attrition Risk: {'Yes' if prediction else 'No'}")
    print(f"Probability of leaving: {probability[1]:.2%}")
