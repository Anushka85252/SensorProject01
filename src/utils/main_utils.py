import sys
from typing import Dict, Tuple
import os
import pandas as pd
import pickle
import yaml
import boto3
from pathlib import Path


from src.constant import *
from src.exception import CustomException
from src.logger import logging


# Compute project root (two levels up from this file: .../src/utils → project root)
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent


class MainUtils:
    def __init__(self) -> None:
        pass

    def _resolve_path(self,filename: str) -> Path:

        p= Path(filename)
        if not p.is_absolute():
            p = PROJECT_ROOT / filename
        return p


    def read_yaml_file(self, filename: str) -> dict:
        try:
            path = self._resolve_path(filename)
            if not path.exists():
                raise FileNotFoundError(f"YAML file not found :{path}")
            with path.open("rb") as yaml_file:
                return yaml.safe_load(yaml_file)


        except Exception as e:
            raise CustomException(e, sys) from e


    def read_schema_config_file(self) -> dict:
        try:
            return self.read_yaml_file(os.path.join("config","schema.yaml"))
            #schema_config = self.read_yaml_file(os.path.join("config", "schema.yaml"))
            #return schema_config
        except Exception as e:
            raise CustomException(e, sys) from e


   


    @staticmethod
    def save_object(file_path: str, obj: object) -> None:
        logging.info("Entered the save_object method of MainUtils class")


        try:
            with open(file_path, "wb") as file_obj:
                pickle.dump(obj, file_obj)


            logging.info("Exited the save_object method of MainUtils class")


        except Exception as e:
            raise CustomException(e, sys) from e


   


    @staticmethod
    def load_object(file_path: str) -> object:
        logging.info("Entered the load_object method of MainUtils class")


        try:
            with open(file_path, "rb") as file_obj:
                obj = pickle.load(file_obj)


            logging.info("Exited the load_object method of MainUtils class")


            return obj


        except Exception as e:
            raise CustomException(e, sys) from e
   
    @staticmethod    
    def load_object(file_path):
        try:
            with open(file_path,'rb') as file_obj:
                return pickle.load(file_obj)
        except Exception as e:
            logging.info('Exception Occured in load_object function utils')
            raise CustomException(e,sys) from e
   