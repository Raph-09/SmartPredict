import mysql.connector
from datetime import datetime

DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',          
    'password': 'akukanem_12',  
    'database': 'mlops'
}

def save_prediction(data_dict):
    """Insert features and prediction into MySQL."""
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS predictions (
                id INT AUTO_INCREMENT PRIMARY KEY,
                type_val INT,
                air_temperature_k FLOAT,
                process_temperature_k FLOAT,
                rotational_speed_rpm FLOAT,
                torque_nm FLOAT,
                tool_wear_min FLOAT,
                Power FLOAT,
                prediction_label VARCHAR(50),
                prediction_value INT,
                timestamp DATETIME
            )
        """)

        cursor.execute("""
            INSERT INTO predictions (
                type_val, air_temperature_k, process_temperature_k,
                rotational_speed_rpm, torque_nm, tool_wear_min, Power,
                prediction_label, prediction_value, timestamp
            ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """, (
            data_dict["type"],
            data_dict["air_temperature_k"],
            data_dict["process_temperature_k"],
            data_dict["rotational_speed_rpm"],
            data_dict["torque_nm"],
            data_dict["tool_wear_min"],
            data_dict["Power"],
            data_dict["prediction_label"],
            data_dict["prediction_value"],
            datetime.now()
        ))

        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print("Database Error:", e)
