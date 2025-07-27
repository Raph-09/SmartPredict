from src.exception_manager.exceptioner import CustomException
from src.logging.logging import get_logger
import pandas as pd



logger = get_logger(__name__)

class DataIngestion:
  def __init__(self,filepath):
    self.filepath = filepath
    self.data = None
    logger.info("Data Ingestion Startd")
  def data_loader (self):
    try:
      logger.info("The data is loading...")
      self.data = pd.read_csv(self.filepath)
      return self.data
      
    except Exception as e:
      logger.info(f"Error occur in the data loading stage{e}")
      raise CustomException("Error occur during data loading",e)
  def data_saver (self):
    try:
      logger.info("The data is saving ...")
      return self.data.to_csv("pred_data",index=False)
       
    except Exception as e:
      logger.info(f"Error occur in the data saving stage{e}")
      raise CustomException("Error occur during data saving",e)



