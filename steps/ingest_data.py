import logging 

import pandas as pd 
from zenml import step

class IngestData:
    def __init__(self,data_path:str) -> pd.DataFrame:
        self.data_path  = data_path

    def load_data(self):
        logging.info(f"Data loaded from {self.data_path}")
        return pd.read_csv(self.data_path)


@step
def ingestData(data_path:str) -> pd.DataFrame:


    try:
        id = IngestData()
        df = id.load_data()
        return df
    except Exception as ex:
        logging.error(f"error while ingesting data {ex}")
        raise ex




