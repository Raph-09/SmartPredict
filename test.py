import pandas as pd
import mysql.connector
from mysql.connector import errorcode

# --- Configuration ---
CSV_PATH = "data/ai4i2020.csv"  
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',          
    'password': 'akukanem_12',  
    'database': 'mlops'
}

TABLE_NAME = 'machine_data_1'
CHUNK_SIZE = 10000  # You can adjust this

# --- SQL to Create Table ---
TABLE_SCHEMA = f"""
CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
    id INT PRIMARY KEY,
    product_id VARCHAR(20),
    type CHAR(1),
    air_temperature_k FLOAT,
    process_temperature_k FLOAT,
    rotational_speed_rpm INT,
    torque_nm FLOAT,
    tool_wear_min INT,
    machine_failure TINYINT(1),
    twf TINYINT(1),
    hdf TINYINT(1),
    pwf TINYINT(1),
    osf TINYINT(1),
    rnf TINYINT(1)
);
"""

try:
    # Connect to MySQL
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()

    # Create the table
    cursor.execute(TABLE_SCHEMA)
    conn.commit()

    # Read CSV in chunks
    for chunk in pd.read_csv(CSV_PATH, chunksize=CHUNK_SIZE):
        chunk.columns = [
            'id', 'product_id', 'type', 'air_temperature_k', 'process_temperature_k',
            'rotational_speed_rpm', 'torque_nm', 'tool_wear_min',
            'machine_failure', 'twf', 'hdf', 'pwf', 'osf', 'rnf'
        ]

        data = [tuple(row) for row in chunk.to_numpy()]
        insert_query = f"""
            INSERT INTO {TABLE_NAME} (
                id, product_id, type, air_temperature_k, process_temperature_k,
                rotational_speed_rpm, torque_nm, tool_wear_min,
                machine_failure, twf, hdf, pwf, osf, rnf
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE id=id;
        """
        cursor.executemany(insert_query, data)
        conn.commit()
        print(f"✅ Inserted {len(data)} rows...")

    print("✅ All rows inserted successfully!")

except mysql.connector.Error as err:
    print(f"❌ Database error: {err}")
except Exception as ex:
    print(f"❌ General error: {ex}")
finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("🔒 Connection closed.")
