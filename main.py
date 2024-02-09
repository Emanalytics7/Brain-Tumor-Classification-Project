from src.braintumorClassifier import logger
from src.braintumorClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.braintumorClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from src.braintumorClassifier.pipeline.stage_03_training import ModelTrainingPipeline


STAGE_NAME = 'Data Ingestion stage'
try:
    logger.info(f'>>>> stage {STAGE_NAME} started <<<<')
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f'>>>> stage {STAGE_NAME} completed <<<< \n\nx==========x')
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = 'Prepare Base Model stage'
try:
    logger.info(f'>>>> stage {STAGE_NAME} started <<<<')
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f'>>>> stage {STAGE_NAME} completed <<<< \n\nx==========x')
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = 'Training stage'
try:
    logger.info(f'>>>> stage {STAGE_NAME} started <<<<')
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f'>>>> stage {STAGE_NAME} completed <<<< \n\nx==========x')

except Exception as e:
    logger.exception(e)
    raise e