from src.exception_manager.exceptioner import CustomException
from src.logging.logging import get_logger
from src.components.model_training import trianer





class ModelTrainerPipeline:
  def __init__(self):
    pass
  def initialize_training(self):
    train = trianer("X_train","y_train")
    train.model_training()
