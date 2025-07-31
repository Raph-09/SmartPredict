from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from src.exception_manager.exceptioner import CustomException
from src.logging.logging import get_logger
import pandas as pd
import pickle
import mlflow
from src.entity.config_manager import *  
import dagshub
import os
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
# from src.entity.config_manager import *


# dagshub.init(repo_owner='akpan1653', repo_name='SmartPredict', mlflow=True)

os.environ['MLFLOW_TRACKING_URI']="https://dagshub.com/akpan1653/SmartPredict.mlflow"
os.environ['MLFLOW_TRACKING_USERNAME']="akpan1653"
os.environ["MLFLOW_TRACKING_PASSWORD"]="c9041b3ac1a05dc118ddebef3a5eaccdf097c413"

mlflow.set_experiment("PredictiveMaintenance")


logger = get_logger(__name__)

class ModelEvaluation:

  def __init__(self, y_test_path, X_test_path):
    self.y_test = pd.read_csv(y_test_path).squeeze()
    self.X_test = pd.read_csv(X_test_path)
    self.model = pickle.load(open(model_saving_path, 'rb'))
    self.model_params = model_params

  def evaluator(self):
    try:
      logger.info("Model Evaluation Started")

      pred = self.model.predict(self.X_test)

      # Calculate metrics
      accuracy = round(accuracy_score(self.y_test, pred),2) 
      precision = precision_score(self.y_test, pred) 
      recall = recall_score(self.y_test, pred) 
      f1 = f1_score(self.y_test, pred) 

      logger.info(f"Accuracy score: {accuracy}")
      logger.info(f"Precision score: {precision}")
      logger.info(f"Recall score: {recall}")
      logger.info(f"F1 score: {f1}")
      
      # Set tracking URI to DagsHub
      mlflow.set_tracking_uri("https://dagshub.com/akpan1653/SmartPredict.mlflow")
      # Log metrics to MLflow
      with mlflow.start_run():
        mlflow.log_param("n_estimators",self.model_params["n_estimators"])
        mlflow.log_param("max_depth",self.model_params["max_depth"])
        mlflow.log_param("min_samples_split",self.model_params["min_samples_split"])
        mlflow.log_param("min_samples_leaf",self.model_params["min_samples_leaf"])
        mlflow.log_param("random_state",self.model_params["random_state"])

        mlflow.log_metric("accuracy", accuracy)
        mlflow.log_metric("precision", precision)
        mlflow.log_metric("recall", recall)
        mlflow.log_metric("f1_score", f1)

        
        cr=classification_report(self.y_test,pred)
        cm=confusion_matrix(self.y_test,pred)

        mlflow.log_text(str(cm),"confusion_matrix.txt")
        mlflow.log_text(cr,"classification_report.txt")

      # Save to a text file
      metrics_text = (
        f"Accuracy:  {accuracy:.4f}\n"
        f"Precision: {precision:.4f}\n"
        f"Recall:    {recall:.4f}\n"
        f"F1 Score:  {f1:.4f}\n"
      )
      with open(model_metrics_path, "w") as f:
        f.write(metrics_text)

      return accuracy, recall, precision, f1

    except Exception as e:
      logger.info(f"Error occurred during model evaluation {e}")
      raise CustomException("Error occurred during model evaluation", e)
