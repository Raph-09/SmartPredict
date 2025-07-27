from src.exception_manager.exceptioner import CustomException
from src.logging.logging import get_logger
from src.pipeline.data_ingestion_pipeline import data_ingestion_pipeline
from src.pipeline.data_transformation_pipeline import DataTansPipeline
from src.pipeline.model_trainer_pipeline import ModelTrainerPipeline
from src.pipeline.model_evaluation_pipeline import ModelEvaluationPipeline




logger = get_logger(__name__)

STAGE_NAME = "Data Ingestion stage"
logger.info(STAGE_NAME)

ingest = data_ingestion_pipeline()
ingest.inititate_ingestion()



STAGE_NAME = "Data Transformation stage"
logger.info(STAGE_NAME)
data_trans = DataTansPipeline()
data_trans.initiate_tranformation()



STAGE_NAME = "Model Trainer stage"
logger.info(STAGE_NAME)
training = ModelTrainerPipeline()
training.initialize_training()


STAGE_NAME = "Model evaluation stage"
logger.info(STAGE_NAME)
evalpipe = ModelEvaluationPipeline()
evalpipe.initialize_evalator()





