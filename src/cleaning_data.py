import logging
from typing import Union
from abc import ABC, abstractmethod

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

class DataStrages(ABC):

    @abstractmethod
    def handle_data(self, df: pd.DataFrame) -> Union[pd.DataFrame,pd.Series]:

        pass

class Datapreprocessing(DataStrages):
    def handle_data(self, df: pd.DataFrame) -> Union[pd.DataFrame,pd.Series]:
        
        try:
            df = df.copy()
            df = df.dropna()
            df = df.reset_index(drop=True)
        
        except Exception as e:
            logging.error(e)
            raise e
        return df