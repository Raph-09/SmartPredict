from flask import Flask, render_template, request
import pandas as pd
import pickle
import os

app = Flask(__name__)

# Load trained model
MODEL_PATH = os.path.join("artifacts", "model_artifact", "model.pkl")
model = pickle.load(open(MODEL_PATH, "rb"))

# Feature order from training
EXPECTED_COLUMNS = [
    "Type",
    "Air temperature [K]",
    "Process temperature [K]",
    "Rotational speed [rpm]",
    "Torque [Nm]",
    "Tool wear [min]",
    "Power"
]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            # Collect input values
            form_data = {
                "Type": int(request.form["type"]),
                "Air temperature [K]": float(request.form["air_temp"]),
                "Process temperature [K]": float(request.form["process_temp"]),
                "Rotational speed [rpm]": float(request.form["rpm"]),
                "Torque [Nm]": float(request.form["torque"]),
                "Tool wear [min]": float(request.form["tool_wear"])
            }

            # Compute engineered feature
            form_data["Power"] = form_data["Torque [Nm]"] * form_data["Rotational speed [rpm]"]

            # Create DataFrame in correct order
            df = pd.DataFrame([form_data])[EXPECTED_COLUMNS]

            # Predict
            prediction = model.predict(df)[0]
            result = "⚠️ Machine Failure" if prediction == 1 else "✅ No Failure"

            return render_template("index.html", result=result)

        except Exception as e:
            return render_template("index.html", result=f"Error: {e}")

    return render_template("index.html", result=None)

if __name__ == "__main__":
    app.run(debug=True)
