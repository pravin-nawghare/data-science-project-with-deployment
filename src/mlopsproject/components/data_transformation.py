import os
import pandas as pd
from sklearn.model_selection import train_test_split
from src.mlopsproject import logger
from src.mlopsproject.config.configuration import DataTransformationConfig

class DataTransformation:
    def __init__(self, config=DataTransformationConfig):
        self.config = config
    
    def train_test_split(self):
        data = pd.read_csv(self.config.data_path)

        #Split the data into train and test set
        train, test = train_test_split(data, test_size=0.2)
        
        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

        logger.info("Splitted data into train and test set")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)