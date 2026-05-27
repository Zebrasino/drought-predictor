from src.core.config import settings
from src.data.loader import load_and_split
from sklearn.ensemble import RandomForestClassifier
from joblib import dump

def train() -> None:
    
    # Create the test and train sets
    X_train, X_test, y_train, y_test = load_and_split()
    
    # Create the model
    model = RandomForestClassifier(n_estimators=100,max_features="sqrt",n_jobs=-1, random_state=settings.random_state)
    
    # Fit the model
    model.fit(X_train,y_train)
    
    # Compute the accuracy of the model
    accuracy = model.score(X_test,y_test)
    
    # Print the accuracy of the model
    print(f"Model accuracy: {accuracy:.4f}")
    
    # Create the directory if it dosen't exist
    settings.model_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Save the model
    dump(model, settings.model_path,compress=3)
    
    # Print the path of the saved model
    print(f"Model saved at: {settings.model_path}")
    
    

if __name__ == "__main__":
    train()