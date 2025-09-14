from src.mlopsproject import logger
from src.mlopsproject.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.mlopsproject.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from src.mlopsproject.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline
from src.mlopsproject.pipeline.model_trainer_pipeline import ModelTrainingTrainingPipeline

STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f"stage {STAGE_NAME} started")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.initiate_data_ingestion()
    logger.info(f"stage {STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation stage"
try:
    logger.info(f"stage {STAGE_NAME} started")
    data_validation = DataValidationTrainingPipeline()
    data_validation.initiate_data_validation()
    logger.info(f"stage {STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation stage"
try:
    logger.info(f"stage {STAGE_NAME} started")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.initiate_data_transformation()
    logger.info(f"stage {STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Trainer stage"
try:
    logger.info(f"stage {STAGE_NAME} started")
    model_trainer = ModelTrainingTrainingPipeline()
    model_trainer.initiate_model_trainer()
    logger.info(f"stage {STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e