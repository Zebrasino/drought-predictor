import pandas as pd
from src.core.config import settings
from sklearn.model_selection import train_test_split

def load_and_split() -> tuple:
    
    # Load the data 
    df = pd.DataFrame(pd.read_csv(settings.raw_data_path))
    
    # Drop the NaN values
    df = df.dropna()
    
    # Round the target column to the nearest integer and convert it to int
    df[settings.target_column] = df[settings.target_column].round().astype(int)
        
    # Split the features in a matrix X
    X = df.drop(columns=[settings.target_column])
    
    # Split the target in a vector y
    y = df[settings.target_column]
    
    # Remove categorical features
    X = X.select_dtypes(include=["number"])
    
    # Return the train and test sets
    return train_test_split(X, y, test_size=settings.test_size, random_state=settings.random_state)