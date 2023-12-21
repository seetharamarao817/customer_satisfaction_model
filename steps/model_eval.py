import logging
from zenml import step
import pandas as pd
@step
def eval_model(data_path : pd.DataFrame) -> None:
    
    pass