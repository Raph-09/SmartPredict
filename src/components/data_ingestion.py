from src.exception_manager.exceptioner import CustomException
from src.logging.logging import get_logger
import pandas as pd
import mysql.connector
from sqlalchemy import create_engine
from src.entity.config_manager import *

logger = get_logger(__name__)

class DataIngestion:
    def __init__(self):
        self.data = None
        logger.info("Data Ingestion Started")

    def data_loader(self):
        try:
            logger.info("Connecting to MySQL and loading data...")

            # Build connection string
            db_url = f"mysql+mysqlconnector://{mysql_user}:{mysql_password}@{mysql_host}/{mysql_database}"

            # Create SQLAlchemy engine
            engine = create_engine(db_url)

            # Read data from the MySQL table
            query = f"SELECT * FROM {mysql_table}"
            self.data = pd.read_sql(query, engine)

            logger.info("✅ Data loaded successfully from MySQL")
            return self.data

        except Exception as e:
            logger.error(f"❌ Error during data loading: {e}")
            raise CustomException("Error occurred during data loading", e)

    def data_saver(self):
        try:
            logger.info(f"Saving data to {processed_data_path} ...")
            self.data.to_csv(processed_data_path, index=False)
            logger.info("✅ Data saved successfully")
            return processed_data_path

        except Exception as e:
            logger.error(f"❌ Error during data saving: {e}")
            raise CustomException("Error occurred during data saving", e)
