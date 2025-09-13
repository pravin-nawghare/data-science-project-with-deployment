from src.mlopsproject import logger
from src.mlopsproject.components.data_validation import DataValidation
from src.mlopsproject.config.configuration import ConfigurationManager

STAGE_NAME = "Data Validation stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_validation(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_data()

if __name__ == '__main__':
    try:
        logger.info(f"stage {STAGE_NAME} started")
        obj = DataValidationTrainingPipeline()
        obj.initiate_data_validation()
        logger.info(f"stage {STAGE_NAME} completed successfully")
    except Exception as e:
        logger.exception(e)
        raise e