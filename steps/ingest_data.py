import logging

import pandas as pd
from zenml import step


class IngestData:
    """
    Data ingestion class which ingests data from the source and returns a DataFrame.
    """

    def __init__(self) -> None:
        """Initialize the data ingestion class."""
        pass

    def get_data(self) -> pd.DataFrame:
        df = pd.read_csv("seetharamarao817/customer_satisfaction_model/data/olist_customers_dataset.csv")
        return df


@step
def ingest_data() -> pd.DataFrame:
    """
    Args:
        None
    Returns:
        df: pd.DataFrame
    """
    try:
        logging.info("Data Ingestion is started")
        ingest_data = IngestData()
        df = ingest_data.get_data()
        logging.info("Data Ingestion is completed")
        return df
    except Exception as e:
        logging.error(e)
        raise e
