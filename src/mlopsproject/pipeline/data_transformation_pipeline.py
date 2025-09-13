import os
from src.mlopsproject.config.configuration import ConfigurationManager
from src.mlopsproject.components.data_transformation import DataTransformation
from src.mlopsproject import logger
from pathlib import Path


STAGE_NAME = "Data Transformaation stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_transformation(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"), "r") as f:
                status = f.read().split(" ")[-1]
            if status == "True":
                config = ConfigurationManager()
                data_transformation_config = config.get_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.train_test_split()
            else:
                raise Exception("Data schema is not valid")
        except Exception as e:
            print(e)
