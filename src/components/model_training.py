from sklearn.ensemble import RandomForestClassifier
import pickle
import pandas as pd
from src.exception_manager.exceptioner import CustomException
from src.logging.logging import get_logger
from src.entity.config_manager import *

logger = get_logger(__name__)


class trianer:
  def __init__ (self,X_train_path,y_train_path):
    self.X_train_path = X_train_path
    self.y_train_path = y_train_path
    self.X_train = pd.read_csv(self.X_train_path)
    self.y_train = pd.read_csv(self.y_train_path).values.ravel()
    self.rf_classifier = None

  def model_training(self):
    try:
      logger.info("Model Training Started")
      # Create a Random Forest classifier with desired parameters
      self.rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42, max_depth=None,min_samples_leaf=1,min_samples_split=2)

      # Train the classifier
      self.rf_classifier.fit(self.X_train, self.y_train)

      # File path to save the model
      logger.info("Tained Model saved")
      file_path = model_saving_path

      # Save the model to the pickle file
      with open(file_path, "wb") as file:
          pickle.dump(self.rf_classifier, file)

      return self.rf_classifier
    except Exception as e:
      logger.info(f"Error occcured during model training {e}")
      raise CustomException ("Error occcured during model training",e)
