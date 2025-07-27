from src.exception_manager.exceptioner import CustomException
from src.logging.logging import get_logger
from src.components.model_evaluation import ModelEvaluation






class ModelEvaluationPipeline:
  def __init__(self):
    pass
  def initialize_evalator (self):
    eval = ModelEvaluation("y_test","X_test")
    eval.evaluator()