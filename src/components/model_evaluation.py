from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from src.exception_manager.exceptioner import CustomException
from src.logging.logging import get_logger
import pandas as pd
import pickle







logger = get_logger(__name__)

class ModelEvaluation:

  def __init__ (self,y_test_path, X_test_path):
    self.y_test = pd.read_csv(y_test_path)
    self.X_test = pd.read_csv(X_test_path)
    self.model = pickle.load(open('model.pickle', 'rb'))


  def evaluator(self):
    try:
      logger.info("Model Evaluation Started")
      pred = self.model.predict(self.X_test)
      # Calculating accuracy
      accuracy = accuracy_score (self.y_test, pred)*100
      logger.info(f"Accuracy score: {accuracy}")

      # Calculating recall
      recall = recall_score(self.y_test, pred)*100
      logger.info(f"Recall score: {recall}")

      # Calculating precision
      precision = precision_score(self.y_test, pred)*100
      logger.info(f"Precision score: {precision}")


      # Calculating F1 score
      f1 = f1_score(self.y_test, pred)*100
      logger.info(f"f1 score: {f1}")
    



      metrics_text = (
      f"Accuracy:  {accuracy:.4f}\n"
      f"Precision: {precision:.4f}\n"
      f"Recall:    {recall:.4f}\n"
      f"F1 Score:  {f1:.4f}\n"
      )


      # Save to a text file
      with open("metrics_report.txt", "w") as f:
        f.write(metrics_text)
      return accuracy, recall, precision, f1

    except Exception as e:
      logger.info(f"Error occured during model evaluation {e}")
      raise CustomException("Error occured during model evaluation",e)