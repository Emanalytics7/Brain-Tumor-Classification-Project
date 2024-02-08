import os
import urllib.request as request
import zipfile
from braintumorClassifier import logger
from braintumorClassifier.utils.common import get_size
from braintumorClassifier.entity.config_entity import DataIngestionConfig
from pathlib import Path

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config


    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, header = request.urlretrieve(
                url = self.config.source_url, 
                filename = self.config.local_data_file
            )
            logger.info(f'Downloaded {filename} with following headers: \n{header}')
        else:
            logger.info(f'File already exists of size : {get_size(Path(self.config.local_data_file))}')

    def extract_zip_file(self):
        """
        Unzips the downloaded file
        """

        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
        logger.info(f'File extracted to: {unzip_path}')
