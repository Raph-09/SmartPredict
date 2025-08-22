# 📘 Project Documentation: Predictive Maintenance with MLOps

## **1. Data Ingestion**

**Objective:** Collect raw data from MySQL database and store it in a structured format for downstream tasks.

* **Process:**

  * Connects to **MySQL** using `sqlalchemy` and `mysql-connector`.
  * Loads data into **Pandas DataFrame**.
  * Saves processed data into a CSV file.

* **Key Components:**

  * `DataIngestion` class in `Data_ingestion.py`.
  * Logging with `logger.py`.
  * Exception handling with `exception.py`.

* **Tools:**

  * **MySQL** (Data Source)
  * **SQLAlchemy + mysql-connector** (Database connection)
  * **Pandas** (Data handling)

---

## **2. Data Transformation**

**Objective:** Clean, preprocess, and prepare the dataset for model training.

* **Steps:**

  1. **Feature Engineering:** Create new feature `Power = Torque × Rotational speed`.
  2. **Irrelevant Feature Removal:** Drop identifiers and redundant features.
  3. **Outlier Handling:** Apply IQR method to remove outliers.
  4. **Encoding:** Label encode categorical variables.
  5. **Variable Splitting:** Define independent variables (X) and target (y).
  6. **Data Balancing:** Apply **SMOTE** for handling imbalanced dataset.
  7. **Train-Test Split:** Split into training (70%) and testing (30%).

* **Key Components:**

  * `DataTransformation` class in `Data_transformation.py`.

* **Tools:**

  * **Pandas** (Preprocessing)
  * **scikit-learn** (Encoding, splitting)
  * **imblearn (SMOTE)** (Balancing dataset)

---

## **3. Model Training**

**Objective:** Train machine learning models on processed data.

* **Process:**

  * Uses **RandomForestClassifier** with tuned parameters.
  * Trained model saved as `model.pickle`.

* **Key Components:**

  * `trainer` class in `Model_training.py`.

* **Tools:**

  * **scikit-learn (RandomForestClassifier)**
  * **pickle** (Model persistence)

---

## **4. Model Evaluation**

**Objective:** Evaluate trained model performance using standard metrics.

* **Metrics:**

  * Accuracy
  * Precision
  * Recall
  * F1-Score

* **Output:**

  * Metrics logged.
  * Saved in `metrics_report.txt`.

* **Key Components:**

  * `ModelEvaluation` class in `Model_evaluation.py`.

* **Tools:**

  * **scikit-learn.metrics**

---

## **5. Data & Model Versioning**

**Objective:** Track and manage versions of data and models.

* **Tools Used:**

  * **DVC (Data Version Control):** For dataset versioning.
  * **Git:** For code versioning.
  * **Dagshub:** Integrated for data, model, and code versioning.

---

## **6. Experiment Tracking**

**Objective:** Track experiments, parameters, and metrics.

* **Tools Used:**

  * **MLflow (Local + Dagshub integration):**

    * Logs model parameters, metrics, and artifacts.
    * Used for model registration and tracking experiments.

---

## **7. Model Deployment**

**Objective:** Deploy the trained model as a service.

* **Steps:**

  1. **Containerization:**

     * Dockerized using `Dockerfile`.
     * Exposed on port 5000.
  2. **Deployment:**

     * Docker image pushed to **Azure Container Registry**.
     * Deployed using **Azure Web App**.
  3. **CI/CD:**

     * **GitHub Actions** automates building, pushing, and deploying containers.

* **Tools:**

  * **Docker** (Containerization)
  * **Azure Container Registry** (Image hosting)
  * **Azure Web App** (Hosting web app)
  * **GitHub Actions** (CI/CD automation)

---

## **8. Monitoring**

**Objective:** Ensure deployed model is performing reliably and detect drift.

* **Process:**

  * Model predictions stored back in **MySQL database**.
  * **EvidentlyAI** used for drift detection and monitoring.

* **Tools:**

  * **MySQL** (Storage for monitoring results)
  * **EvidentlyAI** (Model monitoring & drift detection)

---

## **9. Testing & Automation**

* **Pytest:** Unit tests to verify artifacts (e.g., model existence).
* **GitHub Actions CI/CD:** Automated testing, building, and deployment.

---

# 📊 End-to-End Workflow

1. **Data Source:** MySQL → CSV.
2. **Data Transformation:** Cleaning, feature engineering, balancing.
3. **Training:** RandomForest model.
4. **Evaluation:** Accuracy, Precision, Recall, F1.
5. **Versioning & Tracking:** DVC, Git, Dagshub, MLflow.
6. **Deployment:** Docker + Azure Web App via GitHub Actions.
7. **Monitoring:** EvidentlyAI + MySQL logging.

---

✅ This setup ensures **reproducibility, automation, scalability, and monitoring** across the full ML lifecycle.


