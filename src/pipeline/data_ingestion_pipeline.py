from src.exception_manager.exceptioner import CustomException
from src.logging.logging import get_logger
from src.components.data_ingestion import DataIngestion
from src.entity.config_manager import *



logger = get_logger(__name__)

class data_ingestion_pipeline:
  def __init__(self):
    pass

  def inititate_ingestion(self):
      try:
        data = DataIngestion()
        data.data_loader()
        data.data_saver()
      except Exception as e:
        logger.info(f"Error occured in the data ingestion pipeline stage {e}")
        raise CustomException("Error occured in the data ingestion pipeline stage",e)
      

if __name__ == "__main__":
    pipeline = data_ingestion_pipeline()
    pipeline.inititate_ingestion()
