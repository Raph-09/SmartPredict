from src.utils.common import read_yaml, create_directories
# Example: Using the parameters in model training
from sklearn.ensemble import RandomForestClassifier

# Load configuration files
config = read_yaml("config/config.yaml")
params = read_yaml("params.yaml")

# Automatically create necessary directories (excluding logs)
required_dirs = [
    "data",
    "artifacts",
    "artifacts/data_ingestion",
    "artifacts/data_transformation",
    "artifacts/model_artifact",
    "artifacts/evaluation_result"

]
create_directories(required_dirs)

# Accessing values from config
raw_data_path = config["artifacts"]["raw_data_path"]
processed_data_path = config["artifacts"]["data_ingestion"]["processed_data_path"]
X_train_path = config["artifacts"]["data_transformation"]["train_data"]["X_train"]
X_test_path = config["artifacts"]["data_transformation"]["train_data"]["X_test"]
y_train_path = config["artifacts"]["data_transformation"]["train_data"]["y_train"]
y_test_path = config["artifacts"]["data_transformation"]["train_data"]["y_test"]
model_saving_path = config["artifacts"]["model_artifact"]["model_path"]
model_metrics_path = config["artifacts"]["evaluation_result"]["metrics_path"]


model_params = params["model"]



clf = RandomForestClassifier(
    n_estimators=model_params["n_estimators"],
    max_depth=model_params["max_depth"],
    min_samples_split=model_params["min_samples_split"],
    min_samples_leaf=model_params["min_samples_leaf"],
    random_state=model_params["random_state"]
)
