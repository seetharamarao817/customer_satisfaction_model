from pipelines.training_pipeline import train_pipeline

if __name__ =="__main__":
    train_pipeline(data_path="/workspaces/customer_satisfaction_model/data/olist_customers_dataset.csv")