import numpy as np
from sklearn import preprocessing
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split
from src.exception_manager.exceptioner import CustomException
from src.logging.logging import get_logger
import pandas as pd
from src.entity.config_manager import *



logger = get_logger(__name__)

class DataTransformation:
  def __init__ (self,path):
    self.data = pd.read_csv(path)
    self.X = None
    self.y = None
    logger.info("Data Transformation started")
  
  def feature_creation (self):
    try: 
        self.data['Power'] = self.data[['Rotational speed [rpm]','Torque [Nm]']].product(axis=1)
        logger.info(f"Created a new feature called {self.data['Power']}")
        return self.data
    except Exception as e:
      logger.info(f"Error occured feature creation stage {e}")
      raise CustomException(f"Error occured feature creation stage",e)
  def irrelevant_drop (self):
    try:
      self.data = self.data.drop(['UDI','Product ID','TWF','HDF','PWF','OSF','RNF'],axis=1)
      logger.info("ropping irrelevant features such  as 'UDI','Product ID','TWF','HDF','PWF','OSF','RNF'")
      return self.data
    except Exception as e:
      logger.info(f"Error occurred while dropping irrelevant features {e}")
      raise CustomException("Error occurred while dropping irrelevant features",e)

  def outlier_handling(self, factor=1.5):
    logger.info("Handling outliers")
    try:
      numeric_cols = self.data.select_dtypes(include=[np.number]).columns
      numeric_cols = numeric_cols.drop("Machine failure")
      for col in numeric_cols:
          Q1 = self.data[col].quantile(0.25)
          Q3 = self.data[col].quantile(0.75)
          IQR = Q3 - Q1
          lower_bound = Q1 - factor * IQR
          upper_bound = Q3 + factor * IQR
          self.data = self.data[(self.data[col] >= lower_bound) & (self.data[col] <= upper_bound)]
      return self.data
    except Exception as e:
      logger.info(f"Error occured while handing outliers")
      raise CustomException("Error occured while handing outliers",e)

  def label_encode(self):
        logger.info("Using Label Encoding to convert categorical varaiables to numerical")
        try:
          le = preprocessing.LabelEncoder()
          categorical_columns = self.data.select_dtypes(include=['object']).columns.tolist()
          for col in categorical_columns:
              self.data[col] = le.fit_transform(self.data[col])
          return self.data
        except  Exception as e:
          logger.info(f"Error occured during Label encoding of categorical features {e}")
          raise CustomException ("Error occured during Label encoding of categorical features",e)


  def setting_var (self):
    logger.info("setting independent and dependent variables")
    try:
      self.X = self.data.drop('Machine failure',axis=1)
      self.y = self.data['Machine failure']
      return self.X, self.y
    except Exception as e:
      logger.info(f"Error occured while setting dependent and independent variable {e}")
      raise CustomException("Error occured while setting dependent and independent variable",e)

  def data_balancing (self):
    logger.info("Balancing the data")

    try:
      smote = SMOTE()
      self.X, self.y = smote.fit_resample(self.X, self.y)
      return self.X, self.y
    except Exception as e:
      logger.info(f"Error occured during data balancing {e}")
      raise CustomException ("Error occured during data balancing",e)

  def data_splitter (self):
    logger.info("Splitting the data into training and testing sets")
    try:
      X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, test_size=0.3, random_state=42)

      return  X_train.to_csv(X_train_path,index=False), X_test.to_csv(X_test_path,index=False), y_train.to_csv(y_train_path,index=False), y_test.to_csv(y_test_path,index=False)

    except Exception as e:
      logger.info(f"Eror occured during data splitting {e}")
      raise CustomException("Eror occured during data splitting",e)