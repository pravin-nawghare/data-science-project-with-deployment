from src.mlopsproject.config.configuration import ConfigurationManager
from src.mlopsproject.components.model_trainer import ModelTrainer
from src.mlopsproject import logger

STAGE_NAME = " Model Trainer stage"

class ModelTrainingTrainingPipeline:
    def __init__(self):
        pass

    def initiate_model_trainer(self):
        try:
            config = ConfigurationManager()
            model_trainer_config = config.get_model_trainer_config()
            model_trainer = ModelTrainer(config=model_trainer_config)
            model_trainer.train()
        except Exception as e:
            raise e