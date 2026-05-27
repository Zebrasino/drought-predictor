from pydantic_settings import BaseSettings
from pathlib import Path

class Settings(BaseSettings):
    
    # The path of the data
    raw_data_path : Path = Path("data/raw/drought.csv")
    
    # The path of the model
    model_path : Path = Path("models/drought_model.joblib")
    
    # The size of the test set
    test_size : float = 0.2
    
    # The target column that we want to predict
    target_column : str = "score"
    
    # The random state for riproducibility
    random_state : int = 42
    

settings = Settings()