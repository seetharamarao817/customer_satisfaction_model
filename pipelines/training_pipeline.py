from zenml import pipeline
from steps.ingest_data import ingestData
from steps.data_cleaning import clean_data
from steps.model_training import train_model
from steps.model_eval import eval_model


@pipeline()
def train_pipeline(data_path :str):
    df = ingestData(data_path)
    clean_data(df)
    train_model(df)
    eval_model(df)
    print("Run command: python train")