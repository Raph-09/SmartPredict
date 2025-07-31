from src.exception_manager.exceptioner import CustomException
from src.logging.logging import get_logger
from src.components.model_training import trianer

from src.entity.config_manager import *



class ModelTrainerPipeline:
  def __init__(self):
    pass
  def initialize_training(self):
    train = trianer(X_train_path,y_train_path)
    train.model_training()

if __name__=="__main__":
  training = ModelTrainerPipeline()
  training.initialize_training()