from src.exception_manager.exceptioner import CustomException
from src.logging.logging import get_logger
from src.components.data_transformation import DataTransformation
from src.entity.config_manager import *





class DataTansPipeline:
  def __init__(self):
    pass

  def initiate_tranformation(self):
    data = DataTransformation(processed_data_path)
    data.feature_creation()
    data.irrelevant_drop()
    data.outlier_handling()
    data.label_encode()
    data.setting_var()
    data.data_balancing()
    data.data_splitter()


if __name__=="__main__":
  data_trans = DataTansPipeline()
  data_trans.initiate_tranformation()