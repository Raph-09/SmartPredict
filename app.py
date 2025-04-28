from flask import Flask, request, render_template
import pickle
import numpy as np
import lime
import lime.lime_tabular
import pandas as pd

# Initialize the Flask application
maintenance_app = Flask(__name__)

# Define input features and class labels
input_columns = ['machine_type', 'air_temperature', 'process_temperature', 'rpm', 'torque_force', 'wear_time', 'energy_usage']
target_labels = ['No Maintenance', 'Needs Maintenance']

@maintenance_app.route('/')
def display_home():
    return render_template('index.html')

@maintenance_app.route('/predict', methods=['POST'])
def generate_prediction():
    machine_category = request.form['type']
    air_temperature = float(request.form['air_temp'])
    process_temperature = float(request.form['process_temp'])
    rpm = float(request.form['rotational_speed'])
    torque_force = float(request.form['torque'])
    wear_time = float(request.form['tool_wear'])
    energy_usage = float(request.form['power'])

    # Encode categorical type
    if machine_category == 'L':
        machine_category = 0
    elif machine_category == 'M':
        machine_category = 1
    elif machine_category == 'H':
        machine_category = 2

    # Assemble feature vector
    input_vector = np.array([machine_category, air_temperature, process_temperature, rpm, torque_force, wear_time, energy_usage]).reshape(1, -1)

    # Load serialized model and training dataset for LIME
    trained_model = pickle.load(open('model.pickle', 'rb'))
    training_data = pd.read_csv("X_train.csv")

    # Generate prediction
    maintenance_status = trained_model.predict(input_vector)
    prediction_result = 'Equipment Needs Maintenance' if maintenance_status[0] == 1 else 'Equipment Does Not Need Maintenance'

    # Initialize LIME explainer
    lime_explainer = lime.lime_tabular.LimeTabularExplainer(
        training_data=np.array(training_data),
        feature_names=training_data.columns.tolist(),
        class_names=target_labels,
        mode='classification'
    )

    # Create LIME explanation
    instance_explanation = lime_explainer.explain_instance(
        data_row=input_vector[0],
        predict_fn=trained_model.predict_proba
    )

    # Generate HTML explanation output
    explanation_html_output = instance_explanation.as_html()

    return render_template('result.html', prediction=prediction_result, explanation_html=explanation_html_output)

if __name__ == '__main__':
    maintenance_app.run(debug=True)
