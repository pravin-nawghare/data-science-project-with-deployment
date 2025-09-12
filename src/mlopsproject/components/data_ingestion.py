import os
import urllib.request as request
import zipfile
from src.mlopsproject import logger
from src.mlopsproject.entity.config_entity import (DataIngestionConfig)

class DataIngestion:
    def __init__(self, config:DataIngestionConfig):
        self.config=config

    # downloading the zip file
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_url,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} download with following info: \n{headers}")
        else:
            logger.info(f"File already downloaded")
        
    def extract_zip_file(self):
        """
        zip_file_path = str
        extracts the zip file into unzip directory
        function return None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, "r") as zip_ref:
            zip_ref.extractall(unzip_path)