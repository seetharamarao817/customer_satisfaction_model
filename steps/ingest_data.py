import logging 

import pandas as pd 
from zenml import step

class IngestData:
    def __init__(self):
        pass

    def load_data(self, data_path:str):
        logging.info(f"Data loaded from {data_path}")
        return pd.read_csv(data_path)


@step
def ingestData(data_path:str) -> pd.DataFrame:
    try:
        id = IngestData()
        df = id.load_data(data_path)
        return df
    except Exception as ex:
        logging.error(f"error while ingesting data {ex}")
        raise ex




