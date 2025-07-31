from src.exception_manager.exceptioner import CustomException
from src.logging.logging import get_logger
from src.components.model_evaluation import ModelEvaluation
from src.entity.config_manager import *






class ModelEvaluationPipeline:
  def __init__(self):
    pass
  def initialize_evalator (self):
    eval = ModelEvaluation(y_test_path,X_test_path)
    eval.evaluator()


if __name__=="__main__":
  evalpipe = ModelEvaluationPipeline()
  evalpipe.initialize_evalator()


